其他接口
================

.. toctree:: 
    :maxdepth: 5

下載點位表資料庫
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下載點位表資料庫 
    * @param [in] pointTableName 要下載的點位表名稱    pointTable1.db
    * @param [in] saveFilePath 下載點位表的儲存路徑   C://test/
    * @return 錯誤碼 
    */
    int PointTableDownLoad(String pointTableName, String saveFilePath);

上傳點位表資料庫
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上傳點位表資料庫 
    * @param [in] pointTableFilePath 上傳點位表的全路徑名   C://test/pointTable1.db
    * @return 錯誤碼 
    */
    int PointTableUpLoad(String pointTableFilePath);

切換點位表並應用
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 切換點位表並應用 
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db"
    * @param [in] errorStr 切換點位表錯誤訊息
    * @return 錯誤碼 
    */
    int PointTableSwitch(String pointTableName, String errorStr);

點位表更新lua文件
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 點位表更新lua文件
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db",當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua檔案名稱   "testPointTable.lua"
    * @param [out] errorStr 切換點位表錯誤訊息
    * @return 錯誤碼 
    */
    int PointTableUpdateLua(String pointTableName, String luaFileName, String errorStr);

代碼範例
+++++++++++++++++++++++++++++++++++
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

        robot.PointTableUpLoad("D://zUP/point_table_test1.db");//點位表上傳
        robot.PointTableDownLoad("point_table_test1.db", "D://zUP/");//點位表下載
        String errStr = "";
        robot.PointTableSwitch("point_table_test1.db", errStr);//切换點位表
        //點位表更新Lua程序
        robot.PointTableUpdateLua("point_table_test2.db", "1010Test.lua", errStr);
    }

初始化日誌參數
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 初始化日誌參數
    * @param [in] logType：輸出模式，DIRECT-直接輸出；BUFFER-緩衝輸出；ASYNC-非同步輸出
    * @param [in] logLevel：日誌過濾等級，ERROR-錯誤；WARNING-警告;INFO-訊息；DEBUG-調試
    * @param [in] filePath: 檔案保存路徑，如“D://Log/”
    * @param [in] saveFileNum：儲存檔案個數，同時超出儲存檔案數量和儲存檔案天數的檔案將被刪除
    * @param [in] saveDays: 儲存檔案天數，同時超出儲存檔案數量和儲存檔案天數的檔案將被刪除
    * @return 錯誤碼
    */
    int LoggerInit(FrLogType logType, FrLogLevel logLevel, String filePath, int saveFileNum, int saveDays);

設定日誌過濾等級
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定日誌過濾等級;
    * @param [in] logLevel: 日誌過濾等級，ERROR-錯誤；WARNING-警告;INFO-訊息；DEBUG-調試
    * @return 錯誤碼
    */
    int SetLoggerLevel(FrLogLevel logLevel);


代碼範例
+++++++++++++++++++++++++++++++++++
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
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        robot.SetLoggerLevel(FrLogLevel.DEBUG);
    }

設置機器人週邊協議
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人週邊協議
    * @param [in] protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int SetExDevProtocol(int protocol);

取得機器人週邊協議
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得機器人週邊協議
    * @return List[0]:錯誤碼; List[1] : int protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

代碼範例
+++++++++++++++++++++++++++++++++++
.. code-block:: console
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

        robot.SetExDevProtocol(4096);
        List<Number> rtnArr =  robot.GetTargetPayload(1);
        rtnArr=GetExDevProtocol();
    }

末端感測器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端感測器配置
    * @param [in] config idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param [in] config idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware 軟體版本，0-J1.0/HuiDe1.0(暫未開放)
    * @param [in] config idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    * @return 錯誤碼
    */
    int AxleSensorConfig(DeviceConfig config);

取得末端傳感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得末端傳感器配置
    * @param [out] config idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param [out] config idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @return 錯誤碼
    */
    int AxleSensorConfigGet(DeviceConfig config);

末端感測器激活
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端感測器激活
    * @param [in] actFlag 0-復位；1-激活
    * @return 錯誤碼
    */
    int AxleSensorActivate(int actFlag);

末端感測器暫存器寫入
+++++++++++++++++++++++++++++++++++
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

代碼範例
+++++++++++++++++++++++++++++++++++
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
        DeviceConfig axleSensorConfig = new DeviceConfig(18, 0, 0, 1);
        robot.AxleSensorConfig(axleSensorConfig);

        DeviceConfig getConfig = new DeviceConfig();
        robot.AxleSensorConfigGet(getConfig);
        System.out.println("company is " + getConfig.company + ",  type is " + getConfig.device);

        robot.AxleSensorActivate(1);

        robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
    }

控制器日誌下載
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 控制器日誌下載
    * @param [in] savePath 保存檔案路徑"D://zDown/"
    * @return 錯誤碼
    */
    int RbLogDownload(String savePath);

所有數據源下載
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 所有數據源下載
    * @param [in] savePath 保存檔案路徑"D://zDown/"
    * @return 錯誤碼
    */
    int AllDataSourceDownload(String savePath);

數據備份包下載
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 數據備份包下載
    * @param [in] savePath 保存檔案路徑"D://zDown/"
    * @return 錯誤碼
    */
    int DataPackageDownload(String savePath);

程式碼範例
+++++++++++++++++++++++++++++++++++
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
        int rtn=0;

        rtn = robot.DataPackageDownload("D://zDOWN/");
        System.out.println("DataPackageDownload rtn is: "+rtn);

        System.out.println("AllDataSourceDownload start");
        rtn = robot.AllDataSourceDownload("D://zDOWN/");
        System.out.println("AllDataSourceDownload rtn is: "+rtn);

        System.out.println("RbLogDownload start");
        rtn = robot.RbLogDownload("D://zDOWN/");
        System.out.println("RbLogDownload rtn is: "+rtn);
    }

下發SCP指令
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /** 
    * @brief 下發SCP指令
    * @param [in] mode 0-上傳（上位機->控制器），1-下載（控制器->上位機）
    * @param [in] sshname 上位機用戶名
    * @param [in] sship 上位機ip地址
    * @param [in] usr_file_url 上位機文件路徑
    * @param [in] robot_file_url 機器人控制器文件路徑
    * @return 錯誤碼
    */
    int SetSSHScpCmd(int mode, String sshname, String sship, String usr_file_url, String robot_file_url)

代碼示例
+++++++++++++++++++++++++++++++++++
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

        String file_path= "/fruser/airlab.lua";
        String[] md5 =new String[]{""};

        String[] ssh_keygen=new String[]{""};
        int retval = robot.GetSSHKeygen(ssh_keygen);
        System.out.println(ssh_keygen[0]);

        String ssh_name = "fr";
        String ssh_ip = "192.168.58.45";
        String ssh_route = "/home/fr";
        String ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        System.out.println("SetSSHScpCmd retval is:"+ retval);
        System.out.println("robot url is:"+ ssh_robot_url);

        robot.ComputeFileMD5(file_path, md5);
        System.out.println("md5 is:+"+ md5[0]);
    }

設置寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置寬電壓控制箱溫度及風扇轉速監控參數
    * @param [in] enable 0-不使能監測；1-使能監測
    * @param [in] period 監測週期(s),範圍1-100
    * @return 錯誤碼
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

獲取寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取寬電壓控制箱溫度及風扇轉速監控參數
    * @return List[0]-錯誤碼,List[1]-enable 0-不使能監測；1-使能監測,List[2]-period 監測週期(s),範圍1-100
    */
    List<Number> GetWideBoxTempFanMonitorParam()