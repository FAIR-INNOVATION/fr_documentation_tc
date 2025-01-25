擴展軸
=================

.. toctree:: 
    :maxdepth: 5

設定485擴展軸參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [in] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驅動器軟體版本，1-V1.0
    * @param [in] servoResolution 編碼器分辨率
    * @param [in] axisMechTransRatio 機械傳動比
    * @return 錯誤碼 
    */
    int AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);
    
取得485擴展軸參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得485擴展軸配置參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [out] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驅動器軟體版本，1-V1.0
    * @param [out] servoResolution 編碼器分辨率
    * @param [out] axisMechTransRatio 機械傳動比
    * @return 錯誤碼 
    */
    int AuxServoGetParam(int servoId, ref int servoCompany, ref int servoModel, ref int servoSoftVersion, ref int servoResolution, ref double axisMechTransRatio);
    
設定485擴展軸使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸使能/去使能
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] status 使能狀態，0-去使能， 1-使能
    * @return 錯誤碼 
    */
    int AuxServoEnable(int servoId, int status);
        
設定485擴展軸控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸控制模式
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 錯誤碼 
    */
    int AuxServoSetControlMode(int servoId, int mode);

代碼範例
**********
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);//設定配置參數
    int ID = -1, company = -1, model = -1, soft = -1, servoResolution= -1;
    int radio = -1;
        robot.AuxServoGetParam(1, ref company, ref model, ref soft, ref servoResolution, ref radio);//取得配置參數
        
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 0);//去使能伺服
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//設定位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能伺服
    }

設定485擴展軸回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸回零
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 回零模式，1-目前位置回零；2-負限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 錯誤碼 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

設定485擴展軸目標位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸目標位置(位置模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] pos 目標位置，mm或°
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed);

設定485擴展軸目標速度（速度模式）
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸目標速度（速度模式）
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed);

代碼範例
**********
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//設定位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//伺服回零需要一定的時間
                
        robot.AuxServoSetTargetPos(1, 1000, 100);//設定目標位置
        Thread.Sleep(1000);
        robot.AuxServoSetTargetPos(1, 0, 100);//再次設定目標位置
        Thread.Sleep(1000);

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 1);//設定速度模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//回零需要一定時間
        robot.AuxServoSetTargetSpeed(1, 50);//設定目標速度
        Thread.Sleep(3000);

        robot.AuxServoSetTargetSpeed(1, -300);//設定目標速度
        Thread.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 0);//伺服停止
        Thread.Sleep(100);
    }
    
設定485擴展軸目標轉矩(力矩模式)--暫未開放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定485擴展軸目標轉矩(力矩模式)--暫未開放
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] torque 目標力矩，Nm
    * @return 錯誤碼 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
清除485擴展軸錯誤訊息
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 清除485擴展軸錯誤訊息
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼 
    */
    int AuxServoClearError(int servoId);

取得485擴展軸伺服狀態
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得485擴展軸伺服狀態
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoErrCode 伺服驅動器故障碼
    * @param [out] servoState 伺服驅動器狀態bit0:0-未啟用；1-啟用;bit1:0-未移動；1-正在運動;bit2 0-正限位未觸發；1-正限位觸發；bit3 0-負限位未觸發；1-負限位觸發；bit4 0-未定位完成；1-定位完成；bit5：0-未回零；1-回零完成
    * @param [out] servoPos 伺服當前位置 mm或°
    * @param [out] servoSpeed 伺服當前速度 mm/s或°/s
    * @param [out] servoTorque 伺服當前轉矩Nm
    * @return 錯誤碼 
    */
    int AuxServoGetStatus(int servoId, ref int servoErrCode, ref int servoState, ref double servoPos, ref double servoSpeed, ref double servoTorque);
    
設定狀態回饋中485擴展軸資料軸號
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定狀態回饋中485擴展軸資料軸號
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼 
    */
    int AuxServosetStatusID(int servoId);

代碼範例
+++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

            robot.AuxServoClearError(1);
        int errCode = 0;
        int servoState = 0;
        double pos = 0;
        double speed = 0;
        double torque = 0;
        robot.AuxServoGetStatus(1, ref errCode, ref servoState, ref pos, ref speed, ref torque);

        robot.AuxServosetStatusID(1);
        ROBOT_STATE_PKG pKG = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pKG);
        Console.WriteLine($"the state is {pKG.auxState.servoPos}");
    }

UDP擴充軸通訊參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴充軸通訊參數配置
    * @param [in] ip PLC IP地址
    * @param [in] port	連接埠號
    * @param [in] period	通訊週期(ms，預設為2，請勿修改此參數)
    * @param [in] lossPkgTime	丟包檢測時間(ms)
    * @param [in] lossPkgNum	丟包次數
    * @param [in] disconnectTime	通訊斷開確認時長
    * @param [in] reconnectEnable	通訊斷開自動重連啟用 0-不啟用 1-啟用
    * @param [in] reconnectPeriod	重連週期間隔(ms)
    * @param [in] reconnectNum	重連次數
    * @return 錯誤碼
    */
    int ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum);
        
取得UDP擴充軸通訊參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 取得UDP擴充軸通訊參數
    * @param [out] ip PLC IP地址
    * @param [out] port	連接埠號
    * @param [out] period	通訊週期(ms，預設為2，請勿修改此參數)
    * @param [out] lossPkgTime	丟包檢測時間(ms)
    * @param [out] lossPkgNum	丟包次數
    * @param [out] disconnectTime	通訊斷開確認時長
    * @param [out] reconnectEnable	通訊斷開自動重連啟用 0-不啟用 1-啟用
    * @param [out] reconnectPeriod	重連週期間隔(ms)
    * @param [out] reconnectNum	重連次數
    * @return 錯誤碼
    */
    int ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum);
        
加載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 加載UDP通信
    * @return 錯誤碼
    */
    int ExtDevLoadUDPDriver();

卸載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 卸載UDP通信
    * @return 錯誤碼
    */
    int ExtDevUnloadUDPDriver();

代碼範例
**************

.. code-block:: C#
    :linenos:

    private void btnSetParam_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        string ip = "";
        int port = 0;
        int period = 0;
        int checktime = 0;
        int checknum = 0;
        int disconntime = 0;
        int reconnenable = 0;
        int reconntime = 0;
        int reconnnum = 0;
        robot.ExtDevGetUDPComParam(ref ip, ref port, ref period, ref checktime, ref checknum, ref disconntime, ref reconntime, ref reconnenable, ref reconnnum);
        Console.Writeline($"{ip}  {port}  {period} {checktime}  {checknum}  {disconntime}  {reconnenable}  {reconntime}  {reconnnum}");

        robot.ExtDevLoadUDPDriver();
        Thread.Sleep(1000 * 10);
        robot.ExtDevUnloadUDPDriver();
    }

UDP擴充軸通訊異常斷開後恢復連接
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後恢復連接
    * @return 錯誤碼
    */
    int ExtDevUDPClientComReset();

UDP擴充軸通訊異常斷開後關閉通訊
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後關閉通訊
    * @return 錯誤碼
    */
    int ExtDevUDPClientComClose();

UDP擴充軸參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴充軸參數配置
    * @param [in] axisID 軸號
    * @param [in] axisType 擴展軸類型 0-平移；1-旋轉
    * @param [in] axisDirection 擴展軸方向 0-正向；1-方向
    * @param [in] axisMax 擴展軸最大位置 mm
    * @param [in] axisMin 擴展軸最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 導程mm
    * @param [in] encResolution 編碼器分辨率
    * @param [in] axisOffect焊接起始點擴展軸偏移量
    * @param [in] axisCompany 驅動器廠商 1-禾川；2-匯川；3-松下
    * @param [in] axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 編碼器類型 0-增量；1-絕對值
    * @return 錯誤碼
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

設定擴展軸安裝位置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴展軸安裝位置
    * @param [in] installType 0-機器人安裝在外部軸上，1-機器人安裝在外部軸外
    * @return 錯誤碼
    */
    int SetRobotPosToAxis(int installType);

設定擴展軸系統DH參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴展軸系統DH參數配置
    * @param [in]  axisConfig 外部軸構型，0-單自由度直線滑軌，1-兩自由度L型變位機，2-三自由度，3-四自由度，4-單自由度變位機
    * @param [in]  axisDHd1 外部軸DH參數d1 mm
    * @param [in]  axisDHd2 外部軸DH參數d2 mm
    * @param [in]  axisDHd3 外部軸DH參數d3 mm
    * @param [in]  axisDHd4 外部軸DH參數d4 mm
    * @param [in]  axisDHa1 外部軸DH參數11 mm
    * @param [in]  axisDHa2 外部軸DH參數a2 mm
    * @param [in]  axisDHa3 外部軸DH參數a3 mm
    * @param [in]  axisDHa4 外部軸DH參數a4 mm
    * @return 錯誤碼
    */
    int SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

代碼範例
**********

.. code-block:: C#
    :linenos:

    private void btnSetAxisParam_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int rtn = 0;
        rtn = robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0);
        Console.WriteLine($"SetAxisDHParaConfig rtn is {rtn}");
        rtn = robot.SetRobotPosToAxis(1);
        Console.WriteLine($"SetRobotPosToAxis rtn is {rtn}");
        rtn = robot.ExtAxisParamConfig(1,0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0);
        Console.WriteLine($"ExtAxisParamConfig rtn is {rtn}");
    }

設定擴展軸座標系參考點-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴展軸座標系參考點-四點法
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    int ExtAxisSetRefPoint(int pointNum);

計算擴展軸座標系-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 計算擴展軸座標系-四點法
    * @param [out]  coord 座標系值
    * @return 錯誤碼
    */
    int ExtAxisComputeECoordSys(DescPose& coord);

應用擴展軸座標系
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 應用擴展軸座標系
    * @param [in]  applyAxisId 擴展軸編號 bit0-bit3對應擴展軸編號1-4，如應用擴展軸1和3，則是 0b 0000 0101；也就是5
    * @param [in]  axisCoordNum 擴展軸座標系編號
    * @param [in]  coord 座標系值
    * @param [in]  calibFlag 標定標誌 0-否，1-是
    * @return 錯誤碼
    */
    int ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnCoordCalib_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtAxisSetRefPoint(1);
        //robot.ExtAxisSetRefPoint(2);
        //robot.ExtAxisSetRefPoint(3);
        //robot.ExtAxisSetRefPoint(4);
        //DescPose pos = new DescPose();
        //robot.ExtAxisComputeECoordSys(ref pos);
    }

設定標定參考點在變位機末端座標系下位姿
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定標定參考點在變位機末端座標系下位姿
    * @param [in] pos 位元姿值
    * @return 錯誤碼
    */
    int SetRefPointInExAxisEnd(DescPose pos);

變位機座標系參考點設置
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 變位機座標系參考點設置
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    int PositionorSetRefPoint(int pointNum);

變位機座標系計算-四點法
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 變位機座標系計算-四點法
    * @param [out] coord 座標系值
    * @return 錯誤碼
    */
    int PositionorComputeECoordSys(DescPose& coord);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnCoordCalib_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose refPointPos = new DescPose(122.0, 312.0, 0, 0, 0, 0);
        robot.SetRefPointInExAxisEnd(refPointPos);

        robot.PositionorSetRefPoint(1);
        //robot.PositionorSetRefPoint(2);
        //robot.PositionorSetRefPoint(3);
        //robot.PositionorSetRefPoint(4);

        //DescPose coord = new DescPose();
        //robot.PositionorComputeECoordSys(ref coord);
    }

