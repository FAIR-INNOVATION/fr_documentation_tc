機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設置TPD軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  SetTPDParam(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose);

開始TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t  SetTPDStart(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose); 

停止TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  停止TPD軌跡記錄
    * @return  錯誤碼
    */
    errno_t  SetWebTPDStop();

刪除TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  刪除TPD軌跡記錄
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */   
    errno_t  SetTPDDelete(char name[30]);

TPD軌跡預加載
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD軌跡預加載
    * @param  [in] name  軌跡文件名
    * @return  錯誤碼
    */      
    errno_t  LoadTPD(char name[30]);

TPD軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD軌跡復現
    * @param  [in] name  軌跡文件名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    errno_t  MoveTPD(char name[30], uint8_t blend, float ovl);

獲取TPD起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TPD起始位姿
     * @param  [in] name TPD文件名,不需要文件後綴
     * @return  錯誤碼
     */     
    errno_t  GetTPDStartPose(char name[30], DescPose *desc_pose);

運動到TPD軌跡記錄起點
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 運動到TPD軌跡記錄起點
    * @param [in] name 軌跡文件名
    * @param [in] moveType 運動類型；0-PTP; 1-LIN
    * @param [in] ovl 速度縮放百分比，範圍[0~100]
    * @return 錯誤碼
    */
    errno_t MoveToTPDStart(char name[30], uint8_t moveType, float ovl);
    
機器人TPD軌跡記錄代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTPD(void)
    {
    ROBOT_STATE_PKG pkg = {};
    FRRobot robot;
    robot.LoggerInit();
    robot.SetLoggerLevel(1);
    int rtn = robot.RPC("192.168.58.2");
    if (rtn != 0)
    {
        return -1;
    }
    robot.SetReConnectParam(true, 30000, 500);
    int type = 1;
    char name[30] = "tpd2025";
    int period_ms = 4;
    uint16_t di_choose = 0;
    uint16_t do_choose = 0;
    robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);
    robot.Mode(1);
    robot.Sleep(1000);
    robot.DragTeachSwitch(1);
    robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
    robot.Sleep(3000);
    robot.SetWebTPDStop();
    robot.DragTeachSwitch(0);
    robot.Sleep(1000);
    float ovl = 100.0;
    uint8_t blend = 0;
    DescPose start_pose = {};
    rtn = robot.LoadTPD(name);
    printf("LoadTPD rtn is: %d\n", rtn);
    robot.GetTPDStartPose(name, &start_pose);
    printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
    rtn = robot.MoveToTPDStart(name, 0, 100);
    printf("MoveToTPDStart rtn is: %d\n", rtn);
    rtn = robot.MoveTPD(name, blend, ovl);
    printf("MoveTPD rtn is: %d\n", rtn);
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    robot.SetTPDDelete(name);
    robot.CloseRPC();
    return 0;
    }

機器人TPD軌跡記錄代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTPD(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      int type = 1;
      char name[30] = "tpd2025";
      int period_ms = 4;
      uint16_t di_choose = 0;
      uint16_t do_choose = 0;
      robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);
      robot.Mode(1);
      robot.Sleep(1000);
      robot.DragTeachSwitch(1);
      robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
      robot.Sleep(10000);
      robot.SetWebTPDStop();
      robot.DragTeachSwitch(0);
      float ovl = 100.0;
      uint8_t blend = 0;
      DescPose start_pose = {};
      rtn = robot.LoadTPD(name);
      printf("LoadTPD rtn is: %d\n", rtn);
      robot.GetTPDStartPose(name, &start_pose);
      printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
      robot.MoveCart(&start_pose, 0, 0, 100, 100, ovl, -1, -1);
      robot.Sleep(1000);
      rtn = robot.MoveTPD(name, blend, ovl);
      printf("MoveTPD rtn is: %d\n", rtn);
      std::this_thread::sleep_for(std::chrono::milliseconds(5000));
      robot.SetTPDDelete(name);
      robot.CloseRPC();
      return 0;
    }

