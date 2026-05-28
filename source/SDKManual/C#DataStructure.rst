數據結構說明
================

.. toctree:: 
    :maxdepth: 5

關節位置數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 關節位置數據類型 
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* 六個關節位置，單位deg */
    }

笛卡爾空間位置數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間位置數據類型
    */
    struct DescTran
    {
        public double x;    /* x軸座標，單位mm  */
        public double y;    /* y軸座標，單位mm  */
        public double z;    /* z軸座標，單位mm  */
    }

歐拉角姿態數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 歐拉角姿態數據類型
    */
    struct Rpy
    {
    public double rx;   /* 繞固定軸X旋轉角度，單位：deg  */
    public double ry;   /* 繞固定軸Y旋轉角度，單位：deg  */
    public double rz;   /* 繞固定軸Z旋轉角度，單位：deg  */
    }

笛卡爾空間位姿數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief 笛卡爾空間位姿類型
    */
    struct DescPose
    {
        public DescTran tran;     /* 笛卡爾空間位置  */
        public Rpy rpy;			/* 笛卡爾空間姿態  */
    }

擴展軸位置數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展軸位置數據類型
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* 四個擴展軸位置，單位mm */
    }

力矩傳感器數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 力傳感器的受力分量和力矩分量
    */
    struct ForceTorque
    {
        public double fx;  /* 沿x軸受力分量，單位N  */
        public double fy;  /* 沿y軸受力分量，單位N  */
        public double fz;  /* 沿z軸受力分量，單位N  */
        public double tx;  /* 繞x軸力矩分量，單位Nm */
        public double ty;  /* 繞y軸力矩分量，單位Nm */
        public double tz;  /* 繞z軸力矩分量，單位Nm */
    }

螺旋參數數據類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public struct SpiralParam
    {
        public int circle_num;           /* 螺旋圈數  */
        public float circle_angle;         /* 螺旋傾角  */
        public float rad_init;             /* 螺旋初始半徑，單位mm  */
        public float rad_add;              /* 半徑增量  */
        public float rotaxis_add;          /* 轉軸方向增量  */
        public uint rot_direction;  /* 旋轉方向，0-順時針，1-逆時針  */
        public int velAccMode;      // 速度加速度參數模式：0-角速度恆定；1-線速度恆定
        public SpiralParam(int num, float angle, float initRad, float addRad, float axisAdd, uint direction, int mode)
        {
            circle_num = num;
            circle_angle = angle;
            rad_init = initRad;
            rad_add = addRad;
            rotaxis_add = axisAdd;
            rot_direction = direction;
            velAccMode = mode;
        }
    }

