#! /usr/bin/env python3

import rclpy
import cv2
from core_lib.img_capture_module import ImageCaptureNode
import os

def main(args=None):
    rclpy.init(args=args)
    node = ImageCaptureNode()

    # Delete prior images
    path_to_photos = "C:\jhsrobo\img_capture\img"
    if not os.path.exists(path_to_photos):
        os.makedirs(path_to_photos)
    else:
        try: os.system("del {}\other\*.png".format(node.path))
        except: pass
        try: os.system("del {}\coral\*.png".format(node.path))
        except:pass
    
    rclpy.spin(node)

    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
