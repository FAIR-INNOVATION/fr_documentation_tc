版本更新说明
====================

.. toctree:: 
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **版本号**
     - **日期**
     - **更新描述**

   * - V3.9.9
     - 2026-09-01
     - | 1.更新獲取夾爪運動狀態介面GetGripperMotionDone()，更新夾爪狀態輸出參數定義及使用範圍；
       | 2.修改GetInverseKinExaxis()包含擴展軸位置的逆運動學求解介面，增加關節配置參數，預設值為-1參考目前關節配置；
       | 3.修改FT_SpiralSearch()、FT_LinInsertion()、FT_FindSurface()力控介面增加未檢測到力/力矩的處理策略參數；
       | 4.修改SetDIConfig()、GetDIConfig()、SetDOConfig()、GetDOConfig()機器人控制箱CIO
       | 5.功能配置介面參數描述，更新新增的功能名稱及功能碼；新增獲取安全配置參數校驗和介面GetSafetyParamsCheckSum()；
       | 6.修改機器人基礎控制代碼示例，增加手動高速模式切換代碼示例；
       | 7.新增安全操作密碼校驗介面SafetyOPPasswordCheck()；
       | 8.新增等待夾爪運動狀態介面GripperWaitMotionDone()，支援逾時和策略設定（僅適用於末端開放協定）；
       | 9.新增同步系統時間至機器人介面SetRobottime()；
       | 10.新增關節空間伺服模式運動介面ServoJ()，支援多點位一次輸入；
       | 11.新增雷射記錄復現+常規擺動代碼示例；
       | 12.新增雷射記錄復現+擴展軸非同步運動+定點擺動代碼示例；
       | 13.新增螺旋線探索介面FT_SpiralSearch()；
       | 14.新增切換手動高速模式介面HiSpeedManualSwitch()；
       | 15.新增安全雙通道CI功能配置介面SetSafetyDIConfig()；
       | 16.新增安全雙通道CO功能配置介面SetSafetyDOConfig()；
       | 17.新增安全雙通道CI/CO功能配置設定-讀取-清零驗證示例。

   * - V3.9.8
     - 2026-07-27
     - | 1.更新機器人狀態回饋結構體，增加目前機器人Lua程式運行狀態，0-程式未運行；1-程式運行中(包含程式暫停)；
       | 2.SetExToolCoord()、SetExToolList()設置外部工具座標系和工具座標系列表介面更新參數描述，其中外部工具座標系編號更新為20-39。並更新外部工具座標系操作代碼示例。
       | 3.GetToolCoordWithID()獲取工具座標系參數介面增加工具類型、安裝位置、工具ID、負載編號參數獲取。
       | 4.GetWObjCoordWithID()獲取工件座標系參數介面增加參考座標系參數獲取；
       | 5.GetExToolCoordWithID()獲取外部工具座標系參數介面增加機器人末端安裝工件座標系位姿參數獲取。
       | 6.GetExAxisCoordWithID()獲取擴展軸座標系參數介面增加擴展軸號和標定標誌參數獲取。
       | 7.SetVelReducePara()設置機器人安全速度介面增加機器人關節安全速度參數設置。
       | 8.設置焊接參數代碼示例中增加焊機控制模式獲取示例。
       | 9.設置擴展IO焊接信號代碼示例增加獲取擴展DI、擴展DO功能配置代碼示例。
       | 10.新增設置機器人關節安全速度代碼示例；
       | 11.新增WaitStationaryMotionDone()等待原地空運動完成介面；
       | 12.新增SetStationaryTrackPara()輸送帶原地跟蹤參數配置介面，及輸送帶原地跟蹤代碼示例；
       | 13.新增WorkPieceTrsfStart()、WorkPieceTrsfEnd()工件座標系轉換開始、結束介面，及工件座標系轉換代碼示例。
       | 14.增加GetWeldMachineCtrlMode()獲取焊機控制模式介面。
       | 15.增加GetExtDIConfig()、GetExtDOConfig()獲取擴展DI功能、擴展DO功能介面。
       
   * - V3.9.7
     - 2026-06-25
     - | 1.PhotoelectricSensorTCPCalibration()參數可自適應無路徑的檔案名稱；
       | 2.LoadTrajectoryJ()參數可自適應無路徑的檔案名稱；
       | 3.LoadTrajectoryLA()參數可自適應無路徑的檔案名稱；
       | 4.LoadDefaultProgConfig()參數可自適應無路徑的檔案名稱；
       | 5.ProgramLoad()參數可自適應無路徑的檔案名稱；
       | 6.SetAxleLuaEnableDeviceType()介面增加靈巧手啟用狀態參數；
       | 7.GetAxleLuaEnableDeviceType()介面增加靈巧手啟用狀態參數；
       | 8.修改獲取當前配置的末端設備啟用類型、夾爪動作控制介面；
       | 9.新增靈巧手使能及功能碼；
       | 10.新增SetDexterousHandsMove ()控制靈巧手運動介面；
       | 11.新增SetDexterousHandsAct ()控制靈巧手復位激活介面；
       | 12.新增ClearDexterousHandsError ()清除靈巧手錯誤介面；
       | 13.新增SetDexterousHandsFunc()設置啟用靈巧手動作控制功能介面；
       | 14.新增GetDexterousHandsFunc()獲取啟用靈巧手動作控制功能介面；
       | 15.新增設置、獲取擺動結束回週期零點介面；
       | 16.新增SetWeaveOffsetRT()設置擺動實時偏移、SetSpeedInstant()實時設置速度介面。

   * - V3.9.6
     - 2026-05-26
     - | 1.更新機器人狀態反饋結構體，增加擴展軸座標系編號狀態；
       | 2.更新機器人狀態反饋配置枚舉類型，增加擴展軸座標系編號配置枚舉；
       | 3.新增ExtAxisGetParamConfig()獲取UDP擴展軸參數配置接口。
       | 4.新增ServoJV()機器人關節空間速度伺服模式運動接口。
       | 5.新增ServoMITStart()機器人關節MIT控制開始接口。
       | 6.新增ServoMITEnd()機器人關節MIT控制結束接口。
       | 7.新增ServoMIT()機器人關節MIT控制接口。
       | 8.新增SetLaserWeldingParam()機器人雷射焊接參數配置接口。
       | 9.新增SetLaserWeldingStartEnd()設置機器人雷射焊接開啟停止接口。
       | 10.新增SetLaserWeldingEnable()設置雷射焊機使能去使能接口。
       | 11.新增ResetLaserWeldingErr()設置雷射焊機故障復位接口。
       | 12.新增GetLaserWeldingRunningState()獲取雷射焊機運行狀態接口。
       | 13.新增GetLaserWeldingErrState()獲取雷射焊機故障狀態接口。
       | 14.新增GetLaserWeldingParamTarget()獲取雷射焊接配置參數接口。
       | 15.新增GetLaserWeldingParamActual()獲取當前雷射焊機生效的配置參數接口。
       | 16.新增SetLaserWeldingEnableExtDoNum()配置雷射焊機擴展IO使能DO端口接口。
       | 17.新增SetLaserWeldingStartExtDoNum()配置雷射焊機擴展IO啟動DO端口接口。
       | 18.新增SetLaserWeldingErrResetExtDoNum()配置雷射焊機擴展IO故障復位DO端口接口。
       | 19.新增SetLaserWeldingRunningStateExtDiNum()配置雷射焊機擴展IO運行狀態（出光狀態）DI端口接口。
       | 20.新增SetLaserWeldingErrStateExtDiNum()配置雷射焊機擴展IO故障狀態DI端口接口。

   * - V3.9.5
     - 2026-04-24
     - | 1.SetTrajectoryJSpeed()接口新增模式降速模式、直接切换；
       | 2.FieldBusSlaveWriteAO()接口更改写入数值类型为double类型，其中AO0~AO15为整型，AO16~AO31为浮点型；
       | 3.FieldBusSlaveReadAI()接口更改读取数值类型为double类型，其中AI0~AI15为整形，AI16~AI31为浮点型；
       | 4.更新机器人状态反馈结构体类型；
       | 5.新增机器人状态反馈配置枚举类型；新增SetRobotRealtimeStateConfig()配置机器人CNDE状态反馈接口；
       | 6.新增AddRobotRealtimeState()CNDE状态配置添加一个机器人状态接口；
       | 7.新增DeleteRobotRealtimeState()CNDE状态配置删除一个机器人状态接口；
       | 8.新增SetRobotRealtimeStatePeriod()设置CNDE状态反馈周期接口；
       | 9.新增GetRobotRealtimeStateConfig()获取当前CNDE状态反馈所有状态集合和周期接口。

   * - V3.9.4
     - 2026-03-25
     - | 1.ServoJTStart()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 2.ServoJTEnd()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 3.ServoJT()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 4.ServoMoveStart()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 5.ServoMoveEnd()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 6.ServoJ()接口新增通信類型選擇參數，支持XMLRPC/UDP通信；
       | 7.SetWeldMachineCtrlMode()接口新增控制模式選擇參數；
       | 8.ExtDevGetUDPComParam()接口新增獲取UDP通信參數：重啟控制箱後是否自動重連；
       | 9.新增SetAxleGenComEnable()開啟末端通用透傳功能接口；
       | 10.新增SndRcvAxleGenComCmdData()末端發送非週期數據並等待應答接口；
       | 11.新增SetRobotStopOnComDisc()設置端口通訊斷開時停止機器人運行接口；
       | 12.新增GetRobotStopOnComDisc()獲取端口通訊斷開時停止機器人運行參數接口；
       | 13.新增SetDIConfig()設置控制箱可配置 CI 端口功能接口；
       | 14.新增GetDIConfig()獲取控制箱可配置 CI 端口功能接口；
       | 15.新增SetDOConfig()設置控制箱可配置 CO 端口功能接口；
       | 16.新增GetDOConfig()獲取控制箱可配置 CO 端口功能接口；
       | 17.新增SetToolDIConfig()設置末端可配置 End-CI 端口功能接口；
       | 18.新增GetToolDIConfig()獲取末端可配置 End-CI 端口功能接口；
       | 19.新增SetDIConfigLevel()設置控制箱可配置 CI 有效狀態接口；
       | 20.新增GetDIConfigLevel()獲取控制箱可配置 CI 有效狀態接口；
       | 21.新增SetDOConfigLevel()設置控制箱可配置 CO 有效狀態接口；
       | 22.新增GetDOConfigLevel()獲取控制箱可配置 CO 有效狀態接口；
       | 23.新增SetToolDIConfigLevel()設置末端可配置 CI 有效狀態接口；
       | 24.新增GetToolDIConfigLevel()獲取末端可配置 CI 有效狀態接口；
       | 25.新增SetStandardDILevel()設置控制箱標準 DI 有效狀態接口；
       | 26.新增GetStandardDILevel()獲取控制箱標準 DI 有效狀態接口；
       | 27.新增SetStandardDOLevel()設置控制箱標準 DO 有效狀態接口；
       | 28.新增GetStandardDOLevel()獲取控制箱標準 DO 有效狀態接口；
       | 29.新增SetExAxisCmdDoneTimeUDP() 擴展軸定位完成時間設置接口；
       | 30.新增SendUDPFrameUDP ()發送指令幀接口；
       | 31.新增SetUDPCmdRpyCallback()設置 SDK 通過 UDP 發送指令的執行結果回調函數接口；
       | 32.新增SetVelReducePara()設置安全速度參數接口；
       | 33.新增OriginPointWeaveStart()定點擺動開始接口；
       | 34.新增OriginPointWeaveEnd()定點擺動結束接口；
       | 35.新增SetUserLEDColor()設置用戶自定義機器人末端燈色接口；
       | 36.新增MoveToTPDStart()運動到 TPD 軌跡記錄起點接口；
       | 37.新增OpenLuaDownload()下載開放協議 Lua 文件接口；
       | 38.新增OpenLuaDelete()刪除開放協議 Lua 文件接口；
       | 39.新增AllOpenLuaDelete()刪除開放協議 Lua 文件接口；

   * - V3.9.3
     - 2026-02-11
     - | 1.ServoCart()介面增加擴展軸參數
       | 2.SetOutputResetCtlBoxDO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 3.SetOutputResetCtlBoxAO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 4.SetOutputResetAxleDO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 5.SetOutputResetAxleAO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 6.SetOutputResetExtDO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 7.SetOutputResetExtAO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 8.SetOutputResetSmartToolDO()介面增加暫停恢復後是否重載復位前DO狀態參數
       | 9.增加GetInverseKinExaxis()包含擴展軸位置的逆運動學求解介面

   * - V3.9.2
     - 2026-01-26
     - | 1. FT_RotInsertion() 介面增加未偵測到力/力矩的處理策略參數
       | 2. LaserSensorRecordandReplay() 介面增加機器人定點追蹤相關參數
       | 3. 新增 MoveStationary() 介面
       | 4. 新增 TCPComputeRPY() 介面
       | 5. 新增 TCPComputeXYZ() 介面
       | 6. 新增 TCPRecordFlangePosStart() 介面
       | 7. 新增 TCPRecordFlangePosEnd() 介面
       | 8. 新增 TCPGetRecordFlangePos() 介面
       | 9. 新增 PhotoelectricSensorTCPCalibration() 介面

   * - V3.9.1
     - 2025-12-25
     - | 1. MoveL() 介面增加 oacc 速度縮放因子參數 / 物理加速度參數；
       | 2. MoveC() 介面增加 oacc 速度縮放因子參數 / 物理加速度參數；
       | 3. Circle() 介面優化關於物理速度和物理加速度的參數描述；
       | 4. 增加 FT_Control() 重載函數，具有 rx、ry 啟動閾值、力矩調節係數參數；
       | 5. 增加 SerCoderCompenParams() 介面；

   * - V3.9.0
     - 2025-11-26
     - | 1. JointSensitivityCalibration() 介面增加 j1~j6 關節線性度回傳；
       | 2. 增加 JointHysteresisError() 介面；
       | 3. 增加 JointRepeatability() 介面；
       | 4. 增加 SetAdmittanceParams() 介面；
       | 5. 增加 MoveToIntersectLineStart() 介面；
       | 6. 增加 MoveIntersectLine() 介面；
       
   * - V3.8.7
     - 2025-10-21
     - | 1.NewSpiral()接口增加velAccMode参数
       | 2.FT_Control()增加质量参数和阻尼参数接口
       | 3.增加JointSensitivityCalibration()接口
       | 4.增加JointSensitivityCollect()接口
       | 5.增加MotionQueueClear()接口
       | 6.增加GetSlavePortErrCounter()接口
       | 7.增加SlavePortErrCounterClear()接口
       | 8.增加SetVelFeedForwardRatio()接口
       | 9.增加GetVelFeedForwardRatio()接口
       | 10.增加RobotMCULogCollect()接口
       | 11.状态结构体增加队列中最后一个ServoJ目标位置，ServoJ指令计数

   * - V3.8.6
     - 2025-09-19
     - | 1.SetLoadCoord()接口增加负载编号参数
       | 2.增加LaserTrackingLaserOnOff()接口
       | 3.增加LaserTrackingTrackOnOff()接口
       | 4.增加LaserTrackingSearchStart_xyz()接口
       | 5.增加LaserTrackingSearchStart_point()接口
       | 6.增加LaserTrackingSearchStop()接口
       | 7.增加LaserTrackingSensorConfig()接口
       | 8.增加LaserTrackingSensorSamplePeriod()接口
       | 9.增加LoadPosSensorDriver()接口
       | 10.增加UnLoadPosSensorDriver()接口
       | 11.增加LaserSensorRecord1()接口
       | 12.增加LaserSensorReplay()接口
       | 13.增加MoveLTR()接口
       | 14.增加LaserSensorRecordandReplay()接口
       | 15.增加MoveToLaserRecordStart()接口
       | 16.增加MoveToLaserRecordEnd()接口
       | 17.增加MoveToLaserSeamPos()接口
       | 18.增加GetLaserSeamPos()接口
       | 19.增加ImpedanceControlStartStop()接口
       | 20.增加GetToolCoordWithID()接口
       | 21.增加GetWObjCoordWithID()接口
       | 22.增加GetExToolCoordWithID()接口
       | 23.增加GetExAxisCoordWithID()接口
       | 24.增加GetTargetPayloadWithID()接口
       | 25.增加GetExAxisCoordWithID()接口
       | 26.增加GetCurWObjCoord()接口
       | 27.增加GetCurExToolCoord()接口
       | 28.增加GetCurExToolCoord()接口
       | 29.增加KernelUpgrade()接口
       | 30.增加GetKernelUpgradeResult()接口
       | 31.增加CustomWeaveSetPara()接口
       | 32.增加CustomWeaveGetPara()接口
       | 33.状态结构体增加工具、工件、外部工具、扩展轴坐标系和负载质量、质心数据

   * - V3.8.5
     - 2025-08-20
     - | 1.MoveL()接口增加逆运动学config参数，velAccParamMode参数
       | 2.MoveC()接口增加逆运动学config参数，velAccParamMode参数
       | 3.Circle()接口增加逆运动学config参数，velAccParamMode参数
       | 4.NewSpiral()接口增加逆运动学config参数
       | 5.NewSplinePoint()接口增加逆运动学config参数
       | 6.ExtAxisSyncMoveJ()接口增加逆运动学config参数
       | 7.ExtAxisSyncMoveL()接口增加逆运动学config参数
       | 8.ExtAxisSyncMoveC()接口增加逆运动学config参数
       | 9.新增LaserRecordPoint(coordID)接口
       | 10.新增SetExAxisRobotPlan(strategy)接口
       | 11.新增OpenLuaUpload(filePath)接口
       | 12.新增GetFieldBusConfig()接口
       | 13.新增FieldBusSlaveWriteDO(DOIndex,wirteNum,status)接口
       | 14.新增FieldBusSlaveWriteAO(AOIndex,wirteNum,status)接口
       | 15.新增FieldBusSlaveReadDI(DOIndex,readeNum)接口
       | 16.新增FieldBusSlaveReadAI(AOIndex,readeNum)接口
       | 17.新增FieldBusSlaveWaitDI(DIIndex,status,waitMs)接口
       | 18.新增FieldBusSlaveWaitAI(AIIndex,waitType,value,waitMs)接口
       | 19.新增SetSuckerCtrl(slaveID,len,ctrlValue)接口
       | 20.新增GetSuckerState(slaveID)接口
       | 21.新增WaitSuckerState(slaveID,state,ms)接口

   * - V3.8.4
     - 2025-07-17
     - | 1.ExtAxisMove()接口增加blend平滑参数
       | 2.增加SetFocusCalibPoint(pointNum,point)接口
       | 3.增加ComputeFocusCalib(pointNum)接口
       | 4.增加FocusStart(kp,kpredic,aMax,vMax,type)接口
       | 5.增加FocusEnd()接口
       | 6.增加SetFocusPosition(pos)接口
       | 7.增加SetEncoderUpgrade(path)接口
       | 8.增加SetJointFirmwareUpgrade(type,path)接口
       | 9.增加SetCtrlFirmwareUpgrade(type,path)接口
       | 10.增加SetEndFirmwareUpgrade(type,path)接口
       | 11.增加JointAllParamUpgrade(path)接口
       
   * - V3.8.3
     - 2025-06-24
     - | 1.Circle()接口增加加速度百分比及平滑半径参数
       | 2.EndForceDragControl()接口增加辅助拖动时机器人碰撞检测标志参数
       | 3.ServoJ()接口增加指令ID参数
       | 4.增加SetSSHScpCmd()接口
       | 5.增加SetWideBoxTempFanMonitorParam()接口
       | 6.增加GetWideBoxTempFanMonitorParam()接口
       | 7.状态结构体增加控制箱温度和风扇电流状态数据
              
   * - V3.8.2
     - 2025-06-13
     - | 1.WeaveSetPara()接口增加摆动方向侧倾角(绕摆动X轴偏转)参数
       | 2.WeaveChangeStart()接口增加摆动编号、焊接开始速度、焊接结束速度参数
       | 3.ExtDevSetUDPComParam()接口增加断电重启后是否自动建立连接参数
       | 4.SetCollisionDetectionMethod()接口增加碰撞等级阈值方式选择
       | 5.PtpFIRPlanningStart()接口增加统一关节急动度极值
       | 6.增加WeldingSetVoltageGradualChangeStart()接口
       | 7.增加WeldingSetVoltageGradualChangeEnd()接口
       | 8.增加WeldingSetCurrentGradualChangeStart()接口
       | 9.增加WeldingSetCurrentGradualChangeEnd()接口
       | 10.增加ArcWeldTraceAIChannelCurrent()接口
       | 11.增加ArcWeldTraceAIChannelVoltage()接口
       | 12.增加ArcWeldTraceCurrentPara()接口
       | 13.增加ArcWeldTraceVoltagePara()接口
       | 14.增加GetSmarttoolBtnState()接口
       | 15.增加ExtAxisGetCoord()接口
                     
   * - V3.8.1
     - 2025-04-24
     - | 1.ConveyorSetParam()接口增加跟踪运动类型、跟踪起始距离、跟踪终止距离参数
       | 2.增加AccSmoothStart()接口
       | 3.增加AccSmoothEnd()接口
       | 4.增加RbLogDownload()接口
       | 5.增加AllDataSourceDownload()接口
       | 6.增加DataPackageDownload()接口
       | 7.增加GetRobotSN()接口
       | 8.增加ShutDownRobotOS()接口
       | 9.增加ConveyorComDetect()接口
       | 10.增加ConveyorComDetectTrigger()接口
                     
   * - V3.8.0
     - 2025-02-12
     - | 1.EndForceDragControl()接口增加奇异点规避参数
       | 2.ArcWeldTraceControl()接口增加偏置参数
       | 3.增加WeaveChangeStart()接口
       | 4.增加WeaveChangeEnd()接口
       | 5.增加LoadTrajectoryLA()接口
       | 6.增加MoveTrajectoryLA()接口
       | 7.增加CustomCollisionDetectionStart()接口
       | 8.增加CustomCollisionDetectionEnd()接口