#! usr/bin/env python3

import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import os

class CameraFeedNode(Node):
    def __init__(self):
        super().__init__("camera_feed")
        self.log = self.get_logger()
        self.log.info("This is the image capture node.")

        # Global Variables
        self.path =  "/home/jhsrobo/ROVMIND/ros_workspace/src/img_capture/img"
        self.count = 1
        self.coralCount = 1
        self.coralMode = False
        self.bridge = CvBridge()

        # Subscribers
        self.camera_subscriber = self.create_subscription(Image, "screenshots", self.img_callback, 10)

    def img_callback(self, screenshot):
        img = self.bridge.imgmsg_to_cv2(screenshot, desired_encoding="passthrough")
        #if self.coralMode:
         #   cropped_img = img[30:720, 0:880]
          #  cv2.imwrite("{}/coral/{}.png".format(self.path, self.coralCount), cropped_img)
          #  self.coralCount += 1
        #else:
        cv2.imwrite("{}/{}.png".format(self.path, self.count), img)
        self.count +=  1

def main(args=None):
    rclpy.init(args=args)
    node = CameraFeedNode()

    # Delete prior images
    try: os.system("rm {}/*.png".format(node.path))
    except: pass
    try: os.system("rm {}/coral/*.png".format(node.path))
    except:pass
        
    rclpy.spin(node)

    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()