數據結構說明
================

.. toctree:: 
    :maxdepth: 5

關節位置數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 關節位置數據類型 
    */  
    public class JointPos
    {
      double J1;
      double J2;
      double J3;
      double J4;
      double J5;
      double J6;

      public JointPos(double j1, double j2, double j3, double j4, double j5, double j6)
      {
        J1 = j1;
        J2 = j2;
        J3 = j3;
        J4 = j4;
        J5 = j5;
        J6 = j6;
      }

      public JointPos()
      {

      }
    }

笛卡爾空間位置數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡爾空間位置數據類型
    */
    public class DescTran
    {
      public double x = 0.0;    /* x軸座標，單位mm  */
      public double y = 0.0;    /* y軸座標，單位mm  */
      public double z = 0.0;    /* z軸座標，單位mm  */
      public DescTran(double posX, double posY, double posZ)
      {
        x = posX;
        y = posY;
        z = posZ;
      }

      public DescTran()
      {

      }

    }

歐拉角姿態數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 歐拉角姿態數據類型
    */
    public class Rpy
    {
      public double rx = 0.0;   /* 繞固定軸X旋轉角度，單位：deg  */
      public double ry = 0.0;   /* 繞固定軸Y旋轉角度，單位：deg  */
      public double rz = 0.0;   /* 繞固定軸Z旋轉角度，單位：deg  */
      public Rpy(double rotateX, double rotateY, double rotateZ)
      {
        rx = rotateX;
        ry = rotateY;
        rz = rotateZ;
      }
    }

笛卡爾空間位姿數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief 笛卡爾空間位姿類型
    */
    public class DescPose
    {
      public DescTran tran = new DescTran(0.0, 0.0, 0.0);      /* 笛卡爾空間位置  */
      public Rpy rpy = new Rpy(0.0, 0.0, 0.0);			       /* 笛卡爾空間姿態  */

      public DescPose()
      {

      }

      public DescPose(DescTran descTran, Rpy rotateRpy)
      {
        tran = descTran;
        rpy = rotateRpy;
      }

      public DescPose(double tranX, double tranY, double tranZ, double rX, double ry, double rz)
      {
        tran.x = tranX;
        tran.y = tranY;
        tran.z = tranZ;
        rpy.rx = rX;
        rpy.ry = ry;
        rpy.rz = rz;
      }

      public String toString()
      {
        return String.valueOf(tran.x) + "," +  String.valueOf(tran.y) + "," +String.valueOf(tran.z) + "," +String.valueOf(rpy.rx) + "," +String.valueOf(rpy.ry) + "," +String.valueOf(rpy.rz);
      }
    }

擴展軸位置數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 擴展軸位置數據類型
    */
    public class ExaxisPos
    {
      public double axis1 = 0.0;
      public double axis2 = 0.0;
      public double axis3 = 0.0;
      public double axis4 = 0.0;

      public ExaxisPos()
      {

      }
      public ExaxisPos(double[] exaxisPos)
      {
        axis1 = exaxisPos[0];
        axis2 = exaxisPos[1];
        axis3 = exaxisPos[2];
        axis4 = exaxisPos[3];
      }

      public ExaxisPos(double pos1, double pos2, double pos3, double pos4)
      {
        axis1 = pos1;
        axis2 = pos2;
        axis3 = pos3;
        axis4 = pos4;
      }
    }

力矩傳感器數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力傳感器的受力分量和力矩分量
    */
    public class ForceTorque
    {
      public double fx;  /* 沿x軸受力分量，單位N  */
      public double fy;  /* 沿y軸受力分量，單位N  */
      public double fz;  /* 沿z軸受力分量，單位N  */
      public double tx;  /* 繞x軸力矩分量，單位Nm */
      public double ty;  /* 繞y軸力矩分量，單位Nm */
      public double tz;  /* 繞z軸力矩分量，單位Nm */
      public ForceTorque(double fX, double fY, double fZ, double tX, double tY, double tZ)
      {
        fx = fX;
        fy = fY;
        fz = fZ;
        tx = tX;
        ty = tY;
        tz = tZ;
      }
    }