軌跡預處理
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  軌跡預處理
     * @param  [in] name  軌跡文件名
     * @param  [in] ovl 速度縮放百分比，範圍[0~100]
     * @param  [in] opt 1-控制點，默認爲1
     * @return  錯誤碼
     */     
    errno_t  LoadTrajectoryJ(char name[30], float ovl, int opt);

軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  軌跡復現
     * @return  錯誤碼
     */     
    errno_t  MoveTrajectoryJ();

獲取軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取軌跡起始位姿
     * @param  [in] name 軌跡文件名
     * @return  錯誤碼
     */     
    errno_t  GetTrajectoryStartPose(char name[30], DescPose *desc_pose);

獲取軌跡點編號
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取軌跡點編號
     * @return  錯誤碼
     */     
    errno_t  GetTrajectoryPointNum(int *pnum);

設置軌跡運行中的速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置軌跡運行中的速度
    * @param [in] ovl 速度百分比[0-100.0]
    * @param [in] mode 模式；0-降速模式；1-直接切換
    * @return 錯誤碼
    */
    errno_t SetTrajectoryJSpeed(float ovl, int mode = 0);

機器人設置軌跡運行中的速度代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSetTrajectoryJSpeed() 
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        robot.SetReConnectParam(true, 30000, 500);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return -1;
        }
        
        rtn = robot.TrajectoryJUpLoad("D://zUP/trajHelix_aima_1.txt");
        printf("Upload TrajectoryJ A %d\n", rtn);
        char traj_file_name[90] = "/fruser/traj/trajHelix_aima_1.txt";
        rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        printf("LoadTrajectoryJ %s, rtn is: %d\n", traj_file_name, rtn);
        DescPose traj_start_pose;
        memset(&traj_start_pose, 0, sizeof(DescPose));
        rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
        printf("GetTrajectoryStartPose is: %d\n", rtn);
        printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
        std::this_thread::sleep_for(std::chrono::seconds(1));
        robot.SetSpeed(50);
        robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
        int traj_num = 0;
        rtn = robot.GetTrajectoryPointNum(&traj_num);
        printf("GetTrajectoryStartPose rtn is: %d, traj num is: %d\n", rtn, traj_num);
        rtn = robot.MoveTrajectoryJ();
        printf("MoveTrajectoryJ rtn is: %d\n", rtn);
        robot.Sleep(1000);
        robot.GetRobotRealTimeState(&pkg);
        int trajspeedMode = 1;
        while (pkg.motion_done == 0)
        {
            robot.GetRobotRealTimeState(&pkg);
            rtn = robot.SetTrajectoryJSpeed(10.0, trajspeedMode);
            printf("SetTrajectoryJSpeed is: %d\n", rtn);
            robot.Sleep(1000);
            rtn = robot.SetTrajectoryJSpeed(80.0, trajspeedMode);
            printf("SetTrajectoryJSpeed is: %d\n", rtn);
            robot.Sleep(1000);
        }
        robot.CloseRPC();
        robot.Sleep(1000000);
        return 0;
    }

設置軌跡運行中的力和扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的力和扭矩
     * @param  [in] ft 三個方向的力和扭矩，單位N和Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceTorque(ForceTorque *ft);

設置軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的沿x方向的力
     * @param  [in] fx 沿x方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFx(double fx);

設置軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的沿y方向的力
     * @param  [in] fy 沿y方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFy(double fy);

設置軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的沿z方向的力
     * @param  [in] fz 沿x方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFz(double fz);

設置軌跡運行中的繞x軸的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的繞x軸的扭矩
     * @param  [in] tx 繞x軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTx(double tx);

設置軌跡運行中的繞y軸的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的繞y軸的扭矩
     * @param  [in] ty 繞y軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTy(double ty);

