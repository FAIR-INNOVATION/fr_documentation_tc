數據結構說明
==========================

.. toctree:: 
    :maxdepth: 5

機器人狀態反饋結構體類型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:
    
    class ROBOT_AUX_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("servoId", c_uint8),         # 伺服驅動器ID號
            ("servoErrCode", c_int),     # 伺服驅動器故障碼
            ("servoState", c_int),       # 伺服驅動器狀態
            ("servoPos", c_double),      # 伺服當前位置
            ("servoVel", c_float),       # 伺服當前速度
            ("servoTorque", c_float),    # 伺服當前轉矩
        ]

    class EXT_AXIS_STATUS(Structure):
        _pack_ = 1
        _fields_ = [
            ("pos", c_double),        # 擴展軸位置
            ("vel", c_double),        # 擴展軸速度
            ("errorCode", c_int),     # 擴展軸故障碼
            ("ready", c_uint8),        # 伺服準備好
            ("inPos", c_uint8),        # 伺服到位
            ("alarm", c_uint8),        # 伺服報警
            ("flerr", c_uint8),        # 跟隨誤差
            ("nlimit", c_uint8),       # 到負限位
            ("pLimit", c_uint8),       # 到正限位
            ("mdbsOffLine", c_uint8),  # 驅動器485總線掉線
            ("mdbsTimeout", c_uint8),  # 控制卡與控制箱485通信超時
            ("homingStatus", c_uint8), # 擴展軸回零狀態
        ]

    class WELDING_BREAKOFF_STATE(Structure):
        _pack_ = 1
        _fields_ = [
            ("breakOffState", c_uint8),        # 焊接中斷狀態
            ("weldArcState", c_uint8),        # 焊接電弧中斷狀態
        ]

    # ==================== 完整機器人狀態結構體 ====================
    class RobotStatePkg(Structure):
        """
        機器人狀態反饋數據包
        """
        _pack_ = 1
        _fields_ = [
            # 幀頭信息
            ("frame_head", c_uint16),           # 幀頭，約定為0x5A5A
            ("frame_cnt", c_uint8),             # 幀計數，循環計數0-255
            ("data_len", c_uint16),             # 數據內容的長度
            ("program_state", c_uint8),         # 程式運行狀態，1-停止；2-運行；3-暫停
            ("robot_state", c_uint8),             # 機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動
            ("main_code", c_int),               # 主故障碼
            ("sub_code", c_int),                # 子故障碼
            ("robot_mode", c_uint8),            # 機器人模式，1-手動模式；0-自動模式

            # 關節位置和速度
            ("jt_cur_pos", c_double * 6),       # 6個軸當前關節位置，單位deg
            ("tl_cur_pos", c_double * 6),       # 工具當前位置 [x,y,z,rx,ry,rz]
            ("flange_cur_pos", c_double * 6),   # 末端法蘭當前位置 [x,y,z,rx,ry,rz]
            ("actual_qd", c_double * 6),        # 當前6個關節速度，單位deg/s
            ("actual_qdd", c_double * 6),       # 當前6個關節加速度，單位deg/s^2
            ("target_TCP_CmpSpeed", c_double * 2),  # TCP合成指令速度[位置mm/s,姿態deg/s]
            ("target_TCP_Speed", c_double * 6), # TCP指令速度[x,y,z,rx,ry,rz]
            ("actual_TCP_CmpSpeed", c_double * 2),  # TCP合成實際速度[位置mm/s,姿態deg/s]
            ("actual_TCP_Speed", c_double * 6), # TCP實際速度[x,y,z,rx,ry,rz]
            ("jt_cur_tor", c_double * 6),       # 6個軸當前扭矩，單位N·m

            # 工具和用戶座標系
            ("tool", c_int),                    # 應用的工具座標系編號
            ("user", c_int),                    # 應用的工件座標系編號

            # 數字IO
            ("cl_dgt_output_h", c_uint8),       # 控制箱數字量IO輸出15-8
            ("cl_dgt_output_l", c_uint8),       # 控制箱數字量IO輸出7-0
            ("tl_dgt_output_l", c_uint8),       # 工具數字量IO輸出7-0，僅bit0-bit1有效
            ("cl_dgt_input_h", c_uint8),        # 控制箱數字量IO輸入15-8
            ("cl_dgt_input_l", c_uint8),        # 控制箱數字量IO輸入7-0
            ("tl_dgt_input_l", c_uint8),        # 工具數字量IO輸入7-0，僅bit0-bit1有效

            # 類比量IO
            ("cl_analog_input", c_uint16 * 2),  # 控制箱類比量輸入[0],[1]
            ("tl_anglog_input", c_uint16),      # 工具類比量輸入

            # 力矩感測器
            ("ft_sensor_raw_data", c_double * 6),   # 力矩感測器原始數據
            ("ft_sensor_data", c_double * 6),      # 力矩感測器數據
            ("ft_sensor_active", c_uint8),          # 力矩感測器激活狀態

            # 狀態信號
            ("EmergencyStop", c_uint8),         # 急停標誌，0-急停未按下，1-急停按下
            ("motion_done", c_int),             # 運動到位信號，1-到位，0-未到位
            ("gripper_motiondone", c_uint8),    # 夾爪運動完成信號，1-完成，0-未完成
            ("mc_queue_len", c_int),            # 運動指令隊列長度
            ("collisionState", c_uint8),        # 碰撞檢測，1-碰撞，0-無碰撞
            ("trajectory_pnum", c_int),         # 軌跡點編號
            ("safety_stop0_state", c_uint8),    # 安全停止信號SI0
            ("safety_stop1_state", c_uint8),    # 安全停止信號SI1

            # 夾爪信息
            ("gripper_fault_id", c_uint8),      # 錯誤夾爪號
            ("gripper_fault", c_uint16),        # 夾爪故障
            ("gripper_active", c_uint16),      # 夾爪激活狀態
            ("gripper_position", c_uint8),      # 夾爪位置
            ("gripper_speed", c_int8),          # 夾爪速度
            ("gripper_current", c_int8),        # 夾爪電流
            ("gripper_temp", c_int),            # 夾爪溫度
            ("gripper_voltage", c_int),         # 夾爪電壓

            # 擴展軸狀態
            ("aux_axis_state", ROBOT_AUX_STATE * 25),    # 485擴展軸狀態 (25個)
            ("extAxisStatus", EXT_AXIS_STATUS * 4), # UDP擴展軸狀態 (4個)

            # 擴展IO狀態
            ("extDIState", c_uint16 * 8),       # 擴展DI輸入
            ("extDOState", c_uint16 * 8),       # 擴展DO輸出
            ("extAIState", c_uint16 * 4),        # 擴展AI輸入
            ("extAOState", c_uint16 * 4),        # 擴展AO輸出

            # 機器和關節狀態
            ("rbtEnableState", c_int),                  # 機器人使能狀態
            ("jointDriverTorque", c_double * 6),        # 機器人關節驅動器扭矩
            ("jointDriverTemperature", c_double * 6),   # 機器人關節驅動器溫度

            # 機器人時間
            #("robotTime", c_int * 7),             # 機器人系統時間 [年,月,日,時,分,秒,毫秒]
            ("year", ctypes.c_uint16),  # 年
            ("mouth", ctypes.c_uint8),  # 月
            ("day", ctypes.c_uint8),   # 日
            ("hour", ctypes.c_uint8),   # 時
            ("minute", ctypes.c_uint8), # 分
            ("second", ctypes.c_uint8), # 秒
            ("millisecond", ctypes.c_uint16), # 毫秒

            ("softwareUpgradeState", c_int),      # 機器人軟體升級狀態
            ("endLuaErrCode", c_uint16),          # 末端LUA運行狀態

            # 類比量輸出
            ("cl_analog_output", c_uint16 * 2), # 控制箱類比量輸出[0],[1]
            ("tl_analog_output", c_uint16),       # 工具類比量輸出

            # 旋轉夾爪
            ("gripperRotNum", c_float),         # 旋轉夾爪當前旋轉圈數
            ("gripperRotSpeed", c_uint8),       # 旋轉夾爪當前旋轉速度百分比
            ("gripperRotTorque", c_uint8),      # 旋轉夾爪當前旋轉力矩百分比

            # 焊接中斷狀態 - 使用結構體
            ("weldingBreakOffState", WELDING_BREAKOFF_STATE),  # 焊接中斷狀態

            # 目標關節扭矩
            ("jt_tgt_tor", c_double * 6),       # 關節指令力矩

            ("smartToolState", c_int),          # SmartTool手柄按鈕狀態
            ("wideVoltageCtrlBoxTemp", c_float),        # 寬電壓控制箱溫度
            ("wideVoltageCtrlBoxFanCurrent", c_uint16), # 寬電壓控制箱風扇電流(mA)

            # 座標係數值
            ("toolCoord", c_double * 6),        # 當前工具座標係數值；x,y,z,rx,ry,rz
            ("wobjCoord", c_double * 6),        # 當前工件座標係數值；x,y,z,rx,ry,rz
            ("extoolCoord", c_double * 6),      # 當前外部工具座標係數值；x,y,z,rx,ry,rz
            ("exAxisCoord", c_double * 6),      # 當前擴展軸座標係數值；x,y,z,rx,ry,rz

            # 負載
            ("load", c_double),                 # 負載質量
            ("loadCog", c_double * 3),            # 負載質心

            # 伺服指令
            ("lastServoTarget", c_double * 6),  # 隊列中最後一個ServoJ目標位置
            ("servoJCmdNum", c_int),            # servoJ指令計數

            # 目標關節數據
            ("targetJointPos", c_double * 6),   # 6個關節指令位置，單位°
            ("targetJointVel", c_double * 6),   # 6個關節指令速度，單位°/s
            ("targetJointAcc", c_double * 6),   # 6個關節指令加速度，單位°/s2
            ("targetJointCurrent", c_double * 6), # 6個關節指令電流，單位A
            ("actualJointCurrent", c_double * 6), # 6個關節當前電流，單位A
            ("actualTCPForce", c_double * 6),   # 機器人末端力矩Nm；x,y,z,rx,ry,rz
            ("targetTCPPos", c_double * 6),     # 機器人TCP指令位置mm；x,y,z,rx,ry,rz

            ("collisionLevel", c_uint8 * 6),    # 機器人碰撞等級
            ("speedScaleManual", c_double),     # 手動模式全局速度百分比
            ("speedScaleAuto", c_double),       # 自動模式全局速度百分比
            ("luaLineNum", c_int),              # 當前lua程式運行行號
            ("abnomalStop", c_uint8),           # 0-無異常；1-有異常
            ("currentLuaFileName", c_uint8 * 256),  # 當前運行lua程式名稱
            ("programTotalLine", c_uint8),      # lua程式總行數
            ("safetyBoxSingal", c_uint8 * 6),   # 機器人按鈕盒按鈕狀態

            # 焊接數據
            ("weldVoltage", c_double),          # 焊接電壓 V
            ("weldCurrent", c_double),          # 焊接電流
            ("weldTrackVel", c_double),         # 焊縫跟蹤速度 mm/s

            ("tpdException", c_uint8),            # TPD軌跡加載數量超限，0-未超限，1-超限
            ("alarmRebootRobot", c_uint8),      # 警告，1-鬆開急停按鈕請斷電重啟控制箱，2-關節通訊異常請斷電重啟控制箱
            ("modbusMasterConnect", c_uint8),   # bit0-bit7位對應ModbusTCP的0-7主站連接狀態
            ("modbusSlaveConnect", c_uint8),    # ModbusTCP從站連接狀態
            ("btnBoxStopSignal", c_uint8),      # 按鈕盒急停信號
            ("dragAlarm", c_uint8),             # 拖動警告
            ("safetyDoorAlarm", c_uint8),       # 安全門警告
            ("safetyPlaneAlarm", c_uint8),      # 進入安全牆警告
            ("motonAlarm", c_uint8),            # 運動警告
            ("interfaceAlarm", c_uint8),        # 進入干涉區警告
            ("udpCmdState", c_int),             # 20007端口UDP通訊連接狀態
            ("weldReadyState", c_uint8),        # 焊機準備完成狀態
            ("alarmCheckEmergStopBtn", c_uint8),    # 0-正常；1-通訊異常，檢查急停按鈕是否鬆開
            ("tsTmCmdComError", c_uint8),       # 0-正常；1-扭矩指令通訊失敗
            ("tsTmStateComError", c_uint8),     # 0-正常；1-扭矩狀態通訊失敗
            ("ctrlBoxError", c_int),            # 控制箱錯誤
            ("safetyDataState", c_uint8),       # 安全數據狀態標誌
            ("forceSensorErrState", c_uint8),   # 力感測器連接超時故障
            ("ctrlOpenLuaErrCode", c_uint8 * 4),  # 4個控制器外設協議錯誤碼
            ("strangePosFlag", c_uint8),        # 當前處於奇異位姿標誌
            ("alarm", c_uint8),                 # 警告
            ("driverAlarm", c_uint8),           # 驅動器報警軸號
            ("aliveSlaveNumError", c_uint8),    # 活動從站數量錯誤
            ("slaveComError", c_uint8 * 8),     # 從站錯誤狀態
            ("cmdPointError", c_uint8),         # 指令點錯誤
            ("IOError", c_uint8),               # IO錯誤
            ("gripperError", c_uint8),          # 夾爪錯誤
            ("fileError", c_uint8),             # 文件錯誤
            ("paraError", c_uint8),             # 參數錯誤
            ("exaxisOutLimitError", c_uint8),   # 外部軸超出軟限位錯誤
            ("driverComError", c_uint8 * 6),    # 與驅動器通信故障
            ("driverError", c_uint8),           # 驅動器通信故障軸號
            ("outSoftLimitError", c_uint8),     # 超出軟限位故障
            ("axleGenComData", c_uint8 * 130),   # 軸通用通訊非週期數據
            ("socketConnTimeout", c_uint8),     # socket連接超時
            ("socketReadTimeout", c_uint8),     # socket讀取超時
            ("tsWebStateComErr", c_uint8),      # TS_WEB狀態通訊錯誤
            ("check_sum", c_uint16)          # 和校驗
        ]

控制器狀態反饋數據包
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.7
    
.. csv-table:: 
    :header-rows: 1
    :name: 控制器狀態反饋數據包
    :widths: 20 30

    "變量","含義"
    "program_state","程序運行狀態，1-停止；2-運行；3-暫停"
    "robot_state","機器人運動狀態，1-停止；2-運行；3-暫停；4-拖動"
    "main_code","主故障碼"
    "sub_code",	子故障碼"
    "robot_mode","機器人模式，0-自動模式；1-手動模式"
    "jt_cur_pos[i]","關節當前位置,單位deg,i:0~5"
    "tl_cur_pos[i]","工具當前位姿,單位deg&mm,i:0~5"
    "flange_cur_pos[i]","末端法蘭當前位姿,單位deg&mm,i:0~5"
    "actual_qd[i]","機器人當前關節速度,單位deg/s,i:0~5"
    "actual_qdd[i]","機器人當前關節加速度,單位deg/s^2,i:0~5"
    "target_TCP_CmpSpeed[i]","機器人TCP合成指令速度,單位mm/s&deg/s,i:0~1"
    "target_TCP_Speed[i]","機器人TCP指令速度,單位mm/s&deg/s,i:0~5"
    "actual_TCP_CmpSpeed[i]","機器人TCP合成實際速度,單位mm/s&deg/s,i:0~1"
    "actual_TCP_Speed[i]","機器人TCP實際速度,單位mm/s&deg/s,i:0~5"
    "jt_cur_tor[i]","當前扭矩,單位N·m ,i:0~5"
    "tool","應用的工具座標系編號"
    "user","應用的工件座標系編號"
    "cl_dgt_output_h","控制箱數字量IO輸出15-8"
    "cl_dgt_output_l","控制箱數字量IO輸出7-0"
    "tl_dgt_output_l","工具數字量IO輸出7-0，僅bit0-bit1有效"
    "dgt_input_h","控制箱數字量IO輸入15-8"
    "cl_dgt_input_l","控制箱數字量IO輸入7-0"
    "tl_dgt_input_l","工具數字量IO輸入7-0，僅bit0-bit1有效"
    "cl_analog_input[i]","控制箱模擬量輸入,i:0~2"
    "tl_anglog_input","工具模擬量輸入"
    "ft_sensor_raw_data","力矩傳感器原始數據,單位N&Nm,i:0~5"
    "ft_sensor_data","力矩傳感器數據,單位N&Nm,i:0~5"
    "ft_sensor_active","力矩傳感器激活狀態，0-復位，1-激活"
    "EmergencyStop","急停標誌,0-急停未按下,1-急停按下"
    "motion_done","運動到位信號,1-到位，0-未到位"
    "gripper_motiondone","夾爪運動完成信號,1-完成，0-未完成 "
    "mc_queue_len","運動指令隊列長度"
    "collisionState","碰撞檢測,1-碰撞，0-無碰撞 "
    "trajectory_pnum","軌跡點編號"
    "safety_stop0_state","安全停止信號SI0"
    "safety_stop1_state","安全停止信號SI1"
    "gripper_fault_id","錯誤夾爪號"
    "gripper_fault","夾爪故障"
    "gripper_active","夾爪激活狀態，0-未激活，1-激活"
    "gripper_position","夾爪位置(百分比)"
    "gripper_speed","夾爪速度(百分比)"
    "gripper_current","夾爪電流(百分比)"
    "gripper_tmp","夾爪溫度,單位℃"
    "gripper_voltage","夾爪電壓,單位V"
    "auxState.servoId","485擴展軸,伺服驅動器ID號,i:0~3"
    "auxState.servoErrCode","485擴展軸,伺服驅動器故障碼,i:0~3"
    "auxState.servoState","485擴展軸,伺服驅動器狀態,i:0~3"
    "auxState.servoPos","485擴展軸,伺服當前位置,i:0~3"
    "auxState.servoVel","485擴展軸,伺服當前速度,i:0~3"
    "auxState.servoTorque","485擴展軸,伺服當前轉矩,i:0~3"
    "extAxisStatus[i].pos","UDP擴展軸,位置,i:0~3"
    "extAxisStatus[i].vel","UDP擴展軸,速度,i:0~3"
    "extAxisStatus[i].errorCode","UDP擴展軸,故障碼,i:0~3"
    "extAxisStatus[i].ready","UDP擴展軸,伺服準備好,i:0~3"
    "extAxisStatus[i].inPos","UDP擴展軸,伺服到位,i:0~3"
    "extAxisStatus[i].alarm","UDP擴展軸,伺服報警,i:0~3"
    "extAxisStatus[i].flerr","UDP擴展軸,跟隨誤差,i:0~3"
    "extAxisStatus[i].nlimit","UDP擴展軸,到負限位,i:0~3"
    "extAxisStatus[i].pLimit","UDP擴展軸,到正限位,i:0~3"
    "extAxisStatus[i].mdbsOffLine","UDP擴展軸,驅動器485總線掉線"
    "extAxisStatus[i].mdbsTimeout","UDP擴展軸,控制卡與控制箱485通信超時"
    "extAxisStatus[i].homingStatus","UDP擴展軸,回零狀態"
    "extDIState","擴展數字輸入狀態"
    "extDOState","擴展數字輸出狀態"
    "extAIState","擴展模擬輸入狀態"
    "extAOState","擴展模擬輸出狀態"
    "rbtEnableState","機器人使能狀態"
    "jointDriverTorque","關節驅動器當前扭矩"
    "jointDriverTemperature","關節驅動器當前溫度"
    "year","年"
    "mouth","月"
    "day","日"
    "hour","小時"
    "minute","分"
    "second","秒"
    "millisecond","毫秒"
    "softwareUpgradeState","機器人軟件升級狀態"
    "endLuaErrCode","末端LUA運行狀態"
    "cl_analog_output[i]","控制箱模擬量輸出,i:0~1"
    "tl_analog_output","工具模擬量輸出"
    "gripperRotNum","旋轉夾爪當前旋轉圈數"
    "gripperRotSpeed","旋轉夾爪當前旋轉速度百分比"
    "gripperRotTorque","旋轉夾爪當前旋轉力矩百分比"
    "weldingBreakOffState","焊接中斷狀態"
    "jt_tgt_tor","關節指令力矩"
    "smartToolState","SmartTool手柄按鈕狀態"
    "wideVoltageCtrlBoxTemp","寬電壓控制箱溫度"
    "wideVoltageCtrlBoxFanCurrent","寬電壓控制箱風扇電流(ma)"
    "toolCoord[i]","工具座標系,i:0~5"
    "wobjCoord[i]","工件座標系,i:0~5"
    "extoolCoord[i]","外部工具座標系,i:0~5"
    "exAxisCoord[i]","擴展軸座標系,i:0~5"
    "load","負載質量"
    "loadCog[i]","負載質心,i:0~2"
    "lastServoTarget[i]","隊列中最後一個ServoJ目標位置,i:0~5"
    "servoJCmdNum","ServoJ指令計數"

