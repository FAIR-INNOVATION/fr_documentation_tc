機器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

設置開機自動加載默認的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設置開機自動加載默認的作業程序
    * @param  [in] flag  0-開機不自動加載默認程序，1-開機自動加載默認程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中“/fruser/”為QX固定路徑，“/usr/local/etc/controller/lua/”為LA固定路徑
    * @return  錯誤碼
    */
    errno_t  LoadDefaultProgConfig(uint8_t flag, char program_name[64]);

加載指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  加載指定的作業程序
    * @param  [in] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中“/fruser/”為QX固定路徑，“/usr/local/etc/controller/lua/”為LA固定路徑
    * @return  錯誤碼
    */
    errno_t  ProgramLoad(char program_name[64]);

獲取已加載的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取已加載的作業程序名
    * @param  [out] program_name 作業程序名及路徑，如"/fruser/movej.lua"，其中“/fruser/”為QX固定路徑，“/usr/local/etc/controller/lua/”為LA固定路徑
    * @return  錯誤碼
    */
    errno_t  GetLoadedProgram(char program_name[64]);  

獲取當前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前機器人作業程序執行的行號
    * @param  [out] line  行號
    * @return  錯誤碼
    */   
    errno_t  GetCurrentLine(int *line);

運行當前加載的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  運行當前加載的作業程序
    * @return  錯誤碼
    */
    errno_t  ProgramRun();

暫停當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  暫停當前運行的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramPause();

恢復當前暫停的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  恢復當前暫停的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramResume();  

終止當前運行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  終止當前運行的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramStop();    

獲取機器人作業程序執行狀態
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取機器人作業程序執行狀態
    * @param  [out]  state 1-程序停止或無程序運行，2-程序運行中，3-程序暫停
    * @return  錯誤碼
    */
    errno_t  GetProgramState(uint8_t *state);

機器人LUA程序操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestLuaOp(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      char program_name[64] = "/fruser/test.lua";
      char loaded_name[64] = "";
      uint8_t state;
      int line;
      robot.Mode(0);
      robot.LoadDefaultProgConfig(0, program_name);
      robot.ProgramLoad(program_name);
      robot.ProgramRun();
      robot.Sleep(1000);
      robot.ProgramPause();
      robot.GetProgramState(&state);
      printf("program state:%u\n", state);
      robot.GetCurrentLine(&line);
      printf("current line:%d\n", line);
      robot.GetLoadedProgram(loaded_name);
      printf("program name:%s\n", loaded_name);
      robot.Sleep(1000);
      robot.ProgramResume();
      robot.Sleep(1000);
      robot.ProgramStop();
      robot.Sleep(1000);
      robot.CloseRPC();
      return 0;
    }

下載Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下載Lua文件
    * @param [in] fileName 要下載的lua文件名，例如：“test.lua”
    * @param [in] savePath 保存文件本地路徑，例如：“D://Down/”
    * @return 錯誤碼
    */
    errno_t LuaDownLoad(std::string fileName, std::string savePath);

刪除Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 刪除Lua文件
    * @param [in] fileName 要刪除的lua文件名，例如：“test.lua”
    * @return 錯誤碼
    */
    errno_t LuaDelete(std::string fileName);

獲取當前所有lua文件名稱
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取當前所有lua文件名稱
    * @param [out] luaNames lua文件名列表
    * @return 錯誤碼
    */
    errno_t GetLuaList(std::list<std::string>* luaNames);

上傳Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳Lua文件
    * @param [in] filePath 本地lua文件路徑名
    * @return 錯誤碼
    */
    errno_t LuaUpload(std::string filePath);

機器人LUA文件上傳下載代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestLUAUpDownLoad(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      list<std::string> luaNames;
      rtn = robot.GetLuaList(&luaNames);
      std::cout << "res is: " << rtn << std::endl;
      std::cout << "size is: " << luaNames.size() << std::endl;
      for (auto it = luaNames.begin(); it != luaNames.end(); it++)
      {
        std::cout << it->c_str() << std::endl;
      }
      rtn = robot.LuaDownLoad("test.lua", "D://zDOWN/");
      printf("LuaDownLoad rtn is %d\n", rtn);
      rtn = robot.LuaUpload("D://zUP/airlab.lua");
      printf("LuaUpload rtn is %d\n", rtn);
      rtn = robot.LuaDelete("test.lua");
      printf("LuaDelete rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }