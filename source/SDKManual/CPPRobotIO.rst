機器人 IO
============

.. toctree::
    :maxdepth: 5

設置控制箱數字量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 設置控制箱數字量輸出
    @param [in] id io 編號，範圍 [0~15]
    @param [in] status 0 - 關，1 - 開
    @param [in] smooth 0 - 不平滑， 1 - 平滑
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @return 錯誤碼
    */
    errno_t SetDO (int id, uint8_t status, uint8_t smooth, uint8_t block);

設置工具數字量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 設置工具數字量輸出
    @param [in] id io 編號，範圍 [0~1]
    @param [in] status 0 - 關，1 - 開
    @param [in] smooth 0 - 不平滑， 1 - 平滑
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @return 錯誤碼
    */
    errno_t SetToolDO (int id, uint8_t status, uint8_t smooth, uint8_t block);

設置控制箱模擬量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 設置控制箱模擬量輸出
    @param [in] id io 編號，範圍 [0~1]
    @param [in] value 電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mA] 或電壓 [0~10V]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @return 錯誤碼
    */
    errno_t SetAO (int id, float value, uint8_t block);

設置工具模擬量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 設置工具模擬量輸出
    @param [in] id io 編號，範圍 [0]
    @param [in] value 電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mA] 或電壓 [0~10V]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @return 錯誤碼
    */
    errno_t SetToolAO (int id, float value, uint8_t block);

設置數字量、模擬量輸出代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAODO(void)
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
    uint8_t status = 1;
    uint8_t smooth = 0;
    uint8_t block = 0;
    for (int i = 0; i < 16; i++)
    {
    robot.SetDO(i, status, smooth, block);
    robot.Sleep(300);
    }
    status = 0;
    for (int i = 0; i < 16; i++)
    {
    robot.SetDO(i, status, smooth, block);
    robot.Sleep(300);
    }
    status = 1;
    for (int i = 0; i < 2; i++)
    {
    robot.SetToolDO(i, status, smooth, block);
    robot.Sleep(1000);
    }
    status = 0;
    for (int i = 0; i < 2; i++)
    {
    robot.SetToolDO(i, status, smooth, block);
    robot.Sleep(1000);
    }
    for (int i = 0; i < 100; i++)
    {
    robot.SetAO(0, i * 40.96, block);
    robot.Sleep(30);
    }
    for (int i = 0; i < 100; i++)
    {
    robot.SetToolAO(0, i * 40.96, block);
    robot.Sleep(30);
    }
    robot.CloseRPC();
    return 0;
    }

獲取控制箱數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取控制箱數字量輸入
    @param [in] id io 編號，範圍 [0~15]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @param [out] result 0 - 低電平，1 - 高電平
    @return 錯誤碼
    */
    errno_t GetDI(int id, uint8_t block, uint8_t *result);

獲取工具數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取工具數字量輸入
    @param [in] id io 編號，範圍 [0~1]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @param [out] result 0 - 低電平，1 - 高電平
    @return 錯誤碼
    */
    errno_t GetToolDI(int id, uint8_t block, uint8_t *result);

獲取控制箱模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取控制箱模擬量輸入
    @param [in] id io 編號，範圍 [0~1]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @param [out] result 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mS] 或電壓 [0~10V]
    @return 錯誤碼
    */
    errno_t GetAI(int id, uint8_t block, float *result);

獲取工具模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取工具模擬量輸入
    @param [in] id io 編號，範圍 [0]
    @param [in] block 0 - 阻塞，1 - 非阻塞
    @param [out] result 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mS] 或電壓 [0~10V]
    @return 錯誤碼
    */
    errno_t GetToolAI(int id, uint8_t block, float *result);

獲取機器人末端點記錄按鈕狀態
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取機器人末端點記錄按鈕狀態
    @param [out] state 按鈕狀態，0 - 按下，1 - 鬆開
    @return 錯誤碼
    */
    errno_t GetAxlePointRecordBtnState (uint8_t *state);

獲取機器人末端 DO 輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取機器人末端 DO 輸出狀態
    @param [out] do_state DO 輸出狀態，do0~do1 對應 bit1~bit2, 從 bit0 開始
    @return 錯誤碼
    */
    errno_t GetToolDO (uint8_t *do_state);

獲取機器人控制器 DO 輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 獲取機器人控制器 DO 輸出狀態
    @param [out] do_state_h DO 輸出狀態，co0~co7 對應 bit0~bit7
    @param [out] do_state_l DO 輸出狀態，do0~do7 對應 bit0~bit7
    @return 錯誤碼
    */
    errno_t GetDO (uint8_t *do_state_h, uint8_t *do_state_l);

獲取機器人 DI、DO 狀態代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestGetDIAI(void)
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
    uint8_t status = 1;
    uint8_t smooth = 0;
    uint8_t block = 0;
    uint8_t di = 0, tool_di = 0;
    float ai = 0.0, tool_ai = 0.0;
    float value = 0.0;
    robot.GetDI(0, block, &di);
    printf("di0:%u\n", di);
    tool_di = robot.GetToolDI(1, block, &tool_di);
    printf("tool_di1:%u\n", tool_di);
    robot.GetAI(0, block, &ai);
    printf("ai0:%f\n", ai);
    tool_ai = robot.GetToolAI(0, block, &tool_ai);
    printf("tool_ai0:%f\n", tool_ai);
    uint8_t _button_state = 0;
    robot.GetAxlePointRecordBtnState(&_button_state);
    printf("_button_state is: %u\n", _button_state);
    uint8_t tool_do_state = 0;
    robot.GetToolDO(&tool_do_state);
    printf("tool DO state is: %u\n", tool_do_state);
    uint8_t do_state_h = 0;
    uint8_t do_state_l = 0;
    robot.GetDO(&do_state_h, &do_state_l);
    printf("DO state high is: %u \n DO state low is: %u\n", do_state_h, do_state_l);
    robot.CloseRPC();
    return 0;
    }

等待控制箱數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 等待控制箱數字量輸入
    @param [in] id io 編號，範圍 [0~15]
    @param [in] status 0 - 關，1 - 開
    @param [in] max_time 最大等待時間，單位 ms
    @param [in] opt 超時後策略，0 - 程序停止並提示超時，1 - 忽略超時提示程序繼續執行，2 - 一直等待
    @return 錯誤碼
    */
    errno_t WaitDI (int id, uint8_t status, int max_time, int opt);

等待控制箱多路數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 等待控制箱多路數字量輸入
    @param [in] mode 0 - 多路與，1 - 多路或
    @param [in] id io 編號，bit0~bit7 對應 DI0~DI7，bit8~bit15 對應 CI0~CI7
    @param [in] status 0 - 關，1 - 開
    @param [in] max_time 最大等待時間，單位 ms
    @param [in] opt 超時後策略，0 - 程序停止並提示超時，1 - 忽略超時提示程序繼續執行，2 - 一直等待
    @return 錯誤碼
    */
    errno_t WaitMultiDI (int mode, int id, uint8_t status, int max_time, int opt);

等待工具數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 等待工具數字量輸入
    @param [in] id io 編號，範圍 [0~1]
    @param [in] status 0 - 關，1 - 開
    @param [in] max_time 最大等待時間，單位 ms
    @param [in] opt 超時後策略，0 - 程序停止並提示超時，1 - 忽略超時提示程序繼續執行，2 - 一直等待
    @return 錯誤碼
    */
    errno_t WaitToolDI (int id, uint8_t status, int max_time, int opt);

等待控制箱模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 等待控制箱模擬量輸入
    @param [in] id io 編號，範圍 [0~1]
    @param [in] sign 0 - 大於，1 - 小於
    @param [in] value 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mS] 或電壓 [0~10V]
    @param [in] max_time 最大等待時間，單位 ms
    @param [in] opt 超時後策略，0 - 程序停止並提示超時，1 - 忽略超時提示程序繼續執行，2 - 一直等待
    @return 錯誤碼
    */
    errno_t WaitAI (int id, int sign, float value, int max_time, int opt);

等待工具模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    @brief 等待工具模擬量輸入
    @param [in] id io 編號，範圍 [0]
    @param [in] sign 0 - 大於，1 - 小於
    @param [in] value 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mS] 或電壓 [0~10V]
    @param [in] max_time 最大等待時間，單位 ms
    @param [in] opt 超時後策略，0 - 程序停止並提示超時，1 - 忽略超時提示程序繼續執行，2 - 一直等待
    @return 錯誤碼
    */
    errno_t WaitToolAI (int id, int sign, float value, int max_time, int opt);

等待控制箱數字、模擬輸入信號代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    int TestWaitDIAI(void)
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
    uint8_t status = 1;
    uint8_t smooth = 0;
    uint8_t block = 0;
    uint8_t di = 0, tool_di = 0;
    float ai = 0.0, tool_ai = 0.0;
    float value = 0.0;
    rtn = robot.WaitDI(0, 1, 1000, 1);
    cout << "WaitDI over; rtn is: " << rtn << endl;
    robot.WaitMultiDI(1, 3, 3, 1000, 1);
    cout << "WaitDI over; rtn is: " << rtn << endl;
    robot.WaitToolDI(1, 1, 1000, 1);
    cout << "WaitDI over; rtn is: " << rtn << endl;
    robot.WaitAI(0, 0, 50, 1000, 1);
    cout << "WaitDI over; rtn is: " << rtn << endl;
    robot.WaitToolAI(0, 0, 50, 1000, 1);
    cout << "WaitDI over; rtn is: " << rtn << endl;
    robot.CloseRPC();
    return 0;
    }

設置控制箱DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱DO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return 錯誤碼
    */
    errno_t SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag = 0);

設置控制箱AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱AO停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return 錯誤碼
    */
    errno_t SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag = 0);

設置末端工具DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端工具DO停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return 錯誤碼
    */
    errno_t SetOutputResetAxleDO(int resetFlag, int reloadFlag = 0);

設置末端工具AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端工具AO停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return  錯誤碼
    */
    errno_t SetOutputResetAxleAO(int resetFlag, int reloadFlag = 0);

設置擴展DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展DO停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return  錯誤碼
    */
    errno_t SetOutputResetExtDO(int resetFlag, int reloadFlag = 0);

設置擴展AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置擴展AO停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return  錯誤碼
    */
    errno_t SetOutputResetExtAO(int resetFlag, int reloadFlag = 0);

設置SmartTool停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置SmartTool停止/暫停後輸出是否復位
    * @param [in] resetFlag  0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重加載，0-不加載；1-加載
    * @return  錯誤碼
    */
    errno_t SetOutputResetSmartToolDO(int resetFlag, int reloadFlag = 0);

設置LUA程序停止/暫停後輸出復位程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestDOReset(void)
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
    for (int i = 0; i < 16; i++)
    {
        robot.SetDO(i, 1, 0, 0);
        robot.Sleep(200);
    }
    int resetFlag = 0;
    int resumeReloadFlag = 0;
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);
    robot.ProgramLoad("/fruser/test.lua");
    robot.ProgramRun();
    robot.Sleep(2000);
    robot.PauseMotion();
    robot.Sleep(2000);
    robot.ResumeMotion();
    robot.Sleep(2000);
    robot.CloseRPC();
    return 0;
    }