UDP擴展軸使能
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸使能
    * @param [in] axisID 軸號[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 錯誤碼
    */
    int ExtAxisServoOn(int axisID, int status);

UDP擴展軸回零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸回零
    * @param [in] axisID 軸號[1-4]
    * @param [in] mode 回零方式 0-目前位置回零，1-負限位回零，2-正限位回零
    * @param [in] searchVel 尋零速度(mm/s)
    * @param [in] latchVel 尋零箍位速度(mm/s)
    * @return 錯誤碼
    */
    int ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP擴展軸點動開始
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
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
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP擴展軸點動停止
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸點動停止
    * @param [in] axisID 軸號[1-4]
    * @return 錯誤碼
    */
    int ExtAxisStopJog(int axisID);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnJog_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtAxisServoOn(1, 1);
        robot.ExtAxisSetHoming(1, 0, 10, 3);
        robot.ExtAxisStartJog(1, 1, 100, 100, 20);
        Thread.Sleep(1000 * 2);
        robot.ExtAxisStopJog(1);
        robot.ExtAxisServoOn(1, 0);
    }

UDP擴展軸運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸運動
    * @param [in] pos 目標位置
    * @param [in] ovl 速度百分比
    * @return 錯誤碼
    */
    int ExtAxisMove(ExaxisPos pos, double ovl);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnAxisMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        ExaxisPos pos = new ExaxisPos(10, 0, 0, 0);
        robot.ExtAxisMove(pos, 10);
    }

UDP擴展軸與機器人關節運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸與機器人關節運動同步運動
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] desc_pos 目標笛卡兒位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveJ_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴充軸座標系標定及應用(注意：變位機和直線滑軌的標定介面不同，以下時變位機的標定介面)
        DescPose pos = new DescPose(/* 輸入您的標定點座標 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = new DescPose( );
        robot.PositionorComputeECoordSys(ref coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步關節運動起始點
        DescPose startdescPose = new DescPose(/*輸入您的座標*/);
        JointPos startjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 輸入您的擴展軸起始點座標 */);

        //8.記錄您的同步關節運動終點座標
        DescPose enddescPose = new DescPose(/*輸入您的座標*/);
        JointPos endjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 輸入您的擴展軸終點座標 */);

        //9.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
    }

UDP擴展軸與機器人直線運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸與機器人直線運動同步運動
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡兒位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位元位偏移量
    * @return 錯誤碼
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveL_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴展軸座標系標定及應用
        DescPose pos = new DescPose(/* 輸入您的標定點座標 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要使用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步直線運動起始點
        DescPose startdescPose = new DescPose(/*輸入您的座標*/);
        JointPos startjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 輸入您的擴展軸起始點座標 */);

        //8.記錄您的同步直線運動終點座標
        DescPose enddescPose = new DescPose(/*輸入您的座標*/);
        JointPos endjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 輸入您的擴展軸終點座標 */);

        //9.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
    }
    
UDP擴展軸與機器人圓弧運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP擴展軸與機器人圓弧運動同步運動
    * @param [in] joint_pos_p  路徑點關節位置,單位deg
    * @param [in] desc_pos_p   路徑點笛卡爾位姿
    * @param [in] ptool  工具座標號，範圍[0~14]
    * @param [in] puser  工件座標號，範圍[0~14]
    * @param [in] pvel  速度百分比，範圍[0~100]
    * @param [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p  中间點擴展軸位置，單位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_p  位元位偏移量
    * @param [in] joint_pos_t  目標點關節位置,單位deg
    * @param [in] desc_pos_t   目標點笛卡爾位姿
    * @param [in] ttool  工具座標號，範圍[0~14]
    * @param [in] tuser  工件座標號，範圍[0~14]
    * @param [in] tvel  速度百分比，範圍[0~100]
    * @param [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t  擴展軸位置，單位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_t  位元位偏移量	 
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @return 錯誤碼
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);
    
代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveC_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴展軸座標系標定及應用
        DescPose pos = new DescPose(/* 輸入您的標定點座標 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步圓弧運動起始點
        DescPose startdescPose = new DescPose(/*輸入您的座標*/);
        JointPos startjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 輸入您的擴展軸起始點座標 */);

        //8.記錄您的同步圓弧運動終點座標
        DescPose enddescPose = new DescPose(/*輸入您的座標*/);
        JointPos endjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 輸入您的擴展軸終點座標 */);

        //8.記錄您的同步圓弧運動中間點座標
        DescPose middescPose = new DescPose(/*輸入您的座標*/);
        JointPos midjointPos = new JointPos(/*輸入您的座標*/);
        ExaxisPos midexaxisPos = new ExaxisPos(/* 輸入機器人圓弧中間點時的擴展軸座標 */);

        //9.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
    }

