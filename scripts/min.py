#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.
#*Copyright(c)2021 Hiroyuki Matsuda. All rights reserved.

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
	global n
	if(message.data % 600 == 0)
	n += 1
	#rospy.loginfo(message.data*2)

if __name__=='__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cb)
	pub = rospy.Publisher('twice', Int32, queue_size = 1)
	rate = rospy.Rate(10)
	#rospy.spin()
	while not rospy.is_shutdown():
		pub.publish(n)
		rate.sleep()
