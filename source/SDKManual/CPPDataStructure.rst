資料結構說明
================

.. toctree:: 
    :maxdepth: 5

介面呼叫傳回值類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    typedef  int errno_t;

關節位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節位置資料類型
    */
    typedef  struct
    {
        double jPos[6];   /* 六個關節位置，單位deg */
    }JointPos;

笛卡爾空間位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡爾空間位置資料類型
    */
    typedef struct
    {
        double x;    /* x軸座標，單位mm  */
        double y;    /* y軸座標，單位mm  */
        double z;    /* z軸座標，單位mm  */
    } DescTran;

歐拉角姿態資料型態
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 歐拉角姿態資料型態
    */
    typedef struct
    {
        double rx;   /* 繞固定軸X旋轉角度，單位：deg  */
        double ry;   /* 繞固定軸Y旋轉角度，單位：deg  */
        double rz;   /* 繞固定軸Z旋轉角度，單位：deg  */
    } Rpy;

笛卡爾空間位姿資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    *@brief 笛卡兒空間位姿類型
    */
    typedef struct
    {
        DescTran tran;      /* 笛卡兒空間位置  */
        Rpy rpy;            /* 笛卡兒空間姿態  */
    } DescPose;

擴展軸位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 擴展軸位置資料類型
    */
    typedef  struct
    {
        double ePos[4];   /* 四個擴展軸位置，單位mm */
    }ExaxisPos;

力矩感測器資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 力感測器的受力分量和力矩分量
    */
    typedef struct
    {
        double fx;  /* 沿x軸受力分量，單位N  */
        double fy;  /* 沿y軸受力分量，單位N  */
        double fz;  /* 沿z軸受力分量，單位N  */
        double tx;  /* 绕x軸力矩分量，單位Nm */
        double ty;  /* 绕y軸力矩分量，單位Nm */
        double tz;  /* 绕z軸力矩分量，單位Nm */
    } ForceTorque;

螺旋參數資料類型
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  螺旋參數資料類型
    */
    typedef  struct
    {
        int    circle_num;           /* 螺旋圈數  */
        float  circle_angle;         /* 螺旋傾角  */
        float  rad_init;             /* 螺旋初始半徑，單位mm  */
        float  rad_add;              /* 半徑增量  */
        float  rotaxis_add;          /* 轉軸方向增量  */
        int rot_direction;  /* 旋轉方向，0-順時針，1-逆時針  */
        int velAccMode;      /* 速度加速度參數模式：0-角速度恆定；1-線速度恆定 */
    }SpiralParam;

