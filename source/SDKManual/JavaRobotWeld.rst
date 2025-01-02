机器人焊接
=============

.. toctree:: 
    :maxdepth: 5

焊接开始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 焊接开始
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 起弧超时时间
    * @return 错误码
    */
    int ARCStart(int ioType, int arcNum, int timeout);

焊接结束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 焊接结束
    * @param [in] ioType io类型 0-控制器IO； 1-扩展IO
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] timeout 熄弧超时时间
    * @return 错误码
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

设置焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置焊接电流与输出模拟量对应关系
    * @param [in] relation 关系值
    * @return 错误码
    */
    int WeldingSetCurrentRelation(WeldCurrentAORelation relation);

设置焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置焊接电压与输出模拟量对应关系
    * @param [in] relation 焊接电压-模拟量输出关系值
    * @return 错误码
    */
    int WeldingSetVoltageRelation(WeldVoltageAORelation relation);

获取焊接电流与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取焊接电流与输出模拟量对应关系
    * @param [out] relation 关系值
    * @return 错误码
    */
    int WeldingGetCurrentRelation(WeldCurrentAORelation relation);

获取焊接电压与输出模拟量对应关系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取焊接电压与输出模拟量对应关系
    * @param [out] relation 焊接电压-模拟量输出关系值
    * @return 错误码
    */
    int WeldingGetVoltageRelation(WeldVoltageAORelation relation);

代码示例
++++++++++++++++
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
        DescPose  desc_p1, desc_p2;
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos j1 = new JointPos(-28.529,-140.397,-81.08,-30.934,92.34,-5.629);
        JointPos j2 = new JointPos(-11.045,-130.984,-104.495,-12.854,92.475,-5.547);

        robot.GetForwardKin(j1,desc_p1);
        robot.GetForwardKin(j2,desc_p2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveL(j1, desc_p1,0, 0, 20, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCStart(0, 0, 10000);//焊接开始
        robot.MoveL(j2, desc_p2,0, 0, 20, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCEnd(0, 0, 10000);//焊接结束

        WeldCurrentAORelation currentRelation = new WeldCurrentAORelation(0, 1000, 0, 10, 0);
        robot.WeldingSetCurrentRelation(currentRelation);
        WeldVoltageAORelation voltageAORelation = new WeldVoltageAORelation(0, 100, 0, 10, 1);
        robot.WeldingSetVoltageRelation(voltageAORelation);

        WeldCurrentAORelation tmpCur = new WeldCurrentAORelation();
        WeldVoltageAORelation tmpVol = new WeldVoltageAORelation();
        robot.WeldingGetCurrentRelation(tmpCur);
        robot.WeldingGetVoltageRelation(tmpVol);
    } 

设置焊接电流
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置焊接电流
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] current 焊接电流值(A)
    * @param [in] AOIndex 焊接电流控制箱模拟量输出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 错误码
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

设置焊接电压
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置焊接电压
    * @param [in] ioType 控制IO类型 0-控制箱IO；1-扩展IO
    * @param [in] voltage 焊接电压值(A)
    * @param [in] AOIndex 焊接电压控制箱模拟量输出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 错误码
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

设置摆动参数
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置摆动参数
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    * @param [in] weaveFrequency 摆动频率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
    * @param [in] weaveRange 摆动幅度(mm)
    * @param [in] weaveLeftRange 垂直三角摆动左弦长度(mm)
    * @param [in] weaveRightRange 垂直三角摆动右弦长度(mm)
    * @param [in] additionalStayTime 垂直三角摆动垂三角点停留时间(mm)
    * @param [in] weaveLeftStayTime 摆动左停留时间(ms)
    * @param [in] weaveRightStayTime 摆动右停留时间(ms)
    * @param [in] weaveCircleRadio 圆形摆动-回调比率(0-100%)
    * @param [in] weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
    * @param [in] weaveYawAngle 摆动方向方位角(绕摆动Z轴旋转)，单位°
    * @return 错误码
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle);

即时设置摆动参数
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 即时设置摆动参数
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in]weaveType 摆动类型 0-平面三角波摆动；1-垂直L型三角波摆动；2-顺时针圆形摆动；3-逆时针圆形摆动；4-平面正弦波摆动；5-垂直L型正弦波摆动；6-垂直三角波摆动；7-垂直正弦波摆动
    * @param [in]weaveFrequency 摆动频率(Hz)
    * @param [in]weaveIncStayTime 等待模式 0-周期不包含等待时间；1-周期包含等待时间
    * @param [in]weaveRange 摆动幅度(mm)
    * @param [in]weaveLeftStayTime 摆动左停留时间(ms)
    * @param [in]weaveRightStayTime 摆动右停留时间(ms)
    * @param [in]weaveCircleRadio 圆形摆动-回调比率(0-100%)
    * @param [in]weaveStationary 摆动位置等待，0-等待时间内位置继续移动；1-等待时间内位置静止
    * @return 错误码
    */
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

摆动开始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 摆动开始
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveStart(int weaveNum);

摆动结束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 摆动结束
    * @param [in] weaveNum 摆焊参数配置编号
    * @return 错误码
    */
    int WeaveEnd(int weaveNum);

代码示例
++++++++++++++++
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
        robot.WeldingSetCurrent(0, 500, 0, 0);
        robot.WeldingSetVoltage(0, 60, 1, 0);
        robot.WeaveSetPara(0,0, 2.0, 0, 0.0, 0, 0, 0, 100, 100, 50, 50,1);

        DescPose desc_p1 = new DescPose(688.259,-566.358,-139.354,-158.206,0.324,-117.817);
        DescPose desc_p2 = new DescPose(700.078,-224.752,-149.191,-158.2,0.239,-94.978);


        JointPos j1 = new JointPos(0,0,0,0,0,0);
        JointPos j2 = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, desc_p1, -1, j1);
        robot.GetInverseKin(0, desc_p2, -1, j2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveL(j1, desc_p1,3, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.WeaveSetPara(0,0, 1.0, 0, 10.0, 0, 0, 0, 100, 100, 50, 50,1);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2,3, 0, 10, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
    } 

正向送丝
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 正向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

反向送丝
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 反向送丝
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] wireFeed 送丝控制  0-停止送丝；1-送丝
    * @return 错误码
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

送气
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 送气
    * @param [in] ioType io类型  0-控制器IO；1-扩展IO
    * @param [in] airControl 送气控制  0-停止送气；1-送气
    * @return 错误码
    */
    int SetAspirated(int ioType, int airControl);

代码示例
++++++++++++++++
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
        robot.SetForwardWireFeed(0, 1);
        robot.Sleep(2000);
        robot.SetForwardWireFeed(0, 0);
        robot.Sleep(2000);
        robot.SetReverseWireFeed(0, 1);
        robot.Sleep(2000);
        robot.SetReverseWireFeed(0, 0);
        robot.Sleep(2000);

        robot.SetAspirated(0,1);
        robot.Sleep(2000);
        robot.SetAspirated(0,0);
    }

段焊
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 段焊开始
    * @param [in] startDesePos 起始点笛卡尔位置
    * @param [in] endDesePos 结束点笛卡尔位姿
    * @param [in] startJPos 起始点关节位姿
    * @param [in] endJPos 结束点关节位姿
    * @param [in] weldLength 焊接段长度(mm)
    * @param [in] noWeldLength 非焊接段长度(mm)
    * @param [in] weldIOType 焊接IO类型(0-控制箱IO；1-扩展IO)
    * @param [in] arcNum 焊机配置文件编号
    * @param [in] weldTimeout 起/收弧超时时间
    * @param [in] isWeave 是否摆动
    * @param [in] weaveNum 摆焊参数配置编号
    * @param [in] tool 工具号
    * @param [in] user 工件号
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType,int arcNum, int weldTimeout, boolean isWeave, int weaveNum, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos);

代码示例
++++++++++++++++
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
        DescPose startdescPose = new DescPose(185.859,-520.154,193.129,-177.129,1.339,-137.789);
        JointPos startjointPos = new JointPos(-60.989,-94.515,-89.479,-83.514,91.957,-13.124);

        DescPose enddescPose = new DescPose( -243.7033,-543.868,143.199,-177.954,1.528,177.758);
        JointPos endjointPos = new JointPos(-105.479,-101.919,-87.979,-78.455,91.955,-13.183);

        ExaxisPos exaxisPos = new ExaxisPos( 0, 0, 0, 0 );
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );

        robot.SegmentWeldStart(startdescPose, enddescPose, startjointPos, endjointPos, 80, 40, 0, 0, 5000, true, 0, 3, 0, 30, 30, 100, -1, exaxisPos, 0, 0, offdese);
    }

