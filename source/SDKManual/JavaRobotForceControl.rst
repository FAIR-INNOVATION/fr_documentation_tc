机器人力控
============

.. toctree:: 
    :maxdepth: 5

力传感器配置
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置力传感器
    * @param  [in] config company:力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯
    * @param  [in] config device:设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)
    * @param  [in] config softvesion:软件版本号，暂不使用，默认为0
    * @param  [in] config bus:设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int FT_SetConfig(DeviceConfig config); 

获取力传感器配置 
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取力传感器配置 
    * @param [out] config company:力传感器厂商，17-坤维科技，19-航天十一院，20-ATI传感器，21-中科米点，22-伟航敏芯
    * @param [out] config device:设备号，坤维(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米点(0-MST2010)，伟航敏芯(0-WHC6L-YB-10A)
    * @param [out] config softvesion:软件版本号，暂不使用，默认为0
    * @param [out] config bus:设备挂在末端总线位置，暂不使用，默认为0
    * @return 错误码 
    */ 
    int FT_GetConfig(DeviceConfig config); 

力传感器激活
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力传感器激活
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int FT_Activate(int act); 

力传感器校零
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力传感器校零
    * @param  [in] act  0-去除零点，1-零点矫正
    * @return  错误码
    */
    int FT_SetZero(int act); 

代码示例
+++++++++++++++
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
        DeviceConfig config = new DeviceConfig();
        config.company = 24;
        config.device = 0;
        config.softwareVersion = 0;
        config.bus = 0;

        robot.FT_SetConfig(config);
        robot.Sleep(1000);
        config.company = 0;
        robot.FT_GetConfig(config);
        System.out.println("FT config : " + config.company + ", " + config.device + ", " + config.softwareVersion + ", " + config.bus);

        robot.FT_Activate(0);  //复位
        robot.Sleep(2000);

        robot.FT_Activate(1);  //激活
        robot.Sleep(2000);

        robot.FT_SetZero(0);//0去除零点
        robot.Sleep(2000);

        robot.FT_SetZero(1);//1零点矫正
    }

设置力传感器参考坐标系
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置力传感器参考坐标系
    * @param  [in] type  0-工具坐标系，1-基坐标系, 2-自由坐标系
    * @param  [in] coord  自由坐标系值
    * @return  错误码
    */
    int FT_SetRCS(int type, DescPose coord); 

负载重量辨识记录
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载重量辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @return  错误码
    */
    int FT_PdIdenRecord(int id);

负载重量辨识计算
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载重量辨识计算
    * @return  List[0]:错误码; List[1] : double weight  负载重量，单位kg
    */   
    List<Number> FT_PdIdenCompute();

负载质心辨识记录
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载质心辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @param  [in] index 点编号，范围[1~3]
    * @return  错误码
    */
    int FT_PdCogIdenRecord(int id, int index); 

负载质心辨识计算
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  负载质心辨识计算
    * @param  [out] cog  负载质心，单位mm
    * @return  错误码
    */   
    int FT_PdCogIdenCompute(DescTran cog);

代码示例
+++++++++++++++
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
        DeviceConfig config = new DeviceConfig();
        config.company = 24;
        config.device = 0;
        config.softwareVersion = 0;
        config.bus = 0;

        robot.FT_SetConfig(config);
        robot.Sleep(1000);
        DescPose tcoord, desc_p1, desc_p2, desc_p3;
        tcoord = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p1 = new DescPose(-14.404,-455.283,319.847,-172.935,25.141,-68.097);
        desc_p2 = new DescPose(-107.999,-599.174,285.939,153.472,12.686,-71.284);
        desc_p3 = new DescPose(6.586,-704.897,309.638,178.909,-27.759,-70.479);

        DescPose coord = new DescPose(0, 0 ,0, 1, 0, 0);
        robot.FT_SetRCS(0, coord);
        robot.Sleep(1000);

        tcoord.tran.z = 35.0;
        robot.SetToolCoord(8, tcoord, 1, 0);
        robot.Sleep(1000);
        robot.FT_PdIdenRecord(10);
        robot.Sleep(1000);
        List<Number> rtnArray =  robot.FT_PdIdenCompute();
        System.out.println("payload weight : " + rtnArray.get(1));

        robot.MoveCart(desc_p1, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 1);
        robot.MoveCart(desc_p2, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 2);
        robot.MoveCart(desc_p3, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 3);
        robot.Sleep(1000);

        DescTran rtnCog = new DescTran();
        robot.FT_PdCogIdenCompute(rtnCog);
        System.out.println("cog : " + rtnCog.x + ", " + rtnCog.y + ", " + rtnCog.z);
    }


获取参考坐标系下力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取参考坐标系下力/扭矩数据
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueRCS(int flag, ForceTorque ft); 

获取力传感器原始力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取力传感器原始力/扭矩数据
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    int FT_GetForceTorqueOrigin(int flag, ForceTorque ft); 

