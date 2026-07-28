機器人外設
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  配置夾爪
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    errno_t  SetGripperConfig(int company, int device, int softvesion, int bus);

獲取夾爪配置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取夾爪配置
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    errno_t  GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夾爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  激活夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    errno_t  ActGripper(int index, uint8_t act);

控制夾爪
++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  控制夾爪
	 * @param  [in] index  夾爪編號
	 * @param  [in] pos  位置百分比，範圍[0~100]
	 * @param  [in] vel  速度百分比，範圍[0~100]
	 * @param  [in] force  力矩百分比，範圍[0~100]
	 * @param  [in] max_time  最大等待時間，範圍[0~30000]，單位ms
	 * @param  [in] block  0-阻塞，1-非阻塞
	 * @param  [in] type 夾爪類型，0-平行夾爪；1-旋轉夾爪
	 * @param  [in] rotNum 旋轉圈數
	 * @param  [in] rotVel 旋轉速度百分比[0-100]
	 * @param  [in] rotTorque 旋轉力矩百分比[0-100]
	 * @return  錯誤碼
	 */
	errno_t MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block, int type, double rotNum, int rotVel, int rotTorque);



獲取夾爪運動狀態
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪運動狀態
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] staus  0-運動未完成，1-運動完成
     * @return  錯誤碼
     */
    errno_t  GetGripperMotionDone(uint16_t *fault, uint8_t *status);

獲取夾爪激活狀態
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪激活狀態
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] status  bit0~bit15對應夾爪編號0~15，bit=0爲未激活，bit=1爲激活
     * @return  錯誤碼
     */
    errno_t  GetGripperActivateStatus(uint16_t *fault, uint16_t *status);

獲取夾爪位置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪位置
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] position  位置百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurPosition(uint16_t *fault, uint8_t *position);

獲取夾爪速度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪速度
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] speed  速度百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurSpeed(uint16_t *fault, int8_t *speed);

獲取夾爪電流
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪電流
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] current  電流百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurCurrent(uint16_t *fault, int8_t *current);

獲取夾爪電壓
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪電壓
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] voltage  電壓,單位0.1V
     * @return  錯誤碼
     */
    errno_t  GetGripperVoltage(uint16_t *fault, int *voltage);

獲取夾爪溫度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取夾爪溫度
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] temp  溫度，單位℃
     * @return  錯誤碼
     */
    errno_t  GetGripperTemp(uint16_t *fault, int *temp);

計算預抓取點-視覺
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算預抓取點-視覺
     * @param  [in] desc_pos  抓取點笛卡爾位姿
     * @param  [in] zlength   z軸偏移量
     * @param  [in] zangle    繞z軸旋轉偏移量
     * @return  錯誤碼 
     */
    errno_t  ComputePrePick(DescPose *desc_pos, double zlength, double zangle, DescPose *pre_pos);

計算撤退點-視覺
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算撤退點-視覺
     * @param  [in] desc_pos  抓取點笛卡爾位姿
     * @param  [in] zlength   z軸偏移量
     * @param  [in] zangle    繞z軸旋轉偏移量
     * @return  錯誤碼 
     */
    errno_t  ComputePostPick(DescPose *desc_pos, double zlength, double zangle, DescPose *post_pos);

機器人夾爪操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGripper(void)
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
      int company = 4;
      int device = 0;
      int softversion = 0;
      int bus = 2;
      int index = 2;
      int act = 0;
      int max_time = 30000;
      uint8_t block = 0;
      uint8_t status;
      uint16_t fault;
      uint16_t active_status = 0;
      uint8_t current_pos = 0;
      int8_t current = 0;
      int voltage = 0;
      int temp = 0;
      int8_t speed = 0;
      robot.SetGripperConfig(company, device, softversion, bus);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.GetGripperConfig(&company, &device, &softversion, &bus);
      printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      act = 1;
      robot.ActGripper(index, act);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
      std::this_thread::sleep_for(std::chrono::milliseconds(1000));
      robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);
      robot.GetGripperMotionDone(&fault, &status);
      printf("motion status:%u,%u\n", fault, status);
      robot.GetGripperActivateStatus(&fault, &active_status);
      printf("gripper active fault is: %u, status is: %u\n", fault, active_status);
      robot.GetGripperCurPosition(&fault, &current_pos);
      printf("fault is:%u, current position is: %u\n", fault, current_pos);
      robot.GetGripperCurCurrent(&fault, &current);
      printf("fault is:%u, current current is: %d\n", fault, current);
      robot.GetGripperVoltage(&fault, &voltage);
      printf("fault is:%u, current voltage is: %d \n", fault, voltage);
      robot.GetGripperTemp(&fault, &temp);
      printf("fault is:%u, current temperature is: %d\n", fault, temp);
      robot.GetGripperCurSpeed(&fault, &speed);
      printf("fault is:%u, current speed is: %d\n", fault, speed);
      int retval = 0;
      DescPose prepick_pose = {};
      DescPose postpick_pose = {};
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.ComputePrePick(&p1Desc, 10, 0, &prepick_pose);
      printf("ComputePrePick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z, prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);
      retval = robot.ComputePostPick(&p2Desc, -10, 0, &postpick_pose);
      printf("ComputePostPick retval is: %d\n", retval);
      printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z, postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);
      robot.CloseRPC();
      return 0;
    }

獲取旋轉夾爪的旋轉圈數
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 3.7.6版本加入

.. code-block:: c++
    :linenos:

    /**
	 * @brief  獲取旋轉夾爪的旋轉圈數
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] num  旋轉圈數
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotNum(uint16_t* fault, double* num);

獲取旋轉夾爪的旋轉速度
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  獲取旋轉夾爪的旋轉速度
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] speed  旋轉速度百分比
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotSpeed(uint16_t* fault, int* speed);

獲取旋轉夾爪的旋轉力矩
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  獲取旋轉夾爪的旋轉力矩
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] torque  旋轉力矩百分比
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotTorque(uint16_t* fault, int* torque);

獲取旋轉夾爪狀態代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestRotGripperState(void)
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
      uint16_t fault = 0;
      double rotNum = 0.0;
      int rotSpeed = 0;
      int rotTorque = 0;
      robot.GetGripperRotNum(&fault, &rotNum);
      robot.GetGripperRotSpeed(&fault, &rotSpeed);
      robot.GetGripperRotTorque(&fault, &rotTorque);
      printf("gripper rot num : %lf, gripper rotSpeed : %d, gripper rotTorque : %d\n", rotNum, rotSpeed, rotTorque);
      robot.CloseRPC();
      return 0;
    }


傳動帶啓動、停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳動帶啓動、停止
    * @param [in] status 狀態，1-啓動，0-停止 
    * @return 錯誤碼
    */
    errno_t ConveyorStartEnd(uint8_t status);

記錄IO檢測點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 記錄IO檢測點
    * @return 錯誤碼
    */
    errno_t ConveyorPointIORecord();

記錄A點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 記錄A點
    * @return 錯誤碼
    */
    errno_t ConveyorPointARecord();

記錄參考點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 記錄參考點
    * @return 錯誤碼
    */
    errno_t ConveyorRefPointRecord();

記錄B點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 記錄B點
    * @return 錯誤碼
    */
    errno_t ConveyorPointBRecord();

傳送帶工件IO檢測
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶工件IO檢測
    * @param [in] max_t 最大檢測時間，單位ms
    * @return 錯誤碼
    */
    errno_t ConveyorIODetect(int max_t);

獲取物體當前位置
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取物體當前位置
    * @param [in] mode 
    * @return 錯誤碼
    */
    errno_t ConveyorGetTrackData(int mode);

傳動帶跟蹤開始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳動帶跟蹤開始
    * @param [in] status 狀態，1-啓動，0-停止 
    * @return 錯誤碼
    */
    errno_t ConveyorTrackStart(uint8_t status);

傳動帶跟蹤停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳動帶跟蹤停止
    * @return 錯誤碼
    */
    errno_t ConveyorTrackEnd();

傳動帶參數配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 傳動帶參數配置
    * @param [in] para[0] 編碼器通道 1~2
    * @param [in] para[1] 編碼器轉一圈的脈衝數
    * @param [in] para[2] 編碼器轉一圈傳送帶行走距離
    * @param [in] para[3] 工件座標系編號 針對跟蹤運動功能選擇工件座標系編號，跟蹤抓取、TPD跟蹤設爲0
    * @param [in] para[4] 是否配視覺 0 不配 1 配
    * @param [in] para[5] 速度比 針對傳送帶跟蹤抓取選項（1-100） 其他選項默認爲1 
    * @return 錯誤碼
    */
    errno_t ConveyorSetParam(float para[6], int followType = 0, int startDis = 0, int endDis = 100);

傳動帶抓取點補償
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief 傳動帶抓取點補償
	 * @param [in] cmp 補償位置 double[3]{x, y, z}
	 * @return 錯誤碼
	 */
    errno_t ConveyorCatchPointComp(double cmp[3]);

傳送帶直線運動
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶直線運動
    * @param [in] status 狀態，1-啓動，0-停止 
    * @return 錯誤碼
    */
    errno_t TrackMoveL(char name[32], int tool, int wobj, float vel, float acc, float ovl, float blendR, uint8_t flag, uint8_t type);

傳送帶通訊輸入檢測
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測
    * @param [in] timeout 等待超時時間ms
    * @return 錯誤碼
    */
    errno_t ConveyorComDetect(int timeout);

傳送帶通訊輸入檢測觸發
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測觸發
    * @return 錯誤碼
    */
    errno_t ConveyorComDetectTrigger();

