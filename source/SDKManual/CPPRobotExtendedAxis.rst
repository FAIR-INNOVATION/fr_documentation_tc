擴展軸
=============

.. toctree:: 
    :maxdepth: 5

設置485擴展軸參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [in] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驅動器軟件版本，1-V1.0
    * @param [in] servoResolution 編碼器分辨率
    * @param [in] axisMechTransRatio 機械傳動比
    * @return 錯誤碼
    */
    errno_t AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

獲取485擴展軸配置參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取485擴展軸配置參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [out] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驅動器軟件版本，1-V1.0
    * @param [out] servoResolution 編碼器分辨率
    * @param [out] axisMechTransRatio 機械傳動比
    * @return 錯誤碼
    */
    errno_t AuxServoGetParam(int servoId, int* servoCompany, int* servoModel, int* servoSoftVersion, int* servoResolution, double* axisMechTransRatio);
    
設置485擴展軸使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸使能/去使能
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] status 使能狀態，0-去使能， 1-使能
    * @return 錯誤碼
    */
    errno_t AuxServoEnable(int servoId, int status);

設置485擴展軸控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸控制模式
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 錯誤碼
    */
    errno_t AuxServoSetControlMode(int servoId, int mode);

設置485擴展軸目標位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸目標位置(位置模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] pos 目標位置，mm或°
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetPos(int servoId, double pos, double speed);

設置485擴展軸目標轉矩(力矩模式) - 暫未開放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸目標轉矩(力矩模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] torque 目標力矩，Nm
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetTorque(int servoId, double torque);

設置485擴展軸回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸回零
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 回零模式，0-當前位置回零；1-限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);
    
清除485擴展軸錯誤信息
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 清除485擴展軸錯誤信息
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼
    */
    errno_t AuxServoClearError(int servoId);

獲取485擴展軸伺服狀態
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取485擴展軸伺服狀態
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoErrCode 伺服驅動器故障碼
    * @param [out] servoState 伺服驅動器狀態[十進制數轉為二進制，bit0-bit5：伺服使能-伺服運行-正限位觸發-負限位觸發-定位完成-回零完成]
    * @param [out] servoPos 伺服當前位置 mm或°
    * @param [out] servoSpeed 伺服當前速度 mm/s或°/s
    * @param [out] servoTorque 伺服當前轉矩Nm
    * @return 錯誤碼
    */
    errno_t AuxServoGetStatus(int servoId, int* servoErrCode, int* servoState, double* servoPos, double* servoSpeed, double* servoTorque);

設置485擴展軸目標速度(速度模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸目標速度(速度模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetSpeed(int servoId, double speed);
    
設置狀態反饋中485擴展軸數據軸號
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置狀態反饋中485擴展軸數據軸號
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼
    */
    errno_t AuxServosetStatusID(int servoId);

設置485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸運動加減速度
    * @param [in] acc 485擴展軸運動加速度
    * @param [in] dec 485擴展軸運動減速度
    * @return 錯誤碼
    */
    errno_t AuxServoSetAcc(double acc, double dec);

設置485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置485擴展軸急停加減速度
    * @param [in] acc 485擴展軸急停加速度
    * @param [in] dec 485擴展軸急停減速度
    * @return 錯誤碼
    */
    errno_t AuxServoSetEmergencyStopAcc(double acc, double dec);

獲取485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取485擴展軸運動加減速度
    * @param [out] acc 485擴展軸運動加速度
    * @param [out] dec 485擴展軸運動減速度
    * @return 錯誤碼
    */
    errno_t AuxServoGetAcc(double& acc, double& dec);

獲取485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取485擴展軸急停加減速度
    * @param [out] acc 485擴展軸急停加速度
    * @param [out] dec 485擴展軸急停減速度
    * @return 錯誤碼
    */
    errno_t AuxServoGetEmergencyStopAcc(double& acc, double& dec);

擴展軸控制代碼示例
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
        
    int Test485Auxservo(void)
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
      int retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      int servoCompany;
      int servoModel;
      int servoSoftVersion;
      int servoResolution;
      double axisMechTransRatio;
      retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
      std::cout << "servoCompany " << servoCompany << "\n"
        << "servoModel " << servoModel << "\n"
        << "servoSoftVersion " << servoSoftVersion << "\n"
        << "servoResolution " << servoResolution << "\n"
        << "axisMechTransRatio " << axisMechTransRatio << "\n"
        << std::endl;
      retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
      std::cout << "servoCompany " << servoCompany << "\n"
        << "servoModel " << servoModel << "\n"
        << "servoSoftVersion " << servoSoftVersion << "\n"
        << "servoResolution " << servoResolution << "\n"
        << "axisMechTransRatio " << axisMechTransRatio << "\n"
        << std::endl;
      retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      robot.Sleep(3000);
      robot.AuxServoSetAcc(3000, 3000);
      robot.AuxServoSetEmergencyStopAcc(5000, 5000);
      robot.Sleep(1000);
      double emagacc = 0, acc = 0;
      double emagdec = 0, dec = 0;
      robot.AuxServoGetEmergencyStopAcc(emagacc, emagdec);
      printf("emergency acc is %f dec is %f \n", emagacc, emagdec);
      robot.AuxServoGetAcc(acc, dec);
      printf("acc is %f dec is %f \n", acc, dec);
      robot.AuxServoSetControlMode(1, 0);
      robot.Sleep(2000);
      retval = robot.AuxServoEnable(1, 0);
      std::cout << "AuxServoEnable disenable " << retval << std::endl;
      robot.Sleep(1000);
      int servoerrcode = 0;
      int servoErrCode;
      int servoState;
      double servoPos;
      double servoSpeed;
      double servoTorque;
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoState " << servoState << std::endl;
      robot.Sleep(1000);;
      retval = robot.AuxServoEnable(1, 1);
      std::cout << "AuxServoEnable enable " << retval << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoState " << servoState << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoHoming(1, 1, 5, 1);
      std::cout << "AuxServoHoming " << retval << std::endl;
      robot.Sleep(3000);
      retval = robot.AuxServoSetTargetPos(1, 200, 30);
      std::cout << "AuxServoSetTargetPos " << retval << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoSpeed " << servoSpeed << std::endl;
      robot.Sleep(8000);
      robot.AuxServoSetControlMode(1, 1);
      robot.Sleep(2000);
      robot.AuxServoEnable(1, 0);
      robot.Sleep(1000);
      robot.AuxServoEnable(1, 1);
      robot.Sleep(1000);
      robot.AuxServoSetTargetSpeed(1, 100, 80);
      robot.Sleep(5000);
      robot.AuxServoSetTargetSpeed(1, 0, 80);
      robot.CloseRPC();
      return 0;
    }

UDP擴展軸通訊參數配置
++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸通訊參數配置
    * @param [in] ip PLC IP地址
    * @param [in] port  端口號
    * @param [in] period    通訊週期(ms，默認為2，請勿修改此參數)
    * @param [in] lossPkgTime   丟包檢測時間(ms)
    * @param [in] lossPkgNum    丟包次數
    * @param [in] disconnectTime    通訊斷開確認時長
    * @param [in] reconnectEnable   通訊斷開自動重連使能 0-不使能 1-使能
    * @param [in] reconnectPeriod   重連週期間隔(ms)
    * @param [in] reconnectNum  重連次數
    * @param [in] selfConnect 斷電重啟是否自動建立連接；0-不建立連接；1-建立連接
    * @return 錯誤碼
    */
    errno_t ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum, int selfConnect = 1);
        
獲取UDP擴展軸通訊參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取UDP擴展軸通訊參數
    * @param [out] ip PLC IP地址
    * @param [out] port 端口號
    * @param [out] period 通訊週期(ms，默認為2，請勿修改此參數)
    * @param [out] lossPkgTime 丟包檢測時間(ms)
    * @param [out] lossPkgNum 丟包次數
    * @param [out] disconnectTime 通訊斷開確認時長
    * @param [out] reconnectEnable 通訊斷開自動重連使能 0-不使能 1-使能
    * @param [out] reconnectPeriod 重連週期間隔(ms)
    * @param [out] reconnectNum 重連次數
    * @param [out] selfStart 重啟控制箱後是否自動重連；0-不重連；1-重連
    * @return 錯誤碼
    */
    errno_t ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum, int& selfConnect);
        
加載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 加載UDP通信
    * @return 錯誤碼
    */
    errno_t ExtDevLoadUDPDriver();

卸載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 卸載UDP通信
    * @return 錯誤碼
    */
    errno_t ExtDevUnloadUDPDriver();

UDP擴展軸通信異常斷開後恢復連接
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸通信異常斷開後恢復連接
    * @return 錯誤碼
    */
    errno_t ExtDevUDPClientComReset();

UDP擴展軸通信異常斷開後關閉通訊
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸通信異常斷開後關閉通訊
    * @return 錯誤碼
    */
    errno_t ExtDevUDPClientComClose();

