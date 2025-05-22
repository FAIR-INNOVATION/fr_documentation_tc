傳動帶
======================

.. toctree:: 
    :maxdepth: 5

傳動皮帶啟動、停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorStartEnd(status)``"
    "描述", "傳動皮帶啟動、停止"
    "必選參數", "- ``status``： 傳動帶狀態，1-啟動，0-停止"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #传送带運動，1-運動，0-停止
    status = 1
    robot.ConveyorStartEnd(status)
    #點記錄
    ret = robot.ConveyorPointIORecord()
    print("記錄IO檢測點",ret)
    ret = robot.ConveyorPointARecord()
    print("記錄A點",ret)
    ret = robot.ConveyorRefPointRecord()
    print("記錄參考點",ret)
    ret = robot.ConveyorPointBRecord()
    print("記錄B點",ret)

記錄IO檢測點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointIORecord()``"
    "描述", "記錄IO檢測點"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

記錄A點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointARecord()``"
    "描述", "記錄A點"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

記錄參考點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorRefPointRecord()``"
    "描述", "記錄參考點"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連線。成功連結返回機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot. ConveyorRefPointRecord()
    print("Convey record reference point ",ret)

記錄B點
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointBRecord()``"
    "描述", "記錄B點"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連線。成功連結返回機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.ConveyorPointBRecord()
    print("Convey record B point ",ret)

傳動帶參數配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param)``"
    "描述", "傳動帶參數配置"
    "必選參數", "- `` param``： = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                                    - ``encChannel``: 編码器通道 1-2
                                    - ``resolution``: 編碼器分辨率 編码器旋转一圈脉冲個数
                                    - ``lead``: 機械傳動比 編码器旋转一圈传送带移動距离
                                    - ``wpAxis``: 工件坐標系編號 針對追蹤運動功能選擇工件坐標系編號，追蹤抓取、TPD追蹤設為0
                                    - ``vision``: 是否配视觉  0-不配 1-配,
                                    - ``speedRadio``: 速度比  针对傳送帶追蹤抓取速度範圍為（1-100）  跟踪運動、TPD跟踪設定為1"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連線。成功連結返回機器人對象
    robot = Robot.RPC('192.168.58.2')
    param=[1,10000,200,0,0,20]
    ret = robot.ConveyorSetParam(param,0,0,0)
    print("Set Conveyor Param",ret)

傳動帶抓取點補償
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorCatchPointComp(cmp)``"
    "描述", "傳動帶抓取點補償"
    "必選參數", "- ``cmp``： 補償位置 [x,y,z]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

傳送帶工件IO檢測
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorIODetect(max_t)``"
    "描述", "傳送帶工件IO檢測"
    "必選參數", "- ``max_t``： 最大檢測時間，單位ms"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #傳送帶追蹤抓取
    while(1):
        robot.MoveL([-333.597, 60.354, 404.341, -179.143, -0.778, 91.275],0,0)
        error =robot.ConveyorIODetect(1000)
        print("傳送帶工件IO檢測錯誤碼",error)
        error =robot.ConveyorGetTrackData(1)
        print("取得物體目前位置錯誤碼",error)
        error =robot.ConveyorTrackStart(1)
        print("傳動皮帶追蹤開始錯誤碼",error)
        error =robot.ConveyorTrackMoveL("cvrCatchPoint",0,0,vel = 60.0)
        print("直線運動錯誤碼",error)
        error =robot.MoveGripper(1,55,20,20,30000,0)
        print("夹爪控制錯誤碼",error)
        error =robot.ConveyorTrackMoveL("cvrRaisePoint",0,0,vel = 60.0)
        print("直線運動錯誤碼",error)
        error = robot.ConveyorTrackEnd()
        print("傳動帶跟踪结束錯誤碼錯誤碼",error)
        error = robot.MoveL([-333.625, -229.039, 404.340, -179.141, -0.778, 91.276], 0, 0,vel =30)
        error = robot.MoveL([-333.564, 332.204, 342.217, -179.145, -0.780, 91.268], 0, 0,vel =30)
        error = robot.MoveGripper(1,100,10,21,30000,0)
        print("夹爪控制錯誤碼",error)

取得物體目前位置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorGetTrackData(mode)``"
    "描述", "取得物體目前位置"
    "必選參數", "- ``mode``： 1-跟踪抓取 2-跟踪運動 3-TPD跟踪"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

