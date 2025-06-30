擴展軸
=================

.. toctree:: 
    :maxdepth: 5

設定485擴展軸參數
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] param 485擴展軸參數
    * @return 錯誤碼 
    */
    int AuxServoSetParam(int servoId, Axis485Param param)
    
取得485擴展軸參數
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得485擴展軸配置參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [out] param 485擴展軸參數
    * @return 錯誤碼 
    */
    int AuxServoGetParam(int servoId, Axis485Param param);

設定485擴展軸使能/去使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸使能/去使能
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] status 使能狀態，0-去使能， 1-使能
    * @return 錯誤碼 
    */
    int AuxServoEnable(int servoId, int status);
        
設定485擴展軸控制模式
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸控制模式
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 錯誤碼 
    */
    int AuxServoSetControlMode(int servoId, int mode);

設定485擴展軸回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸回零
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] mode 回零模式，1-目前位置回零；2-負限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 錯誤碼 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

設定485擴展軸目標位置(位置模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸目標位置(位置模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] pos 目標位置，mm或°
    * @param [in] speed 目標速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 錯誤碼 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed, double acc);

設定485擴展軸目標速度（速度模式）
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸目標速度（速度模式）
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] speed 目標速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 錯誤碼 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed, double acc);

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        Axis485Param param = new Axis485Param();
        param.servoCompany = 1;           // 伺服驅動器廠商，1-戴納泰克
        param.servoModel = 1;             // 伺服驅動器型號，1-FD100-750C
        param.servoSoftVersion = 1;       // 伺服驅動器軟體版本，1-V1.0
        param.servoResolution = 131072;        // 編碼器分辨率
        param.axisMechTransRatio = 13.45;  // 機械傳動比
        robot.AuxServoSetParam(1, param);//設定485擴展軸參數

        robot.AuxServoGetParam(1, param);
        System.out.println("auxservo param servoCompany: " + param.servoCompany + "  servoModel:  " + param.servoModel +"  param.servoSoftVersion:  " + param.servoSoftVersion + "  servoResolution:  " + param.servoResolution + "  axisMechTransRatio:  " + param.axisMechTransRatio);
        
        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);
        robot.AuxServoEnable(1, 0);
        robot.Sleep(3000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(2000);
        robot.AuxServoHoming(1, 1, 10, 10,100);
        robot.Sleep(5000);

        robot.AuxServoSetTargetSpeed(1, 100,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, -200,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 0,100);
    }
    
設定485擴展軸目標轉矩(力矩模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定485擴展軸目標轉矩(力矩模式)-暫未開放
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @param [in] torque 目標力矩，Nm
    * @return 錯誤碼 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
清除485擴展軸錯誤訊息
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 清除485擴展軸錯誤訊息
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @return 錯誤碼 
    */
    int AuxServoClearError(int servoId);

設定狀態回饋中485擴展軸資料軸號
+++++++++++++++++++++++++++++++++++++++++ 
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定狀態回饋中485擴展軸資料軸號
    * @param [in] servoId 伺服驅動器ID，範圍[1-16],對應從站ID
    * @return 錯誤碼 
    */
    int AuxServosetStatusID(int servoId);

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);
        robot.AuxServoEnable(1, 0);
        robot.Sleep(3000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(2000);
        robot.AuxServoHoming(1, 1, 10, 10,100);
        robot.Sleep(5000);

        robot.AuxServoSetTargetSpeed(1, 40,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 40,100);

        robot.AuxServosetStatusID(1);

        while (true)
        {
            ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
            System.out.println("aux servo cur Pos :" + pkg.auxState.servoPos + "  cur vel:  " + pkg.auxState.servoVel);
            robot.Sleep(100);
        }
    }

UDP擴展軸通訊參數配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸通訊參數配置
    * @param [in] param 通訊參數
    * @return 錯誤碼
    */
    int ExtDevSetUDPComParam(UDPComParam param);     

取得UDP擴充軸通訊參數配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得UDP擴充軸通訊參數
    * @param [out] param 通訊參數
    * @return 錯誤碼
    */
    int ExtDevGetUDPComParam(UDPComParam param);       

加載UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 加載UDP通信
    * @return 錯誤碼
    */
    int ExtDevLoadUDPDriver();

卸載UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 卸載UDP通信
    * @return 錯誤碼
    */
    int ExtDevUnloadUDPDriver();

