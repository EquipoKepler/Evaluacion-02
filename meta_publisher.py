#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
import numpy as np
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
import tf
import tf2_ros 
import time
from sensor_msgs.msg import LaserScan


def gen_random_goal():

    rand_pos = np.asarray((-4.5,-3.5))+ 0.5*np.random.randn(2)
    rand_rot = tf.transformations.quaternion_from_euler(((np.random.rand()-0.5 )*2*np.pi) ,0,0 )
    
    pose_stamped=PoseStamped()
    pose_stamped.header.frame_id= 'map'
    pose_stamped.pose.position.x=rand_pos[0]
    pose_stamped.pose.position.y=rand_pos[1]
    ########################################
    pose_stamped.pose.orientation.w= rand_rot[0]
    pose_stamped.pose.orientation.x= rand_rot[1]
    pose_stamped.pose.orientation.y= rand_rot[2]
    pose_stamped.pose.orientation.z= rand_rot[3]
    objetivox=pose_stamped.pose.position.x
    objetivoy=pose_stamped.pose.position.y
    
    return pose_stamped
    print('Calculando una meta aleatoria al rededor del punto -4.5, -3.5 (zona 1)',rand_pos)

def talker():
    goal_comp_pub = rospy.Publisher('/meta_competencia', PoseStamped, queue_size=10)
    rospy.init_node('meta_publisher_node')
    rate = rospy.Rate(1) # 1hz
    pose_stamped_goal=gen_random_goal()
    print('Meta publicando')
    print ('coordenadas aleatoria',pose_stamped_goal)

    while not rospy.is_shutdown():
       
       
        
        goal_comp_pub.publish(pose_stamped_goal)
        rate.sleep()
        



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        
      #source ~/CIRE2022/catkin_ws/devel/setup.bash
      #rosrun publisher_meta_etapa2 meta_publisher.py
