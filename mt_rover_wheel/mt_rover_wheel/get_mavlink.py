#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 


import time
from pymavlink import mavutil

master = mavutil.mavlink_connection("/dev/ttyACM2", baud=115200)
master.wait_heartbeat()

RC_1=1  # RIGHT MOTOR
RC_2=2 # LEFT MOTOR



class Subscriber(Node):
    def __init__(self):
        super().__init__("joyCommandSubscriber")
        print("started getting data")
        self.create_subscription(Twist,"/cmd_vel",self.getVelocityCallback,10)

    def getVelocityCallback(self,vel :Twist):
        print("Received Linear Velocity"+str(int(vel.linear.x)))
        print("Received Angular Velocity"+str(int(vel.angular.z)))

        # Here main moto is not to move the rover when both command is coming

        if(vel.linear.x!=1500):
            if(vel.angular.z!=1500):
                print("Both of Linear and angualr is coming ,Rover will not move")
            else:
                print("Linaer set_value"+str(int(vel.linear.x)))
                self.set_servo_pwm(RC_1,vel.linear.x)
                self.set_servo_pwm(RC_2,vel.linear.x)
        else:
            if(vel.angular.z==1500):
                print("Both of the are same same,1500 Rover is stop")
            else:
                print("Angular set_value"+str(int(vel.angular.z)))
                if(vel.angular.z>1500):
                    #    want to go right ,left motor will move faster in forward
                    print("right rotation")
                    self.set_servo_pwm(RC_1,1500-(vel.angular.z-1500))
                    self.set_servo_pwm(RC_2,vel.angular.z)
                    print("Left speed :"+str(int(vel.angular.z))+" ,"+ "Right speed:" +str(int(1500-(vel.angular.z-1500))))
                else:
                    #    want to go Left ,right motor will move faster in forward
                    self.set_servo_pwm(RC_1,(1500-vel.angular.z)+1500)
                    self.set_servo_pwm(RC_2,vel.angular.z)
                    print("Left speed :"+str(int(vel.angular.z))+" ,"+ "Right speed:" +str((1500-vel.angular.z)+1500))

    def set_servo_pwm(self,servo_n, microseconds):
        master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        servo_n ,  # servo instance, offset by 8 MAIN outputs
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )
        
        
def main(args=None):
    rclpy.init(args=args)
    node=Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()