UDP擴展軸參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸參數配置
    * @param [in] axisID 軸號
    * @param [in] axisType 擴展軸類型 0-平移；1-旋轉
    * @param [in] axisDirection 擴展軸方向 0-正向；1-反向 
    * @param [in] axisMax 擴展軸最大位置 mm
    * @param [in] axisMin 擴展軸最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 導程mm
    * @param [in] encResolution 編碼器分辨率
    * @param [in] axisOffect 焊縫起始點擴展軸偏移量
    * @param [in] axisCompany 驅動器廠家 1-禾川；2-匯川；3-松下
    * @param [in] axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 編碼器類型  0-增量；1-絕對值
    * @return 錯誤碼
    */
    errno_t ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

UDP擴展軸參數獲取
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸參數獲取
    * @param [in] axisID 擴展軸號[1-4]
    * @param [out] axisType 擴展軸類型 0-平移；1-旋轉
    * @param [out] axisDirection 擴展軸方向 0-正向；1-反向
    * @param [out] axisMax 擴展軸最大位置 mm
    * @param [out] axisMin 擴展軸最小位置 mm
    * @param [out] axisVel 速度mm/s
    * @param [out] axisAcc 加速度mm/s2
    * @param [out] axisLead 導程mm
    * @param [out] encResolution 編碼器解析度
    * @param [out] axisOffect 焊縫起始點擴展軸偏移量
    * @param [out] axisCompany 驅動器廠家 1-禾川；2-匯川；3-松下
    * @param [out] axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [out] axisEncType 編碼器類型  0-增量；1-絕對值
    * @return 錯誤碼
    */
    errno_t ExtAxisGetParamConfig(int axisID, int& axisType, int& axisDirection, double& axisMax, double& axisMin, double& axisVel, double& axisAcc, double& axisLead, int& encResolution, double& axisOffect, int& axisCompany, int& axisModel, int& axisEncType);

設置擴展軸安裝位置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展軸安裝位置
    * @param [in] installType 0-機器人安裝在外部軸上，1-機器人安裝在外部軸外
    * @return 錯誤碼
    */
    errno_t SetRobotPosToAxis(int installType);

設置擴展軸系統DH參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展軸系統DH參數配置
    * @param [in] axisConfig 外部軸構型，0-單自由度直線滑軌，1-兩自由度L型變位機，2-三自由度，3-四自由度，4-單自由度變位機
    * @param [in] axisDHd1 外部軸DH參數d1 mm
    * @param [in] axisDHd2 外部軸DH參數d2 mm
    * @param [in] axisDHd3 外部軸DH參數d3 mm
    * @param [in] axisDHd4 外部軸DH參數d4 mm
    * @param [in] axisDHa1 外部軸DH參數a1 mm
    * @param [in] axisDHa2 外部軸DH參數a2 mm
    * @param [in] axisDHa3 外部軸DH參數a3 mm
    * @param [in] axisDHa4 外部軸DH參數a4 mm
    * @return 錯誤碼
    */
    errno_t SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

UDP擴展軸使能
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸使能
    * @param [in] axisID 軸號[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 錯誤碼
    */
    errno_t ExtAxisServoOn(int axisID, int status);

UDP擴展軸回零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸回零
    * @param [in] axisID 軸號[1-4]
    * @param [in] mode 回零方式 0-當前位置回零，1-負限位回零，2-正限位回零
    * @param [in] searchVel 尋零速度(mm/s)
    * @param [in] latchVel 尋零箍位速度(mm/s)
    * @return 錯誤碼
    */
    errno_t ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP擴展軸點動開始
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸點動開始
    * @param [in] axisID 軸號[1-4]
    * @param [in] direction 轉動方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc 加速度 (mm/s2)
    * @param [in] maxDistance 最大點動距離
    * @return 錯誤碼
    */
    errno_t ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP擴展軸點動停止
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸點動停止
    * @param [in] axisID 軸號[1-4]
    * @return 錯誤碼
    */
    errno_t ExtAxisStopJog(int axisID);

UDP擴展軸配置與點動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxis(void)
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
        rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
        cout << "ExtDevSetUDPComParam rtn is " << rtn << endl;
        string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0; int selfConnect = 0;
        rtn = robot.ExtDevGetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum, selfConnect);
        string patam = "\nip " + ip + "\nport " + to_string(port) + "\nperiod  " + to_string(period) + "\nlossPkgTime " + to_string(lossPkgTime) + "\nlossPkgNum  " + to_string(lossPkgNum) + "\ndisConntime  " +
            to_string(disconnectTime) + "\nreconnecable  " + to_string(reconnectEnable) + "\nreconnperiod  " + to_string(reconnectPeriod) + "\nreconnnun  " + to_string(reconnectNum) + "\nselfConnect  " + to_string(selfConnect);
        cout << "ExtDevGetUDPComParam rtn is " << rtn << patam << endl;
        robot.ExtDevLoadUDPDriver();
        rtn = robot.SetExAxisCmdDoneTime(5000.0);
        cout << "SetExAxisCmdDoneTime rtn is " << rtn << endl;
        rtn = robot.ExtAxisServoOn(1, 1);
        cout << "ExtAxisServoOn axis id 1 rtn is " << rtn << endl;
        rtn = robot.ExtAxisServoOn(2, 1);
        cout << "ExtAxisServoOn axis id 2 rtn is " << rtn << endl;
        robot.Sleep(2000);
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.Sleep(2000);
        rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
        cout << "ExtAxisSetHoming rtnn is  " << rtn << endl;
        robot.Sleep(4000);
        rtn = robot.SetRobotPosToAxis(1);
        cout << "SetRobotPosToAxis rtn is " << rtn << endl;
        rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
        cout << "SetAxisDHParaConfig rtn is " << rtn << endl;
        int axisType = -1;
        int axisDirection = -1;
        double axisMax = -1;
        double axisMin = -1;
        double axisVel = -1;
        double axisAcc = -1;
        double axisLead = -1;
        int encResolution = -1;
        double axisOffect = -1;
        int axisCompany = -1;
        int axisModel = -1;
        int axisEncType = -1;
        rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
        cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
        rtn = robot.ExtAxisGetParamConfig(1, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType);
        printf("axis id 1 ExtAxisGetParamConfig : axisType %d, axisDirection %d, axisMax %lf, axisMin %lf, axisVel %lf, axisAcc %lf, axisLead%lf, encResolution %d, axisOffect %f, axisCompany %d, axisModel %d, axisEncType %d\n",
            axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType);
            rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);
        cout << "ExtAxisParamConfig axis 2 rtn is " << rtn << endl;
        rtn = robot.ExtAxisGetParamConfig(2, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType);
        printf("axis id 2 ExtAxisGetParamConfig : axisType %d, axisDirection %d, axisMax %lf, axisMin %lf, axisVel %lf, axisAcc %lf, axisLead%lf, encResolution %d, axisOffect %f, axisCompany %d, axisModel %d, axisEncType %d\n",
            axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc, axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType);
        robot.Sleep(1000 * 3);
        robot.ExtAxisStartJog(1, 0, 10, 10, 30);
        robot.Sleep(1000 * 1);
        robot.ExtAxisStopJog(1);
        robot.Sleep(1000 * 3);
        robot.ExtAxisServoOn(1, 0);
        robot.Sleep(1000 * 3);
        robot.ExtAxisStartJog(2, 0, 10, 10, 30);
        robot.Sleep(1000 * 1);
        robot.ExtAxisStopJog(2);
        robot.Sleep(1000 * 3);
        robot.ExtAxisServoOn(2, 0);
        robot.Sleep(1000 * 1);
        robot.ExtDevUnloadUDPDriver();
        robot.CloseRPC();
        return 0;
    }

設置擴展軸坐標系參考點-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展軸坐標系參考點-四點法
    * @param [in] pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    errno_t ExtAxisSetRefPoint(int pointNum);

計算擴展軸坐標系-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 計算擴展軸坐標系-四點法
    * @param [out] coord 坐標系值
    * @return 錯誤碼
    */
    errno_t ExtAxisComputeECoordSys(DescPose& coord);

變位機坐標系參考點設置
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 變位機坐標系參考點設置
    * @param [in] pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    errno_t PositionorSetRefPoint(int pointNum);

變位機坐標系計算-四點法
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 變位機坐標系計算-四點法
    * @param [out] coord 坐標系值
    * @return 錯誤碼
    */
    errno_t PositionorComputeECoordSys(DescPose& coord);

設置標定參考點在變位機末端坐標系下位姿
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置標定參考點在變位機末端坐標系下位姿
    * @param [in] pos 位姿值
    * @return 錯誤碼
    */
    errno_t SetRefPointInExAxisEnd(DescPose pos);

應用擴展軸坐標系
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 應用擴展軸坐標系
    * @param [in] applyAxisId 擴展軸編號 bit0-bit3對應擴展軸編號1-4，如應用擴展軸1和3，則是 0b 0000 0101；也就是5
    * @param [in] axisCoordNum 擴展軸坐標系編號
    * @param [in] coord 坐標系值
    * @param [in] calibFlag 標定標誌 0-否，1-是
    * @return 錯誤碼
    */
    errno_t ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

獲取擴展軸坐標系
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取擴展軸坐標系
    * @param [out] coord 擴展軸坐標系
    * @return 錯誤碼
    */
    errno_t ExtAxisGetCoord(DescPose& coord);