機器人傳送帶操作示例程序
++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestConveyor(void)
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
      int retval = 0;
      retval = robot.ConveyorStartEnd(1);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = robot.ConveyorPointIORecord();
      printf("ConveyorPointIORecord retval is: %d\n", retval);
      retval = robot.ConveyorPointARecord();
      printf("ConveyorPointARecord retval is: %d\n", retval);
      retval = robot.ConveyorRefPointRecord();
      printf("ConveyorRefPointRecord retval is: %d\n", retval);
      retval = robot.ConveyorPointBRecord();
      printf("ConveyorPointBRecord retval is: %d\n", retval);
      retval = robot.ConveyorStartEnd(0);
      printf("ConveyorStartEnd retval is: %d\n", retval);
      retval = 0;
      float param[6] = { 1,10000,200,0,0,20 };
      retval = robot.ConveyorSetParam(param);
      printf("ConveyorSetParam retval is: %d\n", retval);
      double cmp[3] = { 0.0, 0.0, 0.0 };
      retval = robot.ConveyorCatchPointComp(cmp);
      printf("ConveyorCatchPointComp retval is: %d\n", retval);
      int index = 1;
      int max_time = 30000;
      uint8_t block = 0;
      retval = 0;
      DescPose p1Desc(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose p2Desc(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      retval = robot.MoveCart(&p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      printf("MoveCart retval is: %d\n", retval);
      retval = robot.WaitMs(1);
      printf("WaitMs retval is: %d\n", retval);
      retval = robot.ConveyorIODetect(10000);
      printf("ConveyorIODetect retval is: %d\n", retval);
      retval = robot.ConveyorGetTrackData(1);
      printf("ConveyorGetTrackData retval is: %d\n", retval);
      retval = robot.ConveyorTrackStart(1);
      printf("ConveyorTrackStart retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      retval = robot.TrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
      printf("TrackMoveL retval is: %d\n", retval);
      retval = robot.ConveyorTrackEnd();
      printf("ConveyorTrackEnd retval is: %d\n", retval);
      robot.MoveCart(&p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
      retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);
      printf("MoveGripper retval is: %d\n", retval);
      rtn = robot->ConveyorComDetect(1000 * 10);
      printf("ConveyorComDetect rtn is: %d\n", rtn);
      robot.Sleep(2000);
      rtn = robot->ConveyorComDetectTrigger();
      printf("ConveyorComDetectTrigger rtn is: %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

傳送帶原地跟蹤參數配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.9.8
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶原地跟蹤參數配置
    * @param [in] trackMode 0-時間；1-距離；2-時間和距離任意滿足一個
    * @param [in] trackTime 跟蹤時間，單位s
    * @param [in] trackDis 跟蹤距離，單位mm
    * @return 錯誤碼
    */
    int SetStationaryTrackPara(int trackMode, double trackTime, int trackDis);
    
傳送帶原地跟蹤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.9.8
    
.. code-block:: c++
    :linenos:

    int TestStationaryTrack()
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
        printf("\n========== 傳送帶靜止跟蹤測試 ==========");
        JointPos j1(-35.146, -102.684, 120.805, -100.401, -90.295, 150.105);
        DescPose d1(-121.814, -348.341, 209.978, -173.152, -3.585, -5.446);
        ExaxisPos ex(0, 0, 0, 0);
        DescPose zeroOff(0, 0, 0, 0, 0, 0);
        int tool = 1;
        int workpiece = 1;
        float conveyorParam[6] = { 0, 10000, 200, 0, 0, 10 };
        rtn = robot.ConveyorSetParam(conveyorParam);
        robot.MoveJ(&j1, &d1, tool, workpiece, 100, 100, 100, &ex, -1, 0, &zeroOff);
        // Step 1: SetDO 控制訊號
        printf("--- Step 1: SetDO(6,1) ---\n");
        rtn = robot.SetDO(6, 1, 0, 0);
        printf("  SetDO(6,1) rtn={0}\n", rtn);
        // Step 2: 傳送帶跟蹤開始
        printf("--- Step 2: ConveyorTrackStart(2) ---\n");
        rtn = robot.ConveyorTrackStart(2);
        printf("  ConveyorTrackStart(2) rtn={0}\n", rtn);
        // Step 3: 工件IO檢測
        printf("--- Step 3: ConveyorIODetect(10000) ---\n");
        rtn = robot.ConveyorIODetect(10000);
        printf("  ConveyorIODetect(10000) rtn={0}\n", rtn);
        // Step 4: 獲取跟蹤數據
        printf("--- Step 4: ConveyorGetTrackData(2) ---\n");
        rtn = robot.ConveyorGetTrackData(2);
        printf("  ConveyorGetTrackData(2) rtn={0}\n", rtn);
        // Step 5: 靜止跟蹤參數配置 (時間模式, 200s, 距離5)
        printf("--- Step 5: SetStationaryTrackPara(0,200,5) ---\n");
        rtn = robot.SetStationaryTrackPara(0, 5, 5);
        printf("  SetStationaryTrackPara(0,200,5) rtn={0}\n", rtn);
        // Step 6: 執行靜止跟蹤運動
        printf("--- Step 6: MoveStationary() ---\n");
        rtn = robot.MoveStationary();
        rtn = robot.WaitStationaryMotionDone();
        printf("  MoveStationary() rtn={0}\n", rtn);
        // Step 7: 傳送帶跟蹤結束
        printf("--- Step 7: ConveyorTrackEnd() ---\n");
        rtn = robot.ConveyorTrackEnd();
        printf("  ConveyorTrackEnd() rtn={0}\n", rtn);
        // Step 8: SetDO 關閉訊號
        printf("--- Step 8: SetDO(6,0) ---\n");
        rtn = robot.SetDO(6, 0, 0, 0);
        printf("  SetDO(6,0) rtn={0}\n", rtn);
        printf("\n========== 靜止跟蹤測試完成 ==========\n");
        return 0;
    }

末端傳感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端傳感器配置
    * @param [in] idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param [in] idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @param [in] idSoftware 軟件版本，0-J1.0/HuiDe1.0(暫未開放)
    * @param [in] idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    * @return 錯誤碼
    */
    errno_t AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

獲取末端傳感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 獲取末端傳感器配置
     * @param [out] idCompany 廠商，18-JUNKONG；25-HUIDE
     * @param [out] idDevice 類型，0-JUNKONG/RYR6T.V1.0
     * @return 錯誤碼
     */
    errno_t AxleSensorConfigGet(int& idCompany, int& idDevice);

末端傳感器激活
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 末端傳感器激活
     * @param [in] actFlag 0-復位；1-激活
     * @return 錯誤碼
     */
    errno_t AxleSensorActivate(int actFlag);

末端傳感器寄存器寫入
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 末端傳感器寄存器寫入
     * @param [in] devAddr 設備地址編號 0-255
     * @param [in] regHAddr 寄存器地址高8位
     * @param [in] regLAddr 寄存器地址低8位
     * @param [in] regNum 寄存器個數 0-255
     * @param [in] data1 寫入寄存器數值1
     * @param [in] data2 寫入寄存器數值2
     * @param [in] isNoBlock 0-阻塞；1-非阻塞
     * @return 錯誤碼
     */
    errno_t AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端傳感器代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestAxleSensor(void)
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
      robot.AxleSensorConfig(18, 0, 0, 1);
      int company = -1;
      int type = -1;
      robot.AxleSensorConfigGet(company, type);
      printf("company is %d, type is %d\n", company, type);
      rtn = robot.AxleSensorActivate(1);
      printf("AxleSensorActivate rtn is %d\n", rtn);
      robot.Sleep(1000);
      rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
      printf("AxleSensorRegWrite rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }
        
獲取機器人外設協議
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人外設協議
    * @param [out] protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼
    */
    errno_t GetExDevProtocol(int *protocol);

設置機器人外設協議
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置機器人外設協議
    * @param [in] protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼
    */
    errno_t SetExDevProtocol(int protocol);

設置機器人外設協議示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    int TestExDevProtocol(void)
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
      int protocol = 4096;
      rtn = robot.SetExDevProtocol(protocol);
      std::cout << "SetExDevProtocol rtn " << rtn << std::endl;
      rtn = robot.GetExDevProtocol(&protocol);
      std::cout << "GetExDevProtocol rtn " << rtn << " protocol is: " << protocol << std::endl;
      robot.CloseRPC();
      return 0;
    }

獲取末端通訊參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取末端通訊參數
    * @param param 末端通訊參數
    * @return  錯誤碼
    */
    errno_t GetAxleCommunicationParam(AxleComParam* param);

設置末端通訊參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端通訊參數
    * @param param  末端通訊參數
    * @return  錯誤碼
    */
    errno_t SetAxleCommunicationParam(AxleComParam param);

設置末端文件傳輸類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端文件傳輸類型
    * @param type 1-MCU升級文件；2-LUA文件
    * @return  錯誤碼
    */
    errno_t SetAxleFileType(int type);

設置啓用末端LUA執行
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置啓用末端LUA執行
    * @param enable 0-不啓用；1-啓用
    * @return  錯誤碼
    */
    errno_t SetAxleLuaEnable(int enable);

末端LUA文件異常錯誤恢復
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 末端LUA文件異常錯誤恢復
    * @param status 0-不恢復；1-恢復
    * @return  錯誤碼
    */
    errno_t SetRecoverAxleLuaErr(int status);

末端LUA文件異常錯誤恢復
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取末端LUA執行使能狀態
    * @param status status[0]: 0-未使能；1-已使能
    * @return  錯誤碼
    */
    errno_t GetAxleLuaEnableStatus(int status[]);

設置末端LUA末端設備啟用類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端LUA末端設備啟用類型
    * @param forceSensorEnable 力感測器啟用狀態，0-不啟用；1-啟用
    * @param gripperEnable 夾爪啟用狀態，0-不啟用；1-啟用
    * @param IOEnable IO設備啟用狀態，0-不啟用；1-啟用
    * @param dexhandEnable 靈巧手啟用狀態，0-不啟用；1-啟用
    * @return  錯誤碼
    */
    errno_t SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable, int dexhandEnable);

設置末端LUA末端設備啟用類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:
        
    /**
    * @brief 獲取末端LUA末端設備啟用類型
    * @param enable enable[0]:forceSensorEnable 力感測器啟用狀態，0-不啟用；1-啟用
    * @param enable enable[1]:gripperEnable 夾爪啟用狀態，0-不啟用；1-啟用
    * @param enable enable[2]:IOEnable IO設備啟用狀態，0-不啟用；1-啟用
    * @param enable enable[3]:dexhandEnable 靈巧手啟用狀態，0-不啟用；1-啟用
    * @return 錯誤碼
    */
    errno_t GetAxleLuaEnableDeviceType(int* forceSensorEnable, int* gripperEnable, int* IOEnable, int* dexhandEnable);

獲取當前配置的末端設備
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取當前配置的末端設備
    * @param [out] forceSensorEnable 力感測器啟用設備編號 0-未啟用；1-啟用
    * @param [out] gripperEnable 夾爪啟用設備編號，0-不啟用；1-啟用
    * @param [out] IODeviceEnable IO設備啟用設備編號，0-不啟用；1-啟用
    * @param [out] decHandEnable 靈巧手啟用設備編號，0-不啟用；1-啟用
    * @return 錯誤碼
    */
    errno_t GetAxleLuaEnableDevice(int forceSensorEnable[], int gripperEnable[], int IODeviceEnable[], int decHandEnable[]);

設置啟用夾爪動作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置啟用夾爪動作控制功能
    * @param id 夾爪設備編號
    * @param func func[0]-夾爪使能；func[1]-夾爪初始化；func[2]-位置設置；func[3]-速度設置；func[4]-力矩設置；func[6]-讀夾爪狀態；
        func[7]-讀初始化狀態；func[8]-讀故障碼；func[9]-讀位置；func[10]-讀速度；func[11]-讀力矩; func[12]-旋轉夾爪旋轉圈數設置； 
        func[13]-旋轉夾爪旋轉速度設置； func[14]-旋轉夾爪旋轉力矩設置； func[15]-讀旋轉夾爪狀態；func[16]-讀旋轉夾爪初始化狀態；
        func[17]-讀旋轉夾爪圈數；func[18]-讀旋轉夾爪速度；func[19]-讀旋轉夾爪力矩；func[20]-多軸同步運動設置；func[21]-故障清除指令；
        func[22]-單軸運行狀態；func[23]-所有軸運行狀態；
    * @return  錯誤碼
    */
    errno_t SetAxleLuaGripperFunc(int id, int func[32]);

獲取啟用夾爪動作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取啟用夾爪動作控制功能
    * @param id 夾爪設備編號
    * @param func func[0]-夾爪使能；func[1]-夾爪初始化；func[2]-位置設置；func[3]-速度設置；func[4]-力矩設置；func[6]-讀夾爪狀態；
        func[7]-讀初始化狀態；func[8]-讀故障碼；func[9]-讀位置；func[10]-讀速度；func[11]-讀力矩; func[12]-旋轉夾爪旋轉圈數設置； 
        func[13]-旋轉夾爪旋轉速度設置； func[14]-旋轉夾爪旋轉力矩設置； func[15]-讀旋轉夾爪狀態；func[16]-讀旋轉夾爪初始化狀態；
        func[17]-讀旋轉夾爪圈數；func[18]-讀旋轉夾爪速度；func[19]-讀旋轉夾爪力矩；func[20]-多軸同步運動設置；func[21]-故障清除指令；
        func[22]-單軸運行狀態；func[23]-所有軸運行狀態；
    * @return  錯誤碼
    */
    errno_t GetAxleLuaGripperFunc(int id, int func[32]);

機器人Ethercat從站文件寫入
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 機器人Ethercat從站文件寫入
    * @param type 從站文件類型，1-升級從站文件；2-升級從站配置文件
    * @param slaveID 從站號
    * @param fileName 上傳文件名
    * @return  錯誤碼
    */
    errno_t SlaveFileWrite(int type, int slaveID, std::string fileName);

上傳末端Lua開放協議文件
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳末端Lua開放協議文件
    * @param filePath 本地lua文件路徑名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 錯誤碼
    */
    errno_t AxleLuaUpload(std::string filePath);

機器人Ethercat從站進入boot模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 機器人Ethercat從站進入boot模式
    * @return  錯誤碼
    */
    errno_t SetSysServoBootMode();

機器人末端LUA文件操作代碼示例
++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAxleLua(void)
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
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");
        AxleComParam param(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);
        AxleComParam getParam;
        robot.GetAxleCommunicationParam(&getParam);
        printf("GetAxleCommunicationParam param is %d %d %d %d %d %d %d\n", getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify, getParam.timeout, getParam.timeoutTimes, getParam.period);
        robot.SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot.GetAxleLuaEnableStatus(&luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0, 0);
        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int dexhandEnable = 0;
        robot.GetAxleLuaEnableDeviceType(&forceEnable, &gripperEnable, &ioEnable, &dexhandEnable);
        printf("GetAxleLuaEnableDeviceType param is %d %d %d %d\n", forceEnable, gripperEnable, ioEnable, dexhandEnable);
        int func[32] = { 0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
        rtn = robot.SetAxleLuaGripperFunc(2, func);
        printf("SetAxleLuaGripperFunc rtn is %d\n", rtn);
        int getFunc[32] = { 0 };
        rtn = robot.GetAxleLuaGripperFunc(2, getFunc);
        printf("GetAxleLuaGripperFunc rtn is %d\n", rtn);
        int getforceEnable[16] = { 0 };
        int getgripperEnable[16] = { 0 };
        int getioEnable[16] = { 0 };
        int dexhandEnable1[16] = { 0 };
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable, dexhandEnable1);
        printf("\ngetforceEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getforceEnable[i]);
        }
        printf("\ngetgripperEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getgripperEnable[i]);
        }
        printf("\ngetioEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getioEnable[i]);
        }
        printf("\n");
        robot.ActGripper(2, 0);
        robot.Sleep(2000);
        robot.ActGripper(2, 1);
        robot.Sleep(2000);
        robot.MoveGripper(2, 1, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            robot.GetRobotRealTimeState(&pkg);
            printf("gripper pos is %u\n", pkg.gripper_position);
            robot.Sleep(100);
        }
        robot.CloseRPC();
        return 0;
    }

獲取SmartTool按鈕狀態
++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取SmartTool按鈕狀態
    * @param [out] state SmartTool手柄按鈕狀態;(bit0:0-通信正常；1-通信掉線；bit1-撤銷操作；bit2-清空程序；
    bit3-A鍵；bit4-B鍵；bit5-C鍵；bit6-D鍵；bit7-E鍵；bit8-IO鍵；bit9-手自動；bit10開始)
    * @return 錯誤碼
    */
    errno_t GetSmarttoolBtnState(int& state);
    
SmartTool按鈕代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int main(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;

      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      robot.SetReConnectParam(true, 30000, 500);

      while (true)
      {
        int btn = 0;
        robot.GetSmarttoolBtnState(btn);
        cout << "smarttool " << std::bitset<sizeof(btn) * 8>(btn) << endl;

        Sleep(100);
      }
    }

控制陣列式吸盤
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制陣列式吸盤
    * @param [in] slaveID 從站號
    * @param [in] len 長度
    * @param [in] ctrlValue 控制值
    * @return 錯誤碼
    */
    errno_t FRRobot::SetSuckerCtrl(uint8_t slaveID, uint8_t len, uint8_t ctrlValue[20]);

取得陣列式吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得陣列式吸盤狀態
    * @param [in] slaveID 從站號
    * @param [out] state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param [out] pressValue 目前真空度 單位kpa 
    * @param [out] error 吸盤目前的錯誤碼
    * @return 錯誤碼
    */
	errno_t FRRobot::GetSuckerState(uint8_t slaveID, uint8_t* state, int* pressValue, int* error);

等待吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待吸盤狀態
    * @param [in] slaveID 從站號
    * @param [in] state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param [in] ms 等待最大時間
    * @return 錯誤碼
    */
    errno_t FRRobot::WaitSuckerState(uint8_t slaveID, uint8_t state, int ms);

陣列式吸盤控制指令程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testSucker()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //上傳並載入開放協定檔案
        robot.OpenLuaUpload("E://項目/外設SDK/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(1, "CtrlDev_sucker.lua");
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);

        //控制吸盤廣播模式下，按照最大能力吸附
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);

        //循環監控1號吸盤和12號吸盤的狀態
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, &state, &pressVlaue, &error);
            printf("sucker1 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.GetSuckerState(12, &state, &pressVlaue, &error);
            printf("sucker12 state is %d, pressVlaue is %d, error num is %d\n", state, pressVlaue, error);
            robot.Sleep(100);
        }

        //等待1號吸盤是否為吸附到物體的狀態，等待時間100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        printf("WaitSuckerState result is  %d\n", ret);

        //單播模式關閉1號和12號吸盤
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);

        robot.CloseRPC();
    }

