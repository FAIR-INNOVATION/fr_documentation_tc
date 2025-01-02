扩展轴
=============

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetParam(servoId,servoCompany,servoModel,servoSoftVersion, servoResolution,axisMechTransRatio)``"
    "描述", "设置485扩展轴参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')

    ret =robot.AuxServoSetParam(1,1,1,1,131072,15.45)#设置485扩展轴参数
    print("AuxServoSetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetParam(1)#获取485扩展轴配置参数
    print("AuxServoGetParam",ret)
    sleep(1)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret =robot.AuxServoClearError(1)#清除错误
    print("AuxServoClearError",ret)
    sleep(1)

获取485扩展轴配置参数
+++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetParam(servoId)``"
    "描述", "获取485扩展轴配置参数"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoCompany``：伺服驱动器厂商，1-戴纳泰克；
    - ``servoModel``：伺服驱动器型号，1-FD100-750C；
    - ``servoSoftVersion``：伺服驱动器软件版本，1-V1.0；
    - ``servoResolution``：编码器分辨率；
    - ``axisMechTransRatio``：机械传动比；"

代码示例
-----------
参考设置485扩展轴参数的代码示例

设置485扩展轴使能/去使能
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoEnable(servoId,status)``"
    "描述", "设置485扩展轴使能/去使能"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``status``：使能状态，0-去使能， 1-使能;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret =robot.AuxServoSetControlMode(1,0)#设置为位置模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式后需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)
    i=1
    while(i<5):
        ret =robot.AuxServoSetTargetPos(1,300*i,30)#位置模式运动，速度30
        print("AuxServoSetTargetPos",ret)
        sleep(11)
        ret =robot.AuxServoGetStatus(1)#查询状态
        print("AuxServoGetStatus",ret)
        sleep(1)
        i=i+1

设置485扩展轴控制模式
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetControlMode(servoId,mode)``"
    "描述", "设置485扩展轴控制模式"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：控制模式，0-位置模式，1-速度模式;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetPos(servoId,pos,speed)``"
    "描述", "设置485扩展轴目标位置(位置模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``pos``：目标位置，mm或°；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置485扩展轴目标速度(速度模式)
+++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetSpeed(servoId,speed)``"
    "描述", "设置485扩展轴目标速度(速度模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``speed``：目标速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
-------------

.. code-block:: python
    :linenos:

    from time import sleep
    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    ret = robot = Robot.RPC('192.168.58.2')
    ret =robot.AuxServoEnable(1,0)#修改控制模式前需去使能
    print("AuxServoEnable(0)",ret)
    sleep(3)

    ret = robot.AuxServoSetControlMode(1, 1)  # 设置为速度模式
    print("AuxServoSetControlMode",ret)
    sleep(3)

    ret =robot.AuxServoEnable(1,1)#修改控制模式后需使能
    print("AuxServoEnable(1)",ret)
    sleep(3)

    ret =robot.AuxServoHoming(1,1,10,10)#回零
    print("AuxServoHoming",ret)
    sleep(5)

    ret =robot.AuxServoGetStatus(1)#查询状态
    print("AuxServoGetStatus",ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 30)  # 速度模式运动，速度30
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)

    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 60)  # 速度模式运动，速度60
    print("AuxServoSetTargetSpeed", ret)
    sleep(10)
    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

    ret = robot.AuxServoSetTargetSpeed(1, 0)  # 结束速度模式运动前应当把速度设为0
    print("AuxServoSetTargetSpeed", ret)
    sleep(3)
    ret = robot.AuxServoGetStatus(1)  # 查询状态
    print("AuxServoGetStatus", ret)
    sleep(1)

设置485扩展轴目标转矩(力矩模式)-暂未开放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetTargetTorque(servoId,torque)``"
    "描述", "设置485扩展轴目标转矩(力矩模式)"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``torque``：目标力矩，Nm;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoHoming(servoId,mode,searchVel,latchVel)``"
    "描述", "设置485扩展轴回零"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；
    - ``mode``：回零模式，1-当前位置回零；2-负限位回零；3-正限位回零;
    - ``searchVel``： 回零速度，mm/s或°/s;
    - ``latchVel``：箍位速度，mm/s或°/s;"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoClearError(servoId)``"
    "描述", "清除485扩展轴错误信息"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
