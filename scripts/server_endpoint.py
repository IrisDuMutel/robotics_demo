#!/usr/bin/env python

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from robotics_demo.msg import UnityScene
from robotics_demo.msg import TestMsg
from robotics_demo.msg import PosRot, UnityColor, QuadComm ,QuadForce
from robotics_demo.srv import PositionService
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)
    
    tcp_server.start({
        'pos_srv': RosService('position_service', PositionService),
        # Publishers
        'pos_rot': RosPublisher('pos_rot', PosRot, queue_size=10),
        'odom': RosPublisher('odom', Odometry, queue_size=10),
        'odom_2': RosPublisher('odom_2', Odometry, queue_size=10),
        'odometry': RosPublisher('odometry', TestMsg, queue_size=10),

        # Subscribers
        'color': RosSubscriber('color', UnityColor, tcp_server),
        'motorForce': RosSubscriber('motorForce', QuadForce, tcp_server),
        'QuadCommands': RosSubscriber('QuadCommands', Twist, tcp_server),
        'CubeCommand': RosSubscriber('CubeCommand', Odometry, tcp_server),
        'unity_input': RosSubscriber('unity_input', UnityScene, tcp_server),
        'cmd_vel': RosSubscriber('cmd_vel', Twist, tcp_server)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
