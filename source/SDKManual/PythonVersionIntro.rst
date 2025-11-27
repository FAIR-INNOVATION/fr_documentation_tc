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