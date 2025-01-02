机器人轨迹复现
=================

.. toctree:: 
    :maxdepth: 5

设置轨迹记录参数
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDParam(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "设置轨迹记录参数"
    "必选参数", "- ``name``：轨迹名；
    - ``period_ms``：采样周期，固定值，2ms 或 4ms 或 8ms;"
    "默认参数", "- ``type``：数据类型，1-关节位置；
    - ``di_choose``：DI 选择,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不选择，1-选择 默认0;
    - ``do_choose``：DO 选择,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不选择，1-选择 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    type = 1  # 数据类型，1-关节位置
    name = 'tpd2023'  # 轨迹名
    period = 4  #采样周期，2ms或4ms或8ms
    di = 0 # di输入配置
    do = 0 # do输出配置
    ret = robot.SetTPDParam(name, period, di_choose=di)    #配置TPD参数
    print("配置TPD参数错误码", ret)
    robot.Mode(1)  # 机器人切入手动模式
    time.sleep(1)  
    robot.DragTeachSwitch(1)  #机器人切入拖动示教模式
    ret = robot.GetActualTCPPose()
    print("获取当前工具位姿", ret)
    time.sleep(1)
    ret = robot.SetTPDStart(name, period, do_choose=do)   # 开始记录示教轨迹
    print("开始记录示教轨迹错误码", ret)
    time.sleep(15)
    ret = robot.SetWebTPDStop()  # 停止记录示教轨迹
    print("停止记录示教轨迹错误码", ret)
    robot.DragTeachSwitch(0)  #机器人切入非拖动示教模式
    # robot.SetTPDDelete('tpd2023')   # 删除TPD轨迹

开始轨迹记录
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDStart(name, period_ms, type=1,di_choose=0, do_choose=0)``"
    "描述", "开始轨迹记录"
    "必选参数", "- ``name``：轨迹名；
    - ``period_ms``：采样周期，固定值，2ms或4ms或8ms；"
    "默认参数", "- ``type``：数数据类型，1-关节位置 默认1;
    - ``di_choose``：DI 选择,bit0~bit7 对应控制箱 DI0~DI7，bit8~bit9 对应末端DI0~DI1，0-不选择，1-选择 默认0;
    - ``do_choose``：DO 选择,bit0~bit7 对应控制箱 DO0~DO7，bit8~bit9 对应末端 DO0~DO1，0-不选择，1-选择 默认0"
    "返回值", "错误码 成功-0  失败- errcode"

停止轨迹记录
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWebTPDStop()``"
    "描述", "停止轨迹记录"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

删除轨迹记录
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTPDDelete(name)``"
    "描述", "删除轨迹记录"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹预加载
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTPD(name)``"
    "描述", "轨迹预加载"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    # P1=[-321.821, 125.694, 282.556, 174.106, -15.599, 152.669]
    name = 'tpd2023'   #轨迹名
    blend = 1   #是否平滑，1-平滑，0-不平滑
    ovl = 100.0   #速度缩放
    ret = robot.LoadTPD(name)  #轨迹预加载
    print("轨迹预加载错误码",ret)
    ret,P1 = robot.GetTPDStartPose(name)   #获取轨迹起始位姿
    print ("获取轨迹起始位姿错误码",ret,"起始位姿",P1)
    ret = robot.MoveL(P1,0,0)       #运动到起始点
    print("运动到起始点错误码",ret)
    time.sleep(10)
    ret = robot.MoveTPD(name, blend, ovl)  #轨迹复现
    print("轨迹复现错误码",ret)

获取轨迹起始位姿
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTPDStartPose(name)``"
    "描述", "获取轨迹起始位姿"
    "必选参数", "- ``name``:轨迹名"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：轨迹起始位姿"

轨迹复现
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTPD(name,blend,ovl)``"
    "描述", "轨迹复现"
    "必选参数", "- ``name``:轨迹名
    - ``blend``：是否平滑，0-不平滑，1-平滑
    - ``ovl``：速度缩放因子，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹预处理
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadTrajectoryJ(name,ovl,opt=1)``"
    "描述", "轨迹预处理"
    "必选参数", "- ``name``:轨迹名,如：/fruser/traj/trajHelix_aima_1.txt;
    - ``ovl``：速度缩放百分比，范围[0~100];"
    "默认参数", "- ``opt``：1-控制点，默认为1"
    "返回值", "错误码 成功-0  失败- errcode"

轨迹复现
++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveTrajectoryJ()``"
    "描述", "轨迹复现"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取轨迹起始位姿
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryStartPose(name)``"
    "描述", "获取轨迹起始位姿"
    "必选参数", "``name``:轨迹名"
    "默认参数", "无"       
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pose=[x,y,z,rx,ry,rz]``：轨迹起始位姿"

获取轨迹点编号
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTrajectoryPointNum()``"
    "描述", "获取轨迹点编号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``pnum``：轨迹点编号"

设置轨迹运行中的速度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJSpeed(ovl)``"
    "描述", "设置轨迹运行中的速度"
    "必选参数", "``ovl``:速度缩放百分比，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的力和扭矩
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceTorque(ft)``"
    "描述", "设置轨迹运行中的力和扭矩"
    "必选参数", "``ft=[fx,fy,fz,tx,ty,tz]``:单位N和Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿x方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fx)``"
    "描述", "设置轨迹运行中的沿x方向的力"
    "必选参数", "``ft``:沿x方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿y方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fy)``"
    "描述", "设置轨迹运行中的沿y方向的力"
    "必选参数", "``fy``:沿y方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的沿z方向的力
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJForceFx(fz)``"
    "描述", "设置轨迹运行中的沿z方向的力"
    "必选参数", "``fz``:沿z方向的力，单位N"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕x轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tx)``"
    "描述", "设置轨迹运行中的绕x轴的扭矩"
    "必选参数", "``tx``:绕x轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕y轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(ty)``"
    "描述", "设置轨迹运行中的绕y轴的扭矩"
    "必选参数", "``ty``:绕y轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置轨迹运行中的绕z轴的扭矩
+++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTrajectoryJTorqueTx(tz)``"
    "描述", "设置轨迹运行中的绕z轴的扭矩"
    "必选参数", "``tz``:绕z轴的扭矩，单位Nm"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    name = "/fruser/traj/trajHelix_aima_1.txt"   #轨迹名
    blend = 1   #是否平滑，1-平滑，0-不平滑
    ovl = 50.0   #速度缩放
    ft =[0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    ret = robot.LoadTrajectoryJ(name,ovl)  #轨迹预加载
    print("轨迹预加载错误码",ret)
    ret,P1 = robot.GetTrajectoryStartPose(name)   #获取轨迹起始位姿
    print ("获取轨迹起始位姿错误码",ret,"起始位姿",P1)
    ret = robot.MoveL(P1,1,0)       #运动到起始点
    print("运动到起始点错误码",ret)
    ret = robot.GetTrajectoryPointNum()       #获取轨迹点编号
    print("获取轨迹点编号错误码",ret)
    time.sleep(10)
    ret = robot.MoveTrajectoryJ()  #轨迹复现
    print("轨迹复现错误码",ret)
    time.sleep(10)
    ret = robot.SetTrajectoryJSpeed(ovl)  #设置轨迹运行中的速度
    print("设置轨迹运行中的速度错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceTorque(ft)  #设置轨迹运行中的力和扭矩
    print("设置轨迹运行中的力和扭矩错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFx(0) #设置轨迹运行中的沿x方向的力
    print("设置轨迹运行中的沿x方向的力错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFy(0) #设置轨迹运行中的沿y方向的力
    print("设置轨迹运行中的沿y方向的力错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJForceFz(0) #设置轨迹运行中的沿z方向的力
    print("设置轨迹运行中的沿z方向的力错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTx(0) #设置轨迹运行中的绕x轴的扭矩
    print("设置轨迹运行中的绕x轴的扭矩错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTy(0) #设置轨迹运行中的绕y轴的扭矩
    print("设置轨迹运行中的绕y轴的扭矩错误码",ret)
    time.sleep(1)
    ret = robot.SetTrajectoryJTorqueTz(0) #设置轨迹运行中的绕z轴的扭矩
    print("设置轨迹运行中的绕z轴的扭矩错误码",ret)
    time.sleep(1)
