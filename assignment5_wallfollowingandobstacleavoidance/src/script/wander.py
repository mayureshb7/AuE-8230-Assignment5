#! /usr/bin/env python3

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist	

pub = None

def LIDAR(msg):
    regions = {
        'Right': (min(msg.ranges[40:95])),
        'Forward':  min(min(msg.ranges[0:40]),min(msg.ranges[320:360])),
        'Left': min(msg.ranges[260:320]),

    }
    print('lidar')
    take_action(regions)
    
def take_action(regions):

   msg = Twist()

   linear_x = 0 
   angular_z = 0
   FL = 0.12
   FA = 0.46

   
   if regions['Forward'] < 1.5:
       linear_x = regions['Forward']*FL
       angular_z = 0
       print('step1')
       

   else:
        linear_x = 0.5
        print('step2')



   if regions['Right'] <0.8 or regions['Left'] <0.6 or regions['Forward'] < 1.5:
        print('step3')

        if regions['Right'] < 10:
            angular_z = (regions['Right']-regions['Left'])*FA
            print('step4')

        else:
            angular_z = 0.25
            print('step5')

   else:
        angular_z=0
        print('step6')

   #elif regions['']

   #print(Forward)
   msg.linear.x = linear_x
   msg.angular.z = angular_z
   pub.publish(msg)
   
def main():
    global pub
    rospy.init_node('obs')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, LIDAR)
    rospy.spin()

if __name__ == '__main__':
    main()