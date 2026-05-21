Web VPython 3.2

#define size of viewing box to be x: 0-150, y: -50, 50
x_min= 0
x_max=150
y_min=-50
y_max=50

t= 0

sphere_location = vector (0,0,0)
v_i = 0

box_location = vector(0,-1,0)


marble = sphere(pos=sphere_location,radius = 1,texture = textures.wood) # make_trail=True 
box(pos=box_location, size=vector(0.5,0.1,1.0))

while True:
    rate(100) #runs 100 frames per second
    if(marble.pos.y <= y_min):
        
    else:
        marble.pos.y = v_i*t + 0.5 * -9.81 * t**2
    t += 0.01
    
    marble.rotate(angle = 0.05, axis =vector(0,0,1)) #angle = radians turned per frame
    
#in this case, angle = radians turned per 1/100 second
#so w/angular vel = 0.05 * 100 = 5rad/s
#translational and rotational kinetic
#