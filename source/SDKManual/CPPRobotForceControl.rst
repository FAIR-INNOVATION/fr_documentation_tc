機器人力控
============

.. toctree:: 
    :maxdepth: 5

力傳感器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
	 * @brief  配置力傳感器
	 * @param  [in] company  力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI傳感器，21-中科米點，22-偉航敏芯，23-NBIT，24-鑫精誠(XJC)，26-NSR
	 * @param  [in] device  設備號，坤維(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精誠XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)
	 * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
	 * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
	 * @return  錯誤碼
	 */
    errno_t FT_SetConfig(int company, int device, int softvesion, int bus);

獲取力傳感器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取力傳感器配置
    * @param  [in] company  力傳感器廠商，待定
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    errno_t  FT_GetConfig(int *company, int *device, int *softvesion, int *bus);

力傳感器激活
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力傳感器激活
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    errno_t  FT_Activate(uint8_t act);

力傳感器校零
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力傳感器校零
    * @param  [in] act  0-去除零點，1-零點矯正
    * @return  錯誤碼
    */
    errno_t  FT_SetZero(uint8_t act);   

設置力傳感器參考座標系
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設置力傳感器參考座標系
    * @param  [in] ref  0-工具座標系，1-基座標系
    * @return  錯誤碼
    */
    errno_t  FT_SetRCS(uint8_t ref); 

設置力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設置力傳感器下負載重量
     * @param [in] weight 負載重量 kg
     * @return 錯誤碼
     */
    errno_t SetForceSensorPayload(double weight);

設置力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設置力傳感器下負載質心
     * @param [in] x 負載質心x mm
     * @param [in] y 負載質心y mm
     * @param [in] z 負載質心z mm
     * @return 錯誤碼
     */
    errno_t SetForceSensorPayloadCog(double x, double y, double z);

獲取力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
     * @brief 獲取力傳感器下負載重量
     * @param [in] weight 負載重量 kg
     * @return 錯誤碼
     */
    errno_t GetForceSensorPayload(double& weight);

獲取力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 獲取力傳感器下負載質心
     * @param [out] x 負載質心x mm
     * @param [out] y 負載質心y mm
     * @param [out] z 負載質心z mm
     * @return 錯誤碼
     */
    errno_t GetForceSensorPayloadCog(double& x, double& y, double& z);

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 力傳感器自動校零
     * @param [out] weight 傳感器質量 kg
     * @param [out] pos 傳感器質心 mm
     * @return 錯誤碼
     */
    errno_t ForceSensorAutoComputeLoad(double& weight, DescTran& pos);

獲取參考座標系下力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取參考座標系下力/扭矩數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    errno_t  FT_GetForceTorqueRCS(ForceTorque *ft); 

獲取力傳感器原始力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取力傳感器原始力/扭矩數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    errno_t  FT_GetForceTorqueOrigin(ForceTorque *ft); 

力傳感器配置及自動校零代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTInit(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      robot.FT_GetForceTorqueOrigin(0, &ft);
      printf("ft origin:%f,%f,%f,%f,%f,%f\n", ft.fx, ft.fy, ft.fz, ft.tx, ft.ty, ft.tz);
      robot.FT_SetZero(1);
      robot.Sleep(1000);
      DescPose ftCoord = {};
      robot.FT_SetRCS(0, ftCoord);
      robot.SetForceSensorPayload(0.824);
      robot.SetForceSensorPayloadCog(0.778, 2.554, 48.765);
      double weight = 0;
      double x = 0, y = 0, z = 0;
      robot.GetForceSensorPayload(weight);
      robot.GetForceSensorPayloadCog(x, y, z);
      printf("the FT load is %lf, %lf %lf %lf\n", weight, x, y, z);
      robot.SetForceSensorPayload(0);
      robot.SetForceSensorPayloadCog(0, 0, 0);
      double computeWeight = 0;
      DescTran tran = {};
      robot.ForceSensorAutoComputeLoad(weight, tran);
      cout << "the result is weight " << weight << " pos is " << tran.x << " " << tran.y << " " << tran.z << endl;
      robot.CloseRPC();
      return 0;
    }