上傳外設開放協定LUA檔案
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

	/**
	 * @brief 上傳Lua檔案
	 * @param [in] filePath 本機lua檔案路徑名
	 * @return 錯誤碼
	 */
    errno_t FRRobot::OpenLuaUpload(std::string filePath);

取得從站板卡參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  取得從站板卡參數
    * @param  [out] type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  [out] version  協定版本
    * @param  [out] connState  0-未連接 1-已連接
    * @return  錯誤碼
    */
    errno_t GetFieldBusConfig(uint8_t* type, uint8_t* version, uint8_t* connState);

寫入從站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  寫入從站DO
    * @param  [in] DOIndex  DO編號
    * @param  [in] wirteNum  寫入的數量
    * @param  [in] status[8] 寫入的數值，最多寫8個
    * @return  錯誤碼
    */
    errno_t FieldBusSlaveWriteDO(uint8_t DOIndex, uint8_t wirteNum, uint8_t status[8]);

寫入從站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  寫入從站AO
    * @param  [in] AOIndex  AO編號
    * @param  [in] wirteNum  寫入的數量
    * @param  [in] status[8] 寫入的數值，最多寫8個
    * @return  錯誤碼
    */
    errno_t FieldBusSlaveWriteAO(uint8_t AOIndex, uint8_t wirteNum, double status[8]);

