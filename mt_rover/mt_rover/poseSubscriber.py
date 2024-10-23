#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from turtlesim.msg import Pose

class Subscriber(Node):
    def __init__(self):
        super().__init__("poseSubscriber")
        print("started getting data")
        self.pose_subscriber=self.create_subscription(Pose,"/turtle1/pose",self.poseCallback,10)
    def poseCallback(self,msg :Pose):
        print(msg)

        
def main(args=None):
    rclpy.init(args=args)
    node=Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()