#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys
import select
from std_msgs.msg import Int32
import time

last_attack_time = 0 
number_of_attacks = 10

def pose_callback(data):
    global x ,y
    x = data.x
    y = data.y 
    
def key_press():
    rospy.init_node('keyboard_control_node', anonymous=True)
    pub = rospy.Publisher('turtle3/cmd_vel', Twist, queue_size=10)
    pub_tut_3= rospy.Publisher('chatter3', Int32, queue_size=10)
    pub_tut_3_attacknum = rospy.Publisher('num_attack3', Int32, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():

        global last_attack_time, number_of_attacks

        key = get_key()
        cmd = Twist()

        if key == 'w':
            cmd.linear.x = 1.75
        elif key == 's':
            cmd.linear.x = -1.75
        elif key == 'a':
            cmd.angular.z = 1.75
        elif key == 'd':
            cmd.angular.z = -1.75
        elif key == 'q':
            current_time=time.time()
            if (current_time - last_attack_time >= 1.5):
                pub_tut_3.publish(1)
                number_of_attacks -= 1
                pub_tut_3_attacknum.publish(number_of_attacks)
                last_attack_time = current_time
        else:
            continue

        pub.publish(cmd)
        rate.sleep()

def get_key():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    tty.setcbreak(sys.stdin.fileno())
    return key

if __name__ == '__main__':
    import tty
    import termios
    try:
        key_press()
    except rospy.ROSInterruptException:
        pass
