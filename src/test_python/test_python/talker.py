import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher = self.create_publisher(String, 'message', 10)
        timer_period = '0.5'
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello world {self.i}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Published {msg.data}")
        self.i +=1


def main(args=None):
    # print('Hi from test_python.')
    rclpy.init(args=args)

    talker = Talker()
    rclpy.spin(talker)

    talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
