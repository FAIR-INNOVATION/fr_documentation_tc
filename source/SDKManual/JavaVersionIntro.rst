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
       | 11.新螺旋線參數結構體SpiralParam增加速度加速度參數模式；

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
     - | 1.增加OpenLuaUpload()接口
       | 2.增加GetFieldBusConfig()接口
       | 3.增加FieldBusSlaveWriteDO()接口
       | 4.增加FieldBusSlaveWriteAO()接口
       | 5.增加FieldBusSlaveReadDI()接口
       | 6.增加FieldBusSlaveReadAI()接口
       | 7.增加FieldBusSlaveWaitDI()接口
       | 8.增加FieldBusSlaveWaitAI()接口
       | 9.增加SetSuckerCtrl()接口
       | 10.增加GetSuckerState()接口
       | 11.增加WaitSuckerState()接口
       | 12.增加MoveL()速度加速度參數模式velAccParamMode接口
       | 13.增加MoveL()重載函數1接口
       | 14.增加MoveL()重載函數2接口
       | 15.增加MoveC()速度加速度參數模式velAccParamMode接口
       | 16.增加MoveC()重載函數1接口
       | 17.增加Circle()速度加速度參數模式velAccParamMode接口
       | 18.增加Circle()重載函數1接口
       | 19.增加SetExAxisRobotPlan()接口

   * - V3.8.4
     - 2025-07-17
     - | 1.ExtAxisMove()接口增加blend平滑參數；
       | 2.增加SetFocusCalibPoint()接口
       | 3.增加ComputeFocusCalib()接口；
       | 4.增加FocusStart()接口；
       | 5.增加FocusEnd()接口
       | 6.增加SetFocusPosition()接口；
       | 7.增加SetEncoderUpgrade()接口；
       | 8.增加SetJointFirmwareUpgrade()接口
       | 9.增加SetCtrlFirmwareUpgrade()接口；
       | 10.增加SetEndFirmwareUpgrade()接口；
       | 11.增加JointAllParamUpgrade()接口；
       
   * - V3.8.3
     - 2025-06-24
     - | 1.Circle()接口增加加速度百分比及平滑半徑參數；
       | 2.EndForceDragControl()接口增加輔助拖動時機器人碰撞檢測標誌參數；
       | 3.ServoJ()接口增加指令ID參數；
       | 4.增加SetSSHScpCmd()接口
       | 5.增加SetWideBoxTempFanMonitorParam()接口；
       | 6.增加GetWideBoxTempFanMonitorParam()接口；
       | 7.狀態結構體增加控制箱溫度和風扇電流狀態數據；
              
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