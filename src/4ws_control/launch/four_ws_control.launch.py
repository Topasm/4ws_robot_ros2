#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription


import xacro

def generate_launch_description():

    robot_name = "four_ws"
    package_name = robot_name + "_description"
    robot_description = os.path.join(get_package_share_directory(
    package_name), "ros2_control", robot_name + ".ros2_control.xacro")
    robot_description_config = xacro.process_file(robot_description)

    controller_config = os.path.join(
        get_package_share_directory(
            package_name), "config", "controllers.yaml"
    )

    return LaunchDescription([


        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
            output="screen",
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["velocity_controller", "-c", "/controller_manager"],
            output="screen",
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_trajectory_controller", "-c", "/controller_manager"],
            output="screen",
        ),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[
                {"robot_description": robot_description_config.toxml()}],
            output="screen",
        ),
        
        Node(
        package = "joy",
        executable = "joy_node"
        ),


        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        Node(package='four_ws_control', executable='four_ws_control.py', output='screen'),
    ])