代碼範例
+++++++++++++++++++++++++++++++++++++++++

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
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//udp擴展軸通訊

        UDPComParam getParam = new UDPComParam();
        robot.ExtDevGetUDPComParam(getParam);
        System.out.println(" " + getParam.ip + " ,   " + getParam.port + " ,   " + getParam.period + " ,  " + getParam.lossPkgTime + " ,   " + getParam.lossPkgNum + " ,   " + getParam.disconnectTime + " ,   " + getParam.reconnectEnable + " ,   " + getParam.reconnectPeriod + " ,   " + getParam.reconnectNum);
        robot.ExtDevUnloadUDPDriver();//卸載UDP通信
        robot.Sleep(1000);
        robot.ExtDevLoadUDPDriver();//加載UDP通信
        robot.Sleep(1000);
    }

UDP擴充軸通訊異常斷開後恢復連接
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後恢復連接
    * @return 錯誤碼
    */
    int ExtDevUDPClientComReset();

UDP擴充軸通訊異常斷開後關閉通訊
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後關閉通訊
    * @return 錯誤碼
    */
    int ExtDevUDPClientComClose();

UDP擴充軸參數配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] axisOffect 焊缝起始點擴展軸偏移量
    * @param [in] axisCompany 驅動器廠商 1-禾川；2-匯川；3-松下
    * @param [in] axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 編碼器類型 0-增量；1-絕對值
    * @return 錯誤碼
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, int encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

獲取擴展軸驅動器配置信息
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取擴展軸驅動器配置信息
    * @param [in] axisId 軸號[1-4]
    * @return List[0]: 錯誤碼 List[1]: axisCompany 驅動器廠商 1-禾川；2-匯川；3-松下;
    * List[2]: axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * List[3]: axisEncType 編碼器類型 0-增量；1-絕對值
    */
    List<Integer> GetExAxisDriverConfig(int axisId);

設定擴展軸安裝位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展軸安裝位置
    * @param [in] installType 0-機器人安裝在外部軸上，1-機器人安裝在外部軸外
    * @return 錯誤碼
    */
    int SetRobotPosToAxis(int installType);

設定擴展軸系統DH參數配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展軸系統DH參數配置
    * @param [in]  axisConfig 外部軸構型，0-單自由度直線滑軌，1-兩自由度L型變位機，2-三自由度，3-四自由度，4-單自由度變位機
    * @param [in]  axisDHd1 外部軸DH參數d1 mm
    * @param [in]  axisDHd2 外部軸DH參數d2 mm
    * @param [in]  axisDHd3 外部軸DH參數d3 mm
    * @param [in]  axisDHd4 外部軸DH參數d4 mm
    * @param [in]  axisDHa1 外部軸DH參數a1 mm
    * @param [in]  axisDHa2 外部軸DH參數a2 mm
    * @param [in]  axisDHa3 外部軸DH參數a3 mm
    * @param [in]  axisDHa4 外部軸DH參數a4 mm
    * @return 錯誤碼
    */
    int SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

