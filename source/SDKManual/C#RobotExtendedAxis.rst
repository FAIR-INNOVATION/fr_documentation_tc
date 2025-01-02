扩展轴
=================

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [in] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [in] servoResolution 编码器分辨率
    * @param [in] axisMechTransRatio 机械传动比
    * @return 错误码 
    */
    int AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);
    
获取485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取485扩展轴配置参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [out] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [out] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [out] servoResolution 编码器分辨率
    * @param [out] axisMechTransRatio 机械传动比
    * @return 错误码 
    */
    int AuxServoGetParam(int servoId, ref int servoCompany, ref int servoModel, ref int servoSoftVersion, ref int servoResolution, ref double axisMechTransRatio);
    
设置485扩展轴使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码 
    */
    int AuxServoEnable(int servoId, int status);
        
设置485扩展轴控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码 
    */
    int AuxServoSetControlMode(int servoId, int mode);

代码示例
**********
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);//设置配置参数
    int ID = -1, company = -1, model = -1, soft = -1, servoResolution= -1;
    int radio = -1;
        robot.AuxServoGetParam(1, ref company, ref model, ref soft, ref servoResolution, ref radio);//获取配置参数
        
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 0);//去使能伺服
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//设置位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能伺服
    }

设置485扩展轴回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] mode 回零模式，1-当前位置回零；2-负限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed);

设置485扩展轴目标速度(速度模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed);

代码示例
**********
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 0);//设置位置模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//伺服回零需要一定的时间
                
        robot.AuxServoSetTargetPos(1, 1000, 100);//设置目标位置
        Thread.Sleep(1000);
        robot.AuxServoSetTargetPos(1, 0, 100);//再次设置目标位置
        Thread.Sleep(1000);

        robot.AuxServoEnable(1, 0);//去使能
        Thread.Sleep(100);
        robot.AuxServoSetControlMode(1, 1);//设置速度模式
        Thread.Sleep(100);
        robot.AuxServoEnable(1, 1);//使能
        Thread.Sleep(100);
        robot.AuxServoHoming(1, 1, 20, 5);//回零
        Thread.Sleep(4000);//回零需要一定时间
        robot.AuxServoSetTargetSpeed(1, 50);//设置目标速度
        Thread.Sleep(3000);

        robot.AuxServoSetTargetSpeed(1, -300);//设置目标速度
        Thread.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 0);//伺服停止
        Thread.Sleep(100);
    }
    
设置485扩展轴目标转矩(力矩模式)--暂未开放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置485扩展轴目标转矩(力矩模式)--暂未开放
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [in] torque 目标力矩，Nm
    * @return 错误码 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @return 错误码 
    */
    int AuxServoClearError(int servoId);

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取485扩展轴伺服状态
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @param [out] servoErrCode 伺服驱动器故障码
    * @param [out] servoState 伺服驱动器状态  bit0:0-未使能；1-使能;  bit1:0-未运动；1-正在运动;  bit2 0-正限位未触发；1-正限位触发；bit3 0-负限位未触发；1-负限位触发；bit4 0-未定位完成；1-定位完成；  bit5：0-未回零；1-回零完成
    * @param [out] servoPos 伺服当前位置 mm或°
    * @param [out] servoSpeed 伺服当前速度 mm/s或°/s
    * @param [out] servoTorque 伺服当前转矩Nm
    * @return 错误码 
    */
    int AuxServoGetStatus(int servoId, ref int servoErrCode, ref int servoState, ref double servoPos, ref double servoSpeed, ref double servoTorque);
    
设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6
    
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID 
    * @return 错误码 
    */
    int AuxServosetStatusID(int servoId);

代码示例
+++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

            robot.AuxServoClearError(1);
        int errCode = 0;
        int servoState = 0;
        double pos = 0;
        double speed = 0;
        double torque = 0;
        robot.AuxServoGetStatus(1, ref errCode, ref servoState, ref pos, ref speed, ref torque);

        robot.AuxServosetStatusID(1);
        ROBOT_STATE_PKG pKG = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pKG);
        Console.WriteLine($"the state is {pKG.auxState.servoPos}");
    }

UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴通讯参数配置
    * @param [in] ip PLC IP地址
    * @param [in] port	端口号
    * @param [in] period	通讯周期(ms，默认为2，请勿修改此参数)
    * @param [in] lossPkgTime	丢包检测时间(ms)
    * @param [in] lossPkgNum	丢包次数
    * @param [in] disconnectTime	通讯断开确认时长
    * @param [in] reconnectEnable	通讯断开自动重连使能 0-不使能 1-使能
    * @param [in] reconnectPeriod	重连周期间隔(ms)
    * @param [in] reconnectNum	重连次数
    * @return 错误码
    */
    int ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum);
        
获取UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 获取UDP扩展轴通讯参数
    * @param [out] ip PLC IP地址
    * @param [out] port	端口号
    * @param [out] period	通讯周期(ms，默认为2，请勿修改此参数)
    * @param [out] lossPkgTime	丢包检测时间(ms)
    * @param [out] lossPkgNum	丢包次数
    * @param [out] disconnectTime	通讯断开确认时长
    * @param [out] reconnectEnable	通讯断开自动重连使能 0-不使能 1-使能
    * @param [out] reconnectPeriod	重连周期间隔(ms)
    * @param [out] reconnectNum	重连次数
    * @return 错误码
    */
    int ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum);
        
加载UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 加载UDP通信
    * @return 错误码
    */
    int ExtDevLoadUDPDriver();

卸载UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 卸载UDP通信
    * @return 错误码
    */
    int ExtDevUnloadUDPDriver();

代码示例
**************

.. code-block:: C#
    :linenos:

    private void btnSetParam_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        string ip = "";
        int port = 0;
        int period = 0;
        int checktime = 0;
        int checknum = 0;
        int disconntime = 0;
        int reconnenable = 0;
        int reconntime = 0;
        int reconnnum = 0;
        robot.ExtDevGetUDPComParam(ref ip, ref port, ref period, ref checktime, ref checknum, ref disconntime, ref reconntime, ref reconnenable, ref reconnnum);
        Console.Writeline($"{ip}  {port}  {period} {checktime}  {checknum}  {disconntime}  {reconnenable}  {reconntime}  {reconnnum}");

        robot.ExtDevLoadUDPDriver();
        Thread.Sleep(1000 * 10);
        robot.ExtDevUnloadUDPDriver();
    }

UDP扩展轴通信异常断开后恢复连接
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后恢复连接
    * @return 错误码
    */
    int ExtDevUDPClientComReset();

UDP扩展轴通信异常断开后关闭通讯
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后关闭通讯
    * @return 错误码
    */
    int ExtDevUDPClientComClose();

UDP扩展轴参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴参数配置
    * @param [in] axisID 轴号
    * @param [in] axisType 扩展轴类型 0-平移；1-旋转
    * @param [in] axisDirection 扩展轴方向 0-正向；1-方向 
    * @param [in] axisMax 扩展轴最大位置 mm
    * @param [in] axisMin 扩展轴最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 导程mm
    * @param [in] encResolution 编码器分辨率
    * @param [in] axisOffect焊缝起始点扩展轴偏移量
    * @param [in] axisCompany 驱动器厂家 1-禾川；2-汇川；3-松下
    * @param [in] axisModel 驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 编码器类型  0-增量；1-绝对值
    * @return 错误码
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

设置扩展轴安装位置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展轴安装位置
    * @param [in] installType 0-机器人安装在外部轴上，1-机器人安装在外部轴外
    * @return 错误码
    */
    int SetRobotPosToAxis(int installType);

