import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
	def __init__(self):
		super().__init__('listener')
		self.subscriber = self.create_subscription(String, 'message', self.listener_callback, 10)

	def listener_callback(self, msg):
		self.get_logger().info(f"Recieved {msg.data}")



def main(args=None):
	rclpy.init(args=args)

	listener = Listener()
	rclpy.spin(listener)

	listener.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()