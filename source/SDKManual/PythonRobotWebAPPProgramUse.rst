機器人WebAPP程式使用
======================

.. toctree:: 
    :maxdepth: 5

設定開機自動載入預設的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadDefaultProgConfig(flag,program_name)``"
    "描述", "設定開機自動載入預設的作業程序"
    "必選參數", "- ``flag``：1-開机自動加载默認程序，0-不自動加载默認程序
    - ``program_name``：作業程序名稱及路徑，如“/fruser/movej.lua”，其中“/fruser/”為固定路徑"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

載入指定的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramLoad(program_name)``"
    "描述", "載入指定的作業程序"
    "必選參數", "- ``program_name``：作業程序名稱及路徑，如“/fruser/movej.lua”，其中“/fruser/”為固定路徑"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得目前機器人作業程序的執行行號
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurrentLine()``"
    "描述", "取得目前機器人作業程序的執行行號"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``line_num``：當前機器人作业程序的執行行號"

運行目前已載入的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramRun()``"
    "描述", "運行目前已載入的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

暫停目前正在執行的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramPause()``"
    "描述", "暫停目前正在執行的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

恢復目前暫停的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramResume()``"
    "描述", "恢復目前暫停的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

終止目前正在執行的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "終止目前正在執行的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得機器人作業程序執行狀態
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetProgramState()``"
    "描述", "取得機器人作業程序執行狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``state``:機器人作業程式執行狀態，1-程式停止或無程式運行，2-程式運行中，3-程式暫停"

取得已載入的作業程序名
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLoadedProgram()``"
    "描述", "取得已載入的作業程序名"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``program_name``：已載入的作業程序名"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    def print_program_state():
        pstate = robot.GetProgramState()    #查詢程式運行狀態,1-程式停止或無程式運行，2-程式運行中，3-程式暫停
        linenum = robot.GetCurrentLine()    #查詢目前作業程序執行的行號
        name = robot.GetLoadedProgram()     #查詢已載入的作業程序名
        print("the robot program state is:",pstate[1])
        print("the robot program line number is:",linenum[1])
        print("the robot program name is:",name[1])
        time.sleep(1)
    #機器人WebAPP程式使用接口
    robot.Mode(0)   #機器人切入自動運作模式
    print_program_state()
    ret = robot.ProgramLoad('/fruser/test0923.lua')   #載入要執行的機器人程序，testPTP.lua程式需要先在webapp上寫好
    print("載入要執行的機器人程式錯誤碼", ret)
    ret = robot.ProgramRun()     #執行機器人程式
    print("執行機器人程式錯誤碼", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramPause()   #暫停正在執行的機器人程序
    print("暫停正在執行的機器人程序錯誤碼", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramResume()  #恢復暫停執行的機器人程序
    print("恢復暫停執行的機器人程序錯誤碼", ret)
    time.sleep(2)
    print_program_state()
    ret = robot.ProgramStop()    #停止正在執行的機器人程序
    print("停止正在執行的機器人程序", ret)
    time.sleep(2)
    print_program_state()
    flag = 1   #0-開機不自動載入預設程序，1-開機自動載入預設程序
    ret = robot.LoadDefaultProgConfig(flag,'/fruser/testPTP.lua')    #設定開機自動載入預設程序
    print("設定開機自動載入預設程序", ret)

下載Lua文件
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LuaDownLoad(fileName, savePath)``"
    "描述", "下載Lua文件"
    "必選參數", "- ``fileName``：要下載的lua文件名 如“test.lua”
    - ``savePath``：儲存檔案本機路徑 如“D://Down/”"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LuaDownLoad("test", "D://Desktop/test_download/")

上傳Lua文件
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaUpload(filePath)``"
    "描述", "上傳Lua文件"
    "必選參數", "- ``filePath``：上傳檔案的全路徑名  如D://test/test.lua"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - errorStr(lua檔案存在錯誤回傳)"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LuaUpload("D://test/test.lua")

删除Lua文件
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaDelete(fileName)``"
    "描述", "删除Lua文件"
    "必選參數", "- ``fileName``：要刪除的lua檔名“test.lua”"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSoftwareVersion()
    robot.LuaDelete("test2")

取得目前所有lua檔案名稱
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLuaList()``"
    "描述", "取得目前所有lua檔案名稱"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``lua_num``：lua文件数量
    - ``luaNames``：lua檔名列表"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret,num,name  = robot.GetLuaList()
    print(num)
    print(name)