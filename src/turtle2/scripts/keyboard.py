#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys
import select
from std_msgs.msg import Int32
class turtle_attributes:
    def _init_ (self,pos_X,pos_y,health,atk_left):
        self.pos_x = pos_X
        self.pos_y = pos_y
        self.health = health
        self.atk_left = atk_left
        health = 100
        atk_left = 10
def pose_callback(data):
    global x ,y
    x = data.x
    y = data.y 

def key_press():
    rospy.init_node('keyboard_control_node', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pub_c = rospy.Publisher('chatter', Int32, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        key = get_key()
        cmd = Twist()
        if key == 'w':
            cmd.linear.x = 1.0
        elif key == 's':
            cmd.linear.x = -1.0
        elif key == 'a':
            cmd.angular.z = 1.0
        elif key == 'd':
            cmd.angular.z = -1.0
        elif key == 'q':
            pub_c.publish(1)
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
