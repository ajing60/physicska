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
path_type = "ramp" "curves" "loop"

sphere_location = vector (0, 0, 0)
v_i = 0

def path (x):
    if path_type == "ramp": 
        if x < 0: return 10
        if 0 <= x <= 30: return 10 - (0.5 * x)
        return -5

    elif path_type == "curves":
        return 4 * sin (x/10)
    
    elif path_type == "loop":
        if (0.9 <= marble.pos.y <= 1.7): 
            if (4 <= x <= 4.4 or 5.6 <= x <= 6): 
                return ((1 - (x-5)**2)**0.5)+1.7
            elif (1.7 < marble.pos.y): 
                if (4 <= x <= 6): 
                    return -1 * ((1 - (x-5)**2)**0.5)+1.7
            elif 0 <= x <= 5: 
                return 0.5 * math.e**(x+5)
            elif 5 <= x <= 10: 
                return 0.5 * math.e ** (-x + 5)
            else:
                return -5

    return -5

def setup ():
    global path_curve
    if path_curve: path_curve.visible = False
    pts = []
    for x_val in arange (0, 101, 0.5): 
        pts.append (vector (x_val, get_floor (x_val), 0))
    path_curve = curve (pos = pts, color = color.white, radius = 0.2)

marble = sphere (pos = sphere_location, radius = 1, texture = textures.wood)

def slope (x): 
    dx = 0.01
    return (path (x + dx) - path (x-dx))/(2*dx)

while True: 
    rate (fps) # run 100 frames per sec
    marble.pos.y = v_i*t + 0.5 * -9.81 * t** 2

    if marble.pos.y <= path (marble.pos.x): 
        n_slope = slope (marble.pos.x)
        n_mag = sqrt (1 + slope ** 2)
        normal = vector (-n_slope/n_mag, 1/n_mag, 0)

    t += dt
    omega = v.x / radius
    marble.rotate (angle = -omega * dt, axis = vector (0, 0, 1)) #angle = radiuns turned per frame
    #in this case angle = radians turned per 1/100 second
    #with angular vel = 0.05 * 100 = 5 rad/s

path = curve (pos = [vector (0, 0, 0)])
for i in range (0, 50): 
    path.append()