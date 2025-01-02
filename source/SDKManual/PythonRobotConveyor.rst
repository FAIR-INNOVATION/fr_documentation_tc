传动带
======================

.. toctree:: 
    :maxdepth: 5

传动带启动、停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorStartEnd(status)``"
    "描述", "传动带启动、停止"
    "必选参数", "- ``status``： 传动带状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #传送带运动，1-运动，0-停止
    status = 1
    robot.ConveyorStartEnd(status)
    #点记录
    ret = robot.ConveyorPointIORecord()
    print("记录IO检测点",ret)
    ret = robot.ConveyorPointARecord()
    print("记录A点",ret)
    ret = robot.ConveyorRefPointRecord()
    print("记录参考点",ret)
    ret = robot.ConveyorPointBRecord()
    print("记录B点",ret)

记录IO检测点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointIORecord()``"
    "描述", "记录IO检测点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录A点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointARecord()``"
    "描述", "记录A点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

记录参考点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorRefPointRecord()``"
    "描述", "记录参考点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接。 成功连接返回机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot. ConveyorRefPointRecord()
    print("Convey record reference point ",ret)

记录B点
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorPointBRecord()``"
    "描述", "记录B点"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接。 成功连接返回机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.ConveyorPointBRecord()
    print("Convey record B point ",ret)

传动带参数配置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorSetParam(param)``"
    "描述", "传动带参数配置"
    "必选参数", "- `` param``： = [encChannel,resolution,lead,wpAxis,vision,speedRadio] 
                                    - ``encChannel``: 编码器通道 1-2
                                    - ``resolution``: 编码器分辨率 编码器旋转一圈脉冲个数
                                    - ``lead``: 机械传动比 编码器旋转一圈传送带移动距离
                                    - ``wpAxis``: 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
                                    - ``vision``: 是否配视觉  0-不配 1-配,
                                    - ``speedRadio``: 速度比  针对传送带跟踪抓取速度范围为（1-100）  跟踪运动、TPD跟踪设置为1"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
----------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接。 成功连接返回机器人对象
    robot = Robot.RPC('192.168.58.2')
    param=[1,10000,200,0,0,20]
    ret = robot.ConveyorSetParam(param)
    print("Set Conveyor Param",ret)

传动带抓取点补偿
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorCatchPointComp(cmp)``"
    "描述", "传动带抓取点补偿"
    "必选参数", "- ``cmp``： 补偿位置 [x,y,z]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传送带工件IO检测
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorIODetect(max_t)``"
    "描述", "传送带工件IO检测"
    "必选参数", "- ``max_t``： 最大检测时间，单位ms"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #传送带跟踪抓取
    while(1):
        robot.MoveL([-333.597, 60.354, 404.341, -179.143, -0.778, 91.275],0,0)
        error =robot.ConveyorIODetect(1000)
        print("传送带工件IO检测错误码",error)
        error =robot.ConveyorGetTrackData(1)
        print("获取物体当前位置错误码",error)
        error =robot.ConveyorTrackStart(1)
        print("传动带跟踪开始错误码",error)
        error =robot.ConveyorTrackMoveL("cvrCatchPoint",0,0,vel = 60.0)
        print("直线运动错误码",error)
        error =robot.MoveGripper(1,55,20,20,30000,0)
        print("夹爪控制错误码",error)
        error =robot.ConveyorTrackMoveL("cvrRaisePoint",0,0,vel = 60.0)
        print("直线运动错误码",error)
        error = robot.ConveyorTrackEnd()
        print("传动带跟踪结束错误码错误码",error)
        error = robot.MoveL([-333.625, -229.039, 404.340, -179.141, -0.778, 91.276], 0, 0,vel =30)
        error = robot.MoveL([-333.564, 332.204, 342.217, -179.145, -0.780, 91.268], 0, 0,vel =30)
        error = robot.MoveGripper(1,100,10,21,30000,0)
        print("夹爪控制错误码",error)

获取物体当前位置
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorGetTrackData(mode)``"
    "描述", "获取物体当前位置"
    "必选参数", "- ``mode``： 1-跟踪抓取 2-跟踪运动 3-TPD跟踪"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪开始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackStart(status)``"
    "描述", "传动带跟踪开始"
    "必选参数", "- ``status``： 状态，1-启动，0-停止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

传动带跟踪停止
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackEnd()``"
    "描述", "传动带跟踪停止"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

直线运动
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ConveyorTrackMoveL(name,tool,wobj,vel=20,acc=100,ovl=100,blendR=-1.0)``"
    "描述", "直线运动"
    "必选参数", "- ``name``：cvrCatchPoint 或cvrRaisePoint
    - ``tool``: 工具号
    - ``wobj``:  工件号"
    "默认参数", "- ``vel``: 速度 默认20
    - ``acc``: 加速度 默认100
    - ``ovl``: 速度缩放因子 默认100
    - ``blendR``: [-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #参数配置
    param=[1,10000,200,0,0,20]
    ret = robot.ConveyorSetParam(param)
    print("传送带参数配置错误码",ret)
    time.sleep(1)
    #抓取点补偿
    comp = [0.00, 0.00, 0.00]
    ret1 = robot.ConveyorCatchPointComp(comp)
    print("传动带抓取点补偿错误码",ret1)