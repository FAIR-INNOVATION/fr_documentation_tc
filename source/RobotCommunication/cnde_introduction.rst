CNDE簡介
==================

協作機器人可設定網路資料交換協定（以下簡稱CNDE）是一種客戶端透過UDP通訊進行機器人控制和獲取機器人回饋狀態的方式。

表1-1為CNDE可以取得的機器人所有狀態集合，客戶端可以從表中任意挑選若干個需要的狀態，並使機器人依照設定的回饋週期進行狀態回饋。

同樣，客戶端也可以從表1-2中挑選所需的機器人控制功能組合進行機器人控制操作。客戶端和機器人CNDE通訊資料需依照指定的幀格式，機器人CNDE通訊埠為20006。

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

   * - std_DI_box
     - UINT8
     - 控制箱可設定CI輸入(bit0 ~ bit7表示CI0 ~ CI7)

   * - std_DI_box
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

   * - payload_cog
     - DOUBLE_3
     - 負載質心(x,y,z)(mm)

   * - motion_queue_len
     - INT32
     - 當前運動隊列長度

   * - output_BIT_reg_8xX
     - UINT8_X
     - BIT型機器人輸出暫存器(8xX表示暫存器個數，若您需要16個BIT型輸出暫存器，則實際名稱為：“output_BIT_reg_8x2”，機器人最多支援128個BIT型輸出暫存器)

   * - output_INT_reg_X
     - INT32_X
     - INT型機器人輸出暫存器(X表示暫存器個數，若您需要16個INT型輸出暫存器，則實際名稱為：“output_INT_reg_16”，機器人最多支援64個INT型輸出暫存器)

   * - output_DOUBLE_reg_X
     - DOUBLE_X
     - DOUBLE型機器人輸出暫存器(X表示暫存器個數，若您需要16個DOUBLE型輸出暫存器，則實際名稱為：“output_DOUBLE_reg_16”，機器人最多支援64個DOUBLE型輸出暫存器)

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