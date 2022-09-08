#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64


def don(mag):
    a = str(mag)
    b = a[-3]+a[-2]+a[-1]
    print("Currrent RPM slave 1 = ",b)


def callback(pose): #getting the caller id: get fully reoslved name of node
    mag = pose
    don(mag)
    # rospy.loginfo("Angle= %s", pose.data)


rospy.init_node('SUBcrpm', anonymous=True)

while not rospy.is_shutdown():
    rospy.Subscriber('crpm', Float64, callback)  
    rospy.spin() #keeps python form exiting until this node is stopped

