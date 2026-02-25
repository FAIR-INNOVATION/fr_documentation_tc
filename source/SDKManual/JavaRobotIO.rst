機器人IO
============

.. toctree:: 
    :maxdepth: 5

設置控制箱數字量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置控制箱數字量輸出
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetDO(int id, int status, int smooth, int block); 

設置工具數字量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置工具數字量輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolDO(int id, int status, int smooth, int block); 

設置控制箱模擬量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置控制箱模擬量輸出
    * @param  [in] id  id  io編號，範圍[0~1]
    * @param  [in] id  value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] id  block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetAO(int id, double value, int block); 

設置工具模擬量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置工具模擬量輸出
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolAO(int id, double value, int block); 

設置數字量、模擬量輸出代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAODO(Robot robot)
    {

        int status = 1;
        int smooth = 0;
        int block = 0;

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
            robot.SetAO(0, i, block);
            robot.Sleep(30);
        }

        for (int i = 0; i < 100; i++)
        {
            robot.SetToolAO(0, i, block);
            robot.Sleep(30);
        }

        robot.CloseRPC();
        return 0;
    }

獲取控制箱數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取控制箱數字量輸入
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] level  0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetDI(int id, int block, int[] level);

獲取工具數字量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取工具數字量輸入
    * @param  [in] id    io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] level 0-低電平，1-高電平
    * @return  錯誤碼
    */   
    int GetToolDI(int id, int block, int[] level);

獲取控制箱模擬量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取控制箱模擬量輸入
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] persent 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetAI(int id, int block, double[] persent)

獲取工具模擬量輸入
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取工具模擬量輸入
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] persent 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @return  錯誤碼
    */   
    int GetToolAI(int id, int block, double[] persent)

獲取機器人末端點記錄按鈕狀態
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人末端點記錄按鈕狀態
    * @param  [out] state 按鈕狀態，0-按下，1-鬆開
    * @return  錯誤碼
    */   
    int GetAxlePointRecordBtnState(int[] state)

獲取機器人末端DO輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人末端DO輸出狀態
    * @param  [out] do_state DO輸出狀態，do0~do1對應bit1~bit2,從bit0開始
    * @return  錯誤碼
    */   
    int GetToolDO(int[] do_state)

獲取機器人控制器DO輸出狀態
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人控制器DO輸出狀態
    * @param  [out] do_state_h DO輸出狀態，co0~co7對應bit0~bit7
    * @param  [out] do_state_l DO輸出狀態，do0~do7對應bit0~bit7
    * @return  錯誤碼
    */   
    int GetDO(int[] do_state_h, int[] do_state_l)

獲取機器人DI、DO狀態代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetDIAI(Robot robot)
    {
        int status = 1;
        int smooth = 0;
        int block = 0;
        int[] di =new int[]{0}, tool_di =new int[] {0};
        double[] ai =new double[] {0}, tool_ai = new double[]{0};
        double value = 0.0;


        robot.GetDI(0, block, di);
        System.out.println("di0:"+di[0]);

        robot.GetToolDI(1, block, tool_di);
        System.out.println("tool_di1:"+ tool_di[0]);

        robot.GetAI(0, block, ai);
        System.out.println("ai0:"+ ai[0]);

        robot.GetToolAI(0, block, tool_ai);
        System.out.println("tool_ai0:"+ tool_ai[0]);

        int[] _button_state=new int[]{0};
        robot.GetAxlePointRecordBtnState(_button_state);
        System.out.println("_button_state is: "+ _button_state[0]);

        int[] tool_do_state=new int[]{0};
        robot.GetToolDO(tool_do_state);
        System.out.println("tool DO state is: "+ tool_do_state[0]);

        int[] do_state_h=new int[]{0};
        int[] do_state_l=new int[]{0};
        robot.GetDO(do_state_h, do_state_l);
        System.out.println("DO state high is: "+do_state_h[0]+", DO state low is: "+ do_state_l[0]);

        return 0;
    }

等待控制箱數字量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱數字量輸入
    * @param  [in]  id  io編號，範圍[0~15]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitDI(int id, int status, int max_time, int opt); 

等待控制箱多路數字量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱多路數字量輸入
    * @param  [in] mode 0-多路與，1-多路或
    * @param  [in] id  io編號，bit0~bit7對應DI0~DI7，bit8~bit15對應CI0~CI7
    * @param  [in] status 0-關，1-開
    * @param  [in] max_time  最大等待時間，單位ms
    * @param  [in] opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitMultiDI(int mode, int id, int status, int max_time, int opt); 

等待工具數字量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具數字量輸入
    * @param  [in]  id  io編號，範圍[0~1]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolDI(int id, int status, int max_time, int opt); 

等待控制箱模擬量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱模擬量輸入
    * @param  [in]  id  io編號，範圍[0~1]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitAI(int id, int sign, double value, int max_time, int opt);   

等待工具模擬量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具模擬量輸入
    * @param  [in]  id  io編號，範圍[0]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolAI(int id, int sign, double value, int max_time, int opt); 

等待控制箱數字、模擬輸入信號代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWaitDIAI(Robot robot)
    {
        int rtn=-1;

        int status = 1;
        int smooth = 0;
        int block = 0;
        int di = 0, tool_di = 0;
        double ai = 0.0, tool_ai = 0.0;
        double value = 0.0;

        rtn = robot.WaitDI(0, 1, 1000, 1);
        System.out.println("WaitDI over; rtn is: "+ rtn);

        robot.WaitMultiDI(1, 3, 3, 1000, 1);
        System.out.println("WaitDI over; rtn is: "+ rtn);

        robot.WaitToolDI(1, 1, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);

        robot.WaitAI(0, 0, 50, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);

        robot.WaitToolAI(0, 0, 50, 1000, 1);
        System.out.println("WaitDI over; rtn is: " + rtn);
        return 0;
    }

設定控制箱DO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定控制箱DO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetCtlBoxDO(int resetFlag, int reloadFlag)

設定控制箱AO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定控制箱AO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetCtlBoxAO(int resetFlag, int reloadFlag)

設定末端工具DO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定末端工具DO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetAxleDO(int resetFlag, int reloadFlag)

設定末端工具AO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定末端工具AO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetAxleAO(int resetFlag, int reloadFlag)
    
設定擴展DO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展DO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetExtDO(int resetFlag, int reloadFlag)
    
設定擴展AO停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擴展AO停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetExtAO(int resetFlag, int reloadFlag)

設定SmartTool停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定SmartTool停止/暫停後輸出是否復位
    * @param resetFlag 0-不復位；1-復位
    * @param reloadFlag 暫停恢復後是否重載，0-不載入；1-載入
    * @return 錯誤碼
    */
    public int SetOutputResetSmartToolDO(int resetFlag, int reloadFlag)

設定LUA程式停止/暫停後輸出復位程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestDOReset(Robot robot)
    {
        for (int i = 0; i < 16; i++)
        {
            robot.SetDO(i, 1, 0, 0);
            robot.Sleep(200);
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
        robot.Sleep(2000);
        robot.PauseMotion();
        robot.Sleep(2000);
        robot.ResumeMotion();
        robot.Sleep(2000);
        robot.CloseRPC();
    }