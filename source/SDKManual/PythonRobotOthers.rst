其他接口
=================

.. toctree:: 
    :maxdepth: 5

下載點位表資料庫
+++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableDownLoad(point_table_name, save_file_path)``"
    "描述", "下載點位表資料庫"
    "必選參數", "- ``point_table_name``：要下載的點位表名稱    pointTable1.db;
    - ``save_file_path``:下載點位表的儲存路徑   C://test/;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableDownLoad("point_table_a.db","D://Desktop/testPoint/download/")
    print("PointTableDownLoad錯誤碼:",error)
 
上傳點位表資料庫
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpLoad(point_table_file_path)``"
    "描述", "上傳點位表資料庫"
    "必選參數", "- ``point_table_file_path``：上傳點位表的全路徑名   C://test/pointTable1.db"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:   

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpLoad("D://Desktop/testPoint/point_table_a.db")
    print("PointTableUpLoad錯誤碼:",error)

點位表切換
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableSwitch(point_table_name)``"
    "描述", "點位表切換"
    "必選參數", "- ``point_table_name``：要切換的點位表名稱   pointTable1.db,當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableSwitch("point_table_a.db")
    print("PointTableSwitch:",error)

點位表更新lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "描述", "點位表更新lua文件"
    "必選參數", "- ``point_table_name``：要切換的點位表名稱pointTable1.db,當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序
    - ``lua_file_name``: 要更新的lua檔案名稱 testPointTable.lua"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpdateLua("point_table_a.db","testpoint.lua")
    print("PointTableUpdateLua:",error)

初始化日誌參數
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoggerInit(output_model=1, file_path="", file_num=5)``"
    "描述", "初始化日誌參數(未初始化不開啟日志功能)"
    "必選參數", "無"
    "默認參數", "- ``output_model``：輸出模式，0-直接輸出；1-緩衝輸出；2-非同步輸出，默認1;
    - ``file_path``: 文件保存路徑+名称，名称必须是xxx.log的形式，如D://Desktop /fairino.log。默認執行程序所在路徑，默認名称fairino_year+month+ data.log(如:fairino_2024_03_13.log);
    - ``file_num``: 滚動存储的文件数量，1~20個，默認值為5。單個文件上限50M。"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LoggerInit(output_model=0,file_path="D://Desktop/fairino.log",file_num=3)
    robot.SetLoggerLevel(3)

設定日誌過濾等級
+++++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoggerLevel(lvl=1)``"
    "描述", "設定日誌過濾等級"
    "必選參數", "無"
    "默認參數", "- ``lvl``：过滤等级值，值越小輸出日志越少, 1-error, 2-warnning, 3-inform, 4-debug,默認值是1"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LoggerInit(output_model=0,file_path="D://Desktop/fairino.log",file_num=3)
    robot.SetLoggerLevel(3)

設置機器人週邊協議
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExDevProtocol(protocol)``"
    "描述", "設置機器人週邊協議"
    "必選參數", "- ``protocol``：機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret =robot.SetExDevProtocol(4098)
    print("SetExDevProtocol",ret)
    ret =robot.GetExDevProtocol()
    print("GetExDevProtocol",ret)

取得機器人週邊協議
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExDevProtocol()``"
    "描述", "取得機器人週邊協議"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode; 
    - ``protocol``: 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster"

末端感測器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfig(idCompany, idDevice, idSoftware, idBus)``"
    "描述", "末端感測器配置"
    "必選參數", "
    - ``idCompany``: 廠商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 類型，0-JUNKONG/RYR6T.V1.0
    - ``idSoftware``: 軟體版本，0-J1.0/HuiDe1.0(暫未開放)
    - ``idBus``: 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    "
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
    error = robot.AxleSensorConfig(18,0,0,0)
    print("AxleSensorConfig return:", error)

    error = robot.AxleSensorConfigGet()
    print("AxleSensorConfigGet return:", error)

    error = robot.AxleSensorActivate(0)
    print("AxleSensorActivate return:", error)
    time.sleep(1)
    error = robot.AxleSensorActivate(1)
    print("AxleSensorActivate return:", error)

    while(1):
        error = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0)
        print("AxleSensorRegWrite return:", error)
        
取得末端傳感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfigGet()``"
    "描述", "取得末端傳感器配置"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``idCompany``: 廠商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 類型，0-JUNKONG/RYR6T.V1.0"
        
末端感測器激活
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorActivate(actFlag)``"
    "描述", "末端感測器激活"
    "必選參數", "``actFlag``： 0-復位；1-激活"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``coord``: 座標系值[x,y,z,rx,ry,rz]"

末端感測器暫存器寫入
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端感測器暫存器寫入"
    "必選參數", "- ``devAddr``：設備地址編號 0-255
    - ``regHAddr``：暫存器位址高8位
    - ``regLAddr``：暫存器位址低8位
    - ``regNum``：暫存器個數 0-255
    - ``data1``：寫入暫存器數值1
    - ``data2``：寫入暫存器數值2
    - ``isNoBlock``：是否阻塞 0-阻塞；1-非阻塞"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