負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
    * @return  錯誤碼
    */
    errno_t  FT_PdIdenRecord(int id);   

負載重量辨識計算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載重量辨識計算
    * @param  [out] weight  負載重量，單位kg
    * @return  錯誤碼
    */   
    errno_t  FT_PdIdenCompute(float *weight);

負載質心辨識記錄
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載質心辨識記錄
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
    * @param  [in] index 點編號，範圍[1~3]
    * @return  錯誤碼
    */
    errno_t  FT_PdCogIdenRecord(int id, int index);    

負載質心辨識計算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載質心辨識計算
    * @param  [out] cog  負載質心，單位mm
    * @return  錯誤碼
    */   
    errno_t  FT_PdCogIdenCompute(DescTran *cog); 

力傳感器負載辨識代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTLoadCompute(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      robot.FT_GetForceTorqueOrigin(0, &ft);
      printf("ft origin:%f,%f,%f,%f,%f,%f\n", ft.fx, ft.fy, ft.fz, ft.tx, ft.ty, ft.tz);
      robot.FT_SetZero(1);
      robot.Sleep(1000);
      DescPose tcoord = {};
      tcoord.tran.z = 35.0;
      robot.SetToolCoord(10, &tcoord, 1, 0, 0, 0);
      robot.FT_PdIdenRecord(10);
      robot.Sleep(1000);
      float weight = 0.0;
      robot.FT_PdIdenCompute(&weight);
      printf("payload weight:%f\n", weight);
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_p3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      robot.MoveCart(&desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 1);
      robot.MoveCart(&desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 2);
      robot.MoveCart(&desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.Sleep(1000);
      robot.FT_PdCogIdenRecord(10, 3);
      robot.Sleep(1000);
      DescTran cog;
      memset(&cog, 0, sizeof(DescTran));
      robot.FT_PdCogIdenCompute(&cog);
      printf("cog:%f,%f,%f\n", cog.x, cog.y, cog.z);
      robot.CloseRPC();
      return 0;
    }

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  碰撞守護
    * @param  [in] flag 0-關閉碰撞守護，1-開啓碰撞守護
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否檢測碰撞，0-不檢測，1-檢測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大閾值
    * @param  [in] min_threshold 最小閾值
    * @note   力/扭矩檢測範圍：(ft-min_threshold, ft+max_threshold)
    * @return  錯誤碼
    */   
    errno_t  FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]); 

