# Neato-Turtle-Extras
Extra files that are useful to run with the Neato Turtle robot described by the cpeavy2/botvac_node. https://github.com/cpeavy2/botvac_node/tree/main 

1) Cheatsheet (txt file for cutting and pasting into Terminal Command Line) for Installing Neato Turtle code from repositories, written for Raspberry Pi 3, 4, Zero 2 W SBC Robot and Linux Remote Desktop Computer.

2) Cheatsheet for Launching and Running the Neato Turtle.
3) Like 1) but for Server version of the SBC Robot Raspberry Pi.

4) PowerPoint Presentation pdf File "Introduction-to-ROS-with Neato-Turtle.pdf"

5) Config & Launch files for a USB Camera in this repository are intended to be run on the SBC (Single Board Computer) Raspberry Pi Controller. 

5.1) Launch Webcam such as Logitech C270 with the ros-drivers/usb_cam 

5.2) Launch botvac_node to connect with the Neato Botvac device1)

5.3) Launch botvac_node and usb_webcam

5.4) To install this repository on the SBC, either from the SBC connected Monitor or ssh into the SBC from the Remote Desktop:

5.5) In the SBC Home (~/) directory , configure a colcon workspace with a src directory that has a different name than the one used by the botvac_node workspace. The example used here is ~/dev2_ws/src

