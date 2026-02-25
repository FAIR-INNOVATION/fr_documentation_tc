機器人IO
============

.. toctree:: 
    :maxdepth: 5

設置控制箱數字量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置控制箱數字量輸出
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetDO(int id, byte status, byte smooth, byte block); 

設置工具數字量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置工具數字量輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolDO(int id, byte status, byte smooth, byte block); 

設置控制箱模擬量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置控制箱模擬量輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetAO(int id, float value, byte block); 

設置工具模擬量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置工具模擬量輸出
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolAO(int id, float value, byte block);

設置數字量、模擬量輸出代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos: 

    private void button14_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;


        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 0;

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, status, smooth, block);
            Thread.Sleep(300);
        }

        status = 1;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        status = 0;

        for (int i = 0; i < 2; i++)
        {
            robot.SetToolDO(i, status, smooth, block);
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetAO(0, i, block);
            Thread.Sleep(30);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetToolAO(0, i, block);
            Thread.Sleep(30);
        }

    }

獲取控制箱數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取控制箱數字量輸入
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetDI(int id, byte block, ref byte level);

獲取工具數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取工具數字量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetToolDI(int id, byte block, ref byte level); 

獲取控制箱模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取控制箱模擬量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetAI(int id, byte block, ref float persent); 

獲取工具模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取工具模擬量輸入
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetToolAI(int id, byte block, ref float persent); 

獲取機器人末端記錄按鈕狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取機器人末端記錄按鈕狀態
    * @param [out] state 按鈕狀態，0-按下，1-鬆開
    * @return 錯誤碼 
    */ 
    int GetAxlePointRecordBtnState(ref byte state); 

獲取機器人末端DO輸出狀態
++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取機器人末端DO輸出狀態 
    * @param [out] do_state DO輸出狀態，do0~do1對應bit1~bit2,從bit0開始 
    * @return 錯誤碼 
    */ 
    int GetToolDO(ref byte do_state);

獲取機器控制器DO輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取機器人控制器DO輸出狀態 
    * @param [out] do_state_h DO輸出狀態，co0~co7對應bit0~bit7 
    * @param [out] do_state_l DO輸出狀態，do0~do7對應bit0~bit7
    * @return 錯誤碼 
    */ 
    int GetDO(ref int do_state_h, ref int do_state_l);   

獲取機器人DI、DO狀態代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button15_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        robot.GetDI(0, block, ref di);
        Console.WriteLine($"di0: {di}");

        tool_di = (byte)robot.GetToolDI(1, block, ref tool_di);
        Console.WriteLine($"tool_di1: {tool_di}");

        robot.GetAI(0, block, ref ai);
        Console.WriteLine($"ai0: {ai}");

        tool_ai = robot.GetToolAI(0, block, ref tool_ai);
        Console.WriteLine($"tool_ai0: {tool_ai}");

        byte _button_state = 0;
        robot.GetAxlePointRecordBtnState(ref _button_state);
        Console.WriteLine($"_button_state is: {_button_state}");

        byte tool_do_state = 0;
        robot.GetToolDO(ref tool_do_state);
        Console.WriteLine($"tool DO state is: {tool_do_state}");

        int do_state_h = 0;
        int do_state_l = 0;
        robot.GetDO(ref do_state_h, ref do_state_l);
        Console.WriteLine($"DO state high is: {do_state_h}\n DO state low is: {do_state_l}");
    }

等待控制箱數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱數字量輸入
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitDI(int id, byte status, int max_time, int opt); 

等待控制箱多路數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱多路數字量輸入
    * @param  [in] mode 0-多路與，1-多路或
    * @param  [in] id  io編號，bit0~bit7對應DI0~DI7，bit8~bit15對應CI0~CI7
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitMultiDI(int mode, int id, byte status, int max_time, int opt); 

等待工具數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具數字量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolDI(int id, byte status, int max_time, int opt); 

等待控制箱模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱模擬量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitAI(int id, int sign, float value, int max_time, int opt);   

等待工具模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具模擬量輸入
    * @param  [in] id  io編號，範圍[0]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolAI(int id, int sign, float value, int max_time, int opt); 

等待控制箱數字、模擬輸入信號代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnIOTest_Click(object sender, EventArgs e)
    {
        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;

        int rtn = robot.WaitDI(0, 1, 1000, 1);
        Console.WriteLine("WaitDI over; rtn is: " + rtn);

        robot.WaitMultiDI(1, 3, 3, 1000, 1);
        Console.WriteLine("WaitMultiDI over; rtn is: " + rtn);

        robot.WaitToolDI(1, 1, 1000, 1);
        Console.WriteLine("WaitToolDI over; rtn is: " + rtn);

        robot.WaitAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitAI over; rtn is: " + rtn);

        robot.WaitToolAI(0, 0, 50, 1000, 1);
        Console.WriteLine("WaitToolAI over; rtn is: " + rtn);
    }
    
設定控制箱DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定控制箱DO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag);

設定控制箱AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定控制箱AO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag);

設定末端工具DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定末端工具DO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetAxleDO(int resetFlag, int reloadFlag);

設定末端工具AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定末端工具AO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetAxleAO(int resetFlag, int reloadFlag);

設定擴展DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定擴展DO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetExtDO(int resetFlag, int reloadFlag);

設定擴展AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定擴展AO停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetExtAO(int resetFlag, int reloadFlag);

設定SmartTool停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定SmartTool停止/暫停後輸出是否復位
    * @param [in] resetFlag 0-不復位；1-復位
    * @param [in] reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetSmartToolDO(int resetFlag, int reloadFlag);

設定LUA程式停止/暫停後輸出復位程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestDOReset()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, 1, 0, 0);
            Thread.Sleep(200);
        }

        int resetFlag = 1;
        int resumeReloadFlag = 1;
        int rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag);
        robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();

        Thread.Sleep(2000);
        robot.PauseMotion();
        Thread.Sleep(2000);
        robot.ResumeMotion();
        Thread.Sleep(2000);
    }