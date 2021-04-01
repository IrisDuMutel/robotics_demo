#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from robotics_demo.msg import QuadForce

def QuadForces():
    pub = rospy.Publisher('motorForce', QuadForce, queue_size=10)
    rospy.init_node('QuadForces', anonymous=True)
    msg = QuadForce()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg.flm = 0
        msg.frm = 0
        msg.rlm = 0
        msg.rrm = 0
        msg.yaw = 0
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        QuadForces()
    except rospy.ROSInterruptException:
        pass