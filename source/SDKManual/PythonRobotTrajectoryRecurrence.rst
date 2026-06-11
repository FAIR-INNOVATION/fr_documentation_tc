機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設置軌跡記錄參數
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDParam(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "設置軌跡記錄參數"
    "必選參數", "- ``name``：軌跡名；
    - ``period_ms``：採樣週期，固定值，2ms 或 4ms 或 8ms;"
    "默認參數", "- ``type``：數據類型，1-關節位置；
    - ``di_choose``：DI 選擇,bit0~bit7 對應控制箱 DI0~DI7，bit8~bit9 對應末端DI0~DI1，0-不選擇，1-選擇 默認0;
    - ``do_choose``：DO 選擇,bit0~bit7 對應控制箱 DO0~DO7，bit8~bit9 對應末端 DO0~DO1，0-不選擇，1-選擇 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

開始軌跡記錄
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDStart(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "開始軌跡記錄"
    "必選參數", "- ``name``：軌跡名；
    - ``period_ms``：採樣週期，固定值，2ms或4ms或8ms；"
    "默認參數", "- ``type``：數數據類型，1-關節位置 默認1;
    - ``di_choose``：DI 選擇,bit0~bit7 對應控制箱 DI0~DI7，bit8~bit9 對應末端DI0~DI1，0-不選擇，1-選擇 默認0;
    - ``do_choose``：DO 選擇,bit0~bit7 對應控制箱 DO0~DO7，bit8~bit9 對應末端 DO0~DO1，0-不選擇，1-選擇 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

停止軌跡記錄
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWebTPDStop()``"
    "描述", "停止軌跡記錄"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

刪除軌跡記錄
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDDelete(name)``"
    "描述", "刪除軌跡記錄"
    "必選參數", "- ``name``:軌跡名"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

代碼示例
+++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    robot.SetTPDParam(name, period_ms)
    robot.Mode(1)
    time.sleep(1)
    robot.DragTeachSwitch(1)
    robot.SetTPDStart(name, period_ms)
    print("SetTPDStart")
    time.sleep(10)
    robot.SetWebTPDStop()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

軌跡預加載
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTPD(name)``"
    "描述", "軌跡預加載"
    "必選參數", "- ``name``:軌跡名"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

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
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取軌跡起始位姿
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTPDStartPose(name)``"
    "描述", "獲取軌跡起始位姿"
    "必選參數", "- ``name``:軌跡名"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：軌跡起始位姿"

機器人TPD軌跡記錄代碼示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    type = 1
    name = "tpd2025"
    period_ms = 4
    di_choose = 0
    do_choose = 0
    ovl = 100.0
    blend = 0
    rtn = robot.LoadTPD(name)
    print(f"LoadTPD rtn is: {rtn}")
    error,start_pose = robot.GetTPDStartPose(name)
    print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. "
          f"rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
    robot.MoveCart(start_pose, 0, 0, 100, 100)
    time.sleep(1)
    rtn = robot.MoveTPD(name, blend, ovl)
    print(f"MoveTPD rtn is: {rtn}")
    time.sleep(5)
    robot.SetTPDDelete(name)
    robot.CloseRPC()

軌跡預處理
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryJ(name,ovl,opt=1)``"
    "描述", "軌跡預處理"
    "必選參數", "
    - ``name``:軌跡名 如trajHelix_aima_1.txt,同時相容全路徑檔案名，如/fruser/traj/trajHelix_aima_1.txt;
    - ``ovl``：速度縮放百分比，範圍[0~100];"
    "默認參數", "- ``opt``：1-控制點，默認爲1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

軌跡復現
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryJ()``"
    "描述", "軌跡復現"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取軌跡起始位姿
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryStartPose(name)``"
    "描述", "獲取軌跡起始位姿"
    "必選參數", "``name``:軌跡名"
    "默認參數", "無"       
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：軌跡起始位姿"

獲取軌跡點編號
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryPointNum()``"
    "描述", "獲取軌跡點編號"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``pnum``：軌跡點編號"

設置軌跡運行中的速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJSpeed(ovl,mode)``"
    "描述", "設置軌跡運行中的速度"
    "必選參數", "
    - ``ovl``:速度縮放百分比，範圍[0~100]
    - ``mode``:0-降速模式；1-直接切換"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的速度代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')


    def TestSetTrajectoryJSpeed(self):
        # 上傳軌跡文件
        rtn = robot.TrajectoryJUpLoad("C://Users/lenovo/Desktop/trajHelix_aima_1.txt")
        print(f"Upload TrajectoryJ A {rtn}")

        traj_file_name = "trajHelix_aima_1.txt"
        # 加載軌跡文件，參數：文件名，速度百分比，是否循環（1:循環）
        rtn = robot.LoadTrajectoryJ(name=traj_file_name, ovl=100, opt=1)
        print(f"LoadTrajectoryJ {traj_file_name}, rtn is: {rtn}")

        # 獲取軌跡起始點位姿
        rtn, traj_start_pose = robot.GetTrajectoryStartPose(name=traj_file_name)
        print(f"GetTrajectoryStartPose is: {rtn}")
        print(
            f"desc_pos:{traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")

        time.sleep(1)

        # 設置基礎速度並移動到軌跡起始點
        robot.SetSpeed(50)
        robot.MoveCart(desc_pos=traj_start_pose, tool=0, user=0, vel=100, acc=100, ovl=100, blendT=-1, config=-1)

        # 獲取軌跡點數
        rtn, traj_num = robot.GetTrajectoryPointNum()
        print(f"GetTrajectoryStartPose rtn is: {rtn}, traj num is: {traj_num}")

        # 開始執行軌跡運動
        rtn = robot.MoveTrajectoryJ()
        print(f"MoveTrajectoryJ rtn is: {rtn}")

        time.sleep(1)

        # 獲取機器人即時狀態
        trajspeedMode = 0
        while True:
            rtn, pkg = robot.GetRobotRealTimeState()
            if pkg.motion_done != 0:
                break

            # 設置軌跡速度為10%
            rtn = robot.SetTrajectoryJSpeed(ovl=10.0, mode=trajspeedMode)
            print(f"SetTrajectoryJSpeed is: {rtn}")

            time.sleep(1)

            # 設置軌跡速度為80%
            rtn = robot.SetTrajectoryJSpeed(ovl=80.0, mode=trajspeedMode)
            print(f"SetTrajectoryJSpeed is: {rtn}")

            time.sleep(1)

        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)


    # 調用測試函數
    TestSetTrajectoryJSpeed(robot)

設置軌跡運行中的力和扭矩
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceTorque(ft)``"
    "描述", "設置軌跡運行中的力和扭矩"
    "必選參數", "``ft=[fx,fy,fz,tx,ty,tz]``:單位N和Nm"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的沿x方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fx)``"
    "描述", "設置軌跡運行中的沿x方向的力"
    "必選參數", "``ft``:沿x方向的力，單位N"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的沿y方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fy)``"
    "描述", "設置軌跡運行中的沿y方向的力"
    "必選參數", "``fy``:沿y方向的力，單位N"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的沿z方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fz)``"
    "描述", "設置軌跡運行中的沿z方向的力"
    "必選參數", "``fz``:沿z方向的力，單位N"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的繞x軸的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tx)``"
    "描述", "設置軌跡運行中的繞x軸的扭矩"
    "必選參數", "``tx``:繞x軸的扭矩，單位Nm"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的繞y軸的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(ty)``"
    "描述", "設置軌跡運行中的繞y軸的扭矩"
    "必選參數", "``ty``:繞y軸的扭矩，單位Nm"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置軌跡運行中的繞z軸的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tz)``"
    "描述", "設置軌跡運行中的繞z軸的扭矩"
    "必選參數", "- ``tz``:繞z軸的扭矩，單位Nm"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

上傳軌跡J文件
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJUpLoad(filePath)``"
    "描述", "上傳軌跡J文件"
    "必選參數", "- ``filePath``:上傳軌跡文件的全路徑名，C://test/testJ.txt"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

刪除軌跡J文件
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TrajectoryJDelete(filePath)``"
    "描述", "刪除軌跡J文件"
    "必選參數", "- ``filePath``:刪除軌跡文件的全路徑名，C://test/testJ.txt"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人軌跡J文件復現代碼示例
+++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "traj.txt"
    rtn = robot.LoadTrajectoryJ(traj_file_name, 100, 1)
    print(f"LoadTrajectoryJ {traj_file_name}, rtn is: {rtn}")
    rtn,traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos:{traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},"
          f"{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 50, 100, 100)
    rtn,traj_num = robot.GetTrajectoryPointNum()
    print(f"GetTrajectoryStartPose rtn is: {rtn}, traj num is: {traj_num}")
    rtn = robot.SetTrajectoryJSpeed(50.0)
    print(f"SetTrajectoryJSpeed is: {rtn}")
    traj_force = [0.0,0.0,0.0,0.0,0.0,0.0]
    traj_force[0] = 10  # fx = 10
    rtn = robot.SetTrajectoryJForceTorque(traj_force)
    print(f"SetTrajectoryJForceTorque rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFx(10.0)
    print(f"SetTrajectoryJForceFx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFy(0.0)
    print(f"SetTrajectoryJForceFy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJForceFz(0.0)
    print(f"SetTrajectoryJForceFz rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTx(10.0)
    print(f"SetTrajectoryJTorqueTx rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTy(10.0)
    print(f"SetTrajectoryJTorqueTy rtn is: {rtn}")
    rtn = robot.SetTrajectoryJTorqueTz(10.0)
    print(f"SetTrajectoryJTorqueTz rtn is: {rtn}")
    rtn = robot.MoveTrajectoryJ()
    print(f"MoveTrajectoryJ rtn is: {rtn}")
    robot.CloseRPC()

軌跡預處理(軌跡前瞻)
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryLA(name, mode, errorLim, type, precision, vamx, amax, jmax, flag)``"
    "描述", "軌跡預處理(軌跡前瞻)"
    "必選參數", "- ``name``:軌跡文件名
    - ``mode``：採樣模式，0-不進行採樣；1-等數據間隔採樣；2-等誤差限制採樣
    - ``errorLim``:誤差限制，使用直線擬合生效
    - ``type``:平滑方式，0-貝塞爾平滑
    - ``precision``:平滑精度，使用貝塞爾平滑時生效
    - ``vamx``:設定的最大速度，mm/s
    - ``amax``:設定的最大加速度，mm/s2
    - ``jmax``:設定的最大加加速度，mm/s3
    - ``flag``:勻速前瞻開啓開關 0-不開啓；1-開啓"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

軌跡復現(軌跡前瞻)
+++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryLA()``"
    "描述", "軌跡復現(軌跡前瞻)"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

軌跡復現(軌跡前瞻)代碼示例
+++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.TrajectoryJUpLoad("D://zUP/traj.txt")
    print(f"Upload TrajectoryJ A {rtn}")
    traj_file_name = "traj.txt"
    rtn = robot.LoadTrajectoryLA(traj_file_name, 1, 2, 0, 2, 50, 200, 1000, 0)
    print(f"LoadTrajectoryLA {traj_file_name}, rtn is: {rtn}")
    rtn, traj_start_pose = robot.GetTrajectoryStartPose(traj_file_name)
    print(f"GetTrajectoryStartPose is: {rtn}")
    print(f"desc_pos: {traj_start_pose[0]},{traj_start_pose[1]},{traj_start_pose[2]},{traj_start_pose[3]},{traj_start_pose[4]},{traj_start_pose[5]}")
    time.sleep(1)
    robot.SetSpeed(50)
    robot.MoveCart(traj_start_pose, 0, 0, 100, 100, 100)
    rtn = robot.MoveTrajectoryLA()
    print(f"MoveTrajectoryLA rtn is: {rtn}")
    robot.CloseRPC()

運動到TPD軌跡記錄起點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToTPDStart(name, moveType, ovl)``"
    "描述", "運動到TPD軌跡記錄起點"
    "必選參數", "
    - ``name``:軌跡文件名
    - ``moveType``：運動類型；0-PTP; 1-LIN
    - ``ovl``:速度縮放百分比，範圍[0~100]
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

運動到TPD軌跡記錄起點的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    from ctypes import sizeof
    # 與機器人控制器建立連接,連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    import time

    def TestTPD(self):
        type = 1
        name = "tpd2025"
        period_ms = 4
        di_choose = 0
        do_choose = 0

        robot.SetTPDParam(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)

        robot.Mode(1)
        time.sleep(1)
        robot.DragTeachSwitch(1)
        robot.SetTPDStart(type=type, name=name, period_ms=period_ms, di_choose=di_choose, do_choose=do_choose)
        time.sleep(3)
        robot.SetWebTPDStop()
        robot.DragTeachSwitch(0)

        time.sleep(1)
        ovl = 100.0
        blend = 0
        start_pose = [0.0] * 6
        rtn = robot.LoadTPD(name)
        print(f"LoadTPD rtn is: {rtn}")

        rtn, start_pose = robot.GetTPDStartPose(name)
        print(f"start pose, xyz is: {start_pose[0]},{start_pose[1]},{start_pose[2]}. rpy is: {start_pose[3]},{start_pose[4]},{start_pose[5]}")
        # robot.MoveCart(desc_pos=start_pose, tool=0, user=0, vel=100, acc=100, ovl=ovl, blendT=-1, config=-1)
        #time.sleep(1)

        rtn = robot.MoveToTPDStart(name, 0, 100)
        print(f"MoveToTPDStart rtn is: {rtn}")

        rtn = robot.MoveTPD(name, blend, ovl)
        print(f"MoveTPD rtn is: {rtn}")
        time.sleep(5)

        robot.SetTPDDelete(name)

        robot.CloseRPC()
        return 0

    TestTPD(robot)