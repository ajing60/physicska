GlowScript 3.0 VPython

coaster = curve (vector (-2, 5, 0), vector (-1, 3, 0), vector (0, 2, 0), vector (1, 2, 0), vector(2, 3, 0), vector (4,6,0))

theta = pi
d_theta = pi/100
while (theta <= 2*pi):
    theta += d_theta
    coaster.append (3)
