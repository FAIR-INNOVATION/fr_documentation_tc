機器人IO
============

.. toctree:: 
    :maxdepth: 5

設置控制箱數字量輸出
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDO(id, status, smooth=0, block=0)``"
    "描述", "設置控制箱數字量輸出"
    "必選參數", "-  ``id``:io編號，範圍[0~15]；
    - ``status``:0-關，1-開；"
    "默認參數", "- ``smooth``:0-不平滑，1-平滑 默認0;
    - ``block``:0-阻塞，1-非阻塞 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置工具數字量輸出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDO (id, status, smooth=0, block=0)``"
    "描述", "設置工具數字量輸出"
    "必選參數", "-  ``id``:io編號，範圍[0~1]；
    - ``status``:0-關，1-開；"
    "默認參數", "- ``smooth``:0-不平滑，1-平滑；
    - ``block``:0-阻塞，1-非阻塞。"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置控制箱模擬量輸出
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAO(id,value,block=0)``"
    "描述", "設置控制箱模擬量輸出"
    "必選參數", "- ``id``:io編號，範圍[0~1]；
    - ``value``:電流或電壓值百分比，範圍[0~100%]對應電流值[0~20mA]或電壓[0~10V]；"
    "默認參數", "- ``block``:[0]-阻塞，[1]-非阻塞 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置工具模擬量輸出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolAO(id,value,block=0)``"
    "描述", "設置工具模擬量輸出"
    "必選參數", "- ``id``:io編號，範圍[0]；
    - ``value``:電流或電壓值百分比，範圍[0~100%]對應電流值[0~20mA]或電壓[0~10V]；"
    "默認參數", "- ``block``:[0]-阻塞，[1]-非阻塞 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置數字量、模擬量輸出代碼示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0  
    block = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3) 
    status = 0 
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1) 
    status = 0 
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    robot.CloseRPC()

獲取控制箱數字量輸入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDI(id, block=0)``"
    "描述", "獲取控制箱數字量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~15]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``di``: 0-低電平，1-高電平"

獲取工具數字量輸入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDI(id, block=0)``"
    "描述", "獲取工具數字量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode
    - ``di``: 0-低電平，1-高電平"

獲取控制箱模擬量輸入
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAI(id, block = 0)``"
    "描述", "獲取控制箱模擬量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0 "
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``value``: 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mA] 或電壓 [0~10V]"

獲取工具模擬量輸入
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolAI(id, block = 0)``"
    "描述", "獲取末端模擬量輸入"
    "必選參數", "- ``id``:io編號，範圍[0]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``value``: 輸入電流或電壓值百分比，範圍 [0~100] 對應電流值 [0~20mA] 或電壓 [0~10V]"

獲取機器人末端點記錄按鈕狀態
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxlePointRecordBtnState()``"
    "描述", "獲取機器人末端點記錄按鈕狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``buttonstatus``: 按鈕狀態，0-按下，1-鬆開"

獲取機器人末端DO輸出狀態
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDO()``"
    "描述", "獲取機器人末端DO輸出狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``do_state``: DO輸出狀態，do0~do1對應bit1~bit2,從bit0開始"

獲取機器人控制器DO輸出狀態
++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDO()``"
    "描述", "獲取機器人控制器DO輸出狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``do_state_h``: DO輸出狀態，co0~co7對應bit0~bit7 do_state_l DO輸出狀態，do0~do7對應bit0~bit7"

獲取機器人DI、DO狀態代碼示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    block = 0 
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}") 
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    robot.CloseRPC()

