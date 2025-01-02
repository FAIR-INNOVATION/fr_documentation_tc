扩展轴
=================

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴参数
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] param 485扩展轴参数
    * @return 错误码 
    */
    int AuxServoSetParam(int servoId, Axis485Param param)
    
获取485扩展轴参数
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取485扩展轴配置参数
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [out] param 485扩展轴参数
    * @return 错误码 
    */
    int AuxServoGetParam(int servoId, Axis485Param param);

设置485扩展轴使能/去使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码 
    */
    int AuxServoEnable(int servoId, int status);
        
设置485扩展轴控制模式
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码 
    */
    int AuxServoSetControlMode(int servoId, int mode);

设置485扩展轴回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] mode 回零模式，1-当前位置回零；2-负限位回零；3-正限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);

设置485扩展轴目标位置(位置模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoSetTargetPos(int servoId, double pos, double speed, double acc);

设置485扩展轴目标速度(速度模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] speed 目标速度，mm/s或°/s
    * @param [in] acc 加速度百分比[0-100]
    * @return 错误码 
    */
    int AuxServoSetTargetSpeed(int servoId, double speed, double acc);

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        Axis485Param param = new Axis485Param();
        param.servoCompany = 1;           // 伺服驱动器厂商，1-戴纳泰克
        param.servoModel = 1;             // 伺服驱动器型号，1-FD100-750C
        param.servoSoftVersion = 1;       // 伺服驱动器软件版本，1-V1.0
        param.servoResolution = 131072;        // 编码器分辨率
        param.axisMechTransRatio = 13.45;  // 机械传动比
        robot.AuxServoSetParam(1, param);//设置485扩展轴参数

        robot.AuxServoGetParam(1, param);
        System.out.println("auxservo param servoCompany: " + param.servoCompany + "  servoModel:  " + param.servoModel +"  param.servoSoftVersion:  " + param.servoSoftVersion + "  servoResolution:  " + param.servoResolution + "  axisMechTransRatio:  " + param.axisMechTransRatio);
        
        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);
        robot.AuxServoEnable(1, 0);
        robot.Sleep(3000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(2000);
        robot.AuxServoHoming(1, 1, 10, 10,100);
        robot.Sleep(5000);

        robot.AuxServoSetTargetSpeed(1, 100,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, -200,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 0,100);
    }
    
设置485扩展轴目标转矩(力矩模式)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置485扩展轴目标转矩(力矩模式)-暂未开放
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @param [in] torque 目标力矩，Nm
    * @return 错误码 
    */
    int AuxServoSetTargetTorque(int servoId, double torque);
        
清除485扩展轴错误信息
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @return 错误码 
    */
    int AuxServoClearError(int servoId);

设置状态反馈中485扩展轴数据轴号
+++++++++++++++++++++++++++++++++++++++++ 
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-16],对应从站ID
    * @return 错误码 
    */
    int AuxServosetStatusID(int servoId);

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.AuxServoSetControlMode(1, 1);
        robot.Sleep(2000);
        robot.AuxServoEnable(1, 0);
        robot.Sleep(3000);
        robot.AuxServoEnable(1, 1);
        robot.Sleep(2000);
        robot.AuxServoHoming(1, 1, 10, 10,100);
        robot.Sleep(5000);

        robot.AuxServoSetTargetSpeed(1, 40,100);
        robot.Sleep(3000);
        robot.AuxServoSetTargetSpeed(1, 40,100);

        robot.AuxServosetStatusID(1);

        while (true)
        {
            ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
            System.out.println("aux servo cur Pos :" + pkg.auxState.servoPos + "  cur vel:  " + pkg.auxState.servoVel);
            robot.Sleep(100);
        }
    }

UDP扩展轴通讯参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通讯参数配置
    * @param [in] param 通讯参数
    * @return 错误码
    */
    int ExtDevSetUDPComParam(UDPComParam param);     

获取UDP扩展轴通讯参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取UDP扩展轴通讯参数
    * @param [out] param 通讯参数
    * @return 错误码
    */
    int ExtDevGetUDPComParam(UDPComParam param);       

加载UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 加载UDP通信
    * @return 错误码
    */
    int ExtDevLoadUDPDriver();

卸载UDP通信
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 卸载UDP通信
    * @return 错误码
    */
    int ExtDevUnloadUDPDriver();

