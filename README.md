# Neato-Turtle-Extras
Extra files that are useful to run with the Neato Turtle robot described by the cpeavy2/botvac_node. https://github.com/cpeavy2/botvac_node/tree/main 

The launch files in this repository are intended to be run on the SBC (Single Board Computer) Raspberry Pi Controller. 

1) Launch Webcam such as Logitech C270 with the ros-drivers/usb_cam 

2) Launch botvac_node to connect with the Neato Botvac device1)

3) Launch botvac_node and usb_webcam

To install this repository on the SBC, either from the SBC connected Monitor or ssh into the SBC from the Remote Desktop:

1) In the SBC Home (~/) directory , configure a colcon workspace with a src directory that has a different name than the one used by the botvac_node workspace. The example used here is ~/dev2_ws/src

