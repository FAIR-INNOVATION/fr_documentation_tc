機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設定軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定軌跡記錄參數
    * @param  [in] type  記錄資料類型，1-關節位置
    * @param  [in] name  軌跡檔名
    * @param  [in] period_ms  資料採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    int SetTPDParam(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose);

開始軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  開始軌跡記錄
    * @param  [in] type  記錄資料類型，1-關節位置
    * @param  [in] name  軌跡檔名
    * @param  [in] period_ms  資料採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    int SetTPDStart(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose); 

停止軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  停止軌跡記錄
    * @return  錯誤碼
    */
    int SetWebTPDStop(); 

刪除軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  刪除軌跡記錄
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */   
    int SetTPDDelete(string name); 

代碼範例
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

軌跡預載
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡預載
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */      
    int LoadTPD(string name);

取得軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得軌跡起始位姿 
    * @param [in] name  軌跡檔名
    * @param [out] desc_pose 軌跡起始位姿 
    * @return 錯誤碼 
    */ 
    int GetTPDStartPose(string name, ref DescPose desc_pose); 

軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡復現
    * @param  [in] name  軌跡檔名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int MoveTPD(string name, byte blend, float ovl); 

代碼範例
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

外部軌跡檔案預處理
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 外部軌跡檔案預處理 
    * @param [in] name 軌跡檔名  
    * @param [in] ovl 速度縮放百分比，範圍[0~100] 
    * @param [in] opt 1-控制點，預設為1 
    * @return 錯誤碼 
    */ 
    int LoadTrajectoryJ(string name, float ovl, int opt); 

外部軌跡文件軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 外部軌跡文件軌跡復現  
    * @return 錯誤碼 
    */
    int MoveTrajectoryJ();

取得軌跡檔案軌跡起始位置
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得軌跡檔案軌跡起始位置 
    * @param [in] name 軌跡檔名  
    * @param [out] desc_pose 軌跡起始位姿  
    * @return 錯誤碼 
    */ 
    int GetTrajectoryStartPose(string name, ref DescPose desc_pose); 

取得軌跡檔案軌跡點編號
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得軌跡點編號   
    * @param [out] pnum 軌跡點編號  
    * @return 錯誤碼 
    */  
    int GetTrajectoryPointNum(ref int pnum);

設定軌跡檔案軌跡運行速度
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡檔案軌跡運行速度   
    * @param [in] ovl 速度百分比  
    * @return 錯誤碼 
    */  
    int SetTrajectoryJSpeed(double ovl);

設定軌跡檔案軌跡運行中的力和力矩
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡檔案軌跡運行中的力和力矩  
    * @param [in] ft 三個方向的力和扭矩，單位N和Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

設定軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿x方向的力  
    * @param [in] fx  沿x方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFx(double fx);

設定軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿y方向的力  
    * @param [in] fy  沿y方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFy(double fy);

設定軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFz(double fz);

設定軌跡運轉中的繞x軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞x軸的扭矩  
    * @param [in] tx  繞x軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTx(double tx);

設定軌跡運轉中的繞y軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞y軸的扭矩  
    * @param [in] ty  繞y軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTy(double ty);

設定軌跡運轉中的繞z軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞z軸的扭矩  
    * @param [in] tz  繞z軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTz(double tz);

代碼範例
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