代码示例
---------------------------------
参考设置485扩展轴参数的代码示例

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetStatus(servoId)``"
    "描述", "获取485扩展轴伺服状态"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``servoErrCode``：伺服驱动器故障码
    - ``servoState``：伺服驱动器状态 bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成；
    - ``servoPos``：伺服当前位置 mm或°；
    - ``servoSpeed``：伺服当前速度 mm/s或°/s；
    - ``servoTorque``：伺服当前转矩Nm；"

代码示例
---------------------------------
参考设置485扩展轴使能/去使能的代码示例

设置状态反馈中485扩展轴数据轴号-暂未开放
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServosetStatusID(servoId)``"
    "描述", "设置状态反馈中485扩展轴数据轴号"
    "必选参数", "- ``servoId``：伺服驱动器ID，范围[1-15],对应从站ID；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetAcc(acc, dec)``"
    "描述", "设置485扩展轴运动加减速度"
    "必选参数", "- ``acc``：485扩展轴运动加速度
    - ``dec``：485扩展轴运动减速度"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

设置485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoSetEmergencyStopAcc(acc, dec)``"
    "描述", "设置485扩展轴急停加减速度"
    "必选参数", "- ``acc``：485扩展轴急停加速度
    - ``dec``：485扩展轴急停减速度"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

获取485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetEmergencyStopAcc()``"
    "描述", "获取485扩展轴急停加减速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``acc``：485扩展轴急停加速度
    - ``dec``：485扩展轴急停减速度"

获取485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AuxServoGetAcc()``"
    "描述", "获取485扩展轴运动加减速度"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode
    - ``acc``：485扩展轴运动加速度
    - ``dec``：485扩展轴运动减速度"

UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevSetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum)``"
    "描述", "UDP扩展轴通讯参数配置"
    "必选参数", "
    - ``ip``：PLC IP地址；
    - ``port``：端口号；
    - ``period``：通讯周期(ms，暂不开放)；
    - ``lossPkgTime``：丢包检测时间(ms)；
    - ``lossPkgNum``：丢包次数；
    - ``disconnectTime``：通讯断开确认时长；
    - ``reconnectEnable``：通讯断开自动重连使能 0-不使能 1-使能；
    - ``reconnectPeriod``：重连周期间隔(ms)；
    - ``reconnectNum``：重连次数"
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
    #UDP扩展轴通讯参数配置
    error = robot.ExtDevSetUDPComParam('192.168.58.88',2021,2,50,5,50,1,2,5)
    print("ExtDevSetUDPComParam return:",error)
    #UDP扩展轴通讯参数配置
    error = robot.ExtDevGetUDPComParam()
    print("ExtDevGetUDPComParam return:",error)
    
获取UDP扩展轴通讯参数
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevGetUDPComParam()``"
    "描述", "获取UDP扩展轴通讯参数"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "
    - 错误码 成功-0  失败- errcode；
    - ``ip``：PLC IP地址；
    - ``port``：端口号；
    - ``period``：通讯周期(ms，暂不开放)；
    - ``lossPkgTime``：丢包检测时间(ms)；
    - ``lossPkgNum``：丢包次数；
    - ``disconnectTime``：通讯断开确认时长；
    - ``reconnectEnable``：通讯断开自动重连使能 0-不使能 1-使能；
    - ``reconnectPeriod``：重连周期间隔(ms)；
    - ``reconnectNum``：重连次数"
 
加载UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevLoadUDPDriver()``"
    "描述", "加载UDP通信"
    "必选参数", "无"
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
    #加载UDP通信
    error = robot.ExtDevLoadUDPDriver()
    print("ExtDevLoadUDPDriver return:",error)
    #卸载UDP通信
    error = robot.ExtDevUnloadUDPDriver()
    print("ExtDevUnloadUDPDriver return:",error)
     
