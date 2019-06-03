# Pi In The Sky

## Planning

### Goal
Our assignment is to somehow get a Pi in the air (whether it be thrown, shot, etc.) and do two things: collect acceleration data of the whole flight and signal when it thinks it's at the apex of its flight. We have to make some sort of enclosure to hold all of the components in place. 

### Resources and Constraints
Resources: 3D printer, laser cutter, soldering set, hand tools
Constraints: time and materials (we can't use too much material and we are not limetless in our resources)

### Solution
We want to create an enclosure shaped like a slice of pie for our pi (and all of its related components for this project) to be shot out of a sling shot that we will also make. 

### Materials
- Raspberry Pi Zero
- Lithium Battery
- Accelerometer
- PowerBoost 500 Charger
- LED (to signal top of flight)
- acrylic/laser cutter
- 3D printer
- styrofoam

### Design
![PiInTheSkyPlanning](https://github.com/jdreese79/PiInTheSky/blob/master/IMG_8211.jpg)
![PiInTheSkyFrtitzingDiagram](https://github.com/jdreese79/PiInTheSky/blob/master/elodiejackfriztingimage.PNG)

### Schedule

February 1st- Finish Planning (completed)

February 8th- solidworks design almost complete (completed)

February 15th- solidworks design complete and ready to get printed out (completed)

February 22nd- solidworks parts printed out (completed)

March 1st- components wired/ soldering finished (completed)

March 8th- styrofoam cut out (completed)

March 15th- begin slingshot (completed)

March 22nd- wood parts for slingshot cut and assembled (completed)

March 29th- slingshot finalized/ all parts painted

April 12th- progress on code

April 19th- progress on code... however long this takes (final step for code: make it headless/ starts on its own at startup)


### Timeline

2/4/19- Today we began assembling the components on solidworks. We mated a header to the pi and worked on making a bonnet to use for the solidowrks design.

2/6/19- We continued working on the solidworks design and began working on the fritzing.

2/7/19- Finished the fritzing diagram and uploaded it to github. Continued working on the solidworks design while waiting for the bonnet to come.

2/8/19- We continued working on the solidworks design because the bonnet still hasn't come in yet.

2/15/19- Today we lasercut the acrylic base for the raspberry pi.

2/21/19- The bonnet came in and we soldered a header to it for the raspberry pi to connect to. Next class we will solder the remaining headers and wires.

2/22/19- Today we finishd the soldering.

2/25/19- We 3D printed the brackets that will hold the battery in place. We also planned out how we're going to make the slingshot and the pie slice.

2/27/19- Today we finishing the wiring and started working on the styrofoam pie slice.

2/28/19- We finished cutting out all of the layers of the pie slice.

3/1/19- Today we glued together all of the styrofoam layers.

3/6/19- We decided to use our styrofoam model as a prototype and then rebuilt the pie slice using more durable material. We used a more precise way of cutting the layers to create a cleaner shape.

3/7/19- Today we glued the layers together and cut a rectangle out of the center. Finally we cut a small circle out of the top layer to fit the LED mount inside (to act as a cherry on a piece of pie).

3/8/19- Today we worked on creating a model of the pie on solidworks so that we can upload renderings to the wiki.

3/11/19- After completing the pie and the model of the pie, we began brainstorming how we were going to make the slingshot.

3/13/19- We gathered all of the neccesary pieces of wood to cut and then put together to make the slingshot. We marked off the parts of the wood to be cut to make it the desired length.

3/14/19- We learned how to use the power saw and cut all of our pieces the appropriate length. We then began drilling the screws.

3/15/19- The angle of the screws made it so that they stick out a lot and didn't securly hold the wood in place. We tried adding a second screw on each side to fix the problem, though this only made it worse.

3/18/19- We decided that we would start over on the slingshot and use the first attempt as a rough draft. We decided to alter the design slightly from our initial design, which had the flanks coming out at an angle, and make it so the slingshot resembled the uprights in football. This would hopefully make it easier to drill in the screws. We cut all of the pieces using scraps from the original attempt.

3/20/19- We screwed the wood pieces together and added a stand to keep it standing upright without us holding it. We also started making a solidworks rendering of it.

3/25/19- Today we began working on the code for our project.

3/29/19- This week we've continued to make progress on our code.

4/12/19- This week we've continued to make progress on our code.

4/19/19- This week we've continued to make progress on our code.

4/26/19- This week we've continued to make progress on our code.

5/3/18- This week we've continued to make progress on our code.

5/6/19- Today we teste out spray paint on the styrofoam then decided to use regular paint to paint our pie slice.

5/8/19- Today we began to decorate our slice of pie with cherry colors. 

5/9/19- Today we finished decorating our pi slice and now all we have to do is finish the code.

6/3/18- Today we finally completed our code. We put our project together and launched it, then were able to collect the data.

### Challenges

  There were many challenges throughout this project. One of the earlier issues was figuring out how exactly we were going to complete this project. To solve this issue, we had to really understamd what the guidelines wer asking of the project and we had to brainstorm different ways we could go about figuring it out. Wiring our pi also brought up some issues. Our code wouldn't work at first because we didn't wire the bonnet correctly. We solved the issues with the bonnet by creating soldering bridges between the where the wires were and where they needed to go. We also had to do a lot of research to figure out how to wire a battery pack to the pi. The code wasn't as challenging as we expected, though it did pose some obstacles. Two of the biggest challenges were finding the correct equations to determine the time that the pi reached the top of its flight, and making the pi run headless. We used our physics knowledge to ome up with a series of equations to determine the time. The code for this portion was pretty basic. Making thecode run headless went smoothly after we found a really helpful website. The issue with the code running headless, though, was that the data wouldn't save to a text file when it wasn't connected tp the computer. We solved this by changing the headless code from rc.local to bash. 

### Final Product

  Our final product is a pie slice made out of styrofoam with an LED "cherry" and an on/off switch at the top. Inside, is a raspberry pi wired with a powerboost and an accelerometer. When it is turned on, the pi reboots and the LED blinks twice at startup. After this, you can shoot the pi out of the slingshot that we made, and the LED will blink once at the apex of its flight. The LED will then quickly blink twice signaling that the data is being saved and the code is turned off. You can then access the data collected after plugging the pi back into the monitor.
  
![Final Image]( https://github.com/jdreese79/Engineering_4_Notebook/blob/master/pieslicefinalpicture.PNG)
