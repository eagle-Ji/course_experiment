# ROS Reinforcement Learning Node

This repository contains a ROS (Robot Operating System) node implementation for controlling a differential drive robot using a basic reinforcement learning (RL) framework. The node publishes velocity commands to the robot and processes sensor data such as LaserScan and Odometry. The code is designed to be used with ROS 2.

## Project Overview

The RL node is designed to:

- Publish velocity commands (`Twist` messages) to control the robot's movement.
- Optionally subscribe to sensor topics such as `LaserScan` for obstacle detection and `Odometry` for localization.
- The node can be extended to integrate a reinforcement learning agent for intelligent control, but as of now, it sends constant velocity commands for basic movement.

## Code Explanation

### RL_NODE_CLASS

The core class `RL_NODE_CLASS` is a subclass of `rclpy.node.Node`, representing the ROS node in Python. The following components are implemented:

- **Publisher (`vel_pub`)**: A publisher to the topic `/diff_cont/cmd_vel_unstamped` which sends `Twist` messages. These messages are used to control the robot's linear and angular velocity.
  
- **Timer (`self.timer`)**: The timer triggers the `publish_twist` function every 0.2 seconds to continuously send velocity commands to the robot.

- **Subscriptions (commented out)**: The node has the option to subscribe to `LaserScan` and `Odometry` topics, but this part is currently commented out. When uncommented, it will allow the node to receive laser scan data (for obstacle detection) and odometry data (for robot position tracking).
  
  - `scan_callback`: Placeholder function for processing laser scan data.
  - `odom_callback`: This function prints the robot's `x` and `y` position (from the Odometry message) every time a new Odometry message is received.

### `publish_twist` Method

This method publishes a fixed `Twist` message every 0.2 seconds. The message sets the following robot velocities:

- **Linear velocity (x-axis)**: 0.2 m/s
- **Linear velocity (y-axis)**: 0.0 m/s (no movement in the y-direction)
- **Angular velocity (z-axis)**: 0.1 rad/s (gentle rotation)

This function is called periodically by the timer to continuously control the robot’s movement.

### `scan_callback` Method

Currently, this is a placeholder for processing `LaserScan` messages. The function is designed to be expanded later with logic to process sensor data for obstacle detection or other RL-related tasks.

### `odom_callback` Method

This method processes Odometry messages. It prints the robot's `x` and `y` coordinates based on the received Odometry data. The position is rounded to three decimal places.

### `main` Method

- Initializes the ROS 2 communication system with `rclpy.init()`.
- Creates an instance of the `RL_NODE_CLASS` node.
- Starts the ROS event loop with `rclpy.spin()`, keeping the node alive and handling messages.
- Shuts down the ROS communication system when the node is destroyed.

## Installation

1. **Install ROS 2**: Follow the [ROS 2 installation guide](https://docs.ros.org/en/foxy/Installation.html) for your operating system.

2. **Install dependencies**:
   Make sure to have the necessary ROS 2 packages for working with messages like `geometry_msgs`, `sensor_msgs`, and `nav_msgs`. You can install them using:

   ```bash
   sudo apt-get install ros-foxy-geometry-msgs ros-foxy-sensor-msgs ros-foxy-nav-msgs

   # ROS Reinforcement Learning Node

## Installation Instructions

### 1. Clone the Repository

Clone this repository into your ROS 2 workspace's `src` directory:

```bash
cd ~/ros2_ws/src
git clone https://github.com/eagle-Ji/course_experiment.git

cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash
ros2 launch <your_launch_file>
ros2 run <your_package_name> rl_node_class