讀取從站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  讀取從站DI
    * @param  [in] DOIndex  DI編號
    * @param  [in] readeNum  讀取的數量
    * @param  [out] status[8] 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    errno_t FieldBusSlaveReadDI(uint8_t DOIndex, uint8_t readNum, uint8_t status[8]);

讀取從站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief  讀取從站AI
    * @param  [in] AOIndex  AI編號
    * @param  [in] readeNum  讀取的數量
    * @param  [out] status[8] 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    errno_t FieldBusSlaveReadAI(uint8_t AIIndex, uint8_t readNum, double status[8]);

等待擴充DI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴充DI輸入
    * @param [in] DIIndex DI編號
    * @param [in] status 0-低電位；1-高電位
    * @param [in] waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    errno_t FRRobot::FieldBusSlaveWaitDI(uint8_t DIIndex, bool status, int waitMs);

等待擴充AI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴充AI輸入
    * @param [in] AIIndex AI編號
    * @param [in] waitType 0-大於；1-小於
    * @param [in] value AI值
    * @param [in] waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    errno_t FRRobot::FieldBusSlaveWaitAI(uint8_t AIIndex, uint8_t waitType, double value, int waitMs);

從站模式相關介面指令程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    void testFieldBusBoard()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t type = 0, version = 0, connState = 0;
        uint8_t ctrl[8];
        double ctrlAO[8];
        static uint8_t DI[8];
        static double AI[8];

        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //上傳並載入開放協定檔案
        robot.OpenLuaUpload("E://項目/外設SDK/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);

        //取得從站板卡的協定型別、軟體版本、與PLC的連接狀態
        robot.GetFieldBusConfig(&type, &version, &connState);
        printf("type is %d, version is %d,connState is %d\n", type, version, connState);

        //寫入DO0 = 1、DO1 = 0、DO2 = 1
        ctrl[0] = 0;
        ctrl[1] = 1;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);

        //寫入AO2 = 0x1000
        ctrlAO[0] = 0x1005;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        //循環監控DI0~DI3 AI0~AI2
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            printf("DI0 is %d, DI1 is %d,DI2 is %d,DI3 is %d\n", DI[0], DI[1], DI[2], DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            printf("AI0 is %d, AI1 is %d,AI2 is %d\n", AI[0], AI[1], AI[2]);
            robot.Sleep(10);
        }

        //等待DI0是否為1，等待時間100ms，並列印結果
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        printf("FieldBusSlaveWaitDI result is  %d\n", ret);

        //等待AI0是否大於400，等待時間100ms，並列印結果
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        printf("FieldBusSlaveWaitAI result is  %d\n", ret);

        robot.CloseRPC();
    }

雷射外設開啟關閉
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射外設開啟關閉函數
	 * @param [in] OnOff 0-關閉 1-開啟
	 * @param [in] weldId 焊縫ID 預設為0
	 * @return 錯誤碼
	 */
	errno_t LaserTrackingLaserOnOff(int OnOff,int weldId);
        
雷射追蹤開始結束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射追蹤開始結束函數
	 * @param [in] OnOff 0-結束 1-開始
	 * @param [in] coordId 雷射外設工具座標系編號
	 * @return 錯誤碼
	 */
 	errno_t LaserTrackingTrackOnOff(int OnOff, int coordId); 
            
雷射尋位開始-固定方向
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 雷射尋位-固定方向
    * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    * @param [in] vel 速度 單位%
    * @param [in] distance 最大尋位距離 單位mm
    * @param [in] distance 尋位逾時時間 單位ms
    * @param [in] posSensorNum 雷射標定的工具座標編號
    * @return 錯誤碼
    */
    errno_t LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum);
                
