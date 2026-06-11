Web VPython 3.2
#define size of viewing box
x_min = -80
x_max = 80
fps = 100
t = 0
dt = 1/fps
g = 9.81
Fg = vector (0, -g, 0)
#making buttons for path type
path_type = "curves"#"ramp""curves" #loop
mass= 10
path_curve = None
#marble_r=4
marble_r=pow(mass, 1/3)
k = 0.1

#assume marble is slolid spehre -> i=2/5 mr^2

def friction(myevt):
    global k
    k =myevt.value
    
myslider = slider( bind=friction, min=0, max=1, length =200 )

def path (x):
    if path_type == "ramp": 
        if x_min<x < 0: return 10
        if 0 <= x <= 30: return 10 - (0.5 * x)
        return -50
    elif path_type == "curves":
        if  x_min<= x <= x_max: 
            return 4 * sin (x/10)
        else: return -50
    
    #elif path_type == "loop":
    #    if (-70 <= x <=70): 
    #        return ((225 - (x-5)**2)**0.5)+1.7
        #if (-70 <= x <=70 && marble.pos.y <= 0):
        #    return -((225 - (x-5)**2)**0.5)+1.7
        #elif (1.7 < marble.pos.y): 
        #    if (4 <= x <= 6): 
        #        return -1 * ((1 - (x-5)**2)**0.5)+1.7
        #elif 0 <= x <= 5: 
        #    return 0.5 * exp(x+5)
        #elif 5 <= x <= 10: 
        #    return 0.5 * exp(-x + 5)
    #    else:
    #        return -50
    elif path_type == "loop":
        if  x_min<=x<0:
            return 0.03*(x+20)**2-40
        #elif 0<=x<=80:
        #    return -29
        
        '''
        if (0.9 <= marble.pos.y <= 1.7): 
            if (4 <= x <= 4.4 or 5.6 <= x <= 6): 
                return ((1 - (x-5)**2)**0.5)+1.7
            elif (1.7 < marble.pos.y): 
                if (4 <= x <= 6): 
                    return -1 * ((1 - (x-5)**2)**0.5)+1.7
            elif 0 <= x <= 5: 
                return 0.5 * exp(x+5)
            elif 5 <= x <= 10: 
                return 0.5 * exp(-x + 5)
            else:
                return -50
                '''
    return -50

def slope (x): 
    dx = 0.01
    return (path (x + dx) - path (x-dx))/(2*dx)
    
def curvature(x): #radius of curvature
    dx=0.01
    slope1 = slope(x-dx)
    slope2 = slope(x+dx)
    deriv = (slope2-slope1)/(2*dx)
    return (deriv/(1+slope(x)**2)**1.5)
    

#def setup ():
spawn_x = x_min + marble_r
m = slope(spawn_x)
n_mag = sqrt(1 + m**2)
spawn_n = vector(-m / n_mag, 1 / n_mag, 0)
marble_location = vector (spawn_x, path(spawn_x), 0) + (spawn_n * marble_r)
marble = sphere (pos = marble_location, radius = marble_r, texture = textures.earth)
marble.v = vector (20,0,0)

running = False
v_arrow = arrow (pos = marble.pos, axis = marble.v, color = color.yellow, shaftwidth = 0.3)
#v_temp = vector(20,0,0)


def launch(): 
    global running
    running = True
    v_arrow.visible = False

button (text = "LAUNCH", bind = launch)


def clicked(myevt):
    global running
    if running:
        return
    
    click_pos = myevt.pos
    speed = click_pos-marble.pos
    v_arrow.pos = marble.pos
    v_arrow.axis = speed
    v_arrow.visible = True
    marble.v = speed
    
scene.bind('click', clicked)

path_pts = []
step = 0.5
for xcoord in arange(x_min, x_max+step, step):
    path_pts.append(vector(xcoord, path(xcoord), 0))
path_curve = curve(pos=path_pts, color=color.cyan, radius=0.2)

