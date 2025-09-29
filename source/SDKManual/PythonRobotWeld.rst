焊接
======================

.. toctree:: 
    :maxdepth: 5
    
設置焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime)``"
    "描述", "設置焊接工藝曲線參數"
    "必選參數", "
    - ``id``： 焊接工藝編號(1-99)
    - ``startCurrent``： 起弧電流(A)
    - ``startVoltage``：startVoltage 起弧電壓(V)
    - ``startTime``：startTime 起弧時間(ms)
    - ``weldCurrent``：weldCurrent 焊接電流(A)
    - ``weldVoltage``：weldVoltage 焊接電壓(V)
    - ``endCurrent``：endCurrent 收弧電流(A)
    - ``endVoltage``：endVoltage 收弧電壓(V)
    - ``endTime``：endTime 收弧時間(ms)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

獲取焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetProcessParam(id)``"
    "描述", "獲取焊接工藝曲線參數"
    "必選參數", "
    - ``id``： 焊接工藝編號(1-99)
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``startCurrent``：起弧電流(A)
    - ``startVoltage``： 起弧電壓(V)
    - ``startTime``：起弧時間(ms)
    - ``weldCurrent``：焊接電流(A)
    - ``weldVoltage``：焊接電壓(V)
    - ``endCurrent``：收弧電流(A)
    - ``endVoltage``：收弧電壓(V)
    - ``endTime``：收弧時間(ms)
    " 

設置焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "設置焊接電流與輸出模擬量對應關係"
    "必選參數", "- ``currentMin``： 焊接電流-模擬量輸出線性關係左側點電流值(A)
    - ``currentMax``：  焊接電流-模擬量輸出線性關係右側點電流值(A)
    - ``outputVoltageMin``： 焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    - ``outputVoltageMax``：焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    - ``AOIndex``：焊接電流模擬量輸出端口"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "設置焊接電壓與輸出模擬量對應關係"
    "必選參數", "- ``weldVoltageMin``： 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(A)
    - ``weldVoltageMax``：  焊接電壓-模擬量輸出線性關係右側點焊接電壓值(A)
    - ``outputVoltageMin``： 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    - ``outputVoltageMax``：焊接電壓-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    - ``AOIndex``：焊接電壓模擬量輸出端口"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCurrentRelation()``"
    "描述", "獲取焊接電流與輸出模擬量對應關係"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``currentMin``：焊接電流-模擬量輸出線性關係左側點電流值(A)
    - ``currentMax``：焊接電流-模擬量輸出線性關係右側點電流值(A)
    - ``outputVoltageMin``：焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    - ``outputVoltageMax``：焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    - ``AOIndex``：焊接電壓模擬量輸出端口"

獲取焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetVoltageRelation()``"
    "描述", "獲取焊接電壓與輸出模擬量對應關係"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weldVoltageMin``: 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(V)
    - ``weldVoltageMax``: 焊接電壓-模擬量輸出線性關係右側點焊接電壓值(V)
    - ``outputVoltageMin``: 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    - ``outputVoltageMax``: 焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    - ``AOIndex``：焊接電壓模擬量輸出端口"

設置焊接電流
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrent(ioType, current, AOIndex, blend)``"
    "描述", "設置焊接電流"
    "必選參數", "- ``ioType``： 類型 0-控制器IO； 1-擴展IO
    - ``current``： 焊接電流值(A)
    - ``AOIndex``： 焊接電流控制箱模擬量輸出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接電壓
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltage(ioType, voltage, AOIndex, blend)``"
    "描述", "設置焊接電壓"
    "必選參數", "- ``ioType``： 類型 0-控制器IO； 1-擴展IO
    - ``voltage``： 焊接電壓值(V)
    - ``AOIndex``： 焊接電流控制箱模擬量輸出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置擺動參數
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.1.2
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftRange, weaveRightRange, additionalStayTime, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary, weaveYawAngle, weaveRotAngle)``"
    "描述", "設置擺動參數"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號
    - ``weaveType``： 擺動類型 0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    - ``weaveFrequency``： 擺動頻率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-週期不包含等待時間；1-週期包含等待時間必選參數
    - ``weaveRange``： 擺動幅度(mm)
    - ``weaveLeftRange``： 垂直三角擺動左弦長度(mm)
    - ``weaveRightRange``： 垂直三角擺動右弦長度(mm)
    - ``additionalStayTime``： 垂直三角擺動垂三角點停留時間(mm)
    - ``weaveLeftStayTime``： 擺動左停留時間(ms)
    - ``weaveRightStayTime``：  擺動右停留時間(ms)
    - ``weaveCircleRadio``： 圓形擺動-回調比率(0-100%)
    - ``weaveStationary``： 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止"
    "默認參數", "- ``weaveYawAngle``： 擺動方向方位角（繞擺動Z軸旋轉），單位°,默認0
    - ``weaveRotAngle``： 擺動方向方位角（繞擺動X軸旋轉），單位°,默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接參數代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000)
    robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333)
    start_current = 0
    start_voltage = 0
    start_time = 0
    weld_current = 0
    weld_voltage = 0
    end_current = 0
    end_voltage = 0
    end_time = 0
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(1)
    print(f"the Num 1 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    error, start_current, start_voltage, start_time, weld_current, weld_voltage, end_current,end_voltage, end_time = robot.WeldingGetProcessParam(2)
    print(f"the Num 2 process param is {start_current} {start_voltage} {start_time} {weld_current} {weld_voltage} {end_current} {end_voltage} {end_time}")
    rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0)
    print(f"WeldingSetCurrentRelation rtn is: {rtn}")
    rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1)
    print(f"WeldingSetVoltageRelation rtn is: {rtn}")
    current_min = 0
    current_max = 0
    vol_min = 0
    vol_max = 0
    output_vmin = 0
    output_vmax = 0
    cur_index = 0
    vol_index = 0
    rtn,current_min, current_max, output_vmin, output_vmax, cur_index = robot.WeldingGetCurrentRelation()
    print(f"WeldingGetCurrentRelation rtn is: {rtn}")
    print(f"current min {current_min} current max {current_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn,vol_min, vol_max, output_vmin, output_vmax, vol_index = robot.WeldingGetVoltageRelation()
    print(f"WeldingGetVoltageRelation rtn is: {rtn}")
    print(f"vol min {vol_min} vol max {vol_max} output vol min {output_vmin} output vol max {output_vmax}")
    rtn = robot.WeldingSetCurrent(1, 100, 0, 0)
    print(f"WeldingSetCurrent rtn is: {rtn}")
    time.sleep(3)
    rtn = robot.WeldingSetVoltage(1, 10, 0, 0)
    print(f"WeldingSetVoltage rtn is: {rtn}")
    rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0,0.0, 60.000000)
    print(f"rtn is: {rtn}")
    robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0)
    rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200)
    print(f"WeldingSetCheckArcInterruptionParam {rtn}")
    rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0)
    print(f"WeldingSetReWeldAfterBreakOffParam {rtn}")
    enable = 0
    length = 0
    velocity = 0
    move_type = 0
    check_enable = 0
    arc_interrupt_time_length = 0
    rtn,check_enable, arc_interrupt_time_length = robot.WeldingGetCheckArcInterruptionParam()
    print(f"WeldingGetCheckArcInterruptionParam checkEnable {check_enable} arcInterruptTimeLength {arc_interrupt_time_length}")
    rtn,enable, length, velocity, move_type = robot.WeldingGetReWeldAfterBreakOffParam()
    print(f"WeldingGetReWeldAfterBreakOffParam enable = {enable}, length = {length}, velocity = {velocity}, moveType = {move_type}")
    robot.SetWeldMachineCtrlModeExtDoNum(17)
    for i in range(5):
        robot.SetWeldMachineCtrlMode(0)
        time.sleep(1)
        robot.SetWeldMachineCtrlMode(1)
        time.sleep(1)
    robot.CloseRPC()

即時設置擺動參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveOnlineSetPara (weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)``"
    "描述", "即時設置擺動參數"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號
    - ``weaveType``： 擺動類型 0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    - ``weaveFrequency``： 擺動頻率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-週期不包含等待時間；1-週期包含等待時間必選參數
    - ``weaveRange``： 擺動幅度(mm)
    - ``weaveLeftStayTime``： 擺動左停留時間(ms)
    - ``weaveRightStayTime``：  擺動右停留時間(ms)
    - ``weaveCircleRadio``： 圓形擺動-回調比率(0-100%)
    - ``weaveStationary``： 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCheckArcInterruptionParam()``"
    "描述", "獲取機器人焊接電弧意外中斷檢測參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``checkEnable``：是否使能檢測；0-不使能；1-使能
    - ``arcInterruptTimeLength``：電弧中斷確認時長(ms)"

設置機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCheckArcInterruptionParam(checkEnable, arcInterruptTimeLength)``"
    "描述", "設置機器人焊接電弧意外中斷檢測參數"
    "必選參數", "- ``checkEnable``：是否使能檢測；0-不使能；1-使能
    - ``arcInterruptTimeLength``：電弧中斷確認時長(ms)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetReWeldAfterBreakOffParam()``"
    "描述", "獲取機器人焊接中斷恢復參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``enable``：是否使能焊接中斷恢復
    - ``length``：焊縫重疊距離(mm)
    - ``velocity``：機器人回到再起弧點速度百分比(0-100)
    - ``moveType``：機器人運動到再起弧點方式；0-LIN；1-PTP"

設置機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetReWeldAfterBreakOffParam(enable, length, velocity, moveType)``"
    "描述", "設置機器人焊接中斷恢復參數"
    "必選參數", "- ``enable``：是否使能焊接中斷恢復
    - ``length``：焊縫重疊距離(mm)
    - ``velocity``：機器人回到再起弧點速度百分比(0-100)
    - ``moveType``：機器人運動到再起弧點方式；0-LIN；1-PTP"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlModeExtDoNum(DONum)``"
    "描述", "設置焊機控制模式擴展DO端口"
    "必選參數", "- ``DONum``：焊機控制模式DO端口(0-127)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

設置焊機控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlMode(mode)``"
    "描述", "設置焊機控制模式"
    "必選參數", "- ``mode``：焊機控制模式;0-一元化"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

焊接開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCStart(ioType, arcNum, timeout)``"
    "描述", "焊接開始"
    "必選參數", "- ``ioType``：io類型 0-控制器IO； 1-擴展IO
    - ``arcNum``： 焊機配置文件編號
    - ``timeout``： 起弧超時時間"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

焊接結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCEnd(ioType, arcNum, timeout)``"
    "描述", "焊接結束"
    "必選參數", "- ``ioType``： 類型 0-控制器IO； 1-擴展IO
    - ``arcNum``： 焊機配置文件編號
    - ``timeout``： 起弧超時時間"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

擺動開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStart(weaveNum)``"
    "描述", "擺動開始"
    "必選參數", "- ``weaveNum``： 類型 0-控制器IO； 1-擴展IO"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

擺動結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEnd(weaveNum)``"
    "描述", "擺動結束"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

正向送絲
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForwardWireFeed(ioType, wireFeed)``"
    "描述", "正向送絲"
    "必選參數", "- ``ioType``： 0-控制器IO；1-擴展IO
    - ``wireFeed``： 送絲控制  0-停止送絲；1-送絲"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

反向送絲
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetReverseWireFeed(ioType, wireFeed)``"
    "描述", "反向送絲"
    "必選參數", "- ``ioType``： 0-控制器IO；1-擴展IO
    - ``wireFeed``： 送絲控制  0-停止送絲；1-送絲"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

送氣
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAspirated(ioType, airControl)``"
    "描述", "送氣"
    "必選參數", "- ``ioType``： 0-控制器IO；1-擴展IO
    - ``airControl``： 送氣控制  0-停止送氣；1-送氣"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingStartReWeldAfterBreakOff()``"
    "描述", "設置機器人焊接中斷後恢復焊接"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingAbortWeldAfterBreakOff()``"
    "描述", "設置機器人焊接中斷後退出焊接"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

機器人焊接控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.SetForwardWireFeed(0, 1)
    time.sleep(1)
    robot.SetForwardWireFeed(0, 0)
    robot.SetReverseWireFeed(0, 1)
    time.sleep(1)
    robot.SetReverseWireFeed(0, 0)
    robot.SetAspirated(0, 1)
    time.sleep(1)
    robot.SetAspirated(0, 0)
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint, tool=13, user=0)
    robot.ARCStart(1, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=p2Desc, tool=13, user=0)
    robot.ARCEnd(1, 0, 10000)
    robot.WeaveEnd(0)
    robot.WeldingStartReWeldAfterBreakOff()
    robot.WeldingAbortWeldAfterBreakOff()
    robot.CloseRPC()

分段焊接啓動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldStart(startDesePos,  endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave,weaveNum,tool,user,vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0,exaxis_pos=[0.0, 0.0, 0.0, 0.0],  search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "分段焊接啓動"
    "必選參數", "- ``startDesePos``： 初始笛卡爾位姿，單位 [mm][°]
    - ``endDesePos``： 目標笛卡爾位姿，單位 [mm][°]
    - ``startJPos``：初始關節位置，單位 [°] 
    - ``endJPos``：目標關節位置，單位 [°]  
    - ``weldLength``：焊接長度，單位 [mm] 
    - ``noWeldLength``：非焊接長度，單位 [mm] 
    - ``weldIOType``：焊接IO類型(0-控制箱IO；1-擴展IO) arcNum 焊機配置文件編號 
    - ``timeout``：熄弧超時時間 
    - ``isWeave``：焊接 False-不焊接 
    - ``weaveNum``：擺焊參數配置編號 
    - ``tool``：工具號，[0~14]
    - ``user``：工件號，[0~14]"
    "默認參數", "- ``vel``：速度百分比，[0~100] 默認20.0
    - ``acc``：加速度[0~100] 暫不開放 默認0.0
    - ``ovl``：速度縮放因子，[0~100] 默認100.0
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半徑 (非阻塞)，單位 [mm] 默認-1.0
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]
    - ``search``：[0]-不焊絲尋位，[1]-焊絲尋位
    - ``offset_flag``：[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0
    - ``offset_pos``：位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

機器人段焊代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.WeldingSetCurrent(1, 230, 0, 0)
    robot.WeldingSetVoltage(1, 24, 0, 1)
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    rtn = robot.SegmentWeldStart(p1Desc, p2Desc, p1Joint, p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0)
    print(f"SegmentWeldStart rtn is {rtn}")
    robot.CloseRPC()

仿真擺動開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStartSim(weaveNum)``"
    "描述", "仿真擺動開始"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

仿真擺動結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEndSim(weaveNum)``"
    "描述", "仿真擺動結束"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

開始軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectStart(weaveNum)``"
    "描述", "開始軌跡檢測預警(不運動)"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

結束軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectEnd(weaveNum)``"
    "描述", "結束軌跡檢測預警(不運動)"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

擺動漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveChangeStart(weaveChangeFlag, weaveNum, velStart, velEnd)``"
    "描述", "擺動漸變開始"
    "必選參數", "- ``weaveChangeFlag``：擺動編號 1-變擺動參數；2-變擺動參數+焊接速度
    - ``weaveNum``：擺動編號
    - ``velStart``：焊接開始速度，(cm/min)
    - ``velEnd``：焊接結束速度，(cm/min)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

機器人擺動漸變焊接代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [228.879, -503.594, 453.984, -175.580, 8.293, 171.267]
    p1Joint = [102.700, -85.333, 90.518, -102.365, -83.932, 22.134]
    p2Desc = [-333.302, -435.580, 449.866, -174.997, 2.017, 109.815]
    p2Joint = [41.862, -85.333, 90.526, -100.587, -90.014, 22.135]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos= p1Joint,tool= 13,user= 0)
    robot.WeaveStartSim(0)
    robot.MoveL(desc_pos= p2Desc,tool= 13,user= 0)
    robot.WeaveEndSim(0)
    robot.MoveJ(joint_pos= p1Joint,tool= 13,user= 0)
    robot.WeaveInspectStart(0)
    robot.MoveL(desc_pos= p2Desc,tool= 13,user= 0,)
    robot.WeaveInspectEnd(0)
    robot.WeldingSetVoltage(1, 19, 0, 0)
    robot.WeldingSetCurrent(1, 190, 0, 0)
    robot.MoveL(desc_pos= p1Desc,tool= 1,user= 1,vel= 100,acc= 100,ovl= 50)
    robot.ARCStart(1, 0, 10000)
    robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(1, 0, 50, 30)
    robot.MoveL(desc_pos= p2Desc,tool= 1,user= 1,vel= 100)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0)
    robot.ARCEnd(1, 0, 10000)
    robot.CloseRPC()

擺動漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveChangeEnd()``"
    "描述", "擺動漸變結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

擴展IO-配置焊機氣體檢測信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAirControlExtDoNum(DONum)``"
    "描述", "擴展IO-配置焊機氣體檢測信號"
    "必選參數", "
    - ``DONum``：氣體檢測信號擴展DO編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

擴展IO-配置焊機起弧信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcStartExtDoNum(DONum)``"
    "描述", "擴展IO-配置焊機起弧信號"
    "必選參數", "
    - ``DONum``：氣體檢測信號擴展DO編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 
        
擴展IO-配置焊機反向送絲信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireReverseFeedExtDoNum(DONum)``"
    "描述", "擴展IO-配置焊機反向送絲信號"
    "必選參數", "
    - ``DONum``：氣體檢測信號擴展DO編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 
        
擴展IO-配置焊機正向送絲信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireForwardFeedExtDoNum(DONum)``"
    "描述", "擴展IO-配置焊機正向送絲信號"
    "必選參數", "
    - ``DONum``：氣體檢測信號擴展DO編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 
        
擴展IO-配置焊機起弧成功信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "擴展IO-配置焊機起弧成功信號"
    "必選參數", "
    - ``DINum``：焊機準備信號擴展DI編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 
        
擴展IO-配置焊機準備信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "擴展IO-配置焊機準備信號"
    "必選參數", "
    - ``DINum``：焊機準備信號擴展DI編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 
        
擴展IO-配置焊接中斷恢復信號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExtDIWeldBreakOffRecover(reWeldDINum, abortWeldDINum)``"
    "描述", "擴展IO-配置焊接中斷恢復信號"
    "必選參數", "
    - ``reWeldDINum``：焊接中斷後恢復焊接信號擴展DI編號
    - ``abortWeldDINum``：焊接中斷後退出焊接信號擴展DI編號
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

設置擴展IO焊接信號代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetArcStartExtDoNum(10)
    print(f"SetArcStartExtDoNum rtn is {rtn}")
    rtn = robot.SetAirControlExtDoNum(20)
    print(f"SetAirControlExtDoNum rtn is {rtn}")
    rtn = robot.SetWireForwardFeedExtDoNum(30)
    print(f"SetWireForwardFeedExtDoNum rtn is {rtn}")
    rtn = robot.SetWireReverseFeedExtDoNum(40)
    rtn = robot.SetWeldReadyExtDiNum(50)
    print(f"SetWeldReadyExtDiNum rtn is {rtn}")
    rtn = robot.SetArcDoneExtDiNum(60)
    print(f"SetArcDoneExtDiNum rtn is {rtn}")
    rtn = robot.SetExtDIWeldBreakOffRecover(70, 80)
    print(f"SetExtDIWeldBreakOffRecover rtn is {rtn}")
    rtn = robot.SetWireSearchExtDIONum(0, 1)
    print(f"SetWireSearchExtDIONum rtn is {rtn}")
    robot.CloseRPC()

電弧跟蹤控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.9-3.7.9

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd, sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent, offsetType, offsetParameter)``"
    "描述", "電弧跟蹤控制"
    "必選參數", "- ``flag``： 開關，0-關；1-開
    - ``delayTime``：滯後時間，單位ms
    - ``isLeftRight``：左右偏差補償 0-關閉，1-開啓
    - ``klr``：左右調節係數(靈敏度)
    - ``tStartLr``：左右開始補償時間cyc
    - ``stepMaxLr``：左右每次最大補償量 mm
    - ``sumMaxLr``：左右總計最大補償量 mm
    - ``isUpLow``：上下偏差補償 0-關閉，1-開啓
    - ``kud``：上下調節係數(靈敏度)
    - ``tStartUd``：上下開始補償時間cyc
    - ``stepMaxUd``：上下每次最大補償量 mm
    - ``sumMaxUd``：上下總計最大補償量
    - ``axisSelect``：上下座標系選擇，0-擺動；1-工具；2-基座
    - ``referenceType``：上下基準電流設定方式，0-反饋；1-常數
    - ``referSampleStartUd``：上下基準電流採樣開始計數(反饋)，cyc
    - ``referSampleCountUd``：上下基準電流採樣循環計數(反饋)，cyc
    - ``referenceCurrent``：上下基準電流mA
    - ``offsetType``：偏置跟蹤類型，0-不偏置；1-採樣；2-百分比
    - ``offsetParameter``：偏置參數；採樣(偏置採樣開始時間，默認採一週期)；百分比(偏置百分比(-100 ~ 100))"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

電弧跟蹤AI通帶選擇
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceExtAIChannelConfig(channel)``"
    "描述", "電弧跟蹤AI通帶選擇"
    "必選參數", "- ``channel``：電弧跟蹤AI通帶選擇,[0-3]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

電弧追蹤 + 多層多道補償開啓
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayStart()``"
    "描述", "電弧追蹤 + 多層多道補償開啓"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

電弧追蹤 + 多層多道補償關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayEnd()``"
    "描述", "電弧追蹤 + 多層多道補償關閉"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MultilayerOffsetTrsfToBase(pointo, pointX, pointZ, dx, dy, db)``"
    "描述", "偏移量座標變化-多層多道焊"
    "必選參數", "- ``pointo``：基準點笛卡爾位姿
    - ``pointX``：基準點X向偏移方向點笛卡爾位姿
    - ``pointZ``：基準點Z向偏移方向點笛卡爾位姿
    - ``dx``：x方向偏移量(mm)
    - ``dz``：z方向偏移量(mm)
    - ``dry``：繞y軸偏移量(°)"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``offset``：計算結果偏移量"

多層多道焊電弧跟蹤代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    mulitilineorigin1_joint = [-24.090, -63.501, 84.288, -111.940, -93.426, 57.669]
    mulitilineorigin1_desc = [-677.559, 190.951, -1.205, 1.144, -41.482, -82.577]
    mulitilineX1_desc = [-677.556, 211.949, -1.206]
    mulitilineZ1_desc = [-677.564, 190.956, 19.817]
    mulitilinesafe_joint = [-25.734, -63.778, 81.502, -108.975, -93.392, 56.021]
    mulitilinesafe_desc = [-677.561, 211.950, 19.812, 1.144, -41.482, -82.577]
    mulitilineorigin2_joint = [-29.743, -75.623, 101.241, -116.354, -94.928, 55.735]
    mulitilineorigin2_desc = [-563.961, 215.359, -0.681, 2.845, -40.476, -87.443]
    mulitilineX2_desc = [-563.965, 220.355, -0.680]
    mulitilineZ2_desc = [-563.968, 215.362, 4.331]
    epos = [0, 0, 0, 0]
    offset = [0, 0, 0, 0, 0, 0]
    time.sleep(0.01)
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error = robot.WeaveStart(0)
    print(f"WeaveStart return: {error}")
    error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 1,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0)
    print(f"ArcWeldTraceControl return: {error}")
    error = robot.WeaveEnd(0)
    print(f"WeaveEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error,offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 2,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 10000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc[:3], mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0)
    print(f"MultilayerOffsetTrsfToBase return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin1_desc,tool= 13,user= 0,vel= 10,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ARCStart(1, 0, 3000)
    print(f"ARCStart return: {error}")
    error, offset = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc[:3], mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0)
    error = robot.ArcWeldTraceReplayStart()
    print(f"ArcWeldTraceReplayStart return: {error}")
    error = robot.MoveL(desc_pos= mulitilineorigin2_desc,tool= 13,user= 0,vel= 2,speedPercent=100)
    print(f"MoveL return: {error}")
    error = robot.ArcWeldTraceReplayEnd()
    print(f"ArcWeldTraceReplayEnd return: {error}")
    error = robot.ARCEnd(1, 0, 3000)
    print(f"ARCEnd return: {error}")
    error = robot.MoveJ(joint_pos= mulitilinesafe_joint,tool= 13,user= 0,vel= 10)
    print(f"MoveJ return: {error}")
    robot.CloseRPC()

電弧跟蹤焊機電流反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceAIChannelCurrent(channel)``"
    "描述", "電弧跟蹤焊機電流反饋AI通道選擇"
    "必選參數", "- ``channel``：通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

電弧跟蹤焊機電壓反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceAIChannelVoltage(channel)``"
    "描述", "電弧跟蹤焊機電壓反饋AI通道選擇"
    "必選參數", "- ``channel``：通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

電弧跟蹤焊機電流反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceCurrentPara(AILow, AIHigh, currentLow, currentHigh)``"
    "描述", "電弧跟蹤焊機電流反饋轉換參數"
    "必選參數", "無"
    "默認參數", "- ``AILow``：AI通道下限，默認值0V，範圍[0-10V]
    - ``AIHigh``：AI通道上限，默認值10V，範圍[0-10V]
    - ``currentLow``：AI通道下限對應焊機電流值，默認值0V，範圍[0-200V]
    - ``currentHigh``：AI通道上限對應焊機電流值，默認值100V，範圍[0-200V]"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

電弧跟蹤焊機電壓反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceVoltagePara(AILow, AIHigh, voltageLow, voltageHigh)``"
    "描述", "電弧跟蹤焊機電壓反饋轉換參數"
    "必選參數", "無"
    "默認參數", "- ``AILow``：AI通道下限，默認值0V，範圍[0-10V]
    - ``AIHigh``：AI通道上限，默認值10V，範圍[0-10V]
    - ``voltageLow``：AI通道下限對應焊機電壓值，默認值0V，範圍[0-200V]
    - ``voltageHigh``：AI通道上限對應焊機電壓值，默認值100V，範圍[0-200V]"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

電弧跟蹤代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    safetydescPose = [-504.043,275.181,40.908,-28.002,-42.025,-14.044]
    safetyjointPos = [-39.078,-76.732,87.227,-99.47,-94.301,18.714]
    startdescPose = [-473.86,257.879,-20.849,-37.317,-42.021,2.543]
    startjointPos = [-43.487,-76.526,95.568,-104.445,-89.356,3.72]
    enddescPose = [-499.844,141.225,7.72,-34.856,-40.17,13.13]
    endjointPos = [-31.305,-82.998,99.401,-104.426,-89.35,3.696]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ----設置電壓
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ----設置電流
    rtn = robot.ArcWeldTraceAIChannelCurrent(4)
    print("ArcWeldTraceAIChannelCurrent rtn is", rtn)
    rtn = robot.ArcWeldTraceAIChannelVoltage(5)
    print("ArcWeldTraceAIChannelVoltage rtn is", rtn)
    rtn = robot.ArcWeldTraceCurrentPara(0, 5, 0, 500)
    print("ArcWeldTraceCurrentPara rtn is", rtn)
    rtn = robot.ArcWeldTraceVoltagePara(1.018, 10, 0, 50)
    print("ArcWeldTraceVoltagePara rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=20, acc=100)
    robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl= 2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.MoveJ(joint_pos=safetyjointPos, tool=1, user=0, vel=20, acc=100)

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchStart(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊絲尋位開始"
    "必選參數", "- ``refPos``： 1-基準點 0-接觸點
    - ``searchVel``： 尋位速度 %
    - ``searchDis``： 尋位距離 mm
    - ``autoBackFlag``： 自動返回標誌，0-不自動；-自動
    - ``autoBackVel``： 自動返回速度 %
    - ``autoBackDis``： 自動返回距離 mm
    - ``offectFlag``： 1-帶偏移量尋位；0-示教點尋位"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

焊絲尋位結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchEnd(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊絲尋位結束"
    "必選參數", "- ``refPos``： 1-基準點 2-接觸點
    - ``searchVel``： 尋位速度 %
    - ``searchDis``： 尋位距離 mm
    - ``autoBackFlag``： 自動返回標誌，0-不自動；-自動
    - ``autoBackVel``： 自動返回速度 %
    - ``autoBackDis``： 自動返回距離 mm
    - ``offectFlag``： 1-帶偏移量尋位；2-示教點尋位"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算焊絲尋位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWireSearchOffset(seamType, method,varNameRef,varNameRes)``"
    "描述", "計算焊絲尋位偏移量"
    "必選參數", "- ``seamType``： 焊縫類型
    - ``method``： 計算方法
    - ``varNameRef``： 基準點1-6，“#”表示無點變量
    - ``varNameRes``： 接觸點1-6，“#”表示無點變量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``offsetFlag``： 0-偏移量直接疊加到指令點；1-偏移量需要對指令點進行座標變換
    - ``offset``： 偏移位姿[x, y, z, a, b, c]"

等待焊絲尋位完成
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchWait(varname)``"
    "描述", "等待焊絲尋位完成"
    "必選參數", "- ``varName``： 接觸點名稱 “RES0” ~ “RES99”"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

焊絲尋位接觸點寫入數據庫
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPointToDatabase(varName,pos)``"
    "描述", "焊絲尋位接觸點寫入數據庫"
    "必選參數", "- ``varName``： 接觸點名稱 “RES0” ~ “RES99”
    - ``pos``：接觸點數據[x, y, x, a, b, c]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode" 

機器人焊絲尋位代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    toolCoord = [0, 0, 200, 0, 0, 0]
    robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0)
    wobjCoord = [0, 0, 0, 0, 0, 0]
    robot.SetWObjCoord(1, wobjCoord, 0)
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    descStart = [216.543, 445.175, 93.465, 179.683, 1.757, -112.641]
    jointStart = [-128.345, -86.660, 114.679, -119.625, -89.219, 74.303]
    descEnd = [111.143, 523.384, 87.659, 179.703, 1.835, -97.750]
    jointEnd = [-113.454, -81.060, 109.328, -119.954, -89.218, 74.302]
    error = robot.MoveL(desc_pos=descStart,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descEnd,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    descREF0A = [142.135, 367.604, 86.523, 179.728, 1.922, -111.089]
    jointREF0A = [-126.794, -100.834, 128.922, -119.864, -89.218, 74.302]
    descREF0B = [254.633, 463.125, 72.604, 179.845, 2.341, -114.704]
    jointREF0B = [-130.413, -81.093, 112.044, -123.163, -89.217, 74.303]
    descREF1A = [92.556, 485.259, 47.476, -179.932, 3.130, -97.512]
    jointREF1A = [-113.231, -83.815, 119.877, -129.092, -89.217, 74.303]
    descREF1B = [203.103, 583.836, 63.909, 179.991, 2.854, -103.372]
    jointREF1B = [-119.088, -69.676, 98.692, -121.761, -89.219, 74.303]
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos=descREF0A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos=descREF0B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF1A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF1B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("REF1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF0A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF0B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES0")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchStart return: {error}")
    error = robot.MoveL(desc_pos= descREF1A,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descREF1B,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.WireSearchWait("RES1")
    print(f"WireSearchWait return: {error}")
    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print(f"WireSearchEnd return: {error}")
    varNameRef = ["REF0", "REF1", "#", "#", "#", "#"]
    varNameRes = ["RES0", "RES1", "#", "#", "#", "#"]
    offectFlag = 0
    offectPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error, offectFlag, offectPos = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes)
    print(f"GetWireSearchOffset return: {error}")
    error = robot.PointsOffsetEnable(0, offectPos)
    print(f"PointsOffsetEnable return: {error}")
    error = robot.MoveL(desc_pos= descStart,tool= 1,user= 1,vel= 100)
    print(f"MoveL return: {error}")
    error = robot.MoveL(desc_pos= descEnd,tool= 1,user= 1,vel= 100,search=1)
    print(f"MoveL return: {error}")
    error = robot.PointsOffsetDisable()
    robot.CloseRPC()

設置焊接電壓漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageGradualChangeStart(IOType, voltageStart, voltageEnd, AOIndex, blend)``"
    "描述", "設置焊接電壓漸變開始"
    "必選參數", "- ``IOType``：控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    - ``voltageStart``：起始焊接電壓(V)
    - ``voltageEnd``：終止焊接電壓(V)
    - ``AOIndex``：控制箱AO端口號(0-1)
    - ``blend``：是否平滑 0-不平滑；1-平滑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接電壓漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageGradualChangeEnd()``"
    "描述", "設置焊接電壓漸變結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接電流漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentGradualChangeStart(IOType, currentStart, currentEnd, AOIndex, blend)``"
    "描述", "設置焊接電流漸變開始"
    "必選參數", "- ``IOType``：控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    - ``currentStart``：起始焊接電流(A)
    - ``currentEnd``：終止焊接電流(A)
    - ``AOIndex``：控制箱AO端口號(0-1)
    - ``blend``：是否平滑 0-不平滑；1-平滑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焊接電流漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentGradualChangeEnd()``"
    "描述", "設置焊接電流漸變結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人焊接電流電壓漸變代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startdescPose = [-484.707, 276.996, -14.013, -37.657, -40.508, -1.548]
    startjointPos = [-45.421, -75.673, 93.627, -104.302, -87.938, 6.005]
    enddescPose = [-508.767, 137.109, -13.966, -37.639, -40.508, -1.559]
    endjointPos = [-32.768, -80.947, 100.254, -106.201, -87.201, 18.648]
    safedescPose = [-484.709, 294.436, 13.621, -37.660, -40.508, -1.545]
    safejointPos = [-46.604, -75.410, 89.109, -100.003, -88.012, 4.823]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0)
    robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1)
    robot.WeldingSetVoltage(0, 25, 1, 0)  # ----設置電壓
    robot.WeldingSetCurrent(0, 260, 0, 0)  # ----設置電流
    robot.MoveJ(joint_pos=safejointPos, tool=1, user=0, vel=5, acc=100)
    rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0)
    print("WeldingSetCurrentGradualChangeStart rtn is", rtn)
    rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0)
    print("WeldingSetVoltageGradualChangeStart rtn is", rtn)
    rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    print("ArcWeldTraceControl rtn is", rtn)
    robot.MoveJ(joint_pos=startjointPos, tool=1, user=0, vel=5, acc=100)
    robot.ARCStart(0, 0, 10000)
    robot.WeaveStart(0)
    robot.WeaveChangeStart(2, 1, 24, 36)
    robot.MoveL(desc_pos=enddescPose, tool=1, user=0, vel=100, ovl=2, acc=100)
    robot.ARCEnd(0, 0, 10000)
    robot.WeaveChangeEnd()
    robot.WeaveEnd(0)
    robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0)
    robot.WeldingSetCurrentGradualChangeEnd()
    robot.WeldingSetVoltageGradualChangeEnd()

設置自定義擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomWeaveSetPara(id, pointNum, point, stayTime, frequency, incStayType, stationary)``"
    "描述", "設置自定義擺動參數"
    "必選參數", "- ``id``：自定義擺動編號：0-2
    - ``pointNum``：擺動點位個數 0-10
    - ``point``：移動端點數據x,y,z
    - ``stayTime``：擺動停留時間ms
    - ``frequency``：擺動頻率 Hz
    - ``incStayType``：等待模式：0-週期不包含等待時間；1-週期包含等待時間
    - ``stationary``：擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取自定義擺動參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomWeaveGetPara(id)``"
    "描述", "獲取自定義擺動參數"
    "必選參數", "- ``id``：自定義擺動編號：0-2"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``pointNum``：擺動點位個數 0-10
    - ``point``：移動端點數據x,y,z
    - ``stayTime``：擺動停留時間ms
    - ``frequency``：擺動頻率 Hz
    - ``incStayType``：等待模式：0-週期不包含等待時間；1-週期包含等待時間
    - ``stationary``：擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止"

自定義擺動參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    point = [0.0] * 30
    point[0] = -3.0
    point[1] = -3.0
    point[2] = 0.0
    point[3] = -6.0
    point[4] = 0.0
    point[5] = 0.0
    point[6] = -3.0
    point[7] = 3.0
    point[8] = 0.0
    point[9] = 0.0
    point[10] = 0.0
    point[11] = 0.0
    stayTime = [0.0] * 10
    rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0)
    print(f"CustomWeaveSetPara rtn is {rtn}")
    time.sleep(1)
    pointNum = 0
    frequency = 0.0
    incStayType = 0
    stationary = 0
    rtn, pointNum, point, stayTime, frequency, incStayType, stationary = robot.CustomWeaveGetPara(2)
    print(f"pointNum is {pointNum}")
    for i in range(pointNum):
        print(f"point {i}, point x y z {point[i * 3 + 0]},{point[i * 3 + 1]},{point[i * 3 + 2]}")
    print(f"fre is {frequency}, stay is {incStayType},{stationary}")
    robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000)
    desc_p1 = [-288.650, 367.807, 288.404, 0.000, -0.001, 0.001]
    desc_p2 = [-431.714, 367.815, 288.415, 0.001, 0.001, 0.000]
    desc_p3 = [-348.666, 427.798, 288.404, -0.000, -0.000, 0.001]
    j1 = [140.656, -84.560, -91.707, -93.734, 90.000, 50.655]
    j2 = [149.873, -98.298, -77.599, -94.103, 90.000, 59.873]
    j3 = [139.773, -96.173, -80.014, -93.814, 90.000, 49.772]
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.Circle(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50, oacc=10)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveC(desc_pos_p=desc_p3, tool_p=3, user_p=0, vel_p=50, desc_pos_t=desc_p2, tool_t=3, user_t=0, vel_t=50)
    robot.WeaveEnd(0)
    robot.MoveJ(joint_pos=j1, tool=3, user=0, vel=100)
    robot.WeaveStart(0)
    robot.MoveL(desc_pos=desc_p2, tool=3, user=0, vel=100, ovl=10, speedPercent=100)
    robot.WeaveEnd(0)
    robot.CloseRPC()