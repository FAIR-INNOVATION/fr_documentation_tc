其他接口
=================

.. toctree:: 
    :maxdepth: 5

獲取SSH公鑰
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取SSH公鑰
    * @param [out] keygen 公鑰
    * @return 錯誤碼
    */
    errno_t GetSSHKeygen(char keygen[1024]);

下發SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
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
    errno_t SetSSHScpCmd(int mode, char sshname[32], char sship[32], char usr_file_url[128], char robot_file_url[128]);

計算指定路徑下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 計算指定路徑下文件的MD5值
    * @param [in] file_path 文件路徑包含文件名，默認Traj文件夾路徑爲:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 錯誤碼
    */
    errno_t ComputeFileMD5(char file_path[256], char md5[256]);

機器人SSH、MD5指令代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSSHMd5(void)
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
      char file_path[256] = "/fruser/airlab.lua";
      char md5[256] = { 0 };
      uint8_t emerg_state = 0;
      uint8_t si0_state = 0;
      uint8_t si1_state = 0;
      int sdk_com_state = 0;
      char ssh_keygen[1024] = { 0 };
      int retval = robot.GetSSHKeygen(ssh_keygen);
      printf("GetSSHKeygen retval is: %d\n", retval);
      printf("ssh key is: %s \n", ssh_keygen);
      char ssh_name[32] = "fr";
      char ssh_ip[32] = "192.168.58.45";
      char ssh_route[128] = "/home/fr";
      char ssh_robot_url[128] = "/root/robot/dhpara.config";
      retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
      printf("SetSSHScpCmd retval is: %d\n", retval);
      printf("robot url is: %s\n", ssh_robot_url);
      robot.ComputeFileMD5(file_path, md5);
      printf("md5 is: %s \n", md5);
      robot.CloseRPC();
      return 0;
    }

設置機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置機器人 20004 端口反饋週期
    * @param [in] period 機器人 20004 端口反饋週期(ms)
    * @return 錯誤碼
    */
    errno_t SetRobotRealtimeStateSamplePeriod(int period);

獲取機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人 20004 端口反饋週期
    * @param [out] period 機器人 20004 端口反饋週期(ms)
    * @return 錯誤碼
    */
    errno_t GetRobotRealtimeStateSamplePeriod(int& period);

機器人20004端口狀態反饋週期配置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestRealtimePeriod(void)
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
      robot.SetRobotRealtimeStateSamplePeriod(10);
      int getPeriod = 0;
      robot.GetRobotRealtimeStateSamplePeriod(getPeriod);
      cout << "period is " << getPeriod << endl;
      robot.Sleep(1000);
      robot.CloseRPC();
      return 0;
    }


機器人軟件升級
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 機器人軟件升級
    * @param [in] filePath 軟件升級包全路徑
    * @param [in] block 是否阻塞至升級完成 true:阻塞；false:非阻塞
    * @return 錯誤碼
    */
    errno_t SoftwareUpgrade(std::string filePath, bool block);

獲取機器人軟件升級狀態
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人軟件升級狀態
    * @param [out] state 機器人軟件包升級狀態(0-空閒中或上傳升級包中；1~100：升級完成百分比；-1:升級軟件失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓失敗；-5：用戶配置升級失敗；-6：外設配置升級失敗；-7：擴展軸配置升級失敗；-8：機器人配置升級失敗；-9：DH參數配置升級失敗)
    * @return 錯誤碼
    */
    errno_t GetSoftwareUpgradeState(int &state);

機器人軟件升級代碼示例
+++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestUpgrade(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(3);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SoftwareUpgrade("D://zUP/QNX/software.tar.gz", false);
      while (true)
      {
        int curState = -1;
        robot.GetSoftwareUpgradeState(curState);
        printf("upgrade state is %d\n", curState);
        robot.Sleep(300);
      }
      robot.CloseRPC();
      return 0;
    }

下載點位表數據庫
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下載點位表數據庫
    * @param [in] pointTableName 要下載的點位表名稱    pointTable1.db
    * @param [in] saveFilePath 下載點位表的存儲路徑   C://test/
    * @return 錯誤碼
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

上傳點位表數據庫
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳點位表數據庫
    * @param [in] pointTableFilePath 上傳點位表的全路徑名   C://test/pointTable1.db
    * @return 錯誤碼
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

點位表更新lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 點位表更新lua文件
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db",當點位表爲空，即""時，表示將lua程序更新爲未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名稱   "testPointTable.lua"
    * @param [out] errorStr 切換點位表錯誤信息
    * @return 錯誤碼
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

機器人點位表操作代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestPointTable(void)
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
      string save_path = "D://zDOWN/";
      string point_table_name = "point_table_FR5.db";
      rtn = robot.PointTableDownLoad(point_table_name, save_path);
      cout << "download : " << point_table_name << " fail: " << rtn << endl;
      string upload_path = "D://zUP/point_table_FR5.db";
      rtn = robot.PointTableUpLoad(upload_path);
      cout << "retval is: " << rtn << endl;
      string point_tablename = "point_table_FR5.db";
      string lua_name = "airlab.lua";
      rtn = robot.PointTableUpdateLua(point_tablename, lua_name);
      cout << "retval is: " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

控制器日誌下載
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制器日誌下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return 錯誤碼
    */
    errno_t RbLogDownload(std::string savePath);

所有數據源下載
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 所有數據源下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return 錯誤碼
    */
    errno_t AllDataSourceDownload(std::string savePath);

數據備份包下載
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 數據備份包下載
    * @param [in] savePath 保存文件路徑"D://zDown/"
    * @return 錯誤碼
    */
    errno_t DataPackageDownload(std::string savePath);

下載控制器數據代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestDownLoadRobotData(void)
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
      rtn = robot.RbLogDownload("D://zDOWN/");
      cout << "RbLogDownload rtn is " << rtn << endl;
      rtn = robot.AllDataSourceDownload("D://zDOWN/");
      cout << "AllDataSourceDownload rtn is " << rtn << endl;
      rtn = robot.DataPackageDownload("D://zDOWN/");
      cout << "DataPackageDownload rtn is " << rtn << endl;
      robot.CloseRPC();
      return 0;
    }

