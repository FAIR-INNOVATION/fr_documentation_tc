CNDE簡介
==================

協作機器人可設定網路資料交換協定（以下簡稱CNDE）是一種客戶端透過UDP通訊進行機器人控制和獲取機器人回饋狀態的方式。

表1-1為CNDE可以取得的機器人所有狀態集合，客戶端可以從表中任意挑選若干個需要的狀態，並使機器人依照設定的回饋週期進行狀態回饋。

同樣，客戶端也可以從表1-2中挑選需要的機器人控制功能組合進行機器人控制操作。客戶端和機器人CNDE通訊數據需按照指定的幀格式，機器人CNDE通訊端口為20005和20006，20005端口用於TCP通訊，20006端口用於UDP通訊。

使用機器人CNDE功能主要有以下四個步驟：

①輸入、輸出資料內容配置：客戶端向機器人發送一條輸入、輸出配置指令，其中指令內容形如“std_DI_box,cfg_DI_box,motion_queue_len”等一系列控製或狀態功能名稱，機器人端記錄並識別這些名稱後向客戶端回饋對應功能資料類型如“UINT8,UINT8,INT32”，即表示配置成功。

②啟動機器人CNDE資料輸出：客戶端向機器人發送一條啟動CNDE資料輸出指令，機器人即開始依照配置的週期以位元組數組(小端模式)的形式將機器人狀態資料透過UDP傳送至客戶端。

③解析機器人狀態數據：客戶端循環接收機器人回饋的狀態數據，並根據輸出配置時機器人回饋的數據類型和表1-3中每個數據類型對應的位元組長度進行數據解析，得到每個狀態的實際數值。機器人CNDE輸出資料最多支援4096個位元組，可配置CNDE輸出週期為1 ~ 200ms。

④發送機器人控制資料：客戶端根據輸入配置時機器人回饋的資料類型和表1-3中每個資料類型對應的位元組長度進行控制資料組包，並透過UDP通訊傳送到機器人，機器人端收到控制資料後進行資料解析和機器人控制操作。機器人CNDE輸入支援256個配方，客戶端可以根據需要先配置多個輸入配方，在向機器人發送輸入資料時需要指定當前資料對應的配方編號。