雷射尋位開始-任意點方向
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射尋位-任意方向
	 * @param [in] directionPoint 尋位輸入點的xyz座標
	 * @param [in] vel 速度 單位%
	 * @param [in] distance 最大尋位距離 單位mm
	 * @param [in] distance 尋位逾時時間 單位ms
	 * @param [in] posSensorNum 雷射標定的工具座標編號
	 * @return 錯誤碼
	 */
    errno_t LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum);
                    
雷射尋位結束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射尋位結束
	 * @return 錯誤碼
	 */
    errno_t LaserTrackingSearchStop();

雷射網路參數配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射網路參數配置
	 * @param [in] ip 雷射外設的ip地址
	 * @param [in] port 雷射外設的埠號
	 * @return 錯誤碼
	 */
    errno_t LaserTrackingSensorConfig(std::string ip, int port);
    
雷射外設取樣週期配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 雷射外設取樣週期配置
    * @param [in] period 雷射外設取樣週期 單位ms
    * @return 錯誤碼
    */
    errno_t LaserTrackingSensorSamplePeriod(int period);
        
雷射外設驅動載入
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射外設驅動載入
	 * @param [in] type 雷射外設驅動的協定類型 101-睿牛 102-創想 103-全視 104-同舟 105-奧太
	 * @return 錯誤碼
	 */
    errno_t LoadPosSensorDriver(int type);
            
雷射外設驅動卸載
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射外設驅動卸載
	 * @return 錯誤碼
	 */
    errno_t UnLoadPosSensorDriver();
                
雷射焊縫軌跡記錄
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 雷射焊縫軌跡記錄
    * @param [in] status 0-停止記錄 1-即時追蹤  2-開始記錄
    * @param [in] delayTime 延遲時間 單位ms
    * @return 錯誤碼
    */
    errno_t LaserSensorRecord1(int status, int delayTime); 
                    
雷射焊縫軌跡重現
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射焊縫軌跡重現
	 * @param [in] delayTime 延遲時間 單位ms
	 * @param [in] speed 速度 單位%
	 * @return 錯誤碼
	 */
    errno_t LaserSensorReplay(int delayTime, double speed);
                        
雷射追蹤重現
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
	 * @brief 雷射追蹤重現
	 * @return 錯誤碼
	 */
    errno_t MoveLTR();
                            
雷射焊縫軌跡記錄及重現
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 雷射焊縫軌跡記錄及重現
    * @param [in] delayMode 模式 0-延時時間 1-延時距離
    * @param [in] delayTime 延時時間 單位ms
    * @param [in] delayDisExAxisNum 擴展軸編號
    * @param [in] delayDis 延時距離 單位mm
    * @param [in] sensitivePara 補償靈敏係數
    * @param [in] trackMode 定點追蹤類型。0-擴展軸非同步運動；1-機器人
    * @param [in] triggerMode 定點追蹤觸發方式。0-追蹤時長；1-IO
    * @param [in] runTime 機器人定點追蹤時長(s)
    * @param [in] speed 速度 單位%
    * @return 錯誤碼
    */
    errno_t LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum, double delayDis, double sensitivePara, int trackMode, int triggerMode, double runTime, double speed);
                                
運動到焊縫記錄的起點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 運動到焊縫記錄的起點
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl 速度 單位%
    * @return 錯誤碼
    */
    errno_t MoveToLaserRecordStart(int moveType, double ovl);
                                    
運動到焊縫記錄的終點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 運動到焊縫記錄的終點
    * @param [in] moveType 0-moveJ 1-moveL
    * @param [in] ovl 速度 單位%
    * @return 錯誤碼
    */
    errno_t MoveToLaserRecordEnd(int moveType, double ovl);
                                        
運動到雷射感測器尋位點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 運動到雷射感測器尋位點
    * @param [in] moveFlag 運動類型：0-PTP；1-LIN
    * @param [in] ovl 速度縮放因子，0-100
    * @param [in] dataFlag 焊縫快取資料選擇：0-執行規劃資料；1-執行記錄資料
    * @param [in] plateType 板材類型：0-波紋板；1-瓦楞板；2-圍欄板；3-油桶；4-波紋甲殼鋼
    * @param [in] trackOffectType 雷射感測器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-雷射感測器原始資料偏移
    * @param [in] offset 偏移量
    * @return 錯誤碼
    */
    errno_t MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset);
                                            
取得雷射感測器尋位點座標
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 取得雷射感測器尋位點座標資訊
    * @param [in] trackOffectType 雷射感測器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-雷射感測器原始資料偏移
    * @param [in] offset 偏移量
    * @param [out] jPos 關節位置[°]
    * @param [out] descPos 笛卡爾位置[mm]
    * @param [out] tool 工具座標系
    * @param [out] user 工件座標系
    * @param [out] exaxis 擴充軸位置[mm]
    * @return 錯誤碼
    */
    errno_t GetLaserSeamPos(int trackOffectType, DescPose offset, JointPos& jPos, DescPose& descPos, int& tool, int& user, ExaxisPos& exaxis); 
                                                
雷射外設感測器參數配置及除錯程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserConfig()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);
        //設定IP地址和埠號
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        //設定取樣週期
        robot.LaserTrackingSensorSamplePeriod(20);
        //載入驅動
        robot.LoadPosSensorDriver(101);
        //關閉雷射外設
        robot.LaserTrackingLaserOnOff(0,0);
        robot.Sleep(3000);
        //開啟雷射外設
        robot.LaserTrackingLaserOnOff(1, 0);
        robot.CloseRPC();
    }
                                                    
雷射軌跡掃描及軌跡重現的程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLaserRecordAndReplay()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //上傳並載入開放協定檔案
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while(cnt<31)
        { 
            //運動到掃描的起點
            JointPos startjointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //開始軌跡記錄
            robot.LaserSensorRecord1(2, 10);
            //運動到需要記錄的終點
            JointPos endjointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(&endjointPos, &enddescPose, 1, 0, 30, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
            //停止記錄
            robot.LaserSensorRecord1(0, 10);
            //運動到記錄的焊縫起點
            robot.MoveToLaserRecordStart(1, 30);
            //開始軌跡重現
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            //停止軌跡重現
            robot.LaserSensorRecord1(0, 10);
            printf("雷射掃描+軌跡重現穩定性測試第%d次\n", cnt);
            cnt++;
        }
        robot.CloseRPC();
    }
                                                        