擴展軸坐標系標定代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxisCalib(void)
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
       rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
       cout << "ExtDevSetUDPComParam rtn is " << rtn << endl;
       string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
       rtn = robot.ExtDevGetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum);
       string patam = "\nip " + ip + "\nport " + to_string(port) + "\nperiod " + to_string(period) + "\nlossPkgTime " + to_string(lossPkgTime) + "\nlossPkgNum " + to_string(lossPkgNum) + "\ndisConntime " + to_string(disconnectTime) + "\nreconnecable " + to_string(reconnectEnable) + "\nreconnperiod " + to_string(reconnectPeriod) + "\nreconnnun " + to_string(reconnectNum);
       cout << "ExtDevGetUDPComParam rtn is " << rtn << patam << endl;
       robot.ExtDevLoadUDPDriver();
       rtn = robot.ExtAxisServoOn(1, 1);
       cout << "ExtAxisServoOn axis id 1 rtn is " << rtn << endl;
       rtn = robot.ExtAxisServoOn(2, 1);
       cout << "ExtAxisServoOn axis id 2 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.ExtAxisSetHoming(1, 0, 10, 2);
       robot.Sleep(2000);
       rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
       cout << "ExtAxisSetHoming rtnn is " << rtn << endl;
       robot.Sleep(4000);
       rtn = robot.SetRobotPosToAxis(1);
       cout << "SetRobotPosToAxis rtn is " << rtn << endl;
       rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0);
       cout << "SetAxisDHParaConfig rtn is " << rtn << endl;
       rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
       cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
       rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);
       cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
       DescPose toolCoord(0, 0, 210, 0, 0, 0);
       robot.SetToolCoord(1, &toolCoord, 0, 0, 1, 0);
       JointPos jSafe(115.193, -96.149, 92.489, -87.068, -89.15, -83.488);
       JointPos j1(117.559, -92.624, 100.329, -96.909, -94.057, -83.488);
       JointPos j2(112.239, -90.096, 99.282, -95.909, -89.824, -83.488);
       JointPos j3(110.839, -83.473, 93.166, -89.22, -90.499, -83.487);
       JointPos j4(107.935, -83.572, 95.424, -92.873, -87.933, -83.488);
       DescPose descSafe = {};
       DescPose desc1 = {};
       DescPose desc2 = {};
       DescPose desc3 = {};
       DescPose desc4 = {};
       ExaxisPos exaxisPos = { 0, 0, 0, 0 };
       DescPose offdese = { 0, 0, 0, 0, 0, 0 };
       robot.GetForwardKin(&jSafe, &descSafe);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.Sleep(2000);
       robot.GetForwardKin(&j1, &desc1);
       robot.MoveJ(&j1, &desc1, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.Sleep(2000);
       DescPose actualTCPPos = {};
       robot.GetActualTCPPose(0, &actualTCPPos);
       robot.SetRefPointInExAxisEnd(actualTCPPos);
       rtn = robot.PositionorSetRefPoint(1);
       cout << "PositionorSetRefPoint 1 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j2, &desc2);
       rtn = robot.MoveJ(&j2, &desc2, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(2);
       cout << "PositionorSetRefPoint 2 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j3, &desc3);
       robot.MoveJ(&j3, &desc3, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(3);
       cout << "PositionorSetRefPoint 3 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j4, &desc4);
       robot.MoveJ(&j4, &desc4, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(4);
       cout << "PositionorSetRefPoint 4 rtn is " << rtn << endl;
       robot.Sleep(2000);
       DescPose axisCoord = {};
       robot.PositionorComputeECoordSys(axisCoord);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       printf("PositionorComputeECoordSys rtn is %f %f %f %f %f %f\n", axisCoord.tran.x, axisCoord.tran.y, axisCoord.tran.z, axisCoord.rpy.rx, axisCoord.rpy.ry, axisCoord.rpy.rz);
       rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1);
       cout << "ExtAxisActiveECoordSys rtn is " << rtn << endl;
    DescPose getCoord(0, 0, 0, 0, 0, 0);
    rtn = robot.ExtAxisGetCoord(getCoord);
    printf("ExtAxisGetCoord rtn is %f %f %f %f %f %f\n", getCoord.tran.x, getCoord.tran.y, getCoord.tran.z, getCoord.rpy.rx, getCoord.rpy.ry, getCoord.rpy.rz);
    robot.CloseRPC();
    return 0;
    }

UDP擴展軸運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸運動
    * @param [in] pos 目標位置
    * @param [in] ovl 速度百分比
    * @param [in] blend 平滑參數(mm或ms)；-1：等待運動完成
    * @return 錯誤碼
    */
    errno_t ExtAxisMove(ExaxisPos pos, double ovl, double blend = -1);

UDP擴展軸運動代碼示例
+++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxisCalib(void)
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
      ExaxisPos axisPos;
      axisPos.ePos[0] = 20;
      axisPos.ePos[1] = 0;
      axisPos.ePos[2] = 0;
      axisPos.ePos[3] = 0;
      robot.ExtAxisMove(axisPos, 50);
      robot.CloseRPC();
      return 0;
    }

UDP擴展軸與機器人關節運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人關節運動同步運動
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] desc_pos 目標笛卡爾位姿
    * @param [in] tool 工具坐標號，範圍[0~14]
    * @param [in] user 工件坐標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

