#!/usr/bin/env python3
import rospy
import subprocess
from turtlesim.msg import Pose
from std_msgs.msg import Int32
health_1 = 100
health_2 = 100
turtle1_x = None
turtle1_y = None
turtle2_x = None
turtle2_y = None  
rospy.init_node("control")
def pose_callback1(msg):
    global turtle1_x, turtle1_y
    turtle1_x = msg.x
    turtle1_y = msg.y
def pose_callback2(msg):
    global turtle2_x,turtle2_y
    turtle2_x = msg.x
    turtle2_y = msg.y
def recieve_callback(msg):
    global health_1,health_2
    distance_x = abs(turtle1_x - turtle2_x) 
    distance_y = abs(turtle1_y - turtle2_y) 
    if (distance_x<0.5) and (msg.data == 1):
        health_2 = health_2 - 50
        msg.data = 0
    if (distance_y <0.5) and (msg.data == 1):
        health_2 = health_2 - 50
        msg.data = 0
    if (health_2 == 0):
        subprocess.run(['rosservice', 'call','/kill','turtle2'])
        rospy.loginfo("Winner is turtle1")
        

    
sub = rospy.Subscriber('chatter',Int32,recieve_callback)
sub1 = rospy.Subscriber('/turtle1/pose',Pose,pose_callback1)
sub2 = rospy.Subscriber('/turtle2/pose',Pose,pose_callback2)
rospy.spin()
