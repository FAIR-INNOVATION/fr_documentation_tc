机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取机器人安装角度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人安装角度
    * @param  [out] yangle 倾斜角
    * @param  [out] zangle 旋转角
    * @return  错误码
    */
    int GetRobotInstallAngle(ref double yangle, ref double zangle); 

获取系统变量值
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取系统变量值
    * @param  [in] id 系统变量编号，范围[1~20]
    * @param  [out] value  系统变量值
    * @return  错误码
    */
    int GetSysVarValue(int id, ref double value); 

获取当前关节位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前关节位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六个关节位置，单位deg
    * @return  错误码
    */
    int GetActualJointPosDegree(byte flag, ref JointPos jPos); 

获取当前关节位置(弧度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前关节位置(弧度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六个关节位置，单位rad
    * @return  错误码
    */   
    int GetActualJointPosRadian(byte flag, ref JointPos jPos);

获取关节反馈速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取关节反馈速度-deg/s 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed 六个关节速度 
    * @return 错误码 
    */
    int GetActualJointSpeedsDegree(byte flag, ref double[] speed);

获取关节反馈加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取关节反馈加速度-deg/s^2 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] acc 六个关节加速度 
    * @return 错误码 
    */
    int GetActualJointAccDegree(byte flag, ref double[] acc); 

获取TCP指令速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP指令速度-合速度 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 线性速度 
    * @param [out] ori_speed 姿态速度 
    * @return 错误码 
    */
    int GetTargetTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed); 

获取TCP反馈速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 获取TCP反馈速度-合速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 线性速度 
    * @param [out] ori_speed 姿态速度 
    * @return 错误码 
    */
    int GetActualTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed);

获取TCP指令速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP指令速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 错误码 
    */
    int GetTargetTCPSpeed(byte flag, ref double[] speed);

获取TCP反馈速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取TCP反馈速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 错误码 
    */
    int GetActualTCPSpeed(byte flag, ref double[] speed);

获取当前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  错误码
    */
    int GetActualTCPPose(byte flag, ref DescPose desc_pos); 

获取当前工具坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具坐标系编号
    * @return  错误码
    */
    int GetActualTCPNum(byte flag, ref int id);  

获取当前工件坐标系编号
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工件坐标系编号
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件坐标系编号
    * @return  错误码
    */
    int GetActualWObjNum(byte flag, ref int id);

获取当前末端法兰位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前末端法兰位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法兰位姿
    * @return  错误码
    */
    int GetActualToolFlangePose(byte flag, ref DescPose desc_pos);   

逆运动学求解
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆运动学求解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] config 关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos);

逆运动学求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置求解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */   
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos); 

逆运动学求解（参考指定关节位置）
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置判断是否有解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @param  [out] result 0-无解，1-有解
    * @return  错误码
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref JointPos joint_pos); 

判断逆运动学是否有解 
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 逆运动学求解，判断指定参考关节位置是否有解
    * @param [in] posMode 0绝对位姿，1相对位姿-基坐标系，2相对位姿-工具坐标系 
    * @param [in] desc_pos 笛卡尔位姿 
    * @param [in] joint_pos_ref 参考关节位置 
    * @param [out] hasResult 0-无解，1-有解 
    * @return 错误码 
    */ 
    int GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref bool hasResult);  

正运动学求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  正运动学求解
    * @param  [in] joint_pos 关节位置
    * @param  [out] desc_pos 笛卡尔位姿
    * @return  错误码
    */
    int GetForwardKin(JointPos joint_pos, ref DescPose desc_pos); 

获取当前关节转矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 获取当前关节转矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 关节转矩
    * @return  错误码
    */
    int GetJointTorques(byte flag, float[] torques); 

获取当前负载的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前负载的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 负载重量，单位kg
    * @return  错误码
    */
    int GetTargetPayload(byte flag, ref double weight); 

获取当前负载的质心
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前负载的质心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 负载质心，单位mm
    * @return  错误码
    */   
    int GetTargetPayloadCog(byte flag, ref DescTran cog);

获取当前工具坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工具坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐标系位姿
    * @return  错误码
    */
    int GetTCPOffset(byte flag, ref DescPose desc_pos); 

获取当前工件坐标系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前工件坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件坐标系位姿
    * @return  错误码
    */   
    int GetWObjOffset(byte flag, ref DescPose desc_pos); 

获取关节软限位角度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取关节软限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞    
    * @param  [out] negative  负限位角度，单位deg
    * @param  [out] positive  正限位角度，单位deg
    * @return  错误码
    */
    int GetJointSoftLimitDeg(byte flag, ref double[] negative, ref double[] positive); 

获取系统时间
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取系统时间
    * @param  [out] t_ms 单位ms
    * @return  错误码
    */
    int GetSystemClock(ref double t_ms);

获取机器人当前关节配置
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人当前关节位置
    * @param  [out]  config  关节空间配置，范围[0~7]
    * @return  错误码
    */
    int GetRobotCurJointsConfig(ref int config);

获取当前速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人当前速度
    * @param  [out]  vel  速度，单位mm/s
    * @return  错误码
    */   
    int GetDefaultTransVel(ref double vel); 

查询机器人运动是否完成
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查询机器人运动是否完成
    * @param  [out]  state  0-未完成，1-完成
    * @return  错误码
    */   
    int GetRobotMotionDone(ref byte state);

