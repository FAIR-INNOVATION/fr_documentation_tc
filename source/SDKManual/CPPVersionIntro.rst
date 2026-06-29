版本更新說明
====================

.. toctree:: 
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **版本號**
     - **日期**
     - **更新描述**

   * - V3.9.7
     - 2026-06-25
     - | 1.更新機器人狀態回饋結構體，夾爪運動完成信號新增是否偵測到物體狀態；夾爪故障新增2-指令錯誤、3-工件掉落、其他-夾爪故障碼+3；
       | 2.更新設置LUA程式停止/暫停後輸出復位代碼示例，優化載入lua檔案介面僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 3.更新光電感測器TCP校準代碼示例，優化載入檔案介面僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 4.更新設置軌跡運行中的速度代碼示例，優化載入軌跡J檔案介面僅需要輸入軌跡J檔案名稱，不再需要輸入路徑。
       | 5.更新機器人軌跡J檔案複現代碼示例，優化載入軌跡J檔案介面僅需要輸入軌跡J檔案名稱，不再需要輸入路徑。
       | 6.更新軌跡複現（軌跡前瞻）代碼示例，優化載入軌跡J檔案介面僅需要輸入軌跡J檔案名稱，不再需要輸入路徑。
       | 7.LoadDefaultProgConfig()介面作業程式名稱參數僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 8.ProgramLoad()介面作業程式名稱參數僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 9.GetLoadedProgram()介面作業程式名稱參數僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 10.更新機器人LUA程式操作代碼示例，優化載入檔案介面僅需要輸入lua檔案名稱，不再需要輸入路徑。
       | 11.SetAxleLuaEnableDeviceType()介面增加靈巧手啟用狀態參數；
       | 12.GetAxleLuaEnableDeviceType()介面增加靈巧手啟用狀態參數；
       | 13.GetAxleLuaEnableDevice()介面增加靈巧手啟用設備編號狀態參數；
       | 14.SetAxleLuaGripperFunc()介面夾爪功能碼陣列擴充至32個，增加旋轉夾爪控制等；
       | 15.GetAxleLuaGripperFunc()介面夾爪功能碼陣列擴充至32個，增加旋轉夾爪狀態等；
       | 16.SetCoderCompenParams()更新介面名稱錯誤；
       | 17.新增SetDexterousHandsMove ()控制靈巧手運動介面。
       | 18.新增SetDexterousHandsAct ()控制靈巧手復位激活介面。
       | 19.新增ClearDexterousHandsError ()清除靈巧手錯誤介面。
       | 20.新增SetDexterousHandsFunc()設置啟用靈巧手動作控制功能介面。
       | 21.新增GetDexterousHandsFunc()獲取啟用靈巧手動作控制功能介面。
       | 22.新增SetWeaveBackCenterConfig()、GetWeaveBackCenterConfig()設置、獲取擺動結束回週期零點參數。
       | 23.新增SetWeaveOffsetRT()設置擺動實時偏移介面；
       | 24.新增SetSpeedInstant()實時設置速度介面；

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
       | 2.FieldBusSlaveWriteAO()接口更改寫入數值類型為double類型，其中AO0~AO15為整型，AO16~AO31為浮點型；
       | 3.FieldBusSlaveReadAI()接口更改讀取數值類型為double類型，其中AI0~AI15為整型，AI16~AI31為浮點型；
       | 4.更新機器人狀態反饋結構體類型；
       | 5.新增機器人狀態反饋配置枚舉類型；
       | 6.新增SetRobotRealtimeStateConfig()配置機器人CNDE狀態反饋接口；
       | 7.新增AddRobotRealtimeState()CNDE狀態配置添加一個機器人狀態接口；
       | 8.新增DeleteRobotRealtimeState()CNDE狀態配置刪除一個機器人狀態接口；
       | 9.新增SetRobotRealtimeStatePeriod()設置CNDE狀態反饋周期接口；
       | 10.新增GetRobotRealtimeStateConfig()獲取當前CNDE狀態反饋所有狀態集合和周期接口。

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
       | 30.新增OpenLuaDownload()下載開放協議 Lua 文件接口；
       | 31.新增OpenLuaDelete()刪除開放協議 Lua 文件接口；
       | 32.新增AllOpenLuaDelete()刪除開放協議 Lua 文件接口；
       | 33.新增SendUDPFrameUDP ()發送指令幀接口；
       | 34.新增SetCmdRpyCallback()設置 SDK 通過 UDP 發送指令的執行結果回調函數接口；
       | 35.新增SetVelReducePara()設置安全速度參數接口；
       | 36.新增OriginPointWeaveStart()定點擺動開始接口；
       | 37.新增OriginPointWeaveEnd()定點擺動結束接口；
       | 38.新增SetUserLEDColor()設置用戶自定義機器人末端燈色接口；
       | 39.新增MoveToTPDStart()運動到 TPD 軌跡記錄起點接口；

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
     - | 1. JointSensitivityCalibration() 介面增加 j1~j6 關節線性度回傳
       | 2. 增加 JointHysteresisError() 介面
       | 3. 增加 JointRepeatability() 介面
       | 4. 增加 SetAdmittanceParams() 介面
       | 5. 增加 MoveToIntersectLineStart() 介面
       | 6. 增加 MoveIntersectLine() 介面

   * - V3.8.7
     - 2025-10-21
     - | 1.FT_Control()增加質量參數和阻尼參數接口
       | 2.增加JointSensitivityCalibration()接口
       | 3.增加JointSensitivityCollect()接口
       | 4.增加MotionQueueClear()接口
       | 5.增加GetSlavePortErrCounter()接口
       | 6.增加SlavePortErrCounterClear()接口
       | 7.增加SetVelFeedForwardRatio()接口
       | 8.增加GetVelFeedForwardRatio()接口
       | 9.增加RobotMCULogCollect()接口
       | 10.狀態結構體增加ServoJ指令計數及最後一個指令目標位置數據
       | 11.新螺旋線參數結構體SpiralParam增加速度加速度參數模式

   * - V3.8.6
     - 2025-09-19
     - | 1.SetLoadCoord()接口增加負載編號參數
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
       | 33.狀態結構體增加工具、工件、外部工具、擴展軸座標系和負載質量、質心數據

   * - V3.8.5
     - 2025-08-20
     - | 1.MoveL()、MoveC()、Circle()指令增加velAccParamMode參數
       | 2.增加MoveJ()、SplinePTP()、ExtAxisSyncMoveJ()自動正運動學計算接口
       | 3.LoadTrajectoryLA()增加勻速前瞻開關開啟參數
       | 4.增加MoveL()、MoveC()、Circle()、NewSplinePoint()、NewSpiral()、ExtAxisSyncMoveL()、ExtAxisSyncMoveC()自動逆運動學計算接口
       | 5.增加SetSuckerCtrl()、GetSuckerState()、WaitSuckerState()等吸盤控制接口，SetExAxisRobotPlan()同步運動策略接口
       | 6.增加OpenLuaUpload()、GetFieldBusConfig()、FieldBusSlaveWriteDO()、FieldBusSlaveWriteAO()、FieldBusSlaveReadDI()、FieldBusSlaveReadAI()、FieldBusSlaveWaitDI()、FieldBusSlaveWaitAI()等機器人從站模式控制指令

   * - V3.8.4
     - 2025-07-17
     - | 1.ExtAxisMove()接口增加blend平滑參數
       | 2.增加SetFocusCalibPoint()接口
       | 3.增加ComputeFocusCalib()接口
       | 4.增加SetFocusPosition()接口
       | 5.增加FocusStart()接口
       | 6.增加FocusEnd()接口
       | 7.增加SetJointFirmwareUpgrade()接口
       | 8.增加SetCtrlFirmwareUpgrade()接口
       | 9.增加SetEndFirmwareUpgrade()接口
       | 10.增加JointAllParamUpgrade()接口
       
   * - V3.8.3
     - 2025-06-24
     - | 1.Circle()接口增加加速度百分比及平滑半徑參數
       | 2.EndForceDragControl()接口增加輔助拖動時機器人碰撞檢測標誌參數
       | 3.ServoJ()接口增加指令ID參數
       | 4.增加SetWideBoxTempFanMonitorParam()接口
       | 5.增加GetWideBoxTempFanMonitorParam()接口
       | 6.狀態結構體增加控制箱溫度和風扇電流狀態數據
              
   * - V3.8.2
     - 2025-06-13
     - | 1.WeaveSetPara()接口增加擺動方向側傾角(繞擺動X軸偏轉)參數
       | 2.WeaveChangeStart()接口增加擺動編號、焊接開始速度、焊接結束速度參數
       | 3.ExtDevSetUDPComParam()接口增加斷電重啟後是否自動建立連接參數
       | 4.SetCollisionDetectionMethod()接口增加碰撞等級閾值方式選擇
       | 5.PtpFIRPlanningStart()接口增加統一關節急動度極值
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
     - | 1.ConveyorSetParam()接口增加跟蹤運動類型、跟蹤起始距離、跟蹤終止距離參數
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
     - | 1.EndForceDragControl()接口增加奇異點規避參數
       | 2.ArcWeldTraceControl()接口增加偏置參數
       | 3.增加WeaveChangeStart()接口
       | 4.增加WeaveChangeEnd()接口
       | 5.增加LoadTrajectoryLA()接口
       | 6.增加MoveTrajectoryLA()接口
       | 7.增加CustomCollisionDetectionStart()接口
       | 8.增加CustomCollisionDetectionEnd()接口