代码示例
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//udp扩展轴通讯

        UDPComParam getParam = new UDPComParam();
        robot.ExtDevGetUDPComParam(getParam);
        System.out.println(" " + getParam.ip + " ,   " + getParam.port + " ,   " + getParam.period + " ,  " + getParam.lossPkgTime + " ,   " + getParam.lossPkgNum + " ,   " + getParam.disconnectTime + " ,   " + getParam.reconnectEnable + " ,   " + getParam.reconnectPeriod + " ,   " + getParam.reconnectNum);
        robot.ExtDevUnloadUDPDriver();//卸载UDP通信
        robot.Sleep(1000);
        robot.ExtDevLoadUDPDriver();//加载UDP通信
        robot.Sleep(1000);
    }

UDP扩展轴通信异常断开后恢复连接
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后恢复连接
    * @return 错误码
    */
    int ExtDevUDPClientComReset();

UDP扩展轴通信异常断开后关闭通讯
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后关闭通讯
    * @return 错误码
    */
    int ExtDevUDPClientComClose();

UDP扩展轴参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] axisOffect 焊缝起始点扩展轴偏移量
    * @param [in] axisCompany 驱动器厂家 1-禾川；2-汇川；3-松下
    * @param [in] axisModel 驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 编码器类型  0-增量；1-绝对值
    * @return 错误码
    */
    int ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, int encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

获取扩展轴驱动器配置信息
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取扩展轴驱动器配置信息
    * @param [in] axisId 轴号[1-4]
    * @return List[0]: 错误码 List[1]: axisCompany 驱动器厂家 1-禾川；2-汇川；3-松下;
    * List[2]: axisModel 驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * List[3]: axisEncType 编码器类型  0-增量；1-绝对值
    */
    List<Integer> GetExAxisDriverConfig(int axisId);

设置扩展轴安装位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展轴安装位置
    * @param [in] installType 0-机器人安装在外部轴上，1-机器人安装在外部轴外
    * @return 错误码
    */
    int SetRobotPosToAxis(int installType);

设置扩展轴系统DH参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.ExtAxisServoOn(1, 1);//扩展轴1使能
        robot.ExtAxisServoOn(2, 1);//扩展轴2使能
        robot.Sleep(1000);
        robot.ExtAxisSetHoming(1, 0, 10, 3);//1,2扩展轴都回零
        robot.ExtAxisSetHoming(2, 0, 10, 3);
        robot.Sleep(1000);

        int rtn = 0;
        rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0);
        System.out.println("SetAxisDHParaConfig rtn is " + rtn);
        rtn = robot.SetRobotPosToAxis(1);
        System.out.println("SetRobotPosToAxis rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(1,1, 0, 50, -50, 1000, 1000, 1.905, 262144, 200, 0, 0, 0);
        System.out.println("ExtAxisParamConfig rtn is " + rtn);
        rtn = robot.ExtAxisParamConfig(2,2, 0, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 0, 0, 0);
        System.out.println("ExtAxisParamConfig rtn is " + rtn);
    }

设置扩展轴坐标系参考点-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展轴坐标系参考点-四点法
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int ExtAxisSetRefPoint(int pointNum);

计算扩展轴坐标系-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 计算扩展轴坐标系-四点法
    * @param [out]  coord 坐标系值
    * @return 错误码
    */
    int ExtAxisComputeECoordSys(DescPose coord);

应用扩展轴坐标系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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

设置标定参考点在变位机末端坐标系下位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置标定参考点在变位机末端坐标系下位姿
    * @param [in] pos 位姿值
    * @return 错误码
    */
    int SetRefPointInExAxisEnd(DescPose pos);

变位机坐标系参考点设置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 变位机坐标系参考点设置
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    int PositionorSetRefPoint(int pointNum);

变位机坐标系计算-四点法
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 变位机坐标系计算-四点法
    * @param [out] coord 坐标系值
    * @return 错误码
    */
    int PositionorComputeECoordSys(DescPose coord);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端传感器寄存器写入
    * @param [in] devAddr  设备地址编号 0-255
    * @param [in] regHAddr 寄存器地址高8位
    * @param [in] regLAddr 寄存器地址低8位
    * @param [in] regNum  寄存器个数 0-255
    * @param [in] data1 写入寄存器数值1
    * @param [in] data2 写入寄存器数值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 错误码
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