伺服控制器狀態
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 伺服控制器狀態
    :widths: 20 30

    "變量","含義"
    "servoId","伺服驅動器ID號"
    "servoErrCode","伺服驅動器故障碼"
    "servoState","伺服驅動器狀態"
    "servoPos","伺服當前位置"
    "servoVel","伺服當前速度"
    "servoTorque","伺服當前轉矩"

擴展軸狀態
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 擴展軸狀態
    :widths: 20 30

    "變量","含義"
    "pos","擴展軸位置"
    "vel","擴展軸速度"
    "errorCode","擴展軸故障碼"
    "ready","伺服準備好"
    "inPos","伺服到位"
    "alarm","伺服報警"
    "flerr","跟隨誤差"
    "nlimit","到負限位"
    "pLimit","到正限位"
    "mdbsOffLine","驅動器485總線掉線"
    "mdbsTimeout","控制卡與控制箱485通信超時"
    "homingStatus","擴展軸回零狀態"

焊接中斷狀態
~~~~~~~~~~~~~~~~~~~~~~~~
.. versionadded:: python SDK-v2.1.3
    
.. csv-table:: 
    :header-rows: 1
    :name: 焊接中斷狀態
    :widths: 20 30

    "變量","含義"
    "breakOffState","焊接中斷狀態"
    "weldArcState","焊接電弧中斷狀態"

代碼示例
~~~~~~~~~~~~~~~~~~~~~~~~

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
    print("endLuaErrCode:", robot.robot_state_pkg.endLuaErrCode)
    print("cl_analog_output[0]:", robot.robot_state_pkg.cl_analog_output[0])
    print("cl_analog_output[1]:", robot.robot_state_pkg.cl_analog_output[1])
    print("tl_analog_output:", robot.robot_state_pkg.tl_analog_output)
    print("gripperRotNum:", robot.robot_state_pkg.gripperRotNum)
    print("gripperRotSpeed:", robot.robot_state_pkg.gripperRotSpeed)
    print("gripperRotTorque:", robot.robot_state_pkg.gripperRotTorque)
    print("jt_tgt_tor:", robot.robot_state_pkg.jt_tgt_tor)
    print("smartToolState:", robot.robot_state_pkg.smartToolState)
    print("wideVoltageCtrlBoxTemp:", robot.robot_state_pkg.wideVoltageCtrlBoxTemp)
    print("wideVoltageCtrlBoxFanCurrent:", robot.robot_state_pkg.wideVoltageCtrlBoxFanCurrent)
    print("toolCoord0:", robot.robot_state_pkg.toolCoord[0])
    print("toolCoord1:", robot.robot_state_pkg.toolCoord[1])
    print("toolCoord2:", robot.robot_state_pkg.toolCoord[2])
    print("toolCoord3:", robot.robot_state_pkg.toolCoord[3])
    print("toolCoord4:", robot.robot_state_pkg.toolCoord[4])
    print("toolCoord5:", robot.robot_state_pkg.toolCoord[5])
    print("wobjCoord0:", robot.robot_state_pkg.wobjCoord[0])
    print("wobjCoord1:", robot.robot_state_pkg.wobjCoord[1])
    print("wobjCoord2:", robot.robot_state_pkg.wobjCoord[2])
    print("wobjCoord3:", robot.robot_state_pkg.wobjCoord[3])
    print("wobjCoord4:", robot.robot_state_pkg.wobjCoord[4])
    print("wobjCoord5:", robot.robot_state_pkg.wobjCoord[5])
    print("extoolCoord0:", robot.robot_state_pkg.extoolCoord[0])
    print("extoolCoord1:", robot.robot_state_pkg.extoolCoord[1])
    print("extoolCoord2:", robot.robot_state_pkg.extoolCoord[2])
    print("extoolCoord3:", robot.robot_state_pkg.extoolCoord[3])
    print("extoolCoord4:", robot.robot_state_pkg.extoolCoord[4])
    print("extoolCoord5:", robot.robot_state_pkg.extoolCoord[5])
    print("exAxisCoord0:", robot.robot_state_pkg.exAxisCoord[0])
    print("exAxisCoord1:", robot.robot_state_pkg.exAxisCoord[1])
    print("exAxisCoord2:", robot.robot_state_pkg.exAxisCoord[2])
    print("exAxisCoord3:", robot.robot_state_pkg.exAxisCoord[3])
    print("exAxisCoord4:", robot.robot_state_pkg.exAxisCoord[4])
    print("exAxisCoord5:", robot.robot_state_pkg.exAxisCoord[5])
    print("load:", robot.robot_state_pkg.load)
    print("loadCog0:", robot.robot_state_pkg.loadCog[0])
    print("loadCog1:", robot.robot_state_pkg.loadCog[1])
    print("loadCog2:", robot.robot_state_pkg.loadCog[2])
    print("lastServoTarget0:", robot.robot_state_pkg.lastServoTarget[0])
    print("lastServoTarget1:", robot.robot_state_pkg.lastServoTarget[1])
    print("lastServoTarget2:", robot.robot_state_pkg.lastServoTarget[2])
    print("lastServoTarget3:", robot.robot_state_pkg.lastServoTarget[3])
    print("lastServoTarget4:", robot.robot_state_pkg.lastServoTarget[4])
    print("lastServoTarget5:", robot.robot_state_pkg.lastServoTarget[5])
    print("servoJCmdNum:", robot.robot_state_pkg.servoJCmdNum)

機器人狀態反饋配置列表枚舉類型
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
    :linenos:

    # ==================== RobotState配置列表枚舉 ====================
    class RobotState(enum.Enum):
        """CNDE狀態類型枚舉"""
        FrameHead = 0
        FrameCnt = 1
        DataLen = 2
        ProgramState = 3
        RobotState = 4
        MainCode = 5
        SubCode = 6
        RobotMode = 7
        JointCurPos = 8
        ToolCurPos = 9
        FlangeCurPos = 10
        ActualJointVel = 11
        ActualJointAcc = 12
        TargetTCPCmpSpeed = 13
        TargetTCPSpeed = 14
        ActualTCPCmpSpeed = 15
        ActualTCPSpeed = 16
        ActualJointTorque = 17
        Tool = 18
        User = 19
        ClDgtOutputH = 20
        ClDgtOutputL = 21
        TlDgtOutputL = 22
        ClDgtInputH = 23
        ClDgtInputL = 24
        TlDgtInputL = 25
        ClAnalogInput = 26
        TlAnglogInput = 27
        FtSensorRawData = 28
        FtSensorData = 29
        FtSensorActive = 30
        EmergencyStop = 31
        MotionDone = 32
        GripperMotiondone = 33
        McQueueLen = 34
        CollisionState = 35
        TrajectoryPnum = 36
        SafetyStop0State = 37
        SafetyStop1State = 38
        GripperFaultId = 39
        GripperFault = 40
        GripperActive = 41
        GripperPosition = 42
        GripperSpeed = 43
        GripperCurrent = 44
        GripperTemp = 45
        GripperVoltage = 46
        AuxState = 47
        ExtAxisStatus = 48
        ExtDIState = 49
        ExtDOState = 50
        ExtAIState = 51
        ExtAOState = 52
        RbtEnableState = 53
        JointDriverTorque = 54
        JointDriverTemperature = 55
        RobotTime = 56
        SoftwareUpgradeState = 57
        EndLuaErrCode = 58
        ClAnalogOutput = 59
        TlAnalogOutput = 60
        GripperRotNum = 61
        GripperRotSpeed = 62
        GripperRotTorque = 63
        WeldingBreakOffState = 64
        TargetJointTorque = 65
        SmartToolState = 66
        WideVoltageCtrlBoxTemp = 67
        WideVoltageCtrlBoxFanCurrent = 68
        ToolCoord = 69
        WobjCoord = 70
        ExtoolCoord = 71
        ExAxisCoord = 72
        Load = 73
        LoadCog = 74
        LastServoTarget = 75
        ServoJCmdNum = 76
        TargetJointPos = 77
        TargetJointVel = 78
        TargetJointAcc = 79
        TargetJointCurrent = 80
        ActualJointCurrent = 81
        ActualTCPForce = 82
        TargetTCPPos = 83
        CollisionLevel = 84
        SpeedScaleManual = 85
        SpeedScaleAuto = 86
        LuaLineNum = 87
        AbnomalStop = 88
        CurrentLuaFileName = 89
        ProgramTotalLine = 90
        SafetyBoxSingal = 91
        WeldVoltage = 92
        WeldCurrent = 93
        WeldTrackVel = 94
        TpdException = 95
        AlarmRebootRobot = 96
        ModbusMasterConnect = 97
        ModbusSlaveConnect = 98
        BtnBoxStopSignal = 99
        DragAlarm = 100
        SafetyDoorAlarm = 101
        SafetyPlaneAlarm = 102
        MotonAlarm = 103
        InterfaceAlarm = 104
        UdpCmdState = 105
        WeldReadyState = 106
        AlarmCheckEmergStopBtn = 107
        TsTmCmdComError = 108
        TsTmStateComError = 109
        CtrlBoxError = 110
        SafetyDataState = 111
        ForceSensorErrState = 112
        CtrlOpenLuaErrCode = 113
        StrangePosFlag = 114
        Alarm = 115
        DriverAlarm = 116
        AliveSlaveNumError = 117
        SlaveComError = 118
        CmdPointError = 119
        IOError = 120
        GripperError = 121
        FileError = 122
        ParaError = 123
        ExaxisOutLimitError = 124
        DriverComError = 125
        DriverError = 126
        OutSoftLimitError = 127
        AxleGenComData = 128
        SocketConnTimeout = 129
        SocketReadTimeout = 130
        TsWebStateComErr = 131
        CheckSum = 132