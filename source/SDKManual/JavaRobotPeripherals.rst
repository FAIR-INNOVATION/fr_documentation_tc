机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [in] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [in] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int SetGripperConfig(DeviceConfig config);

获取夹爪配置
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [out] config .company  夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [out] config .device  设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [out] config .softvesion  软件版本号，暂不使用，默认为0
    * @param  [out] config .bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int GetGripperConfig(DeviceConfig config);

激活夹爪
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int ActGripper(int index, int act); 

控制夹爪
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] pos  位置百分比，范围[0~100]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] force  力矩百分比，范围[0~100]
    * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [in] type 夹爪类型，0-平行夹爪；1-旋转夹爪
    * @param  [in] rotNum 旋转圈数
    * @param  [in] rotVel 旋转速度百分比[0-100]
    * @param  [in] rotTorque 旋转力矩百分比[0-100]
    * @return 错误码
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, int block, int type, double rotNum, int rotVel, int rotTorque); 

获取夹爪运动状态
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取夹爪运动状态
    * @return List[0]:错误码; List[1] : fault  0-无错误，1-有错误; List[2]: staus  0-运动未完成，1-运动完成
    */
    List<Integer> GetGripperMotionDone(); 

代码示例
++++++++++++++++
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
        int company = 3;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int deviceID = -1;

        DeviceConfig gripperConfig = new DeviceConfig(company, device, softversion, bus);

        robot.SetGripperConfig(gripperConfig);
        robot.Sleep(1000);

        DeviceConfig getConfig = new DeviceConfig();
        robot.GetGripperConfig(getConfig);
        System.out.println("gripper 厂商:" + getConfig.company + " , 类型: " + getConfig.device + " , 软件版本: " + getConfig.softwareVersion);

        int index = 1;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status = -1, fault = -1;
        int rtn = -1;

        rtn = robot.ActGripper(index, act);//激活夹爪
        System.out.println("ActGripper rtn : " + rtn);
        act = 1;
        rtn = robot.ActGripper(index, act);
        System.out.println("ActGripper rtn : " + rtn);

        rtn = robot.MoveGripper(index, 80, 20, 50, max_time,0,0,0,0);//移动夹爪
        System.out.println("MoveGripper rtn : " + rtn);
        robot.Sleep(2000);
        robot.MoveGripper(index, 20, 20, 50, max_time, block,0,0,0,0);//移动夹爪

        robot.Sleep(4000);
        List<Integer> rtnArray = new ArrayList<Integer>() {};
        rtnArray=robot.GetGripperMotionDone();
        System.out.println("gripper motion done : " + rtnArray.get(2) +", " + rtnArray.get(1));
    }

计算预抓取点-视觉
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算预抓取点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] pre_pos  获取点
    * @return 错误码 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, DescPose pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算撤退点-视觉 
    * @param [in] desc_pos  抓取点笛卡尔位姿
    * @param [in] zlength   z轴偏移量 
    * @param [in] zangle    绕z轴旋转偏移量
    * @param [out] post_poss 撤退点
    * @return 错误码 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, DescPose post_pos);

代码示例
++++++++++++++++
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
        int company = 3;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int deviceID = -1;

        DeviceConfig gripperConfig = new DeviceConfig(company, device, softversion, bus);

        robot.SetGripperConfig(gripperConfig);
        robot.Sleep(1000);

        DescPose desc_pos1, desc_pos2;
        desc_pos1 = new DescPose(-228.943, -584.228, 461.958,179.16, 5.559, 125.643);
        robot.ComputePrePick(desc_pos1, 10, 0, desc_pos2);
        System.out.println("ComputePrePick: " + desc_pos2.toString());

        desc_pos2.tran.x = 0;
        robot.ComputePostPick(desc_pos1, 10, 0, desc_pos2);
        System.out.println("ComputePostPick: " + desc_pos2.toString());
    }