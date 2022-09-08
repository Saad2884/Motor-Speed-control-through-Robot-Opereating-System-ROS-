#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32


def don(mag):
    a = str(mag)
    b = a[-5:-1]
    print("Slave 4 PWM = ",b)


def callback(pose): #getting the caller id: get fully reoslved name of node
    mag = pose
    don(mag)
    # rospy.loginfo("Angle= %s", pose.data)


rospy.init_node('SUBpwm4', anonymous=True)

while not rospy.is_shutdown():
    rospy.Subscriber('pwm4', Float32, callback) # 
    rospy.spin() #keeps python form exiting until this node is stopped

