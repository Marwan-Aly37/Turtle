#!/usr/bin/env python3
#Author:Ibrahem Ahmed
import rospy
import subprocess
from turtlesim.msg import Pose
from std_msgs.msg import Int32
import math

health_1 = 100
health_2 = 100
health_3 = 100
health_4 = 100

turtle1_x = 0
turtle1_y = 0
turtle2_x = 0
turtle2_y = 0
turtle3_x = 0
turtle3_y = 0
turtle4_x = 0
turtle4_y = 0

rospy.init_node("control")

def position_turtle1(msg):
    global turtle1_x, turtle1_y
    turtle1_x = msg.x
    turtle1_y = msg.y

def position_turtle2(msg):
    global turtle2_x,turtle2_y
    turtle2_x = msg.x
    turtle2_y = msg.y

def position_turtle3(msg):
   global turtle3_x,turtle3_y
   turtle3_x = msg.x
   turtle3_y = msg.y

def position_turtle4(msg):
    global turtle4_x,turtle4_y
    turtle4_x = msg.x
    turtle4_y = msg.y



def recieve_attack_turtle1(msg):
    global health_1, health_2, health_3 ,health_4

    distance_tut1_tut2 = math.sqrt(abs(turtle1_x - turtle2_x) ** 2 + abs(turtle1_y - turtle2_y) ** 2)
    distance_tut1_tut3 = math.sqrt(abs(turtle1_x - turtle3_x) ** 2 + abs(turtle1_y - turtle3_y) ** 2)
    distance_tut1_tut4 = math.sqrt(abs(turtle1_x - turtle4_x) ** 2 + abs(turtle1_y - turtle4_y) ** 2)

    if (distance_tut1_tut2 < 1.5) and (msg.data == 1):
        health_2 = health_2 - 50
        if (health_2 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle2'])
            rospy.loginfo("Turtle 2 dead")

    if (distance_tut1_tut3 < 1.5) and (msg.data == 1):
        health_3 = health_3 - 50
        if (health_3 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle3'])
            rospy.loginfo("Turtle 3 dead")

    if (distance_tut1_tut4 < 1.5) and (msg.data == 1):
        health_4 = health_4 - 50
        if (health_4<= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle4'])
            rospy.loginfo("Turtle 4 dead")
    if(health_4 == 0 and health_2 == 0 and health_3 == 0):
        rospy.loginfo("Turtle 1 won")
    msg.data = 0


def recieve_attack_turtle2(msg):
   global health_1, health_2, health_3 ,health_4

   distance_tut1_tut2 = math.sqrt(abs(turtle1_x - turtle2_x) ** 2 + abs(turtle1_y - turtle2_y) ** 2)
   distance_tut2_tut3 = math.sqrt(abs(turtle2_x - turtle3_x) ** 2 + abs(turtle2_y - turtle3_y) ** 2)
   distance_tut2_tut4 = math.sqrt(abs(turtle2_x - turtle4_x) ** 2 + abs(turtle2_y - turtle4_y) ** 2)

   if (distance_tut1_tut2 < 1.5) and (msg.data == 1):
        health_1 = health_1 - 50
        if (health_1 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle1'])
            rospy.loginfo("Turtle 1 dead")
    
   if (distance_tut2_tut3 < 1.5) and (msg.data == 1):
       health_3 = health_3 - 50
       if (health_3 <= 0):
           subprocess.run(['rosservice', 'call','/kill','turtle3'])
           rospy.loginfo("Turtle 3 dead")

   if (distance_tut2_tut4 < 1.5) and (msg.data == 1):
        health_4 = health_4 - 50
        if (health_4 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle4'])
            rospy.loginfo("Turtle 4 dead")
   if(health_1 == 0 and health_4 == 0 and health_3 == 0):
       rospy.loginfo("Turtle 2 won")
   msg.data = 0

def recieve_attack_turtle3(msg):
    global health_1, health_2, health_3 ,health_4

    distance_tut1_tut3 = math.sqrt(abs(turtle1_x - turtle3_x) ** 2 + abs(turtle1_y - turtle3_y) ** 2)
    distance_tut2_tut3 = math.sqrt(abs(turtle2_x - turtle3_x) ** 2 + abs(turtle2_y - turtle3_y) ** 2)
    distance_tut3_tut4 = math.sqrt(abs(turtle3_x - turtle4_x) ** 2 + abs(turtle3_y - turtle4_y) ** 2)

    if (distance_tut1_tut3 < 1.5) and (msg.data == 1):
        health_1 = health_1 - 50
        if (health_1 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle1'])
            rospy.loginfo("Turtle 1 dead")

    if (distance_tut2_tut3 < 1.5) and (msg.data == 1):
        health_2 = health_2 - 50
        if (health_2 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle2'])
            rospy.loginfo("Turtle 2 dead")
    
    if (distance_tut3_tut4 < 1.5) and (msg.data == 1):
        health_4 = health_4 - 50
        if (health_4 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle4'])
            rospy.loginfo("Turtle 4 dead")
    if(health_1 == 0 and health_2 == 0 and health_4 == 0):
        rospy.loginfo("Turtle 3 won")
    msg.data = 0

def recieve_attack_turtle4(msg):
    global health_1, health_2, health_3 ,health_4
    distance_tut1_tut4 = math.sqrt(abs(turtle1_x - turtle4_x) ** 2 + abs(turtle1_y - turtle4_y) ** 2)
    distance_tut2_tut4 = math.sqrt(abs(turtle2_x - turtle4_x) ** 2 + abs(turtle2_y - turtle4_y) ** 2)
    distance_tut3_tut4 = math.sqrt(abs(turtle3_x - turtle4_x) ** 2 + abs(turtle3_y - turtle4_y) ** 2)
    if (distance_tut1_tut4 < 1.5) and (msg.data == 1):
        health_1 = health_1 - 50
        if (health_1 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle1'])
            rospy.loginfo("Turtle 1 dead")

    if (distance_tut2_tut4 < 1.5) and (msg.data == 1):
        health_2 = health_2 - 50
        if (health_2 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle2'])
            rospy.loginfo("Turtle 2 dead")

    if (distance_tut3_tut4 < 1.5) and (msg.data == 1):
        health_3 = health_3 - 50
        if (health_3 <= 0):
            subprocess.run(['rosservice', 'call','/kill','turtle3'])
            rospy.loginfo("Turtle 3 dead")
    if(health_1 == 0 and health_2 == 0 and health_3 == 0):
        rospy.loginfo("Turtle 4 won")
    msg.data = 0

def recieve_attack_number_1(attacks):
    if(attacks.data < 0):
        subprocess.run(['rosservice', 'call','/kill','turtle1'])
        rospy.loginfo("Turtle 1 dead")

def recieve_attack_number_2(attacks):
    if(attacks.data < 0):
        subprocess.run(['rosservice', 'call','/kill','turtle2'])
        rospy.loginfo("Turtle 2 dead")

def recieve_attack_number_3(attacks):
    if(attacks.data < 0):
        subprocess.run(['rosservice', 'call','/kill','turtle3'])
        rospy.loginfo("Turtle 3 dead")

def recieve_attack_number_4(attacks):
    if(attacks.data < 0):
        subprocess.run(['rosservice', 'call','/kill','turtle4'])
        rospy.loginfo("Turtle 1 dead")




sub_position1 = rospy.Subscriber('/turtle1/pose', Pose, position_turtle1)
sub_position2 = rospy.Subscriber('/turtle2/pose', Pose, position_turtle2)
sub_position3 = rospy.Subscriber('/turtle3/pose', Pose, position_turtle3)
sub_position4 = rospy.Subscriber('/turtle4/pose', Pose, position_turtle4)





sub_attack1 = rospy.Subscriber('chatter1', Int32, recieve_attack_turtle1)
sub_attack2 = rospy.Subscriber('chatter2', Int32, recieve_attack_turtle2)
sub_attack3 = rospy.Subscriber('chatter3', Int32, recieve_attack_turtle3)
sub_attack4 = rospy.Subscriber('chatter4', Int32, recieve_attack_turtle4)

sub_attack1 = rospy.Subscriber('num_attack1', Int32, recieve_attack_number_1)
sub_attack2 = rospy.Subscriber('num_attack2', Int32, recieve_attack_number_2)
sub_attack3 = rospy.Subscriber('num_attack3', Int32, recieve_attack_number_3)
sub_attack4 = rospy.Subscriber('num_attack4', Int32, recieve_attack_number_4)




rospy.spin()
