其他接口
================

.. toctree:: 
    :maxdepth: 5

傳動皮帶啟動、停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動皮帶啟動、停止 
    * @param [in] status 狀態，1-啟動，0-停止
    * @return 錯誤碼 
    */ 
    int ConveyorStartEnd(byte status); 

記錄IO檢測點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄IO檢測點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointIORecord(); 

記錄A點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄A點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointARecord();

記錄參考點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄參考點 
    * @return 錯誤碼 
    */ 
    int ConveyorRefPointRecord(); 

記錄B點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄B點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointBRecord();

傳送帶工件IO檢測
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳送帶工件IO檢測 
    * @param [in] max_t 最大檢測時間，單位ms
    * @return 錯誤碼 
    */ 
    int ConveyorIODetect(int max_t);

取得物體目前位置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得物體目前位置 
    * @param [in] mode 1-跟踪抓取，2-跟踪運動，3-TPD跟踪
    * @return 錯誤碼 
    */ 
    int ConveyorGetTrackData(int mode);

傳動皮帶追蹤開始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動皮帶追蹤開始 
    * @param [in] status 狀態，1-啟動，0-停止
    * @return 錯誤碼 
    */
    int ConveyorTrackStart(byte status);

傳動皮帶追蹤停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動皮帶追蹤停止 
    * @return 錯誤碼 
    */
    int ConveyorTrackEnd();

傳動帶參數配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 傳送帶參數配置
    * @param [in] para[0] 編碼器通道 1~2
    * @param [in] para[1] 編碼器轉一圈的脈衝數
    * @param [in] para[2] 編碼器轉一圈傳送帶行走距離
    * @param [in] para[3] 工件座標系編號 針對追蹤運動功能選擇工件座標系編號，追蹤抓取、TPD追蹤設為0
    * @param [in] para[4] 是否配視覺  0 不配  1 配
    * @param [in] para[5] 速度比  針對傳送帶追蹤抓取選項（1-100）  其他選項預設為1 
    * @param [in] followType 追蹤運動類型，0-追蹤運動；1-追檢運動
    * @param [in] startDis 追檢抓取需要設置， 追蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 預設值0
    * @param [in] endDis 追檢抓取需要設置，追蹤終止距離， 單位mm， 預設值100
    * @return 錯誤碼
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis=0, int endDis=100);

設定傳動皮帶抓取點補償
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定傳動皮帶抓取點補償 
    * @param [in] cmp 補償位置 double[3]{x, y, z}
    * @return 錯誤碼 
    */
    int ConveyorCatchPointComp(double[] cmp);

傳送帶追蹤直線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳送帶追蹤直線運動 
    * @param [in] name 運動點名稱
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] wobj 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm  
    * @return 錯誤碼 
    */
    int ConveyorTrackMoveL(string name, int tool, int wobj, float vel, float acc, float ovl, float blendR);

代碼範例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnConvert_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose pos1 = new DescPose(0, 0, 0, 0 ,0 ,0);
        DescPose pos2 = new DescPose(0, 0, 0, 0, 0, 0);

        pos1.tran.x = -351.175;
        pos1.tran.y = 3.389;
        pos1.tran.z = 431.172;
        pos1.rpy.rx = -179.111;
        pos1.rpy.ry = -0.241;
        pos1.rpy.rz = 90.388;

        pos2.tran.x = -333.654;
        pos2.tran.y = -229.003;
        pos2.tran.z = 404.335;
        pos2.rpy.rx = -179.139;
        pos2.rpy.ry = -0.779;
        pos2.rpy.rz = 91.269;
        int rtn = -1;

        double[] cmp = new double[3] { 0, 9.99, 0};
        rtn = robot.ConveyorCatchPointComp(cmp);
        if(rtn != 0)
        {
            return;
        }
        Console.WriteLine($"ConveyorCatchPointComp: rtn  {rtn}");

        rtn = robot.MoveCart(pos1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.ConveyorIODetect(10000);
        Console.WriteLine($"ConveyorIODetect: rtn  {rtn}");

        robot.ConveyorGetTrackData(1);
        rtn = robot.ConveyorTrackStart(1);
        Console.WriteLine($"ConveyorTrackStart: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 59, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd: rtn  {rtn}");

        rtn = robot.MoveCart(pos2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 100, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");
    }

取得SSH公鑰
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得SSH公鑰 
    * @param [out] keygen 公鑰
    * @return 錯誤碼 
    */
    int GetSSHKeygen(ref string keygen);

計算指定路徑下檔案的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算指定路徑下檔案的MD5值 
    * @param [in] file_path 檔案路徑包含檔名，預設Traj資料夾路徑為:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 錯誤碼 
    */
    int ComputeFileMD5(string file_path, ref string md5);

取得機器人急停狀態
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人急停狀態 
    * @param [out] state 急停狀態，0-非急停，1-急停
    * @return 錯誤碼 
    */
    int GetRobotEmergencyStopState(ref byte state);

取得SDK與機器人的通訊狀態
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得SDK與機器人的通訊狀態 
    * @param [out] state 通訊狀態，0-通訊正常，1-通訊異常
    * @return 錯誤碼 
    */
    int GetSDKComState(ref int state)

取得安全停止訊號
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得安全停止訊號 
    * @param [out] si0_state 安全停止訊號SI0，0-無效，1-有效
    * @param [out] si1_state 安全停止訊號SI1，0-無效，1-有效
    * @return 錯誤碼 
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state)

取得機器人DH參數補償值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人DH參數補償值 
    * @param [out] dhCompensation 機器人DH參數補償值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 錯誤碼 
    */
    int GetDHCompensation(ref double[] dhCompensation)

代碼範例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnTestOthers_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        double[] dhCompensation = new double[6]{0,0,0,0,0,0};
        rtn = robot.GetDHCompensation(ref dhCompensation);
        Console.WriteLine($"GetDHCompensation:  rtn :{rtn}    {dhCompensation[0]}  {dhCompensation[1]}  {dhCompensation[2]}  {dhCompensation[3]}  {dhCompensation[4]}  {dhCompensation[5]}");
        string ssh = "";
        rtn = robot.GetSSHKeygen(ref ssh);
        Console.WriteLine($"GetSSHKeygen:  ssh {ssh}  rtn  {rtn}");
        string file_path = "/fruser/test.txt";
        string md5 = "";
        robot.ComputeFileMD5(file_path, ref md5);

        byte state = 255;
        rtn = robot.GetRobotEmergencyStopState(ref state);
        Console.WriteLine($"GetRobotEmergencyStopState:  rtn  {rtn}   state {state}");

        int comState = -1;
        rtn = robot.GetSDKComState(ref comState);
        Console.WriteLine($"GetSDKComState:  rtn  {rtn}   state  {comState}");

        byte si0_state = 255;
        byte si1_state = 255;

        rtn = robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState:  rtn  {rtn}   si0_state  {si0_state}   si1_state  {si1_state}");
    }

上傳點位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 點位表從本地電腦上傳至機器人控制器 
    * @param [in] pointTableFilePath 點位表在本機的絕對路徑C://test/pointTabl e1.db
    * @return 錯誤碼 
    */
    int PointTableUpLoad(string pointTableFilePath);

下載點位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 點位表從機器人控制器下載到本地計算機 
    * @param [in] pointTableName 控制器中的點位表名稱：pointTable1.db
    * @param [in] saveFilePath 點位表下載到電腦的路徑 C://test/
    * @return 錯誤碼 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

點位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用給定的點位表更新Lua程式中的點
    * @param [in] pointTableName 控制器中的點位表名稱："pointTable1.db", 當點位表為空，即""時，表示將lua程序更新為未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua檔案名稱   "test.lua"
    * @param [out] errorStr 點位表更新lua錯誤訊息  
    * @return 錯誤碼 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

代碼範例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        rtn = robot.PointTableUpLoad("C://point_table_test.db");
        Thread.Sleep(2000);
        rtn = robot.PointTableDownLoad("point_table_test.db", "D://zDOWN/");
        string errorStr = "";
        rtn = robot.PointTableUpdateLua("point_table_test.db", "test.lua", ref errorStr);
        Console.WriteLine($"PointTableSwitch rtn  is {rtn}" + errorStr);
        rtn = robot.ProgramLoad("/fruser/test.lua");
        rtn = robot.ProgramRun();
    }

初始化日誌參數
+++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
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
    public int LoggerInit(FrLogType logType = FrLogType.DIRECT, FrLogLevel logLevel = FrLogLevel.ERROR, string filePath = "", int saveFileNum = 10, int saveDays = 10);

設定日誌過濾等級
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定日誌過濾等級;
    * @param [in] logLevel: 日誌過濾等級，ERROR-錯誤；WARNING-警告;INFO-訊息；DEBUG-調試
    * @return 錯誤碼
    */
    public int SetLoggerLevel(FrLogLevel logLevel);