螺旋參數數據類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  螺旋參數數據類型
    */
    {
        public int circle_num;           /* 螺旋圈數  */
        public double circle_angle;         /* 螺旋傾角  */
        public double rad_init;             /* 螺旋初始半徑，單位mm  */
        public double rad_add;              /* 半徑增量  */
        public double rotaxis_add;          /* 轉軸方向增量  */
        public int rot_direction;  /* 旋轉方向，0-順時針，1-逆時針  */
        public int velAccMode;     /* 速度加速度參數模式：0-角速度恆定；1-線速度恆定 */
        public SpiralParam(int circleNum, double circleAngle, double radInit, double radAdd, double rotaxisAdd, int rotDirection,int vel_AccMode)
        {
            circle_num = circleNum;
            circle_angle = circleAngle;
            rad_init = radInit;
            rad_add = radAdd;
            rotaxis_add = rotaxisAdd;
            rot_direction = rotDirection;
            velAccMode=vel_AccMode;
        }
    }

擴展軸狀態類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  擴展軸狀態類型
    */
    public class EXT_AXIS_STATUS
    {
     public double pos = 0;        //擴展軸位置
     public double vel = 0;        //擴展軸速度
     public int errorCode = 0;     //擴展軸故障碼
     public int ready = 0;        //伺服準備好
     public int inPos = 0;        //伺服到位
     public int alarm = 0;        //伺服報警
     public int flerr = 0;        //跟隨誤差
     public int nlimit = 0;       //到負限位
     public int pLimit = 0;       //到正限位
     public int mdbsOffLine = 0;  //驅動器485總線掉線
     public int mdbsTimeout = 0;  //控制卡與控制箱485通信超時
     public int homingStatus = 0; //擴展軸回零狀態
    }

傳感器類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  傳感器類型
    */
    public class DeviceConfig
    {
      int company = 0;          // 廠商
      int device = 0;           // 類型/設備號
      int softwareVersion = 0;  // 軟件版本
      int bus = 0;              // 掛載位置

      public DeviceConfig()
      {

      }

      public DeviceConfig(int company, int device, int softwareVersion, int bus)
      {
        this.company = company;
        this.device = device;
        this.softwareVersion = softwareVersion;
        this.bus = bus;
      }
    }

485擴展軸配置
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  485擴展軸配置
    */
    public class Axis485Param
    {
      int servoCompany;           // 伺服驅動器廠商，1-戴納泰克
      int servoModel;             // 伺服驅動器型號，1-FD100-750C
      int servoSoftVersion;       // 伺服驅動器軟件版本，1-V1.0
      int servoResolution;        // 編碼器分辨率
      double axisMechTransRatio;  // 機械傳動比

      public Axis485Param(int company, int model, int softVersion, int resolution, double mechTransRatio)
      {
        servoCompany = company;
        servoModel = model;
        servoSoftVersion = softVersion;
        servoResolution = resolution;
        axisMechTransRatio = mechTransRatio;
      }

      public Axis485Param()
      {

      }
    }

伺服控制器狀態
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  伺服控制器狀態
    */
    public class ROBOT_AUX_STATE
    {
      public int servoId = 0;           //伺服驅動器ID號
      public int servoErrCode = 0;       //伺服驅動器故障碼
      public int servoState = 0;         //伺服驅動器狀態
      public double servoPos = 0;        //伺服當前位置
      public float servoVel = 0;         //伺服當前速度
      public float servoTorque = 0;      //伺服當前轉矩    25
    }

焊接中斷狀態
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  焊接中斷狀態
    */
    public class WELDING_BREAKOFF_STATE
    {
      public int breakOffState = 0;  //焊接中斷狀態
      public int weldArcState = 0;   //焊接電弧中斷狀態
    }

UDP擴展軸通訊參數
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  焊接中斷狀態
    */
    public class WELDING_BREAKOFF_STATE
    {
      public String ip = "192.168.58.88";//IP地址
      public int port = 2021;            //端口號
      public int period = 2;             //通訊週期(ms，默認爲2，請勿修改此參數)
      public int lossPkgTime = 50;       //丟包檢測時間(ms)
      public int lossPkgNum = 2;         //丟包次數
      public int disconnectTime = 100;   //通訊斷開確認時長
      public int reconnectEnable = 0;    //通訊斷開自動重連使能 0-不使能 1-使能
      public int reconnectPeriod = 100;  //重連週期間隔(ms)
      public int reconnectNum = 3;       //重連次數
      public int selfConnect =0;         //斷電重啓是否自動建立連接；0-不建立連接；1-建立連接
    }