焊丝寻位开始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊丝寻位开始
    * @param [in] refPos  1-基准点 2-接触点
    * @param [in] searchVel   寻位速度 %
    * @param [in] searchDis  寻位距离 mm
    * @param [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param [in] autoBackVel  自动返回速度 %
    * @param [in] autoBackDis  自动返回距离 mm
    * @param [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return 错误码 
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊丝寻位结束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊丝寻位结束
    * @param [in] refPos  1-基准点 2-接触点
    * @param [in] searchVel   寻位速度 %
    * @param [in] searchDis  寻位距离 mm
    * @param [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param [in] autoBackVel  自动返回速度 %
    * @param [in] autoBackDis  自动返回距离 mm
    * @param [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return 错误码 
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

计算焊丝寻位偏移量
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 计算焊丝寻位偏移量
    * @param [in] seamType  焊缝类型
    * @param [in] method   计算方法
    * @param [in] varNameRef 基准点1-6，“#”表示无点变量
    * @param [in] varNameRes 接触点1-6，“#”表示无点变量
    * @param [out] offset 偏移位姿[x, y, z, a, b, c]及偏移方式
    * @return 错误码 
    */
    int GetWireSearchOffset(int seamType, int method, String[] varNameRef, String[] varNameRes, DescOffset offset);

等待焊丝寻位完成
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 等待焊丝寻位完成
    * @return 错误码 
    */
    int WireSearchWait(String name);

焊丝寻位接触点写入数据库
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊丝寻位接触点写入数据库
    * @param [in] varName  接触点名称 “RES0” ~ “RES99”
    * @param [in] pos  接触点数据[x, y, x, a, b, c]
    * @return 错误码 
    */
    int SetPointToDatabase(String varName, DescPose pos);

代码示例
++++++++++++++++
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
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(153.736,-715.249,-295.037,-179.829,2.613,-155.615);
        JointPos jointStart = new JointPos(0,0,0,0,0,0);

        DescPose descEnd = new DescPose(73.748,-645.825,-295.016,-179.828,2.608,-155.614);
        JointPos jointEnd = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, descStart, -1, jointStart);
        robot.GetInverseKin(0, descEnd, -1, jointEnd);

        robot.MoveL(jointStart, descStart, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese,0, 100);

        DescPose descREF0A = new DescPose(273.716,-723.539,-295.075,-179.829,2.608,-155.614);
        JointPos jointREF0A = new JointPos(0,0,0,0,0,0);

        DescPose descREF0B = new DescPose(202.588,-723.543,-295.039,-179.829,2.609,-155.614);
        JointPos jointREF0B = new JointPos(0,0,0,0,0,0);

        DescPose descREF1A = new DescPose(75.265,-525.091,-295.059,-179.83,2.609,-155.616);
        JointPos jointREF1A = new JointPos(0,0,0,0,0,0);

        DescPose descREF1B = new DescPose(75.258,-601.157,-295.075,-179.834,2.609,-155.616);
        JointPos jointREF1B = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, descREF0A, -1, jointREF0A);
        robot.GetInverseKin(0, descREF0B, -1, jointREF0B);
        robot.GetInverseKin(0, descREF1A, -1, jointREF1A);
        robot.GetInverseKin(0, descREF1B, -1, jointREF1B);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起点
        robot.MoveL(jointREF0B, descREF0B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向点
        robot.WireSearchWait("REF0");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起点
        robot.MoveL(jointREF1B, descREF1B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向点
        robot.WireSearchWait("REF1");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);


        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起点
        robot.MoveL(jointREF0B, descREF0B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向点
        robot.WireSearchWait("RES0");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起点
        robot.MoveL(jointREF1B, descREF1B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向点
        robot.WireSearchWait("RES1");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef = { "REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };

        DescOffset offectPos = new DescOffset();
        robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectPos);
        robot.PointsOffsetEnable(offectPos.offsetFlag, offectPos.offset);
        robot.MoveL(jointStart, descStart, 3, 1, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 3, 1, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);
        robot.PointsOffsetDisable();
    }

电弧跟踪控制
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 电弧跟踪控制
    * @param [in] flag 开关，0-关；1-开
    * @param [in] delaytime 滞后时间，单位ms
    * @param [in] isLeftRight 左右偏差补偿
    * @param [in] klr 左右调节系数(灵敏度)
    * @param [in] tStartLr 左右开始补偿时间cyc
    * @param [in] stepMaxLr 左右每次最大补偿量 mm
    * @param [in] sumMaxLr 左右总计最大补偿量 mm
    * @param [in] isUpLow 上下偏差补偿
    * @param [in] kud 上下调节系数(灵敏度)
    * @param [in] tStartUd 上下开始补偿时间cyc
    * @param [in] stepMaxUd 上下每次最大补偿量 mm
    * @param [in] sumMaxUd 上下总计最大补偿量
    * @param [in] axisSelect 上下坐标系选择，0-摆动；1-工具；2-基座
    * @param [in] referenceType 上下基准电流设定方式，0-反馈；1-常数
    * @param [in] referSampleStartUd 上下基准电流采样开始计数(反馈)，cyc
    * @param [in] referSampleCountUd 上下基准电流采样循环计数(反馈)，cyc
    * @param [in] referenceCurrent 上下基准电流mA
    * @return 错误码 
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent);

仿真摆动开始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真摆动开始
    * @param [in] weaveNum  摆动参数编号
    * @return 错误码 
    */
    int WeaveStartSim(int weaveNum);

仿真摆动结束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真摆动结束
    * @param [in] weaveNum  摆动参数编号
    * @return 错误码 
    */
    int WeaveEndSim(int weaveNum);

开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 开始轨迹检测预警(不运动)
    * @param [in] weaveNum   摆动参数编号
    * @return 错误码 
    */
    int WeaveInspectStart(int weaveNum);

结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 结束轨迹检测预警(不运动)
    * @param [in] weaveNum   摆动参数编号
    * @return 错误码 
    */
    int WeaveInspectEnd(int weaveNum);

设置焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置焊接工艺曲线参数
    * @param [in] id 焊接工艺编号(1-99)
    * @param [in] param 焊接工艺参数
    * @return 错误码 
    */
    int WeldingSetProcessParam(int id, WeldingProcessParam param);

获取焊接工艺曲线参数
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取焊接工艺曲线参数
    * @param [in] id 焊接工艺编号(1-99)
    * @param [out] param 焊接工艺参数
    * @return 错误码 
    */
    int WeldingGetProcessParam(int id, WeldingProcessParam param);

代码示例
++++++++++++++++
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
        WeldingProcessParam param = new WeldingProcessParam(177.0,27.0,1000,178.0,28.0,176.0,26.0,1000);
        robot.WeldingSetProcessParam(1, param);

        WeldingProcessParam getParam = new WeldingProcessParam();
        robot.WeldingGetProcessParam(1, getParam);
    }

扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机气体检测信号
    * @param [in] DONum  气体检测信号扩展DO编号
    * @return 错误码 
    */
    int SetAirControlExtDoNum(int DONum);

扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机起弧信号
    * @param [in] DONum  焊机起弧信号扩展DO编号
    * @return 错误码 
    */
    int SetArcStartExtDoNum(int DONum);

扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机反向送丝信号
    * @param [in] DONum  反向送丝信号扩展DO编号
    * @return 错误码 
    */
    int SetWireReverseFeedExtDoNum(int DONum);

扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机正向送丝信号
    * @param [in] DONum  正向送丝信号扩展DO编号
    * @return 错误码 
    */
    int SetWireForwardFeedExtDoNum(int DONum);

扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机起弧成功信号
    * @param [in] DINum  起弧成功信号扩展DI编号
    * @return 错误码 
    */
    int SetArcDoneExtDiNum(int DINum);

扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊机准备信号
    * @param [in] DINum  焊机准备信号扩展DI编号
    * @return 错误码 
    */
    int SetWeldReadyExtDiNum(int DINum);

扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 扩展IO-配置焊接中断恢复信号
    * @param [in] reWeldDINum  焊接中断后恢复焊接信号扩展DI编号
    * @param [in] abortWeldDINum  焊接中断后退出焊接信号扩展DI编号
    * @return 错误码 
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

代码示例
++++++++++++++++
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
        robot.SetArcStartExtDoNum(1);
        robot.SetAirControlExtDoNum(2);
        robot.SetWireForwardFeedExtDoNum(3);
        robot.SetWireReverseFeedExtDoNum(4);

        robot.SetWeldReadyExtDiNum(5);
        robot.SetArcDoneExtDiNum(6);
        robot.SetExtDIWeldBreakOffRecover(7, 8);
    }

设置焊丝寻位扩展IO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置焊丝寻位扩展IO端口
    * @param [in] searchDoneDINum 焊丝寻位成功DO端口(0-127)
    * @param [in] searchStartDONum 焊丝寻位启停控制DO端口(0-127)
    * @return 错误码
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

设置焊机控制模式扩展DO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置焊机控制模式扩展DO端口
    * @param [in] DONum 焊机控制模式DO端口(0-127)
    * @return 错误码 
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

设置焊机控制模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置焊机控制模式
    * @param [in] mode 焊机控制模式;0-一元化
    * @return 错误码 
    */
    int SetWeldMachineCtrlMode(int mode);

代码示例
++++++++++++++++
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
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevSetUDPComParam(param);//udp扩展轴通讯
        robot.ExtDevLoadUDPDriver();

        robot.SetWeldMachineCtrlModeExtDoNum(17);//DO
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);//设置焊机控制模式
            robot.Sleep(500);
            robot.SetWeldMachineCtrlMode(1);
            robot.Sleep(500);
        }

        robot.SetWeldMachineCtrlModeExtDoNum(18);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            robot.Sleep(500);
            robot.SetWeldMachineCtrlMode(1);
            robot.Sleep(500);
        }
    }