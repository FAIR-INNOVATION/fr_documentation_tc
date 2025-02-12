焊接
======================

.. toctree:: 
    :maxdepth: 5

焊接開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCStart(ioType, arcNum, timeout)``"
    "描述", "焊接開始"
    "必選參數", "- ``ioType``：io 類型 0-控制器IO；1-擴展IO
    - ``arcNum``： 焊機設定檔編號
    - ``timeout``： 起弧超時時間"
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

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #起弧
    ret = robot.ARCStart(weldIOType,arcNum,weldTimeout)
    print("ARCStart錯誤碼", ret)
    time.sleep(3)

焊接結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCEnd(ioType, arcNum, timeout)``"
    "描述", "焊接結束"
    "必選參數", "- ``ioType``： 類型 0-控制器IO；1-擴充IO
    - ``arcNum``： 焊機設定檔編號
    - ``timeout``： 起弧超時時間"
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

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #收弧
    ret = robot.ARCEnd(weldIOType,arcNum,weldTimeout)
    print("ARCEnd錯誤碼", ret)
    time.sleep(3)

設定焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "設定焊接電流與輸出模擬量對應關係"
    "必選參數", "- ``currentMin``： 焊接電流-類比量輸出線性關係左點電流值(A)
    - ``currentMax``：  焊接電流-類比量輸出線性關係右側點電流值(A)
    - ``outputVoltageMin``： 焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    - ``outputVoltageMax``：焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    - ``AOIndex``：焊接電流類比量輸出端口"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    weldIOType =0

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000

    #設定焊接電流与類比線性關係
    ret = robot.WeldingSetCurrentRelation(0,400,0,10,0)
    print("WeldingSetCurrentRelation", ret)
    time.sleep(1)
    #取得焊接電流與類比量線性關係
    ret = robot.WeldingGetCurrentRelation()
    print("WeldingGetCurrentRelation", ret)
    time.sleep(1)

    #設定焊接電壓与類比線性關係
    ret = robot.WeldingSetVoltageRelation(0,400,0,10,0)
    print("WeldingSetVoltageRelation", ret)
    time.sleep(1)
    #取得焊接電壓與類比線性關係
    ret = robot.WeldingGetVoltageRelation()
    print("WeldingGetVoltageRelation", ret)
    time.sleep(1)

設定焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "設定焊接電壓與輸出模擬量對應關係"
    "必選參數", "- ``weldVoltageMin``： 焊接電壓-類比輸出線性關係左點焊接電壓值(A)
    - ``weldVoltageMax``：  焊接電壓-類比輸出線性關係右側點焊接電壓值(A)
    - ``outputVoltageMin``： 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    - ``outputVoltageMax``：焊接電壓-類比輸出線性關係右側點類比輸出電壓值(V)
    - ``AOIndex``：焊接電壓類比量輸出端口"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCurrentRelation()``"
    "描述", "取得焊接電流與輸出模擬量對應關係"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``currentMin``：焊接電流-類比量輸出線性關係左點電流值(A)
    - ``currentMax``：焊接電流-類比量輸出線性關係右側點電流值(A)
    - ``outputVoltageMin``：焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    - ``outputVoltageMax``：焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    - ``AOIndex``：焊接電壓類比量輸出端口"

取得焊接電壓與輸出類比對應關係
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetVoltageRelation()``"
    "描述", "取得焊接電壓與輸出類比對應關係"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weldVoltageMin``: 焊接電壓-類比輸出線性關係左點焊接電壓值(V)
    - ``weldVoltageMax``: 焊接電壓-類比輸出線性關係右側點焊接電壓值(V)
    - ``outputVoltageMin``: 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    - ``outputVoltageMax``: 焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    - ``AOIndex``：焊接電壓類比量輸出端口"

設定焊接電流
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrent(ioType, current, AOIndex, blend)``"
    "描述", "設定焊接電流"
    "必選參數", "- ``ioType``： 類型 0-控制器IO；1-擴充IO
    - ``current``： 焊接電流值(A)
    - ``AOIndex``： 焊接電流控制箱類比輸出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定焊接電壓
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltage(ioType, voltage, AOIndex, blend)``"
    "描述", "設定焊接電壓"
    "必選參數", "- ``ioType``： 類型 0-控制器IO；1-擴充IO
    - ``voltage``： 焊接電壓值(V)
    - ``AOIndex``： 焊接電流控制箱類比輸出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定擺動參數
