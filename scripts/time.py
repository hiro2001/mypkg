#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0
m = 0

def cb(message):
	global n
	global m

	n = message.data
	if n == 60:
		n = 0
	m = 
	#rospy.loginfo(message.data*2)

if __name__=='__main__':
	rospy.init_node('time')
	sub = rospy.Subscriber('count_up', Int32, cb)
	pub = rospy.Publisher('twice', Int32, queue_size = 1)
	rate = rospy.Rate(10)
	#rospy.spin()
	while not rospy.is_shutdown():
		pub.publish(n)
		rate.sleep()
