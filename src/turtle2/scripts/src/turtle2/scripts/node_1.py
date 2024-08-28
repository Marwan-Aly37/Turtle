import rospy
import subprocess
rospy.init_node("node_1")
subprocess.run(['rosrun','turtle2','keyboard.py'])        

