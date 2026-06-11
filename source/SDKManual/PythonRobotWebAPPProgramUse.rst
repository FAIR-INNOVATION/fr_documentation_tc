機器人WebAPP程序使用
======================

.. toctree:: 
    :maxdepth: 5

設置開機自動加載默認的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadDefaultProgConfig(flag,program_name)``"
    "描述", "設置開機自動加載默認的作業程序"
    "必選參數", "
    - ``flag``：1-開機自動加載默認程序，0-不自動加載默認程序
    - ``program_name``：作業程序名及路徑，如“movej.lua”"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

加載指定的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramLoad(program_name)``"
    "描述", "加載指定的作業程序"
    "必選參數", "- ``program_name``：作業程序名及路徑，如“movej.lua”"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取已加載的作業程序名
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLoadedProgram()``"
    "描述", "獲取已加載的作業程序名"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``program_name``：已加載的作業程序名"

獲取當前機器人作業程序的執行行號
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurrentLine()``"
    "描述", "獲取當前機器人作業程序的執行行號"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``line_num``：當前機器人作業程序的執行行號"

運行當前加載的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramRun()``"
    "描述", "運行當前加載的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

暫停當前運行的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramPause()``"
    "描述", "暫停當前運行的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

恢復當前暫停的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramResume()``"
    "描述", "恢復當前暫停的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

終止當前運行的作業程序
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "終止當前運行的作業程序"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取機器人作業程序執行狀態
++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetProgramState()``"
    "描述", "獲取機器人作業程序執行狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``:機器人作業程序執行狀態，1-程序停止或無程序運行，2-程序運行中，3-程序暫停"

機器人LUA程序操作代碼示例
++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    program_name = "test0610.lua"
    loaded_name = ""
    state = 0
    line = 0
    robot.Mode(0)
    robot.LoadDefaultProgConfig(0, program_name)
    robot.ProgramLoad(program_name)
    robot.ProgramRun()
    time.sleep(1)
    robot.ProgramPause()
    error,state = robot.GetProgramState()
    print(f"program state:{state}")
    error,line = robot.GetCurrentLine()
    print(f"current line:{line}")
    error,loaded_name = robot.GetLoadedProgram()
    print(f"program name:{loaded_name}")
    time.sleep(1)
    robot.ProgramResume()
    time.sleep(1)
    robot.ProgramStop()
    time.sleep(1)
    robot.CloseRPC()

下載Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LuaDownLoad(fileName, savePath)``"
    "描述", "下載Lua文件"
    "必選參數", "- ``fileName``：要下載的lua文件名 如“test.lua”
    - ``savePath``：保存文件本地路徑 如“D://Down/”"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

刪除Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaDelete(fileName)``"
    "描述", "刪除Lua文件"
    "必選參數", "- ``fileName``：要刪除的lua文件名“test.lua”"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取當前所有lua文件名稱
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLuaList()``"
    "描述", "獲取當前所有lua文件名稱"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``lua_num``：lua文件數量
    - ``luaNames``：lua文件名列表"

上傳Lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LuaUpload(filePath)``"
    "描述", "上傳Lua文件"
    "必選參數", "- ``filePath``：上傳文件的全路徑名  如D://test/test.lua"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - errorStr(lua文件存在錯誤返回)"

機器人LUA文件上傳下載代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn,lua_num,luaNames = robot.GetLuaList()
    print(f"res is:{rtn}")
    print(f"size is:{lua_num}")
    for name in luaNames:
        print(name)
    rtn = robot.LuaDownLoad("test0610.lua", "D://zDOWN/")
    print(f"LuaDownLoad rtn is:{rtn}")
    rtn = robot.LuaUpload("D://zDOWN/test0610.lua")
    print(f"LuaUpload rtn is:{rtn}")
    rtn = robot.LuaDelete("test0610.lua")
    print(f"LuaDelete rtn is:{rtn}")
    robot.CloseRPC()
    