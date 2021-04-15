#!/usr/bin/env python
# license removed for brevity
import rospy
import bagpy
from bagpy import bagreader
import pandas as pd

b = bagreader("/home/iris/catkin_ws/src/robotics_demo/bags/unity1.bag")
forceFile = b.message_by_topic("/motorForce")
