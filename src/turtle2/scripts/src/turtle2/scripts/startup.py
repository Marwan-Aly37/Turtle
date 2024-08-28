import rospy
import subprocess
rospy.init_node("start")
subprocess.run(['rosrun','turtle2','node_1.py'])
subprocess.run(['rosrun','turtlesim','turtlesim_node'])    