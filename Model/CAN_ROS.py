import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image

class Ros_Data_Sub():

    def __init__(self, topic_pub, topic_sub):
        # self.
        self.topic_pub = topic_pub
        self.topic_sub = topic_sub

        self.__pub_ = rospy.Publisher(self.topic_pub, Image, queue_size)
        self.__sub_ = rospy.Subscriber(self.topic_sub, Image, self.callback)
        pass


    def callback(self, data):
        # rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
        obj_toPub = Image()
        self.__pub_.publish(obj_toPub)

    def listener(self):
        pass
        

class Can_Data_Sub():

    def __init__(self):
        pass

def main():
    rospy.init_node("test_node", anonymous=True)
    SubObj = Ros_Data_Sub("/test_pub", "/usb_cam/image_raw")
    rospy.spin()


if __name__ == '__main__':

    main()
