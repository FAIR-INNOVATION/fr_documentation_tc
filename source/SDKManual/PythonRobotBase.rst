机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RPC(ip)``"
    "描述", "实例化一个机器人对象"
    "必选参数", "- ``ip``：机器人的IP地址，默认出厂IP为“192.168.58.2”"
    "默认参数", "无"
    "返回值", "- 成功：返回一个机器人对象
    - 失败：创建的对象会被销毁"
     
代码示例
--------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

关闭RPC连接
++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CloseRPC()``"
    "描述", "关闭RPC连接"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "无"
     
代码示例
--------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.CloseRPC()

查询SDK版本号
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSDKVersion()``"
    "描述", "查询SDK版本号"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败-errcode
    - ``sdk``：SDK版本号、控制器版本号"

代码示例
-----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret,version  = robot.GetSDKVersion()    #查询SDK版本号
    if ret ==0:
        print("SDK版本号为", version )
    else:
        print("查询失败，错误码为",ret)

获取控制器IP
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetControllerIP()``"
    "描述", "查询控制器IP"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ip``：控制器IP"

代码示例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret,ip = robot.GetControllerIP()    #查询控制器IP
    if ret ==0:
        print("控制器IP为", ip)
    else:
        print("查询失败，错误码为",ret)

控制机器人手自动模式切换
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Mode(state)``"
    "描述", "控制机器人手自动模式切换"
    "必选参数", "- ``state``：0-自动模式，1-手动模式"
    "默认参数", "无"
    "返回值", "错误码  成功-0  失败- errcode"

代码示例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #机器人手自动模式切换
    ret = robot.Mode(0)   #机器人切入自动运行模式
    print("机器人切入自动运行模式", ret)
    time.sleep(1)
    ret = robot.Mode(1)   #机器人切入手动模式
    print("机器人切入手动模式", ret)

机器人拖动模式
+++++++++++++++++

控制机器人进入或退出拖动示教模式
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DragTeachSwitch(state)``"
    "描述", "控制机器人进入或退出拖动示教模式"
    "必选参数", "- ``state``：1-进入拖动示教模式，0-退出拖动示教模式"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

查询机器人是否处于拖动模式
----------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``IsInDragTeach()``"
    "描述", "查询机器人是否处于拖动示教模式"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``：0-非拖动示教模式，1-拖动示教模式"

代码示例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #机器人手自动模式切换
    ret = robot.Mode(0)   #机器人切入自动运行模式
    print("机器人切入自动运行模式", ret)
    time.sleep(1)
    ret = robot.Mode(1)   #机器人切入手动模式
    print("机器人切入手动模式", ret)

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #机器人进入或退出拖动示教模式
    ret = robot.Mode(1) #机器人切入手动模式
    print("机器人切入手动模式", ret)
    time.sleep(1)
    ret = robot.DragTeachSwitch(1)  #机器人切入拖动示教模式，必须在手动模式下才能切入拖动示教模式
    print("机器人切入拖动示教模式", ret)
    time.sleep(1)
    ret,state = robot.IsInDragTeach()    #查询是否处于拖动示教模式，1-拖动示教模式，0-非拖动示教模式
    if ret == 0:
        print("当前拖动示教模式状态：", state)
    else:
        print("查询失败，错误码为：",ret)
    time.sleep(3)
    ret = robot.DragTeachSwitch(0)  #机器人切入非拖动示教模式，必须在手动模式下才能切入非拖动示教模式
    print("机器人切入非拖动示教模式", ret)
    time.sleep(1)
    ret,state = robot.IsInDragTeach()    #查询是否处于拖动示教模式，1-拖动示教模式，0-非拖动示教模式
    if ret == 0:
        print("当前拖动示教模式状态：", state)
    else:
        print("查询失败，错误码为：",ret)

控制机器人上使能或下使能
++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotEnable(state)``"
    "描述", "控制机器人上使能或下使能"
    "必选参数", "- ``state``：1-上使能，0-下使能"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
----------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #机器人上使能或下使能
    ret = robot.RobotEnable(0)   #机器人下使能
    print("机器人下使能", ret)
    time.sleep(3)
    ret = robot.RobotEnable(1)   #机器人上使能，机器人上电后默认自动上使能
    print("机器人上使能", ret)

关节扭矩功率检测
++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPowerLimit(status, power)``"
    "描述", "关节扭矩功率检测"
    "必选参数", "- ``state``：0-关闭，1-开启
    - ``power``：设定最大功率(W)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

设置机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateSamplePeriod(period)``"
    "描述", "设置机器人 20004 端口反馈周期"
    "必选参数", "- ``period``：机器人 20004 端口反馈周期(ms)"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealtimeStateSamplePeriod()``"
    "描述", "获取机器人 20004 端口反馈周期"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``period``：机器人 20004 端口反馈周期(ms)"

机器人软件升级
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SoftwareUpgrade(filePath, block)``"
    "描述", "机器人软件升级"
    "必选参数", "- ``filePath``：软件升级包全路径
    - ``block``：是否阻塞至升级完成 true:阻塞；false:非阻塞"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode "

获取机器人软件升级状态
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareUpgradeState()``"
    "描述", "获取机器人软件升级状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``state``：机器人软件包升级状态，0：空闲中或上传升级包中，1~100：升级完成百分比，-1：升级软件失败，-2：校验失败，-3：版本校验失败，-4：解压失败，-5：用户配置升级失败，-6：外设配置升级失败，-7：扩展轴配置升级失败，-8：机器人配置升级失败，-9：DH参数配置升级失败"

    