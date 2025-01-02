机器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

设置开机自动加载默认的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置开机自动加载默认的作业程序
    * @param  [in] flag  0-开机不自动加载默认程序，1-开机自动加载默认程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int LoadDefaultProgConfig(int flag, String program_name); 

代码示例
++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.LoadDefaultProgConfig(1,"/fruser/1010Test.lua");
    }

加载指定的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  加载指定的作业程序
    * @param  [in] program_name 作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int ProgramLoad(String program_name); 

获取已加载的作业程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取已加载的作业程序名
    * @param  [out] program_name program_name[0]:作业程序名及路径，如"/fruser/movej.lua"，其中"/fruser/"为固定路径
    * @return  错误码
    */
    int GetLoadedProgram(String[] program_name); 

获取当前机器人作业程序的执行行号
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取当前机器人作业程序执行的行号
    * @param  [out] List[0]:错误码; List[1]:int line 行号
    * @return  错误码
    */   
    List<Integer> GetCurrentLine();

运行当前加载的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  运行当前加载的作业程序
    * @return  错误码
    */
    int ProgramRun();

代码示例
++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
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

暂停运动
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  暂停当前运行的作业程序
    * @return  错误码
    */ 
    int PauseMotion();

恢复运动
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恢复当前暂停的作业程序
    * @return  错误码
    */ 
    int ResumeMotion(); 

终止当前运行的作业程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  终止当前运行的作业程序
    * @return  错误码
    */ 
    int StopMotion();   

代码示例
++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
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
            robot.PauseMotion();//暂停运动
            robot.Sleep(1000);
            robot.ResumeMotion();//恢复运动
            robot.Sleep(1000);
        }
        robot.StopMotion();//停止
    }

下载Lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 下载作业程序
    * @param [in] fileName 要下载的lua文件名"test.lua"或"test.tar.gz"
    * @param [in] savePath 保存文件本地路径“D://Down/”
    * @return 错误码 
    */
    int LuaDownLoad(String fileName, String savePath);

上传Lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 上传作业程序
    * @param [in] filePath 本地lua文件路径名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 错误信息
    * @return 错误码 
    */
    int LuaUpload(String filePath, String errStr);

删除Lua程序
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 删除作业程序
    * @param [in] fileName 要删除的作业程序名"test.lua"
    * @return 错误码 
    */
    int LuaDelete(String fileName);

获取当前所有作业程序名称
+++++++++++++++++++++++++++++++++++

.. versionadded:: JavaSDK-v1.0.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取当前所有作业程序名称
    * @param [out] luaNames 作业程序名称列表
    * @return 错误码 
    */
    int GetLuaList(List<String> luaNames);

代码示例
++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
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