代码示例
+++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotState_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        double yangle = 0, zangle = 0;
        byte flag = 0;
        JointPos j_deg = new JointPos(0, 0, 0, 0, 0, 0);
        JointPos j_rad = new JointPos(0, 0, 0, 0, 0, 0);
        DescPose tcp, flange, tcp_offset, wobj_offset;
        DescTran cog;
        tcp = new DescPose();
        flange = new DescPose();
        tcp_offset = new DescPose();
        wobj_offset = new DescPose();
        cog = new DescTran();

        int id = 0;
        float[] torques = new float[6] { 0, 0, 0, 0, 0, 0};
        double weight = 0.0;
        double[] neg_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        double[] pos_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        double t_ms = 0;
        int config = 0;
        double vel = 0;

        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle:{yangle},zangle:{zangle}");

        robot.GetActualJointPosDegree(flag, ref j_deg);
        Console.WriteLine($"joint pos deg:{j_deg.jPos[0]}, {j_deg.jPos[1]}, {j_deg.jPos[2]}, {j_deg.jPos[3]},{j_deg.jPos[4]},{j_deg.jPos[5]}");
        robot.GetActualJointPosRadian(flag, ref j_rad);
        Console.WriteLine($"joint pos rad:{j_rad.jPos[0]}, {j_rad.jPos[1]}, {j_rad.jPos[2]},{j_rad.jPos[3]},{j_rad.jPos[4]},{j_rad.jPos[5]}");

        robot.GetActualTCPPose(flag, ref tcp);
        Console.WriteLine($"tcp pose:{tcp.tran.x}, {tcp.tran.y}, {tcp.tran.z}, {tcp.rpy.rx}, {tcp.rpy.ry},{tcp.rpy.rz}");

        robot.GetActualToolFlangePose(flag, ref flange);
        Console.WriteLine($"flange pose:{flange.tran.x}, {flange.tran.y}, {flange.tran.z}, {flange.rpy.rx},{flange.rpy.ry},{flange.rpy.rz}");

        robot.GetActualTCPNum(flag, ref id);
        Console.WriteLine($"tcp num : {id}");

        robot.GetActualWObjNum(flag, ref id);
        Console.WriteLine($"wobj num : {id}");

        robot.GetJointTorques(flag, torques);
        Console.WriteLine($"torques:{torques[0]},{torques[1]},{torques[2]},{torques[3]},{torques[4]},{torques[5]}");

        robot.GetTargetPayload(flag, ref weight);
        Console.WriteLine($"payload weight : {weight}");

        robot.GetTargetPayloadCog(flag, ref cog);
        Console.WriteLine($"payload cog:{cog.x},{cog.y},{cog.z}");

        robot.GetTCPOffset(flag, ref tcp_offset);
        Console.WriteLine($"tcp offset:{tcp_offset.tran.x}, {tcp_offset.tran.y}, {tcp_offset.tran.z},{tcp_offset.rpy.rx},{tcp_offset.rpy.ry},{tcp_offset.rpy.rz}");

        robot.GetWObjOffset(flag, ref wobj_offset);
        Console.WriteLine($"wobj offset:{wobj_offset.tran.x}, {wobj_offset.tran.y},{wobj_offset.tran.z},{wobj_offset.rpy.rx},{wobj_offset.rpy.ry},{wobj_offset.rpy.rz}");

        robot.GetJointSoftLimitDeg(flag, ref neg_deg, ref pos_deg);
        Console.WriteLine($"neg limit deg:{neg_deg[0]}, {neg_deg[1]}, {neg_deg[2]}, {neg_deg[3]},{neg_deg[4]},{neg_deg[5]}");
        Console.WriteLine($"pos limit deg:{pos_deg[0]}, {pos_deg[1]}, {pos_deg[2]}, {pos_deg[3]},{pos_deg[4]},{pos_deg[5]}");

        robot.GetSystemClock(ref t_ms);
        Console.WriteLine($"system clock : {t_ms}");

        robot.GetRobotCurJointsConfig(ref config);
        Console.WriteLine($"joint config : {config}");

        robot.GetDefaultTransVel(ref vel);
        Console.WriteLine($"trans vel : {vel}");
    }

查询机器人错误码
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人错误码 
    * @param [out] maincode   主错误码
    * @param [out] subcode    子错误码
    * @return 错误码 
    */ 
    int GetRobotErrorCode(ref int maincode, ref int subcode); 

查询机器人示教管理点数据
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人示教管理点位数据 
    * @param [in] name    点位名
    * @param [out] data   点位数据double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool, wobj,speed,acc,e1,e2,e3,e4}
    * @return 错误码 
    */ 
    int GetRobotTeachingPoint(string name, ref double[] data); 

查询机器人运动队列缓存长度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查询机器人运动队列缓存长度 
    * @param [out] len   缓存长度
    * @return 错误码 
    */
    int GetMotionQueueLength(ref int len);

代码示例
+++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotState2_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte robotMotionState = 255;
        robot.GetRobotMotionDone(ref robotMotionState);
        Console.WriteLine($"robotMotionState  {robotMotionState}");

        int mainErrCode = -1;
        int subErrCode = -1;
        robot.GetRobotErrorCode(ref mainErrCode, ref subErrCode);
        Console.WriteLine($"mainErrCode  {mainErrCode}  subErrCode  {subErrCode} ");

        string name = "a1";
        double[] point = new double[6] {0, 0, 0, 0, 0, 0};
        robot.GetRobotTeachingPoint(name, ref point);
        Console.WriteLine($"GetRobotTeachingPoint:{point[0]},{point[1]},{point[2]},{point[3]},{point[4]},{point[5]}");

        int length = -1;
        robot.GetMotionQueueLength(ref length);
        Console.WriteLine($"GetMotionQueueLength  {length}");
    }

获取机器人实时状态结构体
++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人实时状态结构体
    * @param [out] pkg 机器人实时状态结构体 
    * @return 错误码 
    */
    int GetRobotRealTimeState(ref ROBOT_STATE_PKG pkg);

代码示例
+++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnGetState_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        ROBOT_STATE_PKG pKG = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pKG);
        Console.WriteLine($"the state is {pKG.main_code}");
    }