機器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

設置開機自動加載默認的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置開機自動加載默認的作業程序
    * @param  [in] flag  0-開機不自動加載默認程序，1-開機自動加載默認程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int LoadDefaultProgConfig(byte flag, string program_name); 

加載指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  加載指定的作業程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int ProgramLoad(string program_name); 

獲取已加載的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取已加載的作業程序名
    * @param  [out] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int GetLoadedProgram(ref string program_name); 

獲取當前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前機器人作業程序執行的行號
    * @param  [out] line  行號
    * @return  錯誤碼
    */   
    int GetCurrentLine(ref int line);

運行當前加載的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  運行當前加載的作業程序
    * @return  錯誤碼
    */
    int ProgramRun();

暫停當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  暫停當前運行的作業程序
    * @return  錯誤碼
    */ 
    int ProgramPause();

恢復當前暫停的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恢復當前暫停的作業程序
    * @return  錯誤碼
    */ 
    int ProgramResume(); 

終止當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  終止當前運行的作業程序
    * @return  錯誤碼
    */ 
    int ProgramStop();   

獲取機器人作業程序執行狀態
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取機器人作業程序執行狀態
    * @param  [out]  state 1-程序停止或無程序運行，2-程序運行中，3-程序暫停
    * @return  錯誤碼
    */
    int GetProgramState(ref byte state);

機器人LUA程序操作代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnWebApp_Click(object sender, EventArgs e)
    {
        string program_name = "/fruser/Text1.lua";
        string loaded_name = "";
        byte state=0;
        int line=0;

        robot.Mode(0);
        robot.LoadDefaultProgConfig(0, program_name);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        Thread.Sleep(1000);
        robot.ProgramPause();
        robot.GetProgramState(ref state);
        Console.WriteLine("program state:{0}\n", state);
        robot.GetCurrentLine(ref line);
        Console.WriteLine("current line:{0}\n", line);
        robot.GetLoadedProgram(ref loaded_name);
        Console.WriteLine("program name:{0}\n", loaded_name);
        Thread.Sleep(1000);
        robot.ProgramResume();
        Thread.Sleep(1000);
        robot.ProgramStop();
        Thread.Sleep(1000);
    }

下載Lua文件
+++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 下載Lua文件
    * @param [in] fileName 要下載的作業程序"test.lua"或"test.tar.gz"
    * @param [in] savePath 保存作業程序本地路徑“D://Down/”
    * @return 錯誤碼 
    */
    public int LuaDownLoad(string fileName, string savePath);

上傳Lua文件
+++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 上傳Lua文件
    * @param [in] filePath 本地作業程序路徑名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 錯誤信息
    * @return 錯誤碼 
    */
    public int LuaUpload(string filePath, ref string errStr);

刪除Lua文件
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 刪除Lua文件
    * @param [in] fileName 要刪除的作業程序名"test.lua"
    * @return 錯誤碼 
    */
    public int LuaDelete(string fileName);

獲取當前所有lua文件名稱
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取當前所有lua文件名稱
    * @param [out] luaNames 作業程序名稱列表
    * @return 錯誤碼 
    */
    public int GetLuaList(ref List<string> luaNames) ;


機器人LUA文件上傳下載代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnUploadLua_Click(object sender, EventArgs e)
    {
        int rtn;
        List<string> luaNames = new List<string>();
        rtn = robot.GetLuaList(ref luaNames);
        Console.WriteLine("res is: {0}", rtn);
        Console.WriteLine("size is: {0}", luaNames.Count);
        foreach (var name in luaNames)
        {
        Console.WriteLine(name);
        }
        rtn = robot.LuaDownLoad("TT.lua", "D://zDOWN/");
        Console.WriteLine("LuaDownLoad rtn is {0}", rtn);
        string errStr = "";
        Thread.Sleep(2000);

        rtn = robot.LuaUpload("D://zUP/airlab.lua", ref errStr);
        Console.WriteLine("LuaUpload rtn is {0}", errStr);
        Thread.Sleep(2000);
        rtn = robot.LuaDelete("TT.lua");
        Console.WriteLine("LuaDelete rtn is {0}", rtn);
    }