碰撞守護代碼示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTGuard(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t sensor_id = 1;
      uint8_t select[6] = { 1,1,1,1,1,1 };
      float max_threshold[6] = { 10.0,10.0,10.0,10.0,10.0,10.0 };
      float min_threshold[6] = { 5.0,5.0,5.0,5.0,5.0,5.0 };
      ForceTorque ft;
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      DescPose desc_p3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
      robot.FT_Guard(1, sensor_id, select, &ft, max_threshold, min_threshold);
      robot.MoveCart(&desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.MoveCart(&desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.MoveCart(&desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.FT_Guard(0, sensor_id, select, &ft, max_threshold, min_threshold);
      robot.CloseRPC();
      return 0;
    }

恆力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 恆力控制
    * @param [in] flag 0-關閉恆力控制，1-開啓恆力控制
    * @param [in] sensor_id 力傳感器編號
    * @param [in] select 選擇六個自由度是否檢測碰撞，0-不檢測，1-檢測
    * @param [in] ft 碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param [in] ft_pid 力pid參數，力矩pid參數
    * @param [in] adj_sign 自適應啓停控制，0-關閉，1-開啓
    * @param [in] ILC_sign ILC啓停控制， 0-停止，1-訓練，2-實操
    * @param [in] max_dis 最大調整距離，單位mm
    * @param [in] max_ang 最大調整角度，單位deg
    * @param [in] M rx、ry質量參數[0.1-10],預設2
    * @param [in] B rx、ry阻尼參數[0.1-50],預設8
    * @param [in] threshold rx、ry啟動閾值[0-10],預設0.2
    * @param [in] adjustCoeff rx、ry力矩調節係數[0-1],預設1
    * @param [in] polishRadio 打磨半徑，單位mm
    * @param [in] filter_Sign 濾波開啓標誌 0-關；1-開，默認關閉
    * @param [in] posAdapt_sign 姿態順應開啓標誌 0-關；1-開，默認關閉
    * @param [in] isNoBlock 阻塞標誌，0-阻塞；1-非阻塞
    * @return 錯誤碼
    */
    errno_t FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque* ft, float ft_pid[6], uint8_t adj_sign, 
    uint8_t ILC_sign, float max_dis, float max_ang, double M[2], double B[2], double threshold[2], double adjustCoeff[2], double polishRadio = 0.0, int filter_Sign = 0, int posAdapt_sign = 0, int isNoBlock = 0);

具有阻尼的恆力控制代碼示例
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTControlWithAdjustCoeff(void)
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
      uint8_t sensor_id = 10;
      uint8_t select[6] = { 0,0,1,0,0,0 };
      float ft_pid[6] = { 0.0008, 0.0, 0.0, 0.0, 0.0, 0.0 };
      uint8_t adj_sign = 0;
      uint8_t ILC_sign = 0;
      float max_dis = 1000.0;
      float max_ang = 20;
      ForceTorque ft = {0.0};
      ExaxisPos epos(0, 0, 0, 0);
      JointPos j1(80.765, -98.795, 106.548, -97.734, -89.999, 94.842);
      JointPos j2(43.067, -84.429, 92.620, -98.175, -90.011, 57.144);
      DescPose desc_p1(5.009, -547.463, 262.053, -179.999, -0.019, 75.923);
      DescPose desc_p2(-347.966, -547.463, 262.048, -180.000, -0.019, 75.923);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      double M[2] = { 2.0, 2.0 };
      double B[2] = { 15.0, 15.0 };
      double threshold[2] = {1.0, 1.0};
      double adjustCoeff[2] = {1.0, 0.8};
      double polishRadio = 0.0;
      int filter_Sign = 0;
      int posAdapt_sign = 1;
      int isNoBlock;
      ft.fz = -10.0;
      while(true)
      { 
        rtn = robot.FT_Control(1, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
        printf("FT_Control start rtn is %d\n", rtn);
        robot.MoveL(&j1, &desc_p1, 1, 0, 100, 100, 100, -1, 0, &epos, 0, 0, &offset_pos, 200.0, 0);
        robot.MoveL(&j2, &desc_p2, 1, 0, 100, 100, 100, -1, 0, &epos, 0, 0, &offset_pos, 200.0, 0);
        rtn = robot.FT_Control(0, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
        printf("FT_Control end rtn is %d\n", rtn);
      }
      robot.CloseRPC();
      return 0;
    }

螺旋線探索
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  螺旋線探索
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基座標系
    * @param  [in] dr 每圈半徑進給量
    * @param  [in] ft 力/扭矩閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] max_t_ms 最大探索時間，單位ms
    * @param  [in] max_vel 最大線速度，單位mm/s
    * @return  錯誤碼
    */   
    errno_t  FT_SpiralSearch(int rcs, float dr, float ft, float max_t_ms, float max_vel);  

旋轉插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  旋轉插入
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基座標系
    * @param  [in] angVelRot 旋轉角速度，單位deg/s
    * @param  [in] ft  力/扭矩閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] max_angle 最大旋轉角度，單位deg
    * @param  [in] orn 力/扭矩方向，1-沿z軸方向，2-繞z軸方向
    * @param  [in] max_angAcc 最大旋轉加速度，單位deg/s^2，暫不使用，默認爲0
    * @param  [in] rotorn  旋轉方向，1-順時針，2-逆時針
    * @param [in] strategy 未偵測到力/力矩的處理策略，0-報錯；1-警告，繼續運動
    * @return  錯誤碼
    */   
    errno_t FT_RotInsertion(int rcs, float angVelRot, float ft, float max_angle, uint8_t orn, float max_angAcc, uint8_t rotorn, int strategy = 0);

力感測器旋轉插入程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMove(void)
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
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float oacc = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, oacc, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&j3, &desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &j4, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, oacc, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&j3, &desc_pos3, tool, user, vel, acc, &epos, &j1, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(&desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, -1, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, -1, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&desc_pos3, tool, user, vel, acc, &epos, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, blendR, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        robot.CloseRPC();
        return 0;
    }

直線插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  直線插入
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基座標系
    * @param  [in] ft  力/扭矩閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] lin_v 直線速度，單位mm/s
    * @param  [in] lin_a 直線加速度，單位mm/s^2，暫不使用
    * @param  [in] max_dis 最大插入距離，單位mm
    * @param  [in] linorn  插入方向，0-負方向，1-正方向
    * @return  錯誤碼
    */   
    errno_t  FT_LinInsertion(int rcs, float ft, float lin_v, float lin_a, float max_dis, uint8_t linorn);    

