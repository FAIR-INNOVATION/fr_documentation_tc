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
    robot.ProgramLoad("test.lua");
    robot.ProgramRun();
    robot.Sleep(2000);
    robot.PauseMotion();
    robot.Sleep(2000);
    robot.ResumeMotion();
    robot.Sleep(2000);
    robot.CloseRPC();
    return 0;
    }

設置控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱可配置CI端口功能
    * @param [in] config CI0-CI7功能編碼；
    * 0-無;1-起弧成功;2-焊機準備;3-傳送帶檢測;4-暫停;5-恢復;6-啟動;7-停止;
    8-暫停/恢復;9-啟動/停止;10-腳踏拖動;11-移至作業原點;12-手自動切換;
    13-焊絲尋位成功;14-運動中斷;15-啟動主程序;16-啟動倒帶;17-啟動確認;
    18-光電檢測信號X;19-光電檢測信號Y;20-外部急停輸入信號1;21-外部急停輸入信號2;
    22-一級縮減模式;23-二級縮減模式;24-三級縮減模式(停止);25-恢復焊接;26-終止焊接;
    27-輔助拖動開啟;28-輔助拖動關閉;29-輔助拖動開啟/關閉;30-清除所有錯誤;
    31-手自動切換(高低電平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定點跟蹤開始/結束
    * @return 錯誤碼
    */
    errno_t SetDIConfig(int config[8]);

獲取控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱可配置CI端口功能
    * @param [in] config CI0-CI7功能編碼；
    * 0-無;1-起弧成功;2-焊機準備;3-傳送帶檢測;4-暫停;5-恢復;6-啟動;7-停止;
    8-暫停/恢復;9-啟動/停止;10-腳踏拖動;11-移至作業原點;12-手自動切換;
    13-焊絲尋位成功;14-運動中斷;15-啟動主程序;16-啟動倒帶;17-啟動確認;
    18-光電檢測信號X;19-光電檢測信號Y;20-外部急停輸入信號1;21-外部急停輸入信號2;
    22-一級縮減模式;23-二級縮減模式;24-三級縮減模式(停止);25-恢復焊接;26-終止焊接;
    27-輔助拖動開啟;28-輔助拖動關閉;29-輔助拖動開啟/關閉;30-清除所有錯誤;
    31-手自動切換(高低電平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定點跟蹤開始/結束
    * @return 錯誤碼
    */
    errno_t GetDIConfig(int config[8]);

設置控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱可配置CO端口功能
    * @param [out] config CO0-CO7功能編碼；
    * 0-無;1-機器人報錯;2-機器人運動中;3-噴塗啟停;4-噴塗清槍;5-送氣信號;6-起弧信號;7-點動送絲;
    8-反向送絲;9-JOB輸入口1;10-JOB輸入口2;11-JOB輸入口3;12-傳送帶啟停控制;13-機器人暫停中;14-到達作業原點;
    15-到達干涉區;16-焊絲尋位啟停控制;17-機器人啟動完成;18-程序啟動停止;19-自動手動模式;20-急停輸出信號1-安全;
    21-急停輸出信號2-安全;22-LUA腳本程序運行停止;23-安全狀態輸出-安全;24-保護性停止狀態輸出-安全;
    25-機器人運動中-安全;26-機器人縮減模式-安全;27-機器人非縮減模式-安全;28-機器人非停止;29-機器人報錯-指令點錯誤;
    30-機器人報錯-驅動器錯誤;31-機器人報錯-超出軟限位錯誤;32-機器人報錯-碰撞錯誤;33-機器人報錯-活動從站數量錯誤;
    34-機器人報錯-從站錯誤;35-機器人報錯-IO錯誤;36-機器人報錯-夾爪錯誤;37-機器人報錯-文件錯誤;38-機器人報錯-奇異位姿錯誤;
    39-機器人報錯-驅動器通信錯誤;40-機器人報錯-參數錯誤;41-機器人報錯-外部軸超出軟限位錯誤;42-機器人警告-警告;
    43-機器人警告-安全門警告;44-機器人警告-運動警告;45-機器人警告-干涉區警告;46-機器人警告-安全牆警告;
    47-使能狀態;48-斷線自動抬升中;49-立方體1干涉警告;50-立方體2干涉警告;51-立方體3干涉警告;52-立方體4干涉警告;
    * @return 錯誤碼
    */
    errno_t SetDOConfig(int config[8]);

獲取控制箱可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱可配置CO端口功能
    * @param [out] config CO0-CO7功能編碼；
    * 0-無;1-機器人報錯;2-機器人運動中;3-噴塗啟停;4-噴塗清槍;5-送氣信號;6-起弧信號;7-點動送絲;
    8-反向送絲;9-JOB輸入口1;10-JOB輸入口2;11-JOB輸入口3;12-傳送帶啟停控制;13-機器人暫停中;14-到達作業原點;
    15-到達干涉區;16-焊絲尋位啟停控制;17-機器人啟動完成;18-程序啟動停止;19-自動手動模式;20-急停輸出信號1-安全;
    21-急停輸出信號2-安全;22-LUA腳本程序運行停止;23-安全狀態輸出-安全;24-保護性停止狀態輸出-安全;
    25-機器人運動中-安全;26-機器人縮減模式-安全;27-機器人非縮減模式-安全;28-機器人非停止;29-機器人報錯-指令點錯誤;
    30-機器人報錯-驅動器錯誤;31-機器人報錯-超出軟限位錯誤;32-機器人報錯-碰撞錯誤;33-機器人報錯-活動從站數量錯誤;
    34-機器人報錯-從站錯誤;35-機器人報錯-IO錯誤;36-機器人報錯-夾爪錯誤;37-機器人報錯-文件錯誤;38-機器人報錯-奇異位姿錯誤;
    39-機器人報錯-驅動器通信錯誤;40-機器人報錯-參數錯誤;41-機器人報錯-外部軸超出軟限位錯誤;42-機器人警告-警告;
    43-機器人警告-安全門警告;44-機器人警告-運動警告;45-機器人警告-干涉區警告;46-機器人警告-安全牆警告;
    47-使能狀態;48-斷線自動抬升中;49-立方體1干涉警告;50-立方體2干涉警告;51-立方體3干涉警告;52-立方體4干涉警告;
    * @return 錯誤碼
    */
    errno_t GetDOConfig(int config[8]);

設置末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端可配置End-CI端口功能
    * @param [in] config End CI0-CI1功能編碼；
    * 0-無;1-拖動示教工具開關;2-點記錄信號;3-手自動切換（脈衝信號）;4-TPD記錄啟動/停止;5-暫停運動;
    6-恢復運動;7-啟動;8-停止;9-暫停/恢復;10-啟動/停止;11-力傳感器輔助拖動開啟;12-力傳感器輔助拖動關閉;
    13-力傳感器輔助拖動開啟/關閉;14-激光檢測信號X;15-激光檢測信號Y;16-PTP運動至作業原點;17-運動中斷，根據信號停止當前運動;
    18-啟動主程序;19-啟動倒帶;20-啟動確認;21-恢復焊接;22-終止焊接;23-清除錯誤;24-手自動切換（高低電平）
    25-使能;26-去使能;27-使能/去使能;28-激光伺服跟蹤啟停信號;
    * @return 錯誤碼
    */
    errno_t SetToolDIConfig(int config[2]);

獲取末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取末端可配置End-CI端口功能
    * @param [out] config End CI0-CI1功能編碼；
    * 0-無;1-拖動示教工具開關;2-點記錄信號;3-手自動切換（脈衝信號）;4-TPD記錄啟動/停止;5-暫停運動;
    6-恢復運動;7-啟動;8-停止;9-暫停/恢復;10-啟動/停止;11-力傳感器輔助拖動開啟;12-力傳感器輔助拖動關閉;
    13-力傳感器輔助拖動開啟/關閉;14-激光檢測信號X;15-激光檢測信號Y;16-PTP運動至作業原點;17-運動中斷，根據信號停止當前運動;
    18-啟動主程序;19-啟動倒帶;20-啟動確認;21-恢復焊接;22-終止焊接;23-清除錯誤;24-手自動切換（高低電平）
    25-使能;26-去使能;27-使能/去使能;28-激光伺服跟蹤啟停信號;
    * @return 錯誤碼
    */
    errno_t GetToolDIConfig(int config[2]);
    
設置控制箱可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱可配置CI有效狀態
    * @param [in] config CI0-CI7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t SetDIConfigLevel(int config[8]);
        
獲取控制箱可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱可配置CI有效狀態
    * @param [out] config CI0-CI7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t GetDIConfigLevel(int config[8]);
        
設置控制箱可配置CO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱可配置CO有效狀態
    * @param [in] config CO0-CO7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t SetDOConfigLevel(int config[8]);

獲取控制箱可配置CO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱可配置CO有效狀態
    * @param [out] config CO0-CO7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t GetDOConfigLevel(int config[8]);
    
設置末端可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置末端可配置CI有效狀態
    * @param [in] config CI0-CI1端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t SetToolDIConfigLevel(int config[2]);
    
獲取末端可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取末端可配置CI有效狀態
    * @param [out] config CI0-CI1端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t GetToolDIConfigLevel(int config[2]);
    
設置控制箱標準DI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱標準DI有效狀態
    * @param [in] config DI0-DI7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t SetStandardDILevel(int config[8]);
    
獲取控制箱標準DI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱標準DI有效狀態
    * @param [out] config DI0-DI7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t GetStandardDILevel(int config[8]);

設置控制箱標準DO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置控制箱標準DO有效狀態
    * @param [in] config DO0-DO7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t SetStandardDOLevel(int config[8]);
    
獲取控制箱標準DO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取控制箱標準DO有效狀態
    * @param [out] config DO0-DO7端口有效狀態；0-高電平有效；1-低電平有效
    * @return 錯誤碼
    */
    errno_t GetStandardDOLevel(int config[8]);
        
機器人IO配置代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestIOConfig()
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
        int setDIConfig[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int getDIConfig[8] = { 0 };
        rtn = robot.SetDIConfig(setDIConfig);
        printf("SetDIConfig rtn is %d\n", rtn);
        rtn = robot.GetDIConfig(getDIConfig);
        printf("GetDIConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn, 
            getDIConfig[0], getDIConfig[1], getDIConfig[2], getDIConfig[3], getDIConfig[4], getDIConfig[5], getDIConfig[6], getDIConfig[7]);
        int setDOConfig[8] = { 9, 10, 11, 12, 13, 14, 15, 16 };
        int getDOConfig[8] = { 0 };
        rtn = robot.SetDOConfig(setDOConfig);
        printf("SetDOConfig rtn is %d\n", rtn);
        rtn = robot.GetDOConfig(getDOConfig);
        printf("GetDOConfig rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfig[0], getDOConfig[1], getDOConfig[2], getDOConfig[3], getDOConfig[4], getDOConfig[5], getDOConfig[6], getDOConfig[7]);
        int setToolDIConfig[2] = { 17, 18 };
        int getToolDIConfig[2] = { 0 };
        rtn = robot.SetToolDIConfig(setToolDIConfig);
        printf("SetToolDIConfig rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfig(getToolDIConfig);
        printf("GetToolDIConfig rtn is %d, value is %d %d \n", rtn, getToolDIConfig[0], getToolDIConfig[1]);
        int setDIConfigLevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getDIConfigLevel[8] = { 0 };
        rtn = robot.SetDIConfigLevel(setDIConfigLevel);
        printf("SetDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDIConfigLevel(getDIConfigLevel);
        printf("GetDIConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDIConfigLevel[0], getDIConfigLevel[1], getDIConfigLevel[2], getDIConfigLevel[3], getDIConfigLevel[4], getDIConfigLevel[5], getDIConfigLevel[6], getDIConfigLevel[7]);
        int setDOConfigLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getDOConfigLevel[8] = { 0 };
        rtn = robot.SetDOConfigLevel(setDOConfigLevel);
        printf("SetDOConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetDOConfigLevel(getDOConfigLevel);
        printf("GetDOConfigLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getDOConfigLevel[0], getDOConfigLevel[1], getDOConfigLevel[2], getDOConfigLevel[3], getDOConfigLevel[4], getDOConfigLevel[5], getDOConfigLevel[6], getDOConfigLevel[7]);
        int setToolDIConfigLevel[2] = { 1, 0 };
        int getToolDIConfigLevel[2] = { 0 };
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel);
        printf("SetToolDIConfigLevel rtn is %d\n", rtn);
        rtn = robot.GetToolDIConfigLevel(getToolDIConfigLevel);
        printf("GetToolDIConfigLevel rtn is %d, value is %d %d \n", rtn, getToolDIConfigLevel[0], getToolDIConfigLevel[1]);
        int setStandardDILevel[8] = { 1, 1, 1, 1, 0, 0, 0, 0 };
        int getStandardDILevel[8] = { 0 };
        rtn = robot.SetStandardDILevel(setStandardDILevel);
        printf("SetStandardDILevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDILevel(getStandardDILevel);
        printf("GetStandardDILevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDILevel[0], getStandardDILevel[1], getStandardDILevel[2], getStandardDILevel[3], getStandardDILevel[4], getStandardDILevel[5], getStandardDILevel[6], getStandardDILevel[7]);
        int setStandardDOLevel[8] = { 0, 0, 0, 0, 1, 1, 1, 1 };
        int getStandardDOLevel[8] = { 0 };
        rtn = robot.SetStandardDOLevel(setStandardDOLevel);
        printf("SetStandardDOLevel rtn is %d\n", rtn);
        rtn = robot.GetStandardDOLevel(getStandardDOLevel);
        printf("GetStandsrdDOLevel rtn is %d, value is %d %d %d %d %d %d %d %d \n", rtn,
            getStandardDOLevel[0], getStandardDOLevel[1], getStandardDOLevel[2], getStandardDOLevel[3], getStandardDOLevel[4], getStandardDOLevel[5], getStandardDOLevel[6], getStandardDOLevel[7]);
        robot.Sleep(2000);
        robot.CloseRPC();
        robot.Sleep(1000);
        return 0;
    }