設定焊絲尋位擴充IO端口
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊絲尋位擴充IO端口
    * @param searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param searchStartDONum 焊絲尋位啟動停止控制DO端口(0-127)
    * @return 錯誤碼
    */
    int  SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

代碼範例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        //UDP焊絲尋位
        robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevLoadUDPDriver();
        robot.SetWireSearchExtDIONum(0, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        DescPose descStart = new DescPose(-158.767, -510.596, 271.709, -179.427, -0.745, -137.349);
        JointPos jointStart = new JointPos(61.667, -79.848, 108.639, -119.682, -89.700, -70.985);

        DescPose descEnd = new DescPose(0.332, -516.427, 270.688, 178.165, 0.017, -119.989);
        JointPos jointEnd = new JointPos(79.021, -81.839, 110.752, -118.298, -91.729, -70.981);

        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

        DescPose descREF0A = new DescPose(-66.106, -560.746, 270.381, 176.479, -0.126, -126.745);
        JointPos jointREF0A = new JointPos(73.531, -75.588, 102.941, -116.250, -93.347, -69.689);

        DescPose descREF0B = new DescPose(-66.109, -528.440, 270.407, 176.479, -0.129, -126.744);
        JointPos jointREF0B = new JointPos(72.534, -79.625, 108.046, -117.379, -93.366, -70.687);

        DescPose descREF1A = new DescPose(72.975, -473.242, 270.399, 176.479, -0.129, -126.744);
        JointPos jointREF1A = new JointPos(87.169, -86.509, 115.710, -117.341, -92.993, -56.034);
        DescPose descREF1B = new DescPose(31.355, -473.238, 270.405, 176.480, -0.130, -126.745);
        JointPos jointREF1B = new JointPos(82.117, -87.146, 116.470, -117.737, -93.145, -61.090);
        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
        List<string> varNameRef1 = new List<string> { "REF0", "REF1", "#", "#", "#", "#" };
        List<string> varNameRes1 = new List<string> { "RES0", "RES1", "#", "#", "#", "#" };
        string[] varNameRef = varNameRef1.ToArray();
        string[] varNameRes = varNameRes1.ToArray();
        int offectFlag = 0;
        DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, ref offectFlag, ref offectPos);
        robot.PointsOffsetEnable(0, offectPos);
        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);
        robot.PointsOffsetDisable();
    }

設定焊機控制模式擴展DO端口
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊機控制模式擴展DO端口
    * @param DONum 焊機控制模式DO端口(0-127)
    * @return 錯誤碼
    */
    int  SetWeldMachineCtrlModeExtDoNum(int DONum);

設定焊機控制模式
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊機控制模式
    * @param mode 焊接機控制模式;0-一元化
    * @return 錯誤碼
    */
    int SetWeldMachineCtrlMode(int mode);

代碼範例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button8_Click(object sender, EventArgs e)
    {
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevLoadUDPDriver();

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }

        robot.SetWeldMachineCtrlModeExtDoNum(18);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }
        robot.SetWeldMachineCtrlModeExtDoNum(19);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }
    }

可移動裝置使能
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移動裝置使能
    * @param enable false-去使能；true-使能
    * @return 錯誤碼
    */
    int TractorEnable(bool enable);

