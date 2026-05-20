#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelReader(Node):
    def __init__(self):
        super().__init__('cmd_vel_reader')

        # Create a subscription to the /cmd_vel topic.
        # Arguments: message type, topic name, callback, queue size
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            ### YOUR code here  (hint: name of the callback method below)
            10
        )

        self.get_logger().info('Listening to /cmd_vel...')

    def cmd_vel_callback(self, msg: Twist):
        # msg is a Twist message with two fields:
        #   msg.linear  -> Vector3 (x, y, z)
        #   msg.angular -> Vector3 (x, y, z)
        #
        # Log the received linear and angular velocities.
        ### YOUR code here
        pass


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
