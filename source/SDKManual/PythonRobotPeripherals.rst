機器人外設
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "描述", "配置夾爪"
    "必選參數", "- ``company``：夾爪廠商，1-Robotiq，2-慧靈，3-天機，4-大寰，5-知行；
    - ``device``：設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)"
    "默認參數", "- ``softversion``：軟件版本號，暫不使用，默認爲0；
    - ``bus``：設備掛載末端總線位置，暫不使用，默認爲0；"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取夾爪配置
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperConfig()``"
    "描述", "獲取夾爪配置"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``[number,company,device,softversion]``： number，夾爪編號;company，夾爪廠商，1-Robotiq，2-慧靈，3-天機，4-大寰，5-知行 ;device，設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20);softvesion，軟件版本號，暫不使用，默認爲0。"

激活夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ActGripper(index,action)``"
    "描述", "激活夾爪"
    "必選參數", "- ``index``:夾爪編號；
    - ``action``:0-復位，1-激活"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

控制夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "描述", "控制夾爪"
    "必選參數", "- ``index``:夾爪編號；
    - ``pos``:位置百分比，範圍[0~100]；
    - ``vel``:速度百分比，範圍[0~100];
    - ``force``:力矩百分比，範圍[0~100]；
    - ``maxtime``:最大等待時間，範圍[0~30000]，單位[ms]；
    - ``block``:0-阻塞，1-非阻塞；
    - ``type``:夾爪類型，0-平行夾爪；1-旋轉夾爪；
    - ``rotNum``:rotNum 旋轉圈數；
    - ``rotVel``:旋轉速度百分比[0-100]；
    - ``rotTorque``:旋轉力矩百分比[0-100]。"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取夾爪運動狀態
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperMotionDone()``"
    "描述", "獲取夾爪運動狀態(僅末端開放協定定義，已適配設備獲取的運動狀態為透傳值)"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``[fault,status]``：夾爪運動狀態，fault:0-無錯誤，其他-有錯誤；status:0-運動未完成，1-運動完成未偵測到物體 2-運動完成偵測到物體"

獲取夾爪激活狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperActivateStatus()``"
    "描述", "獲取夾爪激活狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``gripper_active``：bit0~bit15對應夾爪編號0~15，bit=0爲未激活，bit=1爲激活"

獲取夾爪位置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurPosition()``"
    "描述", "獲取夾爪位置"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``position``：位置百分比，範圍0~100%"

獲取夾爪速度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurSpeed()``"
    "描述", "獲取夾爪速度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``speed``：速度百分比，範圍0~100%"

獲取夾爪電流
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperCurCurrent()``"
    "描述", "獲取夾爪電流"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``current``：電流百分比，範圍0~100%"

獲取夾爪電壓
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperVoltage()``"
    "描述", "獲取夾爪電壓"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``voltage``：電壓,單位0.1V"

獲取夾爪溫度
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperTemp()``"
    "描述", "獲取夾爪溫度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``temp``：溫度，單位℃"

計算預抓取點-視覺
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "描述", "計算預抓取點-視覺"
    "必選參數", "- ``desc_pos``：夾抓取點笛卡爾位姿;
    - ``zlength``：z軸偏移量;
    - ``zangle``：繞z軸旋轉偏移量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``pre_pos``：預抓取點笛卡爾位姿"

計算撤退點-視覺
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "描述", "計算撤退點-視覺"
    "必選參數", "- ``desc_pos``：抓取點笛卡爾位姿;
    - ``zlength``：z軸偏移量;
    - ``zangle``：繞z軸旋轉偏移量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``post_pos``：撤退點笛卡爾位姿"

機器人夾爪操作代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 4
    device = 0
    softversion = 0
    bus = 2
    index = 2
    act = 0
    max_time = 30000
    block = 0
    status = 0
    fault = 0
    active_status = 0
    current_pos = 0
    current = 0
    voltage = 0
    temp = 0
    speed = 0
    robot.SetGripperConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.GetGripperConfig()
    print(f"gripper config:{company},{device},{softversion},{bus}")
    robot.ActGripper(index, act)
    time.sleep(1)
    act = 1
    robot.ActGripper(index, act)
    time.sleep(1)
    error = robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    time.sleep(1)
    error = robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{error}")
    error, [fault, status] = robot.GetGripperMotionDone()
    print(f"motion status:{fault},{status}")
    error, [fault, active_status] = robot.GetGripperActivateStatus()
    print(f"gripper active fault is:{fault},status is:{active_status}")
    error, [fault, current_pos] = robot.GetGripperCurPosition()
    print(f"fault is:{fault},current position is:{current_pos}")
    error, [fault, current] = robot.GetGripperCurCurrent()
    print(f"fault is:{fault},current current is:{current}")
    error, [fault, voltage] = robot.GetGripperVoltage()
    print(f"fault is:{fault},current voltage is:{voltage}")
    error, [fault, temp] = robot.GetGripperTemp()
    print(f"fault is:{fault},current temperature is:{temp}")
    error, [fault, speed] = robot.GetGripperCurSpeed()
    print(f"fault is:{fault},current speed is:{speed}")
    retval = 0
    prepick_pose = [0.0]*6
    postpick_pose = [0.0]*6
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval, prepick_pose = robot.ComputePrePick(p1Desc, 10, 0)
    print(f"ComputePrePick retval is:{retval}")
    print(f"xyz is:{prepick_pose[0]},{prepick_pose[1]},{prepick_pose[2]};rpy is:{prepick_pose[3]},{prepick_pose[4]},{prepick_pose[5]}")
    retval, postpick_pose = robot.ComputePostPick(p2Desc, -10, 0)
    print(f"ComputePostPick retval is:{retval}")
    print(f"xyz is:{postpick_pose[0]},{postpick_pose[1]},{postpick_pose[2]};rpy is:{postpick_pose[3]},{postpick_pose[4]},{postpick_pose[5]}")
    robot.CloseRPC()

