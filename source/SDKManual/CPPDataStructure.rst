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
        uint16_t frame_head;      /* 幀頭，約定爲0x5A5A */
        uint8_t  frame_cnt;       /* 幀計數，循環計數0-255 */
        uint16_t data_len;        /* 數據內容的長度 */
        uint8_t  program_state;   /* 程序運行狀態，1-停止；2-運行；3-暫停；*/
        uint8_t  robot_state;     /* 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動 */
        int      main_code;       /* 主故障碼 */
        int      sub_code;        /* 子故障碼 */
        uint8_t  robot_mode;      /* 機器人模式，1-手動模式；0-自動模式； */
        double   jt_cur_pos[6];   /* 6個軸當前關節位置，單位deg */
        double   tl_cur_pos[6];   /* 工具當前位置
                                     tl_cur_pos[0]，沿x軸位置，單位mm，
                                     tl_cur_pos[1]，沿y軸位置，單位mm，
                                     tl_cur_pos[2]，沿z軸位置，單位mm，
                                     tl_cur_pos[3]，繞固定軸X旋轉角度，單位deg
                                     tl_cur_pos[4]，繞固定軸y旋轉角度，單位deg
                                     tl_cur_pos[5]，繞固定軸z旋轉角度，單位deg */
        double   flange_cur_pos[6]; /* 末端法蘭當前位置
                                       flange_cur_pos[0]，沿x軸位置，單位mm，
                                       flange_cur_pos[1]，沿y軸位置，單位mm，
                                       flange_cur_pos[2]，沿z軸位置，單位mm，
                                     flange_cur_pos[3]，繞固定軸X旋轉角度，單位deg
                                     flange_cur_pos[4]，繞固定軸y旋轉角度，單位deg
                                    flange_cur_pos[5]，繞固定軸z旋轉角度，單位deg */
        double   actual_qd[6];      /* 當前6個關節速度，單位deg/s */
        double   actual_qdd[6];     /* 當前6個關節加速度，單位deg/s^2 */
        double   target_TCP_CmpSpeed[2]; /* target_TCP_CmpSpeed[0]，TCP合成指令速度(位置)，單位mm/s
                       target_TCP_CmpSpeed[1]，TCP合成指令速度(姿態)，單位deg/s  */
        double   target_TCP_Speed[6];   /* TCP指令速度
                                target_TCP_Speed[0]，沿x軸速度，單位mm/s，
                                target_TCP_Speed[1]，沿y軸速度，單位mm/s，
                                target_TCP_Speed[2]，沿z軸速度，單位mm/s，
                                target_TCP_Speed[3]，繞固定軸X旋轉角速度，單位deg/s
                                target_TCP_Speed[4]，繞固定軸y旋轉角速度，單位deg/s
                              target_TCP_Speed[5]，繞固定軸z旋轉角速度，單位deg/s */
        double   actual_TCP_CmpSpeed[2];/* actual_TCP_CmpSpeed[0]，TCP合成實際速度(位置)，單位mm/s
                     actual_TCP_CmpSpeed[1]，TCP合成實際速度(姿態)，單位deg/s */
        double   actual_TCP_Speed[6];   /* TCP實際速度
                          actual_TCP_Speed[0]，沿x軸速度，單位mm/s，
                          actual_TCP_Speed[1]，沿y軸速度，單位mm/s，
                          actual_TCP_Speed[2]，沿z軸速度，單位mm/s，
                          actual_TCP_Speed[3]，繞固定軸X旋轉角速度，單位deg/s
                          actual_TCP_Speed[4]，繞固定軸y旋轉角速度，單位deg/s
                          actual_TCP_Speed[5]，繞固定軸z旋轉角速度，單位deg/s */
        double   jt_cur_tor[6];      /* 6個軸當前扭矩，單位N·m */
        int      tool;               /* 應用的工具座標系編號 */
        int      user;               /* 應用的工件座標系編號 */
        uint8_t  cl_dgt_output_h;    /* 控制箱數字量IO輸出15-8 */
        uint8_t  cl_dgt_output_l;    /* 控制箱數字量IO輸出7-0 */
        uint8_t  tl_dgt_output_l;    /* 工具數字量IO輸出7-0，僅bit0-bit1有效 */
        uint8_t  cl_dgt_input_h;     /* 控制箱數字量IO輸入15-8 */
        uint8_t  cl_dgt_input_l;     /* 控制箱數字量IO輸入7-0 */
        uint8_t  tl_dgt_input_l;     /* 工具數字量IO輸入7-0，僅bit0-bit1有效 */
        uint16_t cl_analog_input[2]; /* cl_analog_input[0]，控制箱模擬量輸入0
                                        cl_analog_input[1]，控制箱模擬量輸入1 */
        uint16_t tl_anglog_input;    /* 工具模擬量輸入 */
        double   ft_sensor_raw_data[6]; /* 力矩傳感器原始數據
                                           ft_sensor_raw_data[0]，沿x軸力，單位N
                                           ft_sensor_raw_data[1]，沿y軸力，單位N
                                           ft_sensor_raw_data[2]，沿z軸力，單位N
                                   ft_sensor_raw_data[3]，沿x軸力矩，單位Nm
                                   ft_sensor_raw_data[4]，沿y軸力矩，單位Nm
                                   ft_sensor_raw_data[5]，沿z軸力矩，單位Nm */
        double   ft_sensor_data[6];     /* 力矩傳感器數據，
                                           ft_sensor_data[0]，沿x軸力，單位N
                                           ft_sensor_data[1]，沿y軸力，單位N
                                           ft_sensor_data[2]，沿z軸力，單位N
                                           ft_sensor_data[3]，沿x軸力矩，單位Nm
                                           ft_sensor_data[4]，沿y軸力矩，單位Nm
                                           ft_sensor_data[5]，沿z軸力矩，單位Nm */
        uint8_t  ft_sensor_active;   /* 力矩傳感器激活狀態，0-復位，1-激活 */
        uint8_t  EmergencyStop;      /* 急停標誌，0-急停未按下，1-急停按下 */
        int      motion_done;        /* 運動到位信號，1-到位，0-未到位 */
        uint8_t  gripper_motiondone; /* 夾爪運動完成信號，1-完成，0-未完成 */
        int      mc_queue_len;       /* 運動指令隊列長度 */
        uint8_t  collisionState;     /* 碰撞檢測，1-碰撞，0-無碰撞 */
        int      trajectory_pnum;    /* 軌跡點編號 */
        uint8_t  safety_stop0_state; /* 安全停止信號SI0 */
        uint8_t  safety_stop1_state; /* 安全停止信號SI1 */
        uint8_t  gripper_fault_id;   /* 錯誤夾爪號 */
        uint16_t gripper_fault;      /* 夾爪故障 */
        uint16_t gripper_active;     /* 夾爪激活狀態 */
        uint8_t  gripper_position;   /* 夾爪位置 */
        int8_t   gripper_speed;       /* 夾爪速度 */
        int8_t   gripper_current;     /* 夾爪電流 */
        int      gripper_temp;        /* 夾爪溫度 */
        int      gripper_voltage;     /* 夾爪電壓 */
        robot_aux_state aux_state;
        EXT_AXIS_STATUS extAxisStatus[4];  /* UDP擴展軸狀態 */
        uint16_t extDIState[8];        //擴展DI輸入
        uint16_t extDOState[8];        //擴展DO輸出
        uint16_t extAIState[4];        //擴展AI輸入
        uint16_t extAOState[4];        //擴展AO輸出
        int rbtEnableState;            //機器人使能狀態               
        double   jointDriverTorque[6];        //機器人關節驅動器扭矩    
        double   jointDriverTemperature[6];   //機器人關節驅動器溫度   
        RobotTime robotTime;           //機器人系統時間                
        int softwareUpgradeState;      //機器人軟件升級狀態            
        uint16_t endLuaErrCode;        //末端LUA運行狀態            
        uint16_t cl_analog_output[2];  //控制箱模擬量輸出               
        uint16_t tl_analog_output;     //工具模擬量輸出            
        float gripperRotNum;           //旋轉夾爪當前旋轉圈數 
        uint8_t gripperRotSpeed;       //旋轉夾爪當前旋轉速度百分比
        uint8_t gripperRotTorque;      //旋轉夾爪當前旋轉力矩百分比
        WELDING_BREAKOFF_STATE weldingBreakOffState;  //焊接中斷狀態
        double jt_tgt_tor[6];          //關節指令力矩
        int smartToolState;            //SmartTool手柄按鈕狀態
        float wideVoltageCtrlBoxTemp;        //寬電壓控制箱溫度
        uint16_t wideVoltageCtrlBoxFanCurrent;   //寬電壓控制箱風扇電流(mA)
        double toolCoord[6];      //工具座標系
        double wobjCoord[6];      //工件座標系
        double extoolCoord[6];     //外部工具座標系
        double exAxisCoord[6];     //擴充軸座標系
        double load;          //負載質量
        double loadCog[3];       //負載質心
        double lastServoTarget[6];  //队列中最后一个ServoJ目标位置
        int servoJCmdNum;           //servoJ指令計數
        uint16_t check_sum;      /* 和校驗 */
    }ROBOT_STATE_PKG;