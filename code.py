Web VPython 3.2

#define size of viewing box to be x: 0-150, y: -50, 50

theta = pi
d_theta = pi/git100
while (theta <= 2*pi):
    theta += d_theta
    coaster.append (3*vector (cos(theta),sin(theta),0))
scene.width = 800
scene.height = 500

x_min= 0
x_max=100
y_min=-15
y_max=15

t= 0
dt=0.01
g=9.81


sphere_location = vector (0,0,0)
v_i = 0

box_location = vector(0,-1,0)

def path(x):
    if path_type == "Ramp":
        if x < 0: return 10
        if 0 <= x <= 30: return 10 - (0.5 * x)
        return -5
    elif path_type == "Valley":
        if 10 <= x <= 50:
            return -5 - sqrt(abs(400 - (x-30)**2))
        return -5
    elif path_type == "Curves":
        return 4 * sin(x / 10)
    elif path_type == "Rollercoaster":
        if 20 <= x <= 50:
            return 15 * exp(-((x-35)**2)/50)
        return 0
    return -5



marble = sphere(pos=sphere_location,radius = 1,texture = textures.wood) # make_trail=True 
#box(pos=box_location, size=vector(0.5,0.1,1.0))
    
while True:
    rate(100) #runs 100 frames per second
    marble.pos.y = v_i * t + 0.5 * -9.81 * t**2
    
    
    y = get_floor(marble.pos.x)
    if y is not None and 0 <= marble.pos.x <= 100:
        
    
    
    elif marble.pos.y <= y_min:
        marble.pos.y = y_min  # floor clamp
    
    t += dt
    
    
    omega = v.x / radius
    marble.rotate(angle=-omega * dt, axis=vector(0, 0, 1))
    marble.rotate(angle=0.05, axis=vector(0, 0, 1)) #angle = radians turned per frame
    
#in this case, angle = radians turned per 1/100 second
#so w/angular vel = 0.05 * 100 = 5rad/s
#translational and rotational kinetic
#