獲取旋轉夾爪的旋轉圈數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotNum()``"
    "描述", "獲取旋轉夾爪的旋轉圈數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``num``：旋轉圈數"

獲取旋轉夾爪的旋轉速度百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotSpeed()``"
    "描述", "獲取旋轉夾爪的旋轉速度百分比"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``speed``：旋轉速度百分比"

獲取旋轉夾爪的旋轉力矩百分比
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperRotTorque()``"
    "描述", "獲取旋轉夾爪的旋轉力矩百分比"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``fault``：0-無錯誤，1-有錯誤
    - ``torque``：旋轉力矩百分比"

獲取旋轉夾爪狀態代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    fault = 0
    rotNum = 0.0
    rotSpeed = 0
    rotTorque = 0
    error,fault, rotNum = robot.GetGripperRotNum()
    error,fault, rotSpeed = robot.GetGripperRotSpeed()
    error,fault, rotTorque = robot.GetGripperRotTorque()
    print(f"gripper rot num:{rotNum},gripper rotSpeed:{rotSpeed},gripper rotTorque:{rotTorque}")
    robot.CloseRPC()

傳動帶啓動、停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorStartEnd(status)``"
    "描述", "傳動帶啓動、停止"
    "必選參數", "- ``status``： 傳動帶狀態，1-啓動，0-停止"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

記錄IO檢測點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointIORecord()``"
    "描述", "記錄IO檢測點"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

記錄A點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointARecord()``"
    "描述", "記錄A點"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

記錄參考點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorRefPointRecord()``"
    "描述", "記錄參考點"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

記錄B點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointBRecord()``"
    "描述", "記錄B點"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳送帶工件IO檢測
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorIODetect(max_t)``"
    "描述", "傳送帶工件IO檢測"
    "必選參數", "- ``max_t``： 最大檢測時間，單位ms"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取物體當前位置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorGetTrackData(mode)``"
    "描述", "獲取物體當前位置"
    "必選參數", "- ``mode``： 1-跟蹤抓取 2-跟蹤運動 3-TPD跟蹤"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳動帶跟蹤開始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackStart(status)``"
    "描述", "傳動帶跟蹤開始"
    "必選參數", "- ``status``： 狀態，1-啓動，0-停止"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳動帶跟蹤停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackEnd()``"
    "描述", "傳動帶跟蹤停止"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳動帶參數配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param, followType, startDis, endDis)``"
    "描述", "傳動帶參數配置"
    "必選參數", "- ``param``： = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                    - ``encChannel``: 編碼器通道 1-2
                    - ``resolution``: 編碼器分辨率 編碼器旋轉一圈脈衝個數
                    - ``lead``: 機械傳動比 編碼器旋轉一圈傳送帶移動距離
                    - ``wpAxis``: 工件座標系編號 針對跟蹤運動功能選擇工件座標系編號，跟蹤抓取、TPD跟蹤設爲0
                    - ``vision``: 是否配視覺  0-不配 1-配,
                    - ``speedRadio``: 速度比  針對傳送帶跟蹤抓取速度範圍爲（1-100）  跟蹤運動、TPD跟蹤設置爲1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳動帶抓取點補償
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorCatchPointComp(cmp)``"
    "描述", "傳動帶抓取點補償"
    "必選參數", "- ``cmp``： 補償位置 [x,y,z]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

直線運動
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackMoveL(name,tool,wobj,vel=20,acc=100,ovl=100,blendR=-1.0)``"
    "描述", "直線運動"
    "必選參數", "- ``name``：cvrCatchPoint 或cvrRaisePoint
    - ``tool``: 工具號
    - ``wobj``:  工件號"
    "默認參數", "- ``vel``: 速度 默認20
    - ``acc``: 加速度 默認100
    - ``ovl``: 速度縮放因子 默認100
    - ``blendR``: [-1.0]-運動到位 (阻塞)，[0~1000]-平滑半徑 (非阻塞)，單位 [mm] 默認-1.0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳送帶通訊輸入檢測
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetect(timeout)``"
    "描述", "傳送帶通訊輸入檢測"
    "必選參數", "- ``timeout``：等待超時時間ms"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳送帶通訊輸入檢測觸發
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetectTrigger()``"
    "描述", "傳送帶通訊輸入檢測觸發"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人傳送帶操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.ConveyorStartEnd(1)
    print(f"ConveyorStartEnd retval is:{retval}")
    retval = robot.ConveyorPointIORecord()
    print(f"ConveyorPointIORecord retval is:{retval}")
    retval = robot.ConveyorPointARecord()
    print(f"ConveyorPointARecord retval is:{retval}")
    retval = robot.ConveyorRefPointRecord()
    print(f"ConveyorRefPointRecord retval is:{retval}")
    retval = robot.ConveyorPointBRecord()
    print(f"ConveyorPointBRecord retval is:{retval}")
    retval = robot.ConveyorStartEnd(0)
    print(f"ConveyorStartEnd retval is:{retval}")
    param = [1.0, 10000.0, 200.0, 0.0, 0.0, 20.0]
    retval = robot.ConveyorSetParam(param,0)
    print(f"ConveyorSetParam retval is:{retval}")
    cmp = [0.0, 0.0, 0.0]
    retval = robot.ConveyorCatchPointComp(cmp)
    print(f"ConveyorCatchPointComp retval is:{retval}")
    index = 1
    max_time = 30000
    block = 0
    retval = 0
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    retval = robot.MoveCart(p1Desc, 1, 0, 100.0)
    print(f"MoveCart retval is:{retval}")
    retval = robot.WaitMs(1)
    print(f"WaitMs retval is:{retval}")
    retval = robot.ConveyorIODetect(10000)
    print(f"ConveyorIODetect retval is:{retval}")
    retval = robot.ConveyorGetTrackData(1)
    print(f"ConveyorGetTrackData retval is:{retval}")
    retval = robot.ConveyorTrackStart(1)
    print(f"ConveyorTrackStart retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100)
    print(f"TrackMoveL retval is:{retval}")
    retval = robot.ConveyorTrackEnd()
    print(f"ConveyorTrackEnd retval is:{retval}")
    robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0)
    retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0)
    print(f"MoveGripper retval is:{retval}")
    robot.CloseRPC()

