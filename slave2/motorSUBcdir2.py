#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def don(mag):
    a = str(mag)
    b = a[-9:-1]
    print("Slave 2 DIR = ",b)


def callback(pose): #getting the caller id: get fully reoslved name of node
    mag = pose
    don(mag)
    # rospy.loginfo("Angle= %s", pose.data)


rospy.init_node('SUBdir2', anonymous=True)

while not rospy.is_shutdown():
    rospy.Subscriber('dir2', String, callback) # 
    rospy.spin() #keeps python form exiting until this node is stopped

