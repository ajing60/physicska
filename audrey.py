GlowScript 2.7 VPython
#Call the library for Motion Map
get_library('https://rawgit.com/perlatmsu/physutil/master/js/physutil.js')
 
#Window setup
scene.range = 15
scene.background = vector(1, 1, 0.8)
 
 
#the values below can be adjusted to change the properties of the ramp
ramp_angle = 23 * pi/180
ramp_depth = 6
ramp_width = 30
ramp_origin = vec(-15, -10, 0)
 
#the code below draws the ramp (lines 17 - 45)
ramp_color = color.gray(0.3)
edge_thickness = 0.05
edge_color = color.black
 
a = vertex(pos=vec(0, 0, 0)+ramp_origin, color=ramp_color, opacity=.5)
b = vertex(pos=vec(0, 0, ramp_depth)+ramp_origin, color=ramp_color, opacity=.5)
c = vertex(pos=vec(ramp_width, 0, 0)+ramp_origin, color=ramp_color, opacity=.5)
d = vertex(pos=vec(ramp_width, 0, ramp_depth)+ramp_origin, color=ramp_color, opacity=.5)
e = vertex(pos=vec(0, ramp_width * tan(ramp_angle), 0)+ramp_origin, color=ramp_color, opacity=.5)
f = vertex(pos=vec(0, ramp_width * tan(ramp_angle), ramp_depth)+ramp_origin, color=ramp_color, opacity=.5)
 
ramp_base = quad(v0=a, v1=b, v2=d, v3=c)
ramp_surface = quad(v0=e, v1=f, v2=d, v3=c)
ramp_back = quad(v0=e, v1=f, v2=b, v3=a)
ramp_side_near = triangle(vs=[a, c, e])
ramp_side_far = triangle(vs=[b, d, f])
 
def edge(v1, v2, r):
    cylinder(pos = v1.pos, axis = v2.pos-v1.pos, radius = r, color = edge_color)
 
ab = edge(a, b, edge_thickness)
ac = edge(a, c, edge_thickness)
bd = edge(b, d, edge_thickness)
cd = edge(c, d, edge_thickness)
ae = edge(a, e, edge_thickness)
bf = edge(b, f, edge_thickness)
ef = edge(e, f, edge_thickness)
df = edge(d, f, edge_thickness)
ec = edge(e, c, edge_thickness)
 
 
#The values below can be changed to modify the dimensions of the block
block_width = 3
block_height = 3
block_depth = 3
 
#Create the block on the ramp
block = box( pos=vector(0.5*(block_width**2+block_height**2)**0.5 * cos(atan(block_height/block_width) - ramp_angle), ramp_width * tan(ramp_angle) + 0.5*(block_width**2+block_height**2)**0.5 * sin(atan(block_height/block_width) - ramp_angle), 0.5*ramp_depth) + ramp_origin, 
            axis=vector(ramp_width, -ramp_width * tan(ramp_angle), 0), 
            size=vector(block_width,block_height,block_depth),
            color = vector(0.65, 0.15, 0.15),
            texture = textures.wood_old,
            opacity = 0.7)
 
 
#Set up the physical properties like the mass and velocity of the block, the acceleration due to gravity, time and the coefficient of friction.
mblock = 50
vblock = vector(0, 0, 0)
g = vector(0,-9.8,0)
cof = 0.3   #coefficient of friction#
t = 0
tf = 5
dt = .001
 
#Define the force vectors acting on the block, including kinetic friction
Fgrav = mblock * g
Fnorm = vector(mag(Fgrav) * cos(ramp_angle)*sin(ramp_angle), mag(Fgrav)*cos(ramp_angle)*cos(ramp_angle), 0)
Ffr = vector(-cof*mag(Fnorm)*cos(ramp_angle), cof*mag(Fnorm)*sin(ramp_angle), 0) 
Fnet = Fgrav + Fnorm + Ffr
 
#Create arrows to show the forces with labels
FgravArrow = arrow(pos = block.pos, axis=Fgrav/mblock, shaftwidth=0.3, color = color.green)
FnormArrow = arrow(pos = block.pos, axis=Fnorm/mblock, shaftwidth=0.3, color = color.green)
FfrArrow = arrow(pos = block.pos, axis=Ffr/mblock, shaftwidth=0.3, color = color.green)
FgravLabel = label(pos=FgravArrow.pos, text='Fg', xoffset=-20, yoffset=-50, space=30, height=16, border=4, font='sans', line=False, color = color.black)
FnormLabel = label(pos=FnormArrow.pos, text='Fn', xoffset=-10, yoffset=70, space=30, height=16, border=4, font='sans', line=False, color = color.black)
FfrLabel = label(pos=FfrArrow.pos, text='Ffr', xoffset=-30, yoffset=30, space=30, height=16, border=4, font='sans', line=False, color = color.black)
 
 
#Slide the block (and arrows) down the ramp until it reaches the end of the ramp
while block.pos.y > ( ramp_origin.y+ 0.5*(block_width**2+block_height**2)**0.5 * cos(atan(block_width/block_height) - ramp_angle) ):
    rate(500)
 
 
    block.pos = block.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2 
 
    FgravArrow.pos = FgravArrow.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
    FnormArrow.pos = FnormArrow.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
    FfrArrow.pos = FfrArrow.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
    FgravLabel.pos = FgravLabel.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
    FnormLabel.pos = FnormLabel.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
    FfrLabel.pos = FfrLabel.pos + vblock*dt + 0.5*(Fnet/mblock)*dt**2
 
    vblock = vblock + (Fnet/mblock)*dt
    t = t + dt 