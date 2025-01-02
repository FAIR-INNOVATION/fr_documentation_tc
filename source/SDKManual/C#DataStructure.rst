数据结构说明
================

.. toctree:: 
    :maxdepth: 5

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 关节位置数据类型 
    */  
    struct JointPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
        public double[] jPos;   /* 六个关节位置，单位deg */
    }

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    struct DescTran
    {
        public double x;    /* x轴坐标，单位mm  */
        public double y;    /* y轴坐标，单位mm  */
        public double z;    /* z轴坐标，单位mm  */
    }

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    struct Rpy
    {
    public double rx;   /* 绕固定轴X旋转角度，单位：deg  */
    public double ry;   /* 绕固定轴Y旋转角度，单位：deg  */
    public double rz;   /* 绕固定轴Z旋转角度，单位：deg  */
    }

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    struct DescPose
    {
        public DescTran tran;     /* 笛卡尔空间位置  */
        public Rpy rpy;			/* 笛卡尔空间姿态  */
    }

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
    */
    struct ExaxisPos
    {
        [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
        public double[] ePos;   /* 四个扩展轴位置，单位mm */
    }

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    struct ForceTorque
    {
        public double fx;  /* 沿x轴受力分量，单位N  */
        public double fy;  /* 沿y轴受力分量，单位N  */
        public double fz;  /* 沿z轴受力分量，单位N  */
        public double tx;  /* 绕x轴力矩分量，单位Nm */
        public double ty;  /* 绕y轴力矩分量，单位Nm */
        public double tz;  /* 绕z轴力矩分量，单位Nm */
    }

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  螺旋参数数据类型
    */
    struct SpiralParam
    {
        public int circle_num;         	  /* 螺旋圈数  */
        public float circle_angle;         /* 螺旋倾角  */
        public float rad_init;             /* 螺旋初始半径，单位mm  */
        public float rad_add;              /* 半径增量  */
        public float rotaxis_add;          /* 转轴方向增量  */
        public uint rot_direction;         /* 旋转方向，0-顺时针，1-逆时针  */
    }

扩展轴状态类型
+++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /**
    * @brief  扩展轴状态类型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_AUX_STATE
    {
        public byte servoId;           //伺服驱动器ID号
        public int servoErrCode;       //伺服驱动器故障码
        public int servoState;         //伺服驱动器状态
        public double servoPos;        //伺服当前位置
        public float servoVel;         //伺服当前速度
        public float servoTorque;      //伺服当前转矩
    }

机器人状态反馈结构体类型
+++++++++++++++++++++++++++
.. versionchanged:: C#SDK-v1.0.7

.. code-block:: c#
    :linenos:

    /**
    * @brief  机器人状态反馈结构体类型
    */
    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct ROBOT_STATE_PKG
    {
    public UInt16 frame_head;           //帧头 0x5A5A
    public byte frame_cnt;              //帧计数
    public UInt16 data_len;             //数据长度  5
    public byte program_state;          //程序运行状态，1-停止；2-运行；3-暂停
    public byte robot_state;            //机器人运动状态，1-停止；2-运行；3-暂停；4-拖动  
    public int main_code;               //主故障码
    public int sub_code;                //子故障码
    public byte robot_mode;             //机器人模式，0-自动模式；1-手动模式 16

    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jt_cur_pos;                             //关节当前位置
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] tl_cur_pos;                             //工具当前位姿
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] flange_cur_pos;                         //末端法兰当前位姿
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_qd;                              //机器人当前关节速度
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_qdd;                             //机器人当前关节加速度  
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public double[] target_TCP_CmpSpeed;                  //机器人TCP合成指令速度                         
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] target_TCP_Speed;                       //机器人TCP指令速度                        
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public double[] actual_TCP_CmpSpeed;                 //机器人TCP合成实际速度                        
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] actual_TCP_Speed;                       //机器人TCP实际速度                      
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] jt_cur_tor;                             //当前扭矩         
    public int tool;                        //工具号
    public int user;                        //工件号
    public byte cl_dgt_output_h;            //数字输出15-8
    public byte cl_dgt_output_l;            //数字输出7-0
    public byte tl_dgt_output_l;            //工具数字输出7-0(仅bit0-bit1有效)
    public byte cl_dgt_input_h;             //数字输入15-8
    public byte cl_dgt_input_l;             //数字输入7-0
    public byte tl_dgt_input_l;             //工具数字输入7-0(仅bit0-bit1有效)                    
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public UInt16[] cl_analog_input;        //控制箱模拟量输入
    public UInt16 tl_anglog_input;          //工具模拟量输入                              
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] ft_sensor_raw_data;     //力/扭矩传感器原始数据
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
    public double[] ft_sensor_data;         //力/扭矩传感器数据                           
    public byte ft_sensor_active;           //力/扭矩传感器激活状态， 0-复位，1-激活
    public byte EmergencyStop;              //急停标志
    public int motion_done;                 //到位信号
    public byte gripper_motiondone;         //夹爪运动完成信号
    public int mc_queue_len;                //运动队列长度
    public byte collisionState;             //碰撞检测，1-碰撞；0-无碰撞
    public int trajectory_pnum;             //轨迹点编号
    public byte safety_stop0_state;  /* 安全停止信号SI0 */
    public byte safety_stop1_state;  /* 安全停止信号SI1 */
    public byte gripper_fault_id;    /* 错误夹爪号 */               
    public UInt16 gripper_fault;     /* 夹爪故障 */
    public UInt16 gripper_active;    /* 夹爪激活状态 */
    public byte gripper_position;    /* 夹爪位置 */
    public byte gripper_speed;       /* 夹爪速度 */
    public byte gripper_current;     /* 夹爪电流 */
    public int gripper_tmp;          /* 夹爪温度 */
    public int gripper_voltage;      /* 夹爪电压 */                 
    public ROBOT_AUX_STATE auxState; /* 485扩展轴状态 */ 
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public EXT_AXIS_STATUS[] extAxisStatus;  /* UDP扩展轴状态 */
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
    public UInt16[] extDIState;//扩展DI输入
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 8)]
    public UInt16[] extDOState;//扩展DO输出
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public UInt16[] extAIState;//扩展AI输入
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
    public UInt16[] extAOState;//扩展AO输出           
    public UInt16 check_sum;         /* 和校验 */                  
    }