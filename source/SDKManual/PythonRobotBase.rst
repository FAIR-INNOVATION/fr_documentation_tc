機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RPC(ip)``"
    "描述", "實例化一個機器人對象"
    "必選參數", "- ``ip``：機器人的IP位址，預設出廠IP為“192.168.58.2”"
    "默認參數", "無"
    "傳回值", "- 成功：回傳一個機器人對象
    - 失敗：建立的物件會被銷毀"
     
代碼範例
--------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

關閉rpc連接
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CloseRPC()``"
    "描述", "關閉rpc連接"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "無"
     
代碼範例
--------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.CloseRPC()

查詢SDK版本號
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKVersion()``"
    "描述", "查詢SDK版本號"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗-errcode
    - ``sdk``：SDK版本號、控制器版本號"

代碼範例
-----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret,version  = robot.GetSDKVersion()    #查詢SDK版本號
    if ret ==0:
        print("SDK版本號為", version )
    else:
        print("查詢失敗，錯誤碼為",ret)

獲取控制器IP
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetControllerIP()``"
    "描述", "查詢控制器IP"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``ip``：控制器IP"

代碼範例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret,ip = robot.GetControllerIP()    #查詢控制器IP
    if ret ==0:
        print("控制器IP為", ip)
    else:
        print("查詢失敗，錯誤碼為",ret)

控制機器人手自動模式切換
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Mode(state)``"
    "描述", "控制機器人手自動模式切換"
    "必選參數", "- ``state``：0-自動模式，1-手動模式"
    "默認參數", "無"
    "傳回值", "錯誤碼  成功-0  失败- errcode"

代碼範例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #機器人手自動模式切換
    ret = robot.Mode(0)   #機器人切入自動運作模式
    print("機器人切入自動運作模式", ret)
    time.sleep(1)
    ret = robot.Mode(1)   #機器人切入自動運作模式
    print("機器人切入自動運作模式", ret)

機器人拖曳模式
+++++++++++++++++

控制機器人進入或退出拖曳示教模式
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DragTeachSwitch(state)``"
    "描述", "控制機器人進入或退出拖曳示教模式"
    "必選參數", "- ``state``：1-進入拖曳示教模式，0-退出拖曳示教模式"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

查詢機器人是否處於拖曳模式
----------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``IsInDragTeach()``"
    "描述", "查詢機器人是否處於拖曳示教模式"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``state``：0-非拖曳示教模式，1-拖曳示教模式"

代碼範例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #機器人手自動模式切換
    ret = robot.Mode(0)   #機器人切入自動運作模式
    print("機器人切入自動運作模式", ret)
    time.sleep(1)
    ret = robot.Mode(1)   #機器人切入自動運作模式
    print("機器人切入自動運作模式", ret)

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #機器人进入或退出拖動示教模式
    ret = robot.Mode(1) #機器人切入自動運作模式
    print("機器人切入自動運作模式", ret)
    time.sleep(1)
    ret = robot.DragTeachSwitch(1)  #機器人切入拖曳示教模式，必須在手動模式下才能切入拖曳示教模式
    print("機器人切入拖曳示教模式", ret)
    time.sleep(1)
    ret,state = robot.IsInDragTeach()    #查詢是否處於拖曳示教模式，1-拖曳示教模式，0-非拖曳示教模式
    if ret == 0:
        print("目前拖曳示教模式狀態：", state)
    else:
        print("查詢失敗，錯誤碼為：",ret)
    time.sleep(3)
    ret = robot.DragTeachSwitch(0)  #機器人切入非拖曳示教模式，必須在手動模式下才能切入非拖曳示教模式
    print("機器人切入非拖動示教模式", ret)
    time.sleep(1)
    ret,state = robot.IsInDragTeach()    #查詢是否處於拖曳示教模式，1-拖曳示教模式，0-非拖曳示教模式
    if ret == 0:
        print("目前拖曳示教模式狀態：", state)
    else:
        print("查詢失敗，錯誤碼為：",ret)

控制機器人上使能或下使能
++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotEnable(state)``"
    "描述", "控制機器人上使能或下使能"
    "必選參數", "- ``state``：1-上使能，0-下使能"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #機器人上使能或下使能
    ret = robot.RobotEnable(0)   #機器人下使能
    print("機器人下使能", ret)
    time.sleep(3)
    ret = robot.RobotEnable(1)   #機器人上使能，機器人上電後預設自動上使能
    print("機器人上使能", ret)

關節扭力功率檢測
++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPowerLimit(status, power)``"
    "描述", "關節扭力功率檢測"
    "必選參數", "- ``state``：0-關閉，1-開啟
    - ``power``：設定最大功率(W)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

設定機器人 20004 連接埠回饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateSamplePeriod(period)``"
    "描述", "設定機器人 20004 連接埠回饋週期"
    "必選參數", "- ``period``：機器人 20004 連接埠回饋週期(ms)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得機器人 20004 連接埠回饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealtimeStateSamplePeriod()``"
    "描述", "取得機器人 20004 連接埠回饋週期"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``period``：機器人 20004 連接埠回饋週期(ms)"

機器人軟體升級
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SoftwareUpgrade(filePath, block)``"
    "描述", "機器人軟體升級"
    "必選參數", "- ``filePath``：軟體升級包全路徑
    - ``block``：是否阻塞至升級完成 true:阻塞；false:非阻塞"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode "

取得機器人軟體升級狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareUpgradeState()``"
    "描述", "取得機器人軟體升級狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``state``：機器人軟體包升級狀態，0：空閒或上傳升級包中，1~100：升級完成百分比，-1：升級軟體失敗，-2：校驗失敗，-3：版本校驗失敗，-4：解壓失敗，-5：使用者配置升級失敗，-6：週邊配置升級失敗，-7：擴展軸配置升級失敗，-8：機器人配置升級失敗，-9：DH參數配置升級失敗"

獲取機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealTimeState()``"
    "描述", "獲取機器人狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``robot_state_pkg``：機器人狀態結構體"

獲取控制箱SN碼
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotSN()``"
    "描述", "獲取控制箱SN碼"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``SNCode``：控制箱SN碼"

關閉機器人操作系統
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ShutDownRobotOS()``"
    "描述", "關閉機器人操作系統"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取SmartTool按鈕狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSmarttoolBtnState()``"
    "描述", "獲取SmartTool按鈕狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``：SmartTool手柄按鈕狀態;(bit0:0-通信正常；1-通信掉線；bit1-撤銷操作；bit2-清空程序；bit3-A鍵；bit4-B鍵；bit5-C鍵；bit6-D鍵；bit7-E鍵；bit8-IO鍵；bit9-手自動；bit10開始)"

程式碼範例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
        while True:
        error,state = robot.GetSmarttoolBtnState()
        print(f"{state:016b}")
        time.sleep(0.1)