UDP扩展轴使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴使能
    * @param [in] axisID 轴号[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 错误码
    */
    int ExtAxisServoOn(int axisID, int status);

UDP扩展轴回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴点动开始
    * @param [in] axisID 轴号[1-4]
    * @param [in] direction 转动方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc (加速度 mm/s2)
    * @param [in] maxDistance 最大点动距离
    * @return 错误码
    */
    int ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP扩展轴点动停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴点动停止
    * @param [in] axisID 轴号[1-4]
    * @return 错误码
    */
    int ExtAxisStopJog(int axisID);

代码示例
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }

        robot.ExtAxisServoOn(1, 1);
        robot.ExtAxisSetHoming(1, 0, 10, 3);
        robot.ExtAxisStartJog(1, 1, 100, 100, 20);
        robot.Sleep(1000);
        robot.ExtAxisStopJog(1);
        robot.ExtAxisServoOn(1, 0);
    }

设置扩展DO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展DO
    * @param [in] DONum DO编号
    * @param [in] bOpen 开关 true-开；false-关
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxDO(int DONum, boolean bOpen, boolean smooth, boolean block);

设置扩展AO
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展AO
    * @param [in] AONum AO编号
    * @param [in] value 模拟量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    int SetAuxAO(int AONum, double value, boolean block);

设置扩展DI输入滤波时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展DI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return  错误码
    */
    int SetAuxDIFilterTime(int filterTime);

设置扩展AI输入滤波时间
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置扩展AI输入滤波时间
    * @param [in] AONum AO编号
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    int SetAuxAIFilterTime(int AONum, int filterTime);

等待扩展DI输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param [in] DINum DI编号
    * @param [in] bOpen 开关 0-关；1-开
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    int WaitAuxDI(int DINum, boolean bOpen, int time, boolean errorAlarm);

等待扩展AI输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int WaitAuxAI(int AINum, int sign, int value, int time, boolean errorAlarm);
    
获取扩展AI值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取扩展AI值
    * @param [in] AINum AI编号
    * @param [in] isNoBlock 是否阻塞
    * @return List[0]:错误码; List[1] : value 输入值
    */
    List<Integer> GetAuxAI(int AINum, boolean isNoBlock);

UDP扩展轴运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴运动
    * @param [in] pos 目标位置
    * @param [in] ovl 速度百分比
    * @return 错误码
    */
    int ExtAxisMove(ExaxisPos pos, double ovl);

UDP扩展轴与机器人关节运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief UDP扩展轴与机器人关节运动同步运动
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] ffset_pos  位姿偏移量
    * @return 错误码
    */
    int ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);
    
UDP扩展轴与机器人直线运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码
    */
    int ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

