机器人运动
============

.. toctree:: 
    :maxdepth: 5


jog点动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief jog 点动 
    * @param [in] refType 0-关节点动，2-基坐标系下点动，4-工具坐标系下点动，8-工件坐标系下点动
    * @param [in] nb 1-关节1(或x轴)，2-关节2(或y轴)，3-关节3(或z轴)，4-关节4(或绕x轴旋转)，5-关节5(或绕y轴旋转)，6-关节6(或绕z轴旋转)
    * @param [in] dir 0-负方向，1-正方向
    * @param [in] vel 速度百分比，[0~100]
    * @param [in] acc 加速度百分比， [0~100]
    * @param [in] max_dis 单次点动最大角度，单位[°]或距离，单位[mm]
    * @return 错误码 
    */ 
    int StartJOG(int refType, int nb, int dir, double vel, double acc, double max_dis);

jog点动减速停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  jog点动减速停止
    * @param  [in]  stopType  1-关节点动停止，3-基坐标系下点动停止，5-工具坐标系下点动停止，9-工件坐标系下点动停止
    * @return  错误码
    */
    int StopJOG(int stopType);

jog点动立即停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief jog点动立即停止
    * @return  错误码
    */
    int ImmStopJOG(); 

代码示例
+++++++++++++++++++++++++++++
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
        robot.StartJOG(0, 1, 0, 30, 100, 90);//关节点动
        robot.Sleep(3000);
        robot.StopJOG(1);//点动减速停止
        robot.StartJOG(0, 1, 0, 30, 100, 90);//关节点动
        robot.Sleep(3000);
        robot.ImmStopJOG();//点动立即停止
    }    

关节空间运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos  目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

笛卡尔空间直线运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间直线运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param  [in] epos  扩展轴位置，单位mm
    * @param  [in] search  0-不焊丝寻位，1-焊丝寻位
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] overSpeedStrategy  超速处理策略，1-标准；2-超速时报错停止；3-自适应降速，默认为0
    * @param  [in] speedPercent  允许降速阈值百分比[0-100]，默认10%
    * @return  错误码
    */   
    int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int overSpeedStrategy, int speedPercent);

笛卡尔空间圆弧运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间圆弧运动
    * @param  [in] joint_pos_p  路径点关节位置,单位deg
    * @param  [in] desc_pos_p   路径点笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目标点关节位置,单位deg
    * @param  [in] desc_pos_t   目标点笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm 
    * @return  错误码
    */      
    int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

笛卡尔空间整圆运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间整圆运动
    * @param  [in] joint_pos_p  路径点1关节位置,单位deg
    * @param  [in] desc_pos_p   路径点1笛卡尔位姿
    * @param  [in] ptool  工具坐标号，范围[0~14]
    * @param  [in] puser  工件坐标号，范围[0~14]
    * @param  [in] pvel  速度百分比，范围[0~100]
    * @param  [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_p  扩展轴位置，单位mm
    * @param  [in] joint_pos_t  路径点2关节位置,单位deg
    * @param  [in] desc_pos_t   路径点2笛卡尔位姿
    * @param  [in] ttool  工具坐标号，范围[0~14]
    * @param  [in] tuser  工件坐标号，范围[0~14]
    * @param  [in] tvel  速度百分比，范围[0~100]
    * @param  [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] epos_t  扩展轴位置，单位mm
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @param  [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */      
    int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos);

代码示例
+++++++++++++++++++++++++++++
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
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        JointPos JP2=new JointPos(72.515,-86.774,81.525,-87.724,-91.964,92.958);
        DescPose DP2=new DescPose(-63.512,-529.698,517.946,-178.192,3.07,69.554);
        JointPos JP3=new JointPos(89.281,-102.959,81.527,-69.955,-86.755,92.958);
        DescPose DP3=new DescPose();
        robot.GetForwardKin(JP3,DP3);

        robot.MoveJ(JP1, DP1,0, 0, 30, 30, 100, epos, -1, 0, offset_pos);//关节空间运动
        robot.MoveL(JP2, DP2,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);//直线运动
        robot.MoveC(JP3, DP3, 0, 0, 30, 100, epos, 0, offset_pos, JP1, DP1, 0, 0, 100, 100, epos, 0, offset_pos, 100, -1);
        robot.Circle(JP3, DP3, 0, 0, 10, 100.0, epos, JP2, DP2, 0, 0, 100.0, 100.0, epos, 100.0, 0, offset_pos);

    }    

笛卡尔空间螺旋线运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡尔空间螺旋线运动 
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param);

代码示例
+++++++++++++++++++++++++++++
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
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        SpiralParam param = new SpiralParam(5,10.0,30.0,10.0,5.0,0);//螺旋线
        robot.NewSpiral(JP1, DP1, 0, 0, 50, 100, epos, 100, 0, offset_pos, param);
    }

伺服运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服运动开始，配合ServoJ、ServoCart指令使用
    * @return 错误码 
    */ 
    int ServoMoveStart();

伺服运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服运动结束，配合ServoJ、ServoCart指令使用
    * @return 错误码 
    */ 
    int ServoMoveEnd();

