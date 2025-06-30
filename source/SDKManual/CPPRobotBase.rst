機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  機器人接口類構造函數
    */
    FRRobot();

與控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  與機器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出廠默認為192.168.58.2
    * @return 錯誤碼
    */
    errno_t  RPC(const char *ip);

與控制器關閉通訊
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  與機器人控制器關閉通訊
     * @return 錯誤碼
     */
    errno_t  CloseRPC();

查詢SDK版本號
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢SDK版本號
    * @param  [out] version   SDK版本號
    * @return  錯誤碼
    */  
    errno_t  GetSDKVersion(char *version);

獲取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取控制器IP
    * @param  [out] ip  控制器IP
    * @return  錯誤碼
    */
    errno_t  GetControllerIP(char *ip);

控制機器人進入或退出拖動示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制機器人進入或退出拖動示教模式
    * @param  [in] state 0-退出拖動示教模式，1-進入拖動示教模式
    * @return  錯誤碼
    */
    errno_t  DragTeachSwitch(uint8_t state);

查詢機器人是否處於拖動模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢機器人是否處於拖動示教模式
    * @param  [out] state 0-非拖動示教模式，1-拖動示教模式
    * @return  錯誤碼
    */
    errno_t  IsInDragTeach(uint8_t *state);

控制機器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制機器人上使能或下使能，機器人上電後默認自動上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  錯誤碼
    */
    errno_t  RobotEnable(uint8_t state);

控制機器人手自動模式切換
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制機器人手自動模式切換
    * @param [in] mode 0-自動模式，1-手動模式
    * @return 錯誤碼
    */
    errno_t  Mode(int mode);

關閉機器人操作系統
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 關閉機器人操作系統
    * @return 錯誤碼
    */
    errno_t ShutDownRobotOS();

設置與機器人通訊重連參數
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置與機器人通訊重連參數
    * @param [in] enable 網絡故障時使能重連 true-使能 false-不使能
    * @param [in] reconnectTime 重連時間，單位ms
    * @param [in] period 重連周期，單位ms
    * @return 錯誤碼
    */
    errno_t SetReConnectParam(bool enable, int reconnectTime = 30000, int period = 50);

初始化日誌參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 初始化日誌參數;
    * @param output_model：輸出模式，0-直接輸出；1-緩衝輸出；2-異步輸出;
    * @param file_path: 文件保存路徑+名稱，,長度上限256，名稱必須是xxx.log的形式，比如/home/fr/linux/fairino.log;
    * @param file_num：滾動存儲的文件數量，1~20個.單個文件上限50M;
    * @return errno_t 錯誤碼;
    */
    errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

設置日誌過濾等級
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置日誌過濾等級;
    * @param lvl: 過濾等級值，值越小輸出日誌越少，默認值是1. 1-error, 2-warning, 3-info, 4-debug;
    */
    void SetLoggerLevel(int lvl = 1);

機器人基礎控制代碼示例
++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestRobotCtrl(void)
     {
         ROBOT_STATE_PKG pkg = {};
         FRRobot robot;
         robot.LoggerInit();
         robot.SetLoggerLevel(1);
         int rtn = robot.RPC("192.168.58.2");
         robot.SetReConnectParam(true, 30000, 500);
         char ip[64] = "";
         char version[64] = "";
         uint8_t state;
         robot.GetSDKVersion(version);
         printf("SDK version:%s\n", version);
         robot.GetControllerIP(ip);
         printf("controller ip:%s\n", ip);
         robot.Mode(1);
         robot.Sleep(1000);
         robot.DragTeachSwitch(1);
         robot.Sleep(1000);
         robot.IsInDragTeach(&state);
         printf("drag state :%u\n", state);
         robot.Sleep(3000);
         robot.DragTeachSwitch(0);
         robot.Sleep(1000);
         robot.IsInDragTeach(&state);
         printf("drag state :%u\n", state);
         robot.Sleep(3000);
         robot.RobotEnable(0);
         robot.Sleep(3000);
         robot.RobotEnable(1);
         robot.Mode(0);
         robot.Sleep(1000);
         robot.Mode(1);
         robot.Sleep(3000);
         robot.ShutDownRobotOS();
         robot.CloseRPC();
         return 0;
     }

獲取機器人軟件版本代碼示例
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人軟件版本
    * @param[out]    robotModel 機器人型號
    * @param[out]    webversion web版本
    * @param[out]    controllerVersion 控制器版本
    * @return 錯誤碼
    */
    errno_t GetSoftwareVersion(char robotModel[64], char webVersion[64], char controllerVersion[64]);

獲取機器人硬件版本
+++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人硬件版本
    * @param[out] ctrlBoxBoardversion 控制箱載板硬件版本
    * @param[out] driver1version 驅動器1硬件版本
    * @param[out] driver2version 驅動器2硬件版本
    * @param[out] driver3version 驅動器3硬件版本
    * @param[out] driver4version 驅動器4硬件版本
    * @param[out] driver5version 驅動器5硬件版本
    * @param[out] driver6version 驅動器6硬件版本
    * @param[out] endBoardversion 末端版硬件版本
    */
    errno_t GetHardwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

獲取機器人固件版本
+++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取機器人固件版本
    * @param[out] ctrlBoxBoardversion 控制箱載板固件版本
    * @param[out] driver1version 驅動器1固件版本
    * @param[out] driver2version 驅動器2固件版本
    * @param[out] driver3version 驅動器3固件版本
    * @param[out] driver4version 驅動器4固件版本
    * @param[out] driver5version 驅動器5固件版本
    * @param[out] driver6version 驅動器6固件版本
    * @param[out] endBoardversion 末端版固件版本
    */
    errno_t GetFirmwareVersion(char ctrlBoxBoardversion[128], char driver1version[128], char driver2version[128], char driver3version[128], char driver4version[128], char driver5version[128], char driver6version[128], char endBoardversion[128]);

獲取機器人軟固件版本代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestGetVersions(void)
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
         char robotModel[64] = { 0 };
         char webversion[64] = { 0 };
         char controllerVersion[64] = { 0 };
         char ctrlBoxBoardversion[128] = { 0 };
         char driver1version[128] = { 0 };
         char driver2version[128] = { 0 };
         char driver3version[128] = { 0 };
         char driver4version[128] = { 0 };
         char driver5version[128] = { 0 };
         char driver6version[128] = { 0 };
         char endBoardversion[128] = { 0 };
         rtn = robot.GetSoftwareVersion(robotModel, webversion, controllerVersion);
         printf("Getsoftwareversion rtn is: %d\n", rtn);
         printf("robotmodel is: %s, webversion is: %s, controllerVersion is: %s \n\n", robotModel, webversion, controllerVersion);
         rtn = robot.GetHardwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetHardwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         rtn = robot.GetFirmwareVersion(ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         printf("GetFirmwareversion rtn is: %d\n", rtn);
         printf("GetHardwareversion get hardware versoin is: %s, %s, %s, %s, %s, %s, %s, %s\n\n", ctrlBoxBoardversion, driver1version, driver2version, driver3version, driver4version, driver5version, driver6version, endBoardversion);
         robot.CloseRPC();
         return 0;
     }