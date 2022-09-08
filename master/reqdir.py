#!/usr/bin/env python3 

# the first line is always written to let the ROS know that the programming is done in python
#from tokenize import String
import rospy
from std_msgs.msg import String # importing string from standard message type for ROS

# defining the function
def move():
    rospy.init_node('req_dir', anonymous=True) # initializing node with unique node name
    pub = rospy.Publisher('req_dir', String, queue_size=10) # defining topic name on which ROS message will be published
    dir = String()
    dir = str(input("Input your required Direction ('f' = forward, 'b' = backward, 'x' = stop): "))
    rate = rospy.Rate(1) # defining frequency of the message to publish


    while not rospy.is_shutdown(): # sending the messages while ros node is not shut     
        pub.publish(dir)
        rate.sleep() 
        dir = str(input("Input your required Direction ('f' = forward, 'b' = backward, 'x' = stop): "))


while(True):
    if __name__ == '__main__':
        try:
            move() # calling the function 
        except rospy.ROSInterruptException: 
            pass