关节空间伺服模式运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间伺服模式运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] axisPos  外部轴位置,单位mm
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放，默认为0
    * @param  [in] vel  速度百分比，范围[0~100]，暂不开放，默认为0
    * @param  [in] cmdT  指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param  [in] filterT 滤波时间，单位s，暂不开放，默认为0
    * @param  [in] gain  目标位置的比例放大器，暂不开放，默认为0
    * @return  错误码
    */
    int ServoJ(JointPos joint_pos, ExaxisPos axisPos, double acc, double vel, double cmdT, double filterT, double gain);

代码示例
+++++++++++++++++++++++++++++
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
        JointPos j5 = new JointPos();
        ExaxisPos ePos=new ExaxisPos();
        int ret = robot.GetActualJointPosDegree(j5);
        if (ret == 0)
        {
            int count = 200;
            while (count > 0)
            {
                robot.ServoJ(j5, ePos,100, 100, 0.008, 0, 0);
                j5.J1 += 0.2;//1关节位置增加
                count -= 1;
                robot.WaitMs((int)(8));
            }
        }
    }


笛卡尔空间伺服模式运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡尔空间伺服模式运动
    * @param  [in]  mode  0-绝对运动(基坐标系)，1-增量运动(基坐标系)，2-增量运动(工具坐标系)
    * @param  [in]  desc_pose  目标笛卡尔位姿或位姿增量
    * @param  [in]  pos_gain  位姿增量比例系数，仅在增量运动下生效，范围[0~1]
    * @param  [in]  acc  加速度百分比，范围[0~100],暂不开放，默认为0
    * @param  [in]  vel  速度百分比，范围[0~100]，暂不开放，默认为0
    * @param  [in]  cmdT  指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param  [in]  filterT 滤波时间，单位s，暂不开放，默认为0
    * @param  [in]  gain  目标位置的比例放大器，暂不开放，默认为0
    * @return  错误码
    */
    int ServoCart(int mode, DescPose desc_pose, Object[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain);

代码示例
+++++++++++++++++++++++++++++
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
        DescPose desc_pos_dt = new DescPose(0, 0, 0, 0, 0, 0);
        desc_pos_dt.tran.z = -0.5;
        Object[] pos_gain = { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 };//仅z轴增加
        int mode = 2;//工具坐标系下增量运动
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        int count = 200;

        robot.SetSpeed(20);

        while (count > 0)
        {
            robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            robot.WaitMs((int)(cmdT * 1000));
        }
    }

笛卡尔空间点到点运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 笛卡尔空间点到点运动 
    * @param [in] desc_pos  目标笛卡尔位姿或位姿增量
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] config  关节空间配置，[-1]-参考当前关节位置解算，[0~7]-参考特定关节空间配置解算，默认为-1
    * @return 错误码 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendT, int config);

代码示例
+++++++++++++++++++++++++++++
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
        DescPose DP2=new DescPose(-63.512,-529.698,517.946,-178.192,3.07,69.554);
        robot.MoveCart(DP2, 0, 0, 30.0, 100.0, 100.0, -1.0, -1);
    }

样条运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  样条运动开始
    * @return  错误码
    */
    int SplineStart();

关节空间样条运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  关节空间样条运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
    * @param  [in] tool  工具坐标号，范围[0~14]
    * @param  [in] user  工件坐标号，范围[0~14]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param  [in] ovl  速度缩放因子，范围[0~100]
    * @return  错误码
    */
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl);

样条运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  样条运动结束
    * @return  错误码
    */
    int SplineEnd(); 

代码示例
+++++++++++++++++++++++++++++
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
        DescPose  desc_p1, desc_p2, desc_p3, desc_p4;//笛卡尔空间位置与姿态
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p4 = new DescPose(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = -104.846;
        desc_p1.tran.y = 309.573;
        desc_p1.tran.z = 336.647;
        desc_p1.rpy.rx = 179.681;
        desc_p1.rpy.ry = -0.419;
        desc_p1.rpy.rz = -92.692;

        desc_p2.tran.x = -318.287;
        desc_p2.tran.y = 158.502;
        desc_p2.tran.z = 346.184;
        desc_p2.rpy.rx = 179.602;
        desc_p2.rpy.ry = 1.081;
        desc_p2.rpy.rz = -46.342;

        desc_p3.tran.x = -352.414;
        desc_p3.tran.y = 24.059;
        desc_p3.tran.z = 395.376;
        desc_p3.rpy.rx = 179.755;
        desc_p3.rpy.ry = -1.045;
        desc_p3.rpy.rz = -23.877;

        desc_p4.tran.x = 195.474;
        desc_p4.tran.y = 423.278;
        desc_p4.tran.z = 228.509;
        desc_p4.rpy.rx = -179.199;
        desc_p4.rpy.ry = -0.567;
        desc_p4.rpy.rz = -130.209;

        JointPos j1 = new JointPos();
        JointPos j2 = new JointPos();
        JointPos j3 = new JointPos();
        JointPos j4 = new JointPos();
        robot.GetInverseKin(0, desc_p1, -1, j1);//逆向运动学求解
        robot.GetInverseKin(0, desc_p2, -1, j2);
        robot.GetInverseKin(0, desc_p3, -1, j3);
        robot.GetInverseKin(0, desc_p4, -1, j4);
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveJ(j1, desc_p1,4, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.SplineStart();
        robot.SplinePTP(j4, desc_p4, 0, 0, 100, 100, 100);
        robot.SplinePTP(j1, desc_p1, 0, 0, 100, 100, 100);
        robot.SplinePTP(j2, desc_p2, 0, 0, 100, 100, 100);
        robot.SplinePTP(j3, desc_p3, 0, 0, 100, 100, 100);
        robot.SplineEnd();
    }

新样条运动开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @param [in] type   0-圆弧过渡，1-给定点位为路径点
    * @param [in] averageTime  全局平均衔接时间(ms)(10 ~  )，默认2000
    * @return 错误码 
    */ 
    int NewSplineStart(int type, int averageTime);
    
新样条指令点
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 增加样条运动指令点 
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] lastFlag 是否为最后一个点，0-否，1-是
    * @return 错误码 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag);

