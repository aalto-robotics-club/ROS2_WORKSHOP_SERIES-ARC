#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class ScanDirectionReader(Node):
    def __init__(self):
        super().__init__('scan_direction_reader')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('Listening to /scan...')

    def scan_callback(self, scan: LaserScan):
        # The LaserScan message contains an array of distance readings (scan.ranges).
        # Each index corresponds to an angle:
        #   index = round((target_angle - scan.angle_min) / scan.angle_increment)
        #
        # Compute the index for each direction (front=0°, left=90°, right=270°, behind=180°)
        # then read the distance from scan.ranges at each index.
        ### YOUR code here

        # Log all four distances.
        ### YOUR code here
        pass


def main(args=None):
    rclpy.init(args=args)
    node = ScanDirectionReader()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
