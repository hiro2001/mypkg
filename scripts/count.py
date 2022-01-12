#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.
#*Copyright(c)2021 Hiroyuki Matsuda. All rights reserved.

import rospy
from std_msgs.msg import Int32

rospy.init_node('second')
pub = rospy.Publisher('second_up', Int32, queue_size = 1)
rate = rospy.Rate(1)

n = 0

while not rospy.is_shutdown():
        n += 1
        pub.publish(n)
        rate.sleep()