新样条运动结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @return 错误码 
    */ 
    int NewSplineEnd();
    
终止运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 终止运动
    * @return  错误码
    */
    int StopMotion();

暂停运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
      * @brief 暂停运动 
      * @return 错误码 
    */  
    int PauseMotion();

恢复运动
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 恢复运动 
    * @return 错误码 
    */ 
    int ResumeMotion();

点位整体偏移开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  点位整体偏移开始
    * @param  [in]  flag  0-基坐标系下/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in]  offset_pos  位姿偏移量
    * @return  错误码
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


点位整体偏移结束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  点位整体偏移结束
    * @return  错误码
    */
    int PointsOffsetDisable(); 

代码示例
+++++++++++++++++++++++++++++
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
        DescPose desc_p1 =new DescPose(-104.846, 309.573, 336.647, 179.681, -0.419, -92.692);
        DescPose desc_p2=new DescPose(-194.846, 309.573, 336.647, 179.681,-0.419, -92.692;);
        DescPose desc_p3=new DescPose(-254.846, 259.573,336.647, 179.681, -0.419, -92.692;);
        DescPose desc_p4=new DescPose(-304.846,259.573, 336.647, 179.681, -0.419, -92.692;);
        JointPos j1 = new JointPos();
        JointPos j2 = new JointPos();
        JointPos j3 = new JointPos();
        JointPos j4 = new JointPos();
        robot.GetInverseKin(0, desc_p1, -1, j1);//逆向运动学求解
        robot.GetInverseKin(0, desc_p2, -1, j2);
        robot.GetInverseKin(0, desc_p3, -1, j3);
        robot.GetInverseKin(0, desc_p4, -1, j4);
        robot.MoveCart(desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.NewSplineStart(0, 5000);//新样条开始
        robot.NewSplinePoint(j1, desc_p1, 0, 0, 100, 100, 100, 50, 0);//新样条指令点
        robot.NewSplinePoint(j2, desc_p2, 0, 0, 100, 100, 100, 50, 0);
        robot.NewSplinePoint(j3, desc_p3, 0, 0, 100, 100, 100, 50, 0);
        robot.NewSplinePoint(j4, desc_p4, 0, 0, 100, 100, 100, 50, 1);
        robot.NewSplineEnd();//新样条结束

        DescPose off = new DescPose(0, 0, 100, 0, 0, 0);
        robot.PointsOffsetEnable(0, off);
        robot.MoveL(j1, desc_p1,0, 0, 100, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.PointsOffsetDisable();
    }

控制箱AO飞拍开始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飞拍开始
    * @param [in] AONum 控制箱AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飞拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飞拍停止
    * @return 错误码
    */
    int MoveAOStop();
    
末端AO飞拍开始
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飞拍开始
    * @param [in] AONum 末端AO编号
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默认1000
    * @param [in] maxAOPercent 最大TCP速度值对应的AO百分比，默认100%
    * @param [in] zeroZoneCmp 死区补偿值AO百分比，整形，默认为20%，范围[0-100]
    * @return 错误码
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飞拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飞拍停止
    * @return 错误码
    */
    int MoveToolAOStop();

代码示例
+++++++++++++++++++++++++++++
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
        robot.MoveToolAOStart(0, 100, 80, 1);//末端AO飞拍开始
        //robot.MoveAOStart(0, 100, 80, 1);//控制箱AO飞拍
        DescPose  desc_p1, desc_p2;

        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos j1 = new JointPos(-81.684,-106.159,-74.447,-86.33,94.725,41.639);
        JointPos j2 = new JointPos(-102.804,-106.159,-74.449,-86.328,94.715,41.639);

        robot.GetForwardKin(j1,desc_p1);
        robot.GetForwardKin(j2,desc_p2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveL(j1, desc_p1,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.MoveL(j2, desc_p2,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.MoveToolAOStop();
        //robot.MoveAOStop();
    }