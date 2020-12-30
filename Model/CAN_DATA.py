import numpy as np

class CAN_Data_Obstacle:
    '''障碍物坐标向量'''
    Ped_X = np.zeros(64)
    Ped_Y = np.zeros(64)
    Veh_X = np.zeros(64)
    Veh_Y = np.zeros(64)
    Veh_Relative_Vel_X = np.ones(64)*(1000)
    Veh_Cut_State = ['Undefined']*64
    '''障碍物报文ID'''
    CAN_Obstacle_TotalInf_ID = np.array([0x738])
    CAN_Obstacle_A_ID = np.array([0x739, 0x73c, 0x73f, 0x742, 0x745, 0x748, 0x74b, 0x74e, 0x751, 0x754])
    CAN_Obstacle_B_ID = np.array([0x73a, 0x73d, 0x740, 0x743, 0x746, 0x749, 0x74c, 0x74f, 0x752, 0x755])
    CAN_Obstacle_C_ID = np.array([0x73b, 0x73e, 0x741, 0x744, 0x747, 0x74a, 0x74d, 0x750, 0x753, 0x756])
    # CAN_Obstacle_ID = np.insert(CAN_Obstacle_ID, CAN_Obstacle_ID.shape[0], [x, y, z], axis=0)#增加报文[x, y, z]
    '''n行 x 3列的矩阵，每行对应一个障碍物的的三个报文,第0列包含障碍物的类型和位置信息'''
    CAN_Obstacle_ID = np.transpose(np.array([CAN_Obstacle_A_ID, CAN_Obstacle_B_ID, CAN_Obstacle_C_ID]))
    def __init__(self):
        pass

class CAN_Data_Lane:
    '''车道线参数向量'''
    # Lane_C0 = np.zeros(4).reshape(4,1)
    # Lane_C1 = np.zeros(4).reshape(4,1)
    # Lane_C2 = np.zeros(4).reshape(4,1)
    # Lane_C3 = np.zeros(4).reshape(4,1)
    # Lane_X = np.zeros([4, 50])
    # Lane_Y = np.zeros([4, 50])


    '''车道线报文ID'''
    CAN_Ego_Left_Lane_ID = [0x766, 0x767]
    CAN_Ego_Right_Lane_ID = [0x768, 0x769]

    # CAN_Ego_Lane_Reference_Point_ID = [0x76a]
    # CAN_Number_Of_Next_Lane_ID = [0x76b]
    '''旁白车道线的ID，不用'''
    CAN_Next_Left_Lane0_ID = [0x76c, 0x76d]
    # CAN_Next_Left_Lane1_ID = [0x770, 0x771]
    # CAN_Next_Left_Lane2_ID = [0x774, 0x775]
    # CAN_Next_Left_Lane3_ID = [0x778, 0x779]

    CAN_Next_Right_Lane0_ID = [0x76e, 0x76f]
    # CAN_Next_Right_Lane1_ID = [0x772, 0x773]
    # CAN_Next_Right_Lane2_ID = [0x776, 0x777]
    # CAN_Next_Right_Lane3_ID = [0x77a, 0x77b]

    CAN_LANE_ROAD_EDGE_ID = [0x77c, 0x77d, 0x77e, 0x77f]
    def Clear(self):
        self.Lane_C0 = np.zeros(4).reshape(4,1)
        self.Lane_C1 = np.zeros(4).reshape(4,1)
        self.Lane_C2 = np.zeros(4).reshape(4,1)
        self.Lane_C3 = np.zeros(4).reshape(4,1)
        self.Lane_X = np.zeros([4, 50])
        self.Lane_Y = np.zeros([4, 50])
        pass
        
    def __init__(self):
        pass
        self.Lane_C0 = np.zeros(4).reshape(4,1)
        self.Lane_C1 = np.zeros(4).reshape(4,1)
        self.Lane_C2 = np.zeros(4).reshape(4,1)
        self.Lane_C3 = np.zeros(4).reshape(4,1)
        self.Lane_X = np.zeros([4, 50])
        self.Lane_Y = np.zeros([4, 50])

class CAN_Data_Vehicle:
    '''车辆和Mobileye系统信号'''
    Vehicle_State = [0x700, 0x760]

    def __init__(self):
        pass

class CAN_DATA_TSR:

    CAN_TSR_ID = np.array([0x720, 0x721, 0x722, 0x723, 0x724, 0x725, 0x726])
    CAN_VISION_ONLY_TSR_CONTINUOUS = np.array([0x727])
 
    def __init__(self):
        self.Sign_Position_X = np.zeros(7)
        self.Sign_Position_Y = np.zeros(7)
        self.Sign_Position_Z = np.zeros(7)


class CAN_DATA_TFL:

    CAN_TSR_ID = np.array([0x712, 0x713, 0x714, 0x715, 0x716, 0x717, 0x718, 0x719, 0x71a])
 
    def __init__(self):
        pass