雷射尋位及即時追蹤的程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrack()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        //上傳並載入開放協定檔案
        robot.OpenLuaUpload("E://openlua/CtrlDev_laser_ruiniu-0117.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        robot.Sleep(8000);
        int cnt = 1;
        while (cnt < 2)
        {
            //運動到需要尋位的起始點
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            ExaxisPos exaxisPos(0, 0, 0, 0);
            DescPose offdese(0, 0, 0, 0, 0, 0);
            DescTran directionPoint;
            robot.MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);

            //沿著-y方向開始尋位
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            //如果尋位成功
            if (ret == 0)
            {
                //運動到尋位點
                robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);
                //開始沿著尋位點進行雷射追蹤
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.MoveL(&endjointPos, &enddescPose, 1, 0, 20, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
                //停止追蹤
                robot.LaserTrackingTrackOnOff(0, 2);

            }
            cnt++;
        }
        robot.CloseRPC();
    }
                                                            
擴充軸與機器人同步進行雷射追蹤的程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    void testLasertrackandExitAxis()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        uint8_t ctrl[20];
        uint8_t state;
        int pressVlaue;
        int error;
        robot.CloseRPC();
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");

        if (rtn != 0)
        {
            return;
        }
        robot.SetReConnectParam(true, 30000, 500);

        ExaxisPos startexaxisPos = { 0,0,0,0 };
        ExaxisPos seamexaxisPos = { -10,0,0,0 };
        ExaxisPos endexaxisPos = { -30, 0, 0, 0 };
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        JointPos seamjointPos(0, 0, 0, 0, 0, 0);
        DescPose seamdescPose(0, 0, 0, 0, 0, 0);
        
        int cnt = 1;
        while (cnt < 31)
        {
            //運動到需要尋位的起始點
            JointPos startjointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
            DescPose startdescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);

            //沿著-y方向開始尋位
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            int tool = 0;
            int user = 0;
            robot.GetLaserSeamPos(0, offdese, seamjointPos, seamdescPose, tool, user, startexaxisPos);
            printf("%f, %f, %f,%f, %f, %f,%f, %f, %f,%f, %f, %f\n", seamjointPos.jPos[0], seamjointPos.jPos[1], seamjointPos.jPos[2], seamjointPos.jPos[3], seamjointPos.jPos[4], seamjointPos.jPos[5], seamdescPose.tran.x, seamdescPose.tran.y, seamdescPose.tran.z, seamdescPose.rpy.rx, seamdescPose.rpy.ry, seamdescPose.rpy.rz);

            //如果尋位成功
            if (ret == 0)
            {
                //機器和擴充軸同步運動到尋位點
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);

                //開始沿著尋位點進行雷射追蹤並與擴充軸同步運動
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);;
                //停止追蹤
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            cnt++;
            printf("擴充軸與機器人同步進行雷射追蹤  第%d次\n", cnt);
        }
        robot.CloseRPC();
    } 

末端透傳功能打開關閉
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端透傳功能打開關閉
    * @param [in] 使能，0-關閉，1-開啟
    * @return 錯誤碼
    */
    errno_t SetAxleGenComEnable(int mode);
                                                            
末端透傳功能非週期數據收發
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:
    
    /**
    * @brief 末端透傳功能非週期數據收發
    * @param [in] len_snd 發送的長度
    * @param [in] sndBuff 發送數據
    * @param [in] len_rcv 選擇接受的長度
    * @param [out] rcvBuff 應答的數據
    * @return 錯誤碼
    */
    errno_t SndRcvAxleGenComCmdData(int lenSnd, int sndBuff[130], int lenRcv, int rcvData[130]);
                                                                