控制器狀態回饋資料包
+++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  控制器狀態回饋資料包
     */
    typedef struct _ROBOT_STATE_PKG
    {
      uint16_t frame_head;   // 幀頭，約定為0x5A5A 
      uint8_t frame_cnt;    // 幀計數，循環計數0-255 
      uint16_t data_len;    // 數據內容的長度 
      uint8_t program_state;  // 程式運行狀態，1-停止；2-運行；3-暫停；
      uint8_t robot_state;   // 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動 
      int   main_code;    // 主故障碼 
      int   sub_code;    // 子故障碼 
      uint8_t robot_mode;   // 機器人模式，1-手動模式；0-自動模式； 
      double  jt_cur_pos[6];  // 6個軸當前關節位置，單位deg 
      double  tl_cur_pos[6];  // 工具當前位置
            // tl_cur_pos[0]，沿x軸位置，單位mm，
            // tl_cur_pos[1]，沿y軸位置，單位mm，
            // tl_cur_pos[2]，沿z軸位置，單位mm，
            // tl_cur_pos[3]，繞固定軸X旋轉角度，單位deg
            // tl_cur_pos[4]，繞固定軸y旋轉角度，單位deg
            // tl_cur_pos[5]，繞固定軸z旋轉角度，單位deg 
      double  flange_cur_pos[6]; // 末端法蘭當前位置
            // flange_cur_pos[0]，沿x軸位置，單位mm，
            // flange_cur_pos[1]，沿y軸位置，單位mm，
            // flange_cur_pos[2]，沿z軸位置，單位mm，
            // flange_cur_pos[3]，繞固定軸X旋轉角度，單位deg
            // flange_cur_pos[4]，繞固定軸y旋轉角度，單位deg
            // flange_cur_pos[5]，繞固定軸z旋轉角度，單位deg
      double  actual_qd[6];   // 當前6個關節速度，單位deg/s 
      double  actual_qdd[6];   // 當前6個關節加速度，單位deg/s^2 
      double  target_TCP_CmpSpeed[2]; 
            // target_TCP_CmpSpeed[0]，TCP合成指令速度(位置)，單位mm/s
            // target_TCP_CmpSpeed[1]，TCP合成指令速度(姿態)，單位deg/s */
      double  target_TCP_Speed[6];  // TCP指令速度
              // target_TCP_Speed[0]，沿x軸速度，單位mm/s，
              // target_TCP_Speed[1]，沿y軸速度，單位mm/s，
              // target_TCP_Speed[2]，沿z軸速度，單位mm/s，
              // target_TCP_Speed[3]，繞固定軸X旋轉角速度，單位deg/s
              // target_TCP_Speed[4]，繞固定軸y旋轉角速度，單位deg/s
              // target_TCP_Speed[5]，繞固定軸z旋轉角速度，單位deg/s */
      double  actual_TCP_CmpSpeed[2]; 
              // actual_TCP_CmpSpeed[0]，TCP合成實際速度(位置)，單位mm/s
              // actual_TCP_CmpSpeed[1]，TCP合成實際速度(姿態)，單位deg/s 
      double  actual_TCP_Speed[6];  // TCP實際速度
              // actual_TCP_Speed[0]，沿x軸速度，單位mm/s，
              // actual_TCP_Speed[1]，沿y軸速度，單位mm/s，
              // actual_TCP_Speed[2]，沿z軸速度，單位mm/s，
              // actual_TCP_Speed[3]，繞固定軸X旋轉角速度，單位deg/s
              // actual_TCP_Speed[4]，繞固定軸y旋轉角速度，單位deg/s
              // actual_TCP_Speed[5]，繞固定軸z旋轉角速度，單位deg/s 
      double  jt_cur_tor[6];   // 6個軸當前扭矩，單位N·m 
      int   tool;        // 應用的工具座標系編號 
      int   user;        // 應用的工件座標系編號 
      uint8_t cl_dgt_output_h;  // 控制箱數字量IO輸出15-8 
      uint8_t cl_dgt_output_l;  // 控制箱數字量IO輸出7-0 
      uint8_t tl_dgt_output_l;  // 工具數字量IO輸出7-0，僅bit0-bit1有效 
      uint8_t cl_dgt_input_h;   // 控制箱數字量IO輸入15-8 
      uint8_t cl_dgt_input_l;   // 控制箱數字量IO輸入7-0 
      uint8_t tl_dgt_input_l;   // 工具數字量IO輸入7-0，僅bit0-bit1有效 
      uint16_t cl_analog_input[2]; // cl_analog_input[0]，控制箱模擬量輸入0
                    //cl_analog_input[1]，控制箱模擬量輸入1 
      uint16_t tl_anglog_input;  // 工具模擬量輸入 
      double  ft_sensor_raw_data[6]; // 力矩感測器原始數據
              // ft_sensor_raw_data[0]，沿x軸力，單位N
              // ft_sensor_raw_data[1]，沿y軸力，單位N
              // ft_sensor_raw_data[2]，沿z軸力，單位N
              // ft_sensor_raw_data[3]，沿x軸力矩，單位Nm
              // ft_sensor_raw_data[4]，沿y軸力矩，單位Nm
              // ft_sensor_raw_data[5]，沿z軸力矩，單位Nm 
      double  ft_sensor_data[6];   // 力矩感測器數據，
              // ft_sensor_data[0]，沿x軸力，單位N
              // ft_sensor_data[1]，沿y軸力，單位N
              // ft_sensor_data[2]，沿z軸力，單位N
              // ft_sensor_data[3]，沿x軸力矩，單位Nm
              // ft_sensor_data[4]，沿y軸力矩，單位Nm
              // ft_sensor_data[5]，沿z軸力矩，單位Nm 
      uint8_t ft_sensor_active;  // 力矩感測器激活狀態，0-復位，1-激活 
      uint8_t EmergencyStop;   // 急停標誌，0-急停未按下，1-急停按下 
      int   motion_done;    // 運動到位信號，1-到位，0-未到位 
      uint8_t gripper_motiondone; // 夾爪運動完成信號，1-完成，0-未完成 
      int   mc_queue_len;    // 運動指令隊列長度 
      uint8_t collisionState;   // 碰撞檢測，1-碰撞，0-無碰撞 
      int   trajectory_pnum;  // 軌跡點編號 
      uint8_t safety_stop0_state; // 安全停止信號SI0 
      uint8_t safety_stop1_state; // 安全停止信號SI1 
      uint8_t gripper_fault_id;  // 錯誤夾爪號 
      uint16_t gripper_fault;   // 夾爪故障 
      uint16_t gripper_active;   // 夾爪激活狀態 
      uint8_t gripper_position;  // 夾爪位置 
      int8_t  gripper_speed;   // 夾爪速度 
      int8_t  gripper_current;  // 夾爪電流 
      int   gripper_temp;    // 夾爪溫度 
      int   gripper_voltage;  // 夾爪電壓 
      robot_aux_state aux_state;  // 485擴展軸狀態
      EXT_AXIS_STATUS extAxisStatus[4]; // UDP擴展軸狀態 
      uint16_t extDIState[8];    // 擴展DI輸入
      uint16_t extDOState[8];    // 擴展DO輸出
      uint16_t extAIState[4];    // 擴展AI輸入
      uint16_t extAOState[4];    // 擴展AO輸出
      int rbtEnableState;      // 機器人使能狀態
      double  jointDriverTorque[6];    // 機器人關節驅動器扭矩
      double  jointDriverTemperature[6];  // 機器人關節驅動器溫度
      RobotTime robotTime;      // 機器人系統時間
      int softwareUpgradeState;   // 機器人軟體升級狀態
      uint16_t endLuaErrCode;    // 末端LUA運行狀態
      uint16_t cl_analog_output[2]; // 控制箱模擬量輸出
      uint16_t tl_analog_output;   // 工具模擬量輸出
      float gripperRotNum;      // 旋轉夾爪當前旋轉圈數
      uint8_t gripperRotSpeed;    // 旋轉夾爪當前旋轉速度百分比
      uint8_t gripperRotTorque;   // 旋轉夾爪當前旋轉力矩百分比
      WELDING_BREAKOFF_STATE weldingBreakOffState; //焊接中斷狀態
      double jt_tgt_tor[6];         // 關節指令力矩
      int smartToolState;          // SmartTool手柄按鈕狀態
      float wideVoltageCtrlBoxTemp;     //寬電壓控制箱溫度
      uint16_t wideVoltageCtrlBoxFanCurrent;//寬電壓控制箱風扇電流(mA)
      double toolCoord[6];    //當前工具座標係數值；x,y,z,rx,ry,rz
      double wobjCoord[6];    //當前工件座標係數值；x,y,z,rx,ry,rz
      double extoolCoord[6];   //當前外部工具座標係數值；x,y,z,rx,ry,rz
      double exAxisCoord[6];   //當前擴展軸座標係數值；x,y,z,rx,ry,rz
      double load;        //負載質量
      double loadCog[3];     //負載質心
      double lastServoTarget[6]; //隊列中最後一個ServoJ目標位置
      int servoJCmdNum;      //servoJ指令計數
      double targetJointPos[6];  //6個關節指令位置，單位°
      double targetJointVel[6];  //6個關節指令速度，單位°/s
      double targetJointAcc[6];  //6個關節指令加速度，單位°/s2
      double targetJointCurrent[6]; //6個關節指令電流，單位A
      double actualJointCurrent[6]; //6個關節當前電流，單位A
      double actualTCPForce[6];  //機器人末端力矩Nm；x,y,z,rx,ry,rz
      double targetTCPPos[6];   //機器人TCP指令位置mm；x,y,z,rx,ry,rz
      uint8_t collisionLevel[6]; //機器人碰撞等級
      double speedScaleManual;  //手動模式全局速度百分比
      double speedScaleAuto;   //自動模式全局速度百分比
      int luaLineNum;       //當前lua程式運行行號
      uint8_t abnomalStop;    //0-無異常；1-有異常
      char currentLuaFileName[256]; //當前運行lua程式名稱
      uint8_t programTotalLine;  //lua程式總行數
      uint8_t safetyBoxSingal[6]; //機器人按鈕盒按鈕狀態
      double weldVoltage;     //焊接電壓 V
      double weldCurrent;     //焊接電流
      double weldTrackVel;    //焊縫跟蹤速度 mm/s
      uint8_t tpdException;    //TPD軌跡加載數量超限，0-未超限，1-超限 
      uint8_t alarmRebootRobot;  //警告，1-鬆開急停按鈕請斷電重啟控制箱，2-關節通訊異常請斷電重啟控制箱
      uint8_t modbusMasterConnect; //bit0-bit7位對應ModbusTCP的0-7主站連接狀態 0-未連接  1-連接
      uint8_t modbusSlaveConnect;  //ModbusTCP從站連接狀態 0-未連接；1-已連接
      uint8_t btnBoxStopSignal;   //按鈕盒急停信號，0-鬆開急停；1-按下急停
      uint8_t dragAlarm;      //拖動警告，當前處於自動模式,0-不報警，1-報警 ，2-位置反饋異常不切換
      uint8_t safetyDoorAlarm;   //安全門警告；0-安全門關閉；1-安全門打開
      uint8_t safetyPlaneAlarm;   //進入安全牆警告；0-未進入安全牆；1-已進入安全牆
      uint8_t motonAlarm;      //運動警告
      uint8_t interfaceAlarm;    //進入干涉區警告
      int udpCmdState;       //20007端口UDP通訊連接狀態
      uint8_t weldReadyState;    //焊機準備完成狀態
      uint8_t alarmCheckEmergStopBtn; //0-正常；1-通訊異常，檢查急停按鈕是否鬆開
      uint8_t tsTmCmdComError;   //0-正常；1-扭矩指令通訊失敗
      uint8_t tsTmStateComError;  //0-正常；1-扭矩狀態通訊失敗
      int ctrlBoxError;       //控制箱錯誤
      uint8_t safetyDataState;   //安全數據狀態標誌，0-正常，1-異常
      uint8_t forceSensorErrState; //力感測器連接超時故障；bit0-bit1對應力感測器ID1-ID2
      uint8_t ctrlOpenLuaErrCode[4]; //4個控制器外設協議錯誤碼(500錯誤碼)
      uint8_t strangePosFlag; //當前處於奇異位姿標誌；0-正常；1-奇異位姿
      uint8_t alarm;      //警告
      uint8_t driverAlarm;   //驅動器報警軸號
      uint8_t aliveSlaveNumError; //活動從站數量錯誤，0：正常；1：數量錯誤
      uint8_t slaveComError[8];  //從站錯誤，0：正常；1：從站掉線；2：從站狀態與設定值不一致；3：從站未配置；4：從站配置錯誤；5：從站初始化錯誤；6：從站郵箱通信初始化錯誤
      uint8_t cmdPointError;   //指令點錯誤
      uint8_t IOError;      //IO錯誤
      uint8_t gripperError;    //夾爪錯誤
      uint8_t fileError;     //文件錯誤
      uint8_t paraError;     //參數錯誤
      uint8_t exaxisOutLimitError;  //外部軸超出軟限位錯誤
      uint8_t driverComError[6];   //與驅動器通信故障
      uint8_t driverError;      //驅動器通信故障軸號
      uint8_t outSoftLimitError;   //超出軟限位故障
      char axleGenComData[130];   //機器人末端透傳反饋數據
      uint8_t socketConnTimeout;   //socket連接超時，bit0-bit4:socketID 1-4
      uint8_t socketReadTimeout;   //socket讀取超時，bit0-bit4:socketID 1-4
      uint8_t tsWebStateComErr;   //web-扭矩通訊失敗；0-正常；1-失敗
      uint8_t exaxisCoordID;     //擴展軸坐標系編號
      uint16_t check_sum;     // 和校驗
    }ROBOT_STATE_PKG;

