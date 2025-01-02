焊接
======================

.. toctree:: 
    :maxdepth: 5

焊接开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCStart(ioType, arcNum, timeout)``"
    "描述", "焊接开始"
    "必选参数", "- ``ioType``：io类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
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

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #起弧
    ret = robot.ARCStart(weldIOType,arcNum,weldTimeout)
    print("ARCStart错误码", ret)
    time.sleep(3)

焊接结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ARCEnd(ioType, arcNum, timeout)``"
    "描述", "焊接结束"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``arcNum``： 焊机配置文件编号
    - ``timeout``： 起弧超时时间"
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

    weldIOType =0
    arcNum =0
    weldTimeout=5000
    #收弧
    ret = robot.ARCEnd(weldIOType,arcNum,weldTimeout)
    print("ARCEnd错误码", ret)
    time.sleep(3)

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrentRelation(currentMin, currentMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "设置焊接电流与输出模拟量对应关系"
    "必选参数", "- ``currentMin``： 焊接电流-模拟量输出线性关系左侧点电流值(A)
    - ``currentMax``：  焊接电流-模拟量输出线性关系右侧点电流值(A)
    - ``outputVoltageMin``： 焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电流模拟量输出端口"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    weldIOType =0

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    weldIOType =0
    arcNum =0
    weldTimeout=5000

    #设置焊接电流与模拟量线性关系
    ret = robot.WeldingSetCurrentRelation(0,400,0,10,0)
    print("WeldingSetCurrentRelation", ret)
    time.sleep(1)
    #获取焊接电流与模拟量线性关系
    ret = robot.WeldingGetCurrentRelation()
    print("WeldingGetCurrentRelation", ret)
    time.sleep(1)

    #设置焊接电压与模拟量线性关系
    ret = robot.WeldingSetVoltageRelation(0,400,0,10,0)
    print("WeldingSetVoltageRelation", ret)
    time.sleep(1)
    #获取焊接电压与模拟量线性关系
    ret = robot.WeldingGetVoltageRelation()
    print("WeldingGetVoltageRelation", ret)
    time.sleep(1)

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltageRelation(weldVoltageMin, weldVoltageMax, outputVoltageMin, outputVoltageMax)``"
    "描述", "设置焊接电压与输出模拟量对应关系"
    "必选参数", "- ``weldVoltageMin``： 焊接电压-模拟量输出线性关系左侧点焊接电压值(A)
    - ``weldVoltageMax``：  焊接电压-模拟量输出线性关系右侧点焊接电压值(A)
    - ``outputVoltageMin``： 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电压-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetCurrentRelation()``"
    "描述", "获取焊接电流与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``currentMin``：焊接电流-模拟量输出线性关系左侧点电流值(A)
    - ``currentMax``：焊接电流-模拟量输出线性关系右侧点电流值(A)
    - ``outputVoltageMin``：焊接电流-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``：焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetVoltageRelation()``"
    "描述", "获取焊接电压与输出模拟量对应关系"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weldVoltageMin``: 焊接电压-模拟量输出线性关系左侧点焊接电压值(V)
    - ``weldVoltageMax``: 焊接电压-模拟量输出线性关系右侧点焊接电压值(V)
    - ``outputVoltageMin``: 焊接电压-模拟量输出线性关系左侧点模拟量输出电压值(V)
    - ``outputVoltageMax``: 焊接电流-模拟量输出线性关系右侧点模拟量输出电压值(V)
    - ``AOIndex``：焊接电压模拟量输出端口"

设置焊接电流
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetCurrent(ioType, current, AOIndex, blend)``"
    "描述", "设置焊接电流"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``current``： 焊接电流值(A)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置焊接电压
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetVoltage(ioType, voltage, AOIndex, blend)``"
    "描述", "设置焊接电压"
    "必选参数", "- ``ioType``： 类型 0-控制器IO； 1-扩展IO
    - ``voltage``： 焊接电压值(V)
    - ``AOIndex``： 焊接电流控制箱模拟量输出端口(0-1)
    - ``blend``：是否平滑 0-不平滑，1-平滑"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveSetPara(weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftRange, weaveRightRange, additionalStayTime, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary, weaveYawAngle=0)``"
    "描述", "设置摆动参数"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号
    - ``weaveType``： 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    - ``weaveFrequency``： 摆动频率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-周期不包含等待时间；1-周期包含等待时间必选参数
    - ``weaveRange``： 摆动幅度(mm)
    - ``weaveLeftStayTime``： 摆动左停留时间(ms)
    - ``weaveRightStayTime``：  摆动右停留时间(ms)
    - ``weaveCircleRadio``： 圆形摆动-回调比率(0-100%)
    - ``weaveStationary``： 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止"
    "默认参数", "- ``weaveYawAngle``： 摆动方向方位角（绕摆动Z轴旋转），单位°,默认0"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
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
    #设置摆动参数
    ret = robot.WeaveSetPara(weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveSetPara ", ret)
    time.sleep(1)

    #摆动开始
    ret = robot.WeaveStart(0)
    print("WeaveStart ", ret)
    time.sleep(1)
    ret,pose =robot.GetActualTCPPose(1);
    print(ret,pose)
    pose[2]=pose[2]+50
    ret = robot.MoveL(pose,tool,user)
    print("MoveL ", ret)
    time.sleep(1)
    #即时设置摆动参数
    ret = robot.WeaveOnlineSetPara (weaveNum,weaveType,weaveFraquency,weavelncStayTime,weaveRange,weaveLeftStayTime,weaveRightStayTime,weaveCircleRadio,weaveStationary)
    print("WeaveOnlineSetPara ", ret)
    time.sleep(1)
    #摆动结束
    ret = robot.WeaveEnd(0)
    print("WeaveEnd ", ret)
    time.sleep(1)

即时设置摆动参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveOnlineSetPara (weaveNum, weaveType, weaveFrequency, weaveIncStayTime, weaveRange, weaveLeftStayTime, weaveRightStayTime, weaveCircleRadio, weaveStationary)``"
    "描述", "即时设置摆动参数"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号
    - ``weaveType``： 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    - ``weaveFrequency``： 摆动频率(Hz)
    - ``weaveIncStayTime``： 等待模式 0-周期不包含等待时间；1-周期包含等待时间必选参数
    - ``weaveRange``： 摆动幅度(mm)
    - ``weaveLeftStayTime``： 摆动左停留时间(ms)
    - ``weaveRightStayTime``：  摆动右停留时间(ms)
    - ``weaveCircleRadio``： 圆形摆动-回调比率(0-100%)
    - ``weaveStationary``： 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStart(weaveNum)``"
    "描述", "摆动开始"
    "必选参数", "- ``weaveNum``： 类型 0-控制器IO； 1-扩展IO"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEnd(weaveNum)``"
    "描述", "摆动结束"
    "必选参数", "- ``weaveNum``： 摆焊参数配置编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

正向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForwardWireFeed(ioType, wireFeed)``"
    "描述", "正向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
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

    weldIOType =0
    #正向送丝
    ret = robot.SetForwardWireFeed(weldIOType,1)
    print("SetForwardWireFeed错误码", ret)
    time.sleep(1)
    ret = robot.SetForwardWireFeed(weldIOType,0)
    print("SetForwardWireFeed错误码", ret)
    time.sleep(1)

    #反向送丝
    ret = robot.SetReverseWireFeed(weldIOType,1)
    print("SetReverseWireFeed错误码", ret)
    time.sleep(1)
    #停止反向送丝
    ret = robot.SetReverseWireFeed(weldIOType,0)
    print("SetReverseWireFeed错误码", ret)
    time.sleep(1)

    #送气
    ret = robot.SetAspirated(weldIOType,1)
    print("SetAspirated错误码", ret)
    time.sleep(1)
    #停止送气
    ret = robot.SetAspirated(weldIOType,0)
    print("SetAspirated错误码", ret)
    time.sleep(1)

反向送丝
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetReverseWireFeed(ioType, wireFeed)``"
    "描述", "反向送丝"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``wireFeed``： 送丝控制  0-停止送丝；1-送丝"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

送气
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAspirated(ioType, airControl)``"
    "描述", "送气"
    "必选参数", "- ``ioType``： 0-控制器IO；1-扩展IO
    - ``airControl``： 送气控制  0-停止送气；1-送气"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

段焊获取位置和姿态
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSegmentWeldPoint(startPos, endPos, startDistance)``"
    "描述", "段焊获取位置和姿态"
    "必选参数", "- ``startPos=[x,y,z,rx,ry,rz]``： 起始点坐标
    - ``endPos=[x,y,z,rx,ry,rz]``： 终止点坐标
    - ``startDistance``： 焊接点至起点的长度"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weldPointDesc=[x,y,z,rx,ry,rz]``： 焊接点的笛卡尔坐标信息 
    - ``weldPointJoint=[j1,j2,j3,j4,j5,j6]``： 焊接点的关节坐标信息
    - ``tool``： 工具号
    - ``user``： 工件号"

分段焊接启动
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldStart(startDesePos,  endDesePos, startJPos, endJPos, weldLength, noWeldLength, weldIOType, arcNum, weldTimeout, isWeave,weaveNum,tool,user,vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0,exaxis_pos=[0.0, 0.0, 0.0, 0.0],  search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "分段焊接启动"
    "必选参数", "- ``startDesePos``： 初始笛卡尔位姿，单位 [mm][°]
    - ``endDesePos``： 目标笛卡尔位姿，单位 [mm][°]
    - ``startJPos``：初始关节位置，单位 [°] 
    - ``endJPos``：目标关节位置，单位 [°]  
    - ``weldLength``：焊接长度，单位 [mm] 
    - ``noWeldLength``：非焊接长度，单位 [mm] 
    - ``weldIOType``：焊接IO类型(0-控制箱IO；1-扩展IO) arcNum 焊机配置文件编号 
    - ``timeout``：熄弧超时时间 
    - ``isWeave``：焊接 False-不焊接 
    - ``weaveNum``：摆焊参数配置编号 
    - ``tool``：工具号，[0~14]
    - ``user``：工件号，[0~14]"
    "默认参数", "- ``vel``：速度百分比，[0~100] 默认20.0
    - ``acc``：加速度[0~100] 暂不开放 默认0.0
    - ``ovl``：速度缩放因子，[0~100] 默认100.0
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]"
    "返回值", "- 错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
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

分段焊接终止
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SegmentWeldEnd(ioType, arcNum, timeout)``"
    "描述", "分段焊接终止"
    "必选参数", "- ``ioType``：io类型 0-控制器IO； 1-扩展IO
    - ``arcNum``：焊机配置文件编号
    - ``timeout``：熄弧超时时间"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

焊丝寻位开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchStart(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊丝寻位开始"
    "必选参数", "- ``refPos``： 1-基准点 2-接触点
    - ``searchVel``： 寻位速度 %
    - ``searchDis``： 寻位距离 mm
    - ``autoBackFlag``： 自动返回标志，0-不自动；-自动
    - ``autoBackVel``： 自动返回速度 %
    - ``autoBackDis``： 自动返回距离 mm
    - ``offectFlag``： 1-带偏移量寻位；2-示教点寻位"
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

    refPos = 1 #  1-基准点 2-接触点
    searchVel = 10 #寻位速度 %
    searchDis = 100 #寻位距离 mm
    autoBackFlag = 0 #自动返回标志，0-不自动；1-自动
    autoBackVel = 10 #自动返回速度 %
    autoBackDis = 100 #自动返回距离 mm
    offectFlag = 0  #1-带偏移量寻位；2-示教点寻位
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

焊丝寻位结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchEnd(refPos,searchVel,searchDis,autoBackFlag,autoBackVel,autoBackDis,offectFlag)``"
    "描述", "焊丝寻位结束"
    "必选参数", "- ``refPos``： 1-基准点 2-接触点
    - ``searchVel``： 寻位速度 %
    - ``searchDis``： 寻位距离 mm
    - ``autoBackFlag``： 自动返回标志，0-不自动；-自动
    - ``autoBackVel``： 自动返回速度 %
    - ``autoBackDis``： 自动返回距离 mm
    - ``offectFlag``： 1-带偏移量寻位；2-示教点寻位"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

计算焊丝寻位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWireSearchOffset(seamType, method,varNameRef,varNameRes)``"
    "描述", "计算焊丝寻位偏移量"
    "必选参数", "- ``seamType``： 焊缝类型
    - ``method``： 计算方法
    - ``varNameRef``： 基准点1-6，“#”表示无点变量
    - ``varNameRes``： 接触点1-6，“#”表示无点变量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``offsetFlag``： 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
    - ``offset``： 偏移位姿[x, y, z, a, b, c]"

等待焊丝寻位完成
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WireSearchWait(varname)``"
    "描述", "等待焊丝寻位完成"
    "必选参数", "- ``varName``： 接触点名称 “RES0” ~ “RES99”"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

焊丝寻位接触点写入数据库
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPointToDatabase(varName,pos)``"
    "描述", "焊丝寻位接触点写入数据库"
    "必选参数", "- ``varName``： 接触点名称 “RES0” ~ “RES99”
    - ``pos``：接触点数据[x, y, x, a, b, c]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

电弧跟踪控制
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceControl(flag,delaytime, isLeftRight, klr, tStartLr, stepMaxLr, sumMaxLr, isUpLow, kud, tStartUd, stepMaxUd, sumMaxUd, axisSelect, referenceType, referSampleStartUd, referSampleCountUd, referenceCurrent)``"
    "描述", "电弧跟踪控制"
    "必选参数", "- ``flag``： 开关，0-关；1-开
    - ``delayTime``：滞后时间，单位ms
    - ``isLeftRight``：左右偏差补偿 0-关闭，1-开启
    - ``klr``：左右调节系数(灵敏度)
    - ``tStartLr``：左右开始补偿时间cyc
    - ``stepMaxLr``：左右每次最大补偿量 mm
    - ``sumMaxLr``：左右总计最大补偿量 mm
    - ``isUpLow``：上下偏差补偿 0-关闭，1-开启
    - ``kud``：上下调节系数(灵敏度)
    - ``tStartUd``：上下开始补偿时间cyc
    - ``stepMaxUd``：上下每次最大补偿量 mm
    - ``sumMaxUd``：上下总计最大补偿量
    - ``axisSelect``：上下坐标系选择，0-摆动；1-工具；2-基座
    - ``referenceType``：上下基准电流设定方式，0-反馈；1-常数
    - ``referSampleStartUd``：上下基准电流采样开始计数(反馈)，cyc
    - ``referSampleCountUd``：上下基准电流采样循环计数(反馈)，cyc
    - ``referenceCurrent``：上下基准电流mA"
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

    flag = 1 #开关，0-关；1-开
    delaytime=0 #滞后时间，单位ms
    isLeftRight=0 #左右偏差补偿 0-关闭，1-开启
    klr = 0.06 #左右调节系数(灵敏度)
    tStartLr = 5 #左右开始补偿时间cyc
    stepMaxLr =5 #左右每次最大补偿量 mm
    sumMaxLr = 300 #左右总计最大补偿量 mm
    isUpLow = 1 #上下偏差补偿
    kud =-0.06 #上下调节系数(灵敏度)
    tStartUd = 5 #上下开始补偿时间cyc
    stepMaxUd = 5 #上下每次最大补偿量 mm
    sumMaxUd = 300 #上下总计最大补偿量
    axisSelect = 1 #上下坐标系选择，0-摆动；1-工具；2-基座
    referenceType = 0 #上下基准电流设定方式，0-反馈；1-常数
    referSampleStartUd = 4 # 上下基准电流采样开始计数(反馈)，cyc
    referSampleCountUd = 1 # 上下基准电流采样循环计数(反馈)，cyc
    referenceCurrent = 10 # 上下基准电流mA

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

电弧跟踪AI通带选择
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceExtAIChannelConfig(channel)``"
    "描述", "电弧跟踪AI通带选择"
    "必选参数", "- ``channel``：电弧跟踪AI通带选择,[0-3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

仿真摆动开始
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveStartSim(weaveNum)``"
    "描述", "仿真摆动开始"
    "必选参数", "- ``weaveNum``：摆动参数编号"
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

仿真摆动结束
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveEndSim(weaveNum)``"
    "描述", "仿真摆动结束"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectStart(weaveNum)``"
    "描述", "开始轨迹检测预警(不运动)"
    "必选参数", "- ``weaveNum``：摆动参数编号"
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
    
结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeaveInspectEnd(weaveNum)``"
    "描述", "结束轨迹检测预警(不运动)"
    "必选参数", "- ``weaveNum``：摆动参数编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
    
设置焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime)``"
    "描述", "设置焊接工艺曲线参数"
    "必选参数", "
    - ``id``： 焊接工艺编号(1-99)
    - ``startCurrent``： 起弧电流(A)
    - ``startVoltage``：startVoltage 起弧电压(V)
    - ``startTime``：startTime 起弧时间(ms)
    - ``weldCurrent``：weldCurrent 焊接电流(A)
    - ``weldVoltage``：weldVoltage 焊接电压(V)
    - ``endCurrent``：endCurrent 收弧电流(A)
    - ``endVoltage``：endVoltage 收弧电压(V)
    - ``endTime``：endTime 收弧时间(ms)
    "
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

    id = 1 #焊接工艺编号(1-99)
    startCurrent = 177 #起弧电流(A)
    startVoltage = 27 #起弧电压(V)
    startTime = 1000 #起弧时间(ms)
    weldCurrent = 178 #焊接电流(A)
    weldVoltage = 28 #焊接电压(V)
    endCurrent = 176 #收弧电流(A)
    endVoltage = 26 # 收弧电压(V)
    endTime = 1000 #收弧时间(ms)

    error = robot.WeldingSetProcessParam(id, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage,
                                            endCurrent, endVoltage, endTime)

    print("WeldingSetProcessParam return:",error)

    error = robot.WeldingGetProcessParam(1)
    print("WeldingGetProcessParam return:",error)
        
获取焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WeldingGetProcessParam(id)``"
    "描述", "获取焊接工艺曲线参数"
    "必选参数", "
    - ``id``： 焊接工艺编号(1-99)
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``返回值（调用成功返回） startCurrent``：起弧电流(A)
    - ``startVoltage``： 起弧电压(V)
    - ``startTime``：起弧时间(ms)
    - ``weldCurrent``：焊接电流(A)
    - ``weldVoltage``：焊接电压(V)
    - ``endCurrent``：收弧电流(A)
    - ``endVoltage``：收弧电压(V)
    - ``endTime``：收弧时间(ms)
    " 
    
扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAirControlExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机气体检测信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
            
代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象

    robot = Robot.RPC('192.168.58.2')

    #扩展IO-配置焊机气体检测信号
    error = robot.SetAirControlExtDoNum(10)
    print("SetAirControlExtDoNum 10 return:",error)

    #扩展IO-配置焊机起弧信号
    error = robot.SetArcStartExtDoNum(11)
    print("SetArcStartExtDoNum 11 return:",error)

    #扩展IO-配置焊机反向送丝信号
    error = robot.SetWireReverseFeedExtDoNum(12)
    print("SetWireReverseFeedExtDoNum 12 return:",error)

    #扩展IO-配置焊机正向送丝信号
    error = robot.SetWireForwardFeedExtDoNum(13)
    print("SetWireForwardFeedExtDoNum 13 return:",error)

    #扩展IO-配置焊机起弧成功信号
    error = robot.SetArcDoneExtDiNum(10)
    print("SetArcDoneExtDiNum 10 return:",error)

    #扩展IO-配置焊机准备信号
    error = robot.SetWeldReadyExtDiNum(11)
    print("SetWeldReadyExtDiNum 11 return:",error)

    #扩展IO-配置焊接中断恢复信号
    error = robot.SetExtDIWeldBreakOffRecover(12,13)
    print("SetExtDIWeldBreakOffRecover 12  13 return:",error)
        
扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcStartExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机起弧信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireReverseFeedExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机反向送丝信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireForwardFeedExtDoNum(DONum)``"
    "描述", "扩展IO-配置焊机正向送丝信号"
    "必选参数", "
    - ``DONum``：气体检测信号扩展DO编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "扩展IO-配置焊机起弧成功信号"
    "必选参数", "
    - ``DINum``：焊机准备信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetArcDoneExtDiNum(DINum)``"
    "描述", "扩展IO-配置焊机准备信号"
    "必选参数", "
    - ``DINum``：焊机准备信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 
        
扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExtDIWeldBreakOffRecover(reWeldDINum, abortWeldDINum)``"
    "描述", "扩展IO-配置焊接中断恢复信号"
    "必选参数", "
    - ``reWeldDINum``：焊接中断后恢复焊接信号扩展DI编号
    - ``abortWeldDINum``：焊接中断后退出焊接信号扩展DI编号
    "
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

设置焊丝寻位扩展IO端口
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWireSearchExtDIONum(searchDoneDINum, searchStartDONum)``"
    "描述", "设置焊丝寻位扩展IO端口"
    "必选参数", "- ``searchDoneDINum``：焊丝寻位成功DO端口(0-127)
    - ``searchStartDONum``：焊丝寻位启停控制DO端口(0-127)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

焊机控制模式切换
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

设置焊机控制模式扩展DO端口
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlModeExtDoNum(DONum)``"
    "描述", "设置焊机控制模式扩展DO端口"
    "必选参数", "- ``DONum``：焊机控制模式DO端口(0-127)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

设置焊机控制模式
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWeldMachineCtrlMode(mode)``"
    "描述", "设置焊机控制模式"
    "必选参数", "- ``mode``：焊机控制模式;0-一元化"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode" 

代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
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

电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayStart()``"
    "描述", "电弧追踪 + 多层多道补偿开启"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ArcWeldTraceReplayEnd()``"
    "描述", "电弧追踪 + 多层多道补偿关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MultilayerOffsetTrsfToBase(pointo, pointX, pointZ, dx, dy, db)``"
    "描述", "偏移量坐标变化-多层多道焊"
    "必选参数", "- ``pointo``：基准点笛卡尔位姿
    - ``pointX``：基准点X向偏移方向点笛卡尔位姿
    - ``pointZ``：基准点Z向偏移方向点笛卡尔位姿
    - ``dx``：x方向偏移量(mm)
    - ``dz``：z方向偏移量(mm)
    - ``dry``：绕y轴偏移量(°)"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``offset``：计算结果偏移量"