卸载UDP通信
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUnloadUDPDriver()``"
    "描述", "卸载UDP通信"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
     
UDP扩展轴通信异常断开后恢复连接
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComReset()``"
    "描述", "UDP扩展轴通信异常断开后恢复连接"
    "必选参数", "无"
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
    #UDP扩展轴通信异常断开后恢复连接
    error = robot.ExtDevUDPClientComReset()
    print("ExtDevUDPClientComReset return:",error)
    #UDP扩展轴通信异常断开后关闭通讯
    error = robot.ExtDevUDPClientComClose()
    print("ExtDevUDPClientComClose return:",error)
         
UDP扩展轴通信异常断开后关闭通讯
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtDevUDPClientComClose()``"
    "描述", "UDP扩展轴通信异常断开后关闭通讯"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
         
设置扩展机器人相对扩展轴位置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotPosToAxis(installType)``"
    "描述", "设置扩展机器人相对扩展轴位置"
    "必选参数", "- ``installType``：0-机器人安装在外部轴上，1-机器人安装在外部轴外；"
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
    #设置扩展机器人相对扩展轴位置
    error = robot.SetRobotPosToAxis(1)
    print("SetRobotPosToAxis return:",error)
    #设置扩展轴系统DH参数配置
    error = robot.SetAxisDHParaConfig(4,128.5,206.4,0,0,0,0,0,0,)
    print("SetAxisDHParaConfig return:",error)
    #UDP扩展轴参数配置
    error = robot.ExtAxisParamConfig(1,1,0,1000,-1000,1000,1000,1.905,262144, 200,1,1,0)
    print("ExtAxisParamConfig return:",error)

设置扩展轴系统DH参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxisDHParaConfig(axisConfig,axisDHd1,axisDHd2,axisDHd3,axisDHd4,axisDHa1, axisDHa2,axisDHa3,axisDHa4)``"
    "描述", "设置扩展轴系统DH参数配置"
    "必选参数", "
    - ``axisConfig``：外部轴构型，0-单自由度直线滑轨，1-两自由度L型变位机，2-三自由度，3-四自由度，4-单自由度变位机；
    - ``axisDHd1``：外部轴DH参数d1 mm；
    - ``axisDHd2``：外部轴DH参数d2 mm；
    - ``axisDHd3``：外部轴DH参数d3 mm；
    - ``axisDHd4``：外部轴DH参数d4 mm；
    - ``axisDHa1``：外部轴DH参数a1 mm；
    - ``axisDHa2``：外部轴DH参数a2 mm；
    - ``axisDHa3``：外部轴DH参数a3 mm；
    - ``axisDHa4``：外部轴DH参数a4 mm；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴参数配置
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisParamConfig(axisId, axisType, axisDirection, axisMax, axisMin, axisVel, axisAcc,axisLead, encResolution, axisOffect, axisCompany, axisModel, axisEncType)``"
    "描述", "UDP扩展轴参数配置"
    "必选参数", "
    - ``axisId``：轴号[1-4]；
    - ``axisType``：扩展轴类型 0-平移；1-旋转；
    - ``axisDirection``：扩展轴方向 0-正向；1-反向；
    - ``axisMax``：扩展轴最大位置 mm；
    - ``axisMin``：扩展轴最小位置 mm；
    - ``axisVel``：速度mm/s；
    - ``axisAcc``：加速度mm/s2；
    - ``axisLead``：导程mm；
    - ``encResolution``：编码器分辨率；
    - ``axisOffect``：焊缝起始点扩展轴偏移量；
    - ``axisCompany``：驱动器厂家 1-禾川；2-汇川；3-松下；
    - ``axisModel``：驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG；
    - ``axisEncType``：编码器类型  0-增量；1-绝对值；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
         
设置扩展轴坐标系参考点-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetRefPoint(pointNum)``"
    "描述", "设置扩展轴坐标系参考点-四点法"
    "必选参数", "- ``pointNum``：点编号[1-4]；"
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
    #设置扩展轴坐标系参考点-四点法
    error = robot.ExtAxisSetRefPoint(1)
    print("ExtAxisComputeECoordSys(1) return:",error)
             
计算扩展轴坐标系-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisComputeECoordSys()``"
    "描述", "计算扩展轴坐标系-四点法"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``coord``：扩展轴坐标系值[x,y,z,rx,ry,rz]；"
                  
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #计算扩展轴坐标系-四点法
    error,coord = robot.ExtAxisComputeECoordSys()
    print("ExtAxisComputeECoordSys() return:",error,coord)
    #应用扩展轴坐标系
    error = robot.ExtAxisActiveECoordSys(1,1,coord,1)
    print("ExtAxisActiveECoordSys() return:",error)
         
应用扩展轴坐标系
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisActiveECoordSys(applyAxisId,axisCoordNum,coord,calibFlag)``"
    "描述", "应用扩展轴坐标系"
    "必选参数", "
    - ``applyAxisId``:扩展轴编号 bit0-bit3对应扩展轴编号1-4，如应用扩展轴1和3，则是 0b 0000 0101,也就是5；
    - ``axisCoordNum``：扩展轴坐标系编号；
    - ``coord``：坐标系值[x,y,z,rx,ry,rz]；
    - ``calibFlag``：标定标志 0-否，1-是；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
             
设置标定参考点在变位机末端坐标系下位姿
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRefPointInExAxisEnd(pos)``"
    "描述", "设置标定参考点在变位机末端坐标系下位姿"
    "必选参数", "- ``pos``：位姿值[x,y,z,rx,ry,rz]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
                      
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #设置标定参考点在变位机末端坐标系下位姿
    error = robot.SetRefPointInExAxisEnd(desc_pos)
    print("SetRefPointInExAxisEnd(1) return:",error)
                 
变位机坐标系参考点设置-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorSetRefPoint(pointNum)``"
    "描述", "变位机坐标系参考点设置-四点法"
    "必选参数", "- ``pointNum``：点编号[1-4]；"
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
    #变位机坐标系参考点设置-四点法
    error = robot.SetRefPointInExAxisEnd(desc_pos)
    print("SetRefPointInExAxisEnd(1) return:",error)
                     
变位机坐标系计算-四点法
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PositionorComputeECoordSys()``"
    "描述", "变位机坐标系计算-四点法"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode;
    - ``coord``：变位机坐标系值[x,y,z,rx,ry,rz]；"
                            
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #变位机坐标系计算-四点法
    error,coord = robot.PositionorComputeECoordSys()
    print("PositionorComputeECoordSys() return:",error,coord)
        
末端传感器寄存器写入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AxleSensorRegWrite(devAddr, regHAddr, regLAddr, regNum, data1, data2, isNoBlock)``"
    "描述", "末端传感器寄存器写入"
    "必选参数", "
    - ``devAddr``： 设备地址编号 0-255
    - ``regHAddr``：寄存器地址高8位
    - ``regLAddr``：寄存器地址低8位
    - ``regNum``：寄存器个数 0-255
    - ``data1``：写入寄存器数值1
    - ``data2``：写入寄存器数值2
    - ``isNoBlock``：0-阻塞；1-非阻塞
    "
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode；"
                          
UDP扩展轴使能
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisServoOn(axisID, status)``"
    "描述", "UDP扩展轴使能"
    "必选参数", "- ``axisID``：轴号[1-4]；
    - ``status``：0-去使能；1-使能；"
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
    #UDP扩展轴去使能
    error = robot.ExtAxisServoOn(1,0)
    print("ExtAxisServoOn return:",error)
    #UDP扩展轴使能
    error = robot.ExtAxisServoOn(1,1)
    print("ExtAxisServoOn return:",error)
    #UDP扩展轴回零
    error = robot.ExtAxisSetHoming(1,0,40,40)
    print("ExtAxisSetHoming return:",error)
    time.sleep(1)
    #UDP扩展轴点动开始
    error = robot.ExtAxisStartJog(1,1,20,20,20)
    print("ExtAxisStartJog return:",error)
    time.sleep(1)
    #UDP扩展轴点动停止
    error = robot.ExtAxisStopJog(1)
    print("ExtAxisStopJog return:",error)