def set_curves():
    reset("curves")
def set_loop():
    reset("loop")
def set_ramp():
    reset("ramp")
    
button(text = "curve", bind=set_curves)
button(text = "loop", bind=set_loop)
button(text = "ramp", bind=set_ramp)


def reset(path_new):
    global path_type, t, running, marble_r
    running = False
    omega = 0
    path_type = path_new
    path_curve.clear()
    for xcoord in arange(x_min, x_max+step, step):
        path_curve.append(vector(xcoord, path(xcoord), 0))
    t=0
    spawn_x = x_min + marble_r
    m = slope(spawn_x)
    n_mag = sqrt(1 + m**2)
    spawn_n = vector(-m / n_mag, 1 / n_mag, 0)
    marble.v = vector (20,0,0)
    marble.pos = vector (spawn_x, path(spawn_x), 0) + (spawn_n * marble_r)

def self_reset():
    global t, running, marble_r
    running = False
    omega = 0
    path_curve.clear()
    for xcoord in arange(x_min, x_max+step, step):
        path_curve.append(vector(xcoord, path(xcoord), 0))
    t=0
    spawn_x = x_min + marble_r
    m = slope(spawn_x)
    n_mag = sqrt(1 + m**2)
    spawn_n = vector(-m / n_mag, 1 / n_mag, 0)
    marble.v = vector (20,0,0)
    marble.pos = vector (spawn_x, path(spawn_x), 0) + (spawn_n * marble_r)

button (text = "RESET", bind = self_reset)


omega = 0
while True: 
    rate (fps) # run 100 frames per sec
    if running: 
        if(marble.pos.y <= -49):
            #print("help")
            marble.v = vector(0,0,0)
            omega = 0
        F_net = vector(0,-g*mass,0)
        #marble.pos.y = v_i*t + 0.5 * -9.81 * t** 2
        if marble.pos.y <= (path (marble.pos.x)+marble_r): 
            #path normal vector
            m= slope(marble.pos.x)
            n_mag= sqrt(1+m**2)
            normal= vector(-m/ n_mag, 1/ n_mag, 0)
            tangent = vector(1/n_mag, m/n_mag, 0)
            v_t= dot(marble.v, tangent)
            v_n = dot(marble.v, normal)
            
            #omega = v_t/marble_r
            v_slip = v_t-(omega*marble_r)
            if v_n < 0:
                marble.pos.y = path(marble.pos.x)+marble_r
                marble.v -= normal*v_n
            
            bendy = curvature(marble.pos.x)
            if bendy == 0:
                F_c = 0
            else:
                curvature_r = 1/(abs(bendy))
                F_c = (mass *v_t **2)/(curvature_r)
            
            F_n_mag= -dot(F_net, normal)+ F_c
            
            F_n = normal*F_n_mag
            
            if F_n_mag>0:
                
                if(abs(v_slip) > 0.01):
                    if(v_slip > 0):
                        
                        F_f = -tangent*k*F_n_mag#-tangent*k*(-dot(F_net, normal)) #friction AUDREY AUDREY HELP!
                    else:
                        F_f =tangent*k*F_n_mag
                else:
                    F_f = vector(0,0,0)
            else:
                F_f = vector(0,0,0)
                
            F_f_mag= dot(F_f, tangent)
            torque= -F_f_mag * marble_r
            I =(2/5)* mass* (marble_r**2)
            alpha= torque / I
            omega+= alpha * dt
                
            F_net = F_net + F_n + F_f            
            
        a = F_net/(mass *7/5) #factor in rotational intertia? 7/5
        marble.v += a*dt
        marble.pos += marble.v *dt
            
            
        t += dt
        marble.rotate (angle = -omega * dt, axis = vector (0, 0, 1)) #angle = radiuns turned per frame
        #in this case angle = radians turned per 1/100 second
        #with angular vel = 0.05 * 100 = 5 rad/s

