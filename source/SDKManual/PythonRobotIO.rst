機器人IO
============

.. toctree:: 
    :maxdepth: 5

設定控制箱數位量輸出
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDO(id, status, smooth=0, block=0)``"
    "描述", "設定控制箱數位量輸出"
    "必選參數", "-  ``id``:io編號，範圍[0~15]；
    - ``status``:0-關，1-開；"
    "默認參數", "- ``smooth``:0-不平滑，1-平滑 默認0;
    - ``block``:0-阻塞，1-非阻塞 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 測試控制箱DO
    for i in range(0,16):
        error = robot.SetDO(i,1)      #開啟控制箱DO
    time.sleep(1)
    for i in range(0,16):
        robot.SetDO(i,0)      #關閉控制箱DO

設定工具數位量輸出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolDO (id, status, smooth=0, block=0)``"
    "描述", "設定工具數位量輸出"
    "必選參數", "-  ``id``:io編號，範圍[0~1]；
    - ``status``:0-關，1-開；"
    "默認參數", "- ``smooth``:0-不平滑，1-平滑；
    - ``block``:0-阻塞，1-非阻塞。"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 測試工具DO
    error_tooldo = 0
    for i in range(0,2):
        error = robot.SetToolDO(i,1)    #打開工具DO
    robot.WaitMs(1000)
    for i in range(0,2):
        error = robot.SetToolDO(i,0)    #關閉工具DO

設定控制箱類比輸出
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAO(id,value,block=0)``"
    "描述", "設定控制箱類比輸出"
    "必選參數", "- ``id``:io編號，範圍[0~1]；
    - ``value``:電流或電壓值百分比，範圍[0~100%]对应電流值[0~20mA]或電壓[0~10V]；"
    "默認參數", "- ``block``:[0]-阻塞，[1]-非阻塞 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 測試控制箱AO
    error = robot.SetAO(0,100.0)
    print("設定AO0錯誤碼:", error)
    error = robot.SetAO(1,100.0)
    print("設定AO1錯誤碼:", error)

設定工具類比輸出
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolAO(id,value,block=0)``"
    "描述", "設定工具類比輸出"
    "必選參數", "- ``id``:io編號，範圍[0]；
    - ``value``:電流或電壓值百分比，範圍[0~100%]对应電流值[0~20mA]或電壓[0~10V]；"
    "默認參數", "- ``block``:[0]-阻塞，[1]-非阻塞 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 测试末端AO
    error = robot.SetToolAO(0,100.0)
    print("設定ToolAO0錯誤碼:", error)
    Robot.WaitMs(1000)
    error = robot.SetToolAO(0,0.0)
    print("設定ToolAO0錯誤碼:", error)

取得控制箱數位量輸入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDI(id, block=0)``"
    "描述", "取得控制箱數位量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~15]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``di``: 0-低電平，1-高電平"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetDI(0,0)
    print("獲取DI0",error)

取得工具數位量輸入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolDI(id, block=0)``"
    "描述", "取得工具數位量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode
    - ``di``: 0-低電平，1-高電平"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    tool_di = robot.GetToolDI(1,0)
    print("獲取ToolDI",tool_di)

等待控制箱數位量輸入
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitDI(id,status,maxtime,opt)``"
    "描述", "等待控制箱數位量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~15]；
    - ``status``:0-關，1-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱DI
    error = robot.WaitDI(0,1,max_waittime,0)
    print("WaitDI錯誤碼",error)

等待控制箱多路數字量輸入
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMultiDI(mode,id,status,maxtime,opt)``"
    "描述", "等待控制箱多路數字量輸入"
    "必選參數", "- ``mode``:[0]-多路与，[1]-多路或；
    - ``id``:io編號，bit0~bit7對應DI0~DI7，bit8~bit15對應CI0~CI7；
    - ``status``:bit0~bit7对应DI0~DI7狀態，bit8~bit15对应CI0~CI7狀態位的狀態[0]-關，[1]-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待。"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱多路DI
    error = robot.WaitMultiDI(1,3,1,max_waittime,0)
    print("WaitMultiDI錯誤碼",error)

等待工具數位量輸入
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolDI(id,status,maxtime,opt)``"
    "描述", "等待末端数字量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；
    - ``status``:0-關，1-開；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待工具DI
    error = robot.WaitToolDI(1,1,max_waittime,0)
    print("WaitToolDI錯誤碼",error)

取得控制箱模擬量輸入
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAI(id, block = 0)``"
    "描述", "取得控制箱模擬量輸入"
    "必選參數", "- ``id``:io編號，範圍[0~1]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0 "
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``value``: 輸入電流或電壓值百分比，範圍 [0~100] 对应電流值 [0~20mA] 或電壓 [0~10V]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetAI(0)
    print("獲取AI0",error)

取得工具類比輸入
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolAI (id, block = 0)``"
    "描述", "獲取末端類比量輸入"
    "必選參數", "- ``id``:io編號，範圍[0]；"
    "默認參數", "- ``block``:0-阻塞，1-非阻塞 默認0"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``value``: 輸入電流或電壓值百分比，範圍 [0~100] 对应電流值 [0~20mA] 或電壓 [0~10V]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetToolAI(0)
    print("獲取ToolAI0",error)

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
    - ``opt``:超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待控制箱AI
    error = robot.WaitAI(0,0,50,max_waittime,1)         #忽略超时提示程序继续執行
    print("WaitAI錯誤碼",error)

等待工具類比輸入
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitToolAI(id,sign,value,maxtime,opt)``"
    "描述", "等待末端類比量輸入"
    "必選參數", "- ``id``:io編號，範圍[0]；
    - ``sign``:0-大於，1-小於
    - ``value``:輸入電流或電壓值百分比，範圍[0~100]對應電流值[0~20mA]或電壓[0~10V]；
    - ``maxtime``:最大等待時間，單位[ms]；
    - ``opt``:超時後策略，0-程式停止並提示超時，1-忽略超時提示程式繼續執行，2-一直等待"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    max_waittime = 2000
    #等待工具AI
    error = robot.WaitToolAI(0,0,50,max_waittime,0)
    print("WaitToolAI錯誤碼",error)

設定控制箱DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag)``"
    "描述", "設定控制箱DO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')
    time.sleep(5)
    error = robot.SetDO(1,1)
    print("SetDO 1  return:",error)

    error = robot.SetDO(3,1)
    print("SetDO 3  return:",error)

    error = robot.SetToolDO(1,1)
    print("SetToolDO return:",error)

    error = robot.SetAO(0,25)
    print("SetAO 0   return:",error)

    error = robot.SetAO(1,87)
    print("SetAO 1  return:",error)

    error = robot.SetToolAO(0,54)
    print("SetToolAO return:",error)

    error = robot.SetOutputResetCtlBoxDO(1)
    print("SetOutputResetCtlBoxDO return:",error)

    error = robot.SetOutputResetCtlBoxAO(1)
    print("SetOutputResetCtlBoxAO return:",error)

    error = robot.SetOutputResetAxleDO(1)
    print("SetOutputResetCtlBoxDO return:",error)

    error = robot.SetOutputResetAxleAO(1)
    print("SetOutputResetCtlBoxAO return:",error)

    error = robot.ProgramRun()
    print("ProgramRun return:",error)
    time.sleep(3)
    error = robot.ProgramStop()
    print("ProgramPause return:",error)

    time.sleep(5)

    error = robot.SetDO(1,1)
    print("SetDO 1  return:",error)

    error = robot.SetDO(3,1)
    print("SetDO 3  return:",error)

    error = robot.SetToolDO(1,1)
    print("SetToolDO return:",error)

    error = robot.SetAO(0,25)
    print("SetAO 0   return:",error)

    error = robot.SetAO(1,87)
    print("SetAO 1  return:",error)

    error = robot.SetToolAO(0,54)
    print("SetToolAO return:",error)
    error = robot.SetOutputResetCtlBoxDO(0)
    print("SetOutputResetCtlBoxDO return:",error)

    error = robot.SetOutputResetCtlBoxAO(0)
    print("SetOutputResetCtlBoxAO return:",error)

    error = robot.SetOutputResetAxleDO(0)
    print("SetOutputResetCtlBoxDO return:",error)

    error = robot.SetOutputResetAxleAO(0)
    print("SetOutputResetCtlBoxAO return:",error)

    error = robot.ProgramRun()
    print("ProgramRun return:",error)
    time.sleep(3)
    error = robot.ProgramStop()
    print("ProgramPause return:",error)

設定控制箱AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetCtlBoxDO(resetFlag)``"
    "描述", "設定控制箱AO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定末端工具DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleDO(resetFlag)``"
    "描述", "設定末端工具DO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定末端工具AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetAxleAO(resetFlag)``"
    "描述", "設定末端工具AO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定擴充DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtDO (resetFlag)``"
    "描述", "設定擴充DO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    error = robot.SetAuxDO(1,True,False,False)
    print("SetAuxDO 1  return:",error)

    error = robot.SetAuxDO(3,True,False,False)
    print("SetAuxDO 3  return:",error)

    error = robot.SetAuxAO(0,10,False)
    print("SetAuxAO 0   return:",error)

    error = robot.SetAuxAO(1,87,False)
    print("SetAuxAO 1  return:",error)

    error = robot.SetOutputResetExtDO(1)
    print("SetOutputResetExtDO return:",error)

    error = robot.SetOutputResetExtAO(1)
    print("SetOutputResetExtAO return:",error)

    error = robot.ProgramRun()
    print("ProgramRun return:",error)
    time.sleep(3)
    error = robot.ProgramStop()
    print("ProgramPause return:",error)

    time.sleep(3)
    error = robot.SetAuxDO(1,True,False,False)
    print("SetAuxDO 1  return:",error)

    error = robot.SetAuxDO(3,True,False,False)
    print("SetAuxDO 3  return:",error)

    error = robot.SetAuxAO(0,10,False)
    print("SetAuxAO 0   return:",error)

    error = robot.SetAuxAO(1,87,False)
    print("SetAuxAO 1  return:",error)

    error = robot.SetOutputResetExtDO(0)
    print("SetOutputResetExtDO return:",error)

    error = robot.SetOutputResetExtAO(0)
    print("SetOutputResetExtAO return:",error)

    error = robot.ProgramRun()
    print("ProgramRun return:",error)
    time.sleep(3)
    error = robot.ProgramStop()
    print("ProgramPause return:",error)

設定擴充AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetExtAO (resetFlag)``"
    "描述", "設定擴充AO停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：0-不復位；1-復位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"