.. centered:: 表1-1 機器人輸出配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **資料型別**
     - **描述**

   * - std_DI_box
     - UINT8
     - 控制箱標準DI輸入(bit0 ~ bit7表示DI0 ~ DI7)

   * - cfg_DI_box
     - UINT8
     - 控制箱可設定CI輸入(bit0 ~ bit7表示CI0 ~ CI7)

   * - cfg_DI_tool
     - UINT8
     - 控制箱可配置工具DI輸入(bit0 ~ bit2表示toolDI0 ~ toolDI1)

   * - std_AI0_box
     - DOUBLE
     - 控制箱模擬量輸入AI0(0 ~ 4095)

   * - std_AI1_box
     - DOUBLE
     - 控制箱模擬量輸入AI1(0 ~ 4095)

   * - std_AI_tool
     - DOUBLE
     - 末端工具類比量輸入tool_AI0(0 ~ 4095)

   * - run_up_time
     - DOUBLE
     - 機器人開機時間統計(s)

   * - target_joint_pos
     - DOUBLE_6
     - 關節1-6目標位置(°)

   * - target_joint_vel
     - DOUBLE_6
     - 關節1-6目標速度(°/s)

   * - target_joint_acc
     - DOUBLE_6
     - 關節1-6目標加速度(°/s2)

   * - target_joint_current
     - DOUBLE_6
     - 關節1-6目標電流(A)

   * - target_joint_torque
     - DOUBLE_6
     - 關節1-6目標扭力(Nm)

   * - actual_joint_pos
     - DOUBLE_6
     - 關節1-6當前位置(°)

   * - actual_joint_vel
     - DOUBLE_6
     - 關節1-6當前速度(°/s)

   * - actual_joint_current
     - DOUBLE_6
     - 關節1-6當前電流(A)

   * - actual_joint_torque
     - DOUBLE_6
     - 關節1-6目標扭矩(Nm)

   * - actual_TCP_pos
     - DOUBLE_6
     - 工具當前位置DKR(mm)

   * - actual_TCP_vel
     - DOUBLE_6
     - 工具當前速度DKR(mm/s)

   * - actual_TCP_force
     - DOUBLE_6
     - 工具合力DKR(N)

   * - target_TCP_pos
     - DOUBLE_6
     - 工具目標位置DKR(mm)

   * - target_TCP_vel
     - DOUBLE_6
     - 工具目標速度DKR(mm/s)

   * - std_DO_box
     - UINT8
     - 控制箱標準DO輸出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO輸出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool
     - UINT8
     - 控制箱標準工具DO輸出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模擬量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模擬量AO1 (0.0 ~ 4095.0)

   * - std_AO_tool
     - DOUBLE
     - 工具模擬量AO1 (0.0 ~ 4095.0)

   * - robot_mode
     - UINT8
     - 機器人模式(0-自動；1-手動)

   * - collision_level
     - UINT8_6
     - 關節1-6碰撞等级(1 ~ 10)

   * - speed_scaling_man
     - DOUBLE
     - 手動模式速度百分比(0 ~ 100)

   * - speed_scaling_auto
     - DOUBLE
     - 自動模式速度百分比(0 ~ 100)

   * - program_state
     - UINT8
     - 機器人程式運作狀態(1-停止；2-運動中；3-暫停；4-拖曳)

   * - line_number
     - INT32
     - 當前程式運行行號

   * - payload
     - DOUBLE
     - 負載質量(kg)

   * - pay_cog
     - DOUBLE_3
     - 負載質心(x,y,z)(mm)

   * - motion_queue_len
     - INT32
     - 當前運動隊列長度

   * - ft_sensor_data
     - DOUBLE_6
     - 力感測器原始數據

   * - main_code
     - INT32
     - 主故障碼

   * - sub_code
     - INT32
     - 子故障碼

   * - emergency_stop
     - UINT8
     - 急停狀態

   * - motion_done
     - INT32
     - 運動完成狀態

   * - timestamp_us
     - UINT64
     - 機器人系統時間(us)

   * - output_BIT_reg_8xX
     - UINT8_X
     - BIT型機器人輸出暫存器(8xX表示暫存器個數，若您需要16個BIT型輸出暫存器，則實際名稱為：“output_BIT_reg_8x2”，機器人最多支援128個BIT型輸出暫存器)

   * - output_INT_reg_X
     - INT32_X
     - INT型機器人輸出暫存器(X表示暫存器個數，若您需要16個INT型輸出暫存器，則實際名稱為：“output_INT_reg_16”，機器人最多支援64個INT型輸出暫存器)

   * - output_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型機器人輸出暫存器(X表示暫存器個數，若您需要16個DOUBLE型輸出暫存器，則實際名稱為：“output_DOUBLE_reg_16”，機器人最多支援64個DOUBLE型輸出暫存器)

   * - servoj_time
     - UINT64_5
     - servoj時間戳數據,單位納秒

   * - actual_joint_temp
     - DOUBLE_6
     - 關節j1-j6驅動器溫度，單位°

   * - axle_gen_com_data
     - UINT8_130
     - 末端通用週期性數據

   * - abnormal_stop
     - UINT8
     - 異常狀態，0：無異常，1：有異常

   * - cur_lua_file_name
     - UINT8_256
     - 當前運行lua文件名稱

   * - prog_total_line
     - UINT8
     - 當前文件總行數

   * - safety_box_signal
     - UINT8_6
     - 按鈕盒按鍵信號 0：按下  1：鬆開

   * - welding_voltage
     - DOUBLE
     - 實際焊接電壓，單位V

   * - welding_current
     - DOUBLE
     - 實際焊接電流，單位A

   * - welding_track_speed
     - DOUBLE
     - 焊縫跟蹤速度mm/s

   * - tpd_exception
     - UINT8
     - TPD異常

   * - alarm_reboot_robot
     - UINT8
     - 機器人重啟警告

   * - modbus_master_connect
     - UINT8
     - | Modbus8個主站的連接狀態  
       | bit0-bit7代表0-7個主站0-未連接，1-已連接

   * - modbus_slave_connect
     - UINT8
     - Modbus從站連接狀態 0-未連接 1-已連接

   * - btn_box_stop_signal
     - UINT8
     - 急停按鈕信號

   * - drag_alarm
     - UINT8
     - 拖動警告

   * - safety_door_alarm
     - UINT8
     - 安全門警告，0無警告，1安全門觸發

   * - safety_plane_alarm
     - UINT8
     - 安全牆警告，0無警告，1進入安全牆

   * - motion_alarm
     - UINT8
     - | 運動警告，0-無警告，
       | 1-LIN指令姿態變化過大，
       | 2-TCP超速，
       | 3-發生碰撞，
       | 4-1軸超過最大速度，
       | 5-2軸超過最大速度，
       | 6-3軸超過最大速度，
       | 7-4軸超過最大速度，
       | 8-5軸超過最大速度，
       | 9-6軸超過最大速度，
       | 10-1軸關節指令與反饋偏差過大，
       | 11-2軸關節指令與反饋偏差過大，
       | 12-3軸關節指令與反饋偏差過大，
       | 13-4軸關節指令與反饋偏差過大，
       | 14-5軸關節指令與反饋偏差過大，
       | 15-6軸關節指令與反饋偏差過大，
       | 16-奇異位姿，
       | 17-LIN指令運動速度自適應，
       | 18-目標速度調整超時或調速未完成，
       | 19-旋轉插入運動失敗，
       | 20-螺旋插入運動失敗，
       | 21-直線插入運動失敗，
       | 22-表面定位運動失敗

   * - interfere_alarm
     - UINT8
     - 干涉區警告，0無警告，1進入干涉區

   * - udp_cmd_state
     - INT32
     - UDP連接狀態

   * - weld_ready_state
     - UINT8
     - 焊機準備好狀態，1：準備好，0：焊機錯誤

   * - alarm_check_emerg_stop_btn
     - UINT8
     - 關節通訊異常警告

   * - ts_tm_cmd_com_error
     - UINT8
     - 扭矩系統指令錯誤

   * - ts_tm_state_com_error
     - UINT8
     - 扭矩系統狀態錯誤

   * - ctrl_box_error
     - INT32
     - 控制箱錯誤

   * - safety_data_state
     - UINT8
     - 安全數據狀態標誌，0無異常，1-異常

   * - force_sensor_err_state
     - UINT8
     - 力傳感器連接超時故障；bit0-bit1對應力傳感器ID1-ID2

   * - ctrl_open_lua_errcode
     - UINT8_4
     - 控制器開放協議錯誤碼

   * - servo_id
     - UINT8
     - 伺服驅動器ID號

   * - servo_errcode
     - INT32
     - 伺服驅動器故障碼

   * - servo_state
     - INT32
     - 伺服器驅動器狀態

   * - servo_actual_pos
     - DOUBLE
     - 伺服當前位置

   * - servo_actual_speed
     - DOUBLE
     - 伺服當前速度
   
   * - servo_actual_torque
     - DOUBLE
     - 伺服當前轉矩
   
   * - gripper_active
     - INT32
     - 夾爪激活狀態
   
   * - gripper_position
     - UINT8
     - 夾爪位置反饋（百分比）
   
   * - gripper_speed
     - INT32
     - 夾爪速度反饋（百分比）
   
   * - gripper_current
     - INT32
     - 夾爪電流反饋（百分比）
   
   * - gripper_temp
     - INT32
     - 夾爪當前溫度，單位°
   
   * - gripper_voltage
     - INT32
     - 夾爪當前電壓，單位V
   
   * - rotating_gripper_num
     - DOUBLE
     - 旋轉夾爪旋轉圈數反饋
   
   * - rotating_gripper_speed
     - UINT8
     - 旋轉夾爪旋轉速度反饋（百分比）
   
   * - rotating_gripper_tor
     - UINT8
     - 旋轉夾爪旋轉力矩反饋（百分比）
   
   * - weld_break_off_state
     - UINT8
     - 焊接中斷狀態：0-焊接未中斷   1-焊接中斷
   
   * - weld_arc_state
     - UINT8
     - 焊接電弧狀態 0-電弧未中斷 1-電弧已中斷
   
   * - smarttool_state
     - UINT32
     - 末端擴展IO數據(Smart-Tool)
   
   * - tool_coord
     - DOUBLE_6
     - 當前工具相對於末端位姿
   
   * - wobj_coord
     - DOUBLE_6
     - 當前工件相對於基座位姿
   
   * - exTool_coord
     - DOUBLE_6
     - 當前外部工具相對於工具位姿
   
   * - exAxis_coord
     - DOUBLE_6
     - 當前外部軸相對於基座標系位姿
   
   * - robot_state
     - UINT8
     - | 機器人運行狀態， 
       | 1.已經停止;2.正在運動;3.已經暫停;4.拖動
   
   * - actual_flange_pos
     - DOUBLE_6
     - 末端實際位姿
   
   * - target_TCP_cmpvel
     - DOUBLE_2
     - TCP指令線性、姿態速度，單位mm/s、°/s
   
   * - actual_TCP_cmpvel
     - DOUBLE_2
     - TCP實際線性、姿態速度，單位mm/s、°/s
   
   * - tool_id
     - INT32
     - 工具號
   
   * - wobj_id
     - INT32
     - 工件號
   
   * - ft_sensor_raw_data
     - DOUBLE_6
     - 末端力/力矩-傳感器座標系下原始數據
   
   * - ft_sensor_active
     - UINT8
     - 力/扭矩傳感器激活狀態
   
   * - gripper_motion_done
     - UINT8
     - 夾爪運動完成
   
   * - collision_state
     - UINT8
     - 碰撞檢測狀態
   
   * - trajectory_pnum
     - INT32
     - 離散點運動當前序號
   
   * - safety_stop0_state
     - UINT8
     - 安全停止SI0信號狀態
   
   * - safety_stop1_state
     - UINT8
     - 安全停止SI1信號狀態
   
   * - gripper_fault_id
     - UINT8
     - 錯誤夾爪號
   
   * - gripper_fault
     - INT32
     - 夾爪錯誤編號
   
   * - ext_DI_state
     - UINT8_16
     - 擴展DI
   
   * - ext_DO_state
     - UINT8_16
     - 擴展DO
   
   * - ext_AI_state
     - INT32_4
     - 擴展AI
   
   * - ext_AO_state
     - INT32_4
     - 擴展AO
   
   * - rbt_enable_state
     - INT32
     - 驅動器使能完成狀態
   
   * - joint_driver_torque
     - DOUBLE_6
     - 關節j1-j6實際扭矩值，單位Nm
   
   * - robot_time
     - INT32_7
     - 機器人系統時間，年，月，日，時，分，秒，毫秒
   
   * - software_upgrade_state
     - INT32
     - 機器人軟體升級狀態
   
   * - end_lua_err_code
     - INT32
     - 末端按鈕信號狀態
   
   * - wide_voltage_ctrl_box_temp
     - DOUBLE
     - 寬電壓控制箱溫度，單位°
   
   * - wide_voltage_ctrl_box_fan_current
     - INT32
     - 寬電壓控制箱風扇電流
   
   * - last_servoJ_target
     - DOUBLE_6
     - 最後一個servoJ目標指令位姿
   
   * - servoJ_cmd_num
     - INT32
     - servoJ指令計數
   
   * - strange_pos_flag
     - UINT8
     - 奇異位姿標誌
   
   * - alarm
     - UINT8
     - | 警告，0-無警告，  
       | 1-肩關節配置變化，
       | 2-肘關節配置變化，  
       | 3-腕關節配置變化，
       | 4-RPY初始化失敗，  
       | 5-WaitDI等待超時，
       | 6-WaitAI等待超時，  
       | 7-WaitToolDI等待超時，
       | 8-WaitToolAI等待超時，  
       | 9-起弧成功DI未配置，
       | 10-WaitAuxDI等待超時，  
       | 11-WaitAuxAI等待超時，
       | 12-擺動軌跡中存在不可到達點位，  
       | 13-傳送帶跟蹤抓取點計算失敗，
       | 14-關節扭矩傳感器數據異常
   
   * - dr_alarm
     - UINT8
     - | 驅動器警告，0-無警告，
       | 1-1軸驅動器警告，可復位，  
       | 2-2軸驅動器警告，可復位，
       | 3-3軸驅動器警告，可復位，  
       | 4-4軸驅動器警告，可復位，
       | 5-5軸驅動器警告，可復位，  
       | 6-6軸驅動器警告，可復位
   
   * - alive_slave_num_error
     - UINT8
     - 活動從站數量故障，0-無故障，1-錯誤，不可復位
   
   * - slave_com_error
     - UINT8_8
     - | 從站通信故障，0-無故障，
       | 1-從站掉線，  
       | 2-從站狀態與設置值不一致，
       | 3-從站未配置，  
       | 4-從站配置錯誤，
       | 5-從站初始化錯誤，  
       | 6-從站郵箱通信初始化錯誤
   
   * - cmd_point_error
     - UINT8
     - | 指令點故障，0-無故障，
       | 1-關節指令點錯誤，  
       | 2-直線目標點錯誤，
       | 3-圓弧中間點錯誤，  
       | 4-圓弧目標點錯誤，
       | 5-圓弧指令點間距過小，  
       | 6-整圓/螺旋線中間點1錯誤，
       | 7-整圓/螺旋線中間點2錯誤，  
       | 8-整圓/螺旋線中間點3錯誤，
       | 9-整圓/螺旋線指令點間距過小，  
       | 10-TPD指令點錯誤，
       | 11-TPD指令工具與當前工具不符，  
       | 12-TPD當前指令與下一指令起始點偏差過大，
       | 13-內外部工具切換錯誤，  
       | 14-新螺旋線起點錯誤，
       | 15-新樣條曲線指令點錯誤，  
       | 17-PTP關節指令超限，
       | 18-TPD關節指令超限，  
       | 19-LIN\ARC下發關節指令超限，
       | 20-笛卡爾空間內指令超速，  
       | 21-關節空間內扭矩指令超限，
       | 22-JOG關節指令超限，  
       | 23-軸1關節空間內指令速度超限，
       | 24-軸2關節空間內指令速度超限，  
       | 25-軸3關節空間內指令速度超限，
       | 26-軸4關節空間內指令速度超限，  
       | 27-軸5關節空間內指令速度超限，
       | 28-軸6關節空間內指令速度超限，  
       | 29-關節反饋速度超限，
       | 30-關節指令與反饋偏差過大，  
       | 31-DMP目標點錯誤（包括工具不符），
       | 32-TCP速度超限，  
       | 33-下一指令關節配置發生變化，
       | 34-當前指令關節配置發生變化，  
       | 35-LIN指令中關節速度超限，
       | 36-LIN指令自適應速度超出閾值，  
       | 37-軌跡中存在不可到達點位，
       | 38-軌跡中存在不可到達點位-奇異位姿，  
       | 49-ARCSTART和ARCEND之間不允許PTP和SPTP指令，
       | 50-WEAVESTART和WEAVEEND之間不允許PTP和SPTP指令，  
       | 51-擺焊參數錯誤，
       | 52-擺焊指令點間距過小，  
       | 53-擺動軌跡中存在不可到達點位-奇異位姿，
       | 54-擺動軌跡中存在不可到達點位-關節指令超限，
       | 55-擺動軌跡中存在不可到達點位-規劃異常（工具Z與前進方向X夾角重合），
       | 56-擺動軌跡中存在不可到達點位-規劃異常（圓弧路點錯誤），
       | 65-激光傳感器指令偏差過大，  
       | 66-激光傳感器指令中斷，焊縫跟蹤提前結束，
       | 81-外部軸指令速度超限，  
       | 82-外部軸指令與反饋偏差過大，
       | 83-擴展外設(外部軸/IO)通信中斷，  
       | 84-擴展外設(外部軸/IO)通信丟包異常，
       | 85-外部軸1關節空間內指令速度超限，  
       | 86-外部軸2關節空間內指令速度超限，
       | 87-外部軸3關節空間內指令速度超限，  
       | 88-外部軸4關節空間內指令速度超限，
       | 89-擴展外設(外部軸/IO)Ethercat通信錯誤，  
       | 90-擴展外設(外部軸/IO)Canopen通信錯誤，
       | 97-傳送帶跟蹤-起始點與參考點姿態變化過大，  
       | 113-恆力控制-X方向超過最大調整距離，
       | 114-恆力控制-Y方向超過最大調整距離，  
       | 115-恆力控制-Z方向超過最大調整距離，
       | 116-恆力控制-RX方向超過最大調整角度，  
       | 117-恆力控制-RY方向超過最大調整角度，
       | 118-恆力控制-RZ方向超過最大調整角度，  
       | 119-外部傳感器數據錯誤，
       | 120-螺旋線探索運動失敗，  
       | 121-旋轉插入運動失敗，
       | 122-直線插入運動失敗，  
       | 123-表面定位運動失敗，
       | 124-拖動力異常，進入拖動失敗，  
       | 129-超過最大扭矩記錄點數，
       | 130-速度切換錯誤，  
       | 131-工具方向超限，  
       | 132-動量超限，
       | 133-功率超限，  
       | 134-STL-Flash診斷異常，  
       | 135-STL-RAM診斷異常，
       | 136-STL-CPU診斷異常，  
       | 137-安全板II-ECAT安全數據異常，
       | 138-1軸ECAT安全數據異常，  
       | 139-2軸ECAT安全數據異常，
       | 140-3軸ECAT安全數據異常，  
       | 141-4軸ECAT安全數據異常，
       | 142-5軸ECAT安全數據異常，  
       | 143-6軸ECAT安全數據異常，
       | 145-安全板與控制器通訊異常，  
       | 147-焦點跟隨錯誤，
       | 148-姿態速度超限，  
       | 149-關節狀態字反饋異常
   
   * - IO_error
     - UINT8
     - | IO故障，0-無故障，
       | 1-通道錯誤，可復位，  
       | 2-數值錯誤，可復位，
       | 3-WaitDI等待超時，可復位，  
       | 4-WaitAI等待超時，可復位，
       | 5-WaitAxleDI等待超時，可復位，  
       | 6-WaitAxleAI等待超時，可復位，
       | 7-通道已配置功能錯誤，可復位，  
       | 8-起弧超時，可復位，
       | 9-收弧超時，可復位，  
       | 10-尋位超時，可復位，
       | 11-傳送帶IO檢測超時，可復位，  
       | 12-WaitAuxDI等待超時，可復位，
       | 13-WaitAuxAI等待超時，可復位，  
       | 14-焊絲尋位超時，可復位
   
   * - gripper_error
     - UINT8
     - 夾爪故障，0-無故障，1-夾爪運動超時錯誤，可復位
   
   * - file_error
     - UINT8
     - | 配置文件故障，0-無故障，
       | 1-zbt配置文件版本錯誤，初始化錯誤-不可復位，
       | 2-zbt配置文件加載失敗，初始化錯誤-不可復位，
       | 3-user配置文件版本錯誤，初始化錯誤-不可復位，
       | 4-user配置文件加載失敗，初始化錯誤-不可復位，
       | 5-exaxis配置文件版本錯誤，初始化錯誤-不可復位，
       | 6-exaxis配置文件加載失敗，初始化錯誤-不可復位，
       | 7-機器人型號不一致，需要重新設置-不可復位，
       | 8-dhpara配置文件版本錯誤，初始化錯誤-不可復位，
       | 9-dhpara配置文件加載失敗，初始化錯誤-不可復位，
       | 10-機器人型號未設置-不可復位，
       | 11-load配置文件版本錯誤，初始化錯誤-不可復位，
       | 12-load配置文件加載失敗，初始化錯誤-不可復位，
       | 13-speed配置文件版本錯誤，初始化錯誤-不可復位，
       | 14-speed配置文件加載失敗，初始化錯誤-不可復位，
       | 15-weavepara配置文件版本錯誤，初始化錯誤-不可復位，
       | 16-weavepara配置文件加載失敗，初始化錯誤-不可復位
   
   * - para_error
     - UINT8
     - | 配置參數故障，0-無故障，
       | 1-工具號超限錯誤-可復位，  
       | 2-定位完成閾值錯誤-可復位，
       | 3-碰撞等級錯誤-可復位，  
       | 4-負載重量錯誤-可復位，
       | 5-負載質心X錯誤-可復位，  
       | 6-負載質心Y錯誤-可復位，
       | 7-負載質心Z錯誤-可復位，  
       | 8-DI濾波時間錯誤-可復位，
       | 9-AxleDI濾波時間錯誤-可復位，  
       | 10-AI濾波時間錯誤-可復位，
       | 11-AxleAI濾波時間錯誤-可復位，  
       | 12-DI高低電平範圍錯誤-可復位，
       | 13-DO高低電平範圍錯誤-可復位，  
       | 14-工件號超限錯誤-可復位，
       | 15-外部軸號超限錯誤-可復位，  
       | 16-傳送帶跟蹤-編碼器通道錯誤-可復位，
       | 17-傳送帶跟蹤-工件軸號錯誤-可復位，  
       | 18-FR30L安裝方式-非正裝錯誤-可復位
   
   * - exaxis_out_slimit_error
     - UINT8
     - | 外部軸軟限位故障，0-無故障，
       | 1-外部軸1軸超出軟限位故障，可復位，  
       | 2-外部軸2軸超出軟限位故障，可復位，
       | 3-外部軸3軸超出軟限位故障，可復位，  
       | 4-外部軸4軸超出軟限位故障，可復位，
       | 5-外部軸5軸超出軟限位故障，可復位，  
       | 6-外部軸6軸超出軟限位故障，可復位
   
   * - dr_com_err
     - UINT8_6
     - 驅動器通信故障，0-無故障，1-故障
   
   * - dr_err
     - UINT8
     - | 驅動器故障，0-無故障，
       | 1-1軸驅動器故障，不可復位，  
       | 2-2軸驅動器故障，不可復位，
       | 3-3軸驅動器故障，不可復位，  
       | 4-4軸驅動器故障，不可復位，
       | 5-5軸驅動器故障，不可復位，  
       | 6-6軸驅動器故障，不可復位
   
   * - out_sflimit_err
     - UINT8
     - | 軟限位故障，0-無故障，
       | 1-1軸超出軟限位故障，可復位，  
       | 2-2軸超出軟限位故障，可復位，
       | 3-3軸超出軟限位故障，可復位，  
       | 4-4軸超出軟限位故障，可復位，
       | 5-5軸超出軟限位故障，可復位，  
       | 6-6軸超出軟限位故障，可復位
  
