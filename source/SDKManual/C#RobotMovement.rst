机器人运动
============

.. toctree:: 
    :maxdepth: 5


jog点动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief jog 点动 
    * @param [in] refType 点动类型：0-关节点动，2-基坐标系下点动，4-工具坐标系下点动，8-工件坐标系下点动 
    * @param [in] nb 1-关节 1(或 x 轴)，2-关节 2(或 y 轴)，3-关节 3(或 z 轴)，4-关节4(或绕x轴旋转)，5-关节5(或绕y轴旋转)，6-关节6(或绕z轴旋转)
    * @param [in] dir 0-负方向，1-正方向 
    * @param [in] vel 速度百分比，[0~100] 
    * @param [in] acc 加速度百分比， [0~100] 
    * @param [in] max_dis 单次点动最大角度，单位[°]或距离，单位[mm] 
    * @return 错误码 
    */ 
    int StartJOG(byte refType, byte nb, byte dir, float vel, float acc, float max_dis);

jog点动减速停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  jog点动减速停止
    * @param  [in]  ref  1-关节点动停止，3-基坐标系下点动停止，5-工具坐标系下点动停止，9-工件坐标系下点动停止
    * @return  错误码
    */
    int StopJOG(byte stopType);

jog点动立即停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief jog点动立即停止
    * @return  错误码
    */
    int ImmStopJOG(); 

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJOG_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        robot.SetSpeed(35);
        robot.StartJOG(0, 1, 0, 15, 20.0f, 30.0f);   //单关节运动，StartJOG为非阻塞指令，运动状态下接收其他运动指令（包含StartJOG）会被丢弃
        Thread.Sleep(1000);
        robot.StopJOG(1);  //机器人单轴点动减速停止
        //robot.ImmStopJOG();  //机器人单轴点动立即停止
        robot.StartJOG(0, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(2, 1, 0, 15, 20.0f, 30.0f);   //基坐标系下点动
        Thread.Sleep(1000);
        robot.StopJOG(3);  //机器人单轴点动减速停止
        //robot.ImmStopJOG();  //机器人单轴点动立即停止
        robot.StartJOG(2, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(4, 1, 0, 15, 20.0f, 30.0f);   //工具坐标系下点动
        Thread.Sleep(1000);
        robot.StopJOG(5);  //机器人单轴点动减速停止
        //robot.ImmStopJOG();  //机器人单轴点动立即停止
        robot.StartJOG(4, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(8, 1, 0, 15, 20.0f, 30.0f);   //工件坐标系下点动
        Thread.Sleep(1000);
        robot.StopJOG(9);  //机器人单轴点动减速停止
        //robot.ImmStopJOG();  //机器人单轴点动立即停止
        robot.StartJOG(8, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
    }

关节空间运动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  关节空间运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] desc_pos   目标笛卡尔位姿
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos); 

笛卡尔空间直线运动
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos, int overSpeedStrategy = 0, int speedPercent = 10); 

笛卡尔空间圆弧运动
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, byte poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, byte toffset_flag, DescPose offset_pos_t, float ovl, float blendR); 

笛卡尔空间整圆运动
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, float ovl, byte offset_flag, DescPose offset_pos);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMovetest_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        JointPos j1, j2, j3, j4;
        DescPose desc_pos1, desc_pos2, desc_pos3, desc_pos4, offset_pos;
        ExaxisPos epos;

        j1 = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        j2 = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);

        j3 = new JointPos(-71.746, -87.177, 123.953, -126.25, -89.429, -0.089);
        desc_pos3 = new DescPose(-345.155, 535.733, 421.269, 179.475, 0.571, 18.332);

        ExaxisPos ePos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset = new DescPose();

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;

        robot.SetSpeed(20);
        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, ePos, blendT, flag, offset);
        Console.WriteLine($"movej errcode:  {err}");

        Thread.Sleep(1000);
        err = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, ePos, search, flag, offset);
        Console.WriteLine($"moveL errcode:  {err}");

        Thread.Sleep(1000);
        err = robot.MoveL(j1, desc_pos1, tool, user, vel, acc, ovl, blendR, ePos, search, flag, offset);
        Console.WriteLine($"moveL errcode:  {err}");

        Thread.Sleep(1000);
        err = robot.MoveC(j2, desc_pos2, tool, user, vel, acc, ePos, flag, offset, j3, desc_pos3, tool, user, vel, acc, ePos, flag, offset, ovl, blendR);
        Console.WriteLine($"circle errcode:  {err}");

        Thread.Sleep(1000);
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, ePos, blendT, flag, offset);
        Console.WriteLine($"movej errcode:  {err}");

        Thread.Sleep(1000);
        err = robot.Circle(j2, desc_pos2, tool, user, vel, acc, ePos, j3, desc_pos3, tool, user, vel, acc, ePos, ovl, flag, offset);
        Console.WriteLine($"circle errcode:  {err}");
    }

