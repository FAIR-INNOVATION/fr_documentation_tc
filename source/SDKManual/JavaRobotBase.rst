機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  機器人接口類構造函數
    */
    Robot robot = new Robot(); 

與控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  與機器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出場默認爲192.168.58.2
    * @return 錯誤碼
    */
    int RPC(String ip);

與機器人關閉通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 與機器人關閉通信
    * @return 錯誤碼 
    */ 
    int CloseRPC(); 

查詢SDK版本號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 查詢 SDK 版本號 
    * @return 版本號 
    */  
    String GetSDKVersion();

獲取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取控制器IP
    * @param  [out] ip  控制器IP
    * @return  錯誤碼
    */
    int GetControllerIP(String[] ip);

控制機器人進入或退出拖動示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制機器人進入或退出拖動示教模式
    * @param  [in] state 0-退出拖動示教模式，1-進入拖動示教模式
    * @return  錯誤碼
    */
    int DragTeachSwitch(int state);

查詢機器人是否處於拖動示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查詢機器人是否處於拖動示教模式
    * @param  [in] state 0-非拖動示教模式，1-拖動示教模式
    * @return  錯誤碼
    */
    int IsInDragTeach(List<Number> state);

控制機器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制機器人上使能或下使能，機器人上電後默認自動上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  錯誤碼
    */
    int RobotEnable(int state); 

控制機器人手自動模式切換
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制機器人手自動模式切換
    * @param [in] mode 0-自動模式，1-手動模式
    * @return 錯誤碼
    */
    int Mode(int mode);

關閉機器人操作系統
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 關閉機器人操作系統
    * @return 錯誤碼
    */
    int ShutDownRobotOS();

設置與機器人通訊重連參數
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置與機器人通訊重連參數
    * @param [in] enable 是否使能，true:使能，false:不使能
    * @param [in] times 重連次數
    * @param [in] period 重連時間間隔
    * @return 錯誤碼
    */
    int SetReconnectParam(boolean enable, int times, int period);

初始化日誌參數
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 初始化日誌參數
    * @param [in] logType 輸出模式，DIRECT-直接輸出；BUFFER-緩衝輸出；ASYNC-異步輸出
    * @param [in] logLevel 日誌過濾等級，ERROR-錯誤；WARNING-警告;INFO-信息；DEBUG-調試
    * @param [in] filePath 文件保存路徑，如“D://Log/”
    * @param [in] saveFileNum 保存文件個數，同時超出保存文件個數和保存文件天數的文件將被刪除
    * @param [in] saveDays 保存文件天數，同時超出保存文件個數和保存文件天數的文件將被刪除
    * @return 錯誤碼
    */
    int LoggerInit(FrLogType logType, FrLogLevel logLevel, String filePath, int saveFileNum, int saveDays)

設置日誌過濾等級
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置日誌過濾等級
    * @param [in] logLevel 日誌過濾等級，ERROR-錯誤；WARNING-警告;INFO-信息；DEBUG-調試
    * @return 錯誤碼
    */
    int SetLoggerLevel(FrLogLevel logLevel)

機器人基礎控制代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);
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
        String[] ip={""};
        String version = "";
        version=robot.GetSDKVersion();
        System.out.println("SDK version : " + version);
        int rtn = robot.GetControllerIP(ip);
        System.out.println("controller ip : " +  ip[0] + "  " + rtn);
        robot.Mode(1);//1-手動模式  0-自動模式
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);//進入拖動模式
        robot.Sleep(1000);
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        robot.Sleep(1000);
        robot.DragTeachSwitch(0);//退出拖動模式
        robot.Sleep(1000);
        pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        
        if (pkg.robot_state ==4){
           System.out.println("拖動模式");
        }else {
           System.out.println("非拖動模式");
        }
    }

獲取機器人軟件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人軟件版本
    * @param [out] robotModel 機器人型號
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 錯誤碼 
    */
    int GetSoftwareVersion(String robotModel, String webVersion, String controllerVersion);

獲取機器人硬件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人硬件版本
    * @param [out] ctrlBoxBoardVersion 控制箱載板硬件版本
    * @param [out] driver1Version 驅動器1硬件版本
    * @param [out] driver1Version 驅動器2硬件版本
    * @param [out] driver1Version 驅動器3硬件版本
    * @param [out] driver1Version 驅動器4硬件版本
    * @param [out] driver1Version 驅動器5硬件版本
    * @param [out] driver1Version 驅動器6硬件版本
    * @param [out] endBoardVersion 末端板硬件版本
    * @return 錯誤碼 
    */
    int GetHardwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

獲取機器人固件版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人固件版本
    * @param [out] ctrlBoxBoardVersion 控制箱載板固件版本
    * @param [out] driver1Version 驅動器1固件版本
    * @param [out] driver1Version 驅動器2固件版本
    * @param [out] driver1Version 驅動器3固件版本
    * @param [out] driver1Version 驅動器4固件版本
    * @param [out] driver1Version 驅動器5固件版本
    * @param [out] driver1Version 驅動器6固件版本
    * @param [out] endBoardVersion 末端板固件版本
    * @return 錯誤碼 
    */
    int GetFirmwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

獲取機器人軟固件版本代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設置重連次數、間隔
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
        String ctrlBoxBoardVersion = "";
        String driver1Version = "";
        String driver2Version = "";
        String driver3Version = "";
        String driver4Version = "";
        String driver5Version = "";
        String driver6Version = "";
        String endBoardVersion = "";
        robot.GetHardwareVersion(ctrlBoxBoardVersion ,driver1Version,  driver2Version,  driver3Version,
                 driver4Version,  driver5Version,  driver6Version,  endBoardVersion);

        robot.GetFirmwareVersion(ctrlBoxBoardVersion, driver1Version, driver2Version, driver3Version,
                driver4Version, driver5Version, driver6Version, endBoardVersion);
    }