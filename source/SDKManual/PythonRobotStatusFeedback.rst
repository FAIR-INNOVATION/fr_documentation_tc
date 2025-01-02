状态反馈信息
==========================

.. toctree:: 
    :maxdepth: 5

状态反馈信息对照表
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.0.4
    
.. csv-table:: 
    :header-rows: 1
    :name: 状态反馈信息对照表
    :widths: 20 30

    "变量","含义"
    "program_state","程序运行状态，1-停止；2-运行；3-暂停"
    "robot_state","机器人运动状态，1-停止；2-运行；3-暂停；4-拖动"
    "main_code","主故障码"
    "sub_code",	子故障码"
    "robot_mode","机器人模式，0-自动模式；1-手动模式"
    "jt_cur_pos[i]","关节当前位置,单位deg,i:0~5"
    "tl_cur_pos[i]","工具当前位姿,单位deg&mm,i:0~5"
    "flange_cur_pos[i]","末端法兰当前位姿,单位deg&mm,i:0~5"
    "actual_qd[i]","机器人当前关节速度,单位deg/s^2,i:0~5"
    "actual_qdd[i]","机器人当前关节加速度,单位mm/s,i:0~5"
    "target_TCP_CmpSpeed[i]","机器人TCP合成指令速度,单位mm/s&deg/s,i:0~1"
    "target_TCP_Speed[i]","机器人TCP指令速度,单位mm/s&deg/s,i:0~5"
    "actual_TCP_CmpSpeed[i]","机器人TCP合成实际速度,单位mm/s&deg/s,i:0~1"
    "actual_TCP_Speed[i]","机器人TCP实际速度,单位mm/s&deg/s,i:0~5"
    "jt_cur_tor[i]","当前扭矩,单位N·m ,i:0~5"
    "tool","应用的工具坐标系编号"
    "user","应用的工件坐标系编号"
    "cl_dgt_output_h","控制箱数字量IO输出15-8"
    "cl_dgt_output_l","控制箱数字量IO输出7-0"
    "tl_dgt_output_l","工具数字量IO输出7-0，仅bit0-bit1有效"
    "dgt_input_h","控制箱数字量IO输入15-8"
    "cl_dgt_input_l","控制箱数字量IO输入7-0"
    "tl_dgt_input_l","工具数字量IO输入7-0，仅bit0-bit1有效"
    "cl_analog_input[i]","控制箱模拟量输入,i:0~2"
    "tl_anglog_input","工具模拟量输入"
    "ft_sensor_raw_data","力矩传感器原始数据,单位N&Nm,i:0~5"
    "ft_sensor_data","力矩传感器数据,单位N&Nm,i:0~5"
    "ft_sensor_active","力矩传感器激活状态，0-复位，1-激活"
    "EmergencyStop","急停标志,0-急停未按下,1-急停按下"
    "motion_done","运动到位信号,1-到位，0-未到位"
    "gripper_motiondone","夹爪运动完成信号,1-完成，0-未完成 "
    "mc_queue_len","运动指令队列长度"
    "collisionState","碰撞检测,1-碰撞，0-无碰撞 "
    "trajectory_pnum","轨迹点编号"
    "safety_stop0_state","安全停止信号SI0"
    "safety_stop1_state","安全停止信号SI1"
    "gripper_fault_id","错误夹爪号"
    "gripper_fault","夹爪故障"
    "gripper_active","夹爪激活状态，0-未激活，1-激活"
    "gripper_position","夹爪位置(百分比)"
    "gripper_speed","夹爪速度(百分比)"
    "gripper_current","夹爪电流(百分比)"
    "gripper_tmp","夹爪温度,单位℃"
    "gripper_voltage","夹爪电压,单位V"
    "auxState.servoId","485扩展轴,伺服驱动器ID号,i:0~3"
    "auxState.servoErrCode","485扩展轴,伺服驱动器故障码,i:0~3"
    "auxState.servoState","485扩展轴,伺服驱动器状态,i:0~3"
    "auxState.servoPos","485扩展轴,伺服当前位置,i:0~3"
    "auxState.servoVel","485扩展轴,伺服当前速度,i:0~3"
    "auxState.servoTorque","485扩展轴,伺服当前转矩,i:0~3"
    "extAxisStatus[i].pos","UDP扩展轴,位置,i:0~3"
    "extAxisStatus[i].vel","UDP扩展轴,速度,i:0~3"
    "extAxisStatus[i].errorCode","UDP扩展轴,故障码,i:0~3"
    "extAxisStatus[i].ready","UDP扩展轴,伺服准备好,i:0~3"
    "extAxisStatus[i].inPos","UDP扩展轴,伺服到位,i:0~3"
    "extAxisStatus[i].alarm","UDP扩展轴,伺服报警,i:0~3"
    "extAxisStatus[i].flerr","UDP扩展轴,跟随误差,i:0~3"
    "extAxisStatus[i].nlimit","UDP扩展轴,到负限位,i:0~3"
    "extAxisStatus[i].pLimit","UDP扩展轴,到正限位,i:0~3"
    "extAxisStatus[i].mdbsOffLine","UDP扩展轴,驱动器485总线掉线"
    "extAxisStatus[i].mdbsTimeout","UDP扩展轴,控制卡与控制箱485通信超时"
    "extAxisStatus[i].homingStatus","UDP扩展轴,回零状态"
    "extDIState","扩展数字输入状态"
    "extDOState","扩展数字输出状态"
    "extAIState","扩展模拟输入状态"
    "extAOState","扩展模拟输出状态"
    "rbtEnableState","机器人使能状态"
    "jointDriverTorque","关节驱动器当前扭矩"
    "jointDriverTemperature","关节驱动器当前温度"
    "year","年"
    "mouth","月"
    "day","日"
    "hour","小时"
    "minute","分"
    "second","秒"
    "millisecond","毫秒"
    "softwareUpgradeState","机器人软件升级状态"
    "endLuaErrCode","末端LUA运行状态"
    
代码示例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 与机器人控制器建立连接，连接成功返回一个机器人对象
    robot = Robot.RPC('192.168.58.2')
    print("program_state:", robot.robot_state_pkg.program_state)
    print("robot_state:", robot.robot_state_pkg.robot_state)
    print("main_code:", robot.robot_state_pkg.main_code)
    print("sub_code:", robot.robot_state_pkg.sub_code)
    print("robot_mode:", robot.robot_state_pkg.robot_mode)
    print("jt_cur_pos0:", robot.robot_state_pkg.jt_cur_pos[0])
    print("jt_cur_pos1:", robot.robot_state_pkg.jt_cur_pos[1])
    print("jt_cur_pos2:", robot.robot_state_pkg.jt_cur_pos[2])
    print("jt_cur_pos3:", robot.robot_state_pkg.jt_cur_pos[3])
    print("jt_cur_pos4:", robot.robot_state_pkg.jt_cur_pos[4])
    print("jt_cur_pos5:", robot.robot_state_pkg.jt_cur_pos[5])
    print("tl_cur_pos0:", robot.robot_state_pkg.tl_cur_pos[0])
    print("tl_cur_pos1:", robot.robot_state_pkg.tl_cur_pos[1])
    print("tl_cur_pos2:", robot.robot_state_pkg.tl_cur_pos[2])
    print("tl_cur_pos3:", robot.robot_state_pkg.tl_cur_pos[3])
    print("tl_cur_pos4:", robot.robot_state_pkg.tl_cur_pos[4])
    print("tl_cur_pos5:", robot.robot_state_pkg.tl_cur_pos[5])
    print("flange_cur_pos0:", robot.robot_state_pkg.flange_cur_pos[0])
    print("flange_cur_pos1:", robot.robot_state_pkg.flange_cur_pos[1])
    print("flange_cur_pos2:", robot.robot_state_pkg.flange_cur_pos[2])
    print("flange_cur_pos3:", robot.robot_state_pkg.flange_cur_pos[3])
    print("flange_cur_pos4:", robot.robot_state_pkg.flange_cur_pos[4])
    print("flange_cur_pos5:", robot.robot_state_pkg.flange_cur_pos[5])
    print("actual_qd0:", robot.robot_state_pkg.actual_qd[0])
    print("actual_qd1:", robot.robot_state_pkg.actual_qd[1])
    print("actual_qd2:", robot.robot_state_pkg.actual_qd[2])
    print("actual_qd3:", robot.robot_state_pkg.actual_qd[3])
    print("actual_qd4:", robot.robot_state_pkg.actual_qd[4])
    print("actual_qd5:", robot.robot_state_pkg.actual_qd[5])
    print("actual_qdd0:", robot.robot_state_pkg.actual_qdd[0])
    print("actual_qdd1:", robot.robot_state_pkg.actual_qdd[1])
    print("actual_qdd2:", robot.robot_state_pkg.actual_qdd[2])
    print("actual_qdd3:", robot.robot_state_pkg.actual_qdd[3])
    print("actual_qdd4:", robot.robot_state_pkg.actual_qdd[4])
    print("actual_qdd5:", robot.robot_state_pkg.actual_qdd[5])
    print("target_TCP_CmpSpeed0:", robot.robot_state_pkg.target_TCP_CmpSpeed[0])
    print("target_TCP_CmpSpeed1:", robot.robot_state_pkg.target_TCP_CmpSpeed[1])
    print("target_TCP_Speed0:", robot.robot_state_pkg.target_TCP_Speed[0])
    print("target_TCP_Speed1:", robot.robot_state_pkg.target_TCP_Speed[1])
    print("target_TCP_Speed2:", robot.robot_state_pkg.target_TCP_Speed[2])
    print("target_TCP_Speed3:", robot.robot_state_pkg.target_TCP_Speed[3])
    print("target_TCP_Speed4:", robot.robot_state_pkg.target_TCP_Speed[4])
    print("target_TCP_Speed5:", robot.robot_state_pkg.target_TCP_Speed[5])
    print("actual_TCP_CmpSpeed0:", robot.robot_state_pkg.actual_TCP_CmpSpeed[0])
    print("actual_TCP_CmpSpeed1:", robot.robot_state_pkg.actual_TCP_CmpSpeed[1])
    print("actual_TCP_Speed0:", robot.robot_state_pkg.actual_TCP_Speed[0])
    print("actual_TCP_Speed1:", robot.robot_state_pkg.actual_TCP_Speed[1])
    print("actual_TCP_Speed2:", robot.robot_state_pkg.actual_TCP_Speed[2])
    print("actual_TCP_Speed3:", robot.robot_state_pkg.actual_TCP_Speed[3])
    print("actual_TCP_Speed4:", robot.robot_state_pkg.actual_TCP_Speed[4])
    print("actual_TCP_Speed5:", robot.robot_state_pkg.actual_TCP_Speed[5])
    print("jt_cur_tor0:", robot.robot_state_pkg.jt_cur_tor[0])
    print("jt_cur_tor1:", robot.robot_state_pkg.jt_cur_tor[1])
    print("jt_cur_tor2:", robot.robot_state_pkg.jt_cur_tor[2])
    print("jt_cur_tor3:", robot.robot_state_pkg.jt_cur_tor[3])
    print("jt_cur_tor4:", robot.robot_state_pkg.jt_cur_tor[4])
    print("jt_cur_tor5:", robot.robot_state_pkg.jt_cur_tor[5])
    print("tool:", robot.robot_state_pkg.tool)
    print("user:", robot.robot_state_pkg.user)
    print("cl_dgt_output_h:", robot.robot_state_pkg.cl_dgt_output_h)
    print("cl_dgt_output_l:", robot.robot_state_pkg.cl_dgt_output_l)
    print("tl_dgt_output_l:", robot.robot_state_pkg.tl_dgt_output_l)
    print("cl_dgt_input_h:", robot.robot_state_pkg.cl_dgt_input_h)
    print("cl_dgt_input_l:", robot.robot_state_pkg.cl_dgt_input_l)
    print("tl_dgt_input_l:", robot.robot_state_pkg.tl_dgt_input_l)
    print("cl_analog_input0:", robot.robot_state_pkg.cl_analog_input[0])
    print("cl_analog_input1:", robot.robot_state_pkg.cl_analog_input[1])
    print("tl_anglog_input:", robot.robot_state_pkg.tl_anglog_input)
    print("ft_sensor_raw_data0:", robot.robot_state_pkg.ft_sensor_raw_data[0])
    print("ft_sensor_raw_data1:", robot.robot_state_pkg.ft_sensor_raw_data[1])
    print("ft_sensor_raw_data2:", robot.robot_state_pkg.ft_sensor_raw_data[2])
    print("ft_sensor_raw_data3:", robot.robot_state_pkg.ft_sensor_raw_data[3])
    print("ft_sensor_raw_data4:", robot.robot_state_pkg.ft_sensor_raw_data[4])
    print("ft_sensor_raw_data5:", robot.robot_state_pkg.ft_sensor_raw_data[5])
    print("ft_sensor_data0:", robot.robot_state_pkg.ft_sensor_data[0])
    print("ft_sensor_data1:", robot.robot_state_pkg.ft_sensor_data[1])
    print("ft_sensor_data2:", robot.robot_state_pkg.ft_sensor_data[2])
    print("ft_sensor_data3:", robot.robot_state_pkg.ft_sensor_data[3])
    print("ft_sensor_data4:", robot.robot_state_pkg.ft_sensor_data[4])
    print("ft_sensor_data5:", robot.robot_state_pkg.ft_sensor_data[5])
    print("ft_sensor_active:", robot.robot_state_pkg.ft_sensor_active)
    print("EmergencyStop:", robot.robot_state_pkg.EmergencyStop)
    print("motion_done:", robot.robot_state_pkg.motion_done)
    print("gripper_motiondone:", robot.robot_state_pkg.gripper_motiondone)
    print("mc_queue_len:", robot.robot_state_pkg.mc_queue_len)
    print("collisionState:", robot.robot_state_pkg.collisionState)
    print("trajectory_pnum:", robot.robot_state_pkg.trajectory_pnum)
    print("safety_stop0_state:", robot.robot_state_pkg.safety_stop0_state)
    print("safety_stop1_state:", robot.robot_state_pkg.safety_stop1_state)
    print("gripper_fault_id:", robot.robot_state_pkg.gripper_fault_id)
    print("gripper_fault:", robot.robot_state_pkg.gripper_fault)
    print("gripper_active:", robot.robot_state_pkg.gripper_active)
    print("gripper_position:", robot.robot_state_pkg.gripper_position)
    print("gripper_speed:", robot.robot_state_pkg.gripper_speed)
    print("gripper_current:", robot.robot_state_pkg.gripper_current)
    print("gripper_tmp:", robot.robot_state_pkg.gripper_tmp)
    print("gripper_voltage:", robot.robot_state_pkg.gripper_voltage)
    print("auxState.servoId:", robot.robot_state_pkg.auxState.servoId)
    print("auxState.servoErrCode:", robot.robot_state_pkg.auxState.servoErrCode)
    print("auxState.servoState:", robot.robot_state_pkg.auxState.servoState)
    print("auxState.servoPos:", robot.robot_state_pkg.auxState.servoPos)
    print("auxState.servoVel:", robot.robot_state_pkg.auxState.servoVel)
    print("auxState.servoTorque:", robot.robot_state_pkg.auxState.servoTorque)
    for i in range(4):
        print("extAxisStatus.pos:", i,robot.robot_state_pkg.extAxisStatus[i].pos)
        print("extAxisStatus.vel:", i,robot.robot_state_pkg.extAxisStatus[i].vel)
        print("extAxisStatus.errorCode:", i,robot.robot_state_pkg.extAxisStatus[i].errorCode)
        print("extAxisStatus.ready:", i,robot.robot_state_pkg.extAxisStatus[i].ready)
        print("extAxisStatus.inPos:", i,robot.robot_state_pkg.extAxisStatus[i].inPos)
        print("extAxisStatus.alarm:", i,robot.robot_state_pkg.extAxisStatus[i].alarm)
        print("extAxisStatus.flerr:", i,robot.robot_state_pkg.extAxisStatus[i].flerr)
        print("extAxisStatus.nlimit:", i,robot.robot_state_pkg.extAxisStatus[i].nlimit)
        print("extAxisStatus.pLimit:", i,robot.robot_state_pkg.extAxisStatus[i].pLimit)
        print("extAxisStatus.mdbsOffLine:", i,robot.robot_state_pkg.extAxisStatus[i].mdbsOffLine)
        print("extAxisStatus.mdbsTimeout:", i,robot.robot_state_pkg.extAxisStatus[i].mdbsTimeout)
        print("extAxisStatus.homingStatus:", i,robot.robot_state_pkg.extAxisStatus[i].homingStatus)
    for i in range(8):
        print("extDIState:",i, robot.robot_state_pkg.extDIState[i])
        print("extDOState:", i,robot.robot_state_pkg.extDOState[i])
    for i in range(4):
        print("extAIState:", i,robot.robot_state_pkg.extAIState[i])
        print("extAOState:", robot.robot_state_pkg.extAOState[i])
    print("rbtEnableState:", robot.robot_state_pkg.rbtEnableState)
    print("jointDriverTorque0:", robot.robot_state_pkg.jointDriverTorque[0])
    print("jointDriverTorque1:", robot.robot_state_pkg.jointDriverTorque[1])
    print("jointDriverTorque2:", robot.robot_state_pkg.jointDriverTorque[2])
    print("jointDriverTorque3:", robot.robot_state_pkg.jointDriverTorque[3])
    print("jointDriverTorque4:", robot.robot_state_pkg.jointDriverTorque[4])
    print("jointDriverTorque5:", robot.robot_state_pkg.jointDriverTorque[5])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[0])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[1])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[2])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[3])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[4])
    print("jointDriverTemperature:", robot.robot_state_pkg.jointDriverTemperature[5])
    print("year:", robot.robot_state_pkg.year)
    print("mouth:", robot.robot_state_pkg.mouth)
    print("day:", robot.robot_state_pkg.day)
    print("hour:", robot.robot_state_pkg.hour)
    print("minute:", robot.robot_state_pkg.minute)
    print("second:", robot.robot_state_pkg.second)
    print("millisecond:", robot.robot_state_pkg.millisecond)
    print("softwareUpgradeState:", robot.robot_state_pkg.softwareUpgradeState)
    print("endLuaErrCode:", robot.robot_state_pkg.endLuaErrCode)