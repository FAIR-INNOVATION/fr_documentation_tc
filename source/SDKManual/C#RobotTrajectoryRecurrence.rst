机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置轨迹记录参数
++++++++++++++++++++++++++++
.. code-block:: c#
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
    int SetTPDParam(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose);

开始轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c#
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
    int SetTPDStart(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose); 

停止轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  停止轨迹记录
    * @return  错误码
    */
    int SetWebTPDStop(); 

删除轨迹记录
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  删除轨迹记录
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */   
    int SetTPDDelete(string name); 

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnTCPRecord_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int type = 1;
        string name = "tpd2023";
        int period_ms = 2;
        UInt16 di_choose = 0;
        UInt16 do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        Thread.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        //robot.SetTPDDelete(name);
    }

轨迹预加载
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  轨迹预加载
    * @param  [in] name  轨迹文件名
    * @return  错误码
    */      
    int LoadTPD(string name);

获取轨迹起始位姿
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取轨迹起始位姿 
    * @param [in] name  轨迹文件名
    * @param [out] desc_pose 轨迹起始位姿 
    * @return 错误码 
    */ 
    int GetTPDStartPose(string name, ref DescPose desc_pose); 

轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  轨迹复现
    * @param  [in] name  轨迹文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度缩放百分比，范围[0~100]
    * @return  错误码
    */
    int MoveTPD(string name, byte blend, float ovl); 

代码示例
++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnTPDMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        string name = "tpd2023";
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        int config = -1;
        byte blend = 1;

        DescPose desc_pose = new DescPose();
        robot.GetTPDStartPose(name, ref desc_pose);
        Console.WriteLine($"GetTPDStartPose:{desc_pose.tran.x},{desc_pose.tran.y},{desc_pose.tran.z},{desc_pose.rpy.rx},{desc_pose.rpy.ry},{desc_pose.rpy.rz}");
        robot.SetTrajectoryJSpeed(100.0f);

        robot.LoadTPD(name);
        robot.MoveCart(desc_pose, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveTPD(name, blend, 100.0f);
    }

外部轨迹文件预处理
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 外部轨迹文件预处理 
    * @param [in] name 轨迹文件名  
    * @param [in] ovl 速度缩放百分比，范围[0~100] 
    * @param [in] opt 1-控制点，默认为1 
    * @return 错误码 
    */ 
    int LoadTrajectoryJ(string name, float ovl, int opt); 

外部轨迹文件轨迹复现
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 外部轨迹文件轨迹复现  
    * @return 错误码 
    */
    int MoveTrajectoryJ();

获取轨迹文件轨迹起始位置
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取轨迹文件轨迹起始位置 
    * @param [in] name 轨迹文件名  
    * @param [out] desc_pose 轨迹起始位姿  
    * @return 错误码 
    */ 
    int GetTrajectoryStartPose(string name, ref DescPose desc_pose); 

获取轨迹文件轨迹点编号
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取轨迹点编号   
    * @param [out] pnum 轨迹点编号  
    * @return 错误码 
    */  
    int GetTrajectoryPointNum(ref int pnum);

设置轨迹文件轨迹运行速度
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹文件轨迹运行速度   
    * @param [in] ovl 速度百分比  
    * @return 错误码 
    */  
    int SetTrajectoryJSpeed(double ovl);

设置轨迹文件轨迹运行中的力和力矩
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹文件轨迹运行中的力和力矩  
    * @param [in] ft 三个方向的力和扭矩，单位N和Nm
    * @return 错误码 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

设置轨迹运行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿x方向的力  
    * @param [in] fx  沿x方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFx(double fx);

设置轨迹运行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿y方向的力  
    * @param [in] fy  沿y方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFy(double fy);

设置轨迹运行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，单位N
    * @return 错误码 
    */
    int SetTrajectoryJForceFz(double fz);

设置轨迹运行中的绕x轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕x轴的扭矩  
    * @param [in] tx  绕x轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTx(double tx);

设置轨迹运行中的绕y轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕y轴的扭矩  
    * @param [in] ty  绕y轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTy(double ty);

设置轨迹运行中的绕z轴的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置轨迹运行中的绕z轴的扭矩  
    * @param [in] tz  绕z轴的扭矩，单位Nm
    * @return 错误码 
    */
    int SetTrajectoryJTorqueTz(double tz);

代码示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnTrajectory_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        string name = "/fruser/traj/trajHelix_aima_1.txt";
        int rtn = -1;

        rtn = robot.LoadTrajectoryJ(name, 100, 1);
        Console.WriteLine($"LoadTrajectoryJ:{rtn}");

        DescPose desc_pos2 = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.GetTrajectoryStartPose(name, ref desc_pos2);
        Console.WriteLine($"GetTrajectoryStartPose:{desc_pos2.tran.x},{desc_pos2.tran.y},{desc_pos2.tran.z},{desc_pos2.rpy.rx},{desc_pos2.rpy.ry},{desc_pos2.rpy.rz}");

        int tool = 1;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendT1 = 0.0f;
        int config = -1;
        robot.MoveCart(desc_pos2, tool, user, vel, acc, ovl, blendT, config);

        rtn = robot.SetTrajectoryJSpeed(20);
        Console.WriteLine($"SetTrajectoryJSpeed: rtn  {rtn}");

        rtn = robot.MoveTrajectoryJ();
        Console.WriteLine($"MoveTrajectoryJ:{rtn}");

        int pnum = -1;
        rtn = robot.GetTrajectoryPointNum(ref pnum);
        Console.WriteLine($"GetTrajectoryPointNum: rtn  {rtn}    num {pnum}");

        rtn = robot.SetTrajectoryJSpeed(100);
        Console.WriteLine($"SetTrajectoryJSpeed: rtn  {rtn}");

        ForceTorque ft = new ForceTorque(1, 1, 1, 1, 1, 1);
        rtn = robot.SetTrajectoryJForceTorque(ft);
        Console.WriteLine($"SetTrajectoryJForceTorque: rtn  {rtn}");

        rtn = robot.SetTrajectoryJForceFx(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
        rtn = robot.SetTrajectoryJForceFy(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
        rtn = robot.SetTrajectoryJForceFz(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
        rtn = robot.SetTrajectoryJTorqueTx(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
        rtn = robot.SetTrajectoryJTorqueTy(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
        rtn = robot.SetTrajectoryJTorqueTz(1.0);
        Console.WriteLine($"SetTrajectoryJForceFx: rtn  {rtn}");
    }