機器人狀態反饋配置枚舉類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    enum class RobotState
    {
        ProgramState = 3,           // 程式運行狀態，1-停止；2-運行；3-暫停
        RobotState = 4,             // 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動
        MainCode = 5,               // 主故障碼
        SubCode = 6,                // 子故障碼
        RobotMode = 7,              // 機器人模式，1-手動模式；0-自動模式
        JointCurPos = 8,            // 6個軸當前關節位置，單位deg
        ToolCurPos = 9,             // 工具當前位置：[0]沿x軸位置(mm)，[1]沿y軸(mm)，[2]沿z軸(mm)，[3]繞固定軸X旋轉(deg)，[4]繞固定軸Y(deg)，[5]繞固定軸Z(deg)
        FlangeCurPos = 10,          // 末端法蘭當前位置：[0]沿x軸(mm)，[1]沿y軸(mm)，[2]沿z軸(mm)，[3]繞固定軸X(deg)，[4]繞固定軸Y(deg)，[5]繞固定軸Z(deg)
        ActualJointVel = 11,        // 當前6個關節速度，單位deg/s
        ActualJointAcc = 12,        // 當前6個關節加速度，單位deg/s^2
        TargetTCPCmpSpeed = 13,     // TCP合成指令速度：[0]位置(mm/s)，[1]姿態(deg/s)
        TargetTCPSpeed = 14,        // TCP指令速度：[0]沿x軸(mm/s)，[1]沿y軸(mm/s)，[2]沿z軸(mm/s)，[3]繞X角速度(deg/s)，[4]繞Y(deg/s)，[5]繞Z(deg/s)
        ActualTCPCmpSpeed = 15,     // TCP合成實際速度：[0]位置(mm/s)，[1]姿態(deg/s)
        ActualTCPSpeed = 16,        // TCP實際速度：[0]沿x軸(mm/s)，[1]沿y軸(mm/s)，[2]沿z軸(mm/s)，[3]繞X角速度(deg/s)，[4]繞Y(deg/s)，[5]繞Z(deg/s)
        ActualJointTorque = 17,     // 6個軸當前扭矩，單位N·m
        Tool = 18,                  // 應用的工具座標系編號
        User = 19,                  // 應用的工件座標系編號
        ClDgtOutputH = 20,          // 控制箱數字量IO輸出15-8
        ClDgtOutputL = 21,          // 控制箱數字量IO輸出7-0
        TlDgtOutputL = 22,          // 工具數字量IO輸出7-0，僅bit0-bit1有效
        ClDgtInputH = 23,           // 控制箱數字量IO輸入15-8
        ClDgtInputL = 24,           // 控制箱數字量IO輸入7-0
        TlDgtInputL = 25,           // 工具數字量IO輸入7-0，僅bit0-bit1有效
        ClAnalogInput = 26,         // 控制箱模擬量輸入：[0]通道0，[1]通道1
        TlAnalogInput = 27,         // 工具模擬量輸入
        FtSensorRawData = 28,       // 力矩感測器原始數據：[0]沿x軸力(N)，[1]沿y軸力(N)，[2]沿z軸力(N)，[3]沿x軸力矩(Nm)，[4]沿y軸(Nm)，[5]沿z軸(Nm)
        FtSensorData = 29,          // 力矩感測器數據（經處理）：[0]沿x軸力(N)，[1]沿y軸力(N)，[2]沿z軸力(N)，[3]沿x軸力矩(Nm)，[4]沿y軸(Nm)，[5]沿z軸(Nm)
        FtSensorActive = 30,        // 力矩感測器激活狀態，0-復位，1-激活
        EmergencyStop = 31,         // 急停標誌，0-急停未按下，1-急停按下
        MotionDone = 32,            // 運動到位信號，1-到位，0-未到位
        GripperMotiondone = 33,     // 夾爪運動完成信號，1-完成，0-未完成
        McQueueLen = 34,            // 運動指令隊列長度
        CollisionState = 35,        // 碰撞檢測，1-碰撞，0-無碰撞
        TrajectoryPnum = 36,        // 軌跡點編號
        SafetyStop0State = 37,      // 安全停止信號SI0
        SafetyStop1State = 38,      // 安全停止信號SI1
        GripperFaultId = 39,        // 錯誤夾爪號
        GripperFault = 40,          // 夾爪故障
        GripperActive = 41,         // 夾爪激活狀態
        GripperPosition = 42,       // 夾爪位置
        GripperSpeed = 43,          // 夾爪速度
        GripperCurrent = 44,        // 夾爪電流
        GripperTemp = 45,           // 夾爪溫度
        GripperVoltage = 46,        // 夾爪電壓
        AuxState = 47,              // 485擴展軸狀態
        ExtAxisStatus = 48,         // UDP擴展軸狀態（4個軸）
        ExtDIState = 49,            // 擴展DI輸入（8個）
        ExtDOState = 50,            // 擴展DO輸出（8個）
        ExtAIState = 51,            // 擴展AI輸入（4個）
        ExtAOState = 52,            // 擴展AO輸出（4個）
        RbtEnableState = 53,        // 機器人使能狀態
        JointDriverTorque = 54,     // 機器人關節驅動器扭矩（6個關節）
        JointDriverTemperature = 55,// 機器人關節驅動器溫度（6個關節）
        RobotTime = 56,             // 機器人系統時間
        SoftwareUpgradeState = 57,  // 機器人軟體升級狀態
        EndLuaErrCode = 58,         // 末端LUA運行狀態
        ClAnalogOutput = 59,        // 控制箱模擬量輸出（2個）
        TlAnalogOutput = 60,        // 工具模擬量輸出
        GripperRotNum = 61,         // 旋轉夾爪當前旋轉圈數
        GripperRotSpeed = 62,       // 旋轉夾爪當前旋轉速度百分比
        GripperRotTorque = 63,      // 旋轉夾爪當前旋轉力矩百分比
        WeldingBreakOffState = 64,  // 焊接中斷狀態
        TargetJointTorque = 65,     // 關節指令力矩（6個關節）
        SmartToolState = 66,        // SmartTool手柄按鈕狀態
        WideVoltageCtrlBoxTemp = 67,// 寬電壓控制箱溫度
        WideVoltageCtrlBoxFanCurrent = 68, // 寬電壓控制箱風扇電流(mA)
        ToolCoord = 69,             // 當前工具座標係數值：x,y,z,rx,ry,rz
        WobjCoord = 70,             // 當前工件座標係數值：x,y,z,rx,ry,rz
        ExtoolCoord = 71,           // 當前外部工具座標係數值：x,y,z,rx,ry,rz
        ExAxisCoord = 72,           // 當前擴展軸座標係數值：x,y,z,rx,ry,rz
        Load = 73,                  // 負載質量
        LoadCog = 74,               // 負載質心：x,y,z
        LastServoTarget = 75,       // 隊列中最後一個ServoJ目標位置（6個關節）
        ServoJCmdNum = 76,          // servoJ指令計數
        TargetJointPos = 77,        // 6個關節指令位置，單位°
        TargetJointVel = 78,        // 6個關節指令速度，單位°/s
        TargetJointAcc = 79,        // 6個關節指令加速度，單位°/s²
        TargetJointCurrent = 80,    // 6個關節指令電流，單位A
        ActualJointCurrent = 81,    // 6個關節當前電流，單位A
        ActualTCPForce = 82,        // 機器人末端力矩：x,y,z,rx,ry,rz，單位Nm
        TargetTCPPos = 83,          // 機器人TCP指令位置：x,y,z,rx,ry,rz，單位mm
        CollisionLevel = 84,        // 機器人碰撞等級（6個）
        SpeedScaleManual = 85,      // 手動模式全局速度百分比
        SpeedScaleAuto = 86,        // 自動模式全局速度百分比
        LuaLineNum = 87,            // 當前lua程式運行行號
        AbnomalStop = 88,           // 0-無異常；1-有異常
        CurrentLuaFileName = 89,    // 當前運行lua程式名稱
        ProgramTotalLine = 90,      // lua程式總行數
        SafetyBoxSingal = 91,       // 機器人按鈕盒按鈕狀態（6個）
        WeldVoltage = 92,           // 焊接電壓 V
        WeldCurrent = 93,           // 焊接電流
        WeldTrackVel = 94,          // 焊縫跟蹤速度 mm/s
        TpdException = 95,          // TPD軌跡加載數量超限，0-未超限，1-超限
        AlarmRebootRobot = 96,      // 警告：1-鬆開急停後需斷電重啟，2-關節通訊異常需斷電重啟
        ModbusMasterConnect = 97,   // bit0-7對應ModbusTCP主站0-7連接狀態，0-未連接，1-連接
        ModbusSlaveConnect = 98,    // ModbusTCP從站連接狀態，0-未連接，1-已連接
        BtnBoxStopSignal = 99,      // 按鈕盒急停信號，0-鬆開急停，1-按下急停
        DragAlarm = 100,            // 拖動警告：0-不報警，1-報警，2-位置反饋異常不切換
        SafetyDoorAlarm = 101,      // 安全門警告：0-關閉，1-打開
        SafetyPlaneAlarm = 102,     // 安全牆警告：0-未進入，1-已進入
        MotonAlarm = 103,           // 運動警告
        InterfaceAlarm = 104,       // 進入干涉區警告
        UdpCmdState = 105,          // 20007端口UDP通訊連接狀態
        WeldReadyState = 106,       // 焊機準備完成狀態
        AlarmCheckEmergStopBtn = 107, // 0-正常；1-通訊異常，檢查急停按鈕
        TsTmCmdComError = 108,      // 0-正常；1-扭矩指令通訊失敗
        TsTmStateComError = 109,    // 0-正常；1-扭矩狀態通訊失敗
        CtrlBoxError = 110,         // 控制箱錯誤
        SafetyDataState = 111,      // 安全數據狀態，0-正常，1-異常
        ForceSensorErrState = 112,  // 力感測器連接超時，bit0-bit1對應ID1-ID2
        CtrlOpenLuaErrCode = 113,   // 4個控制器外設協議錯誤碼(500錯誤碼)
        StrangePosFlag = 114,       // 奇異位姿標誌：0-正常，1-奇異位姿
        Alarm = 115,                // 警告
        DriverAlarm = 116,          // 驅動器報警軸號
        AliveSlaveNumError = 117,   // 活動從站數量錯誤：0-正常，1-數量錯誤
        SlaveComError = 118,        // 從站錯誤：0-正常，1-掉線，2-狀態不一致，3-未配置，4-配置錯誤，5-初始化錯誤，6-郵箱通信初始化錯誤
        CmdPointError = 119,        // 指令點錯誤
        IOError = 120,              // IO錯誤
        GripperError = 121,         // 夾爪錯誤
        FileError = 122,            // 文件錯誤
        ParaError = 123,            // 參數錯誤
        ExaxisOutLimitError = 124,  // 外部軸超出軟限位錯誤
        DriverComError = 125,       // 與驅動器通信故障（6個軸）
        DriverError = 126,          // 驅動器通信故障軸號
        OutSoftLimitError = 127,    // 超出軟限位故障
        AxleGenComData = 128,       // 機器人末端透傳反饋數據
        SocketConnTimeout = 129,    // socket連接超時，bit0-bit4對應socketID 1-4
        SocketReadTimeout = 130,    // socket讀取超時，bit0-bit4對應socketID 1-4
        TsWebStateComErr = 131,     // web-扭矩通訊失敗：0-正常，1-失敗
        ExaxisCoordID = 132          //擴展軸坐標系編號
    };