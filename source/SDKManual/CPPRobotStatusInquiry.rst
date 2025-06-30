機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

獲取當前關節位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前關節位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位deg
    * @return  錯誤碼
    */
    errno_t  GetActualJointPosDegree(uint8_t flag, JointPos *jPos);

獲取關節反饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取關節反饋速度-deg/s
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed 六個關節速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualJointSpeedsDegree(uint8_t flag, float speed[6]);

獲取關節反饋加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取關節反饋加速度-deg/s^2
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] acc 六個關節加速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualJointAccDegree(uint8_t flag, float acc[6]);   

獲取TCP指令合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP指令合速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] tcp_speed 線性速度
     * @param  [out] ori_speed 姿態速度
     * @return  錯誤碼 
     */
    errno_t  GetTargetTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

獲取TCP反饋合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP反饋合速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] tcp_speed 線性速度
     * @param  [out] ori_speed 姿態速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

獲取TCP指令速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP指令速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed [x,y,z,rx,ry,rz]速度
     * @return  錯誤碼 
     */ 
    errno_t  GetTargetTCPSpeed(uint8_t flag, float speed[6]);

獲取TCP反饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP反饋速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed [x,y,z,rx,ry,rz]速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualTCPSpeed(uint8_t flag, float speed[6]);

獲取當前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    errno_t  GetActualTCPPose(uint8_t flag, DescPose *desc_pos);

獲取當前工具座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前工具座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具座標系編號
    * @return  錯誤碼
    */
    errno_t  GetActualTCPNum(uint8_t flag, int *id);

獲取當前工件座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前工件座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件座標系編號
    * @return  錯誤碼
    */
    errno_t  GetActualWObjNum(uint8_t flag, int *id);  

獲取當前末端法蘭位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前末端法蘭位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法蘭位姿
    * @return  錯誤碼
    */
    errno_t  GetActualToolFlangePose(uint8_t flag, DescPose *desc_pos);  

獲取當前關節轉矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取當前關節轉矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 關節轉矩
    * @return  錯誤碼
    */
    errno_t  GetJointTorques(uint8_t flag, float torques[6]);

獲取系統時間
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取系統時間
    * @param  [out] t_ms 單位ms
    * @return  錯誤碼
    */
    errno_t  GetSystemClock(float *t_ms);

查詢機器人運動是否完成
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢機器人運動是否完成
    * @param  [out]  state  0-未完成，1-完成
    * @return  錯誤碼
    */   
    errno_t  GetRobotMotionDone(uint8_t *state);

查詢機器人運動隊列緩存長度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查詢機器人運動隊列緩存長度
     * @param  [out]  len  緩存長度
     * @return  錯誤碼
     */ 
    errno_t  GetMotionQueueLength(int *len);

獲取機器人急停狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人急停狀態
    * @param [out] state 急停狀態，0-非急停，1-急停
    * @return 錯誤碼 
    */
    errno_t GetRobotEmergencyStopState(uint8_t *state);

獲取SDK與機器人的通訊狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取SDK與機器人的通訊狀態
    * @param [out] state 通訊狀態，0-通訊正常，1-通訊異常
    */
    errno_t GetSDKComState(int *state);

獲取安全停止信號
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取安全停止信號
    * @param [out] si0_state 安全停止信號SI0，0-無效，1-有效
    * @param [out] si1_state 安全停止信號SI1，0-無效，1-有效
    */
    errno_t GetSafetyStopState(uint8_t *si0_state, uint8_t *si1_state);

獲取機器人關節驅動器溫度(℃)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器溫度(℃)
    * @return 錯誤碼
    */
    errno_t GetJointDriverTemperature(double temperature[]);

獲取機器人關節驅動器扭矩(Nm)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器扭矩(Nm)
    * @return 錯誤碼
    */
    errno_t GetJointDriverTorque(double torque[]);
        
獲取機器人實時狀態結構體
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人實時狀態結構體
    * @param [out] pkg 機器人實時狀態結構體
    * @return 錯誤碼
    */
    errno_t GetRobotRealTimeState(ROBOT_STATE_PKG *pkg);

