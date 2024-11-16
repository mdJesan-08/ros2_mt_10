
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


class JoyListener(Node):

    def __init__(self):
        super().__init__('joy_to_mav')
        self.cmd_vel_pub=self.create_publisher(Twist,"/cmd_vel",10)

        self.subscription = self.create_subscription(Joy,'/joy',self.joy_callback,
            10)


    



        # Adding necessary utility functions here

    def _map(self,current_int,int_min,int_max,out_min,out_max):
        mapped_out =out_min + (current_int-int_min)*(out_max-out_min)/(int_max-int_min)
        return float(mapped_out)




    def joy_callback(self, msg : Joy):
        cmd=Twist()
        print("Current left JoyStick value for -->forward/backward:" +str(msg.axes[1]*1000))
        print("Current Right JoyStick value for --> Rotation:" +str(msg.axes[2]*1000))
        print("Enable ,Right trigger:",str(msg.axes[4]))
        print("Enable ,Left trigger:",str(msg.axes[5]))
        enable=msg.axes[5]
        deadzone=300

        # we are making our default state 1500 as indicates stop always
        # However they has to be float
        cmd.linear.x=1500.0
        cmd.angular.z=1500.0
        if(enable==-1):
            # Note we are scaling it for better readability and usibility

            sacled_linear_pot=msg.axes[1]*1000
            scaled_angular_pot=msg.axes[2]*1000
        

# <--------------------------------------->  
            # Linear movement
            if(sacled_linear_pot>deadzone):
                
                cmd.linear.x=self._map(sacled_linear_pot,300,1000,1500,2200)
                print("Current Forward speed"+str(int(cmd.linear.x)))
            if(sacled_linear_pot<-deadzone):
                # print("forward value",str(linear*1000))
                cmd.linear.x=self._map(sacled_linear_pot,-300,-1000,1500,800)
                print("Current BackWard speed"+str(int(cmd.linear.x)))


# <---------------------------------------> 

            # For Rotational part          
            if(scaled_angular_pot<-deadzone):
                # print("forward value",str(linear*1000))\
                cmd.angular.z=self._map(scaled_angular_pot,-300,-1000,1500,2200)
                print("Current  Right Rotational  speed"+str(int(cmd.angular.z)))
            if(scaled_angular_pot>deadzone):
                # print("forward value",str(linear*1000))
                cmd.angular.z=self._map(scaled_angular_pot,300,1000,1500,800)
                print("Current Left Rotational speed"+str(int(cmd.angular.z)))

# <---------------------------------------> 

        self.cmd_vel_pub.publish(cmd)
    


def main(args=None):
    rclpy.init(args=args)
    joy_listener = JoyListener()
    rclpy.spin(joy_listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
