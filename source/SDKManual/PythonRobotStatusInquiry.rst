机器人状态查询
===============

.. toctree:: 
    :maxdepth: 5

获取机器人安装角度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotInstallAngle()``"
    "描述", "获取机器人安装角度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[yangle,zangle]``：yangle-倾斜角,zangle-旋转角"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotInstallAngle()
    print("获取机器人安装角度", ret)

获取系统变量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSysVarValue(id)``"
    "描述", "获取系统变量值"
    "必选参数", "- ``id``：系统变量编号，范围[1~20]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``var_value``：系统变量值"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1,21):
        error = robot.GetSysVarValue(i)
        print("系统变量编号:",i,"值", error)

获取当前关节位置(角度)
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosDegree(flag=1)``"
    "描述", "获取关节当前位置(角度)"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞，默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：当前关节位置(角度)"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointPosDegree()
    print("获取当前关节位置 (角度)", ret)

获取当前关节位置(弧度)
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosRadian(flag=1)``"
    "描述", "获取关节当前位置(弧度)"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：当前关节位置(弧度)"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointPosRadian()
    print("获取当前关节位置 (弧度)", ret)

获取关节反馈速度-deg/s
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointSpeedsDegree (flag=1)``"
    "描述", "获取关节反馈速度-deg/s"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[j1,j2,j3,j4,j5,j6]``：关节反馈速度-deg/s"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointSpeedsDegree()
    print("获取关节反馈速度-deg/s", ret)

获取TCP指令合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPCompositeSpeed(flag=1)``"
    "描述", "获取TCP指令合速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetTCPCompositeSpeed()
    print("获取TCP指令合速度", ret)

获取TCP反馈合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPCompositeSpeed(flag=1)``"
    "描述", "获取TCP反馈合速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPCompositeSpeed()
    print("获取TCP反馈合速度", ret)

获取TCP指令速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPSpeed(flag=1)``"
    "描述", "获取TCP指令速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP指令速度，mm/s"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetTCPSpeed()
    print("获取TCP指令速度", ret)

获取TCP反馈速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPSpeed(flag=1)``"
    "描述", "获取TCP反馈速度"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP反馈速度"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPSpeed()
    print("获取TCP反馈速度", ret)

获取当前工具位姿
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPPose(flag=1)``"
    "描述", "获取当前工具位姿"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：当前工具位姿"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPPose()
    print("获取当前工具位姿", ret)

获取当前工具坐标系编号
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPNum(flag=1)``"
    "描述", "获取当前工具坐标系编号"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞 默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tool_id``:工具坐标系编号"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPNum()
    print("获取当前工具坐标系编号", ret)

获取当前工件坐标系编号
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualWObjNum(flag=1)``"
    "描述", "获取当前工件坐标系编号"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``wobj_id``:工件坐标系编号"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualWObjNum()
    print("获取当前工件坐标系编号", ret)

获取当前末端法兰位姿
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualToolFlangePose(flag=1)``"
    "描述", "获取当前末端法兰位姿"
    "必选参数", "无"
    "默认参数", "- ``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``flange_pose=[x,y,z,rx,ry,rz]``：当前末端法兰位姿"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualToolFlangePose()
    print("获取当前末端法兰位姿", ret)

逆运动学求解
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKin(type,desc_pos,config=-1)``"
    "描述", "逆运动学，笛卡尔位姿求解关节位置 "
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pose``:[x,y,z,rx,ry,rz],工具位姿，单位[mm][°]"
    "默认参数", "- ``config``:关节配置，[-1]-参考当前关节位置求解，[0~7]-依据关节配置求解 默认-1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆运动学解，笛卡尔位姿求解关节位置"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKin(0,P1,config=-1)
    print("逆运动学，笛卡尔位姿求解关节位置", ret)

逆运动学求解-指定参考位置
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinRef(type,desc_pos,joint_pos_ref)``"
    "描述", "逆运动学，工具位姿求解关节位置，参考指定关节位置求解"
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，单位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，关节参考位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆运动学解，工具位姿求解关节位置"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKinRef(0,P1,J1)
    print("逆运动学，工具位姿求解关节位置，参考指定关节位置求解", ret)

逆运动学求解-是否有解
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinHasSolution(type,desc_pos,joint_pos_ref)``"
    "描述", "逆运动学，工具位姿求解关节位置 是否有解"
    "必选参数", "- ``type``:0-绝对位姿(基坐标系)，1-相对位姿（基坐标系），2-相对位姿（工具坐标系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，单位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，关节参考位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``result``:“True”-有解，“False”-无解"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKinHasSolution(0,P1,J1)
    print("逆运动学，工具位姿求解关节位置是否有解", ret)

正运动学求解
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForwardKin(joint_pos)``"
    "描述", "正运动学，关节位置求解工具位姿"
    "必选参数", "- ``joint_pos``:[j1,j2,j3,j4,j5,j6]:关节位置，单位[°]"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``desc_pos=[x,y,z,rx,ry,rz]``：正运动学解，关节位置求解工具位姿"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    ret = robot.GetForwardKin(J1)
    print("正运动学，关节位置求解工具位姿", ret)

