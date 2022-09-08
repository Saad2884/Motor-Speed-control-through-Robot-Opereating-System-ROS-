#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32


def move():
    rospy.init_node('req_rpm', anonymous=True)
    pub = rospy.Publisher('req_rpm', Float32, queue_size=10)
    speed = Float32()
    speed = int(input("Input your required RPM value: "))
    rate = rospy.Rate(1)


    while not rospy.is_shutdown():     
        pub.publish(speed)
        rate.sleep() 
        speed = int(input("Input your required RPM = "))


while(True):
    if __name__ == '__main__':
        try:
            move()
        except rospy.ROSInterruptException: 
            pass