機器人狀態查詢代碼示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos: 

    int TestGetStatus(void)
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
      float yangle, zangle;
      robot.GetRobotInstallAngle(&yangle, &zangle);
      printf("yangle:%f,zangle:%f\n", yangle, zangle);
      JointPos j_deg = {};
      robot.GetActualJointPosDegree(0, &j_deg);
      printf("joint pos deg:%f,%f,%f,%f,%f,%f\n", j_deg.jPos[0], j_deg.jPos[1], j_deg.jPos[2], j_deg.jPos[3], j_deg.jPos[4], j_deg.jPos[5]);
      float jointSpeed[6] = { 0.0 };
      robot.GetActualJointSpeedsDegree(0, jointSpeed);
      printf("joint speeds deg:%f,%f,%f,%f,%f,%f\n", jointSpeed[0], jointSpeed[1], jointSpeed[2], jointSpeed[3], jointSpeed[4], jointSpeed[5]);
      float jointAcc[6] = { 0.0 };
      robot.GetActualJointAccDegree(0, jointAcc);
      printf("joint acc deg:%f,%f,%f,%f,%f,%f\n", jointAcc[0], jointAcc[1], jointAcc[2], jointAcc[3], jointAcc[4], jointAcc[5]);
      float tcp_speed = 0.0;
      float ori_speed = 0.0;
      robot.GetTargetTCPCompositeSpeed(0, &tcp_speed, &ori_speed);
      printf("GetTargetTCPCompositeSpeed tcp %f; ori %f\n", tcp_speed, ori_speed);
      robot.GetActualTCPCompositeSpeed(0, &tcp_speed, &ori_speed);
      printf("GetActualTCPCompositeSpeed tcp %f; ori %f\n", tcp_speed, ori_speed);
      float targetSpeed[6] = { 0.0 };
      robot.GetTargetTCPSpeed(0, targetSpeed);
      printf("GetTargetTCPSpeed %f,%f,%f,%f,%f,%f\n", targetSpeed[0], targetSpeed[1], targetSpeed[2], targetSpeed[3], targetSpeed[4], targetSpeed[5]);
      float actualSpeed[6] = { 0.0 };
      robot.GetActualTCPSpeed(0, actualSpeed);
      printf("GetTargetTCPSpeed %f,%f,%f,%f,%f,%f\n", actualSpeed[0], actualSpeed[1], actualSpeed[2], actualSpeed[3], actualSpeed[4], actualSpeed[5]);
      DescPose tcp = {};
      robot.GetActualTCPPose(0, &tcp);
      printf("tcp pose:%f,%f,%f,%f,%f,%f\n", tcp.tran.x, tcp.tran.y, tcp.tran.z, tcp.rpy.rx, tcp.rpy.ry, tcp.rpy.rz);
      DescPose flange = {};
      robot.GetActualToolFlangePose(0, &flange);
      printf("flange pose:%f,%f,%f,%f,%f,%f\n", flange.tran.x, flange.tran.y, flange.tran.z, flange.rpy.rx, flange.rpy.ry, flange.rpy.rz);
      int id = 0;
      robot.GetActualTCPNum(0, &id);
      printf("tcp num:%d\n", id);
      robot.GetActualWObjNum(0, &id);
      printf("wobj num:%d\n", id);
      float jtorque[6] = { 0.0 };
      robot.GetJointTorques(0, jtorque);
      printf("torques:%f,%f,%f,%f,%f,%f\n", jtorque[0], jtorque[1], jtorque[2], jtorque[3], jtorque[4], jtorque[5]);
      float t_ms = 0.0;
      robot.GetSystemClock(&t_ms);
      printf("system clock:%f\n", t_ms);
      int config = 0;
      robot.GetRobotCurJointsConfig(&config);
      printf("joint config:%d\n", config);
      uint8_t motionDone = 0;
      robot.GetRobotMotionDone(&motionDone);
      printf("GetRobotMotionDone :%d\n", motionDone);
      int len = 0;
      robot.GetMotionQueueLength(&len);
      printf("GetMotionQueueLength :%d\n", len);
      uint8_t emergState = 0;
      robot.GetRobotEmergencyStopState(&emergState);
      printf("GetRobotEmergencyStopState :%d\n", emergState);
      int comstate = 0;
      robot.GetSDKComState(&comstate);
      printf("GetSDKComState :%d\n", comstate);
      uint8_t si0_state, si1_state;
      robot.GetSafetyStopState(&si0_state, &si1_state);
      printf("GetSafetyStopState :%d %d\n", si0_state, si1_state);
      double temp[6] = { 0.0 };
      robot.GetJointDriverTemperature(temp);
      printf("Temperature:%f,%f,%f,%f,%f,%f\n", temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]);
      double torque[6] = { 0.0 };
      robot.GetJointDriverTorque(torque);
      printf("torque:%f,%f,%f,%f,%f,%f\n", torque[0], torque[1], torque[2], torque[3], torque[4], torque[5]);
      robot.GetRobotRealTimeState(&pkg);
      robot.CloseRPC();
      return 0;
    }