擴展軸狀態類型
+++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /**
    * @brief  擴展軸狀態類型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_AUX_STATE
    {
        public byte servoId;           //伺服驅動器ID號
        public int servoErrCode;       //伺服驅動器故障碼
        public int servoState;         //伺服驅動器狀態
        public double servoPos;        //伺服當前位置
        public float servoVel;         //伺服當前速度
        public float servoTorque;      //伺服當前轉矩
    }

焊接中斷狀態
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct WELDING_BREAKOFF_STATE
    {
        public byte breakOffState;  // 焊接中斷狀態
        public byte weldArcState;   // 焊接電弧中斷狀態
    }

機器人狀態反饋結構體類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  機器人狀態反饋結構體類型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public class ROBOT_STATE_PKG
    {
        public UInt16 frame_head;           // 幀頭 0x5A5A
        public byte frame_cnt;              // 幀計數
        public UInt16 data_len;             // 數據長度  5
        public byte program_state;          // 程式運行狀態，1-停止；2-運行；3-暫停；
        public byte robot_state;            // 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動
        public int main_code;               // 主故障碼
        public int sub_code;                // 子故障碼
        public byte robot_mode;             // 機器人模式，1-手動模式；0-自動模式；

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_pos;         // 6個軸當前關節位置，單位deg
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] tl_cur_pos;         // 工具當前位置
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] flange_cur_pos;     // 末端法蘭當前位置
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qd;          // 當前6個關節速度，單位deg/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_qdd;         // 當前6個關節加速度，單位deg/s^2
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] target_TCP_CmpSpeed;// TCP合成指令速度(位置,姿態)
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] target_TCP_Speed;   // TCP指令速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public double[] actual_TCP_CmpSpeed;// TCP合成實際速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actual_TCP_Speed;   // TCP實際速度
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_cur_tor;         // 6個軸當前扭矩，單位N·m

        public int tool;                    // 應用的工具座標系編號
        public int user;                    // 應用的工件座標系編號
        public byte cl_dgt_output_h;        // 控制箱數字量IO輸出15-8
        public byte cl_dgt_output_l;        // 控制箱數字量IO輸出7-0
        public byte tl_dgt_output_l;        // 工具數字量IO輸出7-0，僅bit0-bit1有效
        public byte cl_dgt_input_h;         // 控制箱數字量IO輸入15-8
        public byte cl_dgt_input_l;         // 控制箱數字量IO輸入7-0
        public byte tl_dgt_input_l;         // 工具數字量IO輸入7-0，僅bit0-bit1有效

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public UInt16[] cl_analog_input;        //控制箱模擬量輸入
        public UInt16 tl_anglog_input;          //工具模擬量輸入                            

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_raw_data; // 力矩感測器原始數據
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] ft_sensor_data;     // 力矩感測器數據
        public byte ft_sensor_active;       // 力矩感測器激活狀態，0-復位，1-激活

        public byte EmergencyStop;          // 急停標誌，0-未按下，1-按下
        public int motion_done;             // 運動到位信號，1-到位，0-未到位
        public byte gripper_motiondone;     // 夾爪運動完成信號，1-完成，0-未完成
        public int mc_queue_len;            // 運動指令隊列長度
        public byte collisionState;         // 碰撞檢測，1-碰撞，0-無碰撞
        public int trajectory_pnum;         // 軌跡點編號
        public byte safety_stop0_state;     // 安全停止信號SI0
        public byte safety_stop1_state;     // 安全停止信號SI1
        public byte gripper_fault_id;       // 錯誤夾爪號
        public UInt16 gripper_fault;     /* 夾爪故障 */
        public UInt16 gripper_active;    /* 夾爪激活狀態 */
        public byte gripper_position;       // 夾爪位置
        public byte gripper_speed;       /* 夾爪速度 */
        public byte gripper_current;     /* 夾爪電流 */
        public int gripper_temp;            // 夾爪溫度
        public int gripper_voltage;         // 夾爪電壓

        public ROBOT_AUX_STATE auxState;   // 485擴展軸狀態

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public EXT_AXIS_STATUS[] extAxisStatus; // UDP擴展軸狀態

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDIState;        //擴展DI輸入
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public UInt16[] extDOState;        //擴展DO輸出
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAIState;        //擴展AI輸入
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public UInt16[] extAOState;        //擴展AO輸出

        public int rbtEnableState;          // 機器人使能狀態

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTorque;      // 機器人關節驅動器扭矩
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jointDriverTemperature; // 機器人關節驅動器溫度

        public ROBOT_TIME robotTime;        // 機器人系統時間
        public int softwareUpgradeState;    // 機器人軟體升級狀態
        public UInt16 endLuaErrCode;    //末端LUA運行狀態 

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
        public  UInt16[] cl_analog_output;  //控制箱模擬量輸出
        public UInt16 tl_analog_output;     //工具模擬量輸出

        public float gripperRotNum;         // 旋轉夾爪當前旋轉圈數
        public byte gripperRotSpeed;        // 旋轉夾爪當前旋轉速度百分比
        public byte gripperRotTorque;       // 旋轉夾爪當前旋轉力矩百分比

        public WELDING_BREAKOFF_STATE weldingBreakOffState; // 焊接中斷狀態

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jt_tgt_tor;         // 關節指令力矩
        public int smartToolState;          // SmartTool手柄按鈕狀態
        public float wideVoltageCtrlBoxTemp; // 寬電壓控制箱溫度
        public UInt16 wideVoltageCtrlBoxFanVel;   //寬電壓控制箱風扇電流（mA）

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] toolCoord;          // 當前工具座標係數值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] wobjCoord;          // 當前工件座標係數值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] extoolCoord;        // 當前外部工具座標係數值；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] exAxisCoord;        // 當前擴展軸座標係數值；x,y,z,rx,ry,rz

        public double load;                 // 負載質量
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
        public double[] loadCog;            // 負載質心
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] lastServoTarget;    // 隊列中最後一個ServoJ目標位置
        public int servoJCmdNum;            // servoJ指令計數

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointPos;     // 6個關節指令位置，單位°
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointVel;     // 6個關節指令速度，單位°/s
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointAcc;     // 6個關節指令加速度，單位°/s²
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetJointCurrent; // 6個關節指令電流，單位A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualJointCurrent; // 6個關節當前電流，單位A
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] actualTCPForce;     // 機器人末端力矩Nm；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] targetTCPPos;       // 機器人TCP指令位置mm；x,y,z,rx,ry,rz
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] collisionLevel;       // 機器人碰撞等級

        public double speedScaleManual;     // 手動模式全局速度百分比
        public double speedScaleAuto;       // 自動模式全局速度百分比
        public int luaLineNum;              // 當前lua程式運行行號
        public byte abnomalStop;            // 0-無異常；1-有異常

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 256)]
        public byte[] currentLuaFileName;   // 當前運行lua程式名稱
        public byte programTotalLine;       // lua程式總行數
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] safetyBoxSingal;      // 機器人按鈕盒按鈕狀態

        public double weldVoltage;          // 焊接電壓 V
        public double weldCurrent;          // 焊接電流
        public double weldTrackVel;         // 焊縫跟蹤速度 mm/s

        public byte tpdException;           // TPD軌跡加載數量超限，0-未超限，1-超限
        public byte alarmRebootRobot;       // 警告，1-鬆開急停按鈕請斷電重啟控制箱，2-關節通訊異常請斷電重啟控制箱
        public byte modbusMasterConnect;    // bit0-bit7位對應ModbusTCP的0-7主站連接狀態  0-未連接   1-連接
        public byte modbusSlaveConnect;     // ModbusTCP從站連接狀態 0-未連接；1-已連接
        public byte btnBoxStopSignal;       // 按鈕盒急停信號，0-鬆開急停；1-按下急停
        public byte dragAlarm;              // 拖動警告，當前處於自動模式,0-不報警，1-報警 ，2-位置反饋異常不切換
        public byte safetyDoorAlarm;        // 安全門警告；0-安全門關閉；1-安全門打開
        public byte safetyPlaneAlarm;       // 進入安全牆警告；0-未進入安全牆；1-已進入安全牆
        public byte motonAlarm;             // 運動警告
        public byte interfaceAlarm;         // 進入干涉區警告
        public int udpCmdState;             // 20007端口UDP通訊連接狀態
        public byte weldReadyState;         // 焊機準備完成狀態
        public byte alarmCheckEmergStopBtn; // 0-正常；1-通訊異常，檢查急停按鈕是否鬆開
        public byte tsTmCmdComError;        // 0-正常；1-扭矩指令通訊失敗
        public byte tsTmStateComError;      // 0-正常；1-扭矩狀態通訊失敗
        public int ctrlBoxError;            // 控制箱錯誤
        public byte safetyDataState;        // 安全數據狀態標誌，0-正常，1-異常
        public byte forceSensorErrState;    // 力感測器連接超時故障；bit0-bit1對應力感測器ID1-ID2

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public byte[] ctrlOpenLuaErrCode;   // 4個控制器外設協議錯誤碼(500錯誤碼)

        public byte strangePosFlag;         // 當前處於奇異位姿標誌；0-正常；1-奇異位姿
        public byte alarm;                  // 警告
        public byte driverAlarm;            // 驅動器報警軸號
        public byte aliveSlaveNumError;     // 活動從站數量錯誤，0：正常；1：數量錯誤

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
        public byte[] slaveComError;        // 從站錯誤，0：正常；1：從站掉線；2：從站狀態與設定值不一致；3：從站未配置；4：從站配置錯誤；5：從站初始化錯誤；6：從站郵箱通信初始化錯誤

        public byte cmdPointError;          // 指令點錯誤
        public byte IOError;                // IO錯誤
        public byte gripperError;           // 夾爪錯誤
        public byte fileError;              // 文件錯誤
        public byte paraError;              // 參數錯誤
        public byte exaxisOutLimitError;    // 外部軸超出軟限位錯誤

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public byte[] driverComError;       // 與驅動器通信故障
        public byte driverError;            // 驅動器通信故障軸號
        public byte outSoftLimitError;      // 超出軟限位故障

        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 130)]
        public byte[] axleGenComData;       // 機器人末端透傳反饋數據

        public byte socketConnTimeout;     // socket連接超時標誌
        public byte socketReadTimeout;     // socket讀取超時標誌
        public byte tsWebStateComErr;      // ts_web_state_com_err
        public byte exaxisCoordID;         // 擴展軸座標系編號
        public UInt16 check_sum;         /* 和校驗 */                 

        // 構造函數：初始化所有陣列欄位
        public ROBOT_STATE_PKG()
        {
            jt_cur_pos = new double[6];
            tl_cur_pos = new double[6];
            flange_cur_pos = new double[6];
            actual_qd = new double[6];
            actual_qdd = new double[6];
            target_TCP_CmpSpeed = new double[2];
            target_TCP_Speed = new double[6];
            actual_TCP_CmpSpeed = new double[2];
            actual_TCP_Speed = new double[6];
            jt_cur_tor = new double[6];
            cl_analog_input = new ushort[2];
            ft_sensor_raw_data = new double[6];
            ft_sensor_data = new double[6];
            extAxisStatus = new EXT_AXIS_STATUS[4];
            extDIState = new ushort[8];
            extDOState = new ushort[8];
            extAIState = new ushort[4];
            extAOState = new ushort[4];
            jointDriverTorque = new double[6];
            jointDriverTemperature = new double[6];
            cl_analog_output = new ushort[2];
            jt_tgt_tor = new double[6];
            toolCoord = new double[6];
            wobjCoord = new double[6];
            extoolCoord = new double[6];
            exAxisCoord = new double[6];
            loadCog = new double[3];
            lastServoTarget = new double[6];
            targetJointPos = new double[6];
            targetJointVel = new double[6];
            targetJointAcc = new double[6];
            targetJointCurrent = new double[6];
            actualJointCurrent = new double[6];
            actualTCPForce = new double[6];
            targetTCPPos = new double[6];
            collisionLevel = new byte[6];
            currentLuaFileName = new byte[256];
            safetyBoxSingal = new byte[6];
            ctrlOpenLuaErrCode = new byte[4];
            slaveComError = new byte[8];
            driverComError = new byte[6];
            axleGenComData = new byte[130];
        }
    }

機器人狀態反饋配置枚舉類型
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  機器人可配置狀態枚舉 範圍 0~132
    */
    public enum RobotState
    {
        FrameHead = 0,
        FrameCnt = 1,
        DataLen = 2,
        ProgramState = 3,
        RobotState = 4,
        MainCode = 5,
        SubCode = 6,
        RobotMode = 7,
        JointCurPos = 8,
        ToolCurPos = 9,
        FlangeCurPos = 10,
        ActualJointVel = 11,
        ActualJointAcc = 12,
        TargetTCPCmpSpeed = 13,
        TargetTCPSpeed = 14,
        ActualTCPCmpSpeed = 15,
        ActualTCPSpeed = 16,
        ActualJointTorque = 17,
        Tool = 18,
        User = 19,
        ClDgtOutputH = 20,
        ClDgtOutputL = 21,
        TlDgtOutputL = 22,
        ClDgtInputH = 23,
        ClDgtInputL = 24,
        TlDgtInputL = 25,
        ClAnalogInput = 26,
        TlAnglogInput = 27,
        FtSensorRawData = 28,
        FtSensorData = 29,
        FtSensorActive = 30,
        EmergencyStop = 31,
        MotionDone = 32,
        GripperMotiondone = 33,
        McQueueLen = 34,
        CollisionState = 35,
        TrajectoryPnum = 36,
        SafetyStop0State = 37,
        SafetyStop1State = 38,
        GripperFaultId = 39,
        GripperFault = 40,
        GripperActive = 41,
        GripperPosition = 42,
        GripperSpeed = 43,
        GripperCurrent = 44,
        GripperTemp = 45,
        GripperVoltage = 46,
        AuxState = 47,
        ExtAxisStatus = 48,
        ExtDIState = 49,
        ExtDOState = 50,
        ExtAIState = 51,
        ExtAOState = 52,
        RbtEnableState = 53,
        JointDriverTorque = 54,
        JointDriverTemperature = 55,
        RobotTime = 56,
        SoftwareUpgradeState = 57,
        EndLuaErrCode = 58,
        ClAnalogOutput = 59,
        TlAnalogOutput = 60,
        GripperRotNum = 61,
        GripperRotSpeed = 62,
        GripperRotTorque = 63,
        WeldingBreakOffState = 64,
        TargetJointTorque = 65,
        SmartToolState = 66,
        WideVoltageCtrlBoxTemp = 67,
        WideVoltageCtrlBoxFanCurrent = 68,
        ToolCoord = 69,
        WobjCoord = 70,
        ExtoolCoord = 71,
        ExAxisCoord = 72,
        Load = 73,
        LoadCog = 74,
        LastServoTarget = 75,
        ServoJCmdNum = 76,
        TargetJointPos = 77,
        TargetJointVel = 78,
        TargetJointAcc = 79,
        TargetJointCurrent = 80,
        ActualJointCurrent = 81,
        ActualTCPForce = 82,
        TargetTCPPos = 83,
        CollisionLevel = 84,
        SpeedScaleManual = 85,
        SpeedScaleAuto = 86,
        LuaLineNum = 87,
        AbnomalStop = 88,
        CurrentLuaFileName = 89,
        ProgramTotalLine = 90,
        SafetyBoxSingal = 91,
        WeldVoltage = 92,
        WeldCurrent = 93,
        WeldTrackVel = 94,
        TpdException = 95,
        AlarmRebootRobot = 96,
        ModbusMasterConnect = 97,
        ModbusSlaveConnect = 98,
        BtnBoxStopSignal = 99,
        DragAlarm = 100,
        SafetyDoorAlarm = 101,
        SafetyPlaneAlarm = 102,
        MotonAlarm = 103,
        InterfaceAlarm = 104,
        UdpCmdState = 105,
        WeldReadyState = 106,
        AlarmCheckEmergStopBtn = 107,
        TsTmCmdComError = 108,
        TsTmStateComError = 109,
        CtrlBoxError = 110,
        SafetyDataState = 111,
        ForceSensorErrState = 112,
        CtrlOpenLuaErrCode = 113,
        StrangePosFlag = 114,
        Alarm = 115,
        DriverAlarm = 116,
        AliveSlaveNumError = 117,
        SlaveComError = 118,
        CmdPointError = 119,
        IOError = 120,
        GripperError = 121,
        FileError = 122,
        ParaError = 123,
        ExaxisOutLimitError = 124,
        DriverComError = 125,
        DriverError = 126,
        OutSoftLimitError = 127,
        AxleGenComData = 128,
        SocketConnTimeout = 129,     //socket連接超時，bit0-bit4:socketID 1-4
        SocketReadTimeout = 130,     //socket讀取超時，bit0-bit4:socketID 1-4
        TsWebStateComErr = 131,     //web-扭矩通訊失敗；0-正常；1-失敗
        ExaxisCoordID = 132          //擴展軸座標系編號
    }