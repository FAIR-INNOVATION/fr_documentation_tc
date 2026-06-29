機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設置TPD軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDParam(int type, String name, int period_ms, int di_choose, int do_choose);

開始TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  開始軌跡開始TPD軌跡記錄記錄
    * @param  [in] type  記錄數據類型，1-關節位置
    * @param  [in] name  軌跡文件名
    * @param  [in] period_ms  數據採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    int SetTPDStart(int type, String name, int period_ms, int di_choose, int do_choose);

停止TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: java
    :linenos:

    /**
    * @brief  停止TPD軌跡記錄
    * @return  錯誤碼
    */
    int SetWebTPDStop(); 

刪除TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  刪除TPD軌跡記錄
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */   
    int SetTPDDelete(string name); 

TPD軌跡預加載
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  軌跡預加載
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */      
    int LoadTPD(String name);

TPD軌跡復現
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  軌跡復現
    * @param  [in] name  軌跡文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int MoveTPD(String name, int blend, double ovl); 

獲取TPD起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取軌跡起始位姿 
    * @param [in] name  軌跡文件名,不需要文件後綴
    * @param [out] desc_pose 獲取的軌跡起始位姿
    * @return 錯誤碼 
    */ 
    int GetTPDStartPose(String name, DescPose desc_pose); 

