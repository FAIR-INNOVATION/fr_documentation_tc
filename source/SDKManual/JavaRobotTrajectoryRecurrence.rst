机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置轨迹记录参数
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置轨迹记录参数
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    int SetTPDParam(int type, String name, int period_ms, int di_choose, int do_choose);

开始轨迹记录
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  开始轨迹记录
    * @param  [in] type  记录数据类型，1-关节位置
    * @param  [in] name  轨迹文件名
    * @param  [in] period_ms  数据采样周期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI选择,bit0~bit7对应控制箱DI0~DI7，bit8~bit9对应末端DI0~DI1，0-不选择，1-选择
    * @param  [in] do_choose  DO选择,bit0~bit7对应控制箱DO0~DO7，bit8~bit9对应末端DO0~DO1，0-不选择，1-选择
    * @return  错误码
    */
    int SetTPDStart(int type, String name, int period_ms, int di_choose, int do_choose);

停止轨迹记录
++++++++++++++++++++++++++++
.. code-block:: java
    :linenos:

    /**
    * @brief  停止轨迹记录
    * @return  错误码
    */
    int SetWebTPDStop(); 

删除轨迹记录
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  删除轨迹记录
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */   
    int SetTPDDelete(string name); 

代码示例
++++++++++++++
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
        int type = 1;
        String name = "tpd_2024";
        int period_ms = 2;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDDelete(name);//删除轨迹记录

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);//设置轨迹记录参数

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);//开始轨迹记录
        robot.Sleep(10000);
        robot.SetWebTPDStop();//停止轨迹记录
        robot.DragTeachSwitch(0);
    }

轨迹预加载
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  轨迹预加载
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */      
    int LoadTPD(String name);

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取轨迹起始位姿 
    * @param [in] name  轨迹文件名,不需要文件后缀
    * @param [out] desc_pose 获取的轨迹起始位姿
    * @return 错误码 
    */ 
    int GetTPDStartPose(String name, DescPose desc_pose); 

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  轨迹复现
    * @param  [in] name  轨迹文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度缩放百分比，范围[0~100]
    * @return  错误码
    */
    int MoveTPD(String name, int blend, double ovl); 

设置轨迹运行中的速度
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置轨迹运行中的速度
    * @param  [in] ovl 速度百分比
    * @return  错误码
    */
    int SetTrajectoryJSpeed(double ovl); 

代码示例
++++++++++++++++++
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
        String name = "tpd_2024";
        int tool = 0;
        int user = 0;
        double vel = 30.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int config = -1;
        byte blend = 1;

        DescPose desc_pose = new DescPose();
        robot.GetTPDStartPose(name,  desc_pose);
        robot.SetTrajectoryJSpeed(100.0);

        robot.LoadTPD(name);
        robot.MoveCart(desc_pose, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveTPD(name, blend, 80.0);
    }

外部轨迹文件预处理
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部轨迹文件预处理 
    * @param [in] name 轨迹文件名  
    * @param [in] ovl 速度缩放百分比，范围[0~100]
    * @param [in] opt 1-控制点，默认为1 
    * @return 错误码 
    */ 
    int LoadTrajectoryJ(String name, double ovl, int opt); 

外部轨迹文件轨迹复现
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部轨迹文件轨迹复现  
    * @return 错误码 
    */
    int MoveTrajectoryJ();

获取轨迹文件轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取轨迹起始位姿 
    * @param [in] name 轨迹文件名  
    * @param [out] desc_pose 获取的轨迹起始位姿
    * @return 错误码 
    */ 
    int GetTrajectoryStartPose(String name, DescPose desc_pose); 

设置轨迹文件轨迹运行中的力和力矩
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹文件轨迹运行中的力和力矩  
    * @param [in] ft 三个方向的力和扭矩，单位N和Nm
    * @return 错误码 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

设置轨迹运行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿x方向的力  
    * @param [in] fx 沿x方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFx(double fx);

设置轨迹运行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿y方向的力
    * @param [in] fy 沿y方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFy(double fy);

设置轨迹运行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFz(double fz);

设置轨迹运行中的绕x轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕x轴的扭矩  
    * @param [in] tx 绕x轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTx(double tx);

设置轨迹运行中的绕y轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕y轴的扭矩  
    * @param [in] ty 绕y轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTy(double ty);

设置轨迹运行中的绕z轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕z轴的扭矩  
    * @param [in] tz 绕z轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTz(double tz);

代码示例
++++++++++++++++++++++++++++
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

        ForceTorque tor = new ForceTorque(10.0,10.0, 10.0, 10.0, 10.0, 10.0);
        robot.SetTrajectoryJForceTorque(tor);

        robot.SetTrajectoryJForceFx(2.0);
        robot.SetTrajectoryJForceFy(2.0);
        robot.SetTrajectoryJForceFz(2.0);
        robot.SetTrajectoryJTorqueTx(2.0);
        robot.SetTrajectoryJTorqueTy(2.0);
        robot.SetTrajectoryJTorqueTz(2.0);


        robot.LoadTrajectoryJ("/fruser/traj/test1011002.txt", 20, 1);
        DescPose startPos = new DescPose();
        robot.GetTrajectoryStartPose("/fruser/traj/test1011002.txt", startPos);
        robot.MoveCart(startPos, 0, 0, 40, 100.0, 100.0, -1.0, -1);

        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("Trajectory point num is " + pkg.trajectory_pnum);
        robot.SetTrajectoryJSpeed(40);
        robot.MoveTrajectoryJ();
    }


