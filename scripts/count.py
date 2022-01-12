#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.

#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size = 1)
rate = rospy.Rate(10)

n = 0

while not rospy.is_shutdown():
	for n in range(0, 10):
		m += 1
	pun.publish(n)
	pub.publish(m)
	rate.sleep()
