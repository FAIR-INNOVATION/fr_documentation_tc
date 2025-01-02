机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSpeed(vel)``"
    "描述", "设置全局速度"
    "必选参数", "- ``vel``:速度百分比，范围[0~100]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetSpeed(20)
    print("设置全局速度错误码:",error)

设置系统变量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysVarValue(id,value)``"
    "描述", "设置系统变量"
    "必选参数", "- ``id``：变量编号，范围[1~20];
    - ``value``：变量值"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1,21):
        error = robot.SetSysVarValue(i,10)
    robot.WaitMs(1000)
    for i in range(1,21):
        sys_var = robot.GetSysVarValue(i)
        print("系统变量编号:",i,"值",sys_var)

设置工具参考点-六点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolPoint(point_num)``"
    "描述", "设置工具参考点-六点法"
    "必选参数", "- ``point_num``：点编号,范围[1~6]"
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
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    for i in range(1,7):
        robot.DragTeachSwitch(1)#切入拖动示教模式
        time.sleep(5)
        error = robot.SetToolPoint(i) #实际应当控制机器人按照要求移动到合适位置后再发送指令
        print("六点法设置工具坐标系，记录点",i,"错误码",error)
        robot.DragTeachSwitch(0)
        time.sleep(1)
    error = robot.ComputeTool()
    print("六点法设置工具坐标系错误码",error)

计算工具坐标系-六点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTool()``"
    "描述", "计算工具坐标系-六点法（设置完六个工具参考点后再进行计算）"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

设置工具参考点-四点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTcp4RefPoint(point_num)``"
    "描述", "设置工具参考点-四点法"
    "必选参数", "``point_num``：点编号,范围[1~4]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    for i in range(1,5):
        robot.DragTeachSwitch(1)#切入拖动示教模式
        time.sleep(5)
        error = robot.SetTcp4RefPoint(i) #应当控制机器人按照要求移动到合适位置后再发送指令
        print("四点法设置工具坐标系，记录点",i,"错误码",error)
        robot.DragTeachSwitch(0)
        time.sleep(1)
    error,t_coord= robot.ComputeTcp4()
    print("四点法设置工具坐标系错误码",error,"工具TCP",t_coord)

计算工具坐标系-四点法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTcp4()``"
    "描述", "计算工具坐标系-四点法（设置完四个工具参考点后再进行计算）"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具坐标系"

设置工具坐标系
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolCoord(id,t_coord,type,install,toolID,loadNum)``"
    "描述", "设置工具坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[1~15]；
    - ``t_coord``:工具中心点相对末端法兰中心位姿，单位[mm][°]；
    - ``type``:0-工具坐标系，1-传感器坐标系；
    - ``install``:安装位置，0-机器人末端，1-机器人外部
    - ``toolID``:工具ID
    - ``loadNum``:负载编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetToolCoord(10,t_coord,0,0,0,0)
    print("设置工具坐标系错误码",error)

设置工具坐标系列表
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolList(id,t_coord ,type, install, loadNum)``"
    "描述", "设置工具坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[1~15]；
    - ``t_coord``:[x,y,z,rx,ry,rz] 工具中心点相对末端法兰中心位姿，单位[mm][°]；
    - ``type``:0-工具坐标系，1-传感器坐标系；
    - ``install``:安装位置，0-机器人末端，1-机器人外部
    - ``loadNum``:负载编号"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetToolList(10,t_coord,0,0,0)
    print("设置工具坐标系列表错误码",error)

设置外部工具参考点-三点法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExTCPPoint(point_num)``"
    "描述", "设置外部工具参考点-三点法"
    "必选参数", "- ``point_num``：点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    for i in range(1,4):
        error = robot.SetExTCPPoint(i) #应当控制机器人按照要求移动到合适位置后再发送指令
        print("三点法设置外部工具坐标系，记录点",i,"错误码",error)
        time.sleep(1)
    error,etcp = robot.ComputeExTCF()
    print("三点法设置外部工具坐标系错误码",error,"外部工具TCP",etcp)
    error = robot.SetExToolCoord(10,etcp,etool)
    print("设置外部工具坐标系错误码",error)
    error = robot.SetExToolList(10,etcp,etool)
    print("设置外部工具坐标系列表错误码",error)

计算外部工具坐标系-三点法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeExTCF (point_num)``"
    "描述", "计算外部工具坐标系-三点法（设置完三个参考点后再进行计算）"
    "必选参数", "``point_num``：点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``etcp=[x,y,z,rx,ry,rz]``：外部工具坐标系"

设置外部工具坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolCoord(id,etcp,etool)``"
    "描述", "设置外部工具坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``etcp``:外部工具坐标系，单位[mm][°]；
    - ``etool``:末端工具坐标系，单位[mm][°]；"
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
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    error = robot.SetExToolCoord(10,etcp,etool)
    print("设置外部工具坐标系错误码",error)

设置外部工具坐标系列表
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolList(id,etcp ,etool)``"
    "描述", "设置外部工具坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``etcp``:外部工具坐标系，单位[mm][°]；
    - ``etool``:末端工具坐标系，单位[mm][°]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    error = robot.SetExToolList(10,etcp,etool)
    print("设置外部工具坐标系列表错误码",error)

设置工件参考点-三点法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoordPoint(point_num)``"
    "描述", "设置工件参考点-三点法"
    "必选参数", "``point_num``:点编号,范围[1~3]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    robot.SetToolList(0,[0,0,0,0,0,0],0,0)#设置参考点前应当将工具和工件号坐标系切换至0
    robot.SetWObjList(0,[0,0,0,0,0,0])
    for i in range(1,4):
        error = robot.SetWObjCoordPoint(i) #实际应当控制机器人按照要求移动到合适位置后再发送指令
        print("三点法设置工件坐标系，记录点",i,"错误码",error)
        time.sleep(1)
    error, w_coord = robot.ComputeWObjCoord(0,0)
    print("三点法计算工件坐标系错误码",error,"工件坐标系", w_coord)

计算工件坐标系-三点法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoord(method, refFrame)``"
    "描述", "计算工件坐标系-三点法（三个参考点设置完成后再进行计算）;"
    "必选参数", "- ``method``：计算方式0：原点-x轴-z轴，1：原点-x轴-xy平面
    - ``refFrame``：参考坐标系"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``wobj_pose=[x,y,z,rx,ry,rz]``：工件坐标系"


设置工件坐标系
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoord(id, coord, refFrame)``"
    "描述", "设置工件坐标系"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``coord``:工件坐标系相对于末端法兰中心位姿，单位 [mm][°]
    - ``refFrame``:参考坐标系"
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
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    error = robot.SetWObjCoord(id=11,coord=w_coord,refFrame=0)
    print("设置工件坐标系错误码",error)

设置工件坐标系列表
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjList(id, coord, refFrame)``"
    "描述", "设置工件坐标系列表"
    "必选参数", "- ``id``:坐标系编号，范围[0~14]；
    - ``coord``:工件坐标系相对于末端法兰中心位姿，单位 [mm][°]
    - ``refFrame``:参考坐标系"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    error = robot.SetWObjList(id=11,coord=w_coord,refFrame=0)
    print("设置工件坐标系列表错误码",error)

设置末端负载重量
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadWeight(weight)``"
    "描述", "设置末端负载重量,错误负载重量设置可能会导致拖动模式下机器人失控"
    "必选参数", "- ``weight``:单位[kg]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetLoadWeight(0)#！！！负载重量设置应于实际相符(错误负载重量设置可能会导致拖动模式下机器人失控)

设置机器人安装方式-固定安装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallPos(method)``"
    "描述", "设置机器人安装方式-固定安装,错误安装方式设置会导致拖动模式下机器人失控"
    "必选参数", "- ``method``:0-平装，1-侧装，2-挂装"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetRobotInstallPos(0) #！！！安装方式设置应与实际一致 0-正装，1-侧装，2-倒装 (错误安装方式设置会导致拖动模式下机器人失控）
    print("设置机器人安装方式错误码",error)

设置机器人安装角度-自由安装
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallAngle(yangle,zangle)``"
    "描述", "设置机器人安装角度-自由安装,错误安装角度设置会导致拖动模式下机器人失控"
    "必选参数", "- ``yangle``：倾斜角
    - ``zangle``：旋转角"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetRobotInstallAngle(0.0,0.0) #！！！安装角度设置应与实际一致 (错误安装角度设置会导致拖动模式下机器人失控）
    print("设置机器人安装角度错误码",error)

设置末端负载质心坐标
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadCoord(x,y,z)``"
    "描述", "设置末端负载质心坐标,错误负载质心设置可能会导致拖动模式下机器人失控"
    "必选参数", "- ``x``: 质心坐标，单位[mm]
    - ``y``: 质心坐标，单位[mm]
    - ``z``: 质心坐标，单位[mm]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetLoadCoord(3.0,4.0,5.0) #！！！负载质心设置应于实际相符(错误负载质心设置可能会导致拖动模式下机器人失控)
    print("设置负载质心错误码",error)

等待指定时间
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMs(t_ms)``"
    "描述", "等待指定时间"
    "必选参数", "- ``t_ms``:单位[ms]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.WaitMs(1000)
    print("等待指定时间错误码",error)

设置机器人加速度
+++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOaccScale(acc)``"
    "描述", "设置机器人加速度"
    "必选参数", "- ``acc``:机器人加速度百分比"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.SetOaccScale (20)

设置机器指定姿态速度开启
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedStart(ratio)``"
    "描述", "指定姿态速度开启"
    "必选参数", "- ``ratio``:姿态速度百分比[0-300]"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

指定姿态速度关闭
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedEnd()``"
    "描述", "指定姿态速度关闭"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "