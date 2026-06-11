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
    robot.ProgramLoad("test.lua")
    robot.ProgramRun()
    time.sleep(2)
    robot.PauseMotion()
    time.sleep(2)
    robot.ResumeMotion()
    time.sleep(2)
    robot.CloseRPC()
    return 0

設置可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDIConfig(config)``"
    "描述", "設置可配置CI端口功能"
    "必選參數", "
    - ``config``：CI0-CI7功能編碼陣列,  0-無;1-起弧成功;2-焊機準備;3-傳送帶檢測;4-暫停;5-恢復;6-啟動;7-停止;
      8-暫停/恢復;9-啟動/停止;10-腳踏拖動;11-移至作業原點;12-手自動切換;
      13-焊絲尋位成功;14-運動中斷;15-啟動主程序;16-啟動倒帶;17-啟動確認;
      18-光電檢測信號X;19-光電檢測信號Y;20-外部急停輸入信號1;21-外部急停輸入信號2;
      22-一級縮減模式;23-二級縮減模式;24-三級縮減模式(停止);25-恢復焊接;26-終止焊接;
      27-輔助拖動開啟;28-輔助拖動關閉;29-輔助拖動開啟/關閉;30-清除所有錯誤;
      31-手自動切換(高低電平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定點跟蹤開始/結束"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取控制箱可配置CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDIConfig()``"
    "描述", "獲取控制箱可配置CI端口功能"
    "必選參數", "
    - ``config``：CI0-CI7功能編碼陣列,  0-無;1-起弧成功;2-焊機準備;3-傳送帶檢測;4-暫停;5-恢復;6-啟動;7-停止;
      8-暫停/恢復;9-啟動/停止;10-腳踏拖動;11-移至作業原點;12-手自動切換;
      13-焊絲尋位成功;14-運動中斷;15-啟動主程序;16-啟動倒帶;17-啟動確認;
      18-光電檢測信號X;19-光電檢測信號Y;20-外部急停輸入信號1;21-外部急停輸入信號2;
      22-一級縮減模式;23-二級縮減模式;24-三級縮減模式(停止);25-恢復焊接;26-終止焊接;
      27-輔助拖動開啟;28-輔助拖動關閉;29-輔助拖動開啟/關閉;30-清除所有錯誤;
      31-手自動切換(高低電平);32-使能;33-去使能;34-使能/去使能(上升下降沿);35-定點跟蹤開始/結束"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDOConfig(config)``"
    "描述", "設置可配置CO端口功能"
    "必選參數", "
    - ``config``：CO0-CO7功能編碼陣列,0-無;1-機器人報錯;2-機器人運動中;3-噴塗啟停;4-噴塗清槍;5-送氣信號;6-起弧信號;7-點動送絲;
      8-反向送絲;9-JOB輸入口1;10-JOB輸入口2;11-JOB輸入口3;12-傳送帶啟停控制;13-機器人暫停中;14-到達作業原點;
      15-到達干涉區;16-焊絲尋位啟停控制;17-機器人啟動完成;18-程序啟動停止;19-自動手動模式;20-急停輸出信號1-安全;
      21-急停輸出信號2-安全;22-LUA腳本程序運行停止;23-安全狀態輸出-安全;24-保護性停止狀態輸出-安全;
      25-機器人運動中-安全;26-機器人縮減模式-安全;27-機器人非縮減模式-安全;28-機器人非停止;29-機器人報錯-指令點錯誤;
      30-機器人報錯-驅動器錯誤;31-機器人報錯-超出軟限位錯誤;32-機器人報錯-碰撞錯誤;33-機器人報錯-活動從站數量錯誤;
      34-機器人報錯-從站錯誤;35-機器人報錯-IO錯誤;36-機器人報錯-夾爪錯誤;37-機器人報錯-文件錯誤;38-機器人報錯-奇異位姿錯誤;
      39-機器人報錯-驅動器通信錯誤;40-機器人報錯-參數錯誤;41-機器人報錯-外部軸超出軟限位錯誤;42-機器人警告-警告;
      43-機器人警告-安全門警告;44-機器人警告-運動警告;45-機器人警告-干涉區警告;46-機器人警告-安全牆警告;
      47-使能狀態;48-斷線自動抬升中;49-立方體1干涉警告;50-立方體2干涉警告;51-立方體3干涉警告;52-立方體4干涉警告;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取可配置CO端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDOConfig()``"
    "描述", "獲取可配置CO端口功能"
    "必選參數", "
    - ``config``：CO0-CO7功能編碼陣列,0-無;1-機器人報錯;2-機器人運動中;3-噴塗啟停;4-噴塗清槍;5-送氣信號;6-起弧信號;7-點動送絲;
      8-反向送絲;9-JOB輸入口1;10-JOB輸入口2;11-JOB輸入口3;12-傳送帶啟停控制;13-機器人暫停中;14-到達作業原點;
      15-到達干涉區;16-焊絲尋位啟停控制;17-機器人啟動完成;18-程序啟動停止;19-自動手動模式;20-急停輸出信號1-安全;
      21-急停輸出信號2-安全;22-LUA腳本程序運行停止;23-安全狀態輸出-安全;24-保護性停止狀態輸出-安全;
      25-機器人運動中-安全;26-機器人縮減模式-安全;27-機器人非縮減模式-安全;28-機器人非停止;29-機器人報錯-指令點錯誤;
      30-機器人報錯-驅動器錯誤;31-機器人報錯-超出軟限位錯誤;32-機器人報錯-碰撞錯誤;33-機器人報錯-活動從站數量錯誤;
      34-機器人報錯-從站錯誤;35-機器人報錯-IO錯誤;36-機器人報錯-夾爪錯誤;37-機器人報錯-文件錯誤;38-機器人報錯-奇異位姿錯誤;
      39-機器人報錯-驅動器通信錯誤;40-機器人報錯-參數錯誤;41-機器人報錯-外部軸超出軟限位錯誤;42-機器人警告-警告;
      43-機器人警告-安全門警告;44-機器人警告-運動警告;45-機器人警告-干涉區警告;46-機器人警告-安全牆警告;
      47-使能狀態;48-斷線自動抬升中;49-立方體1干涉警告;50-立方體2干涉警告;51-立方體3干涉警告;52-立方體4干涉警告;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDIConfig(config)``"
    "描述", "設置末端可配置End-CI端口功能"
    "必選參數", "
    - ``config``：End CI0-CI1功能編碼陣列,0-無;1-拖動示教工具開關;2-點記錄信號;3-手自動切換（脈衝信號）;4-TPD記錄啟動/停止;5-暫停運動;
      6-恢復運動;7-啟動;8-停止;9-暫停/恢復;10-啟動/停止;11-力傳感器輔助拖動開啟;12-力傳感器輔助拖動關閉;
      13-力傳感器輔助拖動開啟/關閉;14-激光檢測信號X;15-激光檢測信號Y;16-PTP運動至作業原點;17-運動中斷，根據信號停止當前運動;
      18-啟動主程序;19-啟動倒帶;20-啟動確認;21-恢復焊接;22-終止焊接;23-清除錯誤;24-手自動切換（高低電平）
      25-使能;26-去使能;27-使能/去使能;28-激光伺服跟蹤啟停信號;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取末端可配置End-CI端口功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDIConfig()``"
    "描述", "獲取末端可配置End-CI端口功能"
    "必選參數", "
    - ``config``：End CI0-CI1功能編碼陣列,0-無;1-拖動示教工具開關;2-點記錄信號;3-手自動切換（脈衝信號）;4-TPD記錄啟動/停止;5-暫停運動;
      6-恢復運動;7-啟動;8-停止;9-暫停/恢復;10-啟動/停止;11-力傳感器輔助拖動開啟;12-力傳感器輔助拖動關閉;
      13-力傳感器輔助拖動開啟/關閉;14-激光檢測信號X;15-激光檢測信號Y;16-PTP運動至作業原點;17-運動中斷，根據信號停止當前運動;
      18-啟動主程序;19-啟動倒帶;20-啟動確認;21-恢復焊接;22-終止焊接;23-清除錯誤;24-手自動切換（高低電平）
      25-使能;26-去使能;27-使能/去使能;28-激光伺服跟蹤啟停信號;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置控制箱可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDIConfigLevel(config)``"
    "描述", "設置控制箱可配置CI有效狀態"
    "必選參數", "
    - ``config``：CI0-CI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取控制箱可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDIConfigLevel()``"
    "描述", "獲取控制箱可配置CI有效狀態"
    "必選參數", "
    - ``config``：CI0-CI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置控制箱可配置CO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDOConfigLevel(config)``"
    "描述", "設置控制箱可配置CO有效狀態"
    "必選參數", "
    - ``config``：CO0-CO7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取控制箱可配置CO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDOConfigLevel()``"
    "描述", "獲取控制箱可配置CO有效狀態"
    "必選參數", "
    - ``config``：CO0-CO7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置末端可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDIConfigLevel(config)``"
    "描述", "設置末端可配置CI有效狀態"
    "必選參數", "
    - ``config``：CI0-CI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取末端可配置CI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDIConfigLevel()``"
    "描述", "獲取末端可配置CI有效狀態"
    "必選參數", "
    - ``config``：CI0-CI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置控制箱標準DI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStandardDILevel(config)``"
    "描述", "設置控制箱標準DI有效狀態"
    "必選參數", "
    - ``config``：DI0-DI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取控制箱標準DI有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetStandardDILevel()``"
    "描述", "獲取控制箱標準DI有效狀態"
    "必選參數", "
    - ``config``：DI0-DI7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置控制箱標準DO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStandardDOLevel(config)``"
    "描述", "設置控制箱標準DO有效狀態"
    "必選參數", "
    - ``config``：DO0-DO7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取控制箱標準DO有效狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetStandardDOLevel()``"
    "描述", "獲取控制箱標準DO有效狀態"
    "必選參數", "
    - ``config``：DO0-DO7端口有效狀態陣列；0-高電平有效；1-低電平有效"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
IO配置相關的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')


    def TestIOConfig(self):
        # 設置和獲取DI配置
        setDIConfig = [1, 2, 3, 4, 5, 6, 7, 8]
        getDIConfig = [0] * 8
        rtn = robot.SetDIConfig(setDIConfig)
        print(f"SetDIConfig rtn is {rtn}")
        rtn, getDIConfig = robot.GetDIConfig()
        print(f"GetDIConfig rtn is {rtn}, value is {getDIConfig[0]} {getDIConfig[1]} {getDIConfig[2]} {getDIConfig[3]} {getDIConfig[4]} {getDIConfig[5]} {getDIConfig[6]} {getDIConfig[7]}")

        # 設置和獲取DO配置
        setDOConfig = [9, 10, 11, 12, 13, 14, 15, 16]
        getDOConfig = [0] * 8
        rtn = robot.SetDOConfig(setDOConfig)
        print(f"SetDOConfig rtn is {rtn}")
        rtn, getDOConfig = robot.GetDOConfig()
        print(f"GetDOConfig rtn is {rtn}, value is {getDOConfig[0]} {getDOConfig[1]} {getDOConfig[2]} {getDOConfig[3]} {getDOConfig[4]} {getDOConfig[5]} {getDOConfig[6]} {getDOConfig[7]}")

        # 設置和獲取工具DI配置
        setToolDIConfig = [17, 18]
        getToolDIConfig = [0] * 2
        rtn = robot.SetToolDIConfig(setToolDIConfig)
        print(f"SetToolDIConfig rtn is {rtn}")
        rtn, getToolDIConfig = robot.GetToolDIConfig()
        print(f"GetToolDIConfig rtn is {rtn}, value is {getToolDIConfig[0]} {getToolDIConfig[1]}")

        # 設置和獲取DI電平配置（0: 低電平有效, 1: 高電平有效）
        setDIConfigLevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getDIConfigLevel = [0] * 8
        rtn = robot.SetDIConfigLevel(setDIConfigLevel)
        print(f"SetDIConfigLevel rtn is {rtn}")
        rtn, getDIConfigLevel = robot.GetDIConfigLevel()
        print(f"GetDIConfigLevel rtn is {rtn}, value is {getDIConfigLevel[0]} {getDIConfigLevel[1]} {getDIConfigLevel[2]} {getDIConfigLevel[3]} {getDIConfigLevel[4]} {getDIConfigLevel[5]} {getDIConfigLevel[6]} {getDIConfigLevel[7]}")

        # 設置和獲取DO電平配置（0: 低電平有效, 1: 高電平有效）
        setDOConfigLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getDOConfigLevel = [0] * 8
        rtn = robot.SetDOConfigLevel(setDOConfigLevel)
        print(f"SetDOConfigLevel rtn is {rtn}")
        rtn, getDOConfigLevel = robot.GetDOConfigLevel()
        print(f"GetDOConfigLevel rtn is {rtn}, value is {getDOConfigLevel[0]} {getDOConfigLevel[1]} {getDOConfigLevel[2]} {getDOConfigLevel[3]} {getDOConfigLevel[4]} {getDOConfigLevel[5]} {getDOConfigLevel[6]} {getDOConfigLevel[7]}")

        # 設置和獲取工具DI電平配置
        setToolDIConfigLevel = [1, 0]
        getToolDIConfigLevel = [0] * 2
        rtn = robot.SetToolDIConfigLevel(setToolDIConfigLevel)
        print(f"SetToolDIConfigLevel rtn is {rtn}")
        rtn, getToolDIConfigLevel = robot.GetToolDIConfigLevel()
        print(f"GetToolDIConfigLevel rtn is {rtn}, value is {getToolDIConfigLevel[0]} {getToolDIConfigLevel[1]}")

        # 設置和獲取標準DI電平配置
        setStandardDILevel = [1, 1, 1, 1, 0, 0, 0, 0]
        getStandardDILevel = [0] * 8
        rtn = robot.SetStandardDILevel(setStandardDILevel)
        print(f"SetStandardDILevel rtn is {rtn}")
        rtn, getStandardDILevel = robot.GetStandardDILevel()
        print(f"GetStandardDILevel rtn is {rtn}, value is {getStandardDILevel[0]} {getStandardDILevel[1]} {getStandardDILevel[2]} {getStandardDILevel[3]} {getStandardDILevel[4]} {getStandardDILevel[5]} {getStandardDILevel[6]} {getStandardDILevel[7]}")

        # 設置和獲取標準DO電平配置
        setStandardDOLevel = [0, 0, 0, 0, 1, 1, 1, 1]
        getStandardDOLevel = [0] * 8
        rtn = robot.SetStandardDOLevel(setStandardDOLevel)
        print(f"SetStandardDOLevel rtn is {rtn}")
        rtn, getStandardDOLevel = robot.GetStandardDOLevel()
        print(f"GetStandsrdDOLevel rtn is {rtn}, value is {getStandardDOLevel[0]} {getStandardDOLevel[1]} {getStandardDOLevel[2]} {getStandardDOLevel[3]} {getStandardDOLevel[4]} {getStandardDOLevel[5]} {getStandardDOLevel[6]} {getStandardDOLevel[7]}")

        # 等待2秒
        time.sleep(2)

        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)

    # 調用測試函數
    TestIOConfig(robot)