代碼範例
+++++++++++++++++++++++++++++++++++++++++

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
        robot.ExtAxisServoOn(1, 1);//擴展軸1使能
        robot.ExtAxisServoOn(2, 1);//擴展軸2使能
        robot.Sleep(1000);
        robot.ExtAxisSetHoming(1, 0, 10, 3);//1,2擴展軸都回零
        robot.ExtAxisSetHoming(2, 0, 10, 3);
        robot.Sleep(1000);

        int rtn = 0;
        rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0);
        System.out.println("SetAxisDHParaConfig rtn is " + rtn);
        rtn = robot.SetRobotPosToAxis(1);
        System.out.println("SetRobotPosToAxis rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(1,1, 0, 50, -50, 1000, 1000, 1.905, 262144, 200, 0, 0, 0);
        System.out.println("ExtAxisParamConfig rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(2,2, 0, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 0, 0, 0);
        System.out.println("ExtAxisParamConfig rtn is " + rtn);
    }

設定擴展軸座標系參考點-四點法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展軸座標系參考點-四點法
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    int ExtAxisSetRefPoint(int pointNum);

計算擴展軸座標系-四點法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 計算擴展軸座標系-四點法
    * @param [out]  coord 座標系值
    * @return 錯誤碼
    */
    int ExtAxisComputeECoordSys(DescPose coord);

應用擴展軸座標系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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

設定標定參考點在變位機末端座標系下位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定標定參考點在變位機末端座標系下位姿
    * @param [in] pos 位元姿值
    * @return 錯誤碼
    */
    int SetRefPointInExAxisEnd(DescPose pos);

變位機座標系參考點設置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 變位機座標系參考點設置
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    int PositionorSetRefPoint(int pointNum);

變位機座標系計算-四點法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 變位機座標系計算-四點法
    * @param [out] coord 座標系值
    * @return 錯誤碼
    */
    int PositionorComputeECoordSys(DescPose coord);

末端感測器暫存器寫入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端感測器暫存器寫入
    * @param [in] devAddr  設備地址編號 0-255
    * @param [in] regHAddr 暫存器位址高8位
    * @param [in] regLAddr 暫存器位址低8位
    * @param [in] regNum  暫存器個數 0-255
    * @param [in] data1 寫入暫存器數值1
    * @param [in] data2 寫入暫存器數值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 錯誤碼
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

UDP擴展軸使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸使能
    * @param [in] axisID 軸號[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 錯誤碼
    */
    int ExtAxisServoOn(int axisID, int status);

UDP擴展軸回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸點動開始
    * @param [in] axisID 軸號[1-4]
    * @param [in] direction 轉動方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc (加速度 mm/s2)
    * @param [in] maxDistance 最大點動距離
    * @return 錯誤碼
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP擴展軸點動停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸點動停止
    * @param [in] axisID 軸號[1-4]
    * @return 錯誤碼
    */
    int ExtAxisStopJog(int axisID);

代碼範例
+++++++++++++++++++++++++++++++++++++++++

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

        robot.ExtAxisServoOn(1, 1);
        robot.ExtAxisSetHoming(1, 0, 10, 3);
        robot.ExtAxisStartJog(1, 1, 100, 100, 20);
        robot.Sleep(1000);
        robot.ExtAxisStopJog(1);
        robot.ExtAxisServoOn(1, 0);
    }

設定擴充DO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴充DO
    * @param [in] DONum DO編號
    * @param [in] bOpen 開關 true-開；false-關
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    int SetAuxDO(int DONum, boolean bOpen, boolean smooth, boolean block);

設定擴充AO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴充AO
    * @param [in] AONum AO編號
    * @param [in] value 類比量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    int SetAuxAO(int AONum, double value, boolean block);

設定擴充DI輸入濾波時間
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴充DI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return  錯誤碼
    */
    int SetAuxDIFilterTime(int filterTime);

設定擴展AI輸入濾波時間
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展AI輸入濾波時間
    * @param [in] AONum AO編號
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    int SetAuxAIFilterTime(int AONum, int filterTime);

等待擴充DI輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待擴充DI輸入
    * @param [in] DINum DI編號
    * @param [in] bOpen 開關 0-關；1-開
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    int WaitAuxDI(int DINum, boolean bOpen, int time, boolean errorAlarm);

等待擴展AI輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int WaitAuxAI(int AINum, int sign, int value, int time, boolean errorAlarm);
    
取得擴展AI值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得擴展AI值
    * @param [in] AINum AI編號
    * @param [in] isNoBlock 是否阻塞
    * @return List[0]:錯誤碼; List[1] : value 輸入值
    */
    List<Integer> GetAuxAI(int AINum, boolean isNoBlock);

UDP擴展軸運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸運動
    * @param [in] pos 目標位置
    * @param [in] ovl 速度百分比
    * @return 錯誤碼
    */
    int ExtAxisMove(ExaxisPos pos, double ovl);

UDP擴展軸與機器人關節運動同步運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP擴展軸與機器人關節運動同步運動
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡兒位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] ffset_pos  位元位偏移量
    * @return 錯誤碼
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);
    
UDP擴展軸與機器人直線運動同步運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos  位元位偏移量
    * @return 錯誤碼
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

UDP擴展軸與機器人圓弧運動同步運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] poffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos_p  位元位偏移量
    * @param [in] joint_pos_t  目標點關節位置,單位deg
    * @param [in] desc_pos_t   目標點笛卡爾位姿
    * @param [in] ttool  工具座標號，範圍[0~14]
    * @param [in] tuser  工件座標號，範圍[0~14]
    * @param [in] tvel  速度百分比，範圍[0~100]
    * @param [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t  擴展軸位置，單位mm
    * @param [in] toffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos_t  位元位偏移量
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @return 錯誤碼
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

代碼範例
+++++++++++++++++++++++++++++++++++++++++

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
        robot.Mode(0);
        int tool = 1;
        int user = 0;
        double vel = 20.0;
        double acc = 100.0;
        double ovl = 100.0;
        ExaxisPos exaxisPos = new ExaxisPos( 0, 0, 0, 0 );

        DescPose d0 = new DescPose(311.189, -309.688, 401.836, -174.375, -1.409, -82.354);
        JointPos j0 =new JointPos(118.217, -99.669, 79.928, -73.559, -85.229, -69.359);

        JointPos joint_pos0 =new JointPos(111.549,-99.821,108.707,-99.308,-85.305,-41.515);
        DescPose desc_pos0 = new DescPose(273.499,-345.746,201.573,-176.566 ,3.235,-116.819);
        ExaxisPos e_pos0=new ExaxisPos(0,0,0,0);

        JointPos joint_pos1 = new JointPos(112.395,-65.118,67.815,-61.449,-88.669,-41.517);
        DescPose desc_pos1 = new DescPose(291.393,-420.519,201.089,156.297,21.019,-120.919);
        ExaxisPos e_pos1 = new ExaxisPos(-30, -30, 0, 0);


        JointPos j2 = new JointPos(111.549,-98.369,108.036,-103.789,-95.203,-69.358);
        DescPose desc_pos2 = new DescPose(234.544,-392.777,205.566,176.584,-5.694,-89.109);
        ExaxisPos epos2 = new ExaxisPos(0.000,0.000,0.000,0.000);

        JointPos j3 = new JointPos(113.908,-61.947,63.829,-64.478,-85.406,-69.256);
        DescPose desc_pos3 = new DescPose(336.049,-444.969,192.799,173.776 ,27.104,-89.455);
        ExaxisPos epos3 = new ExaxisPos(-30.000,-30.000, 0.000, 0.000);

        //圓弧的起點
        JointPos j4 = new JointPos(137.204,-98.475,106.624,-97.769,-90.634,-69.24);
        DescPose desc_pos4 = new DescPose(381.269,-218.688,205.735,179.274,0.128,-63.556);

        JointPos j5 = new JointPos(115.069,-92.709,97.285,-82.809,-90.455,-77.146);
        DescPose desc_pos5 = new DescPose(264.049,-329.478 ,220.747,176.906,11.359,-78.044);
        ExaxisPos  epos5 = new ExaxisPos(-15, 0, 0, 0);


        JointPos j6 = new JointPos(102.409,-63.115,70.559,-70.156,-86.529,-77.148);
        DescPose desc_pos6 = new DescPose(232.407,-494.228 ,158.115,176.803,27.319,-92.056);
        ExaxisPos  epos6 = new ExaxisPos(-30, 0, 0, 0);

        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        //同步關節運動
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.ExtAxisSyncMoveJ(joint_pos0, desc_pos0, 1, 0,20,100,100,e_pos0,-1,0,offset_pos);
        robot.ExtAxisSyncMoveJ(joint_pos1, desc_pos1, 1, 0,20,100,100,e_pos1,-1,0,offset_pos);


        //同步直線運動
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.ExtAxisSyncMoveL(j2, desc_pos2, tool, user, 40, 100, 100, -1, epos2, 0, offset_pos);
        robot.ExtAxisSyncMoveL(j3, desc_pos3, tool, user, 40, 100, 100, -1, epos3, 0, offset_pos);
        //同步圓弧運動
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,20);
        robot.MoveJ(j4, desc_pos4, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);

        robot.ExtAxisSyncMoveC(j5, desc_pos5, tool, user, 40, 100, epos5, 0, offset_pos, j6, desc_pos6, tool, user, 40, 100, epos6, 0, offset_pos, 100, 0);

        robot.Sleep(3000);
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.Mode(1);
    }

可移動裝置使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移動裝置使能
    * @param [in] enable false-去使能；true-使能
    * @return 錯誤碼
    */
    int TractorEnable(Boolean enable);

可移動裝置回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移動裝置回零
    * @return 錯誤碼
    */
    int TractorHoming();

可移動裝置直線運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移動裝置直線運動
    * @param [in] distance 直線運動距離（mm）
    * @param [in] vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    int TractorMoveL(double distance, double vel);

可移動裝置圓弧運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移動裝置圓弧運動
    * @param [in] radio 圓弧運動半徑（mm）
    * @param [in] angle 圓弧運動角度（°）
    * @param [in] vel 直線運動速度百分比（0-100）
    * @return 錯誤碼
    */
    int TractorMoveC(double radio, double angle, double vel);

可移動裝置停止運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移動裝置停止運動
    * @return 錯誤碼
    */
    int TractorStop();

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//udp擴展軸通訊
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);

        robot.TractorEnable(false);
        robot.Sleep(2000);
        robot.TractorEnable(true);
        robot.Sleep(2000);
        robot.TractorHoming();

        robot.Sleep(2000);
        robot.TractorMoveL(100, 20);
        robot.Sleep(5000);
        robot.TractorMoveL(-100, 20);
        robot.Sleep(5000);
        robot.TractorMoveC(300, 90, 20);
        robot.Sleep(2000);
        robot.TractorStop();//小车停止
        robot.TractorMoveC(300, -90, 20);
    }

獲取擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取擴展軸座標系
    * @param [out] coord 擴展軸座標系
    * @return 錯誤碼
    */
    int ExtAxisGetCoord(DescPose coord);