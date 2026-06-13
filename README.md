INTRODUCTION:
The player will choose one of several path options we provide, and can select the coefficient of friction and elasticity of the path material. A marble is placed at the start of the path and the player can set an initial velocity for when the marble is released by clicking to set an arrow. Our path options include sine curves, free falls, and types of ramps so that we can use centripetal force and changes in normal force in our calculations. Based on the starting velocity and the friction and elasticity, the marble will travel a different distance.

USER INTERFACE:
Sliders:
Coefficient of Friction: The user can choose a kinetic coefficient of friction ranging from 0 to 1. The starting coefficient is automatically 0 and the friction updates in real time as you drag the slider. The static friction is automatically set at 1.3 times the kinetic coefficient.
Elasticity: The user can choose the elasticity of the path ranging from 0 to 1. The starting elasticity is automatically 0, meaning the path is not bouncy at all. The elasticity updates in real time as you drag the slider.

Click: Before you launch the marble, click anywhere on the screen (preferably towards the path for a more interesting run) to create a velocity arrow. The direction and length of the arrow correlate to the direction and magnitude of the marble’s starting velocity. If you do not click on the screen, the marble will move with a default horizontal initial velocity. 

Buttons:
	Launch: After you have chosen your desired initial velocity, press launch to apply it to the marble and watch it interact with the path. 
	Reset: Once the marble has run its course, or even if you are dissatisfied with your current run, press reset to bring the marble back to its starting position where you can once again, choose your desired initial velocity. 


Paths:
	Sine: A sine graph which easily shows the changes in normal force and can be entertaining if you increase the elasticity. 
	Free Fall: A large curve down that launches the marble into the air, an excellent show of projectile motion.
	Ramp Down: A simple straight path with a ramp downwards which can be used to demonstrate the changes in translational velocity when the coefficient of friction is changed. 
	Ramp Fancy: A mix of several graphs. It is very fun to test the slider functions on this path!

Graphs: Three graphs all plotted against time. 
	Energy: This graph includes both kinetic and potential energy throughout the marble run.
	Velocity: This graph models the translational velocity of the marble throughout the marble run.
	Normal Force: This graph shows the normal force of the marble throughout the marble run. 

USER INSTRUCTIONS:
1. Run the program!
2. Adjust the parameters to your heart’s desire. You can change the coefficient of friction and elasticity of the path using the two sliders at the top. 
3. Click the type of path that you want to explore. There are four options, make sure to take a look at each!
4. Press anywhere on the black screen to set the initial velocity of the marble. Note that the arrow will carry information about magnitude and direction, so be careful of how far away from the marble itself you click. 
5. Click LAUNCH to see your marble move! It will go through the path selected and even fall off into space, at least until it hits the red bar below the path.
6. Make sure to scroll down to see the energy, velocity, and force graphs. Force is especially interesting because it reveals whenever the marble lifts off the track because the normal force goes to zero.
7. Click RESET to try different paths and parameters. Enjoy!

PHYSICS:
Some calculations we consider are the varying normal forces at different points on the path, mechanical energy and energy lost to friction, if the marble rolls, slides, or slips, and if the marble lifts off the path.

The normal force is calculated by adding up the components of gravity perpendicular to the path's surface by taking the dot product between gravity and the path's normal. The centripetal acceleration is calculated by finding the radius of the curve using the equation
p=((1+(y’)^2)^(3/2))/(y’’ magnitude)

Additionally, friction force was calculated, and the sign was determined depending on the direction and acceleration of the marble. Using the friction force, the torque on the marble was calculated. We set the marble to have a rotational inertia of a solid sphere and calculated the rotational velocity. For the slip vs rotating, we looked at the difference between rotating and translational surface speeds. Depending on the difference, we determined whether to use kinetic or static friction, also determining if the marble slipped or rotated. 

Finally, we added in elasticity, which controls behavior when the marble lifts off the track and hits the path again. If elasticity is set to zero, the marble won’t bounce at all. We have that delta (v) = -v_n (1 + 0) = -v_n, so the final v is just zero. This means that the marble doesn’t have any normal velocity and just rides smoothly along the track. If the elasticity is set to one, the opposite happens and the marble bounces back off the track with the same speed at which it hit it. We let the user choose values in between as well for a more realistic representation of real-life collisions.
