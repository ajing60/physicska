Web VPython 3.2
#define size of viewing box
x_min = 0
x_max = 100
y_min = -15
y_max = 15

fps = 100
t = 0
dt = 1/fps
g = 9.81
Fg = vector (0, -g, 0)

#making buttons for path type
def set_curves():
    globals().update(path_type="curves")

def set_loop():
    globals().update(path_type="loop")

def set_ramp():
    globals().update(path_type="ramp")

button(bind=set_curves)
button(bind=set_loop)
button(bind=set_ramp)


path_type = "curves" #"loop""ramp"
mass= 10
path_curve = None

sphere_location = vector (0, 20, 0)

def path (x):
    if path_type == "ramp": 
        if x < 0: return 10
        if 0 <= x <= 30: return 10 - (0.5 * x)
        return -50

    elif path_type == "curves":
        if 0 <= x <= 90: 
            return 4 * sin (x/10)
        else: return -50
    
    elif path_type == "loop":
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

    return -5

def setup ():
    if path_curve: path_curve.visible = False
    pts = []
    for x_val in arange (0, 100, 0.5): 
        pts.append (vector (x_val, path(x_val), 0))
    path_curve = curve (pos = pts, color = color.white, radius = 0.2)

marble = sphere (pos = sphere_location, radius = 1, texture = textures.wood)
marble.v = vector (20,0,0)

path_pts = []
for xcoord in arange(0, 100.5, 0.5):
    path_pts.append(vector(xcoord, path(xcoord), 0))
path_curve = curve(pos=path_pts, color=color.cyan, radius=0.2)


def slope (x): 
    dx = 0.01
    return (path (x + dx) - path (x-dx))/(2*dx)

while True: 
    rate (fps) # run 100 frames per sec
    F_net = vector(0,-g*mass,0)
    #marble.pos.y = v_i*t + 0.5 * -9.81 * t** 2

    if marble.pos.y <= (path (marble.pos.x)+0.5): 

        #path normal vector
        m= slope(marble.pos.x)
        n_mag= sqrt(1+m**2)
        normal= vector(-m/ n_mag, 1/ n_mag, 0)
        v_n = dot(marble.v, normal)
        if v_n < 0:
            marble.pos.y = path(marble.pos.x)+0.5
            
            marble.v -= normal*v_n
        
        F_n = normal * (-dot(F_net, normal))
        F_net += F_n
        
        
    a = F_net/mass
    marble.v += a*dt
    marble.pos += marble.v *dt
        
        

    t += dt
    #omega = v_i.x / radius
    #marble.rotate (angle = -omega * dt, axis = vector (0, 0, 1)) #angle = radiuns turned per frame
    #in this case angle = radians turned per 1/100 second
    
    #with angular vel = 0.05 * 100 = 5 rad/s


