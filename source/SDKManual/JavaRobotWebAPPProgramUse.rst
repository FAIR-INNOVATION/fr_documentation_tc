機器人WebAPP程式使用
======================

.. toctree:: 
    :maxdepth: 5

設定開機自動載入預設的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定開機自動載入預設的作業程序
    * @param  [in] flag  0-開機不自動載入預設程序，1-開機自動載入預設程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int LoadDefaultProgConfig(int flag, String program_name); 

代碼範例
++++++++++++
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
        robot.LoadDefaultProgConfig(1,"/fruser/1010Test.lua");
    }

載入指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  載入指定的作業程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int ProgramLoad(String program_name); 

取得已載入的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得已載入的作業程序名
    * @param  [out] program_name program_name[0]:作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int GetLoadedProgram(String[] program_name); 

取得目前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得目前機器人作業程式執行的行號
    * @param  [out] List[0]:錯誤碼; List[1]:int line 行號
    * @return  錯誤碼
    */   
    List<Integer> GetCurrentLine();

運行目前已載入的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  運行目前已載入的作業程序
    * @return  錯誤碼
    */
    int ProgramRun();

代碼範例
++++++++++++
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
        robot.Mode(0);
        robot.ProgramLoad("/fruser/1010Test.lua");
        String[] loadedNameStr = new String[1];
        robot.GetLoadedProgram(loadedNameStr);
        System.out.println("Loaded lua Name is " + loadedNameStr[0]);
        robot.ProgramRun();
        while(true)
        {
            List<Integer> results =  robot.GetCurrentLine();
            ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
            System.out.println("current line is " + results.get(1) + " Robot Runing State: " + pkg.robot_state);
            robot.Sleep(500);
        }
    }

暫停運動
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  暫停目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    int PauseMotion();

恢復運動
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恢復目前暫停的作業程序
    * @return  錯誤碼
    */ 
    int ResumeMotion(); 

終止目前正在執行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  終止目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    int StopMotion();   

代碼範例
++++++++++++
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
        robot.Mode(0);
        robot.ProgramLoad("/fruser/1010Test.lua");
        String[] loadedNameStr = new String[1];
        robot.GetLoadedProgram(loadedNameStr);
        System.out.println("Loaded lua Name is " + loadedNameStr[0]);
        robot.ProgramRun();

        for(int i = 0; i < 10;  i++)
        {
            robot.PauseMotion();//暫停運動
            robot.Sleep(1000);
            robot.ResumeMotion();//恢復運動
            robot.Sleep(1000);
        }
        robot.StopMotion();//停止
    }

下載lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 下載作業程序
    * @param [in] fileName 要下載的lua文件名"test.lua"或"test.tar.gz"
    * @param [in] savePath 儲存檔案本機路徑“D://Down/”
    * @return 錯誤碼 
    */
    int LuaDownLoad(String fileName, String savePath);

上傳lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 上傳作業程序
    * @param [in] filePath 本地lua檔案路徑名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 錯誤訊息
    * @return 錯誤碼 
    */
    int LuaUpload(String filePath, String errStr);

删除Lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 刪除作業程序
    * @param [in] fileName 要刪除的作業程序名稱"test.lua"
    * @return 錯誤碼 
    */
    int LuaDelete(String fileName);

取得目前所有作業程序名稱
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得目前所有作業程序名稱
    * @param [out] luaNames 作業程序名稱列表
    * @return 錯誤碼 
    */
    int GetLuaList(List<String> luaNames);

代碼範例
++++++++++++
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
        robot.LuaDownLoad("1010TestLUA.lua", "D://LUA/");
        List<String> names = new ArrayList<String>();
        robot.GetLuaList(names);
        System.out.println("lua Num " + names.size() + "   " + names.get(0));
        String errStr = "";
        robot.LuaUpload("D://LUA/1010TestLUA.lua", errStr);
        System.out.println("robot upload 1010TestLUA lua result " + errStr);
        robot.LuaDelete("1010TestLUA.lua");
    }