基於末端透傳功能倍益康艾灸頭非週期數據通訊代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int testAxleGenCom()
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
      int led_on[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
      int led_off[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int version[5] = { 0xAB, 0xBA, 0x11, 0x00, 0x76 };
      int state[6] = { 0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B };
      int cycleState[6] = { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
      int rcvdata[16] = {0};
      int ret = 0;
      int cnt = 1;
      JointPos p1Joint(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
      DescPose p1Desc(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);
      JointPos p2Joint(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
      DescPose p2Desc(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      //開啟末端透傳功能
      robot.SetAxleGenComEnable(1);
      robot.SetAxleLuaEnable(1);
      while (cnt <= 10000)
      {
        //讀取版本號
        ret = robot.SndRcvAxleGenComCmdData(5, version, 10, rcvdata);
        printf(" hard version : %d,hard code:%d, soft version:%d %d, soft code:%d \n", rcvdata[4], rcvdata[5], rcvdata[6] ,rcvdata[7], rcvdata[8]);
        if (ret != 0)
        {
          break;
        }
        robot.Sleep(1000);
        //讀取艾灸頭在位狀態
        ret = robot.SndRcvAxleGenComCmdData(6, state, 6, rcvdata);
        printf(" state : %d \n", rcvdata[4]);
        robot.Sleep(1000);
        //開啟艾灸頭激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, rcvdata);
        printf("led on rcv data is: %d, %d, %d, %d, %d, %d  \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(4000);
        //關閉艾灸頭激光
        ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, rcvdata);
        printf("led off rcv data is: %d, %d, %d, %d, %d, %d \n", rcvdata[0], rcvdata[1], rcvdata[2], rcvdata[3], rcvdata[4], rcvdata[5]);
        robot.MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot.Sleep(1000);
        printf("***********************complate No. %d SDK test*****************************\n", cnt);
        cnt++;
      }
      robot.CloseRPC();
    }

下載開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 下載開放協議Lua文件
    * @param [in] fileName 開放協議文件名稱“CtrlDev_XXX.lua”
    * @param [in] savePath 開放協議保存文件路徑
    * @return 錯誤碼
    */
    errno_t OpenLuaDownload(std::string fileName, std::string savePath);
    
刪除開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 刪除開放協議Lua文件
    * @param [in] fileName 要刪除的開放協議lua文件名“CtrlDev_XXX.lua”
    * @return 錯誤碼
    */
    errno_t OpenLuaDelete(std::string fileName);
        
刪除所有開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 刪除所有開放協議Lua文件
    * @return 錯誤碼
    */
    errno_t AllOpenLuaDelete();

控制器外設開放協議上傳下載刪除代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestCtrlOpenLuaOperate()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(1);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return 0;
        }
        robot.SetReConnectParam(true, 30000, 500);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        printf("OpenLuaUpload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        printf("OpenLuaDownload rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        printf("SetCtrlOpenLUAName rtn is %d\n", rtn);
        std::string name[4] = {};
        rtn = robot.GetCtrlOpenLUAName(name);
        printf("ctrl open lua names : %s, %s, %s, %s\n", name[0].c_str(), name[1].c_str(), name[2].c_str(), name[3].c_str());
        rtn = robot.LoadCtrlOpenLUA(1);
        printf("LoadCtrlOpenLUA rtn is %d\n", rtn);
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        printf("UnloadCtrlOpenLUA rtn is %d\n", rtn);
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        printf("OpenLuaDelete rtn is %d\n", rtn);
        rtn = robot.AllOpenLuaDelete();
        printf("AllOpenLuaDelete rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }

    
控制靈巧手運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制靈巧手運動
    * @param [in] idstart 起始從站號
    * @param [in] slaveNum 數量
    * @param [in] pos 位置陣列，長度16，範圍(-360~360)
    * @param [in] speed 速度百分比陣列，長度16，範圍[0~100]
    * @param [in] force 力矩百分比陣列，長度16，範圍[0~100]
    * @param [in] max_time 最大等待時間，範圍[0~30000]，單位ms
    * @return 錯誤碼，成功返回0
    */
    errno_t SetDexterousHandsMove(int idstart, int slaveNum, double pos[16], int speed[16], int force[16], int max_time);
        
控制靈巧手復位激活
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制靈巧手復位激活
    * @param [in] id 從站號
    * @param [in] act 0-復位 1-激活
    * @return 錯誤碼，成功返回0
    */
    errno_t SetDexterousHandsAct(int id, int act);
            
清除靈巧手錯誤
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 清除靈巧手錯誤
    * @return 錯誤碼，成功返回0
    */
    errno_t ClearDexterousHandsError();
                
設置啟用靈巧手動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置啟用靈巧手動作控制功能
    * @param [in] id 靈巧手設備編號
    * @param [in] func 0-夾持觸發、1-夾爪初始化、2-位置設置、3-速度設置、4-力矩設置、6-讀夾爪狀態、7-讀初始化狀態、8-讀故障碼、9-讀位置、10-讀速度、11-讀力矩、12-旋轉圈數設置、13-旋轉速度設置、14-旋轉力矩設置、15-讀旋轉夾爪狀態、16-讀旋轉初始化狀態、17-讀旋轉圈數、18-讀旋轉速度、19-讀旋轉力矩、20-多軸同步運動設置、21-故障清除指令、22-單軸運行狀態、23-所有軸運行狀態
    * @return 錯誤碼
    */
    errno_t SetDexterousHandsFunc(int id, int func[32]);
                    
獲取啟用靈巧手動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取啟用靈巧手動作控制功能
    * @param [in] id 靈巧手設備編號
    * @param [out] func 0-夾持觸發、1-夾爪初始化、2-位置設置、3-速度設置、4-力矩設置、6-讀夾爪狀態、7-讀初始化狀態、8-讀故障碼、9-讀位置、10-讀速度、11-讀力矩、12-旋轉圈數設置、13-旋轉速度設置、14-旋轉力矩設置、15-讀旋轉夾爪狀態、16-讀旋轉初始化狀態、17-讀旋轉圈數、18-讀旋轉速度、19-讀旋轉力矩、20-多軸同步運動設置、21-故障清除指令、22-單軸運行狀態、23-所有軸運行狀態
    * @return 錯誤碼
    */
    errno_t GetDexterousHandsFunc(int id, int func[32]);
                        
末端靈巧手配置及運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestDexterousHands()
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
    int id = 1;        // 從站號
    int slaveNum = 4;     // 控制4個手指
    int max_time = 8000;   // 最大等待時間 8秒
    int speed[16] = {0};   // 速度陣列，全0表示使用默認速度
    int force[16] = {0};   // 力矩陣列
    // 初始化力矩陣列：前4個手指設為50%，其餘為0（透過Move指令下發數值）
    for (int i = 0; i < 16; i++)
    {
        force[i] = (i < 4) ? 50 : 0;
    }
    // 輔助函數：設置位置陣列（前4個手指有效）
    double pos[16] = {0.0};
    JointPos j1(-91.876, -85.920, 109.279, -86.239, -96.664, -28.563);
    JointPos j2(-40.954, -85.920, 109.279, -86.239, -96.664, -28.563);
    ExaxisPos epos(0, 0, 0, 0);
    DescPose offset_pos(0, 0, 0, 0, 0, 0);
    printf("===== 靈巧手完整功能測試開始 =====\n");
    // 1. 清除錯誤
    int ret = robot.ClearDexterousHandsError();
    printf("ClearDexterousHandsError rtn %d\n", ret);
    // ========== 2. 設置功能開關 ==========
    int setFunc[32] = {0};
    setFunc[2] = 1;  // 啟用位置設置功能
    setFunc[4] = 1;  // 啟用力矩設置功能
    setFunc[9] = 1;  // 讀位置
    setFunc[10] = 1;  // 讀力矩
    setFunc[11] = 1;  // 讀狀態
    setFunc[22] = 1;  // 單軸運動狀態
    ret = robot.SetDexterousHandsFunc(id, setFunc);
    printf("SetDexterousHandsFunc(使能+初始化+位置/速度/力矩功能啟用) rtn %d\n", ret);
    // ========== 3. 讀取功能狀態（驗證設置是否生效） ==========
    int getFunc[32] = {0}; // GetDexterousHandsFunc 返回32個整數
    ret = robot.GetDexterousHandsFunc(id, getFunc);
    printf("GetDexterousHandsFunc rtn %d\n", ret);
    if (ret == 0)
    {
        // 打印全部32個數值
        printf("GetDexterousHandsFunc 返回的全部32個數值:");
        for (int i = 0; i < 32; i++)
        {
        printf(" [%d]={%d}", i, getFunc[i]);
        if ((i + 1) % 8 == 0)
        {
            printf("\n");
        } 
        else if (i < 31)
        {
            printf(", ");
        }
        }
    }
    // ========== 4. 激活靈巧手 ==========
    ret = robot.SetDexterousHandsAct(id, 1);
    printf("SetDexterousHandsAct(激活) rtn %d\n", ret);
    if (ret != 0)
    {
        printf("激活失敗，測試中止");
        return -1;
    }
    // ========== 5. 初始移動到 20°（透過Move指令下發位置和力矩數值） ==========
    memset(pos, 0, sizeof(pos));
    pos[0] = 20;
    pos[1] = 20;
    pos[2] = 20;
    pos[3] = 20;
    ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
    printf("初始移動 20° -> %d\n", ret);
    robot.Sleep(5000);
    // ========== 6. 往復運動10次（10° ↔ 50°） ==========
    printf("開始往復運動10次...");
    for (int iteration = 1; iteration <= 10; iteration++)
    {
        robot.MoveJ(&j1, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        memset(pos, 0, sizeof(pos));
        pos[0] = 10;
        pos[1] = 10;
        pos[2] = 10;
        pos[3] = 10;
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        printf("移動到 10° -> %d\n", ret);
        robot.Sleep(1000);
        robot.MoveJ(&j2, 0, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
        memset(pos, 0, sizeof(pos));
        pos[0] = 50;
        pos[1] = 50;
        pos[2] = 50;
        pos[3] = 50;
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time);
        printf("移動到 50° -> %d\n", ret);
        robot.Sleep(1000);
    }
    printf("測試完成（功能開關設置/讀取 + 激活 + 10次往復運動）。");
    return 0;
    }        