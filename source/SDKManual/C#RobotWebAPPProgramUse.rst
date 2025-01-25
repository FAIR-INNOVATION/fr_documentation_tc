機器人WebAPP程式使用
======================

.. toctree:: 
    :maxdepth: 5

設定開機自動載入預設的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定開機自動載入預設的作業程序
    * @param  [in] flag  0-開機不自動載入預設程序，1-開機自動載入預設程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int LoadDefaultProgConfig(byte flag, string program_name); 

載入指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  載入指定的作業程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int ProgramLoad(string program_name); 

取得已載入的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得已載入的作業程序名
    * @param  [out] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    int GetLoadedProgram(ref string program_name); 

取得目前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前機器人作業程式執行的行號
    * @param  [out] line  行號
    * @return  錯誤碼
    */   
    int GetCurrentLine(ref int line);

運行目前已載入的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  運行目前已載入的作業程序
    * @return  錯誤碼
    */
    int ProgramRun();

暫停目前正在執行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  暫停目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    int ProgramPause();

恢復目前暫停的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恢復目前暫停的作業程序
    * @return  錯誤碼
    */ 
    int ProgramResume(); 

終止目前正在執行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  終止目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    int ProgramStop();   

取得機器人作業程序執行狀態
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得機器人作業程序執行狀態
    * @param  [out]  state 1-程式停止或無程式運行，2-程式運行中，3-程式暫停
    * @return  錯誤碼
    */
    int GetProgramState(ref byte state);

代碼範例
++++++++++++
.. code-block:: c#
    :linenos:

    private void btnWebApp_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        string program_name = "/fruser/testWebApp.lua";
        string loaded_name = "";
        byte state = 0;
        int line = 0;

        robot.Mode(0);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        Thread.Sleep(2000);
        robot.ProgramPause();
        robot.GetProgramState(ref state);
        Console.WriteLine($"program state : {state}");
        robot.GetCurrentLine(ref line);
        Console.WriteLine($"current line : {line}");
        robot.GetLoadedProgram(ref loaded_name);
        Console.WriteLine($"program name : {loaded_name}");
        Thread.Sleep(1000);
        robot.ProgramResume();
        Thread.Sleep(1000);
        robot.ProgramStop();
    }

下載作業程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 下載作業程序
    * @param [in] fileName 要下載的作業程式"test.lua"或"test.tar.gz"
    * @param [in] savePath 儲存作業程序本機路徑「D://Down/”
    * @return 錯誤碼 
    */
    public int LuaDownLoad(string fileName, string savePath);

上傳作業程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 上傳作業程序
    * @param [in] filePath 本地作業程序路徑名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 錯誤訊息
    * @return 錯誤碼 
    */
    public int LuaUpload(string filePath, ref string errStr);

刪除作業程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 刪除作業程序
    * @param [in] fileName 要刪除的作業程序名稱"test.lua"
    * @return 錯誤碼 
    */
    public int LuaDelete(string fileName);

取得目前所有作業程序名稱
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得目前所有作業程序名稱
    * @param [out] luaNames 作業程序名稱列表
    * @return 錯誤碼 
    */
    public int GetLuaList(ref List<string> luaNames) ;


代碼範例
++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnUploadLua_Click(object sender, EventArgs e)
    {
        string errstr = "";
        robot.LuaUpload("D://Upload/test.lua", ref errstr);
        Console.WriteLine(errstr);
        robot.LuaDownLoad("test.lua", "D://zDOWN/");
        robot.LuaDelete("test.lua");
        List<string> lualist = new List<string>();
        robot.GetLuaList(ref lualist);
        int n = lualist.Count;
        for (int i = 0; i < n; i++)
        {
            Console.WriteLine(lualist[i]);
        }
    }
