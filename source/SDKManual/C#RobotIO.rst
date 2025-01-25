機器人IO
============

.. toctree:: 
    :maxdepth: 5

設定控制箱數位量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定控制箱數位量輸出
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetDO(int id, byte status, byte smooth, byte block); 

設定工具數位量輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工具數位量輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolDO(int id, byte status, byte smooth, byte block); 

設定控制箱類比輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定控制箱類比輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetAO(int id, float value, byte block); 

設定工具類比輸出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工具類比輸出
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolAO(int id, float value, byte block); 

取得控制箱數位量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得控制箱數位量輸入
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetDI(int id, byte block, ref byte level);

取得工具數位量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得工具數位量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetToolDI(int id, byte block, ref byte level); 

等待控制箱數位量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱數位量輸入
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
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
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitMultiDI(int mode, int id, byte status, int max_time, int opt); 

等待工具數位量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具數位量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolDI(int id, byte status, int max_time, int opt); 

取得控制箱模擬量輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得控制箱模擬量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetAI(int id, byte block, ref float persent); 

取得工具類比輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得工具類比輸入
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetToolAI(int id, byte block, ref float persent);    

取得機器人末端記錄按鈕狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人末端記錄按鈕狀態
    * @param [out] state 按鈕狀態，0-按下，1-放開
    * @return 錯誤碼 
    */ 
    int GetAxlePointRecordBtnState(ref byte state); 

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
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitAI(int id, int sign, float value, int max_time, int opt);   

等待工具類比輸入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具類比輸入
    * @param  [in] id  io編號，範圍[0]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolAI(int id, int sign, float value, int max_time, int opt); 

取得機器人末端DO輸出狀態
++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人末端DO輸出狀態 
    * @param [out] do_state DO輸出狀態，do0~do1對應bit1~bit2,從bit0開始
    * @return 錯誤碼 
    */ 
    int GetToolDO(ref byte do_state);

