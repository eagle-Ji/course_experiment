import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TwistStamped
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import numpy as np
TwistStamped
class RL_NODE_CLASS(Node):
    def __init__(self):
        super().__init__('rl_node_class')
        self.vel_pub = self.create_publisher(Twist, '/diff_cont/cmd_vel_unstamped', 10)
        self.timer = self.create_timer(0.2, self.publish_twist)
        # self.sub_scan = self.create_subscription(
        #     LaserScan,
        #     '/scan',
        #     self.scan_callback,
        #     10)
        # self.sub_scan
        # self.sub_odom = self.create_subscription(
        #     Odometry,
        #     '/odom',
        #     self.odom_callback,
        #     10)
        # self.sub_odom

    def publish_twist(self):
        twist_msg =  Twist() #TwistStamped() #Twist()
        twist_msg.linear.x = 0.2
        twist_msg.linear.y = 0.0
        twist_msg.angular.z = 0.1
        # twist_msg.twist.linear.x = 0.2
        # twist_msg.twist.linear.y = 0.0
        # twist_msg.twist.angular.z = 0.1
        self.vel_pub.publish(twist_msg)
        print(twist_msg)
    def scan_callback(self, msg):
        pass 
    def odom_callback(self, msg):
        print("x, y  ::" + str(round(msg.pose.pose.position.x, 3)) + "   " + str(round(msg.pose.pose.position.y, 3)))

        #print(msg.ranges)


def main(args=None):
    rclpy.init(args=args)
    node = RL_NODE_CLASS()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()