機器人TPD軌跡記錄代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTPD(Robot robot)
    {
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(10000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        double ovl = 100.0;
        int blend = 0;

        DescPose start_pose =new DescPose() {};

        int rtn = robot.LoadTPD(name);
        System.out.println("LoadTPD rtn is:"+ rtn);

        robot.GetTPDStartPose(name, start_pose);
        robot.MoveCart(start_pose, 0, 0, 100, 100, ovl, -1, -1);
        robot.Sleep(1000);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.println("MoveTPD rtn is: "+ rtn);
        robot.Sleep(5000);

        robot.SetTPDDelete(name);
        return 0;
    }

軌跡預處理
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部軌跡文件預處理 
    * @param [in] name 軌跡文件名  
    * @param [in] ovl 速度縮放百分比，範圍[0~100]
    * @param [in] opt 1-控制點，默認爲1 
    * @return 錯誤碼 
    */ 
    int LoadTrajectoryJ(String name, double ovl, int opt); 

軌跡復現
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部軌跡文件軌跡復現  
    * @return 錯誤碼 
    */
    int MoveTrajectoryJ();

獲取軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取軌跡起始位姿 
    * @param [in] name 軌跡文件名  
    * @param [out] desc_pose 獲取的軌跡起始位姿
    * @return 錯誤碼 
    */ 
    int GetTrajectoryStartPose(String name, DescPose desc_pose);

獲取軌跡點編號
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取軌跡點編號
    * @return  錯誤碼
    */
    public int GetTrajectoryPointNum(int pnum)

設置軌跡運行中的速度
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /*
    * @brief  設置軌跡運行中的速度
    * @param  ovl 速度百分比
    * @param  mode 模式；0-降速模式；1-直接切換
    * @return  錯誤碼
    */
    public int SetTrajectoryJSpeed(double ovl, int mode)

設置軌跡運行中的力和扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置軌跡運行中的力和扭矩
    * @param  [in] ft 三個方向的力和扭矩，單位N和Nm
    * @return  錯誤碼
    */
    public int SetTrajectoryJForceTorque(ForceTorque ft)

設置軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿x方向的力  
    * @param [in] fx 沿x方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFx(double fx);

設置軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿y方向的力
    * @param [in] fy 沿y方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFy(double fy);

設置軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFz(double fz);

設置軌跡運行中的繞x軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞x軸的扭矩  
    * @param [in] tx 繞x軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTx(double tx);

設置軌跡運行中的繞y軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞y軸的扭矩  
    * @param [in] ty 繞y軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTy(double ty);

設置軌跡運行中的繞z軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置軌跡運行中的繞z軸的扭矩  
    * @param [in] tz 繞z軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTz(double tz);

上傳軌跡J文件
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上傳軌跡J文件  
    * @param [in] filePath 上傳軌跡文件的全路徑名   C://test/testJ.txt
    * @return 錯誤碼 
    */
    int TrajectoryJUpLoad(String filePath);

刪除軌跡J文件
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 刪除軌跡J文件  
    * @param [in] fileName 文件名稱 testJ.txt
    * @return 錯誤碼 
    */
    int TrajectoryJDelete(String fileName);

機器人軌跡J文件復現代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTraj(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/horse.txt");
        System.out.println("Upload TrajectoryJ A :"+ rtn);

        String traj_file_name = "horse.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        System.out.println("LoadTrajectoryJ:"+traj_file_name+", rtn is:"+ rtn);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);


        ExaxisPos epos=new ExaxisPos(0,0,0,0);
        DescPose po=new DescPose(0,0,0,0,0,0);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(traj_num);

        rtn = robot.SetTrajectoryJSpeed(50.0);
        System.out.println("SetTrajectoryJSpeed is:"+ rtn);

        ForceTorque traj_force=new ForceTorque(0,0,0,0,0,0);
        traj_force.fx = 10;
        rtn = robot.SetTrajectoryJForceTorque(traj_force);
        System.out.println("SetTrajectoryJForceTorque rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJForceFx(10.0);
        System.out.println("SetTrajectoryJForceFx rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFy(0.0);
        System.out.println("SetTrajectoryJForceFy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJForceFz(0.0);
        System.out.println("SetTrajectoryJForceFz rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTx(10.0);
        System.out.println("SetTrajectoryJTorqueTx rtn is: "+ rtn);

        rtn = robot.SetTrajectoryJTorqueTy(10.0);
        System.out.println("SetTrajectoryJTorqueTy rtn is:"+ rtn);

        rtn = robot.SetTrajectoryJTorqueTz(10.0);
        System.out.println("SetTrajectoryJTorqueTz rtn is:"+ rtn);

        rtn = robot.MoveTrajectoryJ();
        System.out.println("MoveTrajectoryJ rtn is: "+ rtn);

        return 0;
    }

機器人設置軌跡運行中的速度代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public int TestSetTrajectoryJSpeed(Robot robot) {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        int rtn;

        robot.SetReconnectParam(true, 30000, 500);
        rtn = robot.TrajectoryJUpLoad("D://zUP/horse.txt");
        System.out.printf("Upload TrajectoryJ A %d%n", rtn);
        String trajFileName = "horse.txt";
        rtn = robot.LoadTrajectoryJ(trajFileName, 100, 1);
        System.out.printf("LoadTrajectoryJ %s, rtn is: %d%n", trajFileName, rtn);
        DescPose trajStartPose = new DescPose();
        rtn = robot.GetTrajectoryStartPose(trajFileName, trajStartPose);
        System.out.printf("GetTrajectoryStartPose is: %d%n", rtn);
        System.out.printf("desc_pos:%f,%f,%f,%f,%f,%f%n", trajStartPose.tran.x, trajStartPose.tran.y, trajStartPose.tran.z, trajStartPose.rpy.rx, trajStartPose.rpy.ry, trajStartPose.rpy.rz);
        robot.Sleep(1000);
        robot.SetSpeed(50);
        robot.MoveCart(trajStartPose, 0, 0, 100, 100, 100, -1, -1);
        rtn = robot.GetTrajectoryPointNum(0);
        pkg = robot.GetRobotRealTimeState();
        int trajNum = pkg.trajectory_pnum;
        System.out.printf("GetTrajectoryPointNum rtn is: %d, traj num is: %d%n", rtn, trajNum);

        rtn = robot.MoveTrajectoryJ();
        System.out.printf("MoveTrajectoryJ rtn is: %d%n", rtn);

        robot.Sleep(1000);

        pkg = robot.GetRobotRealTimeState();
        int trajspeedMode = 1;
        while (pkg.motion_done == 0)
        {
            pkg = robot.GetRobotRealTimeState();

            rtn = robot.SetTrajectoryJSpeed(10.0, trajspeedMode);
            System.out.printf("SetTrajectoryJSpeed is: %d%n", rtn);

            robot.Sleep(1000);

            rtn = robot.SetTrajectoryJSpeed(80.0, trajspeedMode);
            System.out.printf("SetTrajectoryJSpeed is: %d%n", rtn);

            robot.Sleep(1000);
        }

        return 0;
    }

軌跡預處理(軌跡前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 軌跡預處理(軌跡前瞻) 
    * @param [in] name  軌跡文件名
    * @param [in] mode 採樣模式，0-不進行採樣；1-等數據間隔採樣；2-等誤差限制採樣
    * @param [in] errorLim 誤差限制，使用直線擬合生效
    * @param [in] type 平滑方式，0-貝塞爾平滑
    * @param [in] precision 平滑精度，使用貝塞爾平滑時生效
    * @param [in] vamx 設定的最大速度，mm/s
    * @param [in] amax 設定的最大加速度，mm/s2
    * @param [in] jmax 設定的最大加加速度，mm/s3
    * @return 錯誤碼 
    */ 
    int LoadTrajectoryLA(String name, int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax); 

軌跡復現(軌跡前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 軌跡復現(軌跡前瞻)  
    * @return 錯誤碼 
    */
    int MoveTrajectoryLA();

軌跡復現(軌跡前瞻)代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadTrajLA(Robot robot)
    {
        int rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");

        String traj_file_name = "/fruser/traj/traj.txt";
        rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);

        DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
        rtn = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);

        robot.Sleep(1000);
        robot.SetSpeed(50);
        robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        rtn = robot.MoveTrajectoryLA();

        robot.CloseRPC();
        return 0;
    }

運動到TPD軌跡記錄起點
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 運動到TPD軌跡記錄起點
    * @param name 軌跡文件名
    * @param moveType 運動類型；0-PTP; 1-LIN
    * @param ovl 速度縮放百分比，範圍[0~100]
    * @return 錯誤碼
    */
    public int MoveToTPDStart(string name, int moveType, double ovl)

運動到TPD軌跡記錄起點的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testTPDmove (Robot robot)
    {
        int rtn = 0;
        int type = 1;
        String name = "tpd2025";
        int period_ms = 4;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        robot.Sleep(3000);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        robot.Sleep(1000);
        double ovl = 100.0;
        int blend = 0;
        DescPose start_pose = new DescPose();
        rtn = robot.LoadTPD(name);
        System.out.printf("LoadTPD rtn is: %d\n", rtn);

        robot.GetTPDStartPose(name, start_pose);
        System.out.printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        //robot.MoveCart(&start_pose, 0, 0, 100, 100, ovl, -1, -1);
        //robot.Sleep(1000);

        rtn = robot.MoveToTPDStart(name, 0, 100);
        System.out.printf("MoveToTPDStart rtn is: %d\n", rtn);

        rtn = robot.MoveTPD(name, blend, ovl);
        System.out.printf("MoveTPD rtn is: %d\n", rtn);

        robot.Sleep(5000);

        robot.SetTPDDelete(name);

        return ;
    }