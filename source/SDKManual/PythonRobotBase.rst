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
    "必選參數", "- ``ip``：機器人的IP地址，默認出廠IP爲“192.168.58.2”"
    "默認參數", "無"
    "返回值", "- 成功：返回一個機器人對象
    - 失敗：創建的對象會被銷燬"

關閉RPC連接
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CloseRPC()``"
    "描述", "關閉RPC連接"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "無"

查詢SDK版本號
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKVersion()``"
    "描述", "查詢SDK版本號"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode
    - ``sdk``：SDK版本號、控制器版本號"

獲取控制器IP
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetControllerIP()``"
    "描述", "查詢控制器IP"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``ip``：控制器IP"

控制機器人進入或退出拖動示教模式
++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DragTeachSwitch(state)``"
    "描述", "控制機器人進入或退出拖動示教模式"
    "必選參數", "- ``state``：1-進入拖動示教模式，0-退出拖動示教模式"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

查詢機器人是否處於拖動模式
++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``IsInDragTeach()``"
    "描述", "查詢機器人是否處於拖動示教模式"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``：0-非拖動示教模式，1-拖動示教模式"

控制機器人上使能或下使能
++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotEnable(state)``"
    "描述", "控制機器人上使能或下使能"
    "必選參數", "- ``state``：1-上使能，0-下使能"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "


控制機器人手自動模式切換
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Mode(state)``"
    "描述", "控制機器人手自動模式切換"
    "必選參數", "- ``state``：0-自動模式，1-手動模式"
    "默認參數", "無"
    "返回值", "錯誤碼  成功-0  失敗- errcode"

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

初始化日誌參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoggerInit(output_model=1, file_path="", file_num=5)``"
    "描述", "初始化日誌參數"
    "必選參數", "無"
    "默認參數", "- ``output_model``：輸出模式，0-直接輸出；1-緩衝輸出；2-異步輸出，默認1
    - ``file_path``：文件保存路徑+名稱，名稱必須是xxx.log的形式，比如/home/fr/linux/fairino.log。默認執行程序所在路徑，默認名稱爲：fairino_year+month+data.log(如:fairino_2024_03_13.log);
    - ``file_num``：滾動存儲的文件數量，1~20個，默認值爲5。單個文件上限50M;"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置日誌過濾等級
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoggerLevel(lvl=1)``"
    "描述", "設置日誌過濾等級"
    "必選參數", "無"
    "默認參數", "- ``lvl``：過濾等級值，值越小輸出日誌越少, 1-error, 2-warnning, 3-inform, 4-debug,默認值是1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人基礎控制代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    time.sleep(1)
    error,version = robot.GetSDKVersion()
    print(f"SDK version: {version}")
    error,ip = robot.GetControllerIP()
    print(f"controller ip: {ip}")

    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(state=1)
    time.sleep(1)
    error,state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.DragTeachSwitch(state=0)
    time.sleep(1)
    error,state = robot.IsInDragTeach()
    print(f"drag state: {state}")
    time.sleep(3)
    robot.RobotEnable(0)
    time.sleep(3)
    robot.RobotEnable(1)
    robot.Mode(0)
    time.sleep(1)
    robot.Mode(1)
    time.sleep(1)
    rtn = robot.HiSpeedManualSwitch(1)
    print(f"change high speed mode : {rtn}")
    time.sleep(1)
    rtn = robot.HiSpeedManualSwitch(0)
    print(f"change low speed mode : {rtn}")
    time.sleep(3)
    robot.ShutDownRobotOS()
  
    robot.CloseRPC()

獲取機器人軟件版本
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareVersion()``"
    "描述", "獲取機器人軟件版本"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``robotModel``：機器人模型
    - ``webVersion``：web版本
    - ``controllerVersion``：控制器版本"

獲取機器人硬件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveHardVersion()``"
    "描述", "獲取機器人硬件版本信息"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

獲取機器人固件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveFirmVersion()``"
    "描述", "獲取機器人固件版本信息"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

獲取機器人軟固件版本代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn,robotModel, webversion, controllerVersion = robot.GetSoftwareVersion()
    print(f"Getsoftwareversion rtn is: {rtn}")
    print(f"robotmodel is: {robotModel}, webversion is: {webversion}, controllerVersion is: {controllerVersion}\n")
    rtn,ctrlBoxBoardversion, driver1version, driver2version,driver3version, driver4version, driver5version,driver6version, endBoardversion = robot.GetHardwareversion()
    print(f"GetHardwareversion rtn is: {rtn}")
    print(f"GetHardwareversion get hardware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    rtn,ctrlBoxBoardversion, driver1version, driver2version,driver3version, driver4version, driver5version,driver6version, endBoardversion = robot.GetFirmwareVersion()
    print(f"GetFirmwareversion rtn is: {rtn}")
    print(f"GetFirmwareversion get firmware version is: {ctrlBoxBoardversion}, {driver1version}, {driver2version}, "
          f"{driver3version}, {driver4version}, {driver5version}, {driver6version}, {endBoardversion}\n")
    robot.CloseRPC()
