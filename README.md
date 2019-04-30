# raw_keyboard_publisher
Generic Keyboard key stroke publisher for ROS2 in Python

Forked and modified from: rohbotics/ros2_teleop_keyboard
url: https://github.com/rohbotics/ros2_teleop_keyboard

#Launch
To run: `ros2 run raw_keyboard_publisher raw_keyboard_publisher`


#Usage
Raw key strokes from the terminal input are published as separate chars to the "/raw_keyboard" topic using the std_msgs/Char messages.

```
Reading from the keyboard and publishing Chars on raw_keyboard topic
--------------------------
CTRL-C to quit
```