等待控制箱數字量輸入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitDI(id,status,maxtime,opt)``"
    "描述", "等待控制箱數字量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~15]；
    - ``status``:0-關，1-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待控制箱多路數字量輸入
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMultiDI(mode,id,status,maxtime,opt)``"
    "描述", "等待控制箱多路數字量輸入"
    "必選參數", "- ``mode``:[0]-多路與，[1]-多路或；
    - ``id``:io編號，bit0~bit7對應DI0~DI7，bit8~bit15對應CI0~CI7；
    - ``status``:bit0~bit7對應DI0~DI7狀態，bit8~bit15對應CI0~CI7狀態位的狀態[0]-關，[1]-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待。"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待工具數字量輸入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolDI(id,status,maxtime,opt)``"
    "描述", "等待末端數字量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；
    - ``status``:0-關，1-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待控制箱模擬量輸入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAI(id,sign,value,maxtime,opt)``"
    "描述", "等待控制箱模擬量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；
    - ``sign``:0-大於，1-小於
    - ``value``:輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待工具模擬量輸入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolAI(id,sign,value,maxtime,opt)``"
    "描述", "等待末端模擬量輸入"
    "必選參數", "- ``id``:io編號，範圍[0]；
    - ``sign``:0-大於，1-小於
    - ``value``:輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程序停止並提示超時，1-忽略超時提示程序繼續執行，2-一直等待"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待控制箱數字、模擬輸入信號代碼示例
++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    status = 1
    smooth = 0
    block = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 0
    for i in range(16):
        robot.SetDO(i, status, smooth, block)
        time.sleep(0.3)
    status = 1
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    status = 0
    for i in range(2):
        robot.SetToolDO(i, status, smooth, block)
        time.sleep(1)
    for i in range(100):
        robot.SetAO(0, i, block)
        time.sleep(0.03)
    for i in range(100):
        robot.SetToolAO(0, i, block)
        time.sleep(0.03)
    block = 0
    error,di = robot.GetDI(0, block)
    print(f"di0: {di}")
    error,tool_di = robot.GetToolDI(1, block)
    print(f"tool_di1: {tool_di}")
    error,ai = robot.GetAI(0, block)
    print(f"ai0: {ai:.2f}")
    error,tool_ai = robot.GetToolAI(0, block)
    print(f"tool_ai0: {tool_ai:.2f}")
    error,button_state = robot.GetAxlePointRecordBtnState()
    print(f"_button_state is: {button_state}")
    error,tool_do_state = robot.GetToolDO()
    print(f"tool DO state: {tool_do_state}")
    error,[do_state_h, do_state_l] = robot.GetDO()
    print(f"DO state hight  : {do_state_h}")
    print(f"DO state low : {do_state_l}")
    rtn = robot.WaitDI(0, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitMultiDI(1, 3, 3, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolDI(1, 1, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    rtn = robot.WaitToolAI(0, 0, 50, 1000, 1)
    print(f"WaitDI over; rtn is: {rtn}")
    robot.CloseRPC()

設定控制箱DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag,reloadFlag)``"
    "描述", "設定控制箱DO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定控制箱AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxAO(resetFlag,reloadFlag)``"
    "描述", "設定控制箱AO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定末端工具DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleDO(resetFlag,reloadFlag)``"
    "描述", "設定末端工具DO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定末端工具AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleAO(resetFlag,reloadFlag)``"
    "描述", "設定末端工具AO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定擴展DO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtDO (resetFlag,reloadFlag)``"
    "描述", "設定擴展DO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定擴展AO停止/暫停後輸出是否復位
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtAO (resetFlag,reloadFlag)``"
    "描述", "設定擴展AO停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定SmartTool停止/暫停後輸出是否復位
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetSmartToolDO(resetFlag,reloadFlag)``"
    "描述", "設定SmartTool停止/暫停後輸出是否復位"
    "必選參數", "
    - ``resetFlag``：0-不復位；1-復位
    - ``reloadFlag``：暫停恢復後是否重載，0-不載入；1-載入"
    "預設參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

設定LUA程式停止/暫停後輸出復位程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    for i in range(16):
        robot.SetDO(i, 1, 0, 0)
        time.sleep(0.2)
    resetFlag = 0
    resumeReloadFlag = 0
    rtn = robot.SetOutputResetCtlBoxDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetCtlBoxAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetAxleAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtDO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetExtAO(resetFlag, resumeReloadFlag)
    robot.SetOutputResetSmartToolDO(resetFlag, resumeReloadFlag)
    robot.ProgramLoad("/fruser/test.lua")
    robot.ProgramRun()
    time.sleep(2)
    robot.PauseMotion()
    time.sleep(2)
    robot.ResumeMotion()
    time.sleep(2)
    robot.CloseRPC()
    return 0