UDP扩展轴回零
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSetHoming(axisID, mode, searchVel, latchVel)``"
    "描述", "UDP扩展轴回零"
    "必选参数", "
    - ``axisID``：轴号[1-4]；
    - ``mode``：回零方式 0当前位置回零，1负限位回零，2-正限位回零；
    - ``searchVel``：寻零速度(mm/s)；
    - ``latchVel``：寻零箍位速度(mm/s)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴点动开始
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStartJog( axisID, direction, vel, acc, maxDistance)``"
    "描述", "UDP扩展轴点动开始"
    "必选参数", "
    - ``axisID``：轴号[1-4]；
    - ``direction``：转动方向 0-反向；1-正向；
    - ``vel``：速度(mm/s)；
    - ``acc``：加速度(mm/s)；
    - ``maxDistance``：最大点动距离；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

UDP扩展轴点动停止
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisStopJog(axisID)``"
    "描述", "UDP扩展轴点动停止"
    "必选参数", "- ``axisID``：轴号[1-4]；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
    
设置扩展DO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDO(DONum,bOpen,smooth,block)``"
    "描述", "设置扩展DO"
    "必选参数", "
    - ``DONum``： DO编号；
    - ``bOpen``：开关 True-开,False-关；
    - ``smooth``：是否平滑 True -是, False -否；
    - ``block``：是否阻塞 True -是, False -否；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
                                    
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #设置扩展DO
    error = robot.SetAuxDO(1,True,False,True)
    print("GetAuxAI",error)
    #设置扩展AO
    error = robot.SetAuxAO(1,60,True)
    print("SetAuxAO",error)
    #设置扩展DI输入滤波时间
    error = robot.SetAuxDIFilterTime(10,False)
    print("SetAuxDIFilterTime",error)
    #设置扩展AI输入滤波时间
    error = robot.SetAuxAIFilterTime(10,True)
    print("SetAuxAIFilterTime",error)
    #等待扩展DI输入
    error = robot.WaitAuxDI(0,False,100,False)
    print("WaitAuxDI",error)
    #等待扩展AI输入
    error = robot.WaitAuxAI(0,0,100,500,False)
    print("WaitAuxAI",error)
    #获取扩展AI值
    error = robot.GetAuxAI(0,False)
    print("GetAuxAI",error)
    #获取扩展DI值
    error = robot.GetAuxDI(0,True)
    print("GetAuxDI",error)
        
设置扩展AO
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAO(AONum,value,block)``"
    "描述", "设置扩展AO"
    "必选参数", "
    - ``AONum``： AO编号；
    - ``value``：模拟量值[0-4095]；
    - ``block``：是否阻塞 True -是, False -否；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
设置扩展DI输入滤波时间
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxDIFilterTime(filterTime)``"
    "描述", "设置扩展DI输入滤波时间"
    "必选参数", "- ``filterTime``： 滤波时间(ms)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
设置扩展AI输入滤波时间
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAuxAIFilterTime(AINum,filterTime)``"
    "描述", "设置扩展AI输入滤波时间"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``filterTime``： 滤波时间(ms)；"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
等待扩展DI输入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxDI(DINum,bOpen,time,errorAlarm)``"
    "描述", "等待扩展DI输入"
    "必选参数", "
    - ``DINum``： DI编号；
    - ``bOpen``：开关 True-开,False-关；
    - ``time``：最大等待时间(ms)；
    - ``errorAlarm``：是否继续运动 True-是,False-否"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
等待扩展AI输入
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitAuxAI(,AINum,sign,value,time,errorAlarm)``"
    "描述", "等待扩展AI输入"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``sign``：0-大于；1-小于；
    - ``value``：AI值；
    - ``time``：最大等待时间(ms)；
    - ``errorAlarm``：是否继续运动 True-是,False-否"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"
        