螺旋探索、直線插入等指令代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestFTSearch(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t status = 1; 
      int sensor_num = 1; 
      float gain[6] = { 0.0001,0.0,0.0,0.0,0.0,0.0 }; 
      uint8_t adj_sign = 0; 
      uint8_t ILC_sign = 0; 
      float max_dis = 100.0; 
      float max_ang = 5.0; 
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      int rcs = 0; 
      float dr = 0.7; 
      float fFinish = 1.0; 
      float t = 60000.0;
      float vmax = 3.0;
      float force_goal = 20.0; 
      float lin_v = 0.0;
      float lin_a = 0.0;
      float disMax = 100.0;
      uint8_t linorn = 1; 
      float angVelRot = 2.0; 
      float forceInsertion = 1.0; 
      int angleMax = 45; 
      uint8_t orn = 1;
      float angAccmax = 0.0; 
      uint8_t rotorn = 1; 
      uint8_t select1[6] = { 0,0,1,1,1,0 }; 
      ft.fz = -10.0;
      robot.FT_Control(status, sensor_num, select1, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_SpiralSearch(rcs, dr, fFinish, t, vmax);
      printf("FT_SpiralSearch rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select1, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select2[6] = { 1,1,1,0,0,0 }; 
      gain[0] = 0.00005;
      ft.fz = -30.0;
      status = 1;
      robot.FT_Control(status, sensor_num, select2, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn);
      printf("FT_LinInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select2, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select3[6] = { 0,0,1,1,1,0 }; 
      ft.fz = -10.0;
      gain[0] = 0.0001;
      status = 1;
      robot.FT_Control(status, sensor_num, select3, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn);
      printf("FT_RotInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select3, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      uint8_t select4[6] = { 1,1,1,0,0,0 }; 
      ft.fz = -30.0;
      status = 1;
      robot.FT_Control(status, sensor_num, select4, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn);
      printf("FT_LinInsertion rtn is %d\n", rtn);
      status = 0;
      robot.FT_Control(status, sensor_num, select4, &ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      robot.CloseRPC();
      return 0;
    }

表面定位
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  表面定位
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基座標系
    * @param  [in] dir  移動方向，1-正方向，2-負方向 
    * @param  [in] axis 移動軸，1-x軸，2-y軸，3-z軸
    * @param  [in] lin_v 探索直線速度，單位mm/s
    * @param  [in] lin_a 探索直線加速度，單位mm/s^2，暫不使用，默認爲0
    * @param  [in] max_dis 最大探索距離，單位mm
    * @param  [in] ft  動作終止力/扭矩閾值，fx,fy,fz,tx,ty,tz  
    * @return  錯誤碼
    */   
    errno_t  FT_FindSurface(int rcs, uint8_t dir, uint8_t axis, float lin_v, float lin_a, float max_dis, float ft);   

計算中間平面位置開始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  計算中間平面位置開始
    * @return  錯誤碼
    */   
    errno_t  FT_CalCenterStart();

計算中間平面位置結束
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  計算中間平面位置結束
    * @param  [out] pos 中間平面位姿
    * @return  錯誤碼
    */      
    errno_t  FT_CalCenterEnd(DescPose *pos);

表面定位代碼示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSurface(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      int rcs = 0;
      uint8_t dir = 1;
      uint8_t axis = 1;
      float lin_v = 3.0;
      float lin_a = 0.0;
      float maxdis = 50.0;
      float ft_goal = 2.0;
      DescPose desc_pos(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose xcenter(0, 0, 0, 0, 0, 0);
      DescPose ycenter(0, 0, 0, 0, 0, 0);
      ForceTorque ft;
      memset(&ft, 0, sizeof(ForceTorque));
      ft.fx = -2.0;
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.FT_CalCenterStart();
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.WaitMs(1000);
      dir = 2;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.FT_CalCenterEnd(&xcenter);
      printf("xcenter:%f,%f,%f,%f,%f,%f\n", xcenter.tran.x, xcenter.tran.y, xcenter.tran.z, xcenter.rpy.rx, xcenter.rpy.ry, xcenter.rpy.rz);
      robot.MoveCart(&xcenter, 9, 0, 60.0, 50.0, 50.0, -1.0, -1);
      robot.FT_CalCenterStart();
      dir = 1;
      axis = 2;
      lin_v = 6.0;
      maxdis = 150.0;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.MoveCart(&desc_pos, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
      robot.WaitMs(1000);
      dir = 2;
      robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
      robot.FT_CalCenterEnd(&ycenter);
      printf("ycenter:%f,%f,%f,%f,%f,%f\n", ycenter.tran.x, ycenter.tran.y, ycenter.tran.z, ycenter.rpy.rx, ycenter.rpy.ry, ycenter.rpy.rz);
      robot.MoveCart(&ycenter, 9, 0, 60.0, 50.0, 50.0, 0.0, -1);
      robot.CloseRPC();
      return 0;
    }

柔順控制開啓
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔順控制開啓
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啓力閾值，單位N
    * @return  錯誤碼
    */   
    errno_t  FT_ComplianceStart(float p, float force); 

柔順控制關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔順控制關閉
    * @return  錯誤碼
    */   
    errno_t  FT_ComplianceStop(); 

柔順控制代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestCompliance(void)
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
      int company = 24;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      int index = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      uint8_t flag = 1;
      int sensor_id = 1;
      uint8_t select[6] = { 1,1,1,0,0,0 };
      float ft_pid[6] = { 0.0005,0.0,0.0,0.0,0.0,0.0 };
      uint8_t adj_sign = 0;
      uint8_t ILC_sign = 0;
      float max_dis = 100.0;
      float max_ang = 0.0;
      ForceTorque ft;
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      memset(&ft, 0, sizeof(ForceTorque));
      JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
      DescPose desc_p1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose desc_p2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
      ft.fx = -10.0;
      ft.fy = -10.0;
      ft.fz = -10.0;
      robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      float p = 0.00005;
      float force = 30.0;
      rtn = robot.FT_ComplianceStart(p, force);
      printf("FT_ComplianceStart rtn is %d\n", rtn);
      int count = 15;
      while (count)
      {
        robot.MoveL(&j1, &desc_p1, 0, 0, 100.0, 180.0, 100.0, -1.0, &epos, 0, 1, &offset_pos);
        robot.MoveL(&j2, &desc_p2, 0, 0, 100.0, 180.0, 100.0, -1.0, &epos, 0, 0, &offset_pos);
        count -= 1;
      }
      robot.FT_ComplianceStop();
      printf("FT_ComplianceStop rtn is %d\n", rtn);
      flag = 0;
      robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
      robot.CloseRPC();
      return 0;
    }

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 負載辨識初始化
    * @return 錯誤碼
    */
    errno_t LoadIdentifyDynFilterInit();

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 負載辨識初始化
    * @return 錯誤碼
    */
    errno_t LoadIdentifyDynVarInit();

負載辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 負載辨識主程序
    * @param [in] joint_torque 關節扭矩
    * @param [in] joint_pos 關節位置
    * @param [in] t 採樣週期
    * @return 錯誤碼
    */
    errno_t LoadIdentifyMain(double joint_torque[6], double joint_pos[6], double t);

獲取負載辨識結果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取負載辨識結果
    * @param [in] gain 
    * @param [out] weight 負載重量
    * @param [out] cog 負載質心
    * @return 錯誤碼
    */
    errno_t LoadIdentifyGetResult(double gain[12], double *weight, DescTran *cog);

機器人負載辨識代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestIdentify(void)
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
      retval = robot.LoadIdentifyDynFilterInit();
      printf("LoadIdentifyDynFilterInit retval is: %d \n", retval);
      retval = robot.LoadIdentifyDynVarInit();
      printf("LoadIdentifyDynVarInit retval is: %d \n", retval);
      JointPos posJ = {};
      DescPose posDec = {};
      float joint_toq[6] = { 0.0 };
      robot.GetActualJointPosDegree(0, &posJ);
      posJ.jPos[1] = posJ.jPos[1] + 10;
      robot.GetJointTorques(0, joint_toq);
      joint_toq[1] = joint_toq[1] + 2;
      double tmpTorque[6] = { 0.0 };
      for (int i = 0; i < 6; i++)
      {
        tmpTorque[i] = joint_toq[i];
      }
      retval = robot.LoadIdentifyMain(tmpTorque, posJ.jPos, 1);
      printf("LoadIdentifyMain retval is: %d \n", retval);
      double gain[12] = { 0,0.05,0,0,0,0,0,0.02,0,0,0,0 };
      double weight = 0;
      DescTran load_pos;
      memset(&load_pos, 0, sizeof(DescTran));
      retval = robot.LoadIdentifyGetResult(gain, &weight, &load_pos);
      printf("LoadIdentifyGetResult retval is: %d ; weight is %f cog is %f %f %f \n", retval, weight, load_pos.x, load_pos.y, load_pos.z);
      robot.CloseRPC();
      return 0;
    }

力傳感器輔助拖動
+++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.0-3.8.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  力傳感器輔助拖動
    * @param  [in] status 控制狀態，0-關閉；1-開啓
    * @param  [in] asaptiveFlag 自適應開啓標誌，0-關閉；1-開啓
    * @param  [in] interfereDragFlag 干涉區拖動標誌，0-關閉；1-開啓
    * @param  [in] ingularityConstraintsFlag 奇異點策略，0-規避；1-穿越
    * @param  [in] forceCollisionFlag 輔助拖動時機器人碰撞檢測標誌；0-關閉；1-開啓
    * @param  [in] M 慣性系數
    * @param  [in] B 阻尼係數
    * @param  [in] K 剛度係數
    * @param  [in] F 拖動六維力閾值
    * @param  [in] Fmax 最大拖動力限制
    * @param  [in] Vmax 最大關節速度限制
    * @return  錯誤碼
    */
    errno_t EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, int ingularityConstraintsFlag, int forceCollisionFlag, std::vector<double> M, std::vector<double> B, std::vector<double> K, std::vector<double> F, double Fmax, double Vmax);

獲取力傳感器拖動開關狀態
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 獲取力傳感器拖動開關狀態
     * @param [out] dragState 力傳感器輔助拖動控制狀態，0-關閉；1-開啓
     * @param [out] sixDimensionalDragState 六維力輔助拖動控制狀態，0-關閉；1-開啓
     * @return 錯誤碼
     */
    errno_t GetForceAndTorqueDragState(int& dragState, int& sixDimensionalDragState);

報錯清除後力傳感器自動開啓
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 報錯清除後力傳感器自動開啓
     * @param [in] status 控制狀態，0-關閉；1-開啓
     * @return 錯誤碼
     */
    errno_t SetForceSensorDragAutoFlag(int status);

力傳感器輔助拖動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestEndForceDragCtrl(void)
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
         robot.SetForceSensorDragAutoFlag(1);
         vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
         vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
         vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
         vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
         robot.EndForceDragControl(1, 0, 0, 0, 1, M, B, K, F, 50, 100);
         robot.Sleep(5000);
         int dragState = 0;
         int sixDimensionalDragState = 0;
         robot.GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
         printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);
         robot.EndForceDragControl(0, 0, 0, 0, 1, M, B, K, F, 50, 100);
         robot.CloseRPC();
         return 0;
     }

設置六維力和關節阻抗混合拖動開關及參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設置六維力和關節阻抗混合拖動開關及參數
     * @param [in] status 控制狀態，0-關閉；1-開啓
     * @param [in] impedanceFlag 阻抗開啓標誌，0-關閉；1-開啓
     * @param [in] lamdeDain 拖動增益
     * @param [in] KGain 剛度增益
     * @param [in] BGain 阻尼增益
     * @param [in] dragMaxTcpVel 拖動末端最大線速度限制
     * @param [in] dragMaxTcpOriVel 拖動末端最大角速度限制
     * @return 錯誤碼
     */
    errno_t ForceAndJointImpedanceStartStop(int status, int impedanceFlag, std::vector<double> lamdeDain, std::vector<double> KGain, std::vector<double> BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

六維力和關節阻抗混合拖動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestForceAndJointImpedance(void)
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
      robot.DragTeachSwitch(1);
      vector <double> lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
      vector <double> KGain = { 0, 0, 0, 0, 0, 0 };
      vector <double> BGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
      rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000, 180);
      printf("ForceAndJointImpedanceStartStop rtn is %d\n", rtn);
      robot.Sleep(5000);
      robot.DragTeachSwitch(0);
      rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000, 180);
      printf("ForceAndJointImpedanceStartStop rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

阻抗啟停控制
+++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 阻抗啟停控制
    * @param [in] status 0：關閉；1-開啟
    * @param [in] workSpace 0-關節空間；1-笛卡爾空間
    * @param [in] forceThreshold 觸發力閾值(N)
    * @param [in] m 質量參數
    * @param [in] b 阻尼參數
    * @param [in] k 剛度參數
    * @param [in] maxV 最大線速度(mm/s)
    * @param [in] maxVA 最大線加速度(mm/s2)
    * @param [in] maxW 最大角速度(°/s)
    * @param [in] maxWA 最大角加速度(°/s2)
    * @return 錯誤碼
    */
    errno_t ImpedanceControlStartStop(int status, int workSpace, double forceThreshold[6], double m[6], double b[6], double k[6], double maxV, double maxVA, double maxW, double maxWA);

機器人阻抗啟停控制程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    int TestImpedanceControl()
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
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      JointPos j1(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
      JointPos j2(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
      DescPose desc_pos1(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
      DescPose desc_pos2(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
      DescPose offset_pos(0, 0, 0, 0, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 200.0;
      float ovl = 100.0;
      float blendT = -1.0;
      float blendR = -1.0;
      uint8_t flag = 0;
      uint8_t search = 0;
      robot.SetSpeed(20);
      int company = 17;
      int device = 0;
      int softversion = 0;
      int bus = 1;
      robot.FT_SetConfig(company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_GetConfig(&company, &device, &softversion, &bus);
      printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
      robot.Sleep(1000);
      robot.FT_Activate(0);
      robot.Sleep(1000);
      robot.FT_Activate(1);
      robot.Sleep(1000);
      robot.Sleep(1000);
      robot.FT_SetZero(0);
      robot.Sleep(1000);
      robot.FT_SetZero(1);
      robot.Sleep(1000);
      double forceThreshold[6] = { 30,30,30,5,5,5 };
      double m[6] = { 0.1,0.1,0.1,0.02,0.02,0.02 };
      double b[6] = { 1,1,1,0.08,0.08,0.08 };
      double k[6] = { 0,0,0,0,0,0 };
      rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
      printf("ImpedanceControlStartStop errcode:%d\n", rtn);
      rtn = robot.MoveL(&desc_pos1, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos1, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, 0, &epos, search, flag, &offset_pos, -1, 1);
      printf("movel errcode:%d\n", rtn);
      robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);    
      robot.CloseRPC();
      return 0;
    }

開啟力矩補償功能及補償係數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @brief 開啟力矩補償功能及補償係數
    * @param [in] status 開關，0-關閉；1-開啟
    * @param [in] torqueCoeff J1-J6力矩補償係數[0-1]
    * @return 錯誤碼
    */
    errno_t SerCoderCompenParams(int status, double torqueCoeff[6]);