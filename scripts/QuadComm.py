#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from robotics_demo.msg import QuadComm

def QuadCommands():
    pub = rospy.Publisher('QuadCommands', QuadComm, queue_size=10)
    rospy.init_node('QuadComm', anonymous=True)
    msg = QuadComm()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg.roll = 0
        msg.pitch = 0
        msg.yaw = 0.5
        msg.h_vel = 0
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        QuadCommands()
    except rospy.ROSInterruptException:
        pass