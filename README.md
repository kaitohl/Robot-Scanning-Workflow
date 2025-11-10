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

# IntelRealSense Camera

Follow the link below and install the IntelRealsense ROS2 package on your device.

https://github.com/IntelRealSense/realsense-ros/blob/ros2-master/README.md

You will need to:

* Install the Intel Realsense SDK 2.0
* Install the Intel Realsense ROS2 wrapper

# Traj_script Repo

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

**Step 3:** Open SlicerROS2 by launching the version of Slicer it was built on. If you followed the SlicerROS2 docs properly, the following commands should launch Slicer.
```bash
cd Slicer-SuperBuild-Debug/Slicer-build
./Slicer
```








