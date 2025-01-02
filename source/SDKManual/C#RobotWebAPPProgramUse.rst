机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置开机自动加载默认的作业程序
    * @param  [in] flag  0-开机不自动加载默认程序，1-开机自动加载默认程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int LoadDefaultProgConfig(byte flag, string program_name); 

加载指定的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  加载指定的作业程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int ProgramLoad(string program_name); 

获取已加载的作业程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取已加载的作业程序名
    * @param  [out] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int GetLoadedProgram(ref string program_name); 

获取当前机器人作业程序的执行行号
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取当前机器人作业程序执行的行号
    * @param  [out] line  行号
    * @return  错误码
    */   
    int GetCurrentLine(ref int line);

运行当前加载的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  运行当前加载的作业程序
    * @return  错误码
    */
    int ProgramRun();

暂停当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  暂停当前运行的作业程序
    * @return  错误码
    */ 
    int ProgramPause();

恢复当前暂停的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恢复当前暂停的作业程序
    * @return  错误码
    */ 
    int ProgramResume(); 

终止当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  终止当前运行的作业程序
    * @return  错误码
    */ 
    int ProgramStop();   

获取机器人作业程序执行状态
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取机器人作业程序执行状态
    * @param  [out]  state 1-程序停止或无程序运行，2-程序运行中，3-程序暂停
    * @return  错误码
    */
    int GetProgramState(ref byte state);

代码示例
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

下载作业程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 下载作业程序
    * @param [in] fileName 要下载的作业程序"test.lua"或"test.tar.gz"
    * @param [in] savePath 保存作业程序本地路径“D://Down/”
    * @return 错误码 
    */
    public int LuaDownLoad(string fileName, string savePath);

上传作业程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 上传作业程序
    * @param [in] filePath 本地作业程序路径名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 错误信息
    * @return 错误码 
    */
    public int LuaUpload(string filePath, ref string errStr);

删除作业程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 删除作业程序
    * @param [in] fileName 要删除的作业程序名"test.lua"
    * @return 错误码 
    */
    public int LuaDelete(string fileName);

获取当前所有作业程序名称
+++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取当前所有作业程序名称
    * @param [out] luaNames 作业程序名称列表
    * @return 错误码 
    */
    public int GetLuaList(ref List<string> luaNames) ;


代码示例
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