设置扩展轴系统DH参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展轴系统DH参数配置
    * @param [in]  axisConfig 外部轴构型，0-单自由度直线滑轨，1-两自由度L型变位机，2-三自由度，3-四自由度，4-单自由度变位机
    * @param [in]  axisDHd1 外部轴DH参数d1 mm
    * @param [in]  axisDHd2 外部轴DH参数d2 mm
    * @param [in]  axisDHd3 外部轴DH参数d3 mm
    * @param [in]  axisDHd4 外部轴DH参数d4 mm
    * @param [in]  axisDHa1 外部轴DH参数11 mm
    * @param [in]  axisDHa2 外部轴DH参数a2 mm
    * @param [in]  axisDHa3 外部轴DH参数a3 mm
    * @param [in]  axisDHa4 外部轴DH参数a4 mm
    * @return 错误码
    */
    int SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

代码示例
**********

.. code-block:: C#
    :linenos:

    private void btnSetAxisParam_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int rtn = 0;
        rtn = robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0);
        Console.WriteLine($"SetAxisDHParaConfig rtn is {rtn}");
        rtn = robot.SetRobotPosToAxis(1);
        Console.WriteLine($"SetRobotPosToAxis rtn is {rtn}");
        rtn = robot.ExtAxisParamConfig(1,0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0);
        Console.WriteLine($"ExtAxisParamConfig rtn is {rtn}");
    }

设置扩展轴坐标系参考点-四点法
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展轴坐标系参考点-四点法
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int ExtAxisSetRefPoint(int pointNum);

计算扩展轴坐标系-四点法
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 计算扩展轴坐标系-四点法
    * @param [out]  coord 坐标系值
    * @return 错误码
    */
    int ExtAxisComputeECoordSys(DescPose& coord);

应用扩展轴坐标系
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 应用扩展轴坐标系
    * @param [in]  applyAxisId 扩展轴编号 bit0-bit3对应扩展轴编号1-4，如应用扩展轴1和3，则是 0b 0000 0101；也就是5
    * @param [in]  axisCoordNum 扩展轴坐标系编号
    * @param [in]  coord 坐标系值
    * @param [in]  calibFlag 标定标志 0-否，1-是
    * @return 错误码
    */
    int ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnCoordCalib_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtAxisSetRefPoint(1);
        //robot.ExtAxisSetRefPoint(2);
        //robot.ExtAxisSetRefPoint(3);
        //robot.ExtAxisSetRefPoint(4);
        //DescPose pos = new DescPose();
        //robot.ExtAxisComputeECoordSys(ref pos);
    }

设置标定参考点在变位机末端坐标系下位姿
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置标定参考点在变位机末端坐标系下位姿
    * @param [in] pos 位姿值
    * @return 错误码
    */
    int SetRefPointInExAxisEnd(DescPose pos);

变位机坐标系参考点设置
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 变位机坐标系参考点设置
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int PositionorSetRefPoint(int pointNum);

变位机坐标系计算-四点法
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 变位机坐标系计算-四点法
    * @param [out] coord 坐标系值
    * @return 错误码
    */
    int PositionorComputeECoordSys(DescPose& coord);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnCoordCalib_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose refPointPos = new DescPose(122.0, 312.0, 0, 0, 0, 0);
        robot.SetRefPointInExAxisEnd(refPointPos);

        robot.PositionorSetRefPoint(1);
        //robot.PositionorSetRefPoint(2);
        //robot.PositionorSetRefPoint(3);
        //robot.PositionorSetRefPoint(4);

        //DescPose coord = new DescPose();
        //robot.PositionorComputeECoordSys(ref coord);
    }

UDP扩展轴使能
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴使能
    * @param [in] axisID 轴号[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 错误码
    */
    int ExtAxisServoOn(int axisID, int status);

UDP扩展轴回零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴回零
    * @param [in] axisID 轴号[1-4]
    * @param [in] mode 回零方式 0-当前位置回零，1-负限位回零，2-正限位回零
    * @param [in] searchVel 寻零速度(mm/s)
    * @param [in] latchVel 寻零箍位速度(mm/s)
    * @return 错误码
    */
    int ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP扩展轴点动开始
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴点动开始
    * @param [in] axisID 轴号[1-4]
    * @param [in] direction 转动方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc 加速度 (mm/s2)
    * @param [in] maxDistance 最大点动距离
    * @return 错误码
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP扩展轴点动停止
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴点动停止
    * @param [in] axisID 轴号[1-4]
    * @return 错误码
    */
    int ExtAxisStopJog(int axisID);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnJog_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        robot.ExtAxisServoOn(1, 1);
        robot.ExtAxisSetHoming(1, 0, 10, 3);
        robot.ExtAxisStartJog(1, 1, 100, 100, 20);
        Thread.Sleep(1000 * 2);
        robot.ExtAxisStopJog(1);
        robot.ExtAxisServoOn(1, 0);
    }

UDP扩展轴运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴运动
    * @param [in] pos 目标位置
    * @param [in] ovl 速度百分比
    * @return 错误码
    */
    int ExtAxisMove(ExaxisPos pos, double ovl);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnAxisMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        ExaxisPos pos = new ExaxisPos(10, 0, 0, 0);
        robot.ExtAxisMove(pos, 10);
    }

UDP扩展轴与机器人关节运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴与机器人关节运动同步运动
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] desc_pos 目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveJ_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用(注意：变位机和直线滑轨的标定接口不同，以下时变位机的标定接口)
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose( );
        robot.PositionorComputeECoordSys(ref coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步关节运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/);
        JointPos startjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */);

        //8.记录您的同步关节运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/);
        JointPos endjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 输入您的扩展轴终点坐标 */);

        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
    }

UDP扩展轴与机器人直线运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴与机器人直线运动同步运动
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

代码示例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveL_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步直线运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/);
        JointPos startjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */);

        //8.记录您的同步直线运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/);
        JointPos endjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 输入您的扩展轴终点坐标 */);

        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
    }
    
UDP扩展轴与机器人圆弧运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief UDP扩展轴与机器人圆弧运动同步运动
    * @param [in] joint_pos_p  路径点关节位置,单位deg
    * @param [in] desc_pos_p   路径点笛卡尔位姿
    * @param [in] ptool  工具坐标号，范围[0~14]
    * @param [in] puser  工件坐标号，范围[0~14]
    * @param [in] pvel  速度百分比，范围[0~100]
    * @param [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p  中间点扩展轴位置，单位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] joint_pos_t  目标点关节位置,单位deg
    * @param [in] desc_pos_t   目标点笛卡尔位姿
    * @param [in] ttool  工具坐标号，范围[0~14]
    * @param [in] tuser  工件坐标号，范围[0~14]
    * @param [in] tvel  速度百分比，范围[0~100]
    * @param [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t  扩展轴位置，单位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos_t  位姿偏移量	 
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);
    
代码示例
************

.. code-block:: C#
    :linenos:

    private void btnSyncMoveC_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

    //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用
        DescPose pos = new DescPose(/* 输入您的标定点坐标 */);
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = new DescPose();
        robot.PositionorComputeECoordSys(ref coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步圆弧运动起始点
        DescPose startdescPose = new DescPose(/*输入您的坐标*/);
        JointPos startjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos startexaxisPos = new ExaxisPos(/* 输入您的扩展轴起始点坐标 */);

        //8.记录您的同步圆弧运动终点坐标
        DescPose enddescPose = new DescPose(/*输入您的坐标*/);
        JointPos endjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos endexaxisPos = new ExaxisPos(/* 输入您的扩展轴终点坐标 */);

        //8.记录您的同步圆弧运动中间点坐标
        DescPose middescPose = new DescPose(/*输入您的坐标*/);
        JointPos midjointPos = new JointPos(/*输入您的坐标*/);
        ExaxisPos midexaxisPos = new ExaxisPos(/* 输入机器人圆弧中间点时的扩展轴坐标 */);

        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(startjointPos, startdescPose, 1, 1, 100, 100, 100, startexaxisPos, 0, 0, offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
    }

设置焊丝寻位扩展IO端口
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊丝寻位扩展IO端口
    * @param searchDoneDINum 焊丝寻位成功DO端口(0-127)
    * @param searchStartDONum 焊丝寻位启停控制DO端口(0-127)
    * @return 错误码
    */
    int  SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

代码示例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        //UDP焊丝寻位
        robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevLoadUDPDriver();
        robot.SetWireSearchExtDIONum(0, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        DescPose descStart = new DescPose(-158.767, -510.596, 271.709, -179.427, -0.745, -137.349);
        JointPos jointStart = new JointPos(61.667, -79.848, 108.639, -119.682, -89.700, -70.985);

        DescPose descEnd = new DescPose(0.332, -516.427, 270.688, 178.165, 0.017, -119.989);
        JointPos jointEnd = new JointPos(79.021, -81.839, 110.752, -118.298, -91.729, -70.981);

        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

        DescPose descREF0A = new DescPose(-66.106, -560.746, 270.381, 176.479, -0.126, -126.745);
        JointPos jointREF0A = new JointPos(73.531, -75.588, 102.941, -116.250, -93.347, -69.689);

        DescPose descREF0B = new DescPose(-66.109, -528.440, 270.407, 176.479, -0.129, -126.744);
        JointPos jointREF0B = new JointPos(72.534, -79.625, 108.046, -117.379, -93.366, -70.687);

        DescPose descREF1A = new DescPose(72.975, -473.242, 270.399, 176.479, -0.129, -126.744);
        JointPos jointREF1A = new JointPos(87.169, -86.509, 115.710, -117.341, -92.993, -56.034);
        DescPose descREF1B = new DescPose(31.355, -473.238, 270.405, 176.480, -0.130, -126.745);
        JointPos jointREF1B = new JointPos(82.117, -87.146, 116.470, -117.737, -93.145, -61.090);
        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起点
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向点
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
        List<string> varNameRef1 = new List<string> { "REF0", "REF1", "#", "#", "#", "#" };
        List<string> varNameRes1 = new List<string> { "RES0", "RES1", "#", "#", "#", "#" };
        string[] varNameRef = varNameRef1.ToArray();
        string[] varNameRes = varNameRes1.ToArray();
        int offectFlag = 0;
        DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, ref offectFlag, ref offectPos);
        robot.PointsOffsetEnable(0, offectPos);
        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);
        robot.PointsOffsetDisable();
    }

设置焊机控制模式扩展DO端口
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊机控制模式扩展DO端口
    * @param DONum 焊机控制模式DO端口(0-127)
    * @return 错误码
    */
    int  SetWeldMachineCtrlModeExtDoNum(int DONum);

设置焊机控制模式
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置焊机控制模式
    * @param mode 焊机控制模式;0-一元化
    * @return 错误码
    */
    int SetWeldMachineCtrlMode(int mode);

代码示例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button8_Click(object sender, EventArgs e)
    {
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevLoadUDPDriver();

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }

        robot.SetWeldMachineCtrlModeExtDoNum(18);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }
        robot.SetWeldMachineCtrlModeExtDoNum(19);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(500);
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(500);
        }
    }

可移动装置使能
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移动装置使能
    * @param enable false-去使能；true-使能
    * @return 错误码
    */
    int TractorEnable(bool enable);

可移动装置停止运动
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移动装置停止运动
    * @return 错误码
    */
    int TractorStop();

可移动装置回零
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移动装置回零
    * @return 错误码
    */
    int  TractorHoming();

可移动装置直线运动
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移动装置直线运动
    * @param distance 直线运动距离（mm）
    * @param vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveL(double distance, double vel);

可移动装置圆弧运动
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 可移动装置圆弧运动
    * @param radio 圆弧运动半径（mm）
    * @param angle 圆弧运动角度（°）
    * @param vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveC(double radio, double angle, double vel);

代码示例
+++++++++
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void button6_Click(object sender, EventArgs e)
    {
        robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10);
        int tru = robot.ExtDevLoadUDPDriver();
        Thread.Sleep(2000);
        Console.WriteLine("tru" + tru);
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);
        int tru1 = robot.TractorEnable(true);
        Thread.Sleep(3000);
        robot.TractorHoming();
        Thread.Sleep(2000);
        robot.TractorMoveL(100, 20);
        Thread.Sleep(2000);
        robot.TractorMoveL(-100, 20);
        Thread.Sleep(2000);
        robot.TractorMoveC(50, 60, 20);
        Thread.Sleep(2000);
        robot.TractorMoveC(50, -60, 20);
        Thread.Sleep(1000);
        robot.TractorStop();//中途停止
    }

设置扩展DO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展DO
    * @param [in] DONum DO编号
    * @param [in] bOpen 开关 true-开；false-关
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
设置扩展AO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展AO
    * @param [in] AONum AO编号 
    * @param [in] value 模拟量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxAO(int AONum, double value, bool block);
    
代码示例
************

.. code-block:: C#
    :linenos:

    private void btnAODO_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        for (int i = 0; i < 128; i++)
        {
            robot.SetAuxDO(i, true, false, true);
            Thread.Sleep(200);
        }

        for(int i = 0; i < 409; i++)
        {
            robot.SetAuxAO(0, i * 10, true);
            robot.SetAuxAO(1, 4095 - i * 10, true);
            robot.SetAuxAO(2, i * 10, true);
            robot.SetAuxAO(3, 4095 - i * 10, true);
            Thread.Sleep(10);
        }
    }
            
设置扩展DI输入滤波时间
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展DI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    int SetAuxDIFilterTime(int filterTime);

设置扩展AI输入滤波时间
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 设置扩展AI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    int SetAuxAIFilterTime(int filterTime);

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param [in] DINum DI编号
    * @param [in] bOpen 开关 0-关；1-开
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    int WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
等待扩展AI输入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param [in] AINum AI编号
    * @param [in] sign 0-大于；1-小于
    * @param [in] value AI值
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    int WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
获取扩展DI值
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 获取扩展DI值
    * @param [in] DINum DI编号
    * @param [in] isNoBlock 是否阻塞
    * @param [out] isOpen 0-关；1-开
    * @return 错误码
    */
    int GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
获取扩展AI值
+++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: C#
    :linenos:

    /**
    * @brief 获取扩展AI值
    * @param [in] AINum AI编号
    * @param [in] isNoBlock 是否阻塞
    * @param [in] value 输入值
    * @return 错误码
    */
    int GetAuxAI(int AINum, bool isNoBlock, int& value);

代码示例
***********
.. code-block:: C#
    :linenos:

    private void btnAIDI_Click(object sender, EventArgs e)
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    robot.SetAuxDIFilterTime(10);
    robot.SetAuxAIFilterTime(10);

    for (int i = 0; i < 20; i++)
    {
        bool curValue = false;
        int rtn = robot.GetAuxDI(i, false, ref curValue);
        txtRtn.Text = rtn.ToString();
        Console.Write($"DI{i}  {curValue}  ");
        Console.WriteLine("  ");
    }

    int curValue = -1;
    int rtn = 0;
    for (int i = 0; i < 4; i++)
    {
        rtn = robot.GetAuxAI(i, true, ref curValue);
        txtRtn.Text = rtn.ToString();
        Console.Write($"AI{i} {curValue}   rtn is {rtn} ");
        Console.WriteLine("  ");
    }

    robot.WaitAuxDI(1, true, 1000, false);
    robot.WaitAuxAI(1, 1, 132, 1000, false);
    }