逆運動學求解
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] config 關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */
    errno_t  GetInverseKin(int type, DescPose *desc_pos, int config, JointPos *joint_pos);

逆運動學求解(參考位置)
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置求解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */   
    errno_t  GetInverseKinRef(int type, DescPose *desc_pos, JointPos *joint_pos_ref, JointPos *joint_pos);

獲取逆運動學是否有解
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判斷是否有解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] result 0-無解，1-有解
    * @return  錯誤碼
    */   
    errno_t  GetInverseKinHasSolution(int type, DescPose *desc_pos, JointPos *joint_pos_ref, uint8_t *result);

正運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  正運動學求解
    * @param  [in] joint_pos 關節位置
    * @param  [out] desc_pos 笛卡爾位姿
    * @return  錯誤碼
    */
    errno_t  GetForwardKin(JointPos *joint_pos, DescPose *desc_pos);

機器人正逆運動學計算代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestInverseKin(void)
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
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      JointPos inverseRtn = {};
      robot.GetInverseKin(0, &desc_pos1, -1, &inverseRtn);
      printf("dcs1 GetInverseKin rtn is %f %f %f %f %f %f \n", inverseRtn.jPos[0], inverseRtn.jPos[1], inverseRtn.jPos[2], inverseRtn.jPos[3], inverseRtn.jPos[4], inverseRtn.jPos[5]);
      robot.GetInverseKinRef(0, &desc_pos1, &j1, &inverseRtn);
      printf("dcs1 GetInverseKinRef rtn is %f %f %f %f %f %f \n", inverseRtn.jPos[0], inverseRtn.jPos[1], inverseRtn.jPos[2], inverseRtn.jPos[3], inverseRtn.jPos[4], inverseRtn.jPos[5]);
      uint8_t hasResut = 0;
      robot.GetInverseKinHasSolution(0, &desc_pos1, &j1, &hasResut);
      printf("dcs1 GetInverseKinRef result %d\n", hasResut);
      DescPose forwordResult = {};
      robot.GetForwardKin(&j1, &forwordResult);
      printf("jpos1 forwordResult rtn is %f %f %f %f %f %f \n", forwordResult.tran.x, forwordResult.tran.y, forwordResult.tran.z, forwordResult.rpy.rx, forwordResult.rpy.ry, forwordResult.rpy.rz);
      robot.CloseRPC();
      return 0;
    }

查詢機器人示教管理點位數據
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查詢機器人示教管理點位數據
     * @param  [in]  name  點位名
     * @param  [out]  data   點位數據
     * @return  錯誤碼
     */ 
    errno_t  GetRobotTeachingPoint(char name[64], float data[20]);

獲取機器人DH參數補償值
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人DH參數補償值
    * @param [out] dhCompensation 機器人DH參數補償值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 錯誤碼
    */
    errno_t GetDHCompensation(double dhCompensation[6]);

獲取控制箱SN碼
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱SN碼
    * @param [out] SNCode 控制箱SN碼
    * @return 錯誤碼
    */
    errno_t GetRobotSN(std::string& SNCode);

查詢機器人示教管理點位數據代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestGetTeachPoint(void)
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
      char name[64] = "P1";
      float data[20] = { 0 };
      rtn = robot.GetRobotTeachingPoint(name, data);
      printf(" %d name is: %s \n", rtn, name);
      for (int i = 0; i < 20; i++)
      {
        printf("data is: %f \n", data[i]);
      }
      int que_len = 0;
      rtn = robot.GetMotionQueueLength(&que_len);
      printf("GetMotionQueueLength rtn is: %d, queue length is: %d \n", rtn, que_len);
      double dh[6] = { 0 };
      int retval = 0;
      retval = robot.GetDHCompensation(dh);
      cout << "retval is: " << retval << endl;
      cout << "dh is: " << dh[0] << " " << dh[1] << " " << dh[2] << " " << dh[3] << " " << dh[4] << " " << dh[5] << endl;
      string SN = "";
      robot.GetRobotSN(SN);
      cout << "robot SN is " << SN << endl;
      robot.CloseRPC();
      return 0;
    }