UDP擴充軸與機器人關節運動同步運動 (自動正運動學計算）
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸與機器人關節運動同步運動 (自動正運動學計算)
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] epos 擴充軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, uint8_t offset_flag, DescPose offset_pos);

UDP擴展軸與機器人關節運動同步運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveJ()
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
      //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
      //  int SetToolPoint(int point_num); //設置工具參考點-六點法
      //  int ComputeTool(ref DescPose tcp_pose); //計算工具坐標系
      //  int SetTcp4RefPoint(int point_num);  //設置工具參考點-四點法
      //  int ComputeTcp4(ref DescPose tcp_pose);  //計算工具坐標系-四點法
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //設置應用工具坐標系
      //  int SetToolList(int id, DescPose coord, int type, int install);  //設置應用工具坐標系列表
      //2.設置UDP通信參數，並加載UDP通信
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3.設置擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸變位機及DH參數
      robot.SetRobotPosToAxis(1); //擴展軸安裝位置
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸變位機，因此只需要設置一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設置驅動器參數
      //4.設置所選的軸使能、回零
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5.進行擴展軸坐標系標定及應用
      DescPose pos = {/* 輸入您的標定點坐標 */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*您需要通過四個不同位置的點來標定擴展軸，因此需要調用此接口4次才能完成標定 */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //將標定結果應用到擴展軸坐標系
      //6.在擴展軸上標定工件坐標系，您需要用到以下接口
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7.記錄您的同步關節運動起始點
      DescPose startdescPose = {/*輸入您的坐標*/ };
      JointPos startjointPos = {/*輸入您的坐標*/ };
      ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點坐標 */ };
      //8.記錄您的同步關節運動終點坐標
      DescPose enddescPose = {/*輸入您的坐標*/ };
      JointPos endjointPos = {/*輸入您的坐標*/ };
      ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點坐標 */ };
      //9.編寫同步運動程序
      //運動到起始點，假設應用的工具坐標系、工件坐標系都是1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //開始同步運動
      robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      // 開始同步運動
      robot.ExtAxisSyncMoveJ(endjointPos, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
      robot.CloseRPC();
    }

UDP擴展軸與機器人直線運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人直線運動同步運動
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡爾位姿
    * @param [in] tool  工具坐標號，範圍[0~14]
    * @param [in] user  工件坐標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

UDP擴充軸與機器人直線運動同步運動 (自動逆運動學計算）
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸與機器人直線運動同步運動 (自動逆運動學計算)
    * @param [in] desc_pos  目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] epos 擴充軸位置，單位mm
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveL(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, uint8_t offset_flag, DescPose offset_pos, int config = -1);

UDP擴展軸與機器人直線運動同步運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveL()
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
      //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
      //  int SetToolPoint(int point_num); //設置工具參考點-六點法
      //  int ComputeTool(ref DescPose tcp_pose); //計算工具坐標系
      //  int SetTcp4RefPoint(int point_num);  //設置工具參考點-四點法
      //  int ComputeTcp4(ref DescPose tcp_pose);  //計算工具坐標系-四點法
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //設置應用工具坐標系
      //  int SetToolList(int id, DescPose coord, int type, int install);  //設置應用工具坐標系列表
      //2.設置UDP通信參數，並加載UDP通信
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3.設置擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸變位機及DH參數
      robot.SetRobotPosToAxis(1); //擴展軸安裝位置
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸變位機，因此只需要設置一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設置驅動器參數
      //4.設置所選的軸使能、回零
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5.進行擴展軸坐標系標定及應用
      DescPose pos = {/* 輸入您的標定點坐標 */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*您需要通過四個不同位置的點來標定擴展軸，因此需要調用此接口4次才能完成標定 */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //將標定結果應用到擴展軸坐標系
      //6.在擴展軸上標定工件坐標系，您需要用到以下接口
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7.記錄您的同步直線運動起始點
      DescPose startdescPose = {/*輸入您的坐標*/ };
      JointPos startjointPos = {/*輸入您的坐標*/ };
      ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點坐標 */ };
      //8.記錄您的同步直線運動終點坐標
      DescPose enddescPose = {/*輸入您的坐標*/ };
      JointPos endjointPos = {/*輸入您的坐標*/ };
      ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點坐標 */ };
      //9.編寫同步運動程序
      //運動到起始點，假設應用的工具坐標系、工件坐標系都是1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //開始同步運動
      robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      // 開始同步運動
      robot.ExtAxisSyncMoveL(enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
      robot.CloseRPC();
    }

