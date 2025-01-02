机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取机器人安装角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人安装角度
    * @return  List[0]:错误码; List[1]:double yangle 倾斜角; List[2]:double zangle 旋转角
    */
    List<Number> GetRobotInstallAngle(); 

获取系统变量值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取系统变量值
    * @param  [in] id 系统变量编号，范围[1~20]
    * @return  List[0]:错误码; List[1]:double value 系统变量值
    */
    List<Number> GetSysVarValue(int id); 

获取当前关节位置(角度)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前关节位置(角度)
    * @param  [out] jPos 获取的六个关节位置，单位deg
    * @return  错误码
    */
    int GetActualJointPosDegree(JointPos jPos); 

获取关节反馈速度-deg/s
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取关节反馈速度-deg/s 
    * @param [out] speed 六个关节速度
    * @return 错误码 
    */
    int GetActualJointSpeedsDegree(Object[] speed);

获取当前工具位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工具位姿
    * @param  [out] desc_pos  工具位姿
    * @return  错误码
    */
    int GetActualTCPPose(DescPose desc_pos); 

逆运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解
    * @param  [in] type 0-绝对位姿(基坐标系)，1-增量位姿(基坐标系)，2-增量位姿(工具坐标系)
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] config 关节空间配置，[-1]-参考当前关节位置解算，[0~7]-依据特定关节空间配置求解
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, JointPos joint_pos);

逆运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置求解
    * @param  [in] posMode 0绝对位姿， 1相对位姿-基坐标系   2相对位姿-工具坐标系
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @param  [out] joint_pos 关节位置
    * @return  错误码
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, JointPos joint_pos); 

逆运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆运动学求解，参考指定关节位置判断是否有解
    * @param  [in] posMode 0绝对位姿， 1相对位姿-基坐标系   2相对位姿-工具坐标系
    * @param  [in] desc_pos 笛卡尔位姿
    * @param  [in] joint_pos_ref 参考关节位置
    * @return  错误码  List[0]:错误码; List[1]: int hasResult 0-无解，1-有解
    */   
    List<Integer> GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref);  

正运动学求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  正运动学求解
    * @param  [in] joint_pos 关节位置
    * @param  [out] desc_pos 笛卡尔位姿
    * @return  错误码
    */
    int GetForwardKin(JointPos joint_pos, DescPose desc_pos); 

获取当前关节转矩
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取当前关节转矩
    * @param  [in]  flag 0-阻塞，1-非阻塞
    * @param  [out]  torques 关节转矩
    * @return  错误码
    */
    int GetJointTorques(int flag, Object[] torques); 

获取当前负载的重量
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前负载的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @return  List[0]:int 错误码; List[1]: double weight  负载重量，单位kg
    */
    List<Number> GetTargetPayload(int flag); 

获取当前负载的质心
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前负载的质心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 负载质心，单位mm
    * @return  错误码
    */   
    int GetTargetPayloadCog(int flag, DescTran cog);

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.SetRobotInstallAngle(23.4, 56.7);
        List<Number> rtnArr =  robot.GetRobotInstallAngle();
        System.out.println("安装角度: " + rtnArr.get(1) + "  " + rtnArr.get(2));
        robot.SetRobotInstallAngle(0, 0);

        robot.SetLoadWeight(0);
        robot.SetLoadCoord(new DescTran(0.0, 0.0, 0.0));

        DescTran cog = new DescTran();
        robot.GetTargetPayloadCog(1, cog);

        System.out.println("weight is " + rtnArr.get(1) + " cog is  " + cog.x + "  " + cog.y + "  " + cog.z);

        List<Integer> Arr = robot.GetRobotCurJointsConfig();
        System.out.println("config is " + Arr.get(1));

        DescPose  desc_p1=new DescPose();

        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        JointPos JP_test=new JointPos();
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        robot.GetInverseKin(0, DP1, -1, JP_test);
        List<Integer> rtnArrInt =  robot.GetInverseKinHasSolution(0, DP1, JP1);//逆向是否有解
        System.out.println("has Solution ? " + rtnArrInt.get(1));
        robot.GetForwardKin(JP1, desc_p1);//正向运动学
        JointPos j2 = new JointPos();
        robot.GetInverseKinRef(0, DP1, JP1, JP_test);//逆向运动学
    }

获取当前工具坐标系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工具坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐标系位姿
    * @return  错误码
    */
    int GetTCPOffset(int flag, DescPose desc_pos); 

获取当前工件坐标系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前工件坐标系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件坐标系位姿
    * @return  错误码
    */   
    int GetWObjOffset(int flag, DescPose desc_pos); 

