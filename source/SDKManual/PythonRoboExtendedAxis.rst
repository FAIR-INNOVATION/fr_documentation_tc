擴展軸
=============

.. toctree:: 
    :maxdepth: 5

設定485擴展軸參數
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "描述", "設定485擴展軸參數"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``servoCompany``：伺服驅動器廠商，1-戴納泰克；
    - ``servoModel``：伺服驅動器型號，1-FD100-750C；
    - ``servoSoftVersion``：伺服驅動器軟體版本，1-V1.0；
    - ``servoResolution``：編碼器分辨率；
    - ``axisMechTransRatio``：機械傳動比；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    ret = robot = Robot.RPC('192.168.58.2')

    ret =robot.AuxServoSetParam(1,1,1,1,131072,15.45)#設定485擴展軸參數
    print("AuxServoSetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetParam(1)#取得485擴展軸配置參數
    print("AuxServoGetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetStatus(1)#查詢狀態
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret =robot.AuxServoClearError(1)#清除錯誤
    print("AuxServoClearError",ret)
    sleep(1)

取得485擴展軸配置參數
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetParam(servoId)``"
    "描述", "取得485擴展軸配置參數"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode;
    - ``servoCompany``：伺服驅動器廠商，1-戴納泰克；
    - ``servoModel``：伺服驅動器型號，1-FD100-750C；
    - ``servoSoftVersion``：伺服驅動器軟體版本，1-V1.0；
    - ``servoResolution``：編碼器分辨率；
    - ``axisMechTransRatio``：機械傳動比；"

代碼範例
-----------
參考設定485擴展軸參數的代碼範例

設定485擴展軸使能/去使能
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoEnable(servoId,status)``"
    "描述", "設定485擴展軸使能/去使能"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``status``：使能狀態，0-去使能， 1-使能;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret =robot.AuxServoSetControlMode(1,0)#設定為位置模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式後需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查詢狀態
    print("AuxServoGetStatus",ret)
    sleep(1)
    i=1
    while(i<5):
        ret =robot.AuxServoSetTargetPos(1,300*i,30)#位置模式運動，速度30
        print("AuxServoSetTargetPos",ret)
        sleep(11)
        ret =robot.AuxServoGetStatus(1)#查詢狀態
        print("AuxServoGetStatus",ret)
        sleep(1)
        i=i+1

設定485擴展軸控制模式
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetControlMode(servoId,mode)``"
    "描述", "設定485擴展軸控制模式"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``mode``：控制模式，0-位置模式，1-速度模式;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
---------------------------------
參考設定485擴展軸使能/去使能的代碼範例

設定485擴展軸目標位置(位置模式)
++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "描述", "設定485擴展軸目標位置(位置模式)"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``pos``：目標位置，mm或°；
    - ``speed``：目標速度，mm/s或°/s;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
---------------------------------
參考設定485擴展軸使能/去使能的代碼範例

設定485擴展軸目標速度（速度模式）
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "描述", "設定485擴展軸目標速度（速度模式）"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``speed``：目標速度，mm/s或°/s;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret = robot.AuxServoSetControlMode(1, 1)  # 設定為速度模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式後需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查詢狀態
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 30)  # 速度模式運動，速度30
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)

    ret = robot.AuxServoGetStatus(1)  # 查詢狀態
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 60)  # 速度模式運動，速度60
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)
    ret = robot.AuxServoGetStatus(1)  # 查詢狀態
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 0)  # 結束速度模式運動前應當把速度設為0
    print("AuxServoSetTargetSpeed", ret)
    sleep(3)
    ret = robot.AuxServoGetStatus(1)  # 查詢狀態
    print("AuxServoGetStatus", ret)
    sleep(1)

設定485擴展軸目標轉矩(力矩模式)-暫未開放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetTorque(servoId,torque)``"
    "描述", "設定485擴展軸目標轉矩(力矩模式)"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``torque``：目標力矩，Nm;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定485擴展軸回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "描述", "設定485擴展軸回零"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``mode``：回零模式，1-目前位置回零；2-負限位回零；3-正限位回零;
    - ``searchVel``： 回零速度，mm/s或°/s;
    - ``latchVel``：箍位速度，mm/s或°/s;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
    
代碼範例
---------------------------------
參考設定485擴展軸使能/去使能的代碼範例

清除485擴展軸錯誤訊息
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoClearError(servoId)``"
    "描述", "清除485擴展軸錯誤訊息"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
    
代碼範例
---------------------------------
參考設定485擴展軸參數的代碼範例

取得485擴展軸伺服狀態
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetStatus(servoId)``"
    "描述", "取得485擴展軸伺服狀態"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode;
    - ``servoErrCode``：伺服驅動器故障碼
    - ``servoState``：伺服驅動器狀態 bit0:0-未使能；1-使能;  bit1:0-未運動；1-正在運動;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成；
    - ``servoPos``：伺服當前位置 mm或°；
    - ``servoSpeed``：伺服當前速度 mm/s或°/s；
    - ``servoTorque``：伺服當前轉矩Nm；"

代碼範例
---------------------------------
參考設定485擴展軸使能/去使能的代碼範例

設定狀態回饋中485擴展軸資料軸號-暫未開放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServosetStatusID(servoId)``"
    "描述", "設定狀態回饋中485擴展軸資料軸號"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetAcc(acc, dec)``"
    "描述", "設定485擴展軸運動加減速度"
    "必選參數", "- ``acc``：485擴展軸運動加速度
    - ``dec``：485擴展軸運動减速度"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetEmergencyStopAcc(acc, dec)``"
    "描述", "設定485擴展軸急停加減速度"
    "必選參數", "- ``acc``：485擴展軸急停加速度
    - ``dec``：485擴展軸急停减速度"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetEmergencyStopAcc()``"
    "描述", "取得485擴展軸急停加減速度"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``acc``：485擴展軸急停加速度
    - ``dec``：485擴展軸急停减速度"

取得485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetAcc()``"
    "描述", "取得485擴展軸運動加減速度"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``acc``：485擴展軸運動加速度
    - ``dec``：485擴展軸運動减速度"

UDP擴展軸通訊參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v3.8.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevSetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum)``"
    "描述", "UDP擴展軸通訊參數配置"
    "必選參數", "
    - ``ip``：PLC IP地址；
    - ``port``：連接埠號；
    - ``period``：通訊週期(ms，暫不開放)；
    - ``lossPkgTime``：丟包檢測時間(ms)；
    - ``lossPkgNum``：丟包次數；
    - ``disconnectTime``：通訊斷開確認時長；
    - ``reconnectEnable``：通訊斷開自動重連啟用 0-不啟用 1-啟用；
    - ``reconnectPeriod``：重連週期間隔(ms)；
    - ``reconnectNum``：重連次數
    - ``selfConnect``：斷電重啟是否自動建立連接; 0-不建立連接; 1-建立連接"
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
    #UDP擴展軸通訊參數配置
    error = robot.ExtDevSetUDPComParam('192.168.58.88',2021,2,50,5,50,1,2,5)
    print("ExtDevSetUDPComParam return:",error)
    #UDP擴展軸通訊參數配置
    error = robot.ExtDevGetUDPComParam()
    print("ExtDevGetUDPComParam return:",error)
    
取得UDP擴充軸通訊參數
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevGetUDPComParam()``"
    "描述", "取得UDP擴充軸通訊參數"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "
    - 錯誤碼 成功-0 失敗- errcode；
    - ``ip``：PLC IP地址；
    - ``port``：連接埠號；
    - ``period``：通訊週期(ms，暫不開放)；
    - ``lossPkgTime``：丟包檢測時間(ms)；
    - ``lossPkgNum``：丟包次數；
    - ``disconnectTime``：通訊斷開確認時長；
    - ``reconnectEnable``：通訊斷開自動重連啟用 0-不啟用 1-啟用；
    - ``reconnectPeriod``：重連週期間隔(ms)；
    - ``reconnectNum``：重連次數"
 
加載UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevLoadUDPDriver()``"
    "描述", "加載UDP通信"
    "必選參數", "無"
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
    #加載UDP通信
    error = robot.ExtDevLoadUDPDriver()
    print("ExtDevLoadUDPDriver return:",error)
    #卸載UDP通信
    error = robot.ExtDevUnloadUDPDriver()
    print("ExtDevUnloadUDPDriver return:",error)
     
卸載UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUnloadUDPDriver()``"
    "描述", "卸載UDP通信"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
     
UDP擴充軸通訊異常斷開後恢復連接
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComReset()``"
    "描述", "UDP擴充軸通訊異常斷開後恢復連接"
    "必選參數", "無"
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
    #UDP擴充軸通訊異常斷開後恢復連接
    error = robot.ExtDevUDPClientComReset()
    print("ExtDevUDPClientComReset return:",error)
    #UDP擴充軸通訊異常斷開後關閉通訊
    error = robot.ExtDevUDPClientComClose()
    print("ExtDevUDPClientComClose return:",error)
         
UDP擴充軸通訊異常斷開後關閉通訊
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComClose()``"
    "描述", "UDP擴充軸通訊異常斷開後關閉通訊"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
         
設定擴展機器人相對擴展軸位置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotPosToAxis(installType)``"
    "描述", "設定扩展機器人相对擴展軸位置"
    "必選參數", "- ``installType``：0-機器人安裝在外部軸上，1-機器人安裝在外部軸外；"
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
    #設定扩展機器人相对擴展軸位置
    error = robot.SetRobotPosToAxis(1)
    print("SetRobotPosToAxis return:",error)
    #設定擴展軸系統DH參數配置
    error = robot.SetAxisDHParaConfig(4,128.5,206.4,0,0,0,0,0,0,)
    print("SetAxisDHParaConfig return:",error)
    #UDP擴充軸參數配置
    error = robot.ExtAxisParamConfig(1,1,0,1000,-1000,1000,1000,1.905,262144, 200,1,1,0)
    print("ExtAxisParamConfig return:",error)

設定擴展軸系統DH參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxisDHParaConfig(axisConfig,axisDHd1,axisDHd2,axisDHd3,axisDHd4,axisDHa1, axisDHa2,axisDHa3,axisDHa4)``"
    "描述", "設定擴展軸系統DH參數配置"
    "必選參數", "
    - ``axisConfig``：外部軸構型，0-單自由度直線滑軌，1-兩自由度L型變位機，2-三自由度，3-四自由度，4-單自由度變位機；
    - ``axisDHd1``：外部軸DH參數d1 mm；
    - ``axisDHd2``：外部軸DH參數d2 mm；
    - ``axisDHd3``：外部軸DH參數d3 mm；
    - ``axisDHd4``：外部軸DH參數d4 mm；
    - ``axisDHa1``：外部軸DH參數a1 mm；
    - ``axisDHa2``：外部軸DH參數a2 mm；
    - ``axisDHa3``：外部軸DH參數a3 mm；
    - ``axisDHa4``：外部軸DH參數a4 mm；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

UDP擴充軸參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisParamConfig(axisId, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc,axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType)``"
    "描述", "UDP擴充軸參數配置"
    "必選參數", "
    - ``axisId``：軸號[1-4]；
    - ``axisType``：擴展軸類型 0-平移；1-旋轉；
    - ``axisDirection``：擴展軸方向 0-正向；1-反向；
    - ``axisMax``：擴展軸最大位置 mm；
    - ``axisMin``：擴展軸最小位置 mm；
    - ``axisVel``：速度mm/s；
    - ``axisAcc``：加速度mm/s2；
    - ``axisLead``：導程mm；
    - ``encResolution``：編碼器分辨率；
    - ``axisOffect``：焊缝起始點擴展軸偏移量；
    - ``axisCompany``：驅動器廠商 1-禾川；2-匯川；3-松下；
    - ``axisModel``：驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG；
    - ``axisEncType``：編碼器類型 0-增量；1-絕對值；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
         
設定擴展軸座標系參考點-四點法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetRefPoint(pointNum)``"
    "描述", "設定擴展軸座標系參考點-四點法"
    "必選參數", "- ``pointNum``：點編號[1-4]；"
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
    #設定擴展軸座標系參考點-四點法
    error = robot.ExtAxisSetRefPoint(1)
    print("ExtAxisComputeECoordSys(1) return:",error)
             
計算擴展軸座標系-四點法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisComputeECoordSys()``"
    "描述", "計算擴展軸座標系-四點法"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode;
    - ``coord``：擴展軸座標系值[x,y,z,rx,ry,rz]；"
                  
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #計算擴展軸座標系-四點法
    error,coord = robot.ExtAxisComputeECoordSys()
    print("ExtAxisComputeECoordSys() return:",error,coord)
    #應用擴展軸座標系
    error = robot.ExtAxisActiveECoordSys(1,1,coord,1)
    print("ExtAxisActiveECoordSys() return:",error)
         
應用擴展軸座標系
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisActiveECoordSys(applyAxisId,axisCoordNum,coord,calibFlag)``"
    "描述", "應用擴展軸座標系"
    "必選參數", "
    - ``applyAxisId``:擴展軸編號 bit0-bit3对应擴展軸編號1-4，如應用擴展軸1和3，则是 0b 0000 0101,也就是5；
    - ``axisCoordNum``：擴展軸座標系編號；
    - ``coord``：座標系值[x,y,z,rx,ry,rz]；
    - ``calibFlag``：標定標誌 0-否，1-是；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
             
設定標定參考點在變位機末端座標系下位姿
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRefPointInExAxisEnd(pos)``"
    "描述", "設定標定參考點在變位機末端座標系下位姿"
    "必選參數", "- ``pos``：位元姿值[x,y,z,rx,ry,rz]；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
                      
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #設定標定參考點在變位機末端座標系下位姿
    error = robot.SetRefPointInExAxisEnd(desc_pos)
    print("SetRefPointInExAxisEnd(1) return:",error)
                 
變位機座標系參考點設置-四點法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorSetRefPoint(pointNum)``"
    "描述", "變位機座標系參考點設置-四點法"
    "必選參數", "- ``pointNum``：點編號[1-4]；"
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
    #變位機座標系參考點設置-四點法
    error = robot.SetRefPointInExAxisEnd(desc_pos)
    print("SetRefPointInExAxisEnd(1) return:",error)
                     
變位機座標系計算-四點法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorComputeECoordSys()``"
    "描述", "變位機座標系計算-四點法"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode;
    - ``coord``：变位机座標系值[x,y,z,rx,ry,rz]；"
                            
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #變位機座標系計算-四點法
    error,coord = robot.PositionorComputeECoordSys()
    print("PositionorComputeECoordSys() return:",error,coord)
        
末端感測器暫存器寫入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端感測器暫存器寫入"
    "必選參數", "
    - ``devAddr``： 設備地址編號 0-255
    - ``regHAddr``：暫存器位址高8位
    - ``regLAddr``：暫存器位址低8位
    - ``regNum``：暫存器個數 0-255
    - ``data1``：寫入暫存器數值1
    - ``data2``：寫入暫存器數值2
    - ``isNoBlock``：0-阻塞；1-非阻塞
    "
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode；"
                          
UDP擴展軸使能
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisServoOn(axisID, status)``"
    "描述", "UDP擴展軸使能"
    "必選參數", "- ``axisID``：軸號[1-4]；
    - ``status``：0-去使能；1-使能；"
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
    #UDP擴展軸去使能
    error = robot.ExtAxisServoOn(1,0)
    print("ExtAxisServoOn return:",error)
    #UDP擴展軸使能
    error = robot.ExtAxisServoOn(1,1)
    print("ExtAxisServoOn return:",error)
    #UDP擴展軸回零
    error = robot.ExtAxisSetHoming(1,0,40,40)
    print("ExtAxisSetHoming return:",error)
    time.sleep(1)
    #UDP擴展軸點動開始
    error = robot.ExtAxisStartJog(1,1,20,20,20)
    print("ExtAxisStartJog return:",error)
    time.sleep(1)
    #UDP擴展軸點動停止
    error = robot.ExtAxisStopJog(1)
    print("ExtAxisStopJog return:",error)

UDP擴展軸回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetHoming(axisID, mode, searchVel, latchVel)``"
    "描述", "UDP擴展軸回零"
    "必選參數", "
    - ``axisID``：軸號[1-4]；
    - ``mode``：回零方式 0當前位置回零，1负限位回零，2-正限位回零；
    - ``searchVel``：尋零速度(mm/s)；
    - ``latchVel``：尋零箍位速度(mm/s)；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

UDP擴展軸點動開始
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStartJog( axisID, direction, vel, acc, maxDistance)``"
    "描述", "UDP擴展軸點動開始"
    "必選參數", "
    - ``axisID``：軸號[1-4]；
    - ``direction``：轉動方向 0-反向；1-正向；
    - ``vel``：速度(mm/s)；
    - ``acc``：加速度(mm/s)；
    - ``maxDistance``：最大點動距離；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

UDP擴展軸點動停止
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStopJog(axisID)``"
    "描述", "UDP擴展軸點動停止"
    "必選參數", "- ``axisID``：軸號[1-4]；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
    
設定擴充DO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDO(DONum,bOpen,smooth,block)``"
    "描述", "設定擴充DO"
    "必選參數", "
    - ``DONum``： DO編號；
    - ``bOpen``：開關 True-開,False-關；
    - ``smooth``：是否平滑 True -是, False -否；
    - ``block``：是否阻塞 True -是, False -否；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
                                    
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #設定擴充DO
    error = robot.SetAuxDO(1,True,False,True)
    print("GetAuxAI",error)
    #設定擴充AO
    error = robot.SetAuxAO(1,60,True)
    print("SetAuxAO",error)
    #設定擴充DI輸入濾波時間
    error = robot.SetAuxDIFilterTime(10,False)
    print("SetAuxDIFilterTime",error)
    #設定擴展AI輸入濾波時間
    error = robot.SetAuxAIFilterTime(10,True)
    print("SetAuxAIFilterTime",error)
    #等待擴充DI輸入
    error = robot.WaitAuxDI(0,False,100,False)
    print("WaitAuxDI",error)
    #等待擴展AI輸入
    error = robot.WaitAuxAI(0,0,100,500,False)
    print("WaitAuxAI",error)
    #取得擴展AI值
    error = robot.GetAuxAI(0,False)
    print("GetAuxAI",error)
    #取得擴展DI值
    error = robot.GetAuxDI(0,True)
    print("GetAuxDI",error)
        
設定擴充AO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAO(AONum,value,block)``"
    "描述", "設定擴充AO"
    "必選參數", "
    - ``AONum``： AO編號；
    - ``value``：類比量值[0-4095]；
    - ``block``：是否阻塞 True -是, False -否；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
設定擴充DI輸入濾波時間
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDIFilterTime(filterTime)``"
    "描述", "設定擴充DI輸入濾波時間"
    "必選參數", "- ``filterTime``： 濾波時間(ms)；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
設定擴展AI輸入濾波時間
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAIFilterTime(AINum,filterTime)``"
    "描述", "設定擴展AI輸入濾波時間"
    "必選參數", "
    - ``AINum``： AI編號；
    - ``filterTime``： 濾波時間(ms)；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
等待擴充DI輸入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxDI(DINum,bOpen,time,errorAlarm)``"
    "描述", "等待擴充DI輸入"
    "必選參數", "
    - ``DINum``： DI編號；
    - ``bOpen``：開關 True-開,False-關；
    - ``time``：最大等待時間(ms)；
    - ``errorAlarm``：是否繼續運動 True-是,False-否"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxAI(,AINum,sign,value,time,errorAlarm)``"
    "描述", "等待擴展AI輸入"
    "必選參數", "
    - ``AINum``： AI編號；
    - ``sign``：0-大於；1-小於；
    - ``value``：AI值；
    - ``time``：最大等待時間(ms)；
    - ``errorAlarm``：是否繼續運動 True-是,False-否"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
取得擴展DI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxDI(DINum,isNoBlock)``"
    "描述", "取得擴展DI值"
    "必選參數", "
    - ``DINum``： DI編號；
    - ``isNoBlock``：是否阻塞 True-阻塞 false-非阻塞；"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode；
    - ``isOpen``： 0-關；1-開；"
          
取得擴展AI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxAI(AINum,isNoBlock)``"
    "描述", "取得擴展AI值"
    "必選參數", "
    - ``AINum``： AI編號；
    - ``isNoBlock``：是否阻塞 True-阻塞 False-非阻塞"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode；
    - ``value``：輸入值；"
          
UDP擴展軸運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisMove(pos,ovl)``"
    "描述", "UDP擴展軸運動"
    "必選參數", "- ``pos=[exaxis[0],exaxis[1],exaxis[2],exaxis[3]]``：目標位置 軸1位置~軸4位置;
    - ``ovl``：速度百分比"
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
    error,joint_pos = robot.GetActualJointPosDegree()
    print("GetActualJointPosDegree",error,joint_pos)
    e_pos =[-10,0,0,0]
    joint_pos[0] = joint_pos[0]+30
    #UDP擴展軸异步運動
    error = robot.ExtAxisMove(e_pos,30)
    print("ExtAxisMove",error)
    print("joint_pos",joint_pos)
    error = robot.MoveJ(joint_pos,0,0,exaxis_pos=e_pos)
    print("MoveJ",error)
              
UDP擴展軸與機器人關節運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveJ(joint_pos,desc_pos,tool,user,exaxis_pos, vel=20.0, acc=0.0, ovl= 100.0,  blendT=-1.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP擴展軸與機器人關節運動同步運動"
    "必選參數", "
    - ``joint_pos``： 目標關節位置，單位 [°]；
    - ``desc_pos``：目標笛卡兒位姿，單位 [mm][°]
    - ``tool``：工具號，[0~14]
    - ``user``：工件號，[0~14]
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位"
    "默認參數", "
    - ``vel``： 速度百分比，[0~100] 默認20.0；
    - ``acc``：加速度百分比，[0~100] 暫不開放,默認0.0 ；
    - ``ovl``：速度縮放因子，[0~100] 預設100.0  ；
    - ``blendT``：[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0；
    - ``offset_pos``：位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "傳回值", "錯誤碼 成功-0 失敗- errcode；"
                                        
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
    point_num=1
    id=1
    coord=[100,200,300,0,0,0,]
    type=0
    install=0
    #1.設定工具坐標系
    # robot.SetToolPoint(point_num)  #設定工具參考點-六點法
    # robot.ComputeTool() #計算工具座標系
    # robot.SetTcp4RefPoint()   #設定工具參考點-四點法
    # robot.ComputeTcp4()   #計算工具座標系-四點法
    # robot.SetToolCoord(id, coord,type,install)  #設定應用工具坐標系
    # robot.SetToolList(id, coord,type,install)   #設定應用工具坐標系列表
    #2.設定UDP通訊參數，並載入UDP通信
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
    robot.ExtDevLoadUDPDriver();
    #3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)#單軸变位机及DH參數
    robot.SetRobotPosToAxis(1);  #擴充軸安裝位置
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)#伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數
    #4.設定所選的軸使能、回零
    robot.ExtAxisServoOn(1, 0);
    robot.ExtAxisSetHoming(1, 0, 20, 3);
    #5.進行擴充軸座標系標定及應用(注意：變位機和直線滑軌的標定介面不同，以下時變位機的標定介面)
    pos =[0,0,0,0,0,0] #輸入您的標定點座標
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)#您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定
    error,coord = robot.PositionorComputeECoordSys()#計算擴展軸標定結果
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1); #將標定結果應用到擴展軸座標系
    method=1
    #6.在擴充軸上標定工件坐標系，您需要用到以下接口
    # robot.SetWObjCoordPoint( point_num)
    # error,coord=robot.ComputeWObjCoord( method)
    # robot.SetWObjCoord(id,coord)
    # robot.SetWObjList(id, coord)
    #7.記錄您的同步關節運動起始點
    startdescPose = [0,0,0,0,0,0]#輸入您的座標
    startjointPos = [0,0,0,0,0,0]#輸入您的座標
    startexaxisPos = [0,0,0,0,]#輸入您的座標
    #8.記錄您的同步關節運動終點座標
    enddescPose = [0,0,0,0,0,0]#輸入您的座標
    endjointPos = [0,0,0,0,0,0]#輸入您的座標
    endexaxisPos = [0,0,0,0,]#輸入您的座標
    #9.編寫同步運動程式
    #運動到起始點，假設應用的工具坐標系、工件坐標係都是1
    robot.ExtAxisMove(startexaxisPos, 20);
    robot.MoveJ(startjointPos,  1, 1, desc_pos=startdescPose,exaxis_pos=startexaxisPos);
    #開始同步運動
    robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, endexaxisPos);
                  
UDP擴展軸與機器人直線運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveL(self, joint_pos,desc_pos, tool, user, exaxis_pos, vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP擴展軸與機器人直線運動同步運動"
    "必選參數", "
    - ``joint_pos``： 目標關節位置，單位 [°]；
    - ``desc_pos``：目標笛卡兒位姿，單位 [mm][°]；
    - ``tool``：工具號，[0~14]；
    - ``user``：工件號，[0~14]；
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位；"
    "默認參數", "
    - ``vel``： 速度百分比，[0~100] 默認20.0；
    - ``acc``：加速度百分比，[0~100] 暫不開放,默認0.0；
    - ``ovl``：速度縮放因子，[0~100] 預設100.0；
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0；
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0；
    - ``offset_pos``：位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "傳回值", "錯誤碼 成功-0 失敗- errcode；"
                                            
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.Mode(0)
    time.sleep(1)
    e_pos =[-20,0,0,0]
    joint_pos0 = [114.089,-85.740, 119.106,-129.884,-91.655, 79.642]
    desc_pos0= [-87.920,-178.539,-64.513,-175.471,7.664,139.650]
    #UDP擴展軸與機器人直線運動同步運動
    error = robot.ExtAxisSyncMoveL(joint_pos0,desc_pos0,1,1,e_pos)
    print("ExtAxisSyncMoveL",error)
                      
UDP擴展軸與機器人圓弧運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveC(joint_pos_p, desc_pos_p, tool_p, user_p,exaxis_pos_p, joint_pos_t, desc_pos_t, tool_t, user_t,exaxis_pos_t,vel_p=20.0, acc_p=100.0, offset_flag_p=0, offset_pos_p =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0)``"
    "描述", " UDP擴展軸與機器人圓弧運動同步運動"
    "必選參數", "
    - ``joint_pos_p``： 路徑點關節位置，單位 [°] ；
    - ``desc_pos_p``：路徑點笛卡爾位姿，單位 [mm][°]；
    - ``tool_p``：路徑點工具號，[0~14]；
    - ``user_p``：路徑點工件號，[0~14]；
    - ``exaxis_pos_p``：路徑點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]；
    - ``joint_pos_t``：目標點關節位置，單位 [°] ；
    - ``desc_pos_t``：目標點笛卡爾位姿，單位 [mm][°]；
    - ``tool_t``：工具號，[0~14]；
    - ``user_t``：工件號，[0~14]；
    - ``exaxis_pos_t``：目標點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]；"
    "默認參數", "
    - ``vel_p``: 路徑點速度百分比，[0~100] 默認20.0；
    - ``acc_p``: 路徑點加速度百分比，[0~100] 暫不開放,默認0.0 ；   
    - ``offset_flag_p``: 路徑點是否偏移[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0；
    - ``offset_pos_p``: 路徑點位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``vel_t``: 目標點速度百分比，[0~100] 默認20.0；
    - ``acc_t``: 目標點加速度百分比，[0~100] 暫不開放 默認0.0；
    - ``offset_flag_t``: 目標點是否偏移[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0；
    - ``offset_pos_t``: 目標點位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``ovl``: 速度縮放因子，[0~100] 預設100.0；
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，單位 [mm] 默認-1.0；"
    "傳回值", "錯誤碼 成功-0 失敗- errcode；"
                                                
代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.Mode(0)
    time.sleep(1)
    desc_pos_mid =[-131.2748107910156, -60.21242523193359, -22.55266761779785, 175.9907989501953, 5.92541742324829, 145.5211791992187]
    desc_pos_end =[-91.3530502319336, -174.5040588378906, -64.93866729736328, 177.1370544433593, 15.96347618103027, 136.1746368408203]
    joint_pos_mid = [120.9549040841584, -109.8869943146658, 134.1448068146658, -126.2150709699876, -88.6738087871287, 79.6419593131188]
    joint_pos_end =[110.1896078279703, -89.01601659189356, 125.5532806698638, -139.7967831451114, -82.93198387221534, 79.6452225788985]
    # #UDP擴展軸與機器人圓弧運動同步運動
    time.sleep(3)
    error = robot.ExtAxisSyncMoveC(joint_pos_mid,desc_pos_mid,1,1,[-10,0,0,0],joint_pos_end,desc_pos_end,1,1,[-20,0,0,0])
    print("ExtAxisSyncMoveC",error)

可移動裝置控制
+++++++++++++++++
.. versionadded:: python SDK-v2.0.5

可移動裝置使能
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorEnable(enable)``"
    "描述", "可移動裝置使能"
    "必選參數", "- ``enable``：使能狀態，0-去使能，1-使能"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

可移動裝置回零
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorHoming()``"
    "描述", "可移動裝置回零"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

可移動裝置直線運動
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveL(distance, vel)``"
    "描述", "可移動裝置直線運動"
    "必選參數", "- ``distance``：直線運動距離（mm）
    - ``vel``：直線運動速度百分比（0-100）"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

可移動裝置圓弧運動
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveC(radio, angle, vel)``"
    "描述", "可移動裝置圓弧運動"
    "必選參數", "- ``radio``：圓弧運動半徑（mm）
    - ``angle``：圓弧運動角度（°）
    - ``vel``：圆弧運動速度百分比（0-100）"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

可移動裝置停止運動
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "可移動裝置停止運動"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 0)
    robot.ExtDevLoadUDPDriver()
    robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0)

    robot.TractorEnable(False)
    time.sleep(2)
    robot.TractorEnable(True)
    time.sleep(2)
    robot.TractorHoming()
    time.sleep(2)
    robot.TractorMoveL(100, 20)
    time.sleep(5)
    robot.TractorMoveL(-100, 20)
    time.sleep(5)
    robot.TractorMoveC(300, 90, 20)
    time.sleep(4)
    error = robot.TractorStop()
    print("TractorStop return ", error)

獲取擴展軸座標系
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v3.8.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisGetCoord()``"
    "描述", "獲取擴展軸座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：擴展軸座標系"
