# ros2_robot_controller


ros2 로 로봇 제어하기 위한 레포


개발환경 : ubuntu 22.04
SBC : Orange Pi
Ros Version : Ros2 Humble



개발 계획:


1. U2D2 로 회전제어
2. vesc 와 연동
And so on..


## dependencies
sudo apt-get install ros-humble-dynamixel-sdk

pip install setuptools==58.2.0


example launch code

ros2 launch teleop_twist_joy teleop.launch.py joy_config:='rosbot_xbox_bluetooth' cmd_vel:=/diff_drive_controller/cmd_vel_unstamped
sudo chmod a+rw /dev/ttyUSB0 