取得機器控制器DO輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器控制器DO輸出狀態 
    * @param [out] do_state_h DO輸出狀態，co0~co7對應bit0~bit7 
    * @param [out] do_state_l DO輸出狀態，do0~do7對應bit0~bit7
    * @return 錯誤碼 
    */ 
    int GetDO(ref int do_state_h, ref int do_state_l);

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnIOTest_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;
        int i;

        for (i = 0; i < 16; i++)//所有控制器IO輸出置 1
        {
            robot.SetDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        status = 0;

        for (i = 0; i < 16; i++)//所有控制器IO輸出置 0
        {
            robot.SetDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        status = 1;

        for (i = 0; i < 2; i++)//所有工具端IO輸出置 1
        {
            robot.SetToolDO(i, status, smooth, block);
            robot.WaitMs(500);
        }
        status = 0;
        for (i = 0; i < 2; i++)//所有工具端IO輸出置 0
        {
            robot.SetToolDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        value = 50.0f;
        robot.SetAO(0, value, block);//設定控制器0號類比輸出50%
        value = 100.0f;
        robot.SetAO(1, value, block);//設定控制器1號類比輸出100%
        robot.WaitMs(300);
        value = 0.0f;
        robot.SetAO(0, value, block);//設定控制器0號類比輸出0%
        value = 0.0f;
        robot.SetAO(1, value, block);//設定控制器1號類比輸出0%

        value = 100.0f;
        robot.SetToolAO(0, value, block);//設定工具端0號類比輸出100%
        robot.WaitMs(1000);
        value = 0.0f;
        robot.SetToolAO(0, value, block);//設定工具端0號類比輸出0%

        robot.GetDI(0, block, ref di);//取得數字輸入
        Console.WriteLine($"di0 : {di}");
        robot.WaitDI(0, 1, 0, 2);       //等待0號埠數字量輸入1，一直等待
        Console.WriteLine("wait di success");
        robot.WaitMultiDI(0, 3, 0, 10000, 2);   //等待多路與， 0和1端口，輸入置1，等待時間10000ms， 一直等待
        Console.WriteLine("wait multi di success");
        robot.GetToolDI(1, block, ref tool_di);//取得工具端數位量輸入
        Console.WriteLine($"tool_di1 : {tool_di}");
        robot.WaitToolDI(1, 0, 0, 2);          //一直等待
        Console.WriteLine("wait tool di success");
        robot.GetAI(0, block, ref ai);
        Console.WriteLine($"ai0 : {ai}");
        robot.GetAI(1, block, ref ai);
        Console.WriteLine($"ai1 : {ai}");
        robot.WaitAI(0, 1, 50.0f, 0, 2);    //等待0號口， 小於 ， %50， 一直等待
        Console.WriteLine("wait ai success");
        robot.WaitToolAI(0, 1, 50, 0, 2);   //一直等待
        Console.WriteLine("wait tool ai success");
        robot.GetToolAI(0, block, ref tool_ai);
        Console.WriteLine($"tool_ai0 : {tool_ai}");
    }
    
取得機器人軟體版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人軟體版本信息
    * @param [out] robotModel 機器人型號
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 錯誤碼 
    */ 
    int GetSoftwareVersion(ref string robotModel, ref string webVersion, ref string controllerVersion);
    
取得機器人硬體版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人硬體版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱載板硬體版本
    * @param [out] driver1Version 驅動器1硬體版本
    * @param [out] driver1Version 驅動器2硬體版本
    * @param [out] driver1Version 驅動器3硬體版本
    * @param [out] driver1Version 驅動器4硬體版本
    * @param [out] driver1Version 驅動器5硬體版本
    * @param [out] driver1Version 驅動器6硬體版本
    * @param [out] endBoardVersion 端板硬體版本
    * @return 錯誤碼 
    */ 
    int GetHardwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

取得機器人韌體版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人韌體版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱載板韌體版本
    * @param [out] driver1Version 驅動器1韌體版本
    * @param [out] driver1Version 驅動器2韌體版本
    * @param [out] driver1Version 驅動器3韌體版本
    * @param [out] driver1Version 驅動器4韌體版本
    * @param [out] driver1Version 驅動器5韌體版本
    * @param [out] driver1Version 驅動器6韌體版本
    * @param [out] endBoardVersion 末端板韌體版本
    * @return 錯誤碼 
    */ 
    int GetFirmwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnGetVersions_Click(object sender, EventArgs e)
    {
        string[] ver = new string[20];
        int rtn = 0;
        rtn = robot.GetSoftwareVersion(ref ver[0], ref ver[1], ref ver[2]);
        rtn = robot.GetHardwareVersion(ref ver[3], ref ver[4], ref ver[5], ref ver[6], ref ver[7], ref ver[8], ref ver[9], ref ver[10]);
        rtn = robot.GetFirmwareVersion(ref ver[11], ref ver[12], ref ver[13], ref ver[14], ref ver[15], ref ver[16], ref ver[17], ref ver[18]);
        Console.WriteLine($"robotmodel  is: {ver[0]}");
        Console.WriteLine($"webVersion  is: {ver[1]}");
        Console.WriteLine($"controllerVersion  is: {ver[2]}");
        Console.WriteLine($"Hard ctrlBox Version  is: {ver[3]}");
        Console.WriteLine($"Hard driver1 Version  is: {ver[4]}");
        Console.WriteLine($"Hard driver2 Version  is: {ver[5]}");
        Console.WriteLine($"Hard driver3 Version  is: {ver[6]}");
        Console.WriteLine($"Hard driver4 Version  is: {ver[7]}");
        Console.WriteLine($"Hard driver5 Version  is: {ver[8]}");
        Console.WriteLine($"Hard driver6 Version  is: {ver[9]}");
        Console.WriteLine($"Hard end Version  is: {ver[10]}");
        Console.WriteLine($"Firm ctrlBox Version  is: {ver[11]}");
        Console.WriteLine($"Firm driver1 Version  is: {ver[12]}");
        Console.WriteLine($"Firm driver2 Version  is: {ver[13]}");
        Console.WriteLine($"Firm driver3 Version  is: {ver[14]}");
        Console.WriteLine($"Firm driver4 Version  is: {ver[15]}");
        Console.WriteLine($"Firm driver5 Version  is: {ver[16]}");
        Console.WriteLine($"Firm driver6 Version  is: {ver[17]}");
        Console.WriteLine($"Firm end Version  is: {ver[18]}");
    }