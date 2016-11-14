#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    global pub
    data.angular.x=180*data.angular.x
    data.linear.x=-data.linear.x
    pub.publish(data)



def talker():
    global pub
    rospy.init_node('TurtleDF')
    pub = rospy.Publisher('cmd_DF',Twist,queue_size=1)
    rospy.Subscriber('cmd_MP',Twist,callback)
    rospy.spin()


if __name__ == '__main__':
        talker()
