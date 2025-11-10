# Robot Scanning Workflow

Tested on:

* Ubuntu 22.04.5 LTS (Jammy)
* ROS2 Humble

## What You Need

1. Mycobot 280 M5
2. IntelRealSense Camera
3. Phatom to scan on
4. SlicerROS2
5. Traj_scripts repo

## Installation

### IntelRealSense Camera

Follow the link below and install the IntelRealsense ROS2 package on your device.

https://github.com/IntelRealSense/realsense-ros/blob/ros2-master/README.md

You will need to:

* Install the Intel Realsense SDK 2.0
* Install the Intel Realsense ROS2 wrapper

### Traj_script Repo

## Setup

**Step 1:** Source your ROS2 environment if it hasn't been done automatically.
```bash
source /opt/ros/humble/setup.bash
```
**Step 2:** Run the following command to enable pointcloud vizualization and depth alignment for the IntelRealSense camera
```bash
ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true align_depth.enable:=true
```
**Step 2.1:** (Optional) To vizualize the video, pointcloud, and depth output, open rviz2 with the following command
```bash
ros2 run rviz2 rviz2
```
Once rviz2 opens, you can display the video, depth, and pointcloud output. To display the outputs, select the "Add" button, and select "Topics" tabs. Select the topics you wish to display on this page.

**Step 3:** We need to allow the robot to be in follow mode to register the point cloud to the robot. Run the following commands to allow follow mode for the robot.
```bash
cd ros2_cobot
colcon build
source install/setup.bash
sudo chmod 777 /dev/ttyACM0
ros2 launch mycobot_280 mycobot_follow.launch.py
```
**Step 4:** Open SlicerROS2 by launching the version of Slicer it was built on. If you followed the SlicerROS2 docs properly, the following commands should launch Slicer.
```bash
source /home/robotics/ros2_cobot/install/setup.bash
cd Slicer-SuperBuild-Debug/Slicer-build
./Slicer
```
**Step 5:** Navigate to the ROIScan module and connect to ``/camera/camera/depth/color/points`` topic. Once succesful, extract point cloud. Make sure to select the center view to see the point cloud nicely.

**Step 6:** After extracting the point cloud, navigate to the ROS2 module, and load your robot in. It will load in at a random spot.

**Step 7:** Now you are ready for fiducial registration.










