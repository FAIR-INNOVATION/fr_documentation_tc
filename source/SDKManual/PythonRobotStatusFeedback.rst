狀態回饋訊息
==========================

.. toctree:: 
    :maxdepth: 5

狀態回饋訊息對照表
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionchanged:: Python SDK-v2.0.8-3.7.8
    
.. csv-table:: 
    :header-rows: 1
    :name: 狀態回饋訊息對照表
    :widths: 20 30

    "變數","意義"
    "program_state","程式運作狀態，1-停止；2-運轉；3-暫停"
    "robot_state","機器人運動狀態，1-停止；2-運轉；3-暫停；4-拖曳"
    "main_code","主故障碼"
    "sub_code", 子故障碼"
    "robot_mode","機器人模式，0-自動模式；1-手動模式"
    "jt_cur_pos[i]","關節目前位置,單位deg,i:0~5"
    "tl_cur_pos[i]","工具當前位姿,單位deg&mm,i:0~5"
    "flange_cur_pos[i]","末端法蘭目前位姿,單位deg&mm,i:0~5"
    "actual_qd[i]","機器人目前關節速度,單位deg/s^2,i:0~5"
    "actual_qdd[i]","機器人當前關節加速度,單位mm/s,i:0~5"
    "target_TCP_CmpSpeed[i]","機器人TCP合成指令速度,單位mm/s&deg/s,i:0~1"
    "target_TCP_Speed[i]","機器人TCP指令速度,單位mm/s&deg/s,i:0~5"
    "actual_TCP_CmpSpeed[i]","機器人TCP合成實際速度,單位mm/s&deg/s,i:0~1"
    "actual_TCP_Speed[i]","機器人TCP實際速度,單位mm/s&deg/s,i:0~5"
    "jt_cur_tor[i]","當前扭力,單位N·m ,i:0~5"
    "tool","應用程式的工具坐標系編號"
    "user","應用的工件座標系編號"
    "cl_dgt_output_h","控制箱數字量IO輸出15-8"
    "cl_dgt_output_l","控制箱數字量IO輸出7-0"
    "tl_dgt_output_l","工具數字量IO輸出7-0，僅bit0-bit1有效"
    "dgt_input_h","控制箱數字量IO輸入15-8"
    "cl_dgt_input_l","控制箱數字量IO輸入7-0"
    "tl_dgt_input_l","工具數字量IO輸入7-0，僅bit0-bit1有效"
    "cl_analog_input[i]","控制箱類比輸入,i:0~2"
    "tl_anglog_input","工具類比輸入"
    "ft_sensor_raw_data","力矩傳感器原始資料,單位N&Nm,i:0~5"
    "ft_sensor_data","力矩感測器資料,單​​位N&Nm,i:0~5"
    "ft_sensor_active","力矩感應器啟動狀態，0-復位，1-啟動"
    "EmergencyStop","急停標誌,0-急停未按下,1-急停按下"
    "motion_done","運動到位訊號,1-到位，0-未到位"
    "gripper_motiondone","夾爪動作完成訊號,1-完成，0-未完成"
    "mc_queue_len","運動指令隊列長度"
    "collisionState","碰撞偵測,1-碰撞，0-無碰撞"
    "trajectory_pnum","軌跡點編號"
    "safety_stop0_state","安全停止訊號SI0"
    "safety_stop1_state","安全停止訊號SI1"
    "gripper_fault_id","錯誤夾爪號"
    "gripper_fault","夾爪故障"
    "gripper_active","夾爪激活狀態，0-未激活，1-激活"
    "gripper_position","夾爪位置(百分比)"
    "gripper_speed","夾爪速度(百分比)"
    "gripper_current","夾爪電流(百分比)"
    "gripper_tmp","夾爪溫度,單位℃"
    "gripper_voltage","夾爪電壓,單位V"
    "auxState.servoId","485擴充軸,伺服驅動程式ID號碼,i:0~3"
    "auxState.servoErrCode","485擴充軸,伺服驅動故障碼,i:0~3"
    "auxState.servoState","485擴充軸,伺服驅動器狀態,i:0~3"
    "auxState.servoPos","485擴充軸,伺服目前位置,i:0~3"
    "auxState.servoVel","485擴充軸,伺服當前速度,i:0~3"
    "auxState.servoTorque","485擴充軸,伺服當前轉矩,i:0~3"
    "extAxisStatus[i].pos","UDP擴展軸,位置,i:0~3"
    "extAxisStatus[i].vel","UDP擴展軸,速度,i:0~3"
    "extAxisStatus[i].errorCode","UDP擴充軸,故障碼,i:0~3"
    "extAxisStatus[i].ready","UDP擴充軸,伺服準備好,i:0~3"
    "extAxisStatus[i].inPos","UDP擴展軸,伺服到位,i:0~3"
    "extAxisStatus[i].alarm","UDP擴展軸,伺服警報,i:0~3"
    "extAxisStatus[i].flerr","UDP擴展軸,跟隨誤差,i:0~3"
    "extAxisStatus[i].nlimit","UDP擴展軸,到負限位,i:0~3"
    "extAxisStatus[i].pLimit","UDP擴展軸,到正限位,i:0~3"
    "extAxisStatus[i].mdbsOffLine","UDP擴充軸,磁碟機485匯流排斷線"
    "extAxisStatus[i].mdbsTimeout","UDP擴充軸,控制卡與控制箱485通訊逾時"
    "extAxisStatus[i].homingStatus","UDP擴充軸,回零狀態"
    "extDIState","擴充數位輸入狀態"
    "extDOState","擴充數位輸出狀態"
    "extAIState","擴充模擬輸入狀態"
    "extAOState","擴充類比輸出狀態"
    "rbtEnableState","機器人啟用狀態"
    "jointDriverTorque","關節驅動器當前扭力"
    "jointDriverTemperature","關節驅動器當前溫度"
    "year","年"
    "mouth","月"
    "day","日"
    "hour","小時"
    "minute","分"
    "second","秒"
    "millisecond","毫秒"
    "softwareUpgradeState","機器人軟體升級狀態"
    "cl_analog_output[i]","控制箱類比輸出,i:0~1"
    "tl_analog_output","工具類比量輸出"
    "gripperRotNum","旋轉夾爪目前旋轉圈數"
    "gripperRotSpeed","旋轉夾爪目前旋轉速度百分比"
    "gripperRotTorque","旋轉夾爪目前旋轉力矩百分比"
    "endLuaErrCode","末端LUA運行狀態"
    
代碼範例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
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
    print("cl_analog_output[0]:",robot.robot_state_pkg.cl_analog_output[0])
    print("cl_analog_output[1]:",robot.robot_state_pkg.cl_analog_output[1])
    print("tl_analog_output:",robot.robot_state_pkg.tl_analog_output)
    print("gripperRotNum:",robot.robot_state_pkg.gripperRotNum)
    print("gripperRotSpeed:",robot.robot_state_pkg.gripperRotSpeed)
    print("gripperRotTorque:",robot.robot_state_pkg.gripperRotTorque)
    print("endLuaErrCode:", robot.robot_state_pkg.endLuaErrCode)