UDP扩展轴与机器人圆弧运动同步运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] joint_pos_t  目标点关节位置,单位deg
    * @param [in] desc_pos_t   目标点笛卡尔位姿
    * @param [in] ttool  工具坐标号，范围[0~14]
    * @param [in] tuser  工件坐标号，范围[0~14]
    * @param [in] tvel  速度百分比，范围[0~100]
    * @param [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t  扩展轴位置，单位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos_t  位姿偏移量
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码
    */
    int ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

代码示例
+++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.Mode(0);
        int tool = 1;
        int user = 0;
        double vel = 20.0;
        double acc = 100.0;
        double ovl = 100.0;
        ExaxisPos exaxisPos = new ExaxisPos( 0, 0, 0, 0 );

        DescPose d0 = new DescPose(311.189, -309.688, 401.836, -174.375, -1.409, -82.354);
        JointPos j0 =new JointPos(118.217, -99.669, 79.928, -73.559, -85.229, -69.359);

        JointPos joint_pos0 =new JointPos(111.549,-99.821,108.707,-99.308,-85.305,-41.515);
        DescPose desc_pos0 = new DescPose(273.499,-345.746,201.573,-176.566 ,3.235,-116.819);
        ExaxisPos e_pos0=new ExaxisPos(0,0,0,0);

        JointPos joint_pos1 = new JointPos(112.395,-65.118,67.815,-61.449,-88.669,-41.517);
        DescPose desc_pos1 = new DescPose(291.393,-420.519,201.089,156.297,21.019,-120.919);
        ExaxisPos e_pos1 = new ExaxisPos(-30, -30, 0, 0);


        JointPos j2 = new JointPos(111.549,-98.369,108.036,-103.789,-95.203,-69.358);
        DescPose desc_pos2 = new DescPose(234.544,-392.777,205.566,176.584,-5.694,-89.109);
        ExaxisPos epos2 = new ExaxisPos(0.000,0.000,0.000,0.000);

        JointPos j3 = new JointPos(113.908,-61.947,63.829,-64.478,-85.406,-69.256);
        DescPose desc_pos3 = new DescPose(336.049,-444.969,192.799,173.776 ,27.104,-89.455);
        ExaxisPos epos3 = new ExaxisPos(-30.000,-30.000, 0.000, 0.000);

        //圆弧的起点
        JointPos j4 = new JointPos(137.204,-98.475,106.624,-97.769,-90.634,-69.24);
        DescPose desc_pos4 = new DescPose(381.269,-218.688,205.735,179.274,0.128,-63.556);

        JointPos j5 = new JointPos(115.069,-92.709,97.285,-82.809,-90.455,-77.146);
        DescPose desc_pos5 = new DescPose(264.049,-329.478 ,220.747,176.906,11.359,-78.044);
        ExaxisPos  epos5 = new ExaxisPos(-15, 0, 0, 0);


        JointPos j6 = new JointPos(102.409,-63.115,70.559,-70.156,-86.529,-77.148);
        DescPose desc_pos6 = new DescPose(232.407,-494.228 ,158.115,176.803,27.319,-92.056);
        ExaxisPos  epos6 = new ExaxisPos(-30, 0, 0, 0);

        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        //同步关节运动
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.ExtAxisSyncMoveJ(joint_pos0, desc_pos0, 1, 0,20,100,100,e_pos0,-1,0,offset_pos);
        robot.ExtAxisSyncMoveJ(joint_pos1, desc_pos1, 1, 0,20,100,100,e_pos1,-1,0,offset_pos);


        //同步直线运动
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.ExtAxisSyncMoveL(j2, desc_pos2, tool, user, 40, 100, 100, -1, epos2, 0, offset_pos);
        robot.ExtAxisSyncMoveL(j3, desc_pos3, tool, user, 40, 100, 100, -1, epos3, 0, offset_pos);
        //同步圆弧运动
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,20);
        robot.MoveJ(j4, desc_pos4, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);

        robot.ExtAxisSyncMoveC(j5, desc_pos5, tool, user, 40, 100, epos5, 0, offset_pos, j6, desc_pos6, tool, user, 40, 100, epos6, 0, offset_pos, 100, 0);

        robot.Sleep(3000);
        robot.MoveJ(j0, d0, 1, 0, vel, acc, ovl, exaxisPos, -1, 0, offset_pos);
        robot.ExtAxisMove(exaxisPos,40);
        robot.Mode(1);
    }

可移动装置使能
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置使能
    * @param [in] enable false-去使能；true-使能
    * @return 错误码
    */
    int TractorEnable(Boolean enable);

可移动装置回零
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置回零
    * @return 错误码
    */
    int TractorHoming();

可移动装置直线运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置直线运动
    * @param [in] distance 直线运动距离（mm）
    * @param [in] vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveL(double distance, double vel);

可移动装置圆弧运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置圆弧运动
    * @param [in] radio 圆弧运动半径（mm）
    * @param [in] angle 圆弧运动角度（°）
    * @param [in] vel 直线运动速度百分比（0-100）
    * @return 错误码
    */
    int TractorMoveC(double radio, double angle, double vel);

可移动装置停止运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 可移动装置停止运动
    * @return 错误码
    */
    int TractorStop();

代码示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevSetUDPComParam(param);//udp扩展轴通讯
        robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
        robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);

        robot.TractorEnable(false);
        robot.Sleep(2000);
        robot.TractorEnable(true);
        robot.Sleep(2000);
        robot.TractorHoming();

        robot.Sleep(2000);
        robot.TractorMoveL(100, 20);
        robot.Sleep(5000);
        robot.TractorMoveL(-100, 20);
        robot.Sleep(5000);
        robot.TractorMoveC(300, 90, 20);
        robot.Sleep(2000);
        robot.TractorStop();//小车停止
        robot.TractorMoveC(300, -90, 20);
    }