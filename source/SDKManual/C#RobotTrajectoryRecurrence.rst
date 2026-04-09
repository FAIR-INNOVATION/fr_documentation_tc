機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設置TPD軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置TPD軌跡記錄參數
    * @param  [in] type  記錄數據類型，1-關節位置
    * @param  [in] name  軌跡文件名
    * @param  [in] period_ms  數據採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    int SetTPDParam(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose);

開始TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  開始TPD軌跡記錄
    * @param  [in] type  記錄數據類型，1-關節位置
    * @param  [in] name  軌跡文件名
    * @param  [in] period_ms  數據採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    int SetTPDStart(int type, string name, int period_ms, UInt16 di_choose, UInt16 do_choose); 

停止TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  停止TPD軌跡記錄
    * @return  錯誤碼
    */
    int SetWebTPDStop(); 

刪除TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  刪除TPD軌跡記錄
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */   
    int SetTPDDelete(string name); 

TPD軌跡預加載
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡預加載
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */      
    int LoadTPD(string name);

獲取TPD軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取軌跡起始位姿 
    * @param [in] name  軌跡文件名
    * @param [out] desc_pose 軌跡起始位姿 
    * @return 錯誤碼 
    */ 
    int GetTPDStartPose(string name, ref DescPose desc_pose); 

TPD軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡復現
    * @param  [in] name  軌跡文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int MoveTPD(string name, byte blend, float ovl); 

