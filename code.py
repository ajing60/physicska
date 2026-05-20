GlowScript 3.0 VPython

coaster = curve (vector (-2, 5, 0), vector (-1, 3, 0), vector (0, 2, 0), vector (1, 2, 0), vector(2, 3, 0), vector (4,6,0))

theta = pi
d_theta = pi/100
while (theta <= 2*pi):
    theta += d_theta
    coaster.append (3*vector (cos(theta),sin(theta),0))

cart = sphere (pos=coaster.point(0).pos+vector(0.1,color=color.red,radius=0.1,speed=0,mass=1))
g=1

def track(posn):
    x=posn.x
    z=posn.z
    y=0
    slope = 0
    displacement = vector (0,0,0)
#find pos along track
    for i in range (coaster.npoints-1):
        if (coaster.point(i).pos.x <= x <= coaster.point(i+1).pos.x and coaster.point(i).pos.z <= z <= coaster.point(i+1).pos.z):
            slope = (coaster.point(i+1).pos.y-coaster.point(i).pos.y)/(coaster.point(i+1).pos.x-coaster.point(i).pos.x)