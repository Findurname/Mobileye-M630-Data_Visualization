import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import threading
import qdarkstyle
import rospy
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


class Camera_Version(QWidget):
    Vedio_Running_Indicator = 'No'
    Vedio_Recording_Indicator = 'No'
    Vedio_Save_Path = ''
    '''每Vedio_Number帧保存一个视频'''
    Record_Vedio_Counter = int(0)
    Vedio_Number = 90000#一个小时保存一个视频
    def __init__(self, parent = None):
        super(Camera_Version, self).__init__(parent)
        self.SetUI()

    def SetUI(self):
        self.resize(444,250)
        self.setWindowTitle('Camera Version')
        self.FixedHeight = 30
        self.Font = QFont()
        self.Font.setPixelSize(18)

        self.Vedio_Winndow = QLabel()
        self.Vedio_Winndow.setFixedSize(444,250)
        self.Vedio_Winndow.setScaledContents (True)#让图片自适应大小
        self.init_image = QPixmap('./Pic/No_Video.jpg')
        self.Vedio_Winndow.setPixmap(self.init_image)
        # self.image = Image()
        # self.image_np = np.zeros((1200, 1920, 3), dtype=np.uint8)
        self.bridge = CvBridge()
        layout = QVBoxLayout()
        layout.addWidget(self.Vedio_Winndow)
        self.setLayout(layout)
 

    def Image_Cb(self, img_msg):
        # np_arr = np.frombuffer(img_msg.data, np.uint8)
        # self.image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        # image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        # self.image_np = np.copy(image)
        # while np_arr.any() != 0:
        # frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        # img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        # self.Vedio_Winndow.setPixmap(QPixmap.fromImage(img))
            # print("image: ", self.image_np.shape)
            # print(self.image_np)
        # pass
 
        frame = self.bridge.imgmsg_to_cv2(img_msg, "passthrough")
        # frame = self.bridge.compressed_imgmsg_to_cv2(img_msg, "passthrough")
        # frame = cv2.resize(frame, (444, 250), interpolation = cv2.INTER_AREA)
        img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.Vedio_Winndow.setPixmap(QPixmap.fromImage(img)) 
        # print(type(frame))
        # print(type(frame[0][0][0]))
        # print(frame.shape)
        # if frame.any() != 0:
            # cv2.imshow("Imshow", frame)
            # cv2.waitKey(3)
    def Open_Vedio_Initial(self):
        # url = "rtsp://192.168.1.10:554/user=admin&password=admin&channel=1&stream=0.sdp?"
        # self.cap = cv2.VideoCapture(url)

        # self.cap = cv2.VideoCapture(0)
        # print(type(self.cap))
        # rospy.init_node("View_ROS", anonymous=True)
        # rospy.Subscriber('/usb_cam/image_raw/compressed', CompressedImage, self.Image_Cb)
        # rospy.Subscriber('/can_first', can_info, self.Can_Cb)
        pass

    def Timer_Start(self):
        print("Timer_Start...")
        threading.Thread(target=self.Vedio_Show_Ros).start()
        pass

    def Record_Vedio_Initial(self,Vedio_Save_Path):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')#('M', 'P', '4', '2')
        '''主程序调用这个函数的时候，会把路径信息传递进来，这样就可以在这个界面里面读取到路径信息了'''
        if self.Record_Vedio_Counter == 0:
            self.Path = Vedio_Save_Path
        else:
            pass
        self.out = cv2.VideoWriter(Vedio_Save_Path + '.avi', fourcc, 25.0, (1280, 720))

    def Vedio_Show(self):
        while self.cap.isOpened():
            if self.Vedio_Running_Indicator == 'No':
                self.Close_Vedio()#这个release放在这里，不然界面会卡死
                break
            else:
                ret, frame0 = self.cap.read()
                frame = cv2.cvtColor(frame0, cv2.COLOR_RGB2BGR)
                # print(type(frame))
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.Vedio_Winndow.setPixmap(QPixmap.fromImage(img))
                if self.Vedio_Recording_Indicator == 'Yes':
                    self.out.write(frame0)
                    self.Record_Vedio_Counter += 1
                    if (self.Record_Vedio_Counter % self.Vedio_Number) == 0:
                        self.out.release()
                        index = int(self.Record_Vedio_Counter/self.Vedio_Number)
                        self.Record_Vedio_Initial(self.Path + '_'+str(index))
                elif self.Vedio_Recording_Indicator == 'Save':
                    self.Save_Vedio()
                else:
                    pass

                    '''waitKey(1)等待1ms，接收一个事件；waitKey(0)无限等待,如果有事件类的判断就可以不需要这个
                    ，需要加事件类判断来中断一下read()，不然帧读取会卡死'''
                    # cv2.waitKey(1)
    def Vedio_Show_Ros(self):

        # rospy.Subscriber('/usb_cam/image_raw/compressed', CompressedImage, self.Image_Cb)
        rospy.Subscriber('/usb_cam/image_raw', Image, self.Image_Cb)
        # frame = cv2.cvtColor(self.image_np, cv2.COLOR_RGB2BGR)
        # # print("----------------Vedio_Show_Ros")
        
        # # print(self.image_np)
        # # frame = self.image_np
        # # print(frame)
        # # print("frame: ", frame.shape)
        # img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        # self.Vedio_Winndow.setPixmap(QPixmap.fromImage(img))
        if self.Vedio_Recording_Indicator == 'Yes':
            self.out.write(frame0)
            self.Record_Vedio_Counter += 1
            if (self.Record_Vedio_Counter % self.Vedio_Number) == 0:
                self.out.release()
                index = int(self.Record_Vedio_Counter/self.Vedio_Number)
                self.Record_Vedio_Initial(self.Path + '_'+str(index))
        elif self.Vedio_Recording_Indicator == 'Save':
            self.Save_Vedio()
        else:
            pass

            '''waitKey(1)等待1ms，接收一个事件；waitKey(0)无限等待,如果有事件类的判断就可以不需要这个
            ，需要加事件类判断来中断一下read()，不然帧读取会卡死'''
            # cv2.waitKey(1)
    def Save_Vedio(self):
        self.out.release()
        self.Record_Vedio_Counter = int(0)
        self.Vedio_Recording_Indicator = 'No'

    def Close_Vedio(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.Vedio_Winndow.setPixmap(self.init_image)
        self.Record_Vedio_Counter = int(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win = Camera_Version()
    win.Open_Vedio_Initial()
    win.Timer_Start()
    win.show()
    sys.exit(app.exec_())