UDP擴展軸與機器人圓弧運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人圓弧運動同步運動
    * @param [in] joint_pos_p  路徑點關節位置,單位deg
    * @param [in] desc_pos_p   路徑點笛卡爾位姿
    * @param [in] ptool  工具坐標號，範圍[0~14]
    * @param [in] puser  工件坐標號，範圍[0~14]
    * @param [in] pvel  速度百分比，範圍[0~100]
    * @param [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p  中間點擴展軸位置，單位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] joint_pos_t  目標點關節位置,單位deg
    * @param [in] desc_pos_t   目標點笛卡爾位姿
    * @param [in] ttool  工具坐標號，範圍[0~14]
    * @param [in] tuser  工件坐標號，範圍[0~14]
    * @param [in] tvel  速度百分比，範圍[0~100]
    * @param [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t  擴展軸位置，單位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_t  位姿偏移量	 
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);

UDP擴充軸與機器人圓弧運動同步運動 (自動逆運動學計算）
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸與機器人圓弧運動同步運動 (自動逆運動學計算)
    * @param [in] desc_pos_p  路徑點笛卡爾位姿
    * @param [in] ptool 工具座標號，範圍[0~14]
    * @param [in] puser 工件座標號，範圍[0~14]
    * @param [in] pvel 速度百分比，範圍[0~100]
    * @param [in] pacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p 擴充軸位置，單位mm
    * @param [in] poffset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_p 位姿偏移量
    * @param [in] desc_pos_t  目標點笛卡爾位姿
    * @param [in] ttool 工具座標號，範圍[0~14]
    * @param [in] tuser 工件座標號，範圍[0~14]
    * @param [in] tvel 速度百分比，範圍[0~100]
    * @param [in] tacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t 擴充軸位置，單位mm
    * @param [in] toffset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_t 位姿偏移量
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveC(DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, uint8_t poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, uint8_t toffset_flag, DescPose offset_pos_t, float ovl, float blendR, int config = -1);    

UDP擴展軸與機器人圓弧運動同步運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveC()
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
      //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
      //  int SetToolPoint(int point_num); //設置工具參考點-六點法
      //  int ComputeTool(ref DescPose tcp_pose); //計算工具坐標系
      //  int SetTcp4RefPoint(int point_num);  //設置工具參考點-四點法
      //  int ComputeTcp4(ref DescPose tcp_pose);  //計算工具坐標系-四點法
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //設置應用工具坐標系
      //  int SetToolList(int id, DescPose coord, int type, int install);  //設置應用工具坐標系列表
      //2.設置UDP通信參數，並加載UDP通信
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3.設置擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸變位機及DH參數
      robot.SetRobotPosToAxis(1); //擴展軸安裝位置
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸變位機，因此只需要設置一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設置驅動器參數
      //4.設置所選的軸使能、回零
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5.進行擴展軸坐標系標定及應用
      DescPose pos = {/* 輸入您的標定點坐標 */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*您需要通過四個不同位置的點來標定擴展軸，因此需要調用此接口4次才能完成標定 */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //將標定結果應用到擴展軸坐標系
      //6.在擴展軸上標定工件坐標系，您需要用到以下接口
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7.記錄您的同步圓弧運動起始點
      DescPose startdescPose = {/*輸入您的坐標*/ };
      JointPos startjointPos = {/*輸入您的坐標*/ };
      ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點坐標 */ };
      //8.記錄您的同步圓弧運動終點坐標
      DescPose enddescPose = {/*輸入您的坐標*/ };
      JointPos endjointPos = {/*輸入您的坐標*/ };
      ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點坐標 */ };
      //9.記錄您的同步圓弧運動中間點坐標
      DescPose middescPose = {/*輸入您的坐標*/ };
      JointPos midjointPos = {/*輸入您的坐標*/ };
      ExaxisPos midexaxisPos = {/* 輸入機器人圓弧中間點時的擴展軸坐標 */ };
      //10.編寫同步運動程序
      //運動到起始點，假設應用的工具坐標系、工件坐標系都是1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //開始同步運動
      robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      // 開始同步運動
      robot.ExtAxisSyncMoveC(middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
      robot.CloseRPC();
    }
    
