其他接口
================

.. toctree:: 
    :maxdepth: 5

獲取SSH公鑰
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取SSH公鑰 
    * @param [out] keygen 公鑰
    * @return 錯誤碼 
    */
    int GetSSHKeygen(ref string keygen);

下發SCP指令
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
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
    int SetSSHScpCmd(int mode, string sshname, string sship, string usr_file_url, string robot_file_url);

計算指定路徑下文件的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算指定路徑下文件的MD5值 
    * @param [in] file_path 文件路徑包含文件名，默認Traj文件夾路徑爲:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 錯誤碼 
    */
    int ComputeFileMD5(string file_path, ref string md5);

機器人SSH、MD5指令代碼示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        string file_path = "/fruser/airlab.lua";
        string md5 = "";
        byte emerg_state = 0;
        byte si0_state = 0;
        byte si1_state = 0;
        int sdk_com_state = 0;

        string ssh_keygen = "";
        int retval = robot.GetSSHKeygen(ref ssh_keygen);
        Console.WriteLine("GetSSHKeygen retval is: {0}", retval);
        Console.WriteLine("ssh key is: {0}", ssh_keygen);

        string ssh_name = "fr";
        string ssh_ip = "192.168.58.45";
        string ssh_route = "/home/fr";
        string ssh_robot_url = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        Console.WriteLine("SetSSHScpCmd retval is: {0}", retval);
        Console.WriteLine("robot url is: {0}", ssh_robot_url);

        robot.ComputeFileMD5(file_path, ref md5);
        Console.WriteLine("md5 is: {0}", md5);
    }

設置機器人 20004 端口反饋週期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人 20004 端口反饋週期
    * @param [in] period 機器人 20004 端口反饋週期(ms)
    * @return 錯誤碼
    */
    int SetRobotRealtimeStateSamplePeriod(int period);

獲取機器人 20004 端口反饋週期
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人 20004 端口反饋週期
    * @param [out] period 機器人 20004 端口反饋週期(ms)
    * @return 錯誤碼
    */
    int GetRobotRealtimeStateSamplePeriod((ref int period);   

機器人20004端口狀態反饋週期配置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button47_Click(object sender, EventArgs e)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        int getPeriod = 0;
        robot.GetRobotRealtimeStateSamplePeriod(ref getPeriod);
        Console.WriteLine("period is {0}", getPeriod);
        Thread.Sleep(1000);
    }

機器人軟件升級
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 機器人軟件升級
    * @param [in] filePath 軟件升級包全路徑
    * @param [in] block 是否阻塞至升級完成 true:阻塞；false:非阻塞
    * @return  錯誤碼
    */
    int SoftwareUpgrade(string filePath, bool block);

獲取機器人軟件升級狀態
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取機器人軟件升級狀態
    * @param [out] state 機器人軟件包升級狀態  0-空閒中或上傳升級包中；1~100：升級完成百分比；-1:升級軟件失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓失敗；-5：用戶配置升級失敗；-6：外設配置升級失敗；-7：擴展軸配置升級失敗；-8：機器人配置升級失敗；-9：DH參數配置升級失敗
    * @return  錯誤碼
    */
    int GetSoftwareUpgradeState(ref int state);

機器人軟件升級代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button48_Click(object sender, EventArgs e)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            int curState = -1;
            robot.GetSoftwareUpgradeState(ref curState);
            Console.WriteLine("upgrade state is {0}", curState);
            Thread.Sleep(300);
        }
    }

下載點位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 點位表從機器人控制器下載到本地計算機 
    * @param [in] pointTableName 控制器中的點位表名稱：pointTable1.db
    * @param [in] saveFilePath 點位表下載到計算機的路徑 C://test/
    * @return 錯誤碼 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

上傳點位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 點位表從本地計算機上傳至機器人控制器 
    * @param [in] pointTableFilePath 點位表在本地計算機的絕對路徑C://test/pointTabl e1.db
    * @return 錯誤碼 
    */
    int PointTableUpLoad(string pointTableFilePath);

點位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用給定的點位表更新lua程序中的點
    * @param [in] pointTableName 控制器中的點位表名稱："pointTable1.db", 當點位表爲空，即""時，表示將lua程序更新爲未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名稱   "test.lua"
    * @param [out] errorStr 點位表更新lua錯誤信息  
    * @return 錯誤碼 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

切換點位表並應用
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 切換點位表並應用
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db"
    * @param [out] errorStr 切換點位表錯誤信息   
    * @return 錯誤碼 
    */
    int PointTableSwitch(string pointTableName, ref string errorStr);

機器人點位表操作代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        string save_path = "D://zDOWN/";
        string point_table_name = "test_point_A.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);
        Console.WriteLine("download : {0} fail: {1}", point_table_name, rtn);

        string upload_path = "D://zUP/test_point_A.db";
        rtn = robot.PointTableUpLoad(upload_path);
        Console.WriteLine("retval is: {0}", rtn);

        string point_tablename = "test_point_A.db";
        string lua_name = "Text1.lua";

        string errorStr = "";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name, ref errorStr);
        Console.WriteLine("retval is: {0}", rtn);
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

下載控制器數據代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button50_Click(object sender, EventArgs e)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");
        Console.WriteLine("RbLogDownload rtn is {0}", rtn);

        rtn = robot.AllDataSourceDownload("D://zDOWN/");
        Console.WriteLine("AllDataSourceDownload rtn is {0}", rtn);

        rtn = robot.DataPackageDownload("D://zDOWN/");
        Console.WriteLine("DataPackageDownload rtn is {0}", rtn);
    }

機器人操作系統升級(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 機器人操作系統升級(LA控制箱)
     * @param [in] filePath 操作系統升級包全路徑
     * @return  錯誤碼
     */
    public int KernelUpgrade(string filePath)

獲取機器人操作系統升級結果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取機器人操作系統升級結果(LA控制箱)
     * @param [out] result 升級結果：0:成功；-1:失敗
     * @return  錯誤碼
     */
    public int GetKernelUpgradeResult(ref int[] result)

設置編碼器升級
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置編碼器升級
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int SetEncoderUpgrade(string path);

設置關節固件升級
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置關節固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int SetJointFirmwareUpgrade(int type, string path);

設置控制箱固件升級
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置控制箱固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int SetCtrlFirmwareUpgrade(int type, string path);

設置末端固件升級
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置末端固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int SetEndFirmwareUpgrade(int type, string path);

關節全參數配置文件升級
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節全參數配置文件升級
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int JointAllParamUpgrade(string path);

機器人從站固件升級代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    private void button83_Click(object sender, EventArgs e)
    {
        robot.RobotEnable(0);
        Thread.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/jointallparameters.db");
        Console.WriteLine($"robot JointAllParamUpgrade rtn is{rtn}");
        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/upgrade/FR_CTRL_PRIMCU_FV201212_MAIN_U4_T01_20250428(MT).bin");
        Console.WriteLine($"robot SetCtrlFirmwareUpgrade rtn is{rtn}");
        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/upgrade/FR_END_FV201009_MAIN_U1_T01_20250428.bin");
        Console.WriteLine($"robot SetEndFirmwareUpgrade rtn is {rtn}");
        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/upgrade/FR_SERVO_FV504214_MAIN_U7_T07_20250519.bin");
        Console.WriteLine($"robot SetJointFirmwareUpgrade rtn is{rtn}");
    }

機器人MCU日誌生成
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 機器人MCU日誌生成
    * @return 錯誤碼
    */
    public int RobotMCULogCollect();

設置端口通訊斷開時停止機器人運行
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 設置端口通訊斷開時停止機器人運行
    * @param [in] portID 端口編號 0-8080；1-8083；2-20002；3-20004
    * @param [in] enable 0-關閉；1-開啟
    * @param [in] confirmTime 通訊中斷確認時長(ms)[0-5000]
    * @return  錯誤碼
    */
    public int SetRobotStopOnComDisc(int portID, bool enable, int confirmTime)

獲取端口通訊斷開時停止機器人運行參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 獲取端口通訊斷開時停止機器人運行參數
    * @param [in] portID 端口編號 0-8080；1-8083；2-20002；3-20004
    * @param [out] enable 0-關閉；1-開啟
    * @param [out] confirmTime 通訊中斷確認時長(ms)[0-5000]
    * @return  錯誤碼
    */
    public int GetRobotStopOnComDisc(int portID, ref bool enable, ref int confirmTime)
    
端口通訊斷開時停止機器人運行參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:
    
    void TestRobotStopOnComDisc()
    {
        int rtn = 0;

        // 設置四個端口的參數
        rtn = robot.SetRobotStopOnComDisc(0, true, 330);
        rtn = robot.SetRobotStopOnComDisc(1, true, 550);
        rtn = robot.SetRobotStopOnComDisc(2, true, 110);
        rtn = robot.SetRobotStopOnComDisc(3, true, 220);
        Console.WriteLine($"SetRobotStopOnComDisc {rtn}");

        bool enable = false;
        int confirmTime = 0;

        // 獲取並打印每個端口的設置
        robot.GetRobotStopOnComDisc(0, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(1, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 8083 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(2, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

        robot.GetRobotStopOnComDisc(3, ref enable, ref confirmTime);
        Console.WriteLine($"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {(enable ? 1 : 0)}; confirm time is {confirmTime}");

    }

UDP發送指令幀
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief UDP發送指令幀
    * @param [in] 指令幀
    * @return 錯誤碼
    */
    public int SendUDPFrame(string frame)
        
基於UDP通訊的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void TestRobotUDP()
    {
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[UDP響應] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };


        //發送幀
        string frameToSend = "/f/bIII52III236III7IIIMode(1)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII52III236III7IIIMode(0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII41III201III153IIIMoveJ(53.857,-89.441,119.453,-22.664,61.059,3.369,-54.249,-491.930,375.396,96.474,-6.896,-7.783,0,0,100,100,100,0.000,0.000,0.000,0.000,-1,0,0,0,0,0,0,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII42III203III163IIIMoveL(81.736,-85.284,114.974,-23.261,88.746,6.799,125.744,-506.570,375.396,96.474,-6.896,-7.783,0,0,100,100,100,-1,0,0.000,0.000,0.000,0.000,0,0,0,0,0,0,0,0,100,0)III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);
        frameToSend = "/f/bIII47III400III15IIIGetMCVersion(1)III/b/f/f/bIII48III424III21IIIGetSlaveFirmVersion()III/b/f";
        robot.SendUDPFrame(frameToSend);
        Thread.Sleep(2000);

    }
        
設置用戶自定義機器人末端燈色
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置用戶自定義機器人末端燈色
    * @param [in] r 末端紅燈控制；0-滅；1-亮
    * @param [in] g 末端綠燈控制；0-滅；1-亮
    * @param [in] b 末端藍燈控制；0-滅；1-亮
    * @return 錯誤碼
    */
    public int SetUserLEDColor(bool r, bool g, bool b)
            
設置用戶自定義機器人末端燈色的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void testled()
    {
        robot.SetUserLEDColor(true, true, true);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(true, false, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, true, false);
        robot.Sleep(1000);
        robot.SetUserLEDColor(false, false, true);
    }