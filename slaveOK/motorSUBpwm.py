#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt16


def don(mag):
    a = str(mag)
    b = a[-3]+a[-2]+a[-1]
    print("Currrent PWM Slave 1 = ",b)


def callback(pose): #getting the caller id: get fully reoslved name of node
    mag = pose
    don(mag)
    # rospy.loginfo("Angle= %s", pose.data)


rospy.init_node('SUBpwm', anonymous=True)

while not rospy.is_shutdown():
    rospy.Subscriber('pwm', UInt16, callback) # 
    rospy.spin() #keeps python form exiting until this node is stopped

