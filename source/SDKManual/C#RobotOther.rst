其他接口
================

.. toctree:: 
    :maxdepth: 5

传动带启动、停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带启动、停止 
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */ 
    int ConveyorStartEnd(byte status); 

记录IO检测点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录IO检测点 
    * @return 错误码 
    */ 
    int ConveyorPointIORecord(); 

记录A点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录A点 
    * @return 错误码 
    */ 
    int ConveyorPointARecord();

记录参考点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录参考点 
    * @return 错误码 
    */ 
    int ConveyorRefPointRecord(); 

记录B点
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 记录B点 
    * @return 错误码 
    */ 
    int ConveyorPointBRecord();

传送带工件IO检测
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传送带工件IO检测 
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码 
    */ 
    int ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取物体当前位置 
    * @param [in] mode 1-跟踪抓取，2-跟踪运动，3-TPD跟踪
    * @return 错误码 
    */ 
    int ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带跟踪开始 
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */
    int ConveyorTrackStart(byte status);

传动带跟踪停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带跟踪停止 
    * @return 错误码 
    */
    int ConveyorTrackEnd();

传动带参数配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传动带参数配置 
    * @param [in] encChannel 编码器通道 1~2
    * @param [in] resolution 编码器转一圈的脉冲数
    * @param [in] lead 编码器转一圈传送带行走距离
    * @param [in] wpAxis 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] vision 是否配视觉  0-不配，1-配
    * @param [in] speedRadio 速度比:针对传送带跟踪抓取选项（1-100）其他选项默认为1
    * @return 错误码 
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio);

设置传动带抓取点补偿
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置传动带抓取点补偿 
    * @param [in] cmp 补偿位置 double[3]{x, y, z}
    * @return 错误码 
    */
    int ConveyorCatchPointComp(double[] cmp);

传送带跟踪直线运动
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 传送带跟踪直线运动 
    * @param [in] name 运动点名称
    * @param [in] tool 工具坐标号，范围[0~14] 
    * @param [in] wobj 工件坐标号，范围[0~14] 
    * @param [in] vel 速度百分比，范围[0~100] 
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放 
    * @param [in] ovl 速度缩放因子，范围[0~100] 
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm  
    * @return 错误码 
    */
    int ConveyorTrackMoveL(string name, int tool, int wobj, float vel, float acc, float ovl, float blendR);

代码示例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnConvert_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose pos1 = new DescPose(0, 0, 0, 0 ,0 ,0);
        DescPose pos2 = new DescPose(0, 0, 0, 0, 0, 0);

        pos1.tran.x = -351.175;
        pos1.tran.y = 3.389;
        pos1.tran.z = 431.172;
        pos1.rpy.rx = -179.111;
        pos1.rpy.ry = -0.241;
        pos1.rpy.rz = 90.388;

        pos2.tran.x = -333.654;
        pos2.tran.y = -229.003;
        pos2.tran.z = 404.335;
        pos2.rpy.rx = -179.139;
        pos2.rpy.ry = -0.779;
        pos2.rpy.rz = 91.269;
        int rtn = -1;

        double[] cmp = new double[3] { 0, 9.99, 0};
        rtn = robot.ConveyorCatchPointComp(cmp);
        if(rtn != 0)
        {
            return;
        }
        Console.WriteLine($"ConveyorCatchPointComp: rtn  {rtn}");

        rtn = robot.MoveCart(pos1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.ConveyorIODetect(10000);
        Console.WriteLine($"ConveyorIODetect: rtn  {rtn}");

        robot.ConveyorGetTrackData(1);
        rtn = robot.ConveyorTrackStart(1);
        Console.WriteLine($"ConveyorTrackStart: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 59, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd: rtn  {rtn}");

        rtn = robot.MoveCart(pos2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 100, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");
    }

获取SSH公钥
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SSH公钥 
    * @param [out] keygen 公钥
    * @return 错误码 
    */
    int GetSSHKeygen(ref string keygen);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算指定路径下文件的MD5值 
    * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
    * @param [out] md5 文件MD5值
    * @return 错误码 
    */
    int ComputeFileMD5(string file_path, ref string md5);

获取机器人急停状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人急停状态 
    * @param [out] state 急停状态，0-非急停，1-急停
    * @return 错误码 
    */
    int GetRobotEmergencyStopState(ref byte state);

获取SDK与机器人的通讯状态
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取SDK与机器人的通讯状态 
    * @param [out] state 通讯状态，0-通讯正常，1-通讯异常
    * @return 错误码 
    */
    int GetSDKComState(ref int state)

获取安全停止信号
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取安全停止信号 
    * @param [out] si0_state 安全停止信号SI0，0-无效，1-有效
    * @param [out] si1_state 安全停止信号SI1，0-无效，1-有效
    * @return 错误码 
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state)