获取扩展DI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxDI(DINum,isNoBlock)``"
    "描述", "获取扩展DI值"
    "必选参数", "
    - ``DINum``： DI编号；
    - ``isNoBlock``：是否阻塞 True-阻塞 false-非阻塞；"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode；
    - ``isOpen``： 0-关；1-开；"
          
获取扩展AI值
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAuxAI(AINum,isNoBlock)``"
    "描述", "获取扩展AI值"
    "必选参数", "
    - ``AINum``： AI编号；
    - ``isNoBlock``：是否阻塞 True-阻塞 False-非阻塞"
    "默认参数", "无"
    "返回值", "- 错误码 成功-0  失败- errcode；
    - ``value``：输入值；"
          
UDP扩展轴运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisMove(pos,ovl)``"
    "描述", "UDP扩展轴运动"
    "必选参数", "- ``pos=[exaxis[0],exaxis[1],exaxis[2],exaxis[3]]``：目标位置 轴1位置~轴4位置;
    - ``ovl``：速度百分比"
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
    error,joint_pos = robot.GetActualJointPosDegree()
    print("GetActualJointPosDegree",error,joint_pos)
    e_pos =[-10,0,0,0]
    joint_pos[0] = joint_pos[0]+30
    #UDP扩展轴异步运动
    error = robot.ExtAxisMove(e_pos,30)
    print("ExtAxisMove",error)
    print("joint_pos",joint_pos)
    error = robot.MoveJ(joint_pos,0,0,exaxis_pos=e_pos)
    print("MoveJ",error)
              
UDP扩展轴与机器人关节运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveJ(joint_pos,desc_pos,tool,user,exaxis_pos, vel=20.0, acc=0.0, ovl= 100.0,  blendT=-1.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP扩展轴与机器人关节运动同步运动"
    "必选参数", "
    - ``joint_pos``： 目标关节位置，单位 [°]；
    - ``desc_pos``：目标笛卡尔位姿，单位 [mm][°]
    - ``tool``：工具号，[0~14]
    - ``user``：工件号，[0~14]
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位"
    "默认参数", "
    - ``vel``： 速度百分比，[0~100] 默认20.0；
    - ``acc``：加速度百分比，[0~100] 暂不开放,默认0.0 ；
    - ``ovl``：速度缩放因子，[0~100] 默认100.0  ；
    - ``blendT``：[-1.0]-运动到位 (阻塞)，[0~500.0]-平滑时间 (非阻塞)，单位 [ms] 默认-1.0；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "返回值", "错误码 成功-0  失败- errcode；"
                                        
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    #1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
    point_num=1
    id=1
    coord=[100,200,300,0,0,0,]
    type=0
    install=0
    #1.设置工具坐标系
    # robot.SetToolPoint(point_num)  #设置工具参考点-六点法
    # robot.ComputeTool() #计算工具坐标系
    # robot.SetTcp4RefPoint()   #设置工具参考点-四点法
    # robot.ComputeTcp4()   #计算工具坐标系-四点法
    # robot.SetToolCoord(id, coord,type,install)  #设置应用工具坐标系
    # robot.SetToolList(id, coord,type,install)   #设置应用工具坐标系列表
    #2.设置UDP通信参数，并加载UDP通信
    robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
    robot.ExtDevLoadUDPDriver();
    #3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
    robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0)#单轴变位机及DH参数
    robot.SetRobotPosToAxis(1);  #扩展轴安装位置
    robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0)#伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数
    #4.设置所选的轴使能、回零
    robot.ExtAxisServoOn(1, 0);
    robot.ExtAxisSetHoming(1, 0, 20, 3);
    #5.进行扩展轴坐标系标定及应用(注意：变位机和直线滑轨的标定接口不同，以下时变位机的标定接口)
    pos =[0,0,0,0,0,0] #输入您的标定点坐标
    robot.SetRefPointInExAxisEnd(pos)
    robot.PositionorSetRefPoint(1)#您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定
    error,coord = robot.PositionorComputeECoordSys()#计算扩展轴标定结果
    robot.ExtAxisActiveECoordSys(1, 1, coord, 1); #将标定结果应用到扩展轴坐标系
    method=1
    #6.在扩展轴上标定工件坐标系，您需要用到以下接口
    # robot.SetWObjCoordPoint( point_num)
    # error,coord=robot.ComputeWObjCoord( method)
    # robot.SetWObjCoord(id,coord)
    # robot.SetWObjList(id, coord)
    #7.记录您的同步关节运动起始点
    startdescPose = [0,0,0,0,0,0]#输入您的坐标
    startjointPos = [0,0,0,0,0,0]#输入您的坐标
    startexaxisPos = [0,0,0,0,]#输入您的坐标
    #8.记录您的同步关节运动终点坐标
    enddescPose = [0,0,0,0,0,0]#输入您的坐标
    endjointPos = [0,0,0,0,0,0]#输入您的坐标
    endexaxisPos = [0,0,0,0,]#输入您的坐标
    #9.编写同步运动程序
    #运动到起始点，假设应用的工具坐标系、工件坐标系都是1
    robot.ExtAxisMove(startexaxisPos, 20);
    robot.MoveJ(startjointPos,  1, 1, desc_pos=startdescPose,exaxis_pos=startexaxisPos);
    #开始同步运动
    robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, endexaxisPos);
                  
UDP扩展轴与机器人直线运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveL(self, joint_pos,desc_pos, tool, user, exaxis_pos, vel=20.0, acc=0.0, ovl=100.0, blendR=-1.0, search=0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0])``"
    "描述", "UDP扩展轴与机器人直线运动同步运动"
    "必选参数", "
    - ``joint_pos``： 目标关节位置，单位 [°]；
    - ``desc_pos``：目标笛卡尔位姿，单位 [mm][°]；
    - ``tool``：工具号，[0~14]；
    - ``user``：工件号，[0~14]；
    - ``exaxis_pos``：外部轴 1 位置 ~ 外部轴 4 位；"
    "默认参数", "
    - ``vel``： 速度百分比，[0~100] 默认20.0；
    - ``acc``：加速度百分比，[0~100] 暂不开放,默认0.0；
    - ``ovl``：速度缩放因子，[0~100] 默认100.0；
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~500.0]-平滑时间 (非阻塞)，单位 [ms] 默认-1.0；
    - ``search``：[0]-不焊丝寻位，[1]-焊丝寻位；
    - ``offset_flag``：[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos``：位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0] ；"
    "返回值", "错误码 成功-0  失败- errcode；"
                                            
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.Mode(0)
    time.sleep(1)
    e_pos =[-20,0,0,0]
    joint_pos0 = [114.089,-85.740, 119.106,-129.884,-91.655, 79.642]
    desc_pos0= [-87.920,-178.539,-64.513,-175.471,7.664,139.650]
    #UDP扩展轴与机器人直线运动同步运动
    error = robot.ExtAxisSyncMoveL(joint_pos0,desc_pos0,1,1,e_pos)
    print("ExtAxisSyncMoveL",error)
                      
UDP扩展轴与机器人圆弧运动同步运动
++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ExtAxisSyncMoveC(joint_pos_p, desc_pos_p, tool_p, user_p,exaxis_pos_p, joint_pos_t, desc_pos_t, tool_t, user_t,exaxis_pos_t,vel_p=20.0, acc_p=100.0, offset_flag_p=0, offset_pos_p =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=100.0, offset_flag_t=0, offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ovl=100.0, blendR=-1.0)``"
    "描述", " UDP扩展轴与机器人圆弧运动同步运动"
    "必选参数", "
    - ``joint_pos_p``： 路径点关节位置，单位 [°] ；
    - ``desc_pos_p``：路径点笛卡尔位姿，单位 [mm][°]；
    - ``tool_p``：路径点工具号，[0~14]；
    - ``user_p``：路径点工件号，[0~14]；
    - ``exaxis_pos_p``：路径点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]；
    - ``joint_pos_t``：目标点关节位置，单位 [°] ；
    - ``desc_pos_t``：目标点笛卡尔位姿，单位 [mm][°]；
    - ``tool_t``：工具号，[0~14]；
    - ``user_t``：工件号，[0~14]；
    - ``exaxis_pos_t``：目标点外部轴 1 位置 ~ 外部轴 4 位置 默认[0.0,0.0,0.0,0.0]；"
    "默认参数", "
    - ``vel_p``: 路径点速度百分比，[0~100] 默认20.0；
    - ``acc_p``: 路径点加速度百分比，[0~100] 暂不开放,默认0.0 ；   
    - ``offset_flag_p``: 路径点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos_p``: 路径点位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``vel_t``: 目标点速度百分比，[0~100] 默认20.0；
    - ``acc_t``: 目标点加速度百分比，[0~100] 暂不开放 默认0.0；
    - ``offset_flag_t``: 目标点是否偏移[0]-不偏移，[1]-工件/基坐标系下偏移，[2]-工具坐标系下偏移 默认 0；
    - ``offset_pos_t``: 目标点位姿偏移量，单位 [mm][°] 默认[0.0,0.0,0.0,0.0,0.0,0.0]；
    - ``ovl``: 速度缩放因子，[0~100] 默认100.0；
    - ``blendR``：[-1.0]-运动到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，单位 [mm] 默认-1.0；"
    "返回值", "错误码 成功-0  失败- errcode；"
                                                
代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.Mode(0)
    time.sleep(1)
    desc_pos_mid =[-131.2748107910156, -60.21242523193359, -22.55266761779785, 175.9907989501953, 5.92541742324829, 145.5211791992187]
    desc_pos_end =[-91.3530502319336, -174.5040588378906, -64.93866729736328, 177.1370544433593, 15.96347618103027, 136.1746368408203]
    joint_pos_mid = [120.9549040841584, -109.8869943146658, 134.1448068146658, -126.2150709699876, -88.6738087871287, 79.6419593131188]
    joint_pos_end =[110.1896078279703, -89.01601659189356, 125.5532806698638, -139.7967831451114, -82.93198387221534, 79.6452225788985]
    # #UDP扩展轴与机器人圆弧运动同步运动
    time.sleep(3)
    error = robot.ExtAxisSyncMoveC(joint_pos_mid,desc_pos_mid,1,1,[-10,0,0,0],joint_pos_end,desc_pos_end,1,1,[-20,0,0,0])
    print("ExtAxisSyncMoveC",error)

可移动装置控制
+++++++++++++++++
.. versionadded:: python SDK-v2.0.5

可移动装置使能
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorEnable(enable)``"
    "描述", "可移动装置使能"
    "必选参数", "- ``enable``：使能状态，0-去使能，1-使能"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置回零
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorHoming()``"
    "描述", "可移动装置回零"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置直线运动
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveL(distance, vel)``"
    "描述", "可移动装置直线运动"
    "必选参数", "- ``distance``：直线运动距离（mm）
    - ``vel``：直线运动速度百分比（0-100）"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置圆弧运动
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``TractorMoveC(radio, angle, vel)``"
    "描述", "可移动装置圆弧运动"
    "必选参数", "- ``radio``：圆弧运动半径（mm）
    - ``angle``：圆弧运动角度（°）
    - ``vel``：圆弧运动速度百分比（0-100）"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

可移动装置停止运动
---------------------------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ProgramStop()``"
    "描述", "可移动装置停止运动"
    "必选参数", "无"
    "默认参数", "无"
    "返回值", "错误码 成功-0  失败- errcode"

代码示例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10)
    robot.ExtDevLoadUDPDriver()
    robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0)
    robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0)

    robot.TractorEnable(False)
    time.sleep(2)
    robot.TractorEnable(True)
    time.sleep(2)
    robot.TractorHoming()
    time.sleep(2)
    robot.TractorMoveL(100, 20)
    time.sleep(5)
    robot.TractorMoveL(-100, 20)
    time.sleep(5)
    robot.TractorMoveC(300, 90, 20)
    time.sleep(4)
    error = robot.TractorStop()
    print("TractorStop return ", error)