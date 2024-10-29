import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoyListener(Node):

    def __init__(self):
        super().__init__('joy_listener')
        self.cmd_vel_pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)

        self.subscription = self.create_subscription(Joy,'/joy',self.joy_callback,
            10)






    def joy_callback(self, msg : Joy):
        cmd=Twist()
        print("left JoyStick forward/backward:" +str(msg.axes[1]*1000))
        print("Right JoyStick Rotation:" +str(msg.axes[2]*1000))
        print("Enable ,Right trigger:",str(msg.axes[4]))
        print("Enable ,Left trigger:",str(msg.axes[5]))
        enable=msg.axes[5]
        deadzone=300
        # linear=msg.axes[1]
        # angular=msg.axes[2]
        cmd.linear.x=0.0
        cmd.linear.z=0.0
        if(enable==-1):
            linear=msg.axes[1]
            angular=msg.axes[2]
        

# <--------------------------------------->  
            # Linear movement
            if(linear*1000>deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.x=1.0
                print("Forward")
            if(linear*1000<-deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.x=-1.0
                print("Backward")


# <---------------------------------------> 

            # For Rotational part          
            if(angular*1000<-deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.z=1.0
                print("Rotate Right")
            if(angular*1000>deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.z=-1.0
                print("Rotate Left")

# <---------------------------------------> 

            if(abs(linear*1000)< deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.x=0.0
                print(linear)
                print("linear Stop")
                # print(cmd.linear.x)
            if(abs(angular*1000)< deadzone):
                # print("forward value",str(linear*1000))
                print(angular)
                cmd.linear.z=0.0
                print("Angular Stop")
                # print(cmd.linear.x)


            print("Linear Value is : "+str(cmd.linear.x))
            print("Angular Value is : "+str(cmd.linear.z))


            #Rotational Movement
            # if(abs(angular*1000)>threshold):
            #     print("Angular value",str(angular*1000))
            #     if(angular>0):
            #         cmd.angular.z=1.0
            #     else:
            #         cmd.angular.z=-1.0



            
        self.cmd_vel_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    joy_listener = JoyListener()
    rclpy.spin(joy_listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