笛卡尔空间螺旋线运动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡尔空间螺旋线运动 
    * @param [in] joint_pos 目标关节位置,单位 deg 
    * @param [in] desc_pos 目标笛卡尔位姿 
    * @param [in] tool 工具坐标号，范围[0~14] 
    * @param [in] user 工件坐标号，范围[0~14] 
    * @param [in] vel 速度百分比，范围[0~100] 
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放 
    * @param [in] epos 扩展轴位置，单位 mm 
    * @param [in] ovl 速度缩放因子，范围[0~100] 
    * @param [in] offset_flag 0-不偏移，1-基坐标系/工件坐标系下偏移，2-工具坐标系下偏移 
    * @param [in] offset_pos 位姿偏移量 
    * @param [in] spiral_param 螺旋参数 
    * @return 错误码 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, ExaxisPos epos, float ovl, byte offset_flag, DescPose offset_pos, SpiralParam spiral_param); 

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescSpiral_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        JointPos j;
        DescPose desc_pos;
        DescPose offset_pos1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos2 = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp;

        j = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        offset_pos1.tran.x = 50.0;
        offset_pos1.rpy.rx = -30.0;
        offset_pos2.tran.x = 50.0;
        offset_pos2.rpy.rx = -5.0;

        sp.circle_num = 5;
        sp.circle_angle = 1.0f;
        sp.rad_init = 10.0f;
        sp.rad_add = 40.0f;
        sp.rotaxis_add = 10.0f;
        sp.rot_direction = 0;

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        byte flag = 2;

        robot.SetSpeed(20);
        int ret = robot.GetForwardKin(j, ref desc_pos);  //只有关节位置的情况下，可用正运动学接口求解笛卡尔空间坐标
        if (ret == 0)
        {
            int err = -1;
            err = robot.MoveJ(j, desc_pos, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
            Console.WriteLine($"movej errcode:  {err}");

            err = robot.NewSpiral(j, desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp);
            Console.WriteLine($"newspiral errcode:  {err}");
        }
        else
        {
            Console.WriteLine($"GetForwardKin errcode: {ret}");
        }
    }

伺服运动开始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 伺服运动开始，配合ServoJ、ServoCart指令使用
    * @return 错误码 
    */ 
    int ServoMoveStart();

伺服运动结束
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 伺服运动结束，配合ServoJ、ServoCart指令使用
    * @return 错误码 
    */ 
    int ServoMoveEnd();

关节空间伺服模式运动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  关节空间伺服模式运动
    * @param  [in] joint_pos  目标关节位置,单位deg
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放，默认为0
    * @param  [in] vel  速度百分比，范围[0~100]，暂不开放，默认为0
    * @param  [in] cmdT  指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param  [in] filterT 滤波时间，单位s，暂不开放，默认为0
    * @param  [in] gain  目标位置的比例放大器，暂不开放，默认为0
    * @return  错误码
    */
    int ServoJ(JointPos joint_pos, float acc, float vel, float cmdT, float filterT, float gain);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJointServoMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        JointPos j = new JointPos(0, 0, 0, 0, 0, 0);

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 200;
        float dt = 0.1f;
        int ret = robot.GetActualJointPosDegree(flag, ref j);
        if (ret == 0)
        {
            while (count > 0)
            {
                robot.ServoJ(j, acc, vel, cmdT, filterT, gain);
                j.jPos[0] += dt;
                count -= 1;
                robot.WaitMs((int)(cmdT * 1000));
            }
        }
        else
        {
            Console.WriteLine($"GetActualJointPosDegree errcode:  {ret}");
        }
    }

笛卡尔空间伺服模式运动
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡尔空间伺服模式运动
    * @param  [in]  mode  0-绝对运动(基坐标系)，1-增量运动(基坐标系)，2-增量运动(工具坐标系)
    * @param  [in]  desc_pos  目标笛卡尔位姿或位姿增量
    * @param  [in]  pos_gain  位姿增量比例系数，仅在增量运动下生效，范围[0~1]
    * @param  [in] acc  加速度百分比，范围[0~100],暂不开放，默认为0
    * @param  [in] vel  速度百分比，范围[0~100]，暂不开放，默认为0
    * @param  [in] cmdT  指令下发周期，单位s，建议范围[0.001~0.0016]
    * @param  [in] filterT 滤波时间，单位s，暂不开放，默认为0
    * @param  [in] gain  目标位置的比例放大器，暂不开放，默认为0
    * @return  错误码
    */
    int ServoCart(int mode, DescPose desc_pos, double[] pos_gain, float acc, float vel, float cmdT, float filterT, float gain);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescServoMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose desc_pos_dt = new DescPose(0, 0, 0, 0, 0, 0);
        desc_pos_dt.tran.z = -0.5;
        double[] pos_gain = new double[6]{ 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 };
        int mode = 2;
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        int flag = 0;
        int count = 500;

        robot.SetSpeed(20);
        while (count > 0)
        {
            robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            robot.WaitMs((int)(cmdT * 1000));
        }
    }

笛卡尔空间点到点运动
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 笛卡尔空间点到点运动 
    * @param [in] desc_pos 基坐标系下目标笛卡尔位姿 
    * @param [in] tool 工具坐标号，范围[0~14] 
    * @param [in] user 工件坐标号，范围[0~14] 
    * @param [in] vel 速度百分比，范围[0~100] 
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放 
    * @param [in] ovl 速度缩放因子，范围[0~100] 
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位 ms 
    * @param [in] config 关节空间配置，[-1]-参考当前关节位置解算，[0~7]-参考特定关节空间配置解算，默认为-1 
    * @return 错误码 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescPTPMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose desc_pos1, desc_pos2, desc_pos3;
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);
        desc_pos3 = new DescPose(-345.155, 535.733, 421.269, 179.475, 0.571, 18.332);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendT1 = 0.0f;
        int config = -1;

        robot.SetSpeed(20);
        robot.MoveCart(desc_pos1, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(desc_pos2, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(desc_pos3, tool, user, vel, acc, ovl, blendT1, config);
    }

样条运动开始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  样条运动开始
    * @return  错误码
    */
    int SplineStart();

样条运动PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl);

样条运动结束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  样条运动结束
    * @return  错误码
    */
    int SplineEnd(); 

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSplineMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        JointPos j1, j2, j3, j4;
        DescPose desc_pos1, desc_pos2, desc_pos3, desc_pos4, offset_pos;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        j2 = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);

        j3 = new JointPos(-49.129, -68.49, 103.297, -128.898, -91.478, -0.062);
        desc_pos3 = new DescPose(-680.308, 547.378, 399.189, -175.909, -1.479, 40.827);

        j4 = new JointPos(-56.126, -54.093, 80.686, -121.655, -91.428, -0.064);
        desc_pos4 = new DescPose(-719.201, 790.816, 389.118, -174.939, -1.428, 33.809);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;
        robot.SetSpeed(20);
        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");
                
        robot.SplineStart();
        robot.SplinePTP(j1, desc_pos1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, desc_pos2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, desc_pos3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, desc_pos4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
    }

新样条运动开始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @param [in] type  0-圆弧过渡，1-给定点位为路径点
    * @param [in] averageTime  全局平均衔接时间(ms)(10 ~  )，默认2000
    * @return 错误码 
    */ 
    int NewSplineStart(int type, int averageTime=2000);
    
新样条指令点
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 增加样条运动指令点 
    * @param [in] joint_pos 目标关节位置,单位 deg 
    * @param [in] desc_pos 目标笛卡尔位姿 
    * @param [in] tool 工具坐标号，范围[0~14] 
    * @param [in] user 工件坐标号，范围[0~14] 
    * @param [in] vel 速度百分比，范围[0~100] 
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放 
    * @param [in] ovl 速度缩放因子，范围[0~100] 
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] lastFlag  是否为最后一个点，0-否，1-是
    * @return 错误码 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新样条运动结束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 新样条运动开始 
    * @return 错误码 
    */ 
    int NewSplineEnd();
    
终止运动
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 终止运动
    * @return  错误码
    */
    int StopMotion();

暂停运动
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
      * @brief 暂停运动 
      * @return 错误码 
    */  
    int PauseMotion();

恢复运动
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 恢复运动 
    * @return 错误码 
    */ 
    int ResumeMotion();

点位整体偏移开始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  点位整体偏移开始
    * @param  [in]  flag  0-基坐标系下/工件坐标系下偏移，2-工具坐标系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


点位整体偏移结束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  点位整体偏移结束
    * @return  错误码
    */
    int PointsOffsetDisable(); 

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnPointOffect_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        JointPos j1, j2;
        DescPose desc_pos1, desc_pos2, offset_pos, offset_pos1;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        j2 = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos1 = new DescPose(50.0, 50.0, 50.0, 5.0, 5.0, 5.0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendR = 0.0f;
        byte flag = 0;
        int type = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetEnable(type, offset_pos1);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.PointsOffsetDisable();
    }

控制箱AO飞拍开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制箱AO飞拍停止
    * @return 错误码
    */
    int MoveAOStop();
    
末端AO飞拍开始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 末端AO飞拍停止
    * @return 错误码
    */
    int MoveToolAOStop();

代码示例
************
.. code-block:: c#
    :linenos:

    private void btnMoveAO_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose();
        JointPos startjointPos = new JointPos();
        DescPose enddescPose = new DescPose();
        JointPos endjointPos = new JointPos();
        DescPose CPose = new DescPose();
        JointPos CJPos = new JointPos();
        DescPose DPose = new DescPose();
        JointPos DJPos = new JointPos();            
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.MoveToolAOStart(0, 100, 80, 1);
        //int rtn = robot.MoveAOStart(0, 100, 80, 1);
        Console.WriteLine(rtn);

        rtn = robot.MoveL(startjointPos, startdescPose, 0, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        //robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, 0, 0, offdese);
        //robot.MoveC(startjointPos, startdescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, 0);
        //robot.Circle(startjointPos, startdescPose, 0, 0, 100, 100, exaxisPos, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 100, 0, offdese);
        //robot.SplineStart();
        //robot.SplinePTP(startjointPos, startdescPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(endjointPos, enddescPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(CJPos, CPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(DJPos, DPose, 0, 0, 100, 100, 100);
        //robot.SplineEnd();

        //robot.NewSplineStart(0, 5000);
        //robot.NewSplinePoint(startjointPos, startdescPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(endjointPos, enddescPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(CJPos, CPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(DJPos, DPose, 0, 0, 100, 100, 100, 5, 1);
        //robot.NewSplineEnd();
        //int count = 1000;
        //while (count > 0)
        //{
        //    robot.ServoJ(startjointPos, 0, 0, 0.008f, 0, 0);
        //    startjointPos.jPos[0] += 0.01;//0关节位置增加
        //    count -= 1;
        //}
        rtn = robot.MoveToolAOStop();
        //rtn = robot.MoveAOStop();
        Console.WriteLine(rtn);
    }

开始奇异位姿保护
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 开始奇异位姿保护
    * @param [in] protectMode 奇异保护模式，0：关节模式；1-笛卡尔模式
    * @param [in] minShoulderPos 肩奇异调整范围(mm), 默认100
    * @param [in] minElbowPos 肘奇异调整范围(mm), 默认50
    * @param [in] minWristPos 腕奇异调整范围(°), 默认10
    * @return 错误码
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇异位姿保护
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 停止奇异位姿保护
    * @return 错误码
    */
    int SingularAvoidEnd();

代码示例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void btnTestSingularAvoidEArc_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(-352.437, -88.350, 226.471, 177.222, 4.924, 86.631);
        JointPos startjointPos = new JointPos(-3.463, -84.308, 105.579, -108.475, -85.087, -0.334);

        DescPose middescPose = new DescPose(-518.339, -23.706, 207.899, -178.420, 0.171, 71.697);
        JointPos midjointPos = new JointPos(-8.587, -51.805, 64.914, -104.695, -90.099, 9.718);

        DescPose enddescPose = new DescPose(-273.934, 323.003, 227.224, 176.398, 2.783, 66.064);
        JointPos endjointPos = new JointPos(-63.460, -71.228, 88.068, -102.291, -90.149, -39.605);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveL(startjointPos, startdescPose, 0, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.SingularAvoidStart(1, 100, 50, 10);
        robot.MoveC(midjointPos, middescPose, 0, 0, 50, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1);
        robot.SingularAvoidEnd();
    }
