#! /usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 
from statistics import mean
pub = None

def LIDAR(msg):

    Trim1 = np.trim_zeros(np.asarray(msg.ranges[40:90]))
    Trim2 = np.trim_zeros(np.asarray(msg.ranges[0:40]))
    Trim3 = np.trim_zeros(np.asarray(msg.ranges[270:320]))
    Trim4 = np.trim_zeros(np.asarray(msg.ranges[320:360]))

    #Right = min(Trim1)
    #Forward = min(Trim2)
    #Left = min(Trim3)

    Right = mean(Trim1)
    Forward1 = mean(Trim2)*0.6
    Forward2 = mean(Trim4)*0.6
    Left = mean(Trim3)

    vel = Twist()

    #linear_x = 0.0 
    #angular_z = 0
    #FL = 0.005
    #FL2 = 0.2
    #FA = 0.46


    if 1 < Forward1 or 1 < Forward2:
       #linear_x = 0.08
       #angular_z = 0
       #print('step1')

       if Right > 0.5 or Left > 0.5:
        linear_x = 0.08
        angular_z = 0
        print('step1')

       elif Right > Left:
        linear_x = 0
        angular_z = 0.5
        print('step2')

       elif Left > Right:
        linear_x = 0
        angular_z = -0.5
        print('step3')

    elif 1 > Forward1 or 1 > Forward2:

       if Right > Left:
        linear_x = 0
        angular_z = 0.5
        print('step4')

       elif Left > Right:
        linear_x = 0
        angular_z = -0.5
       print('step5')           




   #elif regions['']
    #print(Trim1)
    #print(Forward1)
    print(linear_x)
    print(angular_z)
    print(Forward1)
    print(Forward2)
    print(Left)
    print(Right)
    vel.linear.x = linear_x
    vel.angular.z = angular_z
    pub.publish(vel)
    #pub.publish(msg)
   
def main():
    global pub
    rospy.init_node('obs')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, LIDAR)
    rospy.spin()

if __name__ == '__main__':
    main()