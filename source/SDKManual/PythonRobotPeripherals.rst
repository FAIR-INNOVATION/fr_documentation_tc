机器人外设
============

.. toctree:: 
    :maxdepth: 5

获取夹爪配置
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperConfig()``"
    "描述", "获取夹爪配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[number,company,device,softversion]``： number，夹爪编号;company，夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行 ;device，设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20);softvesion，软件版本号，暂不使用，默认为0。"

激活夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ActGripper(index,action)``"
    "描述", "激活夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``action``:0-复位，1-激活"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

控制夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "描述", "控制夹爪"
    "必选参数", "- ``index``:夹爪编号；
    - ``pos``:位置百分比，范围[0~100]；
    - ``vel``:速度百分比，范围[0~100];
    - ``force``:力矩百分比，范围[0~100]；
    - ``maxtime``:最大等待时间，范围[0~30000]，单位[ms]；
    - ``block``:0-阻塞，1-非阻塞；
    - ``type``:夹爪类型，0-平行夹爪；1-旋转夹爪；
    - ``rotNum``:rotNum 旋转圈数；
    - ``rotVel``:旋转速度百分比[0-100]；
    - ``rotTorque``:旋转力矩百分比[0-100]。"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取夹爪运动状态
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperMotionDone()``"
    "描述", "获取夹爪运动状态"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``[fault,status]``：夹爪运动状态，fault:0-无错误，1-有错误；status:0-运动未完成，1-运动完成"

配置夹爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "描述", "配置夹爪"
    "必选参数", "- ``company``：夹爪厂商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行；
    - ``device``：设备号，Robotiq(0-2F-85系列)，慧灵(0-NK系列,1-Z-EFG-100)，天机(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)"
    "默认参数", "- ``softversion``：软件版本号，暂不使用，默认为0；
    - ``bus``：设备挂载末端总线位置，暂不使用，默认为0；"
    "返回值", "错误码 成功-0  失败- errcode "

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    desc_pos1=[-333.683,-228.968,404.329,-179.138,-0.781,91.261]
    desc_pos2=[-333.683,-100.8,404.329,-179.138,-0.781,91.261]
    zlength1 =10
    zlength2 =15
    zangle1 =10
    zangle2 =15
    #测试外设指令
    ret = robot.SetGripperConfig(4,0)  #配置夹爪
    print("配置夹爪错误码", ret)
    time.sleep(1)
    config = robot.GetGripperConfig()     #获取夹爪配置
    print("获取夹爪配置",config)
    error = robot.ActGripper(1,0)  #激活夹爪
    print("激活夹爪错误码",error)
    time.sleep(1)
    error = robot.ActGripper(1,1)#激活夹爪
    print("激活夹爪错误码",error)
    time.sleep(2)
    error = robot.MoveGripper(1,100,48,46,30000,0,0,0,0,0) #控制夹爪
    print("控制夹爪错误码",error)
    time.sleep(3)
    error = robot.MoveGripper(1,0,50,0,30000,0,0,0,0,0) #控制夹爪
    print("控制夹爪错误码",error)
    error = robot.GetGripperMotionDone() #获取夹爪运动状态
    print("获取夹爪运动状态错误码",error)
    error = robot.ComputePrePick(desc_pos1, zlength1, zangle1) #计算预抓取点-视觉
    print("计算预抓取点",error)
    error = robot.ComputePrePick(desc_pos2, zlength2, zangle2) #计算撤退点-视觉
    print("计算撤退点",error)

计算预抓取点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "描述", "计算预抓取点-视觉"
    "必选参数", "- ``desc_pos``：夹抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``pre_pos``：预抓取点笛卡尔位姿"

计算撤退点-视觉
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "描述", "计算撤退点-视觉"
    "必选参数", "- ``desc_pos``：抓取点笛卡尔位姿;
    - ``zlength``：z轴偏移量;
    - ``zangle``：绕z轴旋转偏移量"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``post_pos``：撤退点笛卡尔位姿"

设置启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "设置启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode "

获取启用夹爪动作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "获取启用夹爪动作控制功能"
    "必选参数", "- ``id``：夹爪设备编号"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩,12-15预留"