碰撞守护
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  碰撞守护
    * @param  [in] flag 0-关闭碰撞守护，1-开启碰撞守护
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大阈值
    * @param  [in] min_threshold 最小阈值
    * @note   力/扭矩检测范围：(ft-min_threshold, ft+max_threshold)
    * @return  错误码
    */   
    int FT_Guard(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] max_threshold, Object[] min_threshold); 

代码示例
+++++++++++++++
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
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 1, 0, 0, 0, 0, 0 };//只启用x轴碰撞守护
        Object[] max_threshold = { 5.0, 0.01, 0.01, 0.01, 0.01, 0.01 };
        Object[] min_threshold = { 3.0, 0.01, 0.01, 0.01, 0.01, 0.01 };

        ForceTorque ft = new ForceTorque(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        DescPose  desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(-14.404,-455.283,319.847,-172.935,25.141,-68.097);
        desc_p2 = new DescPose(-107.999,-599.174,285.939,153.472,12.686,-71.284);
        desc_p3 = new DescPose(6.586,-704.897,309.638,178.909,-27.759,-70.479);

        int rtn =  robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        System.out.println("FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
    }

恒力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  恒力控制
    * @param  [in] flag 0-关闭恒力控制，1-开启恒力控制
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid参数，力矩pid参数
    * @param  [in] adj_sign 自适应启停控制，0-关闭，1-开启
    * @param  [in] ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
    * @param  [in] max_dis 最大调整距离，单位mm
    * @param  [in] max_ang 最大调整角度，单位deg
    * @param  [in] filter_Sign 滤波开启标志 0-关；1-开，默认关闭
    * @param  [in] posAdapt_sign 姿态顺应开启标志 0-关；1-开，默认关闭
    * @param  [in] isNoBlock 阻塞标志，0-阻塞；1-非阻塞
    * @return  错误码
    */   
    int FT_Control(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang, int filter_Sign, int posAdapt_sign, int isNoBlock);   

代码示例
+++++++++++++++
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
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 0,0,1,0,0,0 };
        Object[] ft_pid = { 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0 };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;
        ForceTorque ft = new ForceTorque(0, 0, -10, 0 ,0 ,0);

        JointPos j1=new JointPos(-21.724,-136.814,-59.518,-68.853,89.245,-66.35);
        DescPose desc_p1 = new DescPose(703.996,-391.695,240.708,-178.756,-4.709,-45.447);

        JointPos j2=new JointPos(0.079,-130.285,-71.029,-72.115,88.945,-62.736);
        DescPose desc_p2 = new DescPose(738.755,-102.812,226.704,177.488,2.566,-27.209);

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        //关节空间运动
        robot.MoveL(j1, desc_p1, 0, 0, 40.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos, 0, 100);
        int rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        System.out.println("FT_Control start rtn " + rtn);

        robot.MoveL(j2, desc_p2, 0, 0, 10.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos, 0, 100);
        flag = 0;
        rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0 ,0);
        System.out.println("FT_Control end rtn " + rtn);
    }

柔顺控制开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔顺控制开启
    * @param  [in] p 位置调节系数或柔顺系数
    * @param  [in] force 柔顺开启力阈值，单位N
    * @return  错误码
    */   
    int FT_ComplianceStart(double p, double force);

柔顺控制关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔顺控制关闭
    * @return  错误码
    */   
    int FT_ComplianceStop(); 

代码示例
+++++++++++++++
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
        byte flag = 1;
        int sensor_id = 8;
        Object[] select = { 1, 1, 1, 0, 0, 0 };
        Object[] ft_pid = { 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 100.0;
        double max_ang = 0.0;

        ForceTorque ft = new ForceTorque(-10.0, -10.0, -10.0, 0.0, 0.0, 0.0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1;
        j1=new JointPos(-21.724, -136.814, -59.518, -68.853, 89.245, -66.359);

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(703.996, -391.695, 240.708, -178.756, -4.709, -45.447);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang,0,0,0);
        float p = 0.00005f;
        float force = 10.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        System.out.println("FT_ComplianceStart rtn " + rtn);

        robot.MoveL(j1, desc_p1, 0, 0, 20.0, 180.0, 100.0, -1.0, epos, 0, 1, offset_pos, 0, 100);

        rtn = robot.FT_ComplianceStop();
        System.out.println("FT_ComplianceStop rtn " + rtn);
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang,0,0,0);
    }

负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识初始化
    * @return 错误码
    */
    int LoadIdentifyDynFilterInit();

负载辨识变量初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识变量初始化
    * @return 错误码
    */
    int LoadIdentifyDynVarInit();

负载辨识主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 负载辨识主程序
    * @param [in] joint_torque 关节扭矩
    * @param [in] joint_pos 关节位置
    * @param [in] t 采样周期
    * @return 错误码
    */
    int LoadIdentifyMain(Object[] joint_torque, Object[] joint_pos, double t);

获取负载辨识结果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取负载辨识结果
    * @param [in] gain
    * @return List[0]:错误码; List[1] : double weight 负载重量; List[2]: x 负载质心X mm; List[3] : y 负载质心Y mm; List[2]: z 负载质心Z mm
    */
    List<Number> LoadIdentifyGetResult(Object[] gain);

获取力传感器拖动开关状态
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器拖动开关状态
    * @return List[0]:错误码; List[1] : dragState 力传感器辅助拖动控制状态，0-关闭；1-开启; List[1] : sixDimensionalDragState 六维力辅助拖动控制状态，0-关闭；1-开启
    */
    List<Integer> GetForceAndTorqueDragState();

力传感器辅助拖动
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器辅助拖动
    * @param [in] status 控制状态，0-关闭；1-开启
    * @param [in] asaptiveFlag 自适应开启标志，0-关闭；1-开启
    * @param [in] interfereDragFlag 干涉区拖动标志，0-关闭；1-开启
    * @param [in] M 惯性系数
    * @param [in] B 阻尼系数
    * @param [in] K 刚度系数
    * @param [in] F 拖动六维力阈值
    * @param [in] Fmax 最大拖动力限制 Nm
    * @param [in] Vmax 最大关节速度限制 °/s
    * @return 错误码
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, Object[] M, Object[] B, Object[] K, Object[] F, double Fmax, double Vmax);

代码示例
+++++++++++++++
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
        List<Integer> rtnArray = robot.GetForceAndTorqueDragState();
        System.out.println("the drag state is  " + rtnArray.get(1) + "  ForceAndJointImpedance state  " + rtnArray.get(2));

        robot.Sleep(1000);
        Object[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        Object[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        Object[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        robot.EndForceDragControl(1, 0, 0, M, B, K, F, 50, 100);

        rtnArray = robot.GetForceAndTorqueDragState();
        System.out.println("the drag state is" + rtnArray.get(1) + "  ForceAndJointImpedance state  " + rtnArray.get(2));

        robot.Sleep(1000 * 10);
        robot.EndForceDragControl(0, 0, 0, M, B, K, F, 50, 100);

        rtnArray = robot.GetForceAndTorqueDragState();
        System.out.println("the drag state is" + rtnArray.get(1) + "  ForceAndJointImpedance state  " + rtnArray.get(2));
    }

设置六维力和关节阻抗混合拖动开关及参数
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置六维力和关节阻抗混合拖动开关及参数
    * @param [in] status 控制状态，0-关闭；1-开启
    * @param [in] impedanceFlag 阻抗开启标志，0-关闭；1-开启
    * @param [in] lamdeGain 拖动增益
    * @param [in] KGain 刚度增益
    * @param [in] BGain 阻尼增益
    * @param [in] dragMaxTcpVel 拖动末端最大线速度限制
    * @param [in] dragMaxTcpOriVel 拖动末端最大角速度限制
    * @return 错误码
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, Object[] lamdeGain, Object[] KGain, Object[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

代码示例
+++++++++++++++
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
        robot.DragTeachSwitch(1);
        Object[] lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        Object[] KGain = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] BGain = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        List<Integer> rtnArray = robot.GetForceAndTorqueDragState();
        System.out.println("the drag state is  " + rtnArray.get(1) + "  ForceAndJointImpedance state  " + rtnArray.get(2));
    }

设置力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置力传感器下负载重量
    * @param [in] weight 负载重量 kg
    * @return 错误码
    */
    int SetForceSensorPayLoad(double weight);

设置力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置力传感器下负载质心
    * @param [in] cog 负载质心 mm
    * @return 错误码
    */
    int SetForceSensorPayLoadCog(DescTran cog);

获取力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器下负载重量
    * @return List[0]:错误码; List[1] : weight 负载重量 kg
    */
    List<Number> GetForceSensorPayLoad();

获取力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 获取力传感器下负载质心
    * @param [out] cog 负载质心 mm
    * @return 错误码
    */
    int GetForceSensorPayLoadCog(DescTran cog);
    
代码示例
+++++++++++++++
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
        robot.SetForceSensorPayLoad(1.34);
        DescTran cog = new DescTran(0.778, 2.554, 48.765);
        robot.SetForceSensorPayLoadCog(cog);
        double weight = 0;

        List<Number> rtnArrays = robot.GetForceSensorPayLoad();
        DescTran getCog = new DescTran(0.0, 0.0, 0.0);
        robot.GetForceSensorPayLoadCog(getCog);
        System.out.println("the FT load is " +  rtnArrays.get(1) + "  cog is  " + getCog.x + "  " + getCog.y + "   " + getCog.z);
    }

力传感器自动校零
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器自动校零
    * @param [in] massCenter 传感器质量(kg) 及 质心(mm)
    * @return 错误码
    */
    int ForceSensorAutoComputeLoad(MassCenter massCenter);