機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設定軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDParam(int type, String name, int period_ms, int di_choose, int do_choose);

開始軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SetTPDStart(int type, String name, int period_ms, int di_choose, int do_choose);

停止軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: java
    :linenos:

    /**
    * @brief  停止軌跡記錄
    * @return  錯誤碼
    */
    int SetWebTPDStop(); 

刪除軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  刪除軌跡記錄
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */   
    int SetTPDDelete(string name); 

代碼範例
++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        int type = 1;
        String name = "tpd_2024";
        int period_ms = 2;
        int di_choose = 0;
        int do_choose = 0;

        robot.SetTPDDelete(name);//刪除軌跡記錄

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);//設定軌跡記錄參數

        robot.Mode(1);
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);//開始軌跡記錄
        robot.Sleep(10000);
        robot.SetWebTPDStop();//停止軌跡記錄
        robot.DragTeachSwitch(0);
    }

軌跡預載
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  軌跡預載
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */      
    int LoadTPD(String name);

取得軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得軌跡起始位姿 
    * @param [in] name  軌跡檔名,不需要文件後綴
    * @param [out] desc_pose 所獲得的軌跡起始位姿
    * @return 錯誤碼 
    */ 
    int GetTPDStartPose(String name, DescPose desc_pose); 

軌跡復現
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  軌跡復現
    * @param  [in] name  軌跡檔名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int MoveTPD(String name, int blend, double ovl); 

設定軌跡運行中的速度
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定軌跡運行中的速度
    * @param  [in] ovl 速度百分比
    * @return  錯誤碼
    */
    int SetTrajectoryJSpeed(double ovl); 

代碼範例
++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
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

外部軌跡檔案預處理
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部軌跡檔案預處理 
    * @param [in] name 軌跡檔名  
    * @param [in] ovl 速度縮放百分比，範圍[0~100]
    * @param [in] opt 1-控制點，預設為1 
    * @return 錯誤碼 
    */ 
    int LoadTrajectoryJ(String name, double ovl, int opt); 

外部軌跡文件軌跡復現
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 外部軌跡文件軌跡復現  
    * @return 錯誤碼 
    */
    int MoveTrajectoryJ();

軌跡預處理(軌跡前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 軌跡預處理(軌跡前瞻) 
    * @param [in] name  軌跡檔案名
    * @param [in] mode 採樣模式，0-不進行採樣；1-等資料間隔採樣；2-等誤差限制採樣
    * @param [in] errorLim 誤差限制，使用直線擬合生效
    * @param [in] type 平滑方式，0-貝茲平滑
    * @param [in] precision 平滑精度，使用貝茲平滑時生效
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

程式碼範例
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }

        int rtn = 0;

        String nameA = "/fruser/traj/A.txt";
        String nameB = "/fruser/traj/B.txt";

        rtn = robot.LoadTrajectoryLA(nameA, 2, 0.0, 0, 1.0, 100.0, 200.0, 1000.0);//B樣條
        //rtn = robot.LoadTrajectoryLA(nameA, 1, 2, 0, 2, 100.0, 200.0, 1000.0);

        //rtn = robot.LoadTrajectoryLA(nameB, 0, 0, 0, 1, 100.0, 100.0, 1000.0);    // 直線擬合
        System.out.println("LoadTrajectoryLA rtn is :"+ rtn);

        DescPose startPos = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetTrajectoryStartPose(nameA, startPos);

        // MoveCart方法呼叫
        robot.MoveCart(startPos, 1, 0, (float)100.0, (float)100.0, (float)100.0, -1, -1);

        rtn = robot.MoveTrajectoryLA();
        System.out.println("MoveTrajectoryLA rtn is: "+ rtn);
    }

取得軌跡檔案軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得軌跡起始位姿 
    * @param [in] name 軌跡檔名  
    * @param [out] desc_pose 所獲得的軌跡起始位姿
    * @return 錯誤碼 
    */ 
    int GetTrajectoryStartPose(String name, DescPose desc_pose); 

設定軌跡檔案軌跡運行中的力和力矩
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡檔案軌跡運行中的力和力矩  
    * @param [in] ft 三個方向的力和扭矩，單位N和Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceTorque(ForceTorque ft); 

設定軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿x方向的力  
    * @param [in] fx 沿x方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFx(double fx);

設定軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿y方向的力
    * @param [in] fy 沿y方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFy(double fy);

設定軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運行中的沿z方向的力  
    * @param [in] fz  沿z方向的力，單位N
    * @return 錯誤碼 
    */
    int SetTrajectoryJForceFz(double fz);

設定軌跡運轉中的繞x軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞x軸的扭矩  
    * @param [in] tx 繞x軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTx(double tx);

設定軌跡運轉中的繞y軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞y軸的扭矩  
    * @param [in] ty 繞y軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTy(double ty);

設定軌跡運轉中的繞z軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定軌跡運轉中的繞z軸的扭矩  
    * @param [in] tz 繞z軸的扭矩，單位Nm
    * @return 錯誤碼 
    */
    int SetTrajectoryJTorqueTz(double tz);

代碼範例
++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
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

上傳軌跡J文件
++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 上傳軌跡J文件
 * @param [in] filePath 上傳軌跡檔案的全路徑名稱 C://test/testJ.txt
 * @return 錯誤碼
 */
 int TrajectoryJUpLoad(String filePath);

刪除軌跡J文件
++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 刪除軌跡J文件
 * @param [in] fileName 檔名 testJ.txt
 * @return 錯誤碼
 */
 int TrajectoryJDelete(String fileName);

程式碼範例
++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 public static void main(String[] args)
 {
 Robot robot = new Robot();
 robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
 robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
 int rtn = robot.RPC("192.168.58.2");
 if(rtn == 0)
 {
 System.out.println("rpc連線 success");
 }
 else
 {
 System.out.println("rpc連線 fail");
 return ;
 }

 robot.TrajectoryJDelete("testA.txt");//刪除軌跡文件
 robot.TrajectoryJUpLoad("D://zUP/testA.txt");//上傳軌跡J文件

 int retval = 0;
 String traj_file_name= "/fruser/traj/testA.txt";
 retval = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
 System.out.println("LoadTrajectoryJ %s, retval is:"+traj_file_name+retval);

 DescPose traj_start_pose=new DescPose(0,0,0,0,0,0);
 retval = robot.GetTrajectoryStartPose(traj_file_name, traj_start_pose);
 System.out.println("GetTrajectoryStartPose is: %d"+retval);
 System.out.println("desc_pos:"+"("+traj_start_pose.tran.x+","+traj_start_pose.tran.y+","+traj_start_pose.tran.z+","+traj_start_pose.tran.y+","+traj_start_pose.tran.z+","+traj_start_pose.rpy.rx+" );

 robot.SetSpeed(30);
 robot.MoveCart(traj_start_pose, 1, 0, 100, 100, 100, -1, -1);

 robot.Sleep(5000);

 int traj_num = 0;

 ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
 traj_num=pkg.trajectory_pnum;
 System.out.println("GetTrajectoryStartPose traj num is:"+traj_num);

 retval = robot.MoveTrajectoryJ();
 System.out.println("MoveTrajectoryJ retval is:"+retval);
 }
