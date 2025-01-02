机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    int SetSysVarValue(int id, double value); 

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法
    * @param [in] point_num 点编号,范围[1~6]
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num); 

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(DescPose tcp_pose); 

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法
    * @param [in] point_num 点编号,范围[1~4]
    * @return 错误码 
    */ 
    int SetTcp4RefPoint(int point_num);

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(DescPose tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] coord  工具中心点相对于末端法兰中心位姿
    * @param [in] type  0-工具坐标系，1-传感器坐标系
    * @param [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param [in] toolID  工具ID
    * @param [in] loadNum  负载编号
    * @return 错误码 
    */ 
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

代码示例
++++++++++++++++++++++++++++++++++
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
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//获取系统变量
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos jp1=new JointPos(-89.407,-148.279,-83.169,-45.689,133.689,41.705);
        JointPos jp2=new JointPos(-67.595,-143.7,-88.006,-48.514,57.073,56.189);
        JointPos jp3=new JointPos(-88.229,-152.355,-67.815,-78.07,129.029,58.739);
        JointPos jp4=new JointPos(-77.528,-141.519,-89.826,-37.184,90.274,41.769);
        JointPos jp5=new JointPos(-76.744,-138.219,-97.714,-32.595,90.255,42.558);
        JointPos jp6=new JointPos(-77.595,-138.454,-90.065,-40.014,90.275,41.709);
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p4 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p5 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p6 = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(jp1, desc_p1);
        robot.GetForwardKin(jp2, desc_p2);
        robot.GetForwardKin(jp3, desc_p3);
        robot.GetForwardKin(jp4, desc_p4);
        robot.GetForwardKin(jp5, desc_p5);
        robot.GetForwardKin(jp6, desc_p6);
        robot.MoveJ(jp1, desc_p1,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(1);

        robot.MoveJ(jp2, desc_p2,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(2);

        robot.MoveJ(jp3, desc_p3,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(3);

        robot.MoveJ(jp4, desc_p4,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(4);

        robot.MoveJ(jp5, desc_p5,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(5);

        robot.MoveJ(jp6, desc_p6,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(6);

        DescPose coord = new DescPose();
        robot.ComputeTool(coord);
        System.out.println("result is " + coord.tran.x + "  " + coord.tran.y + "  " + coord.tran.z + "  " + coord.rpy.rx + "  " + coord.rpy.ry + "  " + coord.rpy.rz);

        robot.SetToolCoord(5, coord, 0, 0,0,0);//设置工具坐标系
        robot.SetToolList(5, coord, 0, 0, 0);
    }

设置外部工具坐标参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14]
    * @param [in] etcp  工具中心点相对末端法兰中心位姿
    * @param [in] etool  待定
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

代码示例
++++++++++++++++++++++++++++++++++
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
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//获取系统变量
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689 , -37.899, 94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);


        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeExTCF(coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetExToolCoord(5, coordE, coordE);
        robot.SetExToolList(5,coordE, coordE);
    }

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num); 

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算工件坐标系
    * @param [in]  method 计算方式 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in]  refFrame 参考坐标系
    * @param [out]  wobj_pose 工件坐标系
    * @return 错误码 
    */ 
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工件坐标系
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjCoord(int id, DescPose coord, int refFrame);

设置工件坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[1~15]
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

代码示例
++++++++++++++++++++++++++++++++++
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

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689,-37.899,94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);
        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeWObjCoord(0, coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetWObjCoord(5, coordE,0);
        robot.SetWObjList(5,coordE,0);
    }

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(double weight);

设置末端负载质心坐标
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

设置机器人安装方式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in]  install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(int install); 

设置机器人安装角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代码示例
++++++++++++++++++++++++++++++++++
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
        robot.SetLoadWeight(2);
        robot.SetLoadCoord(new DescTran(1.0, 2.0, 3.0));
        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(0, 0);
    }

等待指定时间
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  等待指定时间
    * @param  [in]  t_ms  单位ms
    * @return  错误码
    */
    int WaitMs(int t_ms);

设置机器人加速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc);