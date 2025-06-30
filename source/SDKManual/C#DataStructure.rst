資料結構說明
================

.. toctree:: 
    :maxdepth: 5

關節位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 關節位置資料類型 
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* 六個關節位置，單位deg */
    }

笛卡爾空間位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間位置資料類型
    */
    struct DescTran
    {
        public double x;    /* x軸座標，單位mm  */
        public double y;    /* y軸座標，單位mm  */
        public double z;    /* z軸座標，單位mm  */
    }

歐拉角姿態資料型態
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 歐拉角姿態資料型態
    */
    struct Rpy
    {
    public double rx;   /* 繞固定軸X旋轉角度，單位：deg  */
    public double ry;   /* 繞固定軸Y旋轉角度，單位：deg  */
    public double rz;   /* 繞固定軸Z旋轉角度，單位：deg  */
    }

笛卡爾空間位姿資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief 笛卡爾空間位姿資料類型
    */
    struct DescPose
    {
        public DescTran tran;     /* 笛卡兒空間位置  */
        public Rpy rpy;			/* 笛卡兒空間姿態  */
    }

擴展軸位置資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展軸位置資料類型
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* 四個擴展軸位置，單位mm */
    }

力矩感測器資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 力感測器的受力分量和力矩分量
    */
    struct ForceTorque
    {
        public double fx;  /* 沿x軸受力分量，單位N  */
        public double fy;  /* 沿y軸受力分量，單位N  */
        public double fz;  /* 沿z軸受力分量，單位N  */
        public double tx;  /* 绕x軸力矩分量，單位Nm */
        public double ty;  /* 绕y軸力矩分量，單位Nm */
        public double tz;  /* 绕z軸力矩分量，單位Nm */
    }

螺旋參數資料類型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  螺旋參數資料類型
    */
    struct SpiralParam
    {
        public int circle_num;         	  /* 螺旋圈數  */
        public float circle_angle;         /* 螺旋傾角  */
        public float rad_init;             /* 螺旋初始半徑，單位mm  */
        public float rad_add;              /* 半徑增量  */
        public float rotaxis_add;          /* 轉軸方向增量  */
        public uint rot_direction;         /* 旋轉方向，0-順時針，1-逆時針  */
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
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct WELDING_BREAKOFF_STATE
    {
        public byte breakOffState;  // 焊接中斷狀態
        public byte weldArcState;   // 焊接電弧中斷狀態
    }

機器人狀態回饋結構體類型
+++++++++++++++++++++++++++
.. versionchanged:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief  機器人狀態回饋結構體類型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_STATE_PKG
    {
    public UInt16 frame_head;           //幀頭 0x5A5A
    public byte frame_cnt;              //幀計數
    public UInt16 data_len;             //資料長度  5
    public byte program_state;          //程序運作狀態，1-停止；2-運轉；3-暫停
    public byte robot_state;            //機器人運動狀態，1-停止；2-運轉；3-暫停；4-拖曳
    public int main_code;               //主故障碼
    public int sub_code;                //子故障碼
    public byte robot_mode;             //機器人模式，0-自動模式；1-手動模式 16

    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jt_cur_pos;                             //關節目前位置
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] tl_cur_pos;                             //工具當前位姿
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] flange_cur_pos;                         //末端法蘭目前位姿
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_qd;                              //機器人目前關節速度
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_qdd;                             //機器人當前關節加速度  
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public double[] target_TCP_CmpSpeed;                  //機器人TCP合成指令速度                         
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] target_TCP_Speed;                       //機器人TCP指令速度                        
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public double[] actual_TCP_CmpSpeed;                 //機器人TCP合成實際速度                        
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_TCP_Speed;                       //機器人TCP實際速度                      
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jt_cur_tor;                             //當前扭矩         
    public int tool;                        //工具號
    public int user;                        //工件號
    public byte cl_dgt_output_h;            //數位輸出15-8
    public byte cl_dgt_output_l;            //數位輸出7-0
    public byte tl_dgt_output_l;            //工具數字輸出7-0(僅bit0-bit1有效)
    public byte cl_dgt_input_h;             //數位輸入15-8
    public byte cl_dgt_input_l;             //數位輸入7-0
    public byte tl_dgt_input_l;             //工具數字輸入7-0(僅bit0-bit1有效)                    
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public UInt16[] cl_analog_input;        //控制箱類比輸入
    public UInt16 tl_anglog_input;          //工具類比輸入                              
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] ft_sensor_raw_data;     //力/扭力感測器原始數據
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] ft_sensor_data;         //力/扭力感測器數據                           
    public byte ft_sensor_active;           //力/扭力感測器啟動狀態， 0-復位，1-激活
    public byte EmergencyStop;              //急停標誌
    public int motion_done;                 //到位訊號
    public byte gripper_motiondone;         //夾爪運動完成訊號
    public int mc_queue_len;                //運動隊列長度
    public byte collisionState;             //碰撞偵測，1-碰撞；0-無碰撞
    public int trajectory_pnum;             //軌跡點編號
    public byte safety_stop0_state;  /* 安全停止訊號SI0 */
    public byte safety_stop1_state;  /* 安全停止訊號SI2 */
    public byte gripper_fault_id;    /* 錯誤夾爪號 */               
    public UInt16 gripper_fault;     /* 夾爪故障 */
    public UInt16 gripper_active;    /* 夾爪激活狀態 */
    public byte gripper_position;    /* 夾爪位置 */
    public byte gripper_speed;       /* 夾爪速度 */
    public byte gripper_current;     /* 夾爪電流 */
    public int gripper_tmp;          /* 夾爪溫度 */
    public int gripper_voltage;      /* 夾爪電壓 */                 
    public ROBOT_AUX_STATE auxState; /* 485擴展軸狀態 */ 
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public EXT_AXIS_STATUS[] extAxisStatus;  /* UDP擴展軸狀態 */
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
    public UInt16[] extDIState;//擴充DI輸入
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
    public UInt16[] extDOState;//擴充DO輸入
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public UInt16[] extAIState;//擴充AI輸入
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public UInt16[] extAOState;//擴充AO輸入           
    public int rbtEnableState; //機器人啟用狀態--robot enable state
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jointDriverTorque; //關節驅動扭矩
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jointDriverTemperature; //關節驅動器溫度
    public ROBOT_TIME robotTime; //機器人系統時間
    public int softwareUpgradeState; //軟體升級狀態 0-空閒中或上傳升級包中；1~100：升級完成百分比；-1:升級軟體失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓縮失敗；-5：用戶升級失敗；-6：外設升級失敗；
    public UInt16 endLuaErrCode; //末端LUA運行狀態
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public UInt16[] cl_analog_output; //控制箱模擬量輸出 Control box analog output
    public UInt16 tl_analog_output; //工具類比量輸出 Tool analog output
    public float gripperRotNum; //旋轉夾爪目前旋轉圈數 The current number of turns of the rotating clamp
    public byte gripperRotSpeed; //旋轉夾爪當前旋轉速度百分比 Percentage of the current rotation speed of the rotary clamp
    public byte gripperRotTorque; //旋轉夾爪當前旋轉力矩百分比 Percentage of the current rotating torque of the rotating clamp
    public WELDING_BREAKOFF_STATE weldingBreakOffState;//焊接中斷狀態
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jt_tgt_tor;//关节指令力矩
    public int smartToolState; //SmartTool手柄按鈕狀態
    public UInt16 check_sum; /* 與校驗 */                // + 2 = 609                 
    }