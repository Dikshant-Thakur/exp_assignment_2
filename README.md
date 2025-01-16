
https://github.com/user-attachments/assets/b835a7b5-493d-42aa-85c6-36d9961123f6


![Image](https://github.com/user-attachments/assets/f0d7fa62-d998-495b-8687-814cfc34e248)



# Assignment 2 ROS Package

This repository contains the ROS 2 package developed for Assignment 2, which enables a mobile robot to autonomously navigate to the waypoint corresponding to the lowest ID marker in a predefined environment.


## Overview
The goal of this project is to use a mobile robot equipped with a camera and laser scanner and it needs to visit 4 waypoints. At each waypoint, it will use its camera to detect visual markers (e.g., ArUco markers). The robot will check the marker IDs at all waypoints and identify the smallest ID. Finally, it will navigate to the waypoint linked to the smallest ID. The robot will use PlanSys2 for this process.

## Prerequisites
The following tools and dependencies are required:
- ROS 2 Humble
- Gazebo (for simulation)
- Rviz (for visualization)
- SLAM Toolbox (for mapping and localization)
- Nav2 (for navigation)
- PlanSys2 (for task planning)

## Installation
You can also install PlanSys2, Nav2, and SLAM Toolbox using apt-get, but some parameters may need to be changed. Therefore, it is recommended that you use the provided packages.
## Usage
Run these commands in order:
1. Launch simulation (Gazebo + Rviz):
```bash
ros2 launch assignment_2 assignment_2.launch.py
```
2. Start SLAM Toolbox for mapping:
```bash
ros2 launch slam_toolbox online_sync_launch.py
```
3. Launch Nav2 for navigation:
```bash
ros2 launch nav2_bringup navigation_launch.py
```
4. Start PlanSys2 server and nodes:
``` bash
ros2 launch plansys2_patrol_navigation_example patrol_example_fakesim_launch.py
```
5. To initialize the problem, and implement a FSM.
``` bash
ros2 run plansys2_patrol_navigation_example patrolling_controller_node
```
6. To run the Arurco script, from which the robot uses the OpenCV library to detect the marker
 ``` bash
ros2 run experimental exp2.py
```

## Note
- Occasionally, the navigation server may crash during execution.  
- If this happens:  
  - Turn off all running nodes and processes.  
  - Restart the entire setup from the beginning.
  - Try to modify the marker points. 

- Ensure that all commands are executed in the specified sequence to avoid errors.