获取关节软限位角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取关节软限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] negative  负限位角度，单位deg
    * @param  [out] positive  正限位角度，单位deg
    * @return  错误码
    */
    int GetJointSoftLimitDeg(int flag, Object[] negative, Object[] positive); 

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        DescPose offset = new DescPose();
        robot.GetTCPOffset(1, offset);//工具
        System.out.println("offset is " + offset);
        robot.GetWObjOffset(1, offset);//工件
        System.out.println("offset is " + offset);

        Object[] neg_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        Object[] pos_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        robot.GetJointSoftLimitDeg(1,  neg_deg,  pos_deg);
        System.out.println("neg is " + Arrays.toString(neg_deg) + " pos is " + Arrays.toString(pos_deg));
    }

获取系统时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取系统时间
    * @return  List[0]:int 错误码; List[1]:double t_ms 单位ms
    */
    List<Number> GetSystemClock();

获取机器人当前关节配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人当前关节配置
    * @return  List[0]:int 错误码; List[1]:int config 关节空间配置，范围[0~7]
    */
    List<Integer> GetRobotCurJointsConfig();

获取机器人默认速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取机器人默认速度
    * @return  List[0]:int 错误码; List[1]: double vel 速度，单位mm/s
    */   
    List<Number> GetDefaultTransVel(); 

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        List<Integer> rtnArr = robot.GetRobotCurJointsConfig();
        System.out.println("config is " + rtnArr.get(1));

        List<Number> rtnArrN = robot.GetSystemClock();
        System.out.println("systom clock is  " + rtnArrN.get(1));

        rtnArrN = robot.GetDefaultTransVel();
        System.out.println("机器人当前速度为: " + rtnArrN.get(1));
    }

查询机器人示教管理点数据
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 查询机器人示教管理点位数据 
    * @param [in]  name  点位名
    * @return  List[0]:错误码; List[1] - List[20] : 点位数据double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4} 
    */ 
    List<Number> GetRobotTeachingPoint(String name); 

获取SSH公钥
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取SSH公钥 
    * @param [in] keygen 公钥 
    * @return 错误码    
    */ 
    List<Number> GetRobotTeachingPoint(String name); 

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算指定路径下文件的MD5值 
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt" 
    * @return 错误码   
    */ 
    int ComputeFileMD5(String file_path, String md5); 

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }

        List<Number> rtnArr = robot.GetRobotTeachingPoint("P1");
        System.out.println("point data  " + rtnArr);

        String[] key = {""};
        robot.GetSSHKeygen(key);
        System.out.println("ssh key  " + key[0]);
    }

获取机器人软件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人软件版本
    * @param [out] robotModel 机器人型号
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 错误码 
    */
    int GetSoftwareVersion(String robotModel, String webVersion, String controllerVersion);

获取机器人硬件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人硬件版本
    * @param [out] ctrlBoxBoardVersion 控制箱载板硬件版本
    * @param [out] driver1Version 驱动器1硬件版本
    * @param [out] driver1Version 驱动器2硬件版本
    * @param [out] driver1Version 驱动器3硬件版本
    * @param [out] driver1Version 驱动器4硬件版本
    * @param [out] driver1Version 驱动器5硬件版本
    * @param [out] driver1Version 驱动器6硬件版本
    * @param [out] endBoardVersion 末端板硬件版本
    * @return 错误码 
    */
    int GetHardwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

获取机器人固件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人固件版本
    * @param [out] ctrlBoxBoardVersion 控制箱载板固件版本
    * @param [out] driver1Version 驱动器1固件版本
    * @param [out] driver1Version 驱动器2固件版本
    * @param [out] driver1Version 驱动器3固件版本
    * @param [out] driver1Version 驱动器4固件版本
    * @param [out] driver1Version 驱动器5固件版本
    * @param [out] driver1Version 驱动器6固件版本
    * @param [out] endBoardVersion 末端板固件版本
    * @return 错误码 
    */
    int GetFirmwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        String ctrlBoxBoardVersion = "";
        String driver1Version = "";
        String driver2Version = "";
        String driver3Version = "";
        String driver4Version = "";
        String driver5Version = "";
        String driver6Version = "";
        String endBoardVersion = "";
        robot.GetHardwareVersion(ctrlBoxBoardVersion ,driver1Version,  driver2Version,  driver3Version,
                 driver4Version,  driver5Version,  driver6Version,  endBoardVersion);

        robot.GetFirmwareVersion(ctrlBoxBoardVersion, driver1Version, driver2Version, driver3Version,
                driver4Version, driver5Version, driver6Version, endBoardVersion);
    }