機器人TPD軌跡記錄代碼示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnTPDMove_Click(object sender, EventArgs e)
    {
        int type = 1;
        string name = "tpd2025";
        int period_ms = 4;
        ushort di_choose = 0;
        ushort do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        Thread.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        float ovl = 100.0f;
        byte blend = 0;

        DescPose start_pose = new DescPose();

        int rtn = robot.LoadTPD(name);
        Console.WriteLine("LoadTPD rtn is: {0}\n", rtn);

        robot.GetTPDStartPose(name, ref start_pose);
        Console.WriteLine("start pose, xyz is: {0} {1} {2}. rpy is: {3} {4} {5} \n",
            start_pose.tran.x, start_pose.tran.y, start_pose.tran.z,
            start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        robot.MoveCart(start_pose, 0, 0, 100, 100, ovl, -1, -1);
        Thread.Sleep(1000);

        rtn = robot.MoveTPD(name, blend, ovl);
        Console.WriteLine("MoveTPD rtn is: {0}\n", rtn);
        Thread.Sleep(5000);

        robot.SetTPDDelete(name);
    }

外部軌跡文件預處理
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 外部軌跡文件預處理 
    * @param [in] name 軌跡文件名  
    * @param [in] ovl 速度縮放百分比，範圍[0~100] 
    * @param [in] opt 1-控制點，默認爲1 
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

獲取軌跡文件軌跡起始位置
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取軌跡文件軌跡起始位置 
    * @param [in] name 軌跡文件名  
    * @param [out] desc_pose 軌跡起始位姿  
    * @return 錯誤碼 
    */ 
    int GetTrajectoryStartPose(string name, ref DescPose desc_pose); 

獲取軌跡文件軌跡點編號
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取軌跡點編號   
    * @param [out] pnum 軌跡點編號  
    * @return 錯誤碼 
    */  
    int GetTrajectoryPointNum(ref int pnum);

設置軌跡文件軌跡運行速度
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡文件軌跡運行速度   
    * @param [in] ovl 速度百分比  
    * @return 錯誤碼 
    */  
    int SetTrajectoryJSpeed(double ovl);

設置軌跡文件軌跡運行中的力和力矩
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡文件軌跡運行中的力和力矩  
    * @param [in] ft 三個方向的力和扭矩，單位N和Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

設置軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿x方向的力  
    * @param [in] fx  沿x方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFx(double fx);

設置軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿y方向的力  
    * @param [in] fy  沿y方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFy(double fy);

設置軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFz(double fz);

設置軌跡運行中的繞x軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞x軸的扭矩  
    * @param [in] tx  繞x軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTx(double tx);

設置軌跡運行中的繞y軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞y軸的扭矩  
    * @param [in] ty  繞y軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTy(double ty);

設置軌跡運行中的繞z軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞z軸的扭矩  
    * @param [in] tz  繞z軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTz(double tz);

上傳軌跡J文件
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 上傳軌跡J文件
    * @param [in] filePath 上傳軌跡文件的全路徑名   C://test/testJ.txt
    * @return 錯誤碼
    */
    int TrajectoryJUpLoad(string filePath);

刪除軌跡J文件
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 刪除軌跡J文件
    * @param [in] fileName 文件名稱 testJ.txt
    * @return 錯誤碼
    */
    int TrajectoryJDelete(string fileName);

機器人軌跡J文件復現代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button33_Click(object sender, EventArgs e)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/spray_traj1.txt");
        Console.WriteLine("Upload TrajectoryJ A {0}\n", rtn);

        string traj_file_name = "/fruser/traj/spray_traj1.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        Console.WriteLine("LoadTrajectoryJ {0}, rtn is: {1}\n", traj_file_name, rtn);

        DescPose traj_start_pose = new DescPose();
        rtn = robot.GetTrajectoryStartPose(traj_file_name, ref traj_start_pose);
        Console.WriteLine("GetTrajectoryStartPose is: {0}\n", rtn);
        Console.WriteLine("desc_pos:{0},{1},{2},{3},{4},{5}\n",
            traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z,
            traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);

        Thread.Sleep(1000);

        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(ref traj_num);
        Console.WriteLine("GetTrajectoryStartPose rtn is: {0}, traj num is: {1}\n", rtn, traj_num);

        rtn = robot.SetTrajectoryJSpeed(50.0f);
        Console.WriteLine("SetTrajectoryJSpeed is: {0}\n", rtn);

        ForceTorque traj_force = new ForceTorque();
        traj_force.fx = 10;
        rtn = robot.SetTrajectoryJForceTorque(traj_force);
        Console.WriteLine("SetTrajectoryJForceTorque rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFx(10.0f);
        Console.WriteLine("SetTrajectoryJForceFx rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFy(0.0f);
        Console.WriteLine("SetTrajectoryJForceFy rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJForceFz(0.0f);
        Console.WriteLine("SetTrajectoryJForceFz rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTx(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTx rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTy(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTy rtn is: {0}\n", rtn);

        rtn = robot.SetTrajectoryJTorqueTz(10.0f);
        Console.WriteLine("SetTrajectoryJTorqueTz rtn is: {0}\n", rtn);

        rtn = robot.MoveTrajectoryJ();
        Console.WriteLine("MoveTrajectoryJ rtn is: {0}\n", rtn);
    }

軌跡預處理(軌跡前瞻)
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡預處理(軌跡前瞻)
    * @param  [in] name  軌跡文件名
    * @param  [in] mode 採樣模式，0-不進行採樣；1-等數據間隔採樣；2-等誤差限制採樣
    * @param  [in] errorLim 誤差限制，使用直線擬合生效
    * @param  [in] type 平滑方式，0-貝塞爾平滑
    * @param  [in] precision 平滑精度，使用貝塞爾平滑時生效
    * @param  [in] vamx 設定的最大速度，mm/s
    * @param  [in] amax 設定的最大加速度，mm/s2
    * @param  [in] jmax 設定的最大加加速度，mm/s3
    * @return  錯誤碼   
    */
    int LoadTrajectoryLA(string name, int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax);

軌跡復現(軌跡前瞻)
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  軌跡復現(軌跡前瞻)
    * @return  錯誤碼   
    */
    int MoveTrajectoryLA();

軌跡復現(軌跡前瞻)代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button8_Click(object sender, EventArgs e)
    {
        int rtn = 0;

        string nameA = "/fruser/traj/A.txt";
        string nameB = "/fruser/traj/B.txt";

        rtn = robot.LoadTrajectoryLA(nameB, 0, 0, 0, 1, 100.0, 100.0, 1000.0);    // 直線擬合
        Console.WriteLine($"LoadTrajectoryLA rtn is {rtn}");

        DescPose startPos = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetTrajectoryStartPose(nameA, ref startPos);

        //
        robot.MoveCart(startPos, 1, 0, (float)100.0, (float)100.0, (float)100.0, -1, -1);

        rtn = robot.MoveTrajectoryLA();
        Console.WriteLine($"MoveTrajectoryLA rtn is {rtn}");
    }

運動到TPD軌跡記錄起點
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 運動到TPD軌跡記錄起點
    * @param [in] name 軌跡文件名
    * @param [in] moveType 運動類型；0-PTP; 1-LIN
    * @param [in] ovl 速度縮放百分比，範圍[0~100]
    * @return 錯誤碼
    */
    public int MoveToTPDStart(string name, int moveType, double ovl)

運動到TPD軌跡記錄起點的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void testTPDmove()
    {
        string name = "tpd2025";
        int type = 1;
        int period_ms = 4;
        int rtn = 0;
        UInt16 di_choose = 0;
        UInt16 do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        Thread.Sleep(3000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        Thread.Sleep(3000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        Thread.Sleep(1000);
        float ovl = 100.0f;
        byte blend = 0;
        DescPose start_pose = new DescPose();
        rtn = robot.LoadTPD(name);
        Console.WriteLine($"LoadTPD rtn is:{rtn}\n");

        robot.GetTPDStartPose(name, ref start_pose);
        Console.WriteLine($"start pose, xyz is: %f %f %f. rpy is: {start_pose.tran.x},{start_pose.tran.y}, {start_pose.tran.z}, {start_pose.rpy.rx}, {start_pose.rpy.ry}, {start_pose.rpy.rz}");

        rtn = robot.MoveToTPDStart(name, 0, 100.0);

        rtn = robot.MoveTPD(name, blend, ovl);
        Thread.Sleep(5000*5);

        robot.SetTPDDelete(name);
    }