傳動皮帶追蹤開始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackStart(status)``"
    "描述", "傳動皮帶追蹤開始"
    "必選參數", "- ``status``： 狀態，1-啟動，0-停止"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

傳動皮帶追蹤停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackEnd()``"
    "描述", "傳動皮帶追蹤停止"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

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
    - ``blendR``: [-1.0]-運動到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，單位 [mm] 默認-1.0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #參數配置
    param=[1,10000,200,0,0,20]
    ret = robot.ConveyorSetParam(param,0,0,0)
    print("傳送帶參數配置錯誤碼",ret)
    time.sleep(1)
    #抓取點补偿
    comp = [0.00, 0.00, 0.00]
    ret1 = robot.ConveyorCatchPointComp(comp)
    print("傳動帶抓取點補償錯誤碼",ret1)

傳送帶參數配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param, followType, startDis, endDis)``"
    "描述", "傳送帶參數配置"
    "必選參數", "- ``param``: = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                    - ``encChannel``: 編碼器通道 1-2
                    - ``resolution``: 編碼器分辨率 (每轉脈衝數)
                    - ``lead``: 機械傳動比 (編碼器每轉傳送帶移動距離)
                    - ``wpAxis``: 工件坐標系編號 (追蹤抓取、TPD追蹤設為0)
                    - ``vision``: 是否配置視覺 0-否 1-是
                    - ``speedRadio``: 速度比 (追蹤抓取速度範圍1-100，運動追蹤、TPD追蹤設為1)
    - ``followType``: 追蹤運動類型，0-運動追蹤；1-追檢運動"
    "默認參數", "- ``startDis``: 追檢抓取需要設置，追蹤起始距離 (-1:自動計算)，單位mm，默認值0
    - ``endDis``: 追檢抓取需要設置，追蹤終止距離，單位mm，默認值100"
    "返回值", "錯誤碼 成功-0 失敗- errcode"


傳送帶通訊輸入檢測
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorComDetect(timeout)``"
    "描述", "傳送帶通訊輸入檢測"
    "必選參數", "- ``timeout``: 等待超時時間(ms)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

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
    "返回值", "錯誤碼 成功-0 失敗- errcode"

代碼示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def Trigger(robot):
        i = int(input("請輸入一個數字以觸發: "))

        rtn = robot.ConveyorComDetectTrigger()
        print(f"ConveyorComDetectTrigger 返回值: {rtn}")

    def ConveyorTest(robot):
        retval = 0

        # 如需使用請取消註釋
        # param = [1, 10000, 200, 0, 0, 20]
        # retval = robot.ConveyorSetParam(param, 0, 0, 0)
        # print(f"ConveyorSetParam 返回值: {retval}")

        index = 1
        max_time = 30000
        block = 0
        retval = 0

        # 定義位姿和關節位置
        startdescPose = [139.176, 4.717, 9.088, -179.999, -0.004, -179.990]
        startjointPos = [-34.129, -88.062, 97.839, -99.780, -90.003, -34.140]

        homePose = [139.177, 4.717, 69.084, -180.000, -0.004, -179.989]
        homejointPos = [-34.129, -88.618, 84.039, -85.423, -90.003, -34.140]

        exaxisPos = [0, 0, 0, 0]
        offdese = [0, 0, 0, 0, 0, 0]

        # 移動到安全位置
        retval = robot.MoveL(desc_pos=homePose, tool=1, user=1)
        print(f"移動到安全位置 MoveL 返回值: {retval}")

        # 啟動觸發線程
        textT = threading.Thread(target=Trigger, args=(robot,))
        textT.daemon = True
        textT.start()

        # 傳送帶操作
        retval = robot.ConveyorComDetect(10000)
        print(f"ConveyorComDetect 返回值: {retval}")

        retval = robot.ConveyorGetTrackData(2)
        print(f"ConveyorGetTrackData 返回值: {retval}")

        retval = robot.ConveyorTrackStart(2)
        print(f"ConveyorTrackStart 返回值: {retval}")

        # 移動命令
        robot.MoveL(desc_pos=startdescPose, tool=1, user=1)
        robot.MoveL(desc_pos=startdescPose, tool=1, user=1)

        # 結束傳送帶追蹤
        retval = robot.ConveyorTrackEnd()
        print(f"ConveyorTrackEnd 返回值: {retval}")

        # 返回安全位置
        robot.MoveL(desc_pos=homePose, tool=1, user=1)

    ConveyorTest(robot)
