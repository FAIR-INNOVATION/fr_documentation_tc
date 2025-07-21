機器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

設置開機自動加載默認的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置開機自動加載默認的作業程序
    * @param  [in] flag  0-開機不自動加載默認程序，1-開機自動加載默認程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int LoadDefaultProgConfig(int flag, String program_name); 

加載指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  加載指定的作業程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int ProgramLoad(String program_name); 

獲取已加載的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取已加載的作業程序名
    * @param  [out] program_name program_name[0]:作業程序名及路徑，如"/fruser/movej.lua"，其中"/fruser/"爲固定路徑
    * @return  錯誤碼
    */
    int GetLoadedProgram(String[] program_name); 

獲取當前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前機器人作業程序執行的行號
    * @param  [out] List[0]:錯誤碼; List[1]:int line 行號
    * @return  錯誤碼
    */   
    List<Integer> GetCurrentLine();

運行當前加載的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  運行當前加載的作業程序
    * @return  錯誤碼
    */
    int ProgramRun();

暫停當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  暫停當前運行的作業程序
    * @return  錯誤碼
    */ 
    int PauseMotion();

恢復當前暫停的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恢復當前暫停的作業程序
    * @return  錯誤碼
    */ 
    int ResumeMotion(); 

終止當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  終止當前運行的作業程序
    * @return  錯誤碼
    */ 
    int StopMotion();   

獲取機器人作業程序執行狀態
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人作業程序執行狀態
    * @param   [out] state 1-程序停止或無程序運行，2-程序運行中，3-程序暫停
    * @return  錯誤碼
    */
    public int GetProgramState(int[] state)

機器人LUA程序操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLuaOp(Robot robot)
    {
        String program_name = "/fruser/Text1.lua";
        String[] loaded_name = new String[]{""};
        int[] state=new int[]{0};
        List<Integer> line=new ArrayList<>();

        robot.Mode(0);
        robot.LoadDefaultProgConfig(0, program_name);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        robot.Sleep(1000);
        robot.ProgramPause();
        robot.GetProgramState(state);
        System.out.println("program state:"+ state[0]);
        line=robot.GetCurrentLine();
        System.out.println("current line:"+ line);
        robot.GetLoadedProgram(loaded_name);
        System.out.println("program name:"+ loaded_name[0]);
        robot.Sleep(1000);
        robot.ProgramResume();
        robot.Sleep(1000);
        robot.ProgramStop();
        robot.Sleep(1000);

        robot.CloseRPC();
        return 0;
    }

下載Lua程序
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下載作業程序
    * @param [in] fileName 要下載的lua文件名"test.lua"或"test.tar.gz"
    * @param [in] savePath 保存文件本地路徑“D://Down/”
    * @return 錯誤碼 
    */
    int LuaDownLoad(String fileName, String savePath);

刪除Lua程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 刪除作業程序
    * @param [in] fileName 要刪除的作業程序名"test.lua"
    * @return 錯誤碼 
    */
    int LuaDelete(String fileName);

獲取當前所有lua文件名稱
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取當前所有lua文件名稱
    * @param [out] luaNames 作業程序名稱列表
    * @return 錯誤碼 
    */
    int GetLuaList(List<String> luaNames);

上傳Lua程序
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上傳作業程序
    * @param [in] filePath 本地lua文件路徑名 ".../test.lua"或".../test.tar.gz"
    * @param [out] errStr 錯誤信息
    * @return 錯誤碼 
    */
    int LuaUpload(String filePath, String errStr);

機器人LUA文件上傳下載代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLUAUpDownLoad(Robot robot)
    {
        List<String> luaNames=new ArrayList<>();
        int rtn = robot.GetLuaList(luaNames);
        System.out.println("res is: "+rtn);
        System.out.println("size is: "+luaNames.size());
        for (int it =1; it < luaNames.size(); it++)
        {
            System.out.println(luaNames.get(it));
        }

        rtn = robot.LuaDownLoad("test.lua", "D://zDOWN/");
        System.out.println("LuaDownLoad rtn is:"+rtn);

        rtn = robot.LuaUpload("D://zUP/XG.lua","");
        System.out.println("LuaUpload rtn is:"+ rtn);

        rtn = robot.LuaDelete("XG.lua");
        System.out.println("LuaDelete rtn is:"+ rtn);

        return 0;
    }