可移動裝置停止運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移動裝置停止運動
    * @return 錯誤碼
    */
    int TractorStop();

可移動裝置回零
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移動裝置回零
    * @return 錯誤碼
    */
    int  TractorHoming();

可移動裝置直線運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移動裝置直線運動
    * @param distance 直線運動距離（mm）
    * @param vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    int TractorMoveL(double distance, double vel);

可移動裝置圓弧運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移動裝置圓弧運動
    * @param radio 圓弧運動半徑（mm）
    * @param angle 圓弧運動角度（°）
    * @param vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    int TractorMoveC(double radio, double angle, double vel);

代碼範例
+++++++++
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgs e)
    {
        robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10);
        int tru = robot.ExtDevLoadUDPDriver();
        Thread.Sleep(2000);
        Console.WriteLine("tru" + tru);
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);
        int tru1 = robot.TractorEnable(true);
        Thread.Sleep(3000);
        robot.TractorHoming();
        Thread.Sleep(2000);
        robot.TractorMoveL(100, 20);
        Thread.Sleep(2000);
        robot.TractorMoveL(-100, 20);
        Thread.Sleep(2000);
        robot.TractorMoveC(50, 60, 20);
        Thread.Sleep(2000);
        robot.TractorMoveC(50, -60, 20);
        Thread.Sleep(1000);
        robot.TractorStop();//中途停止
    }

設定擴充DO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴充DO
    * @param [in] DONum DO編號
    * @param [in] bOpen 開關 true-開；false-關
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    int SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
設定擴充AO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴充AO
    * @param [in] AONum AO編號 
    * @param [in] value 類比量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    int SetAuxAO(int AONum, double value, bool block);
    
代碼範例
************

.. code-block:: C#
    :linenos:

    private void btnAODO_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, true, false, true);
            Thread.Sleep(200);
        }

        for(int i = 0; i < 409; i++)
        {
            robot.SetAuxAO(0, i * 10, true);
            robot.SetAuxAO(1, 4095 - i * 10, true);
            robot.SetAuxAO(2, i * 10, true);
            robot.SetAuxAO(3, 4095 - i * 10, true);
            Thread.Sleep(10);
        }
    }
            
設定擴充DI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴充DI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    int SetAuxDIFilterTime(int filterTime);

設定擴展AI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 設定擴展AI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    int SetAuxAIFilterTime(int filterTime);

等待擴充DI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 等待擴充DI輸入
    * @param [in] DINum DI編號
    * @param [in] bOpen 開關 0-關；1-開
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    int WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
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
    int WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
取得擴展DI值
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 取得擴展DI值
    * @param [in] DINum DI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [out] isOpen 0-關；1-開
    * @return 錯誤碼
    */
    int GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
取得擴展AI值
+++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 取得擴展AI值
    * @param [in] AINum AI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [in] value 輸入值
    * @return 錯誤碼
    */
    int GetAuxAI(int AINum, bool isNoBlock, int& value);

代碼範例
***********
.. code-block:: C#
    :linenos:

    private void btnAIDI_Click(object sender, EventArgs e)
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    robot.SetAuxDIFilterTime(10);
    robot.SetAuxAIFilterTime(10);

    for (int i = 0; i < 20; i++)
    {
        bool curValue = false;
        int rtn = robot.GetAuxDI(i, false, ref curValue);
        txtRtn.Text = rtn.ToString();
        Console.Write($"DI{i}  {curValue}  ");
        Console.WriteLine("  ");
    }

    int curValue = -1;
    int rtn = 0;
    for (int i = 0; i < 4; i++)
    {
        rtn = robot.GetAuxAI(i, true, ref curValue);
        txtRtn.Text = rtn.ToString();
        Console.Write($"AI{i} {curValue}   rtn is {rtn} ");
        Console.WriteLine("  ");
    }

    robot.WaitAuxDI(1, true, 1000, false);
    robot.WaitAuxAI(1, 1, 132, 1000, false);
    }