設定SmartTool停止/暫停後輸出是否重設
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOutputResetSmartToolDO(resetFlag)``"
    "描述", "設定SmartTool停止/暫停後輸出是否重設"
    "必選參數", "- ``resetFlag``：是否复位，0-不复位，1-复位"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleCommunicationParam()``"
    "描述", "取得末端通訊參數"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：資料位:資料位元支援（8,9），目前常用為 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用為 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用為 0
    - ``timeout``：超時時間:1~1000ms，此值需結合週邊裝置搭配設定合理的時間參數
    - ``timeoutTimes``：超時次數:1~10，主要進行超時重發，減少偶發異常提高使用者體驗
    - ``period``：週期性指令時間間隔:1~1000ms，主要用於週期性指令每次下發的時間間隔"

設定末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleCommunicationParam(baudRate, dataBit, stopBit, verify, timeout, timeoutTimes, period)``"
    "描述", "設定末端通訊參數"
    "必選參數", "- ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：資料位:資料位元支援（8,9），目前常用為 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用為 1
    - ``verify``：校验位:0-None，1-Odd，2-Even,目前常用為 0
    - ``timeout``：超時時間:1~1000ms，此值需結合週邊裝置搭配設定合理的時間參數
    - ``timeoutTimes``：超時次數:1~10，主要進行超時重發，減少偶發異常提高使用者體驗
    - ``period``：週期性指令時間間隔:1~1000ms，主要用於週期性指令每次下發的時間間隔"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

設定末端檔案傳輸類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleFileType(type)``"
    "描述", "設定末端檔案傳輸類型"
    "必選參數", "- ``type``：1-MCU升級文件,2-LUA文件"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

設定啟用末端LUA執行
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnable(enable)``"
    "描述", "設定啟用末端LUA執行"
    "必選參數", "- ``enable``：0-不啟用；1-啟用"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

末端LUA文件異常錯誤恢復
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRecoverAxleLuaErr(enable)``"
    "描述", "末端LUA文件異常錯誤恢復"
    "必選參數", "- ``status``：0-不恢復；1-恢復"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

獲取末端LUA執行啟用狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableStatus()``"
    "描述", "獲取末端LUA執行啟用狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``enable``：0-不啟用；1-啟用"

設定末端LUA末端設備啟用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnableDeviceType(forceSensorEnable, gripperEnable, IOEnable)``"
    "描述", "設定末端LUA末端設備啟用類型"
    "必選參數", "- ``forceSensorEnable``：力传感器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable``：IO设备啟用狀態，0-不啟用；1-啟用"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得末端LUA末端設備啟用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDeviceType()``"
    "描述", "取得末端LUA末端設備啟用類型"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``forceSensorEnable``：力传感器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable``：IO设备啟用狀態，0-不啟用；1-啟用"

取得目前配置的末端設備
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDevice()``"
    "描述", "取得目前配置的末端設備"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``forceSensorEnable[8]``：力传感器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable[8]``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable[8]``：IO设备啟用狀態，0-不啟用；1-啟用"

控制器日誌下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RbLogDownload(savePath)``"
    "描述", "控制器日誌下載"
    "必選參數", "- ``savePath``：保存文件路徑D://zDown/"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

所有數據源下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AllDataSourceDownload(savePath)``"
    "描述", "所有數據源下載"
    "必選參數", "- ``savePath``：保存文件路徑D://zDown/"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

數據備份包下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DataPackageDownload(savePath)``"
    "描述", "数据备份包下载"
    "必选参数", "- ``savePath``：保存文件路径D://zDown/"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"


下發SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSSHScpCmd(mode, sshname, sship, usr_file_url, robot_file_url)``"
    "描述", "下發SCP指令"
    "必選參數", "- ``mode``：0-上傳（上位機->控制器），1-下載（控制器->上位機）
    - ``sshname``：上位機用戶名
    - ``sship``：上位機ip地址
    - ``usr_file_url``：上位機文件路徑
    - ``robot_file_url``：機器人控制器文件路徑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

代碼示例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ssh_name = "fr"
    ssh_ip = "192.168.58.45"
    ssh_route = "/home/fr"
    ssh_robot_url = "/root/robot/dhpara.config"
    retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url)
    print(f"SetSSHScpCmd retval is: {retval}")
    print(f"robot url is: {ssh_robot_url}")

設置寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWideBoxTempFanMonitorParam(enable, period)``"
    "描述", "設置寬電壓控制箱溫度及風扇轉速監控參數"
    "必選參數", "- ``enable``：0-不使能監測；1-使能監測
    - ``period``：監測週期(s),範圍1-100"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWideBoxTempFanMonitorParam()``"
    "描述", "獲取寬電壓控制箱溫度及風扇轉速監控參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``enable``：0-不使能監測；1-使能監測
    - ``period``：監測週期(s),範圍1-100"