機器人IO
============

.. toctree:: 
    :maxdepth: 5

設定控制箱數位量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定控制箱數位量輸出
    * @param  [in] id  io編號，範圍[0~15]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetDO(int id, int status, int smooth, int block); 

設定工具數位量輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定工具數位量輸出
    * @param  [in] id  io編號，範圍[0~1]
    * @param  [in] status 0-關，1-開
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolDO(int id, int status, int smooth, int block); 

設定控制箱類比輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定控制箱類比輸出
    * @param  [in] id  id  io編號，範圍[0~1]
    * @param  [in] id  value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] id  block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetAO(int id, double value, int block); 

設定工具類比輸出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定工具類比輸出
    * @param  [in] id  io編號，範圍[0]
    * @param  [in] value 電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  錯誤碼
    */
    int SetToolAO(int id, double value, int block); 

等待控制箱數位量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱數位量輸入
    * @param  [in]  id  io編號，範圍[0~15]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
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
    * @param  [in] opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitMultiDI(int mode, int id, int status, int max_time, int opt); 

等待工具數位量輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具數位量輸入
    * @param  [in]  id  io編號，範圍[0~1]
    * @param  [in]  status 0-關，1-開
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
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
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitAI(int id, int sign, double value, int max_time, int opt);   

等待工具類比輸入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具類比輸入
    * @param  [in]  id  io編號，範圍[0]
    * @param  [in]  sign 0-大於，1-小於
    * @param  [in]  value 輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mS]或電壓[0~10V]
    * @param  [in]  max_time  最大等待時間，單位ms
    * @param  [in]  opt  超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待
    * @return  錯誤碼
    */
    int WaitToolAI(int id, int sign, double value, int max_time, int opt); 

代碼範例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.SetDO(8, 1, 0, 0);
        robot.Sleep(3000);
        robot.SetDO(8, 0, 0, 0);

        robot.SetToolDO(0, 1, 0, 0);
        robot.Sleep(3000);
        robot.SetToolDO(0, 0, 0, 0);

        for(int i = 0; i < 90; i++)
        {
            robot.SetAO(0, i+1, 0);
            robot.SetAO(1, i+1, 0);
            robot.Sleep(50);
        }
        robot.SetAO(0, 0.0, 0);
        robot.SetAO(1, 0.0, 0);

        for(int i = 0; i < 99; i++)
        {
            robot.SetToolAO(0, i+1, 0);
            robot.Sleep(50);
        }
        robot.SetToolAO(0, 0.0, 0);

        System.out.println("wait  start ");
        robot.WaitDI(1, 1, 10000, 0);//WaitDI
        robot.WaitMultiDI(0, 6, 6, 10000, 0);//WaitMultiDI
        robot.WaitToolDI(0, 1, 5000, 0);//WaitToolDI
        robot.WaitAI(0, 0, 8.0, 5000, 0);//WaitAI
        robot.WaitToolAI(0, 0, 20, 5000, 0);//WaitToolAI
        System.out.println("wait  end ");
    }

設定控制箱DO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定控制箱DO停止/暫停後輸出是否重設 
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetCtlBoxDO(int resetFlag);

設定控制箱AO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定控制箱AO停止/暫停後輸出是否重設 
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetCtlBoxAO(int resetFlag);

設定末端工具DO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定末端工具DO停止/暫停後輸出是否重設
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetAxleDO(int resetFlag);

設定末端工具AO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定末端工具AO停止/暫停後輸出是否重設 
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetAxleAO(int resetFlag);
    
設定擴充DO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定擴充DO停止/暫停後輸出是否重設
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetExtDO(int resetFlag);
    
設定擴充AO停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定擴充AO停止/暫停後輸出是否重設
    * @param [in] resetFlag  0-不復位；1-復位
    * @return 錯誤碼 
    */ 
    int SetOutputResetExtAO(int resetFlag);

代碼範例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.SetOutputResetCtlBoxDO(1);
        robot.SetOutputResetAxleDO(1);//工具
        robot.SetOutputResetCtlBoxAO(1);
        robot.SetOutputResetAxleAO(1);//工具
    }