傳送帶原地跟蹤參數配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStationaryTrackPara(self, trackMode, trackTime, trackDis)``"
    "描述", "傳送帶原地跟蹤參數配置"
    "必選參數", "
    - ``trackMode``: 0-時間；1-距離；2-時間和距離任意滿足一個
    - ``trackTime``: 跟蹤時間，單位s
    - ``trackDis``: 跟蹤距離
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

等待原地空運動完成
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitStationaryMotionDone(self)``"
    "描述", "等待原地空運動完成"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

傳送帶原地跟蹤運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-V3.9.8

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time


    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5) 
        j1 = [-35.146, -102.684, 120.805, -100.401, -90.295, 150.105]
        d1 = [-121.814, -348.341, 209.978, -173.152, -3.585, -5.446]

        ex = [0.0, 0.0, 0.0, 0.0]
        zeroOff = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        tool = 1
        workpiece = 1

        para = [0, 10000, 200, 0, 0, 10]
    
        rtn = robot.ConveyorSetParam(para= para)
        print(f"ConveyorSetParam rtn is {rtn}")

        robot.MoveJ(joint_pos=j1, desc_pos=d1, tool=tool, user=workpiece,
                    vel=100, acc=100, ovl=100, exaxis_pos=ex,
                    blendT=-1, offset_flag=0, offset_pos=zeroOff)

        print("--- Step 1: SetDO(6,1) ---")
        rtn = robot.SetDO(6, 1, 0, 0)
        print(f"  SetDO(6,1) rtn={rtn}")

        print("--- Step 2: ConveyorTrackStart(2) ---")
        rtn = robot.ConveyorTrackStart(2)
        print(f"  ConveyorTrackStart(2) rtn={rtn}")

        print("--- Step 3: ConveyorIODetect(10000) ---")
        rtn = robot.ConveyorIODetect(10000)
        print(f"  ConveyorIODetect(10000) rtn={rtn}")

        print("--- Step 4: ConveyorGetTrackData(2) ---")
        rtn = robot.ConveyorGetTrackData(2)
        print(f"  ConveyorGetTrackData(2) rtn={rtn}")

        print("--- Step 5: SetStationaryTrackPara(0,5,5) ---")
        rtn = robot.SetStationaryTrackPara(0, 5, 5)
        print(f"  SetStationaryTrackPara(0,5,5) rtn={rtn}")

        print("--- Step 6: MoveStationary() ---")
        rtn = robot.MoveStationary()
        print(f"  MoveStationary() rtn={rtn}")

        rtn = robot.WaitStationaryMotionDone()
        print(f"  WaitStationaryMotionDone() rtn={rtn}")

        print("--- Step 7: ConveyorTrackEnd() ---")
        rtn = robot.ConveyorTrackEnd()
        print(f"  ConveyorTrackEnd() rtn={rtn}")

        print("--- Step 8: SetDO(6,0) ---")
        rtn = robot.SetDO(6, 0, 0, 0)
        print(f"  SetDO(6,0) rtn={rtn}")

        robot.CloseRPC()


    if __name__ == "__main__":
        main()

末端傳感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfig(idCompany, idDevice, idSoftware, idBus)``"
    "描述", "末端傳感器配置"
    "必選參數", "
    - ``idCompany``: 廠商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 類型，0-JUNKONG/RYR6T.V1.0
    - ``idSoftware``: 軟件版本，0-J1.0/HuiDe1.0(暫未開放)
    - ``idBus``: 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取末端傳感器配置
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorConfigGet()``"
    "描述", "獲取末端傳感器配置"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``idCompany``: 廠商，18-JUNKONG；25-HUIDE
    - ``idDevice``: 類型，0-JUNKONG/RYR6T.V1.0"
        
末端傳感器激活
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorActivate(actFlag)``"
    "描述", "末端傳感器激活"
    "必選參數", "``actFlag``： 0-復位；1-激活"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``: 座標系值[x,y,z,rx,ry,rz]"

末端傳感器寄存器寫入
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端傳感器寄存器寫入"
    "必選參數", "- ``devAddr``：設備地址編號 0-255
    - ``regHAddr``：寄存器地址高8位
    - ``regLAddr``：寄存器地址低8位
    - ``regNum``：寄存器個數 0-255
    - ``data1``：寫入寄存器數值1
    - ``data2``：寫入寄存器數值2
    - ``isNoBlock``：是否阻塞 0-阻塞；1-非阻塞"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

末端傳感器代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleSensorConfig(18, 0, 0, 1)
    error, company, type = robot.AxleSensorConfigGet()
    print(f"company is:{company},type is:{type}")
    rtn = robot.AxleSensorActivate(1)
    print(f"AxleSensorActivate rtn is:{rtn}")
    time.sleep(1)
    rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0)
    print(f"AxleSensorRegWrite rtn is:{rtn}")
    robot.CloseRPC()

獲取機器人外設協議
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExDevProtocol()``"
    "描述", "獲取機器人外設協議"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode; 
    - ``protocol``: 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster"

設置機器人外設協議
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExDevProtocol(protocol)``"
    "描述", "設置機器人外設協議"
    "必選參數", "- ``protocol``：機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置機器人外設協議代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    protocol = 4096
    rtn = robot.SetExDevProtocol(protocol)
    print(f"SetExDevProtocol rtn:{rtn}")
    rtn, protocol = robot.GetExDevProtocol()
    print(f"GetExDevProtocol rtn:{rtn},protocol is:{protocol}")
    robot.CloseRPC()


獲取末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleCommunicationParam()``"
    "描述", "獲取末端通訊參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：數據位:數據位支持（8,9），目前常用爲 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用爲 1
    - ``verify``：校驗位:0-None，1-Odd，2-Even,目前常用爲 0
    - ``timeout``：超時時間:1~1000ms，此值需要結合外設搭配設置合理的時間參數
    - ``timeoutTimes``：超時次數:1~10，主要進行超時重發，減少偶發異常提高用戶體驗
    - ``period``：週期性指令時間間隔:1~1000ms，主要用於週期性指令每次下發的時間間隔"

設置末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleCommunicationParam(baudRate, dataBit, stopBit, verify, timeout, timeoutTimes, period)``"
    "描述", "設置末端通訊參數"
    "必選參數", "- ``baudRate``：波特率:支持1-9600，2-14400，3-19200，4-38400，5-56000，6-67600，7-115200，8-128000
    - ``dataBit``：數據位:數據位支持（8,9），目前常用爲 8
    - ``stopBit``：停止位:1-1，2-0.5，3-2，4-1.5，目前常用爲 1
    - ``verify``：校驗位:0-None，1-Odd，2-Even,目前常用爲 0
    - ``timeout``：超時時間:1~1000ms，此值需要結合外設搭配設置合理的時間參數
    - ``timeoutTimes``：超時次數:1~10，主要進行超時重發，減少偶發異常提高用戶體驗
    - ``period``：週期性指令時間間隔:1~1000ms，主要用於週期性指令每次下發的時間間隔"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置末端文件傳輸類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleFileType(type)``"
    "描述", "設置末端文件傳輸類型"
    "必選參數", "- ``type``：1-MCU升級文件,2-LUA文件"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置啓用末端LUA執行
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnable(enable)``"
    "描述", "設置啓用末端LUA執行"
    "必選參數", "- ``enable``：0-不啓用；1-啓用"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

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
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取末端LUA執行使能狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableStatus()``"
    "描述", "獲取末端LUA執行使能狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``enable``：0-不啓用；1-啓用"

設置末端LUA末端設備啟用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnableDeviceType(self, forceSensorEnable, gripperEnable, IOEnable, dexhandEnable)``"
    "描述", "設置末端LUA末端設備啟用類型"
    "必選參數", "
    - ``forceSensorEnable``：力感測器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable``：IO設備啟用狀態，0-不啟用；1-啟用
    - ``dexhandEnable``：靈巧手啟用狀態，0-不啟用；1-啟用"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取末端LUA末端設備啟用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDeviceType()``"
    "描述", "獲取末端LUA末端設備啟用類型"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``forceSensorEnable``：力感測器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable``：IO設備啟用狀態，0-不啟用；1-啟用
    - ``dexhandEnable``：靈巧手啟用狀態，0-不啟用；1-啟用"

獲取當前配置的末端設備
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDevice()``"
    "描述", "獲取當前配置的末端設備"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``forceSensorEnable[8]``：力感測器啟用狀態，0-不啟用；1-啟用
    - ``gripperEnable[8]``：夾爪啟用狀態，0-不啟用；1-啟用
    - ``IOEnable[8]``：IO設備啟用狀態，0-不啟用；1-啟用
    - ``dexhandEnable``：靈巧手啟用狀態，0-不啟用；1-啟用"

設置啟用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "設置啟用夾爪動作控制功能"
    "必選參數", "
    - ``id``：夾爪設備編號
    - ``func``：0-夾爪使能；1-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩,12-旋轉夾爪旋轉圈數設置； 13-旋轉夾爪旋轉速度設置； 14-旋轉夾爪旋轉力矩設置； 15-讀旋轉夾爪狀態；16-讀旋轉夾爪初始化狀態；17-讀旋轉夾爪圈數；18-讀旋轉夾爪速度；19-讀旋轉夾爪力矩；20-多軸同步運動設置；21-故障清除指令；22-單軸運行狀態；23-所有軸運行狀態；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取啟用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "獲取啟用夾爪動作控制功能"
    "必選參數", "- ``id``：夾爪設備編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``func``：0-夾爪使能；1-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩,12-旋轉夾爪旋轉圈數設置； 13-旋轉夾爪旋轉速度設置； 14-旋轉夾爪旋轉力矩設置； 15-讀旋轉夾爪狀態；16-讀旋轉夾爪初始化狀態；17-讀旋轉夾爪圈數；18-讀旋轉夾爪速度；19-讀旋轉夾爪力矩；20-多軸同步運動設置；21-故障清除指令；22-單軸運行狀態；23-所有軸運行狀態；"

機器人Ethercat從站文件寫入
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SlaveFileWrite(type,slaveID,fileName)``"
    "描述", "機器人Ethercat從站文件寫入"
    "必選參數", "- ``type``：從站文件類型，1-升級從站文件；2-升級從站配置文件
    - ``slaveID``：從站號
    - ``fileName``：上傳文件名"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

上傳末端Lua開放協議文件
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleLuaUpload(filePath)``"
    "描述", "上傳末端Lua開放協議文件"
    "必選參數", "- ``filePath``：本地lua文件路徑名 .../AXLE_LUA_End_DaHuan.lua"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人Ethercat從站進入boot模式
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysServoBootMode(filePath)``"
    "描述", "機器人Ethercat從站進入boot模式"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人末端LUA文件操作代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua")
    param = [7, 8, 1, 0, 5, 3, 1]  # 對應AxleComParam參數
    robot.SetAxleCommunicationParam(7, 8, 1, 0, 5, 3, 1)
    error,getParam0,getParam1,getParam2,getParam3,getParam4,getParam5,getParam6 = robot.GetAxleCommunicationParam()
    print(f"GetAxleCommunicationParam param is:{getParam0} {getParam1} {getParam2} {getParam3} {getParam4} {getParam5} {getParam6}")
    robot.SetAxleLuaEnable(1)
    error,luaEnableStatus = robot.GetAxleLuaEnableStatus()
    robot.SetAxleLuaEnableDeviceType(0, 1, 0)
    error,forceEnable, gripperEnable, ioEnable = robot.GetAxleLuaEnableDeviceType()
    print(f"GetAxleLuaEnableDeviceType param is:{forceEnable} {gripperEnable} {ioEnable}")
    func = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    robot.SetAxleLuaGripperFunc(1, func)
    error,getFunc = robot.GetAxleLuaGripperFunc(1)
    error,getforceEnable, getgripperEnable, getioEnable = robot.GetAxleLuaEnableDevice()
    print("\ngetforceEnable status:", end=" ")
    for i in range(8):
        print(f"{getforceEnable[i]},", end="")
    print("\ngetgripperEnable status:", end=" ")
    for i in range(8):
        print(f"{getgripperEnable[i]},", end="")
    print("\ngetioEnable status:", end=" ")
    for i in range(8):
        print(f"{getioEnable[i]},", end="")
    print()
    robot.ActGripper(1, 0)
    time.sleep(2)
    robot.ActGripper(1, 1)
    time.sleep(2)
    robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0)
    while True:
        error,pkg = robot.GetRobotRealTimeState()
        print(f"gripper pos is:{pkg.gripper_position}")
        time.sleep(0.1)
    robot.CloseRPC()

    
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

SmartTool按鈕代碼示例
+++++++++++++++++++++++++++++++++++++++++++++

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


設置拖動開啓前負載力檢測
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTorqueDetectionSwitch(flag)``"
    "描述", "設置拖動開啓前負載力檢測"
    "必選參數", "- ``flag``：0-關閉；1-開啓"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光外設打開關閉函數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingLaserOnOff(OnOff, weldId)``"
    "描述", "激光外設打開關閉函數"
    "必選參數", "- ``OnOff``：0-關閉；1-開啓"
    "默認參數", "- ``weldId``：焊縫ID 默認爲0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光跟蹤開始結束函數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingTrackOnOff(OnOff, coordId)``"
    "描述", "激光跟蹤開始結束函數"
    "必選參數", "- ``OnOff``：0-關閉；1-開啓
    - ``coordId``：激光外設工具座標系編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光尋位-固定方向
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSearchStart_xyz(direction, vel, distance, timeout, posSensorNum)``"
    "描述", "激光尋位-固定方向"
    "必選參數", "- ``direction``：0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
    - ``vel``：速度 單位%
    - ``distance``：最大尋位距離 單位mm
    - ``timeout``：尋位超時時間 單位ms
    - ``posSensorNum``：激光標定的工具座標編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光尋位-任意方向
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSearchStart_point(directionPoint, vel, distance, timeout, posSensorNum)``"
    "描述", "激光尋位-任意方向"
    "必選參數", "- ``directionPoint``：尋位輸入的點的xyz左邊,[x,y,z]
    - ``vel``：速度 單位%
    - ``distance``：最大尋位距離 單位mm
    - ``timeout``：尋位超時時間 單位ms
    - ``posSensorNum``：激光標定的工具座標編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光IP配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSensorConfig(ip, port)``"
    "描述", "激光IP配置"
    "必選參數", "- ``ip``：激光外設的ip地址
    - ``port``：激光外設的端口號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光外設採樣週期配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserTrackingSensorSamplePeriod(period)``"
    "描述", "激光外設採樣週期配置"
    "必選參數", "- ``period``：激光外設採樣週期 單位ms"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光外設驅動加載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadPosSensorDriver(type)``"
    "描述", "激光外設驅動加載"
    "必選參數", "- ``type``：激光外設驅動的協議類型 101-睿牛 102-創想 103-全視 104-同舟 105-奧太"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光外設驅動卸載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``UnLoadPosSensorDriver()``"
    "描述", "激光外設驅動卸載"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光焊縫軌跡記錄
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorRecord1(status, delayTime)``"
    "描述", "激光焊縫軌跡記錄"
    "必選參數", "- ``status``：0-停止記錄 1-實時跟蹤  2-開始記錄
    - ``delayTime``：延時時間 單位ms"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光焊縫軌跡復現
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorReplay(delayTime, speed)``"
    "描述", "激光焊縫軌跡復現"
    "必選參數", "- ``delayTime``：延時時間 單位ms
    - ``speed``：速度 單位%"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
激光跟蹤復現
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveLTR()``"
    "描述", "激光跟蹤復現"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

激光焊縫軌跡復現
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LaserSensorRecordandReplay(delayMode, delayTime, delayDisExAxisNum, delayDis, sensitivePara, int trackMode, int triggerMode, double runTime, speed)``"
    "描述", "雷射焊縫軌跡重現"
    "必選參數", "- ``delayMode``：模式 0-延時時間 1-延時距離
    - ``delayTime``：延時時間 單位ms
    - ``delayDisExAxisNum``：擴展軸編號
    - ``delayDis``：延時距離 單位mm
    - ``sensitivePara``：補償靈敏係數
    - ``trackMode``：定點追蹤類型。0-擴展軸非同步運動；1-機器人
    - ``triggerMode``：定點追蹤觸發方式。0-追蹤時長；1-IO
    - ``runTime``：機器人定點追蹤時長(s)
    - ``speed``：速度 單位%"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

運動到焊縫記錄的起點
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserRecordStart(moveType, ovl)``"
    "描述", "運動到焊縫記錄的起點"
    "必選參數", "- ``moveType``：0-PTP 1-LIN
    - ``ovl``：速度 單位%"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

運動到焊縫記錄的終點
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserRecordEnd(moveType, ovl)``"
    "描述", "運動到焊縫記錄的終點"
    "必選參數", "- ``moveType``：0-PTP 1-LIN
    - ``ovl``：速度 單位%"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

運動到激光傳感器尋位點
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToLaserSeamPos(moveFlag, ovl, dataFlag, plateType, trackOffectType, offset)``"
    "描述", "運動到激光傳感器尋位點"
    "必選參數", "- ``moveFlag``：運動類型：0-PTP；1-LIN
    - ``ovl``：速度縮放因子，0-100
    - ``dataFlag``：焊縫緩存數據選擇：0-執行規劃數據；1-執行記錄數據
    - ``plateType``：板材類型：0-波紋板；1-瓦楞板；2-圍欄板；3-油桶；4-波紋甲殼鋼
    - ``trackOffectType``：激光傳感器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-激光傳感器原始數據偏移
    - ``offset``：偏移量"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取激光傳感器尋位點座標信息
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetLaserSeamPos(trackOffectType, offset)``"
    "描述", "獲取激光傳感器尋位點座標信息"
    "必選參數", "- ``trackOffectType``：激光傳感器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-激光傳感器原始數據偏移
    - ``offset``：偏移量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``jPos``：關節位置[°]
    - ``descPos``：笛卡爾位置[mm]
    - ``tool``：工具座標系
    - ``user``：工件座標系
    - ``exaxis``：擴展軸位置[mm]"

激光外設傳感器參數配置及調試代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LaserTrackingSensorConfig("192.168.58.20", 5020)
    robot.LaserTrackingSensorSamplePeriod(20)
    robot.LoadPosSensorDriver(101)
    robot.LaserTrackingLaserOnOff(0, 0)
    time.sleep(3)
    robot.LaserTrackingLaserOnOff(1, 0)
    robot.CloseRPC()

激光軌跡掃描及軌跡復現的代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    i = 0
    while i<10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(2, 10)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 50,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserSensorRecord1(0, 10)
        robot.MoveToLaserRecordStart(1, 30)
        robot.LaserSensorReplay(10, 100)
        robot.MoveLTR()
        robot.LaserSensorRecord1(0, 10)
        i = i+1
    robot.CloseRPC()

激光尋位及實時跟蹤的代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua")
    time.sleep(2)
    robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua")
    robot.UnloadCtrlOpenLUA(0)
    robot.LoadCtrlOpenLUA(0)
    time.sleep(8)
    time.sleep(8)
    i = 0
    while i < 10:
        startjointPos = [56.205, -117.951, 141.872, -118.149, -94.217, -122.176]
        startdescPose = [-97.552, -282.855, 26.675, 174.182, -1.338, -91.707]
        exaxisPos = [0.0] * 4
        offdese = [0.0] * 6
        directionPoint = [0.0] * 3
        robot.MoveL(desc_pos=startdescPose,tool= 1,user= 0,vel= 100,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3)
        robot.LaserTrackingSearchStop()
        robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese)
        robot.LaserTrackingTrackOnOff(1, 3)
        endjointPos = [68.809, -87.100, 121.120, -127.233, -95.038, -109.555]
        enddescPose = [-103.555, -464.234, 13.076, 174.179, -1.344, -91.709]
        robot.MoveL(desc_pos=enddescPose,tool= 1,user= 0,vel= 20,acc= 100,ovl= 100,blendR= -1,exaxis_pos= exaxisPos,search= 0,offset_flag= 0, offset_pos= offdese,overSpeedStrategy= 1,speedPercent= 1)
        robot.LaserTrackingTrackOnOff(0, 3)
        i = i + 1
        print(i)
    robot.CloseRPC()

擴展軸與機器人同步進行激光跟蹤的代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startexaxisPos = [0.0, 0.0, 0.0, 0.0]
    seamexaxisPos = [-10.0, 0.0, 0.0, 0.0]
    endexaxisPos = [-30.0, 0.0, 0.0, 0.0]
    offdese = [0.0] * 6
    seamjointPos = [0.0] * 6
    seamdescPose = [0.0] * 6
    i=0
    while i < 10:
        startjointPos = [58.337, -119.628, 146.037, -116.358, -92.224, -117.654]
        startdescPose = [-53.375, -255.363, 0.919, 178.054, 1.077, -94.026]
        robot.ExtAxisSyncMoveJ(joint_pos=startjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= startexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
        ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2)
        robot.LaserTrackingSearchStop()
        tool = 0
        user = 0
        rnte, seamjointPos, seamdescPose, tool, user, startexaxisPos = robot.GetLaserSeamPos(0, offdese)
        print(f"{seamjointPos[0]},{seamjointPos[1]},{seamjointPos[2]},{seamjointPos[3]},{seamjointPos[4]},{seamjointPos[5]},{seamdescPose[0]},{seamdescPose[1]},{seamdescPose[2]},{seamdescPose[3]},{seamdescPose[4]},{seamdescPose[5]}")
        if ret == 0:
            robot.ExtAxisSyncMoveJ(joint_pos=seamjointPos, tool=1,user= 0,vel= 100,acc= 100, ovl=100,exaxis_pos= seamexaxisPos,blendT= -1,offset_flag= 0,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(1, 2)
            endjointPos = [70.580, -90.918, 126.593, -125.154, -92.162, -105.403]
            enddescPose = [-53.375, -419.020, 0.920, 178.054, 1.076, -94.026]
            robot.ExtAxisSyncMoveL(desc_pos=enddescPose, tool=1,user= 0,vel= 20,acc= 100, ovl=100,blendR= -1,exaxis_pos= endexaxisPos,offset_pos= offdese)
            robot.LaserTrackingTrackOnOff(0, 2)
        i = i+1
        print(i)
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

    "原型", "``FieldBusSlaveWriteDO(DOIndex, writeNum, status)``"
    "描述", "寫入從站DO"
    "必選參數", "- ``DOIndex``：DO編號
    - ``writeNum``：寫入的數量
    - ``status``：寫入的數值，最多寫8個"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

寫入從站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveWriteAO(AOIndex, writeNum, status)``"
    "描述", "寫入從站AO"
    "必選參數", "- ``AOIndex``：AO編號
    - ``writeNum``：寫入的數量
    - ``status``：寫入的數值，最多寫8個"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

讀取從站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadDI(DIIndex, readNum)``"
    "描述", "讀取從站DI"
    "必選參數", "- ``DIIndex``：DI編號
    - ``readNum``：讀取的數量"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``status[8]``：讀取到的數值，最多讀8個"

讀取從站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FieldBusSlaveReadAI(AIIndex, readNum)``"
    "描述", "讀取從站AI"
    "必選參數", "- ``AIIndex``：AI編號
    - ``readNum``：讀取的數量"
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

末端透傳功能打開關閉SDK接口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleGenComEnable(mode)``"
    "描述", "開啟末端通用透傳功能"
    "必選參數", "- ``mode``：使能，0-關閉，1-開啟"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

末端透傳功能非週期數據收發SDK接口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SndRcvAxleGenComCmdData( len_snd, sndBuff, len_rcv)``"
    "描述", "末端發送非週期數據並等待應答"
    "必選參數", "
    - ``len_snd``：發送的長度;
    - ``sndBuff[]``：發送數據;
    - ``len_rcv``：選擇接受的長度;
    - ``rcvBuff[]``：應答的數據;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

基於末端透傳功能倍益康艾灸頭非週期數據通信代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    import time


    def testAxleGenCom(self):

        led_on = [0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79]
        led_off = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        version = [0xAB, 0xBA, 0x11, 0x00, 0x76]
        state = [0xAB, 0xBA, 0x1B, 0x01, 0xAA, 0x2B]
        cycleState = [0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78]
        cnt = 1

        p1Joint = [88.708, -86.178, 140.989, -141.825, -89.162, -49.879]
        p1Desc = [188.007, -377.850, 260.207, 178.715, 2.823, -131.466]
        p2Joint = [112.131, -75.554, 126.989, -139.027, -88.044, -26.477]
        p2Desc = [368.003, -377.848, 260.211, 178.715, 2.823, -131.465]

        exaxisPos = [0, 0, 0, 0]
        offdese = [0, 0, 0, 0, 0, 0]

        #開啟末端透傳功能
        robot.SetAxleGenComEnable(1)
        robot.SetAxleLuaEnable(1)

        while cnt <= 10000:
            #讀取版本號
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(len_snd=5, sndBuff=version, len_rcv=10)
            print(ret)
            print(rcvdata)
            print(f"hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}")
            if ret != 0:
                break
            time.sleep(1)
            # 讀取艾灸頭在位狀態
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, state, 6)
            print(f"state : {rcvdata[4]} ")
            time.sleep(1)
            # 開啟艾灸頭激光
            ret,rcvdata = robot.SndRcvAxleGenComCmdData(6, led_on, 6)
            print(f"led on rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p1Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,
                            offset_flag=0, offset_pos=offdese)
            time.sleep(4)
            # 關閉艾灸頭激光
            ret, rcvdata = robot.SndRcvAxleGenComCmdData(6, led_off, 6)
            print(f"led off rcv data is: {rcvdata[0]}, {rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}")
            robot.MoveJ(joint_pos=p2Joint, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=exaxisPos, blendT=-1,offset_flag=0, offset_pos=offdese)
            time.sleep(1)
            print(f"***********************complate No. {cnt} SDK test*****************************")
            cnt = cnt + 1

        robot.CloseRPC()
        return 0

    testAxleGenCom(robot)
    
下載開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaDownload(fileName, savePath)``"
    "描述", "下載開放協議Lua文件"
    "必選參數", "
    - ``fileName``：開放協議文件名稱“CtrlDev_XXX.lua”;
    - ``savePath``：開放協議保存文件路徑;
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
刪除指定開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OpenLuaDelete(fileName)``"
    "描述", "刪除指定開放協議Lua文件"
    "必選參數", "
    - ``fileName``：要刪除的開放協議lua文件名“CtrlDev_XXX.lua”
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
刪除所有開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AllOpenLuaDelete()``"
    "描述", "刪除所有開放協議Lua文件"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

開放協議lua文件操作SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')


    def TestCtrlOpenLuaOperate(self):
        # 上傳Lua文件到機器人
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua")
        print(f"OpenLuaUpload rtn is {rtn}")
        
        # 從機器人下載Lua文件
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/")
        print(f"OpenLuaDownload rtn is {rtn}")
        
        # 設置控制開放的Lua文件名
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua")
        print(f"SetCtrlOpenLUAName rtn is {rtn}")
        
        # 獲取控制開放的Lua文件名
        rtn, name = robot.GetCtrlOpenLUAName()
        print(f"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}")
        
        # 加載控制開放的Lua
        rtn = robot.LoadCtrlOpenLUA(1)
        print(f"LoadCtrlOpenLUA rtn is {rtn}")
        time.sleep(2)
        
        # 卸載控制開放的Lua
        rtn = robot.UnloadCtrlOpenLUA(1)
        print(f"UnloadCtrlOpenLUA rtn is {rtn}")
        
        # 刪除指定的Lua文件
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua")
        print(f"OpenLuaDelete rtn is {rtn}")
        
        # 刪除所有Lua文件
        rtn = robot.AllOpenLuaDelete()
        print(f"AllOpenLuaDelete rtn is {rtn}")
        
        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)


    # 調用測試函數
    TestCtrlOpenLuaOperate(robot)

控制靈巧手運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDexterousHandsMove(self, idstart, slaveNum, pos, speed, force, max_time)``"
    "描述", "控制靈巧手運動"
    "必選參數", "
    - ``idstart``：起始從站號;
    - ``slaveNum``：數量;
    - ``pos[16]``：位置(-360~360);
    - ``speed[16]``：速度百分比，範圍[0~100];
    - ``force[16]``：力矩百分比，範圍[0~100];
    - ``max_time``：最大等待時間，範圍[0~30000]，單位ms;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
控制靈巧手復位激活
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDexterousHandsAct(self, id, act)``"
    "描述", "控制靈巧手復位激活"
    "必選參數", "
    - ``id``：從站號;
    - ``act``：0-復位 1-激活"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
        
清除靈巧手錯誤
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ClearDexterousHandsError(self)``"
    "描述", "清除靈巧手錯誤"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置啟用靈巧手動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetDexterousHandsFunc(self, id, func)``"
    "描述", "設置啟用靈巧手動作控制功能"
    "必選參數", "
    - ``id``：靈巧手從站編號;
    - ``func``：功能陣列，32個元素
        0-夾持觸發、1-夾爪初始化、2-位置設置、3-速度設置、4-力矩設置、
        6-讀夾爪狀態、7-讀初始化狀態、8-讀故障碼、9-讀位置、10-讀速度、
        11-讀力矩、12-旋轉圈數設置、13-旋轉速度設置、14-旋轉力矩設置、
        15-讀旋轉夾爪狀態、16-讀旋轉初始化狀態、17-讀旋轉圈數、18-讀旋轉速度、
        19-讀旋轉力矩、20-多軸同步運動設置、21-故障清除指令、22-單軸運行狀態、
        23-所有軸運行狀態"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
獲取啟用靈巧手動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDexterousHandsFunc(self, id)``"
    "描述", "獲取啟用靈巧手動作控制功能"
    "必選參數", "
    - ``id``：靈巧手從站編號;
    - ``func``：功能陣列，32個元素
        0-夾持觸發、1-夾爪初始化、2-位置設置、3-速度設置、4-力矩設置、
        6-讀夾爪狀態、7-讀初始化狀態、8-讀故障碼、9-讀位置、10-讀速度、
        11-讀力矩、12-旋轉圈數設置、13-旋轉速度設置、14-旋轉力矩設置、
        15-讀旋轉夾爪狀態、16-讀旋轉初始化狀態、17-讀旋轉圈數、18-讀旋轉速度、
        19-讀旋轉力矩、20-多軸同步運動設置、21-故障清除指令、22-單軸運行狀態、
        23-所有軸運行狀態"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

末端靈巧手配置及運動代碼示例  
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:  
     
    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')

    def main(self):

        id = 1                 
        slaveNum = 4         
        max_time = 8000      
        speed = [0] * 16     
        force = [0] * 16     

        for i in range(16):
            force[i] = 50 if i < 4 else 0

        def set_positions(v1, v2, v3, v4):
            pos = [0.0] * 16
            pos[0] = v1
            pos[1] = v2
            pos[2] = v3
            pos[3] = v4
            return pos

        j1 = [-53.426,-85.916,109.280,-86.236,-96.663,-28.560]
        j2 = [-91.877,-85.917,109.281,-86.236,-96.663,-28.560]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        ret = robot.ClearDexterousHandsError()
        print(f"ClearDexterousHandsError -> {ret}")

        setFunc = [0] * 32
        setFunc[2] = 1   
        setFunc[4] = 1   
        setFunc[9] = 1   
        setFunc[10] = 1  
        setFunc[11] = 1  
        setFunc[22] = 1  

        ret = robot.SetDexterousHandsFunc(id, setFunc)
        print(f"SetDexterousHandsFunc(使能+初始化+位置/速度/力矩功能啟用) -> {ret}")

        ret, getFunc = robot.GetDexterousHandsFunc(id)
        print(f"GetDexterousHandsFunc -> {ret}")
        if ret == 0:
            print("GetDexterousHandsFunc :")
            for i in range(len(getFunc)):
                print(f"  [{i}]={getFunc[i]}", end="")
                if (i + 1) % 8 == 0:
                    print()  
                elif i < len(getFunc) - 1:
                    print(", ", end="")
            if len(getFunc) % 8 != 0:

        ret = robot.SetDexterousHandsAct(id, 1)
        print(f"SetDexterousHandsAct() -> {ret}")
        if ret != 0:
            return
            pos = set_positions(20, 20, 20, 20)
        ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
        print(f"ret: {ret}")
        time.sleep(5)

        for iteration in range(1, 11):
            robot.MoveJ(joint_pos=j1, tool=1, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

            pos = set_positions(10, 10, 10, 10)
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
            time.sleep(1)

            robot.MoveJ(joint_pos=j2, tool=1, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

            pos = set_positions(50, 50, 50, 50)
            ret = robot.SetDexterousHandsMove(id, slaveNum, pos, speed, force, max_time)
            time.sleep(1)

    main(robot)