設置軌跡運行中的繞z軸的扭矩
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設置軌跡運行中的繞z軸的扭矩
     * @param  [in] tz 繞z軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTz(double tz);

上傳軌跡J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 上傳軌跡J文件
	 * @param [in] filePath 上傳軌跡文件的全路徑名   C://test/testJ.txt
	 * @return 錯誤碼
	 */
	errno_t TrajectoryJUpLoad(const std::string& filePath);

刪除軌跡J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 刪除軌跡J文件
	 * @param [in] fileName 文件名稱 testJ.txt
	 * @return 錯誤碼
	 */
	errno_t TrajectoryJDelete(const std::string& fileName);

機器人軌跡J文件復現代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestTraj(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj1.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj1.txt";
      rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
      printf("LoadTrajectoryJ %s, rtn is: %d\n", traj_file_name, rtn);
      DescPose traj_start_pose;
      memset(&traj_start_pose, 0, sizeof(DescPose));
      rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
      printf("GetTrajectoryStartPose is: %d\n", rtn);
      printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
      std::this_thread::sleep_for(std::chrono::seconds(1));
      robot.SetSpeed(50);
      robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
      int traj_num = 0;
      rtn = robot.GetTrajectoryPointNum(&traj_num);
      printf("GetTrajectoryStartPose rtn is: %d, traj num is: %d\n", rtn, traj_num);
      rtn = robot.SetTrajectoryJSpeed(50.0);
      printf("SetTrajectoryJSpeed is: %d\n", rtn);
      ForceTorque traj_force;
      memset(&traj_force, 0, sizeof(ForceTorque));
      traj_force.fx = 10;
      rtn = robot.SetTrajectoryJForceTorque(&traj_force);
      printf("SetTrajectoryJForceTorque rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFx(10.0);
      printf("SetTrajectoryJForceFx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFy(0.0);
      printf("SetTrajectoryJForceFy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJForceFz(0.0);
      printf("SetTrajectoryJForceFz rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTx(10.0);
      printf("SetTrajectoryJTorqueTx rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTy(10.0);
      printf("SetTrajectoryJTorqueTy rtn is: %d\n", rtn);
      rtn = robot.SetTrajectoryJTorqueTz(10.0);
      printf("SetTrajectoryJTorqueTz rtn is: %d\n", rtn);
      rtn = robot.MoveTrajectoryJ();
      printf("MoveTrajectoryJ rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

軌跡預處理(軌跡前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
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
	 * @param [in] flag 勻速前瞻開關；0-不開啟；1-開啟
	 * @return 錯誤碼
	 */
	 errno_t LoadTrajectoryLA(char name[30], int mode, double errorLim, int type, double precision, double vamx, double amax, double jmax, int flag = 0);

軌跡復現(軌跡前瞻)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  軌跡復現(軌跡前瞻)
    * @return  錯誤碼
    */
    errno_t MoveTrajectoryLA();

軌跡復現(軌跡前瞻)代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLoadTrajLA(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt");
      printf("Upload TrajectoryJ A %d\n", rtn);
      char traj_file_name[30] = "/fruser/traj/traj.txt";
      rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 100, 200, 1000);
      printf("LoadTrajectoryLA %s, rtn is: %d\n", traj_file_name, rtn);
      DescPose traj_start_pose;
      memset(&traj_start_pose, 0, sizeof(DescPose));
      rtn = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
      printf("GetTrajectoryStartPose is: %d\n", rtn);
      printf("desc_pos:%f,%f,%f,%f,%f,%f\n", traj_start_pose.tran.x, traj_start_pose.tran.y, traj_start_pose.tran.z, traj_start_pose.rpy.rx, traj_start_pose.rpy.ry, traj_start_pose.rpy.rz);
      std::this_thread::sleep_for(std::chrono::seconds(1));
      robot.SetSpeed(50);
      robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);
      rtn = robot.MoveTrajectoryLA();
      printf("MoveTrajectoryLA rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }