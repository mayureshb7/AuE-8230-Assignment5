
This files describes running Obstacle Avoidance and Wallfollowing of a Turtlebot3 Burger on Gazebo and Obstacle Avoidance by Turtlebot3 Burger in real world

	1) Wall Following - Gazebo
		a) Launch command: roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_wallfollowing.launch
		b) After launching the file, wall following world will be established in Gazebo, 
		Turtlebot3 burger model will be placed at x,y,z=0 coordinates in gazebo and turtlebot3 burger will run on python code wall_follower.py
		c) The Turtlebot3 burger LIDAR Senses the wall distance within the specified range and navigates itself to maintain a specific distance to whe wall.
		d) P controller has been implemented in linear velocity as well as angular velocity
	
	2) Obstacle Avoidance - Gazebo
		a) Launch command: roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_obstacleavoidance.launch
		b) After launching the file, Obstacle world will be established in Gazebo,
		Turtlebot3 Burger will be placed at x,y,z=0 coordinates in gazebo and turtlebot3 burger will run on python code wander.py
		c) The Turtlebot3 burger LIDAR Senses the obstacle distance within the specified range and navigates itself to avoid the obstacles.
		d) P controller has been implemented in linear velocity as well as angular velocity
		
	3) Obstacle Avoidance - Real World 
	To implement obstacle avoidance in real world following commands should be followed on terminal:
		a) Connect/SSH into turtlebot burger3 model
		b) Make sure to run Roscore on ubuntu and check if IP address in ubuntu and pi are correct to establish a successfull connection: ssh ubuntu@{IP ADDRESS OF PI)
		c) Bring-up the turtlebot by using command on pi: roslaunch turtlebot3_bringup turtlebot3_robot.launch
		d) run python code by using command rosrun assignment5_wallfollowingandobstacleavoidance wander1.py for real world obstacle avoidance
	
	Refer to videos for demonstration of above tasks from assignment5_wallfollowingandobstacleavoidance/videos