获取机器人DH参数补偿值
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取安全停止信号 
    * @param [out] dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码 
    */
    int GetDHCompensation(ref double[] dhCompensation)

代码示例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnTestOthers_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        double[] dhCompensation = new double[6]{0,0,0,0,0,0};
        rtn = robot.GetDHCompensation(ref dhCompensation);
        Console.WriteLine($"GetDHCompensation:  rtn :{rtn}    {dhCompensation[0]}  {dhCompensation[1]}  {dhCompensation[2]}  {dhCompensation[3]}  {dhCompensation[4]}  {dhCompensation[5]}");
        string ssh = "";
        rtn = robot.GetSSHKeygen(ref ssh);
        Console.WriteLine($"GetSSHKeygen:  ssh {ssh}  rtn  {rtn}");
        string file_path = "/fruser/test.txt";
        string md5 = "";
        robot.ComputeFileMD5(file_path, ref md5);

        byte state = 255;
        rtn = robot.GetRobotEmergencyStopState(ref state);
        Console.WriteLine($"GetRobotEmergencyStopState:  rtn  {rtn}   state {state}");

        int comState = -1;
        rtn = robot.GetSDKComState(ref comState);
        Console.WriteLine($"GetSDKComState:  rtn  {rtn}   state  {comState}");

        byte si0_state = 255;
        byte si1_state = 255;

        rtn = robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState:  rtn  {rtn}   si0_state  {si0_state}   si1_state  {si1_state}");
    }

上传点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从本地计算机上传至机器人控制器 
    * @param [in] pointTableFilePath 点位表在本地计算机的绝对路径C://test/pointTabl e1.db
    * @return 错误码 
    */
    int PointTableUpLoad(string pointTableFilePath);

下载点位表
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 点位表从机器人控制器下载到本地计算机 
    * @param [in] pointTableName 控制器中的点位表名称：pointTable1.db
    * @param [in] saveFilePath 点位表下载到计算机的路径 C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(string pointTableName, string saveFilePath);

点位表更新Lua程序
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 使用给定的点位表更新lua程序中的点
    * @param [in] pointTableName 控制器中的点位表名称："pointTable1.db", 当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "test.lua"
    * @param [out] errorStr 点位表更新lua错误信息  
    * @return 错误码 
    */
    int PointTableUpdateLua(string pointTableName, string luaFileName, ref string errorStr);

代码示例
+++++++++
.. code-block:: c#
    :linenos:

    private void btnUpload_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        int rtn = -1;
        rtn = robot.PointTableUpLoad("C://point_table_test.db");
        Thread.Sleep(2000);
        rtn = robot.PointTableDownLoad("point_table_test.db", "D://zDOWN/");
        string errorStr = "";
        rtn = robot.PointTableUpdateLua("point_table_test.db", "test.lua", ref errorStr);
        Console.WriteLine($"PointTableSwitch rtn  is {rtn}" + errorStr);
        rtn = robot.ProgramLoad("/fruser/test.lua");
        rtn = robot.ProgramRun();
    }

初始化日志参数
+++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 初始化日志参数
    * @param [in] logType：输出模式，DIRECT-直接输出；BUFFER-缓冲输出；ASYNC-异步输出
    * @param [in] logLevel：日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @param [in] filePath: 文件保存路径，如“D://Log/”
    * @param [in] saveFileNum：保存文件个数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @param [in] saveDays: 保存文件天数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @return 错误码
    */
    public int LoggerInit(FrLogType logType = FrLogType.DIRECT, FrLogLevel logLevel = FrLogLevel.ERROR, string filePath = "", int saveFileNum = 10, int saveDays = 10);

设置日志过滤等级
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param [in] logLevel: 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @return 错误码
    */
    public int SetLoggerLevel(FrLogLevel logLevel);


代码示例
+++++++++

.. versionadded:: C#SDK-v1.0.5

.. code-block:: c#
    :linenos:

    private void btnTestLog_Click(object sender, EventArgs e)
    {
        robot = new Robot();//实例化机器人对象
        robot.RPC("192.168.58.2"); //与控制箱建立连接
        string path = "D://log/";
        robot.LoggerInit(FrLogType.ASYNC, FrLogLevel.DEBUG, path, 5, 5);
        robot.SetLoggerLevel(FrLogLevel.INFO);
    }

设置机器人外设协议
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int SetExDevProtocol(int protocol);

获取机器人外设协议
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人外设协议
    * @param [out] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int GetExDevProtocol(ref int protocol);

代码示例
++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: console
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int protocol = 4098;//ModbusMaster 
        robot.SetExDevProtocol(protocol);

        robot.GetExDevProtocol(ref protocol);
        Console.Writeline("protocol is" + protocol);
    }

