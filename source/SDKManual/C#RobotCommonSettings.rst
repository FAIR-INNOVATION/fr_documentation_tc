机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    int SetSpeed(int vel); 

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-六点法 
    * @param [in] point_num 点编号,范围[1~6] 
    * @return 错误码 
    */ 
    int SetToolPoint(int point_num); 

计算工具坐标系--六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTool(ref DescPose tcp_pose); 

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工具参考点-四点法 
    * @param [in] point_num 点编号,范围[1~4] 
    * @return 错误码 
    */ 

计算工具坐标系-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算工具坐标系
    * @param [out] tcp_pose 工具坐标系
    * @return 错误码 
    */ 
    int ComputeTcp4(ref DescPose tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具坐标系
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] coord  工具中心点相对于末端法兰中心位姿
    * @param  [in] type  0-工具坐标系，1-传感器坐标系
    * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
    * param   [in] toolID 工具ID
    * @param  [in] loadNum 负载编号
    * @return  错误码
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);  

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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

设置外部工具坐标参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置外部工具参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3] 
    * @return 错误码 
    */ 
    int SetExTCPPoint(int point_num); 

计算外部工具坐标系-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 计算外部工具坐标系-三点法
    * @param [out] tcp_pose 外部工具坐标系
    * @return 错误码 
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置外部工具坐标系 
    * @param [in] id 坐标系编号，范围[0~14] 
    * @param [in] etcp 工具中心点相对末端法兰中心位姿 
    * @param [in] etool 待定 
    * @return 错误码 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

设置工件坐标系参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置工件参考点-三点法 
    * @param [in] point_num 点编号,范围[1~3]  
    * @return 错误码 
    */ 
    int SetWObjCoordPoint(int point_num); 

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  计算工件坐标系
    * @param [in] method 计算方法 0：原点-x轴-z轴  1：原点-x轴-xy平面
    * @param [in] refFrame 参考坐标系
    * @param [out] wobj_pose 工件坐标系
    * @return 错误码
    */
    int ComputeWObjCoord(int method, int refFrame, ref DescPose wobj_pose); 

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工件坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14] 
    * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
    * @param  [in] refFrame 参考坐标系
    * @return  错误码
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    int SetLoadWeight(float weight);

设置末端负载质心坐标
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    int SetLoadCoord(DescTran coord); 

设置机器人安装方式
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in] install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    int SetRobotInstallPos(byte install); 

设置机器人安装角度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代码示例
++++++++++
.. code-block:: c#
    :linenos:

    private void btnCommonSets_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int i;
        double value = 0;
        int id;
        int type;
        int install;

        DescTran coord = new DescTran();
        DescPose t_coord, etcp, etool, w_coord;
        t_coord = new DescPose();
        etcp = new DescPose();
        w_coord = new DescPose();

        robot.SetSpeed(20);

        for (i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, (float)(i + 0.5));
            robot.WaitMs(100);
        }

        for (i = 1; i < 21; i++)
        {
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value : {value}");
        }

        robot.SetLoadWeight((float)2.5);
        coord.x = 3.0;
        coord.y = 4.0;
        coord.z = 5.0;
        robot.SetLoadCoord(coord);
                
        id = 3;
        t_coord.tran.x = 1.0;
        t_coord.tran.y = 2.0;
        t_coord.tran.z = 300.0;
        t_coord.rpy.rx = 4.0;
        t_coord.rpy.ry = 5.0;
        t_coord.rpy.rz = 6.0;
        type = 0;
        install = 0;

        int rtn1 = -1;
        int rtn2 = -1;
        rtn1 = robot.SetToolCoord(id, t_coord, type, install);
        rtn2 = robot.SetToolList(id, t_coord, type, install);
        Console.WriteLine($"set tool coord result {rtn1}, set tool list rtn{rtn2}");
            
        etcp.tran.x = 1.0;
        etcp.tran.y = 2.0;
        etcp.tran.z = 3.0;
        etcp.rpy.rx = 4.0;
        etcp.rpy.ry = 5.0;
        etcp.rpy.rz = 6.0;
        etool.tran.x = 11.0;
        etool.tran.y = 22.0;
        etool.tran.z = 330.0;
        etool.rpy.rx = 44.0;
        etool.rpy.ry = 55.0;
        etool.rpy.rz = 66.0;
        id = 5;
        robot.SetExToolCoord(id, etcp, etool);
        robot.SetExToolList(id, etcp, etool);

        w_coord.tran.x = 110.0;
        w_coord.tran.y = 12.0;
        w_coord.tran.z = 13.0;
        w_coord.rpy.rx = 14.0;
        w_coord.rpy.ry = 15.0;
        w_coord.rpy.rz = 16.0;
        id = 12;
        robot.SetWObjCoord(id, w_coord);
        //robot.SetWObjList(id, w_coord);

        double yangle = 0, zangle = 0;
        robot.SetRobotInstallPos(1);//侧装
        robot.SetRobotInstallAngle(15.0, 25.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
        robot.SetRobotInstallAngle(10.0, 10.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
    }

等待指定时间
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待指定时间
    * @param  [in]  t_ms  单位ms
    * @return  错误码
    */
    int WaitMs(int t_ms);

设置机器人加速度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置机器人加速度
    * @param [in] acc 机器人加速度百分比
    * @return 错误码
    */
    int SetOaccScale(double acc)