获取当前关节转矩
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointTorques(flag=1)``"
    "描述", "获取当前关节转矩"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``torques=[j1,j2,j3,j4,j5,j6]``：关节扭矩"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot 
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetJointTorques()
    print("获取当前关节转矩", ret)

获取当前负载的重量
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayload(flag=1)``"
    "描述", "获取当前负载的质量"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``weight``：当前负载重量，单位 [kg]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetPayload(0)
    print("获取当前负载的质量", ret)

获取当前负载的质心
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayloadCog(flag=1)``"
    "描述", "获取当前负载的质心"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``cog=[x,y,z]``: 当前质心坐标，单位 [mm]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetPayloadCog(0)
    print("获取当前负载的质心", ret)

获取当前工具坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTCPOffset(flag=1)``"
    "描述", "获取当前工具坐标系"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: 当前工具坐标系相对位姿，单位[mm][°]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTCPOffset()
    print("获取当前工具坐标系", ret)

获取当前工件坐标系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWObjOffset(flag=1)``"
    "描述", "获取当前工件坐标系"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞，默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: 当前工件坐标系相对位姿，单位[mm][°]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetWObjOffset()
    print("获取当前工件坐标系", ret)

获取关节软限位角度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointSoftLimitDeg(flag=1)``"
    "描述", "获取关节软限位角度"
    "必选参数", "无"
    "默认参数", "``flag``：0-阻塞，1-非阻塞  默认1"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[j1min,j1max,j2min,j2max,j3min,j3max, j4min,j4max,j5min, j5max, j6min,j6max]``：轴1~轴6，关节负限位与正限位，单位[mm]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetJointSoftLimitDeg()
    print("获取关节软限位角度", ret)

获取系统时间
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSystemClock()``"
    "描述", "获取系统时间"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``t_ms``: 系统时间，单位 [ms]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSystemClock()
    print("获取系统时间", ret)

获取机器人当前关节配置
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotCurJointsConfig()``"
    "描述", "获取机器人当前关节配置"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``config``: 机器人当前关节配置，范围 [0~7]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotCurJointsConfig()
    print("获取机器人当前关节配置", ret)

获取默认速度
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDefaultTransVel()``"
    "描述", "获取默认速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``vel``: 默认速度，单位 [mm/s]"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetDefaultTransVel()
    print("获取默认速度", ret)

查询机器人运动是否完成
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotMotionDone()``"
    "描述", "查询机器人运动是否完成"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``state``: 机器人运动状态，0-未完成，1-完成"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotMotionDone()
    print("查询机器人运动是否完成", ret)

查询机器人错误码
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotErrorCode()``"
    "描述", "查询机器人错误码"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[maincode subcode]``：机器人错误码，maincode-主错误码，subcode-子错误码"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotErrorCode()
    print("查询机器人错误码", ret)

查询机器人示教管理点位数据
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotTeachingPoint(name)``"
    "描述", "查询机器人示教管理点位数据"
    "必选参数", "``name``：点位名"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``[x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4]``：点位数据"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotTeachingPoint("11")
    print("查询机器人示教管理点位数据错误码", ret)

获取SSH公钥
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSSHKeygen()``"
    "描述", "获取SSH公钥"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``keygen``：公钥"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSSHKeygen() #获取SSH
    print("获取SSH", ret)

计算指定路径下文件的MD5值
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFileMD5(file_path)``"
    "描述", "计算指定路径下文件的MD5值"
    "必选参数", "- ``file_path``：文件路径包含文件名，默认Traj文件夹路径为:/fruser/traj/,如/fruser/traj/trajHelix_aima_1.txt"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``md5``：文件MD5值"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.ComputeFileMD5("/fruser/201.lua")   #计算指定路径下文件的MD5值
    print("计算指定路径下文件的MD5值", ret)

获取机器人版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareVersion()``"
    "描述", "获取机器人版本信息"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``robotModel``：机器人模型
    - ``webVersion``：web版本
    - ``controllerVersion``：控制器版本"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')

    ret = robot.GetSoftwareVersion()
    print("GetSoftwareVersion()：", ret)

获取机器人硬件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveHardVersion()``"
    "描述", "获取机器人硬件版本信息"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSlaveHardVersion()
    print("GetSlaveHardVersion()：", ret)

获取机器人固件版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveFirmVersion()``"
    "描述", "获取机器人固件版本信息"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

代码示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSlaveFirmVersion()
    print("GetSlaveFirmVersion()：", ret)

获取DH补偿参数
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDHCompensation()``"
    "描述", "获取DH补偿参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``dhCompensation=[cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]``：机器人DH参数补偿值(mm)"

代码示例
------------
.. code-block:: python
    :linenos:

    import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetDHCompensation()
    print(error)

获取关节驱动器当前扭矩
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTorque()``"
    "描述", "获取关节驱动器当前扭矩"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``data=[j1,j2,j3,j4,j5,j6]``：关节驱动器当前扭矩"

获取关节驱动器当前温度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTemperature()``"
    "描述", "获取关节驱动器当前温度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode 
    - ``data=[t1,t2,t3,t4,t5,t6]``：关节驱动器当前温度"