機器人狀態反饋結構體類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  機器人狀態反饋結構體類型
    */
    public class ROBOT_STATE_PKG {
        public int frame_head;                      // 幀頭
        public int frame_cnt;                       // 幀計數
        public int data_len;                        // 數據長度
        public int program_state;                   // 程式狀態 - 1-停止；2-運行；3-暫停
        public int robot_state;                     // 機器人運動狀態 - 1-停止；2-運行；3-暫停；4-拖動
        public int main_code;                       // 主故障碼
        public int sub_code;                        // 子故障碼
        public int robot_mode;                      // 機器人模式 - 1-手動模式；0-自動模式
        public double[] jt_cur_pos = new double[6]; // 6個軸當前關節位置，單位deg
        public double[] tl_cur_pos = new double[6]; // 工具當前位置 - [x,y,z,rx,ry,rz]
        public double[] flange_cur_pos = new double[6]; // 末端法蘭當前位置 - [x,y,z,rx,ry,rz]
        public double[] actual_qd = new double[6];  // 當前6個關節速度，單位deg/s
        public double[] actual_qdd = new double[6]; // 當前6個關節加速度，單位deg/s^2
        public double[] target_TCP_CmpSpeed = new double[2]; // TCP合成指令速度 - [位置mm/s, 姿態deg/s]
        public double[] target_TCP_Speed = new double[6]; // TCP指令速度 - [vx,vy,vz,wx,wy,wz]
        public double[] actual_TCP_CmpSpeed = new double[2]; // TCP合成實際速度 - [位置mm/s, 姿態deg/s]
        public double[] actual_TCP_Speed = new double[6]; // TCP實際速度 - [vx,vy,vz,wx,wy,wz]
        public double[] jt_cur_tor = new double[6]; // 當前關節力矩
        public int tool;                            // 工具ID
        public int user;                            // 工件ID
        public int cl_dgt_output_h;                 // 控制櫃數字輸出高位元組
        public int cl_dgt_output_l;                 // 控制櫃數字輸出低位元組
        public int tl_dgt_output_l;                 // 工具數字輸出低位元組
        public int cl_dgt_input_h;                  // 控制櫃數字輸入高位元組
        public int cl_dgt_input_l;                  // 控制櫃數字輸入低位元組
        public int tl_dgt_input_l;                  // 工具數字輸入低位元組
        public int[] cl_analog_input = new int[2];  // 控制櫃類比輸入
        public int tl_anglog_input;                 // 工具類比輸入
        public double[] ft_sensor_raw_data = new double[6]; // 力感測器原始數據
        public double[] ft_sensor_data = new double[6]; // 力感測器數據
        public int ft_sensor_active;                // 力感測器激活狀態
        public int EmergencyStop;                   // 急停狀態
        public int motion_done;                     // 運動完成
        public int gripper_motiondone;              // 夾爪運動完成訊號，0-未完成，1-完成(未偵測到物體)，2-運動完成（偵測到物體）
        public int mc_queue_len;                    // 運動佇列長度
        public int collisionState;                  // 碰撞狀態
        public int trajectory_pnum;                 // 軌跡點序號
        public int safety_stop0_state;              // 安全停止0狀態
        public int safety_stop1_state;              // 安全停止1狀態
        public int gripper_fault_id;                // 夾爪故障ID
        public int gripper_fault;                   // 夾爪故障
        public int gripper_active;                  // 夾爪激活
        public int gripper_position;                // 夾爪位置
        public int gripper_speed;                   // 夾爪速度
        public int gripper_current;                 // 夾爪電流
        public int gripper_temp;                    // 夾爪溫度
        public int gripper_voltage;                 // 夾爪電壓
        public AuxState aux_state = new AuxState(); // 內部輔助軸狀態
        public EXT_AXIS_STATUS[] extAxisStatus = new EXT_AXIS_STATUS[4]; // 擴展軸狀態陣列
        public short[] extDIState = new short[8];   // 擴展IO
        public short[] extDOState = new short[8];   // 擴展IO
        public short[] extAIState = new short[4];   // 擴展IO
        public short[] extAOState = new short[4];   // 擴展IO
        public int rbtEnableState;                  // 機器人使能狀態
        public double[] jointDriverTorque = new double[6]; // 關節驅動器力矩
        public double[] jointDriverTemperature = new double[6]; // 關節驅動器溫度
        public ROBOT_TIME robotTime = new ROBOT_TIME(); // 機器人時間物件
        public int softwareUpgradeState;            // 軟體升級狀態
        public int endLuaErrCode;                   // 末端Lua錯誤碼
        public int[] cl_analog_output = new int[2]; // 控制櫃類比輸出
        public int tl_analog_output;                // 工具類比輸出
        public float gripperRotNum;                 // 旋轉夾爪圈數
        public int gripperRotSpeed;                 // 旋轉夾爪速度
        public int gripperRotTorque;                // 旋轉夾爪力矩
        public WELDING_BREAKOFF_STATE weldingBreakOffState = new WELDING_BREAKOFF_STATE(); // 焊接中斷狀態
        public double[] jt_tgt_tor = new double[6]; // 目標關節力矩
        public int smartToolState;                  // 智能工具狀態
        public float wideVoltageCtrlBoxTemp;        // 寬電壓控制箱溫度
        public int wideVoltageCtrlBoxFanCurrent;    // 寬電壓控制箱風扇電流
        public double[] toolCoord = new double[6];  // 工具座標系
        public double[] wobjCoord = new double[6];  // 工件座標系
        public double[] extoolCoord = new double[6]; // 外部工具座標系
        public double[] exAxisCoord = new double[6]; // 擴展軸座標系
        public double load;                         // 負載
        public double[] loadCog = new double[3];    // 負載重心
        public double[] lastServoTarget = new double[6]; // 上一次伺服J目標位置
        public int servoJCmdNum;                    // 伺服J命令數量
        public double[] targetJointPos = new double[6]; // 目標關節位置
        public double[] targetJointVel = new double[6]; // 目標關節速度
        public double[] targetJointAcc = new double[6]; // 目標關節加速度
        public double[] targetJointCurrent = new double[6]; // 目標關節電流
        public double[] actualJointCurrent = new double[6]; // 實際關節電流
        public double[] actualTCPForce = new double[6]; // 實際TCP力
        public double[] targetTCPPos = new double[6]; // 目標TCP位置
        public int[] collisionLevel = new int[6];   // 碰撞等級
        public double speedScaleManual;              // 手動速度比例
        public double speedScaleAuto;                // 自動速度比例
        public int luaLineNum;                       // Lua行號
        public int abnomalStop;                      // 異常停止
        public String currentLuaFileName;            // 當前Lua檔案名稱
        public int programTotalLine;                 // 程式總行數
        public int[] safetyBoxSingal = new int[6];   // 安全箱信號
        public double weldVoltage;                   // 焊接電壓
        public double weldCurrent;                   // 焊接電流
        public double weldTrackVel;                  // 焊接跟蹤速度
        public int tpdException;                     // TPD異常
        public int alarmRebootRobot;                 // 報警重啟機器人
        public int modbusMasterConnect;              // Modbus主站連接
        public int modbusSlaveConnect;               // Modbus從站連接
        public int btnBoxStopSignal;                 // 按鈕盒停止信號
        public int dragAlarm;                        // 拖動報警
        public int safetyDoorAlarm;                  // 安全門報警
        public int safetyPlaneAlarm;                 // 安全平面報警
        public int motonAlarm;                       // 運動報警
        public int interfaceAlarm;                   // 干涉報警
        public int udpCmdState;                      // UDP命令狀態
        public int weldReadyState;                   // 焊接準備狀態
        public int alarmCheckEmergStopBtn;           // 報警檢查急停按鈕
        public int tsTmCmdComError;                  // 命令通信錯誤
        public int tsTmStateComError;                // 狀態通信錯誤
        public int ctrlBoxError;                     // 控制箱錯誤
        public int safetyDataState;                  // 安全數據狀態
        public int forceSensorErrState;              // 力感測器錯誤狀態
        public int[] ctrlOpenLuaErrCode = new int[4]; // 控制打開Lua錯誤碼
        public int strangePosFlag;                   // 奇異位置標誌
        public int alarm;                            // 報警
        public int driverAlarm;                      // 驅動器報警
        public int aliveSlaveNumError;               // 存活從站數量錯誤
        public int[] slaveComError = new int[8];     // 從站通信錯誤
        public int cmdPointError;                    // 命令點錯誤
        public int IOError;                          // IO錯誤
        public int gripperError;                     // 夾爪錯誤
        public int fileError;                        // 檔案錯誤
        public int paraError;                        // 參數錯誤
        public int exaxisOutLimitError;              // 擴展軸超出軟限位錯誤
        public int[] driverComError = new int[6];    // 驅動器通信錯誤
        public int driverError;                      // 驅動器錯誤
        public int outSoftLimitError;                // 超出軟限位錯誤
        public byte[] axleGenComData = new byte[130]; // 通用軸通信數據
        public int check_sum;                        // 校驗和
        public int socketConnTimeout;                // Socket連接超時
        public int socketReadTimeout;                // Socket讀取超時
        public int tsWebStateComErr;                 // TS Web狀態通信錯誤
        public int exaxisCoordID;                  //擴展軸座標系編號
    }
  
機器人狀態反饋配置結果類
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * 機器人狀態反饋配置結果類，包含狀態列表和週期
    */
    public static class StateConfigResult {
      public final List<RobotState> stateList;
      public final int period;
    }

機器人狀態反饋配置列舉類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * 機器人狀態列舉類型
    * 用於即時狀態反饋配置
    */
    enum class RobotState
    {
        ProgramState,           // 程式運行狀態，1-停止；2-運行；3-暫停
        RobotState,             // 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動
        MainCode,               // 主故障碼
        SubCode,                // 子故障碼
        RobotMode,              // 機器人模式，1-手動模式；0-自動模式
        JointCurPos,            // 6個軸目前關節位置，單位deg
        ToolCurPos,             // 工具目前位置：[0]沿x軸位置(mm)，[1]沿y軸(mm)，[2]沿z軸(mm)，[3]繞固定軸X旋轉(deg)，[4]繞固定軸Y(deg)，[5]繞固定軸Z(deg)
        FlangeCurPos,           // 末端法蘭目前位置：[0]沿x軸(mm)，[1]沿y軸(mm)，[2]沿z軸(mm)，[3]繞固定軸X(deg)，[4]繞固定軸Y(deg)，[5]繞固定軸Z(deg)
        ActualJointVel,         // 目前6個關節速度，單位deg/s
        ActualJointAcc,         // 目前6個關節加速度，單位deg/s²
        TargetTCPCmpSpeed,      // TCP合成指令速度：[0]位置(mm/s)，[1]姿態(deg/s)
        TargetTCPSpeed,         // TCP指令速度：[0]沿x軸(mm/s)，[1]沿y軸(mm/s)，[2]沿z軸(mm/s)，[3]繞X角速度(deg/s)，[4]繞Y(deg/s)，[5]繞Z(deg/s)
        ActualTCPCmpSpeed,      // TCP合成實際速度：[0]位置(mm/s)，[1]姿態(deg/s)
        ActualTCPSpeed,         // TCP實際速度：[0]沿x軸(mm/s)，[1]沿y軸(mm/s)，[2]沿z軸(mm/s)，[3]繞X角速度(deg/s)，[4]繞Y(deg/s)，[5]繞Z(deg/s)
        ActualJointTorque,      // 6個軸目前扭矩，單位N·m
        Tool,                   // 應用的工具座標系編號
        User,                   // 應用的工件座標系編號
        ClDgtOutputH,           // 控制箱數位量IO輸出15-8
        ClDgtOutputL,           // 控制箱數位量IO輸出7-0
        TlDgtOutputL,           // 工具數位量IO輸出7-0，僅bit0-bit1有效
        ClDgtInputH,            // 控制箱數位量IO輸入15-8
        ClDgtInputL,            // 控制箱數位量IO輸入7-0
        TlDgtInputL,            // 工具數位量IO輸入7-0，僅bit0-bit1有效
        ClAnalogInput,          // 控制箱類比量輸入：[0]通道0，[1]通道1
        TlAnalogInput,          // 工具類比量輸入
        FtSensorRawData,        // 力矩感測器原始資料：[0]沿x軸力(N)，[1]沿y軸力(N)，[2]沿z軸力(N)，[3]沿x軸力矩(Nm)，[4]沿y軸(Nm)，[5]沿z軸(Nm)
        FtSensorData,           // 力矩感測器資料（經處理）：[0]沿x軸力(N)，[1]沿y軸力(N)，[2]沿z軸力(N)，[3]沿x軸力矩(Nm)，[4]沿y軸(Nm)，[5]沿z軸(Nm)
        FtSensorActive,         // 力矩感測器啟動狀態，0-復位，1-啟動
        EmergencyStop,          // 急停標誌，0-急停未按下，1-急停按下
        MotionDone,             // 運動到位信號，1-到位，0-未到位
        GripperMotiondone,      // 夾爪運動完成訊號，0-未完成，1-完成(未偵測到物體)，2-運動完成（偵測到物體）
        McQueueLen,             // 運動指令佇列長度
        CollisionState,         // 碰撞偵測，1-碰撞，0-無碰撞
        TrajectoryPnum,         // 軌跡點編號
        SafetyStop0State,       // 安全停止信號SI0
        SafetyStop1State,       // 安全停止信號SI1
        GripperFaultId,         // 錯誤夾爪號
        GripperFault,           // 夾爪故障
        GripperActive,          // 夾爪啟動狀態
        GripperPosition,        // 夾爪位置
        GripperSpeed,           // 夾爪速度
        GripperCurrent,         // 夾爪電流
        GripperTemp,            // 夾爪溫度
        GripperVoltage,         // 夾爪電壓
        AuxState,               // 485擴展軸狀態
        ExtAxisStatus,          // UDP擴展軸狀態（4個軸）
        ExtDIState,             // 擴展DI輸入（8個）
        ExtDOState,             // 擴展DO輸出（8個）
        ExtAIState,             // 擴展AI輸入（4個）
        ExtAOState,             // 擴展AO輸出（4個）
        RbtEnableState,         // 機器人使能狀態
        JointDriverTorque,      // 機器人關節驅動器扭矩（6個關節）
        JointDriverTemperature, // 機器人關節驅動器溫度（6個關節）
        RobotTime,              // 機器人系統時間
        SoftwareUpgradeState,   // 機器人軟體升級狀態
        EndLuaErrCode,          // 末端LUA運行狀態
        ClAnalogOutput,         // 控制箱類比量輸出（2個）
        TlAnalogOutput,         // 工具類比量輸出
        GripperRotNum,          // 旋轉夾爪目前旋轉圈數
        GripperRotSpeed,        // 旋轉夾爪目前旋轉速度百分比
        GripperRotTorque,       // 旋轉夾爪目前旋轉力矩百分比
        WeldingBreakOffState,   // 焊接中斷狀態
        TargetJointTorque,      // 關節指令力矩（6個關節）
        SmartToolState,         // SmartTool手柄按鈕狀態
        WideVoltageCtrlBoxTemp, // 寬電壓控制箱溫度
        WideVoltageCtrlBoxFanCurrent, // 寬電壓控制箱風扇電流(mA)
        ToolCoord,              // 目前工具座標系數值：x,y,z,rx,ry,rz
        WobjCoord,              // 目前工件座標系數值：x,y,z,rx,ry,rz
        ExtoolCoord,            // 目前外部工具座標系數值：x,y,z,rx,ry,rz
        ExAxisCoord,            // 目前擴展軸座標系數值：x,y,z,rx,ry,rz
        Load,                   // 負載質量
        LoadCog,                // 負載質心：x,y,z
        LastServoTarget,        // 佇列中最後一個ServoJ目標位置（6個關節）
        ServoJCmdNum,           // servoJ指令計數
        TargetJointPos,         // 6個關節指令位置，單位°
        TargetJointVel,         // 6個關節指令速度，單位°/s
        TargetJointAcc,         // 6個關節指令加速度，單位°/s²
        TargetJointCurrent,     // 6個關節指令電流，單位A
        ActualJointCurrent,     // 6個關節目前電流，單位A
        ActualTCPForce,         // 機器人末端力矩：x,y,z,rx,ry,rz，單位Nm
        TargetTCPPos,           // 機器人TCP指令位置：x,y,z,rx,ry,rz，單位mm
        CollisionLevel,         // 機器人碰撞等級（6個）
        SpeedScaleManual,       // 手動模式全域速度百分比
        SpeedScaleAuto,         // 自動模式全域速度百分比
        LuaLineNum,             // 目前lua程式運行行號
        AbnomalStop,            // 0-無異常；1-有異常
        CurrentLuaFileName,     // 目前運行lua程式名稱
        ProgramTotalLine,       // lua程式總行數
        SafetyBoxSingal,        // 機器人按鈕盒按鈕狀態（6個）
        WeldVoltage,            // 焊接電壓 V
        WeldCurrent,            // 焊接電流
        WeldTrackVel,           // 焊縫跟蹤速度 mm/s
        TpdException,           // TPD軌跡載入數量超限，0-未超限，1-超限
        AlarmRebootRobot,       // 警告：1-鬆開急停後需斷電重啟，2-關節通訊異常需斷電重啟
        ModbusMasterConnect,    // bit0-7對應ModbusTCP主站0-7連接狀態，0-未連接，1-連接
        ModbusSlaveConnect,     // ModbusTCP從站連接狀態，0-未連接，1-已連接
        BtnBoxStopSignal,       // 按鈕盒急停信號，0-鬆開急停，1-按下急停
        DragAlarm,              // 拖動警告：0-不報警，1-報警，2-位置反饋異常不切換
        SafetyDoorAlarm,        // 安全門警告：0-關閉，1-打開
        SafetyPlaneAlarm,       // 安全牆警告：0-未進入，1-已進入
        MotonAlarm,             // 運動警告
        InterfaceAlarm,         // 進入干涉區警告
        UdpCmdState,            // 20007埠UDP通訊連接狀態
        WeldReadyState,         // 焊機準備完成狀態
        AlarmCheckEmergStopBtn, // 0-正常；1-通信異常，檢查急停按鈕
        TsTmCmdComError,        // 0-正常；1-扭矩指令通訊失敗
        TsTmStateComError,      // 0-正常；1-扭矩狀態通訊失敗
        CtrlBoxError,           // 控制箱錯誤
        SafetyDataState,        // 安全數據狀態，0-正常，1-異常
        ForceSensorErrState,    // 力感測器連接超時，bit0-bit1對應ID1-ID2
        CtrlOpenLuaErrCode,     // 4個控制器外設協定錯誤碼(500錯誤碼)
        StrangePosFlag,         // 奇異位姿標誌：0-正常，1-奇異位姿
        Alarm,                  // 警告
        DriverAlarm,            // 驅動器報警軸號
        AliveSlaveNumError,     // 活動從站數量錯誤：0-正常，1-數量錯誤
        SlaveComError,          // 從站錯誤：0-正常，1-離線，2-狀態不一致，3-未配置，4-配置錯誤，5-初始化錯誤，6-郵箱通信初始化錯誤
        CmdPointError,          // 指令點錯誤
        IOError,                // IO錯誤
        GripperError,           // 夾爪錯誤
        FileError,              // 檔案錯誤
        ParaError,              // 參數錯誤
        ExaxisOutLimitError,    // 外部軸超出軟限位錯誤
        DriverComError,         // 與驅動器通訊故障（6個軸）
        DriverError,            // 驅動器通訊故障軸號
        OutSoftLimitError,      // 超出軟限位故障
        AxleGenComData,         // 機器人末端透傳反饋數據
        SocketConnTimeout,      // socket連接超時，bit0-bit4對應socketID 1-4
        SocketReadTimeout,      // socket讀取超時，bit0-bit4對應socketID 1-4
        TsWebStateComErr,       // web-扭矩通訊失敗：0-正常，1-失敗
        ExaxisCoordID           // 擴展軸座標系編號
    };