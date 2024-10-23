#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
# pura kahina ta oop based jeita korte amra Alhamdulillah ov vosto

class MyNode(Node):

    def  __init__(self):
        # super() is method  bro ,
        # don't use it as a object super()
        super().__init__("first_node")
        # constructor call   hoar somoy e call hobe
        self.counter=0
        self.create_timer(1,self.timer_callback)
        print("Ami      kokhon    print hobo")

    def timer_callback(self):
        data="hello from callback "+str(self.counter)
        print(data)
        self.counter+=1

# <------------------------------->

def main(args=None):
    # kisu korar age communication build up koro,which is a must
    rclpy.init(args=args)
    # r hoilo ai args tar args e function r args gula k pass korabe

    node=MyNode()
    rclpy.spin(node)
    # sobar last e node tare shutdown korao aita korba soabr age
    rclpy.shutdown()

# <------------------------------->

# __name__=='__main__' r alada mahotto     ase oit amra dekhbo insAllah pore 
if  __name__=='__main__':
    main()
