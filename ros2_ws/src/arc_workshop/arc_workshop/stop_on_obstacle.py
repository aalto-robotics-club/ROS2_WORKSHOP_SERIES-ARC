#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class StopOnObstacle(Node):
    def __init__(self):
        super().__init__('stop_on_obstacle')

        self.stop_distance = 0.3  # meters

        self.scan_subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        # Create a publisher to send velocity commands on /cmd_vel.
        # Arguments: message type, topic name, queue size
        self.cmd_vel_publisher = self.create_publisher(
            ### YOUR code here
        )

        self.get_logger().info('Stop-on-obstacle node started.')

    def scan_callback(self, scan: LaserScan):
        front_index = int(round((0.0 - scan.angle_min) / scan.angle_increment))
        front_distance = scan.ranges[front_index]

        if front_distance < self.stop_distance:
            # Build a Twist message with all zeros to stop the robot,
            # then publish it on /cmd_vel.
            stop_msg = Twist()
            ### YOUR code here  (hint: set linear and angular fields to 0.0)

            self.cmd_vel_publisher.publish(stop_msg)
            self.get_logger().warn(
                f'Obstacle in front: {front_distance:.3f} m. Stopping robot.'
            )
        else:
            self.get_logger().info(
                f'Front clear: {front_distance:.3f} m'
            )


def main(args=None):
    rclpy.init(args=args)
    node = StopOnObstacle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
