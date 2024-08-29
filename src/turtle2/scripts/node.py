#!/usr/bin/env python3
import subprocess
import rospy
from std_msgs.msg import Int32
def turtles():

    num = int(input("Enter number of players: "))

    rospy.init_node("number_of_players_node")
    pub = rospy.Publisher("players_topic", Int32, queue_size=10)
    rate = rospy.Rate(1)
    rospy.sleep(1)
    for i in range (5):
        pub.publish(num)
        rospy.sleep
    

    #try:
    #    subprocess.run(['rosservice', 'call','/kill','turtle2'])
    #    subprocess.run(['rosservice', 'call','/kill','turtle3'])
    #    subprocess.run(['rosservice', 'call','/kill','turtle4'])
    #except:
        #subprocess.run(['rosservice', 'call','/kill','turtle1'])
    subprocess.run(['rosservice', 'call','/kill','turtle1'])
    if (num == 1):
        subprocess.run(['rosservice','call','/spawn','5.5','5.5','0.0','turtle1'])
    elif(num == 2):  
        subprocess.run(['rosservice','call','/spawn','1.0','5.5','0.0','turtle1']) 
        subprocess.run(['rosservice','call','/spawn','10.0','5.5','3.2','turtle2'])  
    elif(num == 3):
        subprocess.run(['rosservice','call','/spawn','1.0','10.0','0.0','turtle1']) 
        subprocess.run(['rosservice','call','/spawn','1.0','1.0','0.0','turtle2'])     
        subprocess.run(['rosservice','call','/spawn','10.0','5.5','3.2','turtle3']) 
    elif(num == 4): 
        subprocess.run(['rosservice','call','/spawn','1.0','10.0','0.0','turtle1']) 
        subprocess.run(['rosservice','call','/spawn','10.0','10.0','3.2','turtle2'])     
        subprocess.run(['rosservice','call','/spawn','1.0','1.0','0.0','turtle3']) 
        subprocess.run(['rosservice','call','/spawn','10.0','1.0','3.2','turtle4'])  
    else: 
        turtles()
turtles()