代碼範例
+++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnTestLog_Click(object sender, EventArgs e)
    {
        robot = new Robot();//實例化機器人對象
        robot.RPC("192.168.58.2"); //與控制箱建立連接
        string path = "D://log/";
        robot.LoggerInit(FrLogType.ASYNC, FrLogLevel.DEBUG, path, 5, 5);
        robot.SetLoggerLevel(FrLogLevel.INFO);
    }

設置機器人週邊協議
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置機器人週邊協議
    * @param [in] protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int SetExDevProtocol(int protocol);

取得機器人週邊協議
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人週邊協議
    * @param [out] protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int GetExDevProtocol(ref int protocol);

代碼範例
++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: console
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int protocol = 4098;//ModbusMaster 
        robot.SetExDevProtocol(protocol);

        robot.GetExDevProtocol(ref protocol);
        Console.Writeline("protocol is" + protocol);
    }

末端感測器配置
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 末端感應器配置
 * @param [in] idCompany 廠商，18-JUNKONG；25-HUIDE
 * @param [in] idDevice 類型，0-JUNKONG/RYR6T.V1.0
 * @param [in] idSoftware 軟體版本，0-J1.0/HuiDe1.0(暫未開放)
 * @param [in] idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
 * @return 錯誤碼
 */
 int AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

取得末端感測器配置
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得末端感測器配置
 * @param [out] idCompany 廠商，18-JUNKONG；25-HUIDE
 * @param [out] idDevice 類型，0-JUNKONG/RYR6T.V1.0
 * @return 錯誤碼
 */
 int AxleSensorConfigGet(ref int idCompany, ref int idDevice);

末端感測器激活
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 末端感應器激活
 * @param [in] actFlag 0-重設；1-激活
 * @return 錯誤碼
 */
 int AxleSensorActivate(int actFlag);

末端感測器暫存器寫入
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 末端感測器暫存器寫入
 * @param [in] devAddr 裝置位址編號 0-255
 * @param [in] regHAddr 暫存器位址高8位
 * @param [in] regLAddr 暫存器位址低8位
 * @param [in] regNum 暫存器個數 0-255
 * @param [in] data1 寫入暫存器數值1
 * @param [in] data2 寫入暫存器數值2
 * @param [in] isNoBlock 0-阻塞；1-非阻塞
 * @return 錯誤碼
 */
 int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

程式範例
+++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 private void button2_Click_1(object sender, EventArgs e)
 {
 robot.AxleSensorConfig(18, 0, 0, 1);
 int company = -1;
 int type = -1;
 robot.AxleSensorConfigGet(ref company, ref type);
 Console.WriteLine($"company is {company}, type is {type}");
 robot.AxleSensorActivate(1);
 robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
 }
 
控制器日誌下載
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制器日誌下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return  錯誤碼
    */
    int RbLogDownload(string savePath);

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {  
        Console.WriteLine("RbLogDownload start");
        int rtn = robot.RbLogDownload(@"D:\zDOWN1\");
        Console.WriteLine($"RbLogDownload rtn is {rtn}");
    }

所有數據源下載
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 所有數據源下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return  錯誤碼
    */
    int AllDataSourceDownload(string savePath);

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        Console.WriteLine("AllDataSourceDownload start");
        int rtn = robot.AllDataSourceDownload(@"D:\zDOWN\");
        Console.WriteLine($"AllDataSourceDownload rtn is {rtn}");
    }

數據備份包下載
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 數據備份包下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return  錯誤碼
    */
    int DataPackageDownload(string savePath);

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        Console.WriteLine("DataPackageDownload start");
        int rtn = robot.DataPackageDownload(@"D:\zDOWN\");
        Console.WriteLine($"DataPackageDownload rtn is {rtn}");
    }

獲取控制箱SN碼
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取控制箱SN碼
    * @param [out] SNCode 控制箱SN碼
    * @return 錯誤碼
    */
    int GetRobotSN(string SNCode);

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        string SN = "";
        int rtn = robot.GetRobotSN(ref SN); 
        Console.WriteLine($"robot SN is {SN}");
    }

關閉機器人操作系統
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關閉機器人操作系統
    * @return 錯誤碼
    */
    int ShutDownRobotOS();

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgse)
    {   
        int rtn = robot.ShutDownRobotOS();
        Console.WriteLine($"ShutDownRobotOS rtn is {rtn}");
    }