設置擴展DO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展DO
    * @param [in] DONum DO編號
    * @param [in] bOpen 開關 true-開；false-關
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    errno_t SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
設置擴展AO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展AO
    * @param [in] AONum AO編號 
    * @param [in] value 模擬量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    errno_t SetAuxAO(int AONum, double value, bool block);
  
設置擴展DI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展DI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    errno_t SetAuxDIFilterTime(int filterTime);

設置擴展AI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展AI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    errno_t SetAuxAIFilterTime(int filterTime);

等待擴展DI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴展DI輸入
    * @param [in] DINum DI編號
    * @param [in] bOpen 開關 0-關；1-開
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    errno_t WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴展AI輸入
    * @param [in] AINum AI編號
    * @param [in] sign 0-大於；1-小於
    * @param [in] value AI值
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    errno_t WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
獲取擴展DI值
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取擴展DI值
    * @param [in] DINum DI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [out] isOpen 0-關；1-開
    * @return 錯誤碼
    */
    errno_t GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
獲取擴展AI值
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取擴展AI值
    * @param [in] AINum AI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [in] value 輸入值
    * @return 錯誤碼
    */
    errno_t GetAuxAI(int AINum, bool isNoBlock, int& value);

擴展IO代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAuxDOAO(void)
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
      for (int i = 0; i < 128; i++)
      {
        robot.SetAuxDO(i, true, false, true);
        Sleep(100);
      }
      for (int i = 0; i < 128; i++)
      {
        robot.SetAuxDO(i, false, false, true);
        Sleep(100);
      }
      for (int i = 0; i < 409; i++)
      {
        robot.SetAuxAO(0, i * 10, true);
        robot.SetAuxAO(1, 4095 - i * 10, true);
        robot.SetAuxAO(2, i * 10, true);
        robot.SetAuxAO(3, 4095 - i * 10, true);
        Sleep(10);
      }
      robot.SetAuxDIFilterTime(10);
      robot.SetAuxAIFilterTime(0, 10);
      for (int i = 0; i < 20; i++)
      {
        bool curValue = false;
        int rtn = robot.GetAuxDI(i, false, curValue);
        cout << "DI" << i << "  " << curValue << endl;
      }
      int curValue = -1;
      for (int i = 0; i < 4; i++)
      {
        rtn = robot.GetAuxAI(i, true, curValue);
      }
      robot.WaitAuxDI(1, false, 1000, false);
      robot.WaitAuxAI(1, 1, 132, 1000, false);
      robot.CloseRPC();
      return 0;
    }

可移動裝置使能
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 可移動裝置使能
    * @param enable false-去使能；true-使能
    * @return 錯誤碼
    */
    errno_t TractorEnable(bool enable);

可移動裝置回零
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 可移動裝置回零
    * @return 錯誤碼
    */
    errno_t TractorHoming();

可移動裝置直線運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
    * @brief 可移動裝置直線運動
    * @param distance 直線運動距離（mm）
    * @param vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    errno_t TractorMoveL(double distance, double vel);

可移動裝置圓弧運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 可移動裝置圓弧運動
    * @param radio 圓弧運動半徑（mm）
    * @param angle 圓弧運動角度（°）
    * @param vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    errno_t TractorMoveC(double radio, double angle, double vel);

可移動裝置停止運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 可移動裝置停止運動
    * @return 錯誤碼
    */
    errno_t TractorStop();

可移動裝置代碼示例
+++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestTractor(void)
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
      robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 1);
      robot.ExtDevLoadUDPDriver();
      rtn = robot.ExtAxisServoOn(1, 1);
      rtn = robot.ExtAxisServoOn(2, 1);
      robot.Sleep(2000);
      robot.ExtAxisSetHoming(1, 0, 10, 2);
      robot.Sleep(2000);
      rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
      robot.Sleep(4000);
      robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
      robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
      robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);
      robot.TractorEnable(false);
      robot.Sleep(2000);
      robot.TractorEnable(true);
      robot.Sleep(2000);
      robot.TractorHoming();
      robot.Sleep(2000);
      robot.TractorMoveL(100, 2);
      robot.Sleep(5000);
      robot.TractorStop();
      robot.TractorMoveL(-100, 20);
      robot.Sleep(5000);
      robot.TractorMoveC(300, 90, 20);
      robot.Sleep(10000);
      robot.TractorMoveC(300, -90, 20);
      robot.Sleep(1);
      robot.CloseRPC();
      return 0;
    }

UDP擴展軸定位完成時間設置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸定位完成時間設置
    * @param [in] time 定位完成時間[ms]
    * @return 錯誤碼
    */
    errno_t SetExAxisCmdDoneTime(double time);