機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

獲取當前關節位置(角度)
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosDegree(flag=1)``"
    "描述", "獲取關節當前位置(角度)"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞，默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：當前關節位置(角度)"

獲取當前關節位置(弧度)
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosRadian(flag=1)``"
    "描述", "獲取關節當前位置(弧度)"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：當前關節位置(弧度)"

獲取關節反饋速度-deg/s
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointSpeedsDegree(flag=1)``"
    "描述", "獲取關節反饋速度-deg/s"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``speed=[j1,j2,j3,j4,j5,j6]``：關節反饋速度-deg/s"

獲取關節反饋加速度-deg/s^2
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointAccDegree(flag=1)``"
    "描述", "獲取關節反饋加速度-deg/s^2"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``acc=[j1,j2,j3,j4,j5,j6]``：關節反饋加速度-deg/s^2"

獲取TCP指令合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPCompositeSpeed(flag=1)``"
    "描述", "獲取TCP指令合速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-線性合速度 ori_speed-姿態合速度"

獲取TCP反饋合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPCompositeSpeed(flag=1)``"
    "描述", "獲取TCP反饋合速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-線性合速度 ori_speed-姿態合速度"

獲取TCP指令速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPSpeed(flag=1)``"
    "描述", "獲取TCP指令速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP指令速度，mm/s"

獲取TCP反饋速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPSpeed(flag=1)``"
    "描述", "獲取TCP反饋速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP反饋速度"

獲取當前工具位姿
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPPose(flag=1)``"
    "描述", "獲取當前工具位姿"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：當前工具位姿"

獲取當前工具座標系編號
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPNum(flag=1)``"
    "描述", "獲取當前工具座標系編號"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tool_id``:工具座標系編號"

獲取當前工件座標系編號
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualWObjNum(flag=1)``"
    "描述", "獲取當前工件座標系編號"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``wobj_id``:工件座標系編號"

獲取當前末端法蘭位姿
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualToolFlangePose(flag=1)``"
    "描述", "獲取當前末端法蘭位姿"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``flange_pose=[x,y,z,rx,ry,rz]``：當前末端法蘭位姿"

獲取當前關節轉矩
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointTorques(flag=1)``"
    "描述", "獲取當前關節轉矩"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``torques=[j1,j2,j3,j4,j5,j6]``：關節扭矩"

獲取系統時間
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSystemClock()``"
    "描述", "獲取系統時間"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``t_ms``: 系統時間，單位 [ms]"

查詢機器人運動是否完成
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotMotionDone()``"
    "描述", "查詢機器人運動是否完成"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``: 機器人運動狀態，0-未完成，1-完成"

查詢機器人運動隊列緩存長度
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetMotionQueueLength()``"
    "描述", "查詢機器人運動隊列緩存長度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``len``：緩存長度"

獲取機器人急停狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotEmergencyStopState()``"
    "描述", "獲取機器人急停狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``：急停狀態，0-非急停，1-急停"

獲取SDK與機器人的通訊狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKComState()``"
    "描述", "獲取SDK與機器人的通訊狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``state``：通訊狀態，0-通訊正常，1-通訊異常"

獲取安全停止信號
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSafetyStopState()``"
    "描述", "獲取安全停止信號"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[si0_state,si1_state]``：si0_state 安全停止信號SI0，0-無效，1-有效 si1_state 安全停止信號SI1，0-無效，1-有效"

獲取關節驅動器當前溫度(℃)
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTemperature()``"
    "描述", "獲取關節驅動器當前溫度(℃)"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``data=[t1,t2,t3,t4,t5,t6]``：各關節當前溫度"

獲取關節驅動器當前扭矩(Nm)
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTorque()``"
    "描述", "獲取關節驅動器當前扭矩(Nm)"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``data=[j1,j2,j3,j4,j5,j6]``：關節扭矩 [fx,fy,fz,tx,ty,tz]"

獲取機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealTimeState()``"
    "描述", "獲取機器人狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``robot_state_pkg``：機器人狀態結構體"

機器人狀態查詢代碼示例
++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error,[yangle, zangle] = robot.GetRobotInstallAngle()
    print(f"yangle:{yangle},zangle:{zangle}")
    error,j_deg = robot.GetActualJointPosDegree(0)
    print(f"joint pos deg:{j_deg[0]},{j_deg[1]},{j_deg[2]},{j_deg[3]},{j_deg[4]},{j_deg[5]}")
    error,jointSpeed = robot.GetActualJointSpeedsDegree(0)
    print(f"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}")
    error,jointAcc = robot.GetActualJointAccDegree(0)
    print(f"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}")
    error,[tcp_speed, ori_speed] = robot.GetTargetTCPCompositeSpeed(0)
    print(f"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,[tcp_speed, ori_speed] = robot.GetActualTCPCompositeSpeed(0)
    print(f"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}")
    error,targetSpeed = robot.GetTargetTCPSpeed(0)
    print(f"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}")
    error,actualSpeed = robot.GetActualTCPSpeed(0)
    print(f"GetActualTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}")
    error,tcp = robot.GetActualTCPPose(0)
    print(f"tcp pose:{tcp[0]},{tcp[1]},{tcp[2]},{tcp[3]},{tcp[4]},{tcp[5]}")
    error,flange = robot.GetActualToolFlangePose(0)
    print(f"flange pose:{flange[0]},{flange[1]},{flange[2]},{flange[3]},{flange[4]},{flange[5]}")
    error,id = robot.GetActualTCPNum(0)
    print(f"tcp num:{id}")
    error,id = robot.GetActualWObjNum(0)
    print(f"wobj num:{id}")
    error,jtorque = robot.GetJointTorques(0)
    print(f"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}")
    error,t_ms = robot.GetSystemClock()
    print(f"system clock:{t_ms}")
    error,config = robot.GetRobotCurJointsConfig()
    print(f"joint config:{config}")
    error,motionDone = robot.GetRobotMotionDone()
    print(f"GetRobotMotionDone:{motionDone}")
    error,len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength:{len}")
    error,emergState = robot.GetRobotEmergencyStopState()
    print(f"GetRobotEmergencyStopState:{emergState}")
    error,comstate = robot.GetSDKComState()
    print(f"GetSDKComState:{comstate}")
    error,[si0_state, si1_state] = robot.GetSafetyStopState()
    print(f"GetSafetyStopState:{si0_state} {si1_state}")
    error,temp = robot.GetJointDriverTemperature()
    print(f"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}")
    error,torque = robot.GetJointDriverTorque()
    print(f"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}")
    error,pkg = robot.GetRobotRealTimeState()
    robot.CloseRPC()

逆運動學求解
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKin(type,desc_pos,config=-1)``"
    "描述", "逆運動學，笛卡爾位姿求解關節位置 "
    "必選參數", "- ``type``:0-絕對位姿(基座標系)，1-相對位姿（基座標系），2-相對位姿（工具座標系）
    - ``desc_pose``:[x,y,z,rx,ry,rz],工具位姿，單位[mm][°]"
    "默認參數", "- ``config``:關節配置，[-1]-參考當前關節位置求解，[0~7]-依據關節配置求解 默認-1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆運動學解，笛卡爾位姿求解關節位置"

逆運動學求解-指定參考位置
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinRef(type,desc_pos,joint_pos_ref)``"
    "描述", "逆運動學，工具位姿求解關節位置，參考指定關節位置求解"
    "必選參數", "- ``type``:0-絕對位姿(基座標系)，1-相對位姿（基座標系），2-相對位姿（工具座標系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，單位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，關節參考位置，單位[°]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆運動學解，工具位姿求解關節位置"

逆運動學求解-是否有解
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinHasSolution(type,desc_pos,joint_pos_ref)``"
    "描述", "逆運動學，工具位姿求解關節位置 是否有解"
    "必選參數", "- ``type``:0-絕對位姿(基座標系)，1-相對位姿（基座標系），2-相對位姿（工具座標系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，單位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，關節參考位置，單位[°]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``result``:“True”-有解，“False”-無解"

正運動學求解
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForwardKin(joint_pos)``"
    "描述", "正運動學，關節位置求解工具位姿"
    "必選參數", "- ``joint_pos``:[j1,j2,j3,j4,j5,j6]:關節位置，單位[°]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``desc_pos=[x,y,z,rx,ry,rz]``：正運動學解，關節位置求解工具位姿"

機器人正逆運動學計算代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    error, inverseRtn = robot.GetInverseKin(0, desc_pos=desc_pos1, config=-1)
    print(f"dcs1 GetInverseKin rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, inverseRtn = robot.GetInverseKinRef(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef rtn is {inverseRtn[0]}, {inverseRtn[1]}, {inverseRtn[2]}, "
          f"{inverseRtn[3]}, {inverseRtn[4]}, {inverseRtn[5]}")
    error, hasResult = robot.GetInverseKinHasSolution(0, desc_pos=desc_pos1, joint_pos_ref=j1)
    print(f"dcs1 GetInverseKinRef result {hasResult}")
    error, forwordResult = robot.GetForwardKin(j1)
    print(f"jpos1 forwordResult rtn is {forwordResult[0]}, {forwordResult[1]}, {forwordResult[2]}, "
          f"{forwordResult[3]}, {forwordResult[4]}, {forwordResult[5]}")
    robot.CloseRPC()

查詢機器人示教管理點位數據
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotTeachingPoint(name)``"
    "描述", "查詢機器人示教管理點位數據"
    "必選參數", "``name``：點位名"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4]``：點位數據"

獲取DH補償參數
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDHCompensation()``"
    "描述", "獲取DH補償參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``dhCompensation=[cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]``：機器人DH參數補償值(mm)"

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

查詢機器人示教管理點位數據代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    name = "P1"
    rtn, data = robot.GetRobotTeachingPoint(name)
    print(f"{rtn} name is: {name}")
    for i in range(20):
        print(f"data is: {data[i]}")
    rtn,que_len = robot.GetMotionQueueLength()
    print(f"GetMotionQueueLength rtn is: {rtn}, queue length is: {que_len}")
    retval,dh = robot.GetDHCompensation()
    print(f"retval is: {retval}")
    print(f"dh is: {dh[0]} {dh[1]} {dh[2]} {dh[3]} {dh[4]} {dh[5]}")
    error,sn = robot.GetRobotSN()
    print(f"robot SN is {sn[0]}")
    robot.CloseRPC()

根據編號獲取工具座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetToolCoordWithID(id)``"
    "描述", "根據編號獲取工具座標系"
    "必選參數", "- ``id``：工具座標系編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

根據編號獲取工件座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWObjCoordWithID(id)``"
    "描述", "根據編號獲取工件座標系"
    "必選參數", "- ``id``：工件座標系編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

根據編號獲取外部工具座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExToolCoordWithID(id)``"
    "描述", "根據編號獲取外部工具座標系"
    "必選參數", "- ``id``：外部工具座標系編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

根據編號獲取擴展軸座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetExAxisCoordWithID(id)``"
    "描述", "根據編號獲取擴展軸座標系"
    "必選參數", "- ``id``：擴展軸座標系編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

根據編號獲取負載質量及質心
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayloadWithID(id)``"
    "描述", "根據編號獲取負載質量及質心"
    "必選參數", "- ``id``：擴展軸座標系編號"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weight``：負載質量
    - ``cog``：負載質心"

獲取當前工具座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurToolCoord()``"
    "描述", "獲取當前工具座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

獲取當前工件座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurWObjCoord()``"
    "描述", "獲取當前工件座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

獲取當前外部工具座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurExToolCoord()``"
    "描述", "獲取當前外部工具座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

獲取當前擴展軸座標系
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetCurExAxisCoord()``"
    "描述", "獲取當前擴展軸座標系"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``coord``：座標系數值"

獲取機器人座標系及負載代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    id = 1
    toolCoord = [0.0] * 6
    extoolCoord = [0.0] * 6
    wobjCoord = [0.0] * 6
    exAxisCoord = [0.0] * 6
    for i in range(100):
        print(f"當前ID爲:{id}")
        coordSet0 = [0.0] * 6
        coordSet = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        etcp = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
        etool = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
        cog = [1.0, 2.0, 3.0]
        if i % 2 == 0:
            robot.SetToolCoord(id, coordSet, 0, 0, 1, 0)
            time.sleep(0.1)
            robot.SetWObjCoord(id, coordSet, 0)
            time.sleep(0.1)
            robot.ExtAxisActiveECoordSys(id, 1, coordSet, 1)
            time.sleep(0.1)
            rtn = robot.SetExToolCoord(id, etcp, etool)
            time.sleep(0.1)
            rtn = robot.SetLoadWeight(id, 1.5)
            time.sleep(0.1)
            rtn = robot.SetLoadCoord(cog[0],cog[1],cog[2],id)
            time.sleep(0.1)
        else:
            robot.SetToolCoord(id, coordSet0, 0, 0, 1, 0)
            time.sleep(0.1)
            robot.SetWObjCoord(id, coordSet0, 0)
            time.sleep(0.1)
            robot.ExtAxisActiveECoordSys(id, 1, coordSet0, 1)
            time.sleep(0.1)
            rtn = robot.SetExToolCoord(id, coordSet0, coordSet0)
            time.sleep(0.1)
            rtn = robot.SetLoadWeight(id, 0)
            time.sleep(0.1)
            rtn = robot.SetLoadCoord(coordSet0[0],coordSet0[1],coordSet0[2] , id)
            time.sleep(0.1)
        rtn, toolCoord = robot.GetCurToolCoord()
        print(f"GetToolCoord {toolCoord[0]},{toolCoord[1]},{toolCoord[2]},{toolCoord[3]},{toolCoord[4]},{toolCoord[5]}")
        rtn, wobjCoord = robot.GetCurWObjCoord()
        print(f"GetWObjCoord {wobjCoord[0]},{wobjCoord[1]},{wobjCoord[2]},{wobjCoord[3]},{wobjCoord[4]},{wobjCoord[5]}")
        rtn, extoolCoord = robot.GetCurExToolCoord()
        print(f"GetExToolCoord {extoolCoord[0]},{extoolCoord[1]},{extoolCoord[2]},{extoolCoord[3]},{extoolCoord[4]},{extoolCoord[5]}")
        rtn, exAxisCoord = robot.GetCurExAxisCoord()
        print(f"GetExAxisCoord {exAxisCoord[0]},{exAxisCoord[1]},{exAxisCoord[2]},{exAxisCoord[3]},{exAxisCoord[4]},{exAxisCoord[5]}")
        weight = 0.0
        getCog = [0.0] * 3
        rtn, weight = robot.GetTargetPayload(0)
        rtn, getCog = robot.GetTargetPayloadCog(0)
        print(f"GetTargetPayload {weight},{getCog[0]},{getCog[1]},{getCog[2]}")
        
        rtn, toolCoord = robot.GetToolCoordWithID(id)
        print(f"GetToolCoordWithID {id},{toolCoord[0]},{toolCoord[1]},{toolCoord[2]},{toolCoord[3]},{toolCoord[4]},{toolCoord[5]}")
        rtn, wobjCoord = robot.GetWObjCoordWithID(id)
        print(f"GetWObjCoordWithID {id},{wobjCoord[0]},{wobjCoord[1]},{wobjCoord[2]},{wobjCoord[3]},{wobjCoord[4]},{wobjCoord[5]}")
        rtn, extoolCoord = robot.GetExToolCoordWithID(id)
        print(f"GetExToolCoordWithID {id},{extoolCoord[0]},{extoolCoord[1]},{extoolCoord[2]},{extoolCoord[3]},{extoolCoord[4]},{extoolCoord[5]}")
        rtn, exAxisCoord = robot.GetExAxisCoordWithID(id)
        print(f"GetExAxisCoordWithID {id},{exAxisCoord[0]},{exAxisCoord[1]},{exAxisCoord[2]},{exAxisCoord[3]},{exAxisCoord[4]},{exAxisCoord[5]}")
        weight = 0.0
        getCog = [0.0] * 3
        rtn, weight, getCog = robot.GetTargetPayloadWithID(id)
        print(f"GetTargetPayloadWithID {id},{weight},{getCog[0]},{getCog[1]},{getCog[2]}")
        time.sleep(0.5)
        print(f"times {i}")