機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設定軌跡記錄參數
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDParam(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "設定軌跡記錄參數"
    "必選參數", "- ``name``：軌跡名；
    - ``period_ms``：採樣週期，固定值，2ms 或 4ms 或 8ms;"
    "默認參數", "- ``type``：資料類型，1-關節位置；
    - ``di_choose``：DI 選擇,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不選擇，1-選擇 默認0;
    - ``do_choose``：DO 選擇,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不選擇，1-選擇 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    type = 1  # 資料類型，1-關節位置
    name = 'tpd2023'  # 軌跡名
    period = 4  #採樣週期，2ms或4ms或8ms
    di = 0 # di輸入配置
    do = 0 # do輸出配置
    ret = robot.SetTPDParam(name, period, di_choose=di)    #配置TPD參數
    print("配置TPD參數錯誤碼", ret)
    robot.Mode(1)  # 機器人切入自動運作模式
    time.sleep(1)  
    robot.DragTeachSwitch(1)  #機器人切入拖曳示教模式
    ret = robot.GetActualTCPPose()
    print("取得當前工具位姿", ret)
    time.sleep(1)
    ret = robot.SetTPDStart(name, period, do_choose=do)   # 開始記錄示教軌跡
    print("開始記錄示教軌跡錯誤碼", ret)
    time.sleep(15)
    ret = robot.SetWebTPDStop()  # 停止記錄示教軌跡
    print("停止記錄示教軌跡錯誤碼", ret)
    robot.DragTeachSwitch(0)  #機器人切入非拖動示教模式
    # robot.SetTPDDelete('tpd2023')   # 删除TPD軌跡

開始軌跡記錄
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDStart(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "開始軌跡記錄"
    "必選參數", "- ``name``：軌跡名；
    - ``period_ms``：採樣週期，固定值，2ms或4ms或8ms；"
    "默認參數", "- ``type``：資料類型，1-關節位置 默認1;
    - ``di_choose``：DI 選擇,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不選擇，1-選擇 默認0;
    - ``do_choose``：DO 選擇,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不選擇，1-選擇 默認0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

停止軌跡記錄
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWebTPDStop()``"
    "描述", "停止軌跡記錄"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

刪除軌跡記錄
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDDelete(name)``"
    "描述", "刪除軌跡記錄"
    "必選參數", "- ``name``:軌跡名"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

軌跡預載
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTPD(name)``"
    "描述", "軌跡預載"
    "必選參數", "- ``name``:軌跡名"
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
    # P1=[-321.821, 125.694, 282.556, 174.106, -15.599, 152.669]
    name = 'tpd2023'   #軌跡名
    blend = 1   #是否平滑，1-平滑，0-不平滑
    ovl = 100.0   #速度縮放
    ret = robot.LoadTPD(name)  #軌跡預載
    print("軌跡預載錯誤碼",ret)
    ret,P1 = robot.GetTPDStartPose(name)   #取得軌跡起始位姿
    print ("取得軌跡起始位姿錯誤碼",ret,"起始位姿",P1)
    ret = robot.MoveL(P1,0,0)       #運動到起始點
    print("運動到起始點錯誤碼",ret)
    time.sleep(10)
    ret = robot.MoveTPD(name, blend, ovl)  #軌跡復現
    print("軌跡復現錯誤碼",ret)

取得軌跡起始位姿
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTPDStartPose(name)``"
    "描述", "取得軌跡起始位姿"
    "必選參數", "- ``name``:軌跡名"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：軌跡起始位姿"

軌跡復現
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTPD(name,blend,ovl)``"
    "描述", "軌跡復現"
    "必選參數", "- ``name``:軌跡名
    - ``blend``：是否平滑，0-不平滑，1-平滑
    - ``ovl``：速度縮放因子，範圍[0~100]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

軌跡預處理
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryJ(name,ovl,opt=1)``"
    "描述", "軌跡預處理"
    "必選參數", "- ``name``:軌跡名,如：/fruser/traj/trajHelix_aima_1.txt;
    - ``ovl``：速度縮放百分比，範圍[0~100];"
    "默認參數", "- ``opt``：1-控制點，預設為1"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

軌跡復現
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryJ()``"
    "描述", "軌跡復現"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得軌跡起始位姿
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryStartPose(name)``"
    "描述", "取得軌跡起始位姿"
    "必選參數", "``name``:軌跡名"
    "默認參數", "無"       
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：軌跡起始位姿"

取得軌跡點編號
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryPointNum()``"
    "描述", "取得軌跡點編號"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``pnum``：軌跡點編號"

設定軌跡運行中的速度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJSpeed(ovl)``"
    "描述", "設定軌跡運行中的速度"
    "必選參數", "``ovl``:速度縮放百分比，範圍[0~100]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡运行中的力和扭矩
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceTorque(ft)``"
    "描述", "設定軌跡运行中的力和扭矩"
    "必選參數", "``ft=[fx,fy,fz,tx,ty,tz]``:單位N和Nm"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運行中的沿x方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fx)``"
    "描述", "設定軌跡運行中的沿x方向的力"
    "必選參數", "``ft``:沿x方向的力，單位N"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運行中的沿y方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fy)``"
    "描述", "設定軌跡運行中的沿y方向的力"
    "必選參數", "``fy``:沿y方向的力，單位N"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運行中的沿z方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fz)``"
    "描述", "設定軌跡運行中的沿z方向的力"
    "必選參數", "``fz``:沿z方向的力，單位N"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運轉中的繞x軸的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tx)``"
    "描述", "設定軌跡運轉中的繞x軸的扭矩"
    "必選參數", "``tx``:繞x軸的扭矩，單位Nm"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運轉中的繞y軸的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(ty)``"
    "描述", "設定軌跡運轉中的繞y軸的扭矩"
    "必選參數", "``ty``:繞y軸的扭矩，單位Nm"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定軌跡運轉中的繞z軸的扭矩
+++++++++++++++++++++++++++
.. versionchanged:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tz)``"
    "描述", "設定軌跡運轉中的繞z軸的扭矩"
    "必选参数", "- ``tz``:繞z軸的扭矩，單位Nm"
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
    name = "/fruser/traj/trajHelix_aima_1.txt"   #軌跡名
    blend = 1   #是否平滑，1-平滑，0-不平滑
    ovl = 50.0   #速度縮放
    ft =[0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    ret = robot.LoadTrajectoryJ(name,ovl)  #軌跡預載
    print("軌跡預載錯誤碼",ret)
    ret,P1 = robot.GetTrajectoryStartPose(name)   #取得軌跡起始位姿
    print ("取得軌跡起始位姿錯誤碼",ret,"起始位姿",P1)
    ret = robot.MoveL(P1,1,0)       #運動到起始點
    print("運動到起始點錯誤碼",ret)
    ret = robot.GetTrajectoryPointNum()       #取得軌跡點編號
    print("取得軌跡點編號錯誤碼",ret)
    time.sleep(10)
    ret = robot.MoveTrajectoryJ()  #軌跡復現
    print("軌跡復現錯誤碼",ret)
    time.sleep(10)
    ret = robot.SetTrajectoryJSpeed(ovl)  #設定軌跡運行中的速度
    print("設定軌跡運行中的速度錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceTorque(ft)  #設定軌跡运行中的力和扭矩
    print("設定軌跡运行中的力和扭矩錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFx(0) #設定軌跡運行中的沿x方向的力
    print("設定軌跡運行中的沿x方向的力錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFy(0) #設定軌跡運行中的沿y方向的力
    print("設定軌跡運行中的沿y方向的力錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFz(0) #設定軌跡運行中的沿z方向的力
    print("設定軌跡運行中的沿z方向的力錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTx(0) #設定軌跡運轉中的繞x軸的扭矩
    print("設定軌跡運轉中的繞x軸的扭矩錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTy(0) #設定軌跡運轉中的繞y軸的扭矩
    print("設定軌跡運轉中的繞y軸的扭矩錯誤碼",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTz(0) #設定軌跡運轉中的繞z軸的扭矩
    print("設定軌跡運轉中的繞z軸的扭矩錯誤碼",ret)
    time.sleep(1)

上傳軌跡J文件
+++++++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJUpLoad(filePath)``"
    "描述", "上傳軌跡J文件"
    "必選參數", "- ``filePath``:上傳軌跡檔案的全路徑名，C://test/testJ.txt"
    "預設參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

刪除軌跡J文件
+++++++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJDelete(filePath)``"
    "描述", "刪除軌跡J文件"
    "必選參數", "- ``filePath``:刪除軌跡檔案的全路徑名，C://test/testJ.txt"
    "預設參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.LoggerInit()
    robot.SetLoggerLevel(lvl=1)
    
    retval = robot.TrajectoryJDelete("testA.txt")
    print("TrajectoryJDelete return ", retval)
    robot.TrajectoryJUpLoad("D://zUP/testA.txt")

    traj_file_name = "/fruser/traj/testA.txt"
    retval = robot.LoadTrajectoryJ(traj_file_name, 100, 1)
    print("LoadTrajectoryJ return ", retval)

    retval,traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print("GetTrajectoryStartPose return ", retval)
    print("軌跡起始位姿:", traj_start_pose[0], traj_start_pose[1], traj_start_pose[2], traj_start_pose[3], traj_start_pose[4], traj_start_pose[5])

    robot.SetSpeed(20)
    robot.MoveCart(traj_start_pose, 1, 0)

    time.sleep(5)

    retval,traj_num = robot.GetTrajectoryPointNum()
    print("GetTrajectoryPointNum return ", retval)
    print("軌跡點編號: ", traj_num)

    retval = robot.MoveTrajectoryJ()
    print("MoveTrajectoryJ return ", retval)