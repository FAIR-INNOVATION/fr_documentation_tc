其他接口
================

.. toctree:: 
    :maxdepth: 5

獲取SSH公鑰
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取SSH公鑰
    * @param [out] keygen 公鑰
    * @return 錯誤碼
    */
    int GetSSHKeygen(String[] keygen)

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

計算指定路徑下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 計算指定路徑下文件的MD5值
    * @param [in] file_path 文件路徑包含文件名，默認Traj文件夾路徑爲:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 錯誤碼
    */
    int ComputeFileMD5(String file_path, String[] md5)

機器人SSH、MD5指令代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSSHMd5(Robot robot)
    {
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
        return 0;
    }

設置機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置機器人 20004 端口反饋週期
    * @param [in] period 機器人 20004 端口反饋週期(ms)
    * @return  錯誤碼
    */
    public int SetRobotRealtimeStateSamplePeriod(int period)

獲取機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人 20004 端口反饋週期
    * @return  List[0]:錯誤碼; List[1]:機器人 20004 端口反饋週期(ms)
    */
    public List<Integer> GetRobotRealtimeStateSamplePeriod()

機器人20004端口狀態反饋週期配置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRealtimePeriod(Robot robot)
    {
        robot.SetRobotRealtimeStateSamplePeriod(10);
        List<Integer> getPeriod = new ArrayList<>();
        getPeriod=robot.GetRobotRealtimeStateSamplePeriod();
        robot.Sleep(1000);

        return 0;
    }

機器人軟件升級
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 機器人軟件升級
     * @param [in] filePath 軟件升級包全路徑
     * @param [in] block 是否阻塞至升級完成 true:阻塞；false:非阻塞
     * @return  錯誤碼
     */
    public int SoftwareUpgrade(String filePath, boolean block)

獲取機器人軟件升級狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人軟件升級狀態
    * @return  List[0]:錯誤碼; List[1]:機器人軟件升級狀態 0-空閒中或上傳升級包中；1~100：升級完成百分比；-1:升級軟件失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓失敗；-5：用戶配置升級失敗；-6：外設配置升級失敗；-7：擴展軸配置升級失敗；-8：機器人配置升級失敗；-9：DH參數配置升級失敗
    */
    public List<Integer> GetSoftwareUpgradeState()

機器人軟件升級代碼示例
+++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestUpgrade(Robot robot)
    {
        robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", false);
        while (true)
        {
            List<Integer> inter=new ArrayList<>();
            inter=robot.GetSoftwareUpgradeState();
            System.out.println("upgrade state is:"+ inter.get(1));
            robot.Sleep(300);
        }
    }

下載點位表數據庫
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下載點位表數據庫 
    * @param [in] pointTableName 要下載的點位表名稱    pointTable1.db
    * @param [in] saveFilePath 下載點位表的存儲路徑   C://test/
    * @return 錯誤碼 
    */
    int PointTableDownLoad(String pointTableName, String saveFilePath);

上傳點位表數據庫
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上傳點位表數據庫 
    * @param [in] pointTableFilePath 上傳點位表的全路徑名   C://test/pointTable1.db
    * @return 錯誤碼 
    */
    int PointTableUpLoad(String pointTableFilePath);

點位表更新lua文件
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 點位表更新lua文件
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db",當點位表爲空，即""時，表示將lua程序更新爲未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名稱   "testPointTable.lua"
    * @param [out] errorStr 切換點位表錯誤信息
    * @return 錯誤碼 
    */
    int PointTableUpdateLua(String pointTableName, String luaFileName, String errorStr);

機器人點位表操作代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPointTable(Robot robot)
    {
        String save_path = "D://zDOWN/";
        String point_table_name = "point_table_FR5.db";
        int rtn = robot.PointTableDownLoad(point_table_name, save_path);

        String upload_path = "D://zUP/point_table_FR5.db";
        rtn = robot.PointTableUpLoad(upload_path);

        String point_tablename = "point_table_FR5.db";
        String lua_name = "airlab.lua";
        String err="";
        rtn = robot.PointTableUpdateLua(point_tablename, lua_name,err);

        robot.CloseRPC();
        return 0;
    }

控制器日誌下載
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 控制器日誌下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
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
    * @param [in] savePath 保存文件路徑"D://zDown/"
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
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return 錯誤碼
    */
    int DataPackageDownload(String savePath);

下載控制器數據代碼示例
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestDownLoadRobotData(Robot robot)
    {
        int rtn = robot.RbLogDownload("D://zDOWN/");

        rtn = robot.AllDataSourceDownload("D://zDOWN/");

        rtn = robot.DataPackageDownload("D://zDOWN/");
        return 0;
    }

設置編碼器升級
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置編碼器升級
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    int SetEncoderUpgrade(String path)

設置關節固件升級
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置關節固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    public int SetJointFirmwareUpgrade(int type, String path)

設置控制箱固件升級
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置控制箱固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    public int SetCtrlFirmwareUpgrade(int type, String path)

設置末端固件升級
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置末端固件升級
    * @param [in] type 升級文件類型；1-升級固件；2-升級從站配置文件
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    public int SetEndFirmwareUpgrade(int type, String path)

關節全參數配置文件升級
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 關節全參數配置文件升級
    * @param [in] path 本地升級包全路徑(D://zUP/XXXXX.bin)
    * @return 錯誤碼
    */
    public int JointAllParamUpgrade(String path)

機器人從站固件升級代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFirmWareUpgrade(Robot robot)
    {
        robot.RobotEnable(0);
        robot.Sleep(200);
        int rtn = robot.JointAllParamUpgrade("D://zUP/standardQX/jointallparametersFR56.0.db");
        System.out.println("robot JointAllParamUpgrade rtn is:"+ rtn);

        rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Cbd_Asix_V2.0.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade config param rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/upgrade/FAIR_Cobot_Axle_Asix_V2.4.bin");
        System.out.println("robot SetEndFirmwareUpgrade config param rtn is:"+ rtn);

        robot.SetSysServoBootMode();
        rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/standardQX/FR_CTRL_PRIMCU_FV201010_MAIN_U4_T01_20240529.bin");
        System.out.println("robot SetCtrlFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/standardQX/FR_END_FV201010_MAIN_U01_T01_20250522.bin");
        System.out.println("robot SetEndFirmwareUpgrade rtn is:"+ rtn);

        rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/standardQX/FR_SERVO_FV502211_MAIN_U7_T07_20250217.bin");
        System.out.println("robot SetJointFirmwareUpgrade rtn is:"+ rtn);

        robot.CloseRPC();
    }

機器人操作系統升級(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 機器人操作系統升級(LA控制箱)
     * @param [in] filePath 操作系統升級包全路徑
     * @return  錯誤碼
     */
    public int KernelUpgrade(String filePath)

獲取機器人操作系統升級結果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取機器人操作系統升級結果(LA控制箱)
     * @param [out] result 升級結果：0:成功；-1:失敗
     * @return  錯誤碼
     */
    public int GetKernelUpgradeResult(int[] result)