.. centered:: 表1-2 機器人輸入控製配置功能

.. list-table::
   :widths: 20 40 80
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **資料型別**
     - **描述**

   * - speed_mask
     - UINT8
     - 全域速度設定遮罩：0-不生效；1-生效

   * - speed
     - UINT8
     - 設定全域速度（0-100）

   * - std_DO_mask
     - UINT8
     - 控制箱標準DO輸出控制遮罩(bit0 ~ bit7表示DO0 ~ DO7)

   * - std_DO_box
     - UINT8
     - 控制箱標準DO輸出(bit0 ~ bit7表示DO0 ~ DO7)

   * - cfg_DO_mask
     - UINT8
     - 控制箱可配置CO輸出控制遮罩(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_box
     - UINT8
     - 控制箱可配置CO輸出(bit0 ~ bit7表示CO0 ~ CO7)

   * - cfg_DO_tool_mask
     - UINT8
     - 控制箱標準工具DO輸出控制遮罩(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - cfg_DO_tool
     - UINT8
     - 控制箱標準工具DO輸出(bit0 ~ bit1表示toolDO0 ~ toolDO1)

   * - std_AO_mask
     - UINT8
     - 機器人類比輸出控制遮罩(bit0 ~ bit1表示控制箱AO0 ~ AO1；bit2表示工具AO0)

   * - std_AO0_box
     - DOUBLE
     - 控制箱模擬量AO0 (0.0 ~ 4095.0)

   * - std_AO1_box
     - DOUBLE
     - 控制箱模擬量AO1 (0.0 ~ 4095.0)

   * - std_AO0_tool
     - DOUBLE
     - 工具模擬量AO1 (0.0 ~ 4095.0)

   * - input_BIT_reg_8xX
     - UINT8_X
     - BIT型機器人輸入暫存器(8xX表示暫存器個數，若您需要16個BIT型輸入暫存器，則實際名稱為：“input_BIT_reg_8x2”，機器人最多支援128個BIT型暫存器)

   * - input_INT_reg_X
     - INT32_X
     - INT型機器人輸入暫存器(X表示暫存器個數，若您需要16個INT型輸入暫存器，則實際名稱為：“input_INT_reg_16”，機器人最多支援64個INT型暫存器)
  
   * - input_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型機器人輸入暫存器(X表示暫存器個數，若您需要16個DOUBLE型輸入暫存器，則實際名稱為：“input_DOUBLE_reg_16”，機器人最多支援64個DOUBLE型暫存器)

.. centered:: 表1-3 資料型別及位元組長度對應關係

.. list-table::
   :widths: 60 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **資料型別**
     - **位元組長度**

   * - UINT8
     - 1

   * - INT32
     - 4

   * - DOUBLE
     - 8

   * - UINT8_X
     - 1*X

   * - INT32_X
     - 4*X

   * - DOUBLE_X
     - 8*X