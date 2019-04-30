import rclpy
import sys, select, termios, tty

from rclpy.qos import qos_profile_default
from std_msgs.msg import Char

settings = termios.tcgetattr(sys.stdin)

msg = """
Reading from the keyboard and publishing Chars on raw_keyboard topic
--------------------------
CTRL-C to quit
"""

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def main(args=None):
	rclpy.init()
	node = rclpy.create_node('raw_keyboard_publisher')
	pub = node.create_publisher(Char, 'raw_keyboard')

	try:
		print(msg)
		while(1):
			key = getKey()
			if (key == '\x03'):
				break
			char = Char()
			char.data = key
			pub.publish(char)

	except:
		print("exception")
		print(e)

	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
