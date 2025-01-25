機器人WebAPP程式使用
======================

.. toctree:: 
    :maxdepth: 5

設定開機自動載入預設的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定開機自動載入預設的作業程序
    * @param  [in] flag  0-開機不自動載入預設程序，1-開機自動載入預設程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    errno_t  LoadDefaultProgConfig(uint8_t flag, char program_name[64]);

載入指定的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  載入指定的作業程序
    * @param  [in] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    errno_t  ProgramLoad(char program_name[64]);

取得已載入的作業程序名
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得已載入的作業程序名
    * @param  [out] program_name 作業程序名稱及路徑，如"/fruser/movej.lua"，其中"/fruser/"為固定路徑
    * @return  錯誤碼
    */
    errno_t  GetLoadedProgram(char program_name[64]);  

取得目前機器人作業程序的執行行號
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前機器人作業程式執行的行號
    * @param  [out] line  行號
    * @return  錯誤碼
    */   
    errno_t  GetCurrentLine(int *line);

運行目前已載入的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  運行目前已載入的作業程序
    * @return  錯誤碼
    */
    errno_t  ProgramRun();

暫停目前正在執行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  暫停目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramPause();

恢復目前暫停的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  恢復目前暫停的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramResume();  

終止目前正在執行的作業程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  終止目前正在執行的作業程序
    * @return  錯誤碼
    */ 
    errno_t  ProgramStop();    

取得機器人作業程序執行狀態
+++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得機器人作業程序執行狀態
    * @param  [out]  state 1-程式停止或無程式運行，2-程式運行中，3-程式暫停
    * @return  錯誤碼
    */
    errno_t  GetProgramState(uint8_t *state);

代碼範例
++++++++++++
.. code-block:: c++
    :linenos:

    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #include "FRRobot.h"
    #include "RobotTypes.h"

    using namespace std;

    int main(void)
    {
        FRRobot robot;                 //實例化機器人對象
        robot.RPC("192.168.58.2");     //與機器人控制器建立通信连接

        char program_name[64] = "/fruser/ptps.lua";
        char loaded_name[64] = "";
        uint8_t state;
        int line;

        robot.Mode(0);
        robot.ProgramLoad(program_name);
        robot.ProgramRun();
        sleep(5);
        robot.ProgramPause();
        robot.GetProgramState(&state);
        printf("program state:%u\n", state);
        robot.GetCurrentLine(&line);
        printf("current line:%d\n", line);
        robot.GetLoadedProgram(loaded_name);
        printf("program name:%s\n", loaded_name);
        sleep(5);
        robot.ProgramResume();
        sleep(5);
        robot.ProgramStop();
        sleep(2);

        return 0;
    }

下載Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下載Lua文件
    * @param [in] fileName 要下載的lua檔名，例如：“test.lua”
    * @param [in] savePath 儲存檔案本機路徑，例如：“D://Down/”
    * @return 錯誤碼
    */
    errno_t LuaDownLoad(std::string fileName, std::string savePath);

上傳Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳Lua文件
    * @param [in] filePath 本地lua檔案路徑名
    * @return 錯誤碼
    */
    errno_t LuaUpload(std::string filePath);

删除Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 删除Lua文件
    * @param [in] fileName 要刪除的lua檔名，例如：“test.lua”
    * @return 錯誤碼
    */
    errno_t LuaDelete(std::string fileName);

取得目前所有lua檔案名稱
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得目前所有lua檔案名稱
    * @param [out] luaNames lua檔名列表
    * @return 錯誤碼
    */
    errno_t GetLuaList(std::list<std::string>* luaNames);

代碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的頭文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的頭文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;
    int main(void)
    {
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(3);
        robot.RPC("192.168.58.2");

        /* 取得lua名稱 */
        list<std::string> luaNames;
        int res = robot.GetLuaList(&luaNames);
        std::cout << "res is: " << res << std::endl;
        std::cout << "size is: " << luaNames.size() <<std::endl;
        for(auto it = luaNames.begin(); it != luaNames.end(); it++)
        {
            std::cout << it->c_str() << std::endl;
        }

        /* 下載lua */
        res = robot.LuaDownLoad("test.lua", "D://Down/");
        std::cout << "res is: " << res << std::endl;

        /* 上傳lua */
        res = robot.LuaUpload("D://Down/test.lua");
        std::cout << "res is: " << res << std::endl;

        /* 删除lua */
        res = robot.LuaDelete("test.lua");
        std::cout << "res is: " << res << std::endl;

        robot.CloseRPC();
        return 0;
    }