++++++++++++++++++++++++++++++++++
.. versionchanged:: Python SDK-v2.0.8-3.7.8
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftRange, weaveRightRange, additionalStayTime, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary, weaveYawAngle=0)``"
    "描述", "設定擺動參數"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號
    - ``weaveType``： 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
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
    "默認參數", "- ``weaveYawAngle``： 摆動方向方位角（绕摆動Z軸旋转），單位°,默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    weaveNum =0
    weaveType = 0
    weaveFraquency = 1
    weavelncStayTime = 0
    weaveRange = 10
    weaveLeftStayTime = 10
    weaveRightStayTime = 10
    weaveCircleRadio =0
    weaveStationary =1
    #設定擺動參數
    ret = robot.WeaveSetPara(weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveSetPara ", ret)
    time.sleep(1)

    #擺盪開始
    ret = robot.WeaveStart(0)
    print("WeaveStart ", ret)
    time.sleep(1)
    ret,pose =robot.GetActualTCPPose(1);
    print(ret,pose)
    pose[2]=pose[2]+50
    ret = robot.MoveL(pose,tool,user)
    print("MoveL ", ret)
    time.sleep(1)
    #即时設定擺動參數
    ret = robot.WeaveOnlineSetPara (weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveOnlineSetPara ", ret)
    time.sleep(1)
    #擺盪結束
    ret = robot.WeaveEnd(0)
    print("WeaveEnd ", ret)
    time.sleep(1)

即时設定擺動參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveOnlineSetPara (weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)``"
    "描述", "即时設定擺動參數"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號
    - ``weaveType``： 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    - ``weaveFrequency``： 擺動頻率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-週期不包含等待時間；1-週期包含等待時間必選參數
    - ``weaveRange``： 擺動幅度(mm)
    - ``weaveLeftStayTime``： 擺動左停留時間(ms)
    - ``weaveRightStayTime``：  擺動右停留時間(ms)
    - ``weaveCircleRadio``： 圓形擺動-回調比率(0-100%)
    - ``weaveStationary``： 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

擺盪開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStart(weaveNum)``"
    "描述", "擺盪開始"
    "必選參數", "- ``weaveNum``： 類型 0-控制器IO；1-擴充IO"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

擺盪結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEnd(weaveNum)``"
    "描述", "擺盪結束"
    "必選參數", "- ``weaveNum``： 擺焊參數配置編號"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

正向送絲
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForwardWireFeed(ioType, wireFeed)``"
    "描述", "正向送絲"
    "必選參數", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送絲控制 0-停止送絲；1-送絲"
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

    weldIOType =0
    #正向送絲
    ret = robot.SetForwardWireFeed(weldIOType,1)
    print("SetForwardWireFeed錯誤碼", ret)
    time.sleep(1)
    ret = robot.SetForwardWireFeed(weldIOType,0)
    print("SetForwardWireFeed錯誤碼", ret)
    time.sleep(1)

    #反向送絲
    ret = robot.SetReverseWireFeed(weldIOType,1)
    print("SetReverseWireFeed錯誤碼", ret)
    time.sleep(1)
    #停止反向送絲
    ret = robot.SetReverseWireFeed(weldIOType,0)
    print("SetReverseWireFeed錯誤碼", ret)
    time.sleep(1)

    #送氣
    ret = robot.SetAspirated(weldIOType,1)
    print("SetAspirated錯誤碼", ret)
    time.sleep(1)
    #停止送氣
    ret = robot.SetAspirated(weldIOType,0)
    print("SetAspirated錯誤碼", ret)
    time.sleep(1)

反向送絲
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetReverseWireFeed(ioType, wireFeed)``"
    "描述", "反向送絲"
    "必選參數", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送絲控制 0-停止送絲；1-送絲"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

送氣
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAspirated(ioType, airControl)``"
    "描述", "送氣"
    "必選參數", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``airControl``： 送氣控制  0-停止送氣；1-送氣"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

段焊獲取位置與姿態
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSegmentWeldPoint(startPos, endPos, startDistance)``"
    "描述", "段焊獲取位置與姿態"
    "必選參數", "- ``startPos=[x,y,z,rx,ry,rz]``： 起始點座標
    - ``endPos=[x,y,z,rx,ry,rz]``： 終止點座標
    - ``startDistance``： 焊接點至起點的長度"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weldPointDesc=[x,y,z,rx,ry,rz]``： 焊接點的笛卡兒座標信息 
    - ``weldPointJoint=[j1,j2,j3,j4,j5,j6]``： 焊接點的關節座標信息
    - ``tool``： 工具號
    - ``user``： 工件號"

分段焊接啟動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldStart(startDesePos,  endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave,weaveNum,tool,user,vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0,exaxis_pos=[0.0, 0.0, 0.0, 0.0],  search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "分段焊接啟動"
    "必選參數", "- ``startDesePos``： 初始笛卡兒位姿，單位 [mm][°]
    - ``endDesePos``： 目標笛卡兒位姿，單位 [mm][°]
    - ``startJPos``：初始關節位置，單位 [°] 
    - ``endJPos``：目標關節位置，單位 [°]  
    - ``weldLength``：焊接長度，單位 [mm] 
    - ``noWeldLength``：非焊接長度，單位 [mm] 
    - ``weldIOType``：焊接IO類型(0-控制箱IO；1-擴展IO) arcNum 焊機設定檔編號 
    - ``timeout``：熄弧超時時間 
    - ``isWeave``：焊接 False-不焊接 
    - ``weaveNum``：擺焊參數配置編號 
    - ``tool``：工具號，[0~14]
    - ``user``：工件號，[0~14]"
    "默認參數", "- ``vel``：速度百分比，[0~100] 默認20.0
    - ``acc``：加速度[0~100] 暫不開放 默認0.0
    - ``ovl``：速度縮放因子，[0~100] 預設100.0
    - ``blendR``：[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，單位 [mm] 默認-1.0
    - ``exaxis_pos``：外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位
    - ``offset_flag``：[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0
    - ``offset_pos``：位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    weaveNum =0
    tool =1
    user =0
    weaveType = 0
    weaveFraquency = 1
    weavelncStayTime = 0
    weaveRange = 10
    weaveLeftStayTime = 10
    weaveRightStayTime = 10
    weaveCircleRadio =0
    weaveStationary =1
    start_desc=[0,0,0,0,0,0]
    end_desc=[0,0,0,0,0,0]
    start_joint=[0,0,0,0,0,0]
    end_joint=[0,0,0,0,0,0]
    ret,start_desc =robot.GetActualTCPPose(1);
    print("start_desc",start_desc)
    ret,end_desc =robot.GetActualTCPPose(1);
    end_desc[1]=end_desc[1]+200
    print("start_desc",start_desc)
    print("end_desc",end_desc)
    ret,start_joint=robot.GetInverseKin(0,start_desc)
    ret,end_joint=robot.GetInverseKin(0,end_desc)
    print("start_joint",start_joint)
    print("end_joint",end_joint)
    weldLength =40
    noweldLength =40
    #段焊

    ret = robot.SegmentWeldStart(start_desc,end_desc,start_joint,end_joint,weldLength,noweldLength,weldIOType,arcNum,weldTimeout,True,weaveNum,tool,user)
    print("SegmentWeldStart", ret)

分段焊接終止
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldEnd(ioType, arcNum, timeout)``"
    "描述", "分段焊接終止"
    "必選參數", "- ``ioType``：io 類型 0-控制器IO；1-擴展IO
    - ``arcNum``：焊機設定檔編號
    - ``timeout``：熄弧超時時間"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchStart(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊絲尋位開始"
    "必選參數", "- ``refPos``： 1-基準點 2-接觸點
    - ``searchVel``： 尋位速度 %
    - ``searchDis``： 尋位距離 mm
    - ``autoBackFlag``： 自動返回標誌，0-不自動；-自動
    - ``autoBackVel``： 自動返回速度 %
    - ``autoBackDis``： 自動返回距離 mm
    - ``offectFlag``： 1-帶偏移量尋位；2-示教點尋位"
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

    refPos = 1 #  1-基準點 2-接觸點
    searchVel = 10 #尋位速度 %
    searchDis = 100 #尋位距離 mm
    autoBackFlag = 0 #自動返回标志，0-不自動；1-自動
    autoBackVel = 10 #自動返回速度 %
    autoBackDis = 100 #自動返回距離 mm
    offectFlag = 0  #1-帶偏移量尋位；2-示教點尋位
    descStart =[203.061, 56.768, 62.719, -177.249, 1.456, -83.597]
    jointStart = [-127.012, -112.931, -94.078, -62.014, 87.186, 91.326]
    descEnd = [122.471, 55.718, 62.209, -177.207, 1.375, -76.310]
    jointEnd = [-119.728, -113.017, -94.027, -62.061, 87.199, 91.326]

    robot.MoveL(descStart,1,1,joint_pos= jointStart,vel=100)
    robot.MoveL(descEnd,1,1,joint_pos= jointEnd,vel=100)

    descREF0A = [147.139, -21.436, 60.717, -179.633, -3.051, -83.170]
    jointREF0A = [-121.731, -106.193, -102.561, -64.734, 89.972, 96.171]

    descREF0B = [139.247, 43.721, 65.361, -179.634, -3.043, -83.170]
    jointREF0B = [-122.364, -113.991, -90.860, -68.630, 89.933, 95.540]

    descREF1A = [289.747, 77.395, 58.390, -179.074, -2.901, -89.790]
    jointREF1A =[-135.719, -119.588, -83.454, -70.245, 88.921, 88.819]

    descREF1B = [259.310, 79.998, 64.774, -179.073, -2.900, -89.790]
    jointREF1B =[-133.133, -119.029, -83.326, -70.976, 89.069, 91.401]

    error = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0)
    print("WireSearchStart return:",error)

    robot.MoveL(descREF0A,1,1, joint_pos = jointREF0A, vel=100)
    print("MoveL(descREF0A return:",error)
    robot.MoveL(descREF0B,1,1, joint_pos = jointREF0B, vel=10,search=1)
    print("MoveL(descREF0B return:",error)

    error =robot.WireSearchWait("REF0")
    print("WireSearchWait return:",error)

    error = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0)
    print("WireSearchEnd return:",error)

    error = robot.WireSearchStart(1,10,100,0,10,100,0)
    print("WireSearchStart return:",error)

    robot.MoveL(descREF1A,1,1, joint_pos = jointREF1A, vel=100)
    robot.MoveL(descREF1B,1,1, joint_pos = jointREF1B, vel=10,search=1)

    error =robot.WireSearchWait("REF1")
    print("WireSearchWait return:",error)

    error = robot.WireSearchEnd(1,10,100,0,10,100,0)
    print("WireSearchEnd return:",error)

    error = robot.WireSearchStart(1,10,100,0,10,100,0)
    print("WireSearchStart return:",error)

    robot.MoveL(descREF0A,1,1, joint_pos = jointREF0A, vel=100)
    robot.MoveL(descREF0B,1,1, joint_pos = jointREF0B, vel=10,search=1)

    error =robot.WireSearchWait("RES0")
    print("WireSearchWait return:",error)

    error = robot.WireSearchEnd(1,10,100,0,10,100,0)
    print("WireSearchEnd return:",error)

    error = robot.WireSearchStart(1,10,100,0,10,100,0)
    print("WireSearchStart return:",error)

    robot.MoveL(descREF1A,1,1, joint_pos = jointREF1A, vel=100)
    robot.MoveL(descREF1B,1,1, joint_pos = jointREF1B, vel=10,search=1)

    error =robot.WireSearchWait("RES1")
    print("WireSearchWait return:",error)

    error = robot.WireSearchEnd(1,10,100,0,10,100,0)
    print("WireSearchEnd return:",error)

    varNameRef = ["REF0", "REF1", "#", "#", "#", "#"]
    varNameRes = ["RES0", "RES1", "#", "#", "#", "#"]
    error = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes)
    print("GetWireSearchOffect return:",error)
    if error[0]==0:
        ref = error[1]
        offdesc =error[2]

        error = robot.PointsOffsetEnable(ref,offdesc)
        print("PointsOffsetEnable return:",error)

        error = robot.MoveL(descStart, 1, 1, joint_pos=jointStart, vel=100)
        print("MoveL return:",error)
        robot.MoveL(descEnd, 1, 1, joint_pos=jointEnd, vel=10)
        print("MoveL return:",error)
        error = robot.PointsOffsetDisable()
        print("PointsOffsetDisable return:",error)

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
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

計算焊絲尋位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWireSearchOffset(seamType, method,varNameRef,varNameRes)``"
    "描述", "計算焊絲尋位偏移量"
    "必選參數", "- ``seamType``： 焊缝類型
    - ``method``： 計算方法
    - ``varNameRef``： 基準點1-6，「#」表示無點變數
    - ``varNameRes``： 接觸點1-6，「#」表示無點變數"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
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
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

焊絲尋位接觸點寫入資料庫
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPointToDatabase(varName,pos)``"
    "描述", "焊絲尋位接觸點寫入資料庫"
    "必選參數", "- ``varName``： 接觸點名稱 “RES0” ~ “RES99”
    - ``pos``：接触點數據[x, y, x, a, b, c]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

電弧追蹤控制
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd, sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent)``"
    "描述", "電弧追蹤控制"
    "必選參數", "- ``flag``： 開關，0-關；1-開
    - ``delayTime``：滯後時間，單位ms
    - ``isLeftRight``：左右偏差補償 0-關閉，1-開啟
    - ``klr``：左右調節係數(靈敏度)
    - ``tStartLr``：左右開始補償時間cyc
    - ``stepMaxLr``：左右每次最大補償量 mm
    - ``sumMaxLr``：左右總計最大補償量 mm
    - ``isUpLow``：上下偏差補償 0-關閉，1-開啟
    - ``kud``：上下調節係數(靈敏度)
    - ``tStartUd``：上下開始補償時間cyc
    - ``stepMaxUd``：上下每次最大補償量 mm
    - ``sumMaxUd``：上下总计最大补偿量
    - ``axisSelect``：上下座標系選擇，0-擺動；1-工具；2-基座
    - ``referenceType``：上下基準電流設定方式，0-回饋；1-常數
    - ``referSampleStartUd``：上下基準電流取樣開始計數(回饋)，cyc
    - ``referSampleCountUd``：上下基準電流取樣循環計數(回饋)，cyc
    - ``referenceCurrent``：上下基準電流mA"
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

    flag = 1 #開關，0-關；1-開
    delaytime=0 #滯後時間，單位ms
    isLeftRight=0 #左右偏差補償 0-關閉，1-開啟
    klr = 0.06 #左右調節係數(靈敏度)
    tStartLr = 5 #左右開始補償時間cyc
    stepMaxLr =5 #左右每次最大補償量 mm
    sumMaxLr = 300 #左右總計最大補償量 mm
    isUpLow = 1 #上下偏差補償
    kud =-0.06 #上下調節係數(靈敏度)
    tStartUd = 5 #上下開始補償時間cyc
    stepMaxUd = 5 #上下每次最大補償量 mm
    sumMaxUd = 300 #上下总计最大补偿量
    axisSelect = 1 #上下座標系選擇，0-擺動；1-工具；2-基座
    referenceType = 0 #上下基準電流設定方式，0-回饋；1-常數
    referSampleStartUd = 4 # 上下基準電流取樣開始計數(回饋)，cyc
    referSampleCountUd = 1 # 上下基準電流取樣循環計數(回饋)，cyc
    referenceCurrent = 10 # 上下基準電流mA

    startdescPose = [-583.168, 325.637, 1.176, 75.262, 0.978, -3.571]
    startjointPos = [-49.049, -77.203, 136.826, -189.074, -79.407, -11.811]
    enddescPose = [-559.439, 420.491, 32.252, 77.745, 1.460, -10.130]
    endjointPos = [-54.986, -77.639, 131.865, -185.707, -80.916, -12.218]

    error = robot.WeldingSetCurrent(1, 230, 0)
    print("WeldingSetCurrent return:",error)
    robot.WeldingSetVoltage(1, 24, 0)

    print("WeldingSetVoltage return:",error)
    robot.ArcWeldTraceExtAIChannelConfig(0)
    print("ArcWeldTraceExtAIChannelConfig return:",error)

    robot.MoveJ(startjointPos,13,0,desc_pos=startdescPose,vel =5)
    print("MoveJ return:",error)

    error = robot.ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd,
                                sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent)
    print("WireSearchStart return:",error)

    robot.ARCStart(1, 0, 10000)
    print("ARCStart return:",error)

    robot.MoveL(enddescPose,13,0,joint_pos=endjointPos,vel =5)
    print("MoveJ return:",error)

    robot.ARCEnd(1, 0, 10000)
    print("ARCEnd return:",error)

    flag = 0
    error = robot.ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd,
                                sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent)
    print("WireSearchStart return:",error)

電弧追蹤AI通帶選擇
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceExtAIChannelConfig(channel)``"
    "描述", "電弧追蹤AI通帶選擇"
    "必選參數", "- ``channel``：電弧追蹤AI通帶選擇,[0-3]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

仿真擺盪開始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStartSim(weaveNum)``"
    "描述", "仿真擺盪開始"
    "必選參數", "- ``weaveNum``：擺動參數編號"
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

    desc1 = [238.209, -403.633, 251.291, 177.222, -1.433, 133.675]
    joint1= [-48.728, -86.235, -95.288, -90.025, 92.715, 87.595]
    desc2 = [238.207, -596.305, 251.294, 177.223, -1.432, 133.675]
    joint2= [-60.240, -110.743, -66.784, -94.531, 92.351, 76.078 ]


    error = robot.MoveL(desc1,1,0,joint_pos=joint1)
    print("MoveL return:",error)

    error = robot.WeaveStartSim(0)
    print("WeaveStartSim return:",error)

    error = robot.MoveL(desc2,1,0,joint_pos=joint2)
    print("MoveL return:",error)

    error = robot.WeaveEndSim(0)
    print("WeaveEndSim return:",error)

仿真擺盪結束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEndSim(weaveNum)``"
    "描述", "仿真擺盪結束"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

開始軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectStart(weaveNum)``"
    "描述", "開始軌跡偵測預警(不運動)"
    "必選參數", "- ``weaveNum``：擺動參數編號"
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

    desc1 = [238.209, -403.633, 251.291, 177.222, -1.433, 133.675]
    joint1= [-48.728, -86.235, -95.288, -90.025, 92.715, 87.595]
    desc2 = [238.207, -596.305, 251.294, 177.223, -1.432, 133.675]
    joint2= [-60.240, -110.743, -66.784, -94.531, 92.351, 76.078 ]

    error = robot.MoveL(desc1,1,0,joint_pos=joint1)
    print("MoveL return:",error)

    error = robot.WeaveInspectStart(0)
    print("WeaveInspectStart return:",error)

    error = robot.MoveL(desc2,1,0,joint_pos=joint2)
    print("MoveL return:",error)

    error = robot.WeaveInspectEnd(0)
    print("WeaveInspectEnd return:",error)
    
結束軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectEnd(weaveNum)``"
    "描述", "結束軌跡偵測預警(不運動)"
    "必選參數", "- ``weaveNum``：擺動參數編號"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
    
設定焊接製程曲線參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime)``"
    "描述", "設定焊接製程曲線參數"
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
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
            
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    id = 1 #焊接工藝編號(1-99)
    startCurrent = 177 #起弧電流(A)
    startVoltage = 27 #起弧電壓(V)
    startTime = 1000 #起弧時間(ms)
    weldCurrent = 178 #焊接電流(A)
    weldVoltage = 28 #焊接電壓(V)
    endCurrent = 176 #收弧電流(A)
    endVoltage = 26 # 收弧電壓(V)
    endTime = 1000 #收弧時間(ms)

    error = robot.WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage,
                                            endCurrent, endVoltage, endTime)

    print("WeldingSetProcessParam return:",error)

    error = robot.WeldingGetProcessParam(1)
    print("WeldingGetProcessParam return:",error)
        
取得焊接製程曲線參數
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetProcessParam(id)``"
    "描述", "取得焊接製程曲線參數"
    "必選參數", "
    - ``id``： 焊接工藝編號(1-99)
    "
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``傳回值（调用成功返回） startCurrent``：起弧電流(A)
    - ``startVoltage``： 起弧電壓(V)
    - ``startTime``：起弧時間(ms)
    - ``weldCurrent``：焊接電流(A)
    - ``weldVoltage``：焊接電壓(V)
    - ``endCurrent``：收弧電流(A)
    - ``endVoltage``：收弧電壓(V)
    - ``endTime``：收弧時間(ms)
    " 
    
擴展IO-配置焊機氣體偵測訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAirControlExtDoNum(DONum)``"
    "描述", "擴展IO-配置焊機氣體偵測訊號"
    "必選參數", "
    - ``DONum``：氣體偵測訊號擴展DO編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
            
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    #擴展IO-配置焊機氣體偵測訊號
    error = robot.SetAirControlExtDoNum(10)
    print("SetAirControlExtDoNum 10 return:",error)

    #擴充IO-配置焊接機起弧訊號
    error = robot.SetArcStartExtDoNum(11)
    print("SetArcStartExtDoNum 11 return:",error)

    #擴充IO-配置焊接機反向送絲訊號
    error = robot.SetWireReverseFeedExtDoNum(12)
    print("SetWireReverseFeedExtDoNum 12 return:",error)

    #擴充IO-配置焊接機正向送絲訊號
    error = robot.SetWireForwardFeedExtDoNum(13)
    print("SetWireForwardFeedExtDoNum 13 return:",error)

    #擴充IO-配置焊接機起弧成功訊號
    error = robot.SetArcDoneExtDiNum(10)
    print("SetArcDoneExtDiNum 10 return:",error)

    #擴充IO-配置焊接機準備訊號
    error = robot.SetWeldReadyExtDiNum(11)
    print("SetWeldReadyExtDiNum 11 return:",error)

    #擴展IO-配置焊接中斷恢復訊號
    error = robot.SetExtDIWeldBreakOffRecover(12,13)
    print("SetExtDIWeldBreakOffRecover 12  13 return:",error)
        
擴充IO-配置焊接機起弧訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcStartExtDoNum(DONum)``"
    "描述", "擴充IO-配置焊接機起弧訊號"
    "必選參數", "
    - ``DONum``：氣體偵測訊號擴展DO編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
        
擴充IO-配置焊接機反向送絲訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireReverseFeedExtDoNum(DONum)``"
    "描述", "擴充IO-配置焊接機反向送絲訊號"
    "必選參數", "
    - ``DONum``：氣體偵測訊號擴展DO編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
        
擴充IO-配置焊接機正向送絲訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireForwardFeedExtDoNum(DONum)``"
    "描述", "擴充IO-配置焊接機正向送絲訊號"
    "必選參數", "
    - ``DONum``：氣體偵測訊號擴展DO編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
        
擴充IO-配置焊接機起弧成功訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "擴充IO-配置焊接機起弧成功訊號"
    "必選參數", "
    - ``DINum``：焊接機準備訊號擴展DI編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
        
擴充IO-配置焊接機準備訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "擴充IO-配置焊接機準備訊號"
    "必選參數", "
    - ``DINum``：焊接機準備訊號擴展DI編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 
        
擴展IO-配置焊接中斷恢復訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExtDIWeldBreakOffRecover(reWeldDINum, abortWeldDINum)``"
    "描述", "擴展IO-配置焊接中斷恢復訊號"
    "必選參數", "
    - ``reWeldDINum``：焊接中斷後恢復焊接訊號擴展DI編號
    - ``abortWeldDINum``：焊接中斷後退出焊接訊號擴展DI編號
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

設定焊絲尋位擴充IO端口
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireSearchExtDIONum(searchDoneDINum, searchStartDONum)``"
    "描述", "設定焊絲尋位擴充IO端口"
    "必選參數", "- ``searchDoneDINum``：焊絲尋位成功DO端口(0-127)
    - ``searchStartDONum``：焊絲尋位啟動停止控制DO端口(0-127)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

焊机控制模式切换
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

設定焊機控制模式擴展DO端口
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlModeExtDoNum(DONum)``"
    "描述", "設定焊機控制模式擴展DO端口"
    "必選參數", "- ``DONum``：焊機控制模式DO端口(0-127)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

設定焊機控制模式
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlMode(mode)``"
    "描述", "設定焊機控制模式"
    "必選參數", "- ``mode``：焊接機控制模式;0-一元化"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode" 

代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10)
    print("ExtDevSetUDPComParam return ", error)
    error = robot.ExtDevLoadUDPDriver()
    print("ExtDevLoadUDPDriver return ", error)

    robot.SetWeldMachineCtrlModeExtDoNum(DONum=17)
    robot.SetWeldMachineCtrlMode(mode=0)
    robot.SetWeldMachineCtrlModeExtDoNum(DONum=18)
    robot.SetWeldMachineCtrlMode(mode=0)
    robot.SetWeldMachineCtrlModeExtDoNum(DONum=19)
    robot.SetWeldMachineCtrlMode(mode=0)

    error = robot.SetWeldMachineCtrlModeExtDoNum(DONum=17)
    print("SetWeldMachineCtrlModeExtDoNum return ", error)
    for  i  in  range(0,5):
        error = robot.SetWeldMachineCtrlMode(mode=0)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)
        error = robot.SetWeldMachineCtrlMode(mode=1)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)

    error = robot.SetWeldMachineCtrlModeExtDoNum(DONum=18)
    print("SetWeldMachineCtrlModeExtDoNum return ", error)
    for  i  in  range(0,5):
        error = robot.SetWeldMachineCtrlMode(mode=0)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)
        error = robot.SetWeldMachineCtrlMode(mode=1)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)

    error = robot.SetWeldMachineCtrlModeExtDoNum(DONum=19)
    print("SetWeldMachineCtrlModeExtDoNum return ", error)
    for  i  in  range(0,5):
        error = robot.SetWeldMachineCtrlMode(mode=0)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)
        error = robot.SetWeldMachineCtrlMode(mode=1)
        print("SetWeldMachineCtrlMode return ", error)
        time.sleep(0.5)

電弧追蹤 + 多層多道補償開啟
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayStart()``"
    "描述", "電弧追蹤 + 多層多道補償開啟"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

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
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MultilayerOffsetTrsfToBase(pointo, pointX, pointZ, dx, dy, db)``"
    "描述", "偏移量座標變化-多層多道焊"
    "必選參數", "- ``pointo``：基准點笛卡兒位姿
    - ``pointX``：基准點X向偏移方向點笛卡兒位姿
    - ``pointZ``：基准點Z向偏移方向點笛卡兒位姿
    - ``dx``：x方向偏移量(mm)
    - ``dz``：z方向偏移量(mm)
    - ``dry``：绕y軸偏移量(°)"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``offset``：計算結果偏移量"

設定機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingSetCheckArcInterruptionParam(checkEnable, arcInterruptTimeLength)``"
 "描述", "設定機器人焊接電弧意外中斷偵測參數"
 "必選參數", "- ``checkEnable``：是否使能檢測；0-不使能；1-使能
 - ``arcInterruptTimeLength``：電弧中斷確認時長(ms)"
 "預設參數", "無"
 "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingGetCheckArcInterruptionParam()``"
 "描述", "取得機器人焊接電弧意外中斷偵測參數"
 "必選參數", "無"
 "預設參數", "無"
 "傳回值", "- 錯誤碼 成功-0 失敗- errcode
 - ``checkEnable``：是否使能偵測；0-不使能；1-使能
 - ``arcInterruptTimeLength``：電弧中斷確認時長(ms)"

設定機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingSetReWeldAfterBreakOffParam(enable, length, velocity, moveType)``"
 "描述", "設定機器人焊接中斷恢復參數"
 "必選參數", "- ``enable``：是否使能焊接中斷恢復
 - ``length``：焊縫重疊距離(mm)
 - ``velocity``：機器人回到再起弧點速度百分比(0-100)
 - ``moveType``：機器人運動到再起弧點方式；0-LIN；1-PTP"
 "預設參數", "無"
 "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingGetReWeldAfterBreakOffParam()``"
 "描述", "取得機器人焊接中斷恢復參數"
 "必選參數", "無"
 "預設參數", "無"
 "傳回值", "- 錯誤碼 成功-0 失敗- errcode
 - ``enable``：是否使能焊接中斷恢復
 - ``length``：焊縫重疊距離(mm)
 - ``velocity``：機器人回到再起弧點速度百分比(0-100)
 - ``moveType``：機器人運動到再起弧點方式；0-LIN；1-PTP"

設定機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingStartReWeldAfterBreakOff()``"
 "描述", "設定機器人焊接中斷後恢復焊接"
 "必選參數", "無"
 "預設參數", "無"
 "傳回值", "錯誤碼 成功-0 失敗- errcode "

設定機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8-3.7.8

.. csv-table::
 :stub-columns: 1
 :widths: 10 30

 "原型", "``WeldingAbortWeldAfterBreakOff()``"
 "描述", "設定機器人焊接中斷後退出焊接"
 "必選參數", "無"
 "預設參數", "無"
 "傳回值", "錯誤碼 成功-0 失敗- errcode "

程式碼範例
------------
.. code-block:: python
 :linenos:

 from fairino import Robot
 # 與機器人控制器建立連接，連接成功返回一個機器人對象
 robot = Robot.RPC('192.168.58.2')

 rtn = -1
 rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200)
 print("WeldingSetCheckArcInterruptionParam return", rtn)
 rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0)
 print("WeldingSetReWeldAfterBreakOffParam return", rtn)
 enable = 0
 length = 0
 velocity = 0
 moveType = 0
 checkEnable = 0
 arcInterruptTimeLength = 0
 rtn, checkEnable, arcInterruptTimeLength = robot.WeldingGetCheckArcInterruptionParam()
 print("WeldingGetCheckArcInterruptionParam checkEnable:", checkEnable)
 print("WeldingGetCheckArcInterruptionParam arcInterruptTimeLength:", arcInterruptTimeLength)
 rtn, enable, length, velocity, moveType = robot.WeldingGetReWeldAfterBreakOffParam()
 print("*****")
 print("WeldingGetReWeldAfterBreakOffParam enable:", enable)
 print("WeldingGetReWeldAfterBreakOffParam length:", length)
 print("WeldingGetReWeldAfterBreakOffParam velocity:", velocity)
 print("WeldingGetReWeldAfterBreakOffParam moveType:", moveType)

 robot.ProgramLoad("/fruser/test.lua")
 robot.ProgramRun()

 time.sleep(5)

 while True:
 print("welding breakoff state is ", robot.robot_state_pkg.weldingBreakOffState.breakOffState)
 if robot.robot_state_pkg.weldingBreakOffState.breakOffState == 1:
 print("welding breakoff !")
 time.sleep(2)
 rtn = robot.WeldingStartReWeldAfterBreakOff()
 print("WeldingStartReWeldAfterBreakOff return", rtn)
 break
 time.sleep(0.1)