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
    "描述", "獲取夾爪運動狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``[fault,status]``：夾爪運動狀態，fault:0-無錯誤，1-有錯誤；status:0-運動未完成，1-運動完成"

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
                    - ``speedRadio``: 速度比  針對傳送帶跟蹤抓取速度範圍爲（1-100）  跟蹤運動、TPD跟蹤設置爲1
    - ``followType``：跟蹤運動類型，0-跟蹤運動；1-追檢運動"
    "默認參數", "- ``startDis``：追檢抓取需要設置， 跟蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 默認值0
    - ``endDis``：追檢抓取需要設置，跟蹤終止距離， 單位mm， 默認值100"
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

設置末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaEnableDeviceType(forceSensorEnable, gripperEnable, IOEnable)``"
    "描述", "設置末端LUA末端設備啓用類型"
    "必選參數", "- ``forceSensorEnable``：力傳感器啓用狀態，0-不啓用；1-啓用
    - ``gripperEnable``：夾爪啓用狀態，0-不啓用；1-啓用
    - ``IOEnable``：IO設備啓用狀態，0-不啓用；1-啓用"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaEnableDeviceType()``"
    "描述", "獲取末端LUA末端設備啓用類型"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``forceSensorEnable``：力傳感器啓用狀態，0-不啓用；1-啓用
    - ``gripperEnable``：夾爪啓用狀態，0-不啓用；1-啓用
    - ``IOEnable``：IO設備啓用狀態，0-不啓用；1-啓用"

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
    - ``forceSensorEnable[8]``：力傳感器啓用狀態，0-不啓用；1-啓用
    - ``gripperEnable[8]``：夾爪啓用狀態，0-不啓用；1-啓用
    - ``IOEnable[8]``：IO設備啓用狀態，0-不啓用；1-啓用"

設置啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "設置啓用夾爪動作控制功能"
    "必選參數", "- ``id``：夾爪設備編號
    - ``func``：0-夾爪使能；1-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩,12-15預留"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "獲取啓用夾爪動作控制功能"
    "必選參數", "- ``id``：夾爪設備編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``func``：0-夾爪使能；1-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩,12-15預留"

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