#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def don(mag):
    a = str(mag)
    b = a[-10:-1]
    print("Currrent direction Slave 1 = ",b)


def callback(pose): #getting the caller id: get fully reoslved name of node
    mag = pose
    don(mag)
    # rospy.loginfo("Angle= %s", pose.data)


rospy.init_node('SUBdir', anonymous=True)

while not rospy.is_shutdown():
    rospy.Subscriber('dir', String, callback) # 
    rospy.spin() #keeps python form exiting until this node is stopped

