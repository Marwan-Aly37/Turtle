Package Name: turtle2

Create Workspace

Workspace Name: turtle_ws

src dir given

catkin_make for creating devel and build dir

source setup.bash in devel dir

Python scripts: Each keyboard script is responsible for contolling one turtle

keyboard.py-->turtle1 / keyboard2.py-->turtle2 / keyboard3.py-->turtle3 / keyboard4.py-->turtle4    

control.py--> runs the logic for the gameplay decreasing health and informing us when a turtle is dead and who is the winner

node.py--> Responsible for resetting the game and spawning the turtles it also takes input from the player on how many players are playing and spawns the turtles accordingly. The position for spawning turtles is changes depending on how many players are playing the game. 

window.py--> opens the turtlesim window 

startup.py--> runs control.py, Window.py and node.py simultaneously to reduce the number of commands being typed into the terminal

To run the code go to terminal and type:
      roscore
      rosrun turtle2 startup.py   #runs the game and shoud ask you for number of players as input and spawns turtles accordingly
      rosrun turtle2 keyboard.py  #each computer should run one keyboard script so computer 1 runs keyboard.py, computer 2 runs keyboard2.py and so on
Your all set after running the keyboard script move the turtle with the WASD keys and attack with q
-q has a countdown after each use to prevent spamming
-each turtle starts with 100 health and each attack does 50 damage so 2 hits and your turtle will despawn
-must install ROS to run
