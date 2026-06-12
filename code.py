Web VPython 3.2
#define size of viewing box
x_min = -80
x_max = 80
fps = 30
t = 0
dt = 1/fps
g = 9.81 #14.81
#making buttons for path type
path_type = "curves"#"ramp""curves" #loop
mass= 10
path_curve = None
marble_r=pow(mass, 1/3)
k = 0.0
k_static = k*1.3
elasticity = 0.6

#assume marble is slolid spehre -> i=2/5 mr^2

def friction(myevt):
    global k, k_static
    k =myevt.value
    k_static = k*1.3
    
scene.append_to_caption("\t<b>Coefficient of Friction</b>\n")
scene.append_to_caption ("\n\t")
wtext(text="0")
myslider = slider( bind=friction, min=0, max=1, length =200)
wtext (text="1")
scene.append_to_caption("\n\n")

def change_elasticity(myevt):
    global elasticity
    elasticity = myevt.value

scene.append_to_caption("\t<b>Elasticity</b>\n")
scene.append_to_caption ("\n\t")
wtext(text="0")
bounce_slider = slider( bind=change_elasticity, min=0, max=1, length =200)
wtext (text="1")
scene.append_to_caption("\n\n")

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

button (text = "LAUNCH", bind = launch, color = color.green)


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
    
energy_graph = graph (title = "Energy Graph", xtitle = "time (sec)", ytitle = "energy (J)", width = 450, height = 250, align = "left")
potential_curve = gcurve (graph = energy_graph, color = color.blue, label = "potential energy")
kinetic_curve = gcurve (graph = energy_graph, color = color.red, label = "kinetic energy")

velocity_graph = graph(title="Velocity Graph", xtitle="time (sec)", ytitle="velocity (m/s)", width=450, height=250, align = "left")
velocity_curve = gcurve(graph=velocity_graph, color=color.green, label="magnitude")

force_graph = graph(title="Force Graph", xtitle="time (sec)", ytitle="normal force (N)", width=450, height=250, align = "left")
normal_curve = gcurve(graph=force_graph, color=color.orange, label="normal force")

def reset(path_new):
    global path_type, t, running, marble_r, omega
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
    potential_curve.data = []
    kinetic_curve.data = []
    velocity_curve.data = []
    normal_curve.data = []

def self_reset():
    global t, running, marble_r, omega
    omega = 0
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
    potential_curve.data = []
    kinetic_curve.data = []
    velocity_curve.data = []
    normal_curve.data = []

button (text = "RESET", bind = self_reset,color = color.red)
button(text = "curve", bind=set_curves)
button(text = "loop", bind=set_loop)
button(text = "ramp", bind=set_ramp)

omega = 0
F_n_mag = 0
while True: 
    rate (fps) # run 100 frames per sec
    if running: 
        if(marble.pos.y <= -(50-marble_r)):#hard stop
            marble.v = vector(0,0,0)
            omega = 0
            
        F_net = vector(0,-g*mass,0) #gravity
        
        if marble.pos.y <= (path (marble.pos.x)+marble_r): #on path
            #path normal vector
            m= slope(marble.pos.x)
            n_mag= sqrt(1+m**2)
            normal= vector(-m/ n_mag, 1/ n_mag, 0)
            tangent = vector(1/n_mag, m/n_mag, 0)
            v_t= dot(marble.v, tangent) #along path/tangent
            v_n = dot(marble.v, normal)#normal
            
            ##ALLERRTTTT 
            if v_n < 0:
                marble.pos = vector(marble.pos.x,path(marble.pos.x)+marble_r, 0)
                marble.v -= normal*v_n * (1 + elasticity) #ratio between velocity
            
                marble.pos += normal * (path(marble.pos.x) + marble_r - marble.pos.y) * (1 / normal.y)
                marble.pos.y = path(marble.pos.x) + marble_r
                marble.v -= normal * v_n
                v_t = dot(marble.v, tangent)
                
                
            bendy = curvature(marble.pos.x)
            F_c = mass * v_t**2 * bendy #centripetal force sorta
            
            F_n_mag = -dot(F_net, normal) + F_c #total magnitude
            
            if F_n_mag>0: #ifthere is normal force
                F_n = normal * F_n_mag #check
                v_diff=v_t-(omega*marble_r) #difference? between translationan and rotational surface speed
                #v_diff = 0 roll without slip
                
                if(abs(v_diff) > 0.01):#can change num? if there is a significant difference 
                    if(v_diff > 0): #slipping kinetic fric
                        F_f = -tangent*k*F_n_mag
                    else: #rolling
                        F_f =tangent*k*F_n_mag
                        
                    F_f_mag= dot(F_f, tangent)
                    torque= -F_f_mag * marble_r
                    I =(2/5)* mass* (marble_r**2)
                    alpha= torque / I
                    omega+= alpha * dt
                    F_net = F_net + F_n + F_f
                    a = F_net / mass
                    
                else: #vdiff = 0 roll no slip/ static
                    a_t = dot(F_net,tangent)/mass
                    static_max = (-2/7)*mass*a_t #force to overcome static
                    
                    if (abs(static_max) <=k_static*F_n_mag): #less than
                        F_f = tangent*static_max #they see me rollinnn
                        omega=v_t/marble_r
                        F_net = F_net + F_n + F_f
                        a = F_net / (mass * (7.0 / 5.0)) #factor in rotational inertia 7/5
                        
                    else: #becomes kinetic
                        if v_diff>0:
                            F_f = -tangent* k *F_n_mag
                        else:
                            F_f = tangent*k * F_n_mag
                        F_f_mag= dot(F_f, tangent)
                        torque= -F_f_mag * marble_r
                        I =(2/5)* mass* (marble_r**2)
                        alpha= torque /I
                        omega+= alpha * dt
                        F_net = F_net + F_n + F_f
                        a = F_net / mass
                        
            else: #left the surface
                F_n_mag = 0
                F_n = vector(0, 0, 0)
                F_f = vector(0, 0, 0)
                a = F_net / mass
                
        else: #not on surface
            F_n_mag = 0
            a = F_net / mass
        
        
        marble.v += a*dt
        marble.pos += marble.v *dt
            
            
        t += dt
        marble.rotate (angle = -omega * dt, axis = vector (0, 0, 1)) #angle = radiuns turned per frame
        #in this case angle = radians turned per 1/100 second
        #with angular vel = 0.05 * 100 = 5 rad/s
        
        v_mag = mag (marble.v)
        #translational plus rotational formulas
        I = (2/5) * mass * (marble_r**2)
        KE = (0.5 * mass * v_mag**2) + (0.5 * I * omega**2)
        
        #using y = -50 as baseline zero potential energy ig??
        PE = mass * g * (marble.pos.y + 50) 
        
        
        potential_curve.plot(pos=(t, PE))
        #print(PE)
        kinetic_curve.plot(pos=(t, KE))
        velocity_curve.plot(pos=(t, v_mag))
        normal_curve.plot(pos=(t, F_n_mag))