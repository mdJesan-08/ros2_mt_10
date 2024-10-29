#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

#we are using twist messege
from geometry_msgs.msg import Twist 

# we are   importing this for sending data to arduino
import serial
import time

# we are selecting arduino port
port="/dev/ttyACM4"
arduinoData=serial.Serial(port,115200)
time.sleep(1)
##############################

class Subscriber(Node):
    def __init__(self):
        super().__init__("joyCommandSubscriber")
        print("started getting data")
        self.create_subscription(Twist,"/turtle1/cmd_vel",self.getVelocityCallback,10)
        self.create_timer(.001,self.rerturn_value_callBack)

    def getVelocityCallback(self,vel :Twist):
        # cmd=str(velocityMsg.linear.x)+str(velocityMsg.angular.z)
        # cmd+="$"
        # we are mapping from 0 to  5while


        
        # -1----->+4=3 LEFT ROTATE
        #  0----->+4=4  ANGULAR STOP
        #  1----->+4=5  RIGHT ROTATE
        
        cmdLinear=int(vel.linear.x)+1
        cmdAngular=int(vel.linear.z)+4
        # cmd2=int(velocityMsg.linear.z)+3
        # print("linear Speed: " + str(velocityMsg.linear.x))
        # print("Turn Speed: " +str(velocityMsg.angular.z))
        print(cmdLinear)
        print(cmdAngular)
        # print(cmd2)
        # arduinoData.write(cmd.encode())
        
        if(cmdLinear==1):
           
           
        else:
            arduinoData.write(cmdLinear.to_bytes(1,'little'))
    

    def rerturn_value_callBack(self):
        while(arduinoData.in_waiting>0):
            print(arduinoData.readline())
        
def main(args=None):
    rclpy.init(args=args)
    node=Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()