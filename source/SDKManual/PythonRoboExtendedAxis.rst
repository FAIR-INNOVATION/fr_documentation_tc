擴展軸
=============

.. toctree:: 
    :maxdepth: 5

設置485擴展軸參數
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "描述", "設置485擴展軸參數"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``servoCompany``：伺服驅動器廠商，1-戴納泰克；
    - ``servoModel``：伺服驅動器型號，1-FD100-750C；
    - ``servoSoftVersion``：伺服驅動器軟件版本，1-V1.0；
    - ``servoResolution``：編碼器分辨率；
    - ``axisMechTransRatio``：機械傳動比；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取485擴展軸配置參數
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetParam(servoId)``"
    "描述", "獲取485擴展軸配置參數"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode;
    - ``servoCompany``：伺服驅動器廠商，1-戴納泰克；
    - ``servoModel``：伺服驅動器型號，1-FD100-750C；
    - ``servoSoftVersion``：伺服驅動器軟件版本，1-V1.0；
    - ``servoResolution``：編碼器分辨率；
    - ``axisMechTransRatio``：機械傳動比；"

設置485擴展軸使能/去使能
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoEnable(servoId,status)``"
    "描述", "設置485擴展軸使能/去使能"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``status``：使能狀態，0-去使能， 1-使能;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸控制模式
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetControlMode(servoId,mode)``"
    "描述", "設置485擴展軸控制模式"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``mode``：控制模式，0-位置模式，1-速度模式;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸目標位置(位置模式)
++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "描述", "設置485擴展軸目標位置(位置模式)"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``pos``：目標位置，mm或°；
    - ``speed``：目標速度，mm/s或°/s;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸目標轉矩(力矩模式)-暫未開放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetTorque(servoId,torque)``"
    "描述", "設置485擴展軸目標轉矩(力矩模式)"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``torque``：目標力矩，Nm;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "描述", "設置485擴展軸回零"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``mode``：回零模式，1-當前位置回零；2-負限位回零；3-正限位回零;
    - ``searchVel``： 回零速度，mm/s或°/s;
    - ``latchVel``：箍位速度，mm/s或°/s;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

清除485擴展軸錯誤信息
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoClearError(servoId)``"
    "描述", "清除485擴展軸錯誤信息"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取485擴展軸伺服狀態
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetStatus(servoId)``"
    "描述", "獲取485擴展軸伺服狀態"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode;
    - ``servoErrCode``：伺服驅動器故障碼
    - ``servoState``：伺服驅動器狀態 bit0:0-未使能；1-使能;  bit1:0-未運動；1-正在運動;  bit2 0-正限位未觸發；1-正限位觸發；bit3 0-負限位未觸發；1-負限位觸發；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成；
    - ``servoPos``：伺服當前位置 mm或°；
    - ``servoSpeed``：伺服當前速度 mm/s或°/s；
    - ``servoTorque``：伺服當前轉矩Nm；"

設置485擴展軸目標速度(速度模式)
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "描述", "設置485擴展軸目標速度(速度模式)"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；
    - ``speed``：目標速度，mm/s或°/s;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置狀態反饋中485擴展軸數據軸號
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServosetStatusID(servoId)``"
    "描述", "設置狀態反饋中485擴展軸數據軸號"
    "必選參數", "- ``servoId``：伺服驅動器ID，範圍[1-15],對應從站ID；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetAcc(acc, dec)``"
    "描述", "設置485擴展軸運動加減速度"
    "必選參數", "- ``acc``：485擴展軸運動加速度
    - ``dec``：485擴展軸運動減速度"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetEmergencyStopAcc(acc, dec)``"
    "描述", "設置485擴展軸急停加減速度"
    "必選參數", "- ``acc``：485擴展軸急停加速度
    - ``dec``：485擴展軸急停減速度"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetAcc()``"
    "描述", "獲取485擴展軸運動加減速度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``acc``：485擴展軸運動加速度
    - ``dec``：485擴展軸運動減速度"

獲取485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetEmergencyStopAcc()``"
    "描述", "獲取485擴展軸急停加減速度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``acc``：485擴展軸急停加速度
    - ``dec``：485擴展軸急停減速度"

擴展軸控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45)
    print(f"AuxServoSetParam is: {retval}")
    servoCompany = 0
    servoModel = 0
    servoSoftVersion = 0
    servoResolution = 0
    axisMechTransRatio = 0.0
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14)
    print(f"AuxServoSetParam is: {retval}")
    retval, servoCompany, servoModel, servoSoftVersion, servoResolution, axisMechTransRatio = robot.AuxServoGetParam(1)
    print(f"servoCompany {servoCompany}\n"
          f"servoModel {servoModel}\n"
          f"servoSoftVersion {servoSoftVersion}\n"
          f"servoResolution {servoResolution}\n"
          f"axisMechTransRatio {axisMechTransRatio}\n")
    retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36)
    print(f"AuxServoSetParam is: {retval}")
    time.sleep(3)
    robot.AuxServoSetAcc(3000, 3000)
    robot.AuxServoSetEmergencyStopAcc(5000, 5000)
    time.sleep(1)
    emagacc = 0.0
    emagdec = 0.0
    acc = 0.0
    dec = 0.0
    error,emagacc, emagdec = robot.AuxServoGetEmergencyStopAcc()
    print(f"emergency acc is {emagacc}  dec is {emagdec}")
    error,acc, dec = robot.AuxServoGetAcc()
    print(f"acc is {acc}  dec is {dec}")
    robot.AuxServoSetControlMode(1, 0)
    time.sleep(2)
    retval = robot.AuxServoEnable(1, 0)
    print(f"AuxServoEnable disenable {retval}")
    time.sleep(1)
    servoErrCode = 0
    servoState = 0
    servoPos = 0.0
    servoSpeed = 0.0
    servoTorque = 0.0
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoEnable(1, 1)
    print(f"AuxServoEnable enable {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoState {servoState}")
    time.sleep(1)
    retval = robot.AuxServoHoming(1, 1, 5, 1,100)
    print(f"AuxServoHoming {retval}")
    time.sleep(3)
    retval = robot.AuxServoSetTargetPos(1, 200, 30,100)
    print(f"AuxServoSetTargetPos {retval}")
    time.sleep(1)
    retval, servoErrCode, servoState, servoPos, servoSpeed, servoTorque = robot.AuxServoGetStatus(1)
    print(f"AuxServoGetStatus servoSpeed {servoSpeed}")
    time.sleep(8)
    robot.AuxServoSetControlMode(1, 1)
    time.sleep(2)
    robot.AuxServoEnable(1, 0)
    time.sleep(1)
    robot.AuxServoEnable(1, 1)
    time.sleep(1)
    robot.AuxServoSetTargetSpeed(1, 100, 80)
    time.sleep(5)
    robot.AuxServoSetTargetSpeed(1, 0, 80)
    robot.CloseRPC()

UDP擴展軸通訊參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevSetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum, selfConnect)``"
    "描述", "UDP擴展軸通訊參數配置"
    "必選參數", "
    - ``ip``：PLC IP地址；
    - ``port``：端口號；
    - ``period``：通訊週期(ms，暫不開放)；
    - ``lossPkgTime``：丟包檢測時間(ms)；
    - ``lossPkgNum``：丟包次數；
    - ``disconnectTime``：通訊斷開確認時長；
    - ``reconnectEnable``：通訊斷開自動重連使能 0-不使能 1-使能；
    - ``reconnectPeriod``：重連週期間隔(ms)；
    - ``reconnectNum``：重連次數
    - ``selfConnect``：斷電重啓是否自動建立連接；0-不建立連接；1-建立連接"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取UDP擴展軸通訊參數
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevGetUDPComParam()``"
    "描述", "獲取UDP擴展軸通訊參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "
    - 錯誤碼 成功-0  失敗- errcode；
    - ``ip``：PLC IP地址；
    - ``port``：端口號；
    - ``period``：通訊週期(ms，暫不開放)；
    - ``lossPkgTime``：丟包檢測時間(ms)；
    - ``lossPkgNum``：丟包次數；
    - ``disconnectTime``：通訊斷開確認時長；
    - ``reconnectEnable``：通訊斷開自動重連使能 0-不使能 1-使能；
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

UDP擴展軸通信異常斷開後恢復連接
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComReset()``"
    "描述", "UDP擴展軸通信異常斷開後恢復連接"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

UDP擴展軸通信異常斷開後關閉通訊
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComClose()``"
    "描述", "UDP擴展軸通信異常斷開後關閉通訊"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

UDP擴展軸參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisParamConfig(axisId, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc,axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType)``"
    "描述", "UDP擴展軸參數配置"
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
    - ``axisOffect``：焊縫起始點擴展軸偏移量；
    - ``axisCompany``：驅動器廠家 1-禾川；2-匯川；3-松下；
    - ``axisModel``：驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG；
    - ``axisEncType``：編碼器類型  0-增量；1-絕對值；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置擴展機器人相對擴展軸位置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotPosToAxis(installType)``"
    "描述", "設置擴展機器人相對擴展軸位置"
    "必選參數", "- ``installType``：0-機器人安裝在外部軸上，1-機器人安裝在外部軸外；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置擴展軸系統DH參數配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxisDHParaConfig(axisConfig,axisDHd1,axisDHd2,axisDHd3,axisDHd4,axisDHa1, axisDHa2,axisDHa3,axisDHa4)``"
    "描述", "設置擴展軸系統DH參數配置"
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"
                          
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

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
    - ``mode``：回零方式 0當前位置回零，1負限位回零，2-正限位回零；
    - ``searchVel``：尋零速度(mm/s)；
    - ``latchVel``：尋零箍位速度(mm/s)；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

UDP擴展軸配置與點動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
    print(f"ExtDevSetUDPComParam rtn is {rtn}")
    ip = ""
    port = 0
    period = 0
    lossPkgTime = 0
    lossPkgNum = 0
    disconnectTime = 0
    reconnectEnable = 0
    reconnectPeriod = 0
    reconnectNum = 0
    rtn,[ip, port, period, lossPkgTime, lossPkgNum,disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum] = robot.ExtDevGetUDPComParam()
    param_str = (f"\nip {ip}\nport {port}\nperiod {period}\nlossPkgTime {lossPkgTime}"
                 f"\nlossPkgNum {lossPkgNum}\ndisConntime {disconnectTime}"
                 f"\nreconnecable {reconnectEnable}\nreconnperiod {reconnectPeriod}"
                 f"\nreconnnun {reconnectNum}")
    print(f"ExtDevGetUDPComParam rtn is {rtn}{param_str}")
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
    rtn = robot.ExtAxisServoOn(2, 1)
    print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    print(f"ExtAxisSetHoming rtn is {rtn}")
    time.sleep(4)
    rtn = robot.SetRobotPosToAxis(1)
    print(f"SetRobotPosToAxis rtn is {rtn}")
    rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0)
    print(f"SetAxisDHParaConfig rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")
    time.sleep(3)
    robot.ExtAxisStartJog(1, 0, 10, 10, 30)
    time.sleep(1)
    robot.ExtAxisStopJog(1)
    time.sleep(3)
    robot.ExtAxisServoOn(1, 0)
    time.sleep(3)
    robot.ExtAxisStartJog(2, 0, 10, 10, 30)
    time.sleep(1)
    robot.ExtAxisStopJog(2)
    time.sleep(3)
    robot.ExtAxisServoOn(2, 0)
    robot.ExtDevUnloadUDPDriver()
    robot.CloseRPC()

設置擴展軸座標系參考點-四點法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetRefPoint(pointNum)``"
    "描述", "設置擴展軸座標系參考點-四點法"
    "必選參數", "- ``pointNum``：點編號[1-4]；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
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
    "返回值", "- 錯誤碼 成功-0  失敗- errcode;
    - ``coord``：擴展軸座標系值[x,y,z,rx,ry,rz]；"
                 
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

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
    "返回值", "- 錯誤碼 成功-0  失敗- errcode;
    - ``coord``：變位機座標系值[x,y,z,rx,ry,rz]；"
             
設置標定參考點在變位機末端座標系下位姿
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRefPointInExAxisEnd(pos)``"
    "描述", "設置標定參考點在變位機末端座標系下位姿"
    "必選參數", "- ``pos``：位姿值[x,y,z,rx,ry,rz]；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

應用擴展軸座標系
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisActiveECoordSys(applyAxisId,axisCoordNum,coord,calibFlag)``"
    "描述", "應用擴展軸座標系"
    "必選參數", "
    - ``applyAxisId``:擴展軸編號 bit0-bit3對應擴展軸編號1-4，如應用擴展軸1和3，則是 0b 0000 0101,也就是5；
    - ``axisCoordNum``：擴展軸座標系編號；
    - ``coord``：座標系值[x,y,z,rx,ry,rz]；
    - ``calibFlag``：標定標誌 0-否，1-是；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取擴展軸座標系
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisGetCoord()``"
    "描述", "獲取擴展軸座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：擴展軸座標系"

擴展軸座標系標定代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1)
    print(f"ExtDevSetUDPComParam rtn is {rtn}")
    rtn,udp_params = robot.ExtDevGetUDPComParam()
    ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum = udp_params
    patam = (
        f"\nip {ip}\nport {port}\nperiod {period}\nlossPkgTime {lossPkgTime}\n"
        f"lossPkgNum {lossPkgNum}\ndisConntime {disconnectTime}\nreconnecable {reconnectEnable}\n"
        f"reconnperiod {reconnectPeriod}\nreconnnun {reconnectNum}"
    )
    print(f"ExtDevGetUDPComParam rtn is {rtn}{patam}")
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
    rtn = robot.ExtAxisServoOn(2, 1)
    print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    print(f"ExtAxisSetHoming rtn is {rtn}")
    time.sleep(4)
    rtn = robot.SetRobotPosToAxis(1)
    print(f"SetRobotPosToAxis rtn is {rtn}")
    rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0)
    print(f"SetAxisDHParaConfig rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 1 rtn is {rtn}")
    rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0)
    print(f"ExtAxisParamConfig axis 2 rtn is {rtn}")
    toolCoord = [0, 0, 210, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    jSafe = [115.193, -96.149, 92.489, -87.068, -89.15, -83.488]
    j1 = [117.559, -92.624, 100.329, -96.909, -94.057, -83.488]
    j2 = [112.239, -90.096, 99.282, -95.909, -89.824, -83.488]
    j3 = [110.839, -83.473, 93.166, -89.22, -90.499, -83.487]
    j4 = [107.935, -83.572, 95.424, -92.873, -87.933, -83.488]
    descSafe = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc1 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc2 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc3 = [0.0,0.0,0.0,0.0,0.0,0.0]
    desc4 = [0.0,0.0,0.0,0.0,0.0,0.0]
    exaxisPos = [0.0,0.0,0.0,0.0]
    offdese = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, descSafe = robot.GetForwardKin(jSafe)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    error, desc1 = robot.GetForwardKin(j1)
    robot.MoveJ(joint_pos=j1,tool= 1,user= 0,vel= 100)
    time.sleep(2)
    actualTCPPos = [0.0,0.0,0.0,0.0,0.0,0.0]
    error, actualTCPPos = robot.GetActualTCPPose(0)
    robot.SetRefPointInExAxisEnd(actualTCPPos)
    rtn = robot.PositionorSetRefPoint(1)
    print(f"PositionorSetRefPoint 1 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc2 = robot.GetForwardKin(j2)
    rtn = robot.MoveJ(joint_pos=j2,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(2)
    print(f"PositionorSetRefPoint 2 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc3 = robot.GetForwardKin(j3)
    robot.MoveJ(joint_pos=j3,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(3)
    print(f"PositionorSetRefPoint 3 rtn is {rtn}")
    time.sleep(2)
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    robot.ExtAxisStartJog(1, 0, 50, 50, 10)
    time.sleep(1)
    robot.ExtAxisStartJog(2, 0, 50, 50, 10)
    time.sleep(1)
    error, desc4 = robot.GetForwardKin(j4)
    robot.MoveJ(joint_pos=j4,tool= 1,user= 0,vel= 100)
    rtn = robot.PositionorSetRefPoint(4)
    print(f"PositionorSetRefPoint 4 rtn is {rtn}")
    time.sleep(2)
    axisCoord = [0.0,0.0,0.0,0.0,0.0,0.0]
    error,axisCoord = robot.PositionorComputeECoordSys()
    robot.MoveJ(joint_pos=jSafe,tool= 1,user= 0,vel= 100)
    print(f"PositionorComputeECoordSys rtn is {axisCoord[0]} {axisCoord[1]} {axisCoord[2]} {axisCoord[3]} {axisCoord[4]} {axisCoord[5]}")
    rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1)
    print(f"ExtAxisActiveECoordSys rtn is {rtn}")
    robot.CloseRPC()
          
UDP擴展軸運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisMove(pos,ovl,blend=-1)``"
    "描述", "UDP擴展軸運動"
    "必選參數", "- ``pos=[exaxis[0],exaxis[1],exaxis[2],exaxis[3]]``：目標位置 軸1位置~軸4位置;
    - ``ovl``：速度百分比"
    "默認參數", "- ``blend``：平滑參數(mm或ms)，-1,等待運動完成，默認-1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
                                        
UDP擴展軸運動代碼示例
++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    axisPos = [20,0,0,0]
    robot.ExtAxisMove(axisPos, 50, -1)
    robot.CloseRPC()
    return 0

UDP擴展軸與機器人關節運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveJ(joint_pos,tool,user,exaxis_pos, desc_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl= 100.0,  blendT=-1.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP擴展軸與機器人關節運動同步運動"
    "必選參數", "
    - ``joint_pos``： 目標關節位置，單位 [°]；
    - ``desc_pos``：目標笛卡爾位姿，單位 [mm][°]
    - ``tool``：工具號，[0~14]
    - ``user``：工件號，[0~14]
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位"
    "默認參數", "
    - ``desc_pos``:目標笛卡爾位姿，單位 [mm][°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用正運動學求解返回值;
    - ``vel``： 速度百分比，[0~100] 默認20.0；
    - ``acc``：加速度百分比，[0~100] 暫不開放,默認0.0 ；
    - ``ovl``：速度縮放因子，[0~100] 默認100.0  ；
    - ``blendT``：[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0；
    - ``offset_pos``：位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "返回值", "錯誤碼 成功-0  失敗- errcode；"
                                        
UDP擴展軸與機器人關節運動同步運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 設置UDP通信參數並加載
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 設置擴展軸參數
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 擴展軸使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 擴展軸座標系標定
    pos = []  # 請在此填寫標定點座標
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 此操作應重複4次（用4個點）
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步運動起點與終點
    startdescPose = []  # 請填寫具體座標
    startjointPos = []  # 請填寫具體座標
    startexaxisPos = []  # 請填寫具體座標
    enddescPose = []  # 請填寫具體座標
    endjointPos = []  # 請填寫具體座標
    endexaxisPos = []  # 請填寫具體座標
    # 運動到起始點
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, -1, 0, offdese)
    robot.CloseRPC()
                  
UDP擴展軸與機器人直線運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveL(desc_pos, tool, user, exaxis_pos, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],config=-1)``"
    "描述", "UDP擴展軸與機器人直線運動同步運動"
    "必選參數", "
    - ``desc_pos``：目標笛卡爾位姿，單位 [mm][°]；
    - ``tool``：工具號，[0~14]；
    - ``user``：工件號，[0~14]；
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位；"
    "默認參數", "
    - ``joint_pos``:目標關節位置，單位 [°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel``： 速度百分比，[0~100] 默認20.0；
    - ``acc``：加速度百分比，[0~100] 暫不開放,默認0.0；
    - ``ovl``：速度縮放因子，[0~100] 默認100.0；
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0；
    - ``search``：[0]-不焊絲尋位，[1]-焊絲尋位；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0；
    - ``offset_pos``：位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0] ；
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1"
    "返回值", "錯誤碼 成功-0  失敗- errcode；"
                                            
UDP擴展軸與機器人直線運動同步運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 設置UDP通信參數並加載
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 設置擴展軸參數
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 擴展軸使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 擴展軸座標系標定
    pos = []  # 請填寫標定點座標
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 需調用4次用於標定
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步運動起點與終點
    startdescPose = []  # 填寫座標
    startjointPos = []  # 填寫座標
    startexaxisPos = []  # 填寫座標
    enddescPose = []  # 填寫座標
    endjointPos = []  # 填寫座標
    endexaxisPos = []  # 填寫座標
    # 運動到起始點
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos, tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0)
    # 執行同步直線運動
    robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, endexaxisPos, 100, 100, 100, 0, 0, offdese)
    robot.CloseRPC()
                      
UDP擴展軸與機器人圓弧運動同步運動
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveC(desc_pos_p, tool_p, user_p,exaxis_pos_p, desc_pos_t, tool_t, user_t,exaxis_pos_t,joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=100.0, offset_flag_p=0, offset_pos_p =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0, config=-1)``"
    "描述", " UDP擴展軸與機器人圓弧運動同步運動"
    "必選參數", "
    - ``desc_pos_p``：路徑點笛卡爾位姿，單位 [mm][°]；
    - ``tool_p``：路徑點工具號，[0~14]；
    - ``user_p``：路徑點工件號，[0~14]；
    - ``exaxis_pos_p``：路徑點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]；
    - ``desc_pos_t``：目標點笛卡爾位姿，單位 [mm][°]；
    - ``tool_t``：工具號，[0~14]；
    - ``user_t``：工件號，[0~14]；
    - ``exaxis_pos_t``：目標點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]；"
    "默認參數", "
    - ``joint_pos_p``:目標關節位置，單位 [°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``joint_pos_t``:目標關節位置，單位 [°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel_p``: 路徑點速度百分比，[0~100] 默認20.0；
    - ``acc_p``: 路徑點加速度百分比，[0~100] 暫不開放,默認0.0 ；   
    - ``offset_flag_p``: 路徑點是否偏移[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0；
    - ``offset_pos_p``: 路徑點位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``vel_t``: 目標點速度百分比，[0~100] 默認20.0；
    - ``acc_t``: 目標點加速度百分比，[0~100] 暫不開放 默認0.0；
    - ``offset_flag_t``: 目標點是否偏移[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0；
    - ``offset_pos_t``: 目標點位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``ovl``: 速度縮放因子，[0~100] 默認100.0；
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半徑 (非阻塞)，單位 [mm] 默認-1.0；
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1"
    "返回值", "錯誤碼 成功-0  失敗- errcode；"
                                                
UDP擴展軸與機器人圓弧運動同步運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 設置UDP通信參數並加載
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10)
    robot.ExtDevLoadUDPDriver()
    # 設置擴展軸參數
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)
    robot.SetRobotPosToAxis(1)
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)
    # 擴展軸使能、回零
    robot.ExtAxisServoOn(1, 0)
    robot.ExtAxisSetHoming(1, 0, 20, 3)
    # 擴展軸座標系標定
    pos = []  # 輸入標定點座標
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)  # 調用4次以完成標定
    coord = []
    error,coord = robot.PositionorComputeECoordSys()
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1)
    # 同步圓弧起始點、中間點、終點
    startdescPose = []# 輸入座標
    startjointPos = []# 輸入座標
    startexaxisPos =[]  # 輸入擴展軸座標
    middescPose = []# 輸入中間點
    midjointPos = []
    midexaxisPos =[]
    enddescPose = []
    endjointPos = []
    endexaxisPos =[]
    # 運動到起始點
    robot.ExtAxisMove(startexaxisPos, 20, -1)
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos,tool= 1,user= 1,vel= 100,acc= 100,ovl= 100,exaxis_pos= startexaxisPos,blendT= 0,offset_flag= 0,offset_pos= offdese)
    # 開始同步圓弧運動
    robot.ExtAxisSyncMoveC(midjointPos,middescPose,1,1,midexaxisPos,
                           endjointPos,enddescPose,1,1,endexaxisPos,
                           100,100,0,offdese,
                           100,100,0,offdese,
                           100,0)
    robot.CloseRPC()

設置擴展DO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDO(DONum,bOpen,smooth,block)``"
    "描述", "設置擴展DO"
    "必選參數", "
    - ``DONum``： DO編號；
    - ``bOpen``：開關 True-開,False-關；
    - ``smooth``：是否平滑 True -是, False -否；
    - ``block``：是否阻塞 True -是, False -否；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置擴展AO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAO(AONum,value,block)``"
    "描述", "設置擴展AO"
    "必選參數", "
    - ``AONum``： AO編號；
    - ``value``：模擬量值[0-4095]；
    - ``block``：是否阻塞 True -是, False -否；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
設置擴展DI輸入濾波時間
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDIFilterTime(filterTime)``"
    "描述", "設置擴展DI輸入濾波時間"
    "必選參數", "- ``filterTime``： 濾波時間(ms)；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
設置擴展AI輸入濾波時間
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAIFilterTime(AINum,filterTime)``"
    "描述", "設置擴展AI輸入濾波時間"
    "必選參數", "
    - ``AINum``： AI編號；
    - ``filterTime``： 濾波時間(ms)；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
等待擴展DI輸入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxDI(DINum,bOpen,time,errorAlarm)``"
    "描述", "等待擴展DI輸入"
    "必選參數", "
    - ``DINum``： DI編號；
    - ``bOpen``：開關 True-開,False-關；
    - ``time``：最大等待時間(ms)；
    - ``errorAlarm``：是否繼續運動 True-是,False-否"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
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
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
獲取擴展DI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxDI(DINum,isNoBlock)``"
    "描述", "獲取擴展DI值"
    "必選參數", "
    - ``DINum``： DI編號；
    - ``isNoBlock``：是否阻塞 True-阻塞 false-非阻塞；"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode；
    - ``isOpen``： 0-關；1-開；"
          
獲取擴展AI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxAI(AINum,isNoBlock)``"
    "描述", "獲取擴展AI值"
    "必選參數", "
    - ``AINum``： AI編號；
    - ``isNoBlock``：是否阻塞 True-阻塞 False-非阻塞"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode；
    - ``value``：輸入值；"

擴展IO代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    for i in range(128):
        robot.SetAuxDO(i, True, False, True)
        time.sleep(0.1)
    for i in range(128):
        robot.SetAuxDO(i, False, False, True)
        time.sleep(0.1)
    for i in range(409):
        value1 = i * 10
        value2 = 4095 - i * 10
        robot.SetAuxAO(0, value1, True)
        robot.SetAuxAO(1, value2, True)
        robot.SetAuxAO(2, value1, True)
        robot.SetAuxAO(3, value2, True)
        time.sleep(0.01)
    robot.SetAuxDIFilterTime(10)
    robot.SetAuxAIFilterTime(0, 10)
    for i in range(20):
        curValue = False
        error, curValue = robot.GetAuxDI(i, False)  # 注意：如庫內部需引用方式，這裏需修改
        print(f"DI{i}   {curValue}")
    curValue = -1
    for i in range(4):
        error, curValue = robot.GetAuxAI(i, True)  # 同樣注意引用傳參問題
        print(f"AI{i}   {curValue}")
    robot.WaitAuxDI(1, False, 1000, False)
    robot.WaitAuxAI(1, 1, 132, 1000, False)
    robot.CloseRPC()

可移動裝置使能
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorEnable(enable)``"
    "描述", "可移動裝置使能"
    "必選參數", "- ``enable``：使能狀態，0-去使能，1-使能"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

可移動裝置回零
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorHoming()``"
    "描述", "可移動裝置回零"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

可移動裝置直線運動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveL(distance, vel)``"
    "描述", "可移動裝置直線運動"
    "必選參數", "- ``distance``：直線運動距離（mm）
    - ``vel``：直線運動速度百分比（0-100）"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

可移動裝置圓弧運動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveC(radio, angle, vel)``"
    "描述", "可移動裝置圓弧運動"
    "必選參數", "- ``radio``：圓弧運動半徑（mm）
    - ``angle``：圓弧運動角度（°）
    - ``vel``：圓弧運動速度百分比（0-100）"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

可移動裝置停止運動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "可移動裝置停止運動"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

可移動裝置代碼示例
++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 1)
    robot.ExtDevLoadUDPDriver()
    rtn = robot.ExtAxisServoOn(1, 1)
    rtn = robot.ExtAxisServoOn(2, 1)
    time.sleep(2)
    robot.ExtAxisSetHoming(1, 0, 10, 2)
    time.sleep(2)
    rtn = robot.ExtAxisSetHoming(2, 0, 10, 2)
    time.sleep(4)
    robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0)
    robot.TractorEnable(False)
    time.sleep(2)
    robot.TractorEnable(True)
    time.sleep(2)
    robot.TractorHoming()
    time.sleep(2)
    robot.TractorMoveL(100, 2)
    time.sleep(5)
    robot.TractorStop()
    robot.TractorMoveL(-100, 20)
    time.sleep(5)
    robot.TractorMoveC(300, 90, 20)
    time.sleep(10)
    robot.TractorMoveC(300, -90, 20)
    time.sleep(1)
    robot.CloseRPC()

激光傳感器記錄點
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserRecordPoint(coordID)``"
    "描述", "激光傳感器記錄點"
    "必選參數", "- ``coordID``：激光傳感器座標系"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``joint``：激光傳感器識別點關節位置
    - ``desc``：激光傳感器識別點笛卡爾位置
    - ``exaxis``：激光傳感器識別點擴展軸位置"

激光傳感器記錄點代碼示例
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    direction_point = [0, 0, 0]
    rtn = robot.LaserTrackingSearchStart(2, direction_point, 10, 100, 10000, 2)
    print(f"LaserTrackingSearchStart rtn is {rtn}")
    robot.LaserTrackingSearchStop()
    coord_id = 2
    rtn, joint, desc, exaxis = robot.LaserRecordPoint(coord_id)
    print(f"rtn is {rtn}")
    print(f"desc_pos:{desc[0]},{desc[1]},{desc[2]},"
          f"{desc[3]},{desc[4]},{desc[5]}")
    print(f"joint_pos:{joint[0]},{joint[1]},{joint[2]},{joint[3]},{joint[4]},{joint[5]}")
    print(f"exaxis pos is {exaxis[0]} {exaxis[1]} {exaxis[2]} {exaxis[3]}")
    off = [0] * 6
    robot.MoveJ(joint,tool=1,user=0,vel=100,acc=100,ovl=50,exaxis_pos=exaxis,blendT=-1,offset_flag=0,offset_pos=off)
    robot.CloseRPC()

設置擴展軸與機器人同步運動策略
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExAxisRobotPlan(strategy)``"
    "描述", "設置擴展軸與機器人同步運動策略"
    "必選參數", "- ``strategy``：策略；0-以機器人爲主；1-擴展軸與機器人同步"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置擴展軸與機器人同步運動策略代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    joint_pos1 = [-22.016, -49.217, 124.714, -161.100, -85.108, -0.333]
    joint_pos2 = [-21.083, -46.613, 110.079, -147.796, -80.757, -0.330]
    joint_pos3 = [-25.572, -60.090, 135.397, -163.889, -82.489, -0.345]
    desc_pos1 = [2.637, -0.001, 30.673, 178.786, -4.134, 68.326]
    desc_pos2 = [213.812, -1.440, 47.311, 177.410, 0.166, 68.946]
    desc_pos3 = [444.342, -12.723, 82.470, -177.701, -1.325, 65.151]
    epos1 = [0.001, 0.000, 0.000, 0.000]
    epos2 = [299.977, 0.000, 0.000, 0.000]
    epos3 = [399.969, 0.000, 0.000, 0.000]
    offset_pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SetExAxisRobotPlan(0)
    print(f"SetExAxisRobotPlan rtn is {rtn}")
    time.sleep(1)
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos1,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos1,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 1 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos2,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos2,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 2 rtn is {rtn}")
    rtn = robot.ExtAxisSyncMoveL(desc_pos=desc_pos3,tool=1,user=0,vel=100,acc=100,ovl=100,blendR=-1,exaxis_pos=epos3,offset_flag=0,offset_pos=offset_pos)
    print(f"ExtAxisSyncMoveL 3 rtn is {rtn}")
    time.sleep(8)
    robot.CloseRPC()

控制陣列式吸盤
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSuckerCtrl(slaveID, len, ctrlValue)``"
    "描述", "控制陣列式吸盤"
    "必選參數", "- ``slaveID``：從站號
    - ``len``：長度
    - ``ctrlValue``：控制值 1-按最大真空度吸取 2-按設定真空度吸取 3-停止吸取"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取陣列式吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSuckerState(slaveID)``"
    "描述", "獲取陣列式吸盤狀態"
    "必選參數", "- ``slaveID``：從站號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``：吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    - ``pressValue``：當前真空度 單位kpa
    - ``error``：吸盤當前的錯誤碼"

等待吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitSuckerState(slaveID, state, ms)``"
    "描述", "等待吸盤狀態"
    "必選參數", "- ``slaveID``：從站號
    - ``state``：吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    - ``ms``：等待最大時間"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

陣列式吸盤控制指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("C://項目/外設SDK/CtrlDev_sucker.lua")
    time.sleep(2)
    robot.UnloadCtrlOpenLUA(1)
    robot.LoadCtrlOpenLUA(1)
    time.sleep(1)
    ctrl = bytearray(20)
    ctrl[0] = 1
    robot.SetSuckerCtrl(0, 1, ctrl)
    for i in range(100):
        rtn, state, press_value, error = robot.GetSuckerState(1)
        print(f"sucker1 state is {state}, pressValue is {press_value}, error num is {error}")
        rtn, state, press_value, error = robot.GetSuckerState(12)
        print(f"sucker12 state is {state}, pressValue is {press_value}, error num is {error}")
        time.sleep(0.1)
    ret = robot.WaitSuckerState(1, 1, 100)
    print(f"WaitSuckerState result is {ret}")
    ctrl[0] = 3
    robot.SetSuckerCtrl(1, 1, ctrl)
    robot.SetSuckerCtrl(12, 1, ctrl)
    robot.CloseRPC()

上傳開放協議的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaUpload(filePath)``"
    "描述", "上傳開放協議的Lua文件"
    "必選參數", "- ``filePath``：本地開放協議lua文件路徑名"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取從站板卡參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetFieldBusConfig()``"
    "描述", "獲取從站板卡參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``type``：0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    - ``version``：協議版本
    - ``connState``：0-未連接 1-已連接"

寫入從站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWriteDO(DOIndex, wirteNum, status)``"
    "描述", "寫入從站DO"
    "必選參數", "- ``DOIndex``：DO編號
    - ``wirteNum``：寫入的數量
    - ``status``：寫入的數值，最多寫8個"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

寫入從站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWriteAO(AOIndex, wirteNum, status)``"
    "描述", "寫入從站AO"
    "必選參數", "- ``AOIndex``：AO編號
    - ``wirteNum``：寫入的數量
    - ``status``：寫入的數值，最多寫8個"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

讀取從站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadDI(DOIndex, readeNum)``"
    "描述", "讀取從站DI"
    "必選參數", "- ``DOIndex``：DI編號
    - ``readeNum``：讀取的數量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``status[8]``：讀取到的數值，最多讀8個"

讀取從站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadAI(AOIndex, readeNum)``"
    "描述", "讀取從站AI"
    "必選參數", "- ``AOIndex``：AI編號
    - ``readeNum``：讀取的數量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``status[8]``：讀取到的數值，最多讀8個"

等待擴展DI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWaitDI(DIIndex, status, waitMs)``"
    "描述", "等待擴展DI輸入"
    "必選參數", "- ``DIIndex``：DI編號
    - ``status``：0-低電平；1-高電平
    - ``waitMs``：最大等待時間(ms)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWaitAI(AIIndex, waitType, value, waitMs)``"
    "描述", "等待擴展AI輸入"
    "必選參數", "- ``AIIndex``：AI編號
    - ``waitType``：0-大於；1-小於
    - ``value``：AI值
    - ``waitMs``：最大等待時間(ms)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

從站模式相關接口指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/外設/CtrlDev_field.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(3,"CtrlDev_field.lua")
    robot.UnloadCtrlOpenLUA(3)
    robot.LoadCtrlOpenLUA(3)
    time.sleep(8)
    rtn,type, version, conn_state = robot.GetFieldBusConfig()
    print(f"type is {type}, version is {version}, connState is {conn_state}")
    # Write digital outputs
    ctrl = [1, 0, 1]  # DO0=1, DO1=0, DO2=1
    robot.FieldBusSlaveWriteDO(0, 3, ctrl)
    # Write analog output
    ctrl_ao = [0x1000]  # AO2 = 0x1000
    robot.FieldBusSlaveWriteAO(2, 1, ctrl_ao)
    for i in range(100):
        rtn,di = robot.FieldBusSlaveReadDI(0, 4)
        print(f"DI0 is {di[0]}, DI1 is {di[1]}, DI2 is {di[2]}, DI3 is {di[3]}")
        rtn, ai = robot.FieldBusSlaveReadAI(0, 3)
        print(f"AI0 is {ai[0]}, AI1 is {ai[1]}, AI2 is {ai[2]}")
        time.sleep(0.01)
    ret = robot.FieldBusSlaveWaitDI(0, 1, 100)
    print(f"FieldBusSlaveWaitDI result is {ret}")
    ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00, 100)
    print(f"FieldBusSlaveWaitAI result is {ret}")
    robot.CloseRPC()