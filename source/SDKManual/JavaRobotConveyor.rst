传送带
============

.. toctree:: 
    :maxdepth: 5

传动带启动、停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带启动、停止
    * @param  [in] status 状态，1-启动，0-停止
    * @return  错误码
    */
    int ConveyorStartEnd(int status);

记录IO检测点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录IO检测点
    * @return  错误码
    */
    int ConveyorPointIORecord();

记录A点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录A点
    * @return  错误码
    */
    int ConveyorPointARecord(); 

记录参考点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录参考点
    * @return  错误码
    */
    int ConveyorRefPointRecord();

记录B点
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  记录B点
    * @return 错误码
    */
    int ConveyorPointBRecord(); 

传动带参数配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传动带参数配置
    * @param [in] encChannel 编码器通道 1~2
    * @param [in] resolution 编码器转一圈的脉冲数
    * @param [in] lead 编码器转一圈传送带行走距离
    * @param [in] wpAxis 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
    * @param [in] vision 是否配视觉  0 不配  1 配
    * @param [in] speedRadio 速度比  针对传送带跟踪抓取选项（1-100）  其他选项默认为1
    * @return 错误码
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio); 

设置传动带抓取点补偿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置传动带抓取点补偿
    * @param [in] cmp 补偿位置 double[3]{x, y, z}
    * @return 错误码 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

传送带工件IO检测
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传送带工件IO检测
    * @param [in] max_t 最大检测时间，单位ms
    * @return 错误码 
    */ 
    int ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取物体当前位置
    * @param [in] mode 1-跟踪抓取，2-跟踪运动，3-TPD跟踪
    * @return 错误码 
    */ 
    int ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪开始
    * @param [in] status 状态，1-启动，0-停止
    * @return 错误码 
    */ 
    int ConveyorTrackStart(int status);

传动带跟踪停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 传动带跟踪停止
    * @return 错误码 
    */ 
    int ConveyorTrackEnd();

直线运动
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 直线运动
    * @param [in] name 运动点描述
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] wobj 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码 
    */ 
    int ConveyorTrackMoveL(String name, int tool, int wobj, double vel, double acc, double ovl, double blendR);   

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
        int rtn = -1;
        rtn = robot.ConveyorPointIORecord();//记录IO切入点
        System.out.println("ConveyorPointIORecord: rtn " + rtn);

        rtn = robot.ConveyorPointARecord();//记录A点
        System.out.println("ConveyorPointARecord: rtn " + rtn);

        rtn = robot.ConveyorRefPointRecord();//记录参考点
        System.out.println("ConveyorRefPointRecord: rtn  " + rtn);

        rtn = robot.ConveyorPointBRecord();//记录B点
        System.out.println("ConveyorPointBRecord: rtn " + rtn);

        //配置传送带
        robot.ConveyorSetParam(1, 10000, 2.0, 1, 1, 20);
        System.out.println("ConveyorSetParam: rtn  " + rtn);
        //传送带跟踪抓取
        DescPose pos1 = new DescPose(-351.549,87.914,354.176,-179.679,-0.134,2.468);
        DescPose pos2 = new DescPose(-351.203,-213.393,351.054,-179.932,-0.508,2.472);

        Object[] cmp = {0.0, 0.0, 0.0};
        rtn = robot.ConveyorCatchPointComp(cmp);//设置传动带抓取点补偿
        if(rtn != 0)
        {
            return;
        }
        System.out.println("ConveyorCatchPointComp: rtn  " + rtn);

        rtn = robot.MoveCart(pos1, 1, 0, 30.0, 180.0, 100.0, -1.0, -1);
        System.out.println("MoveCart: rtn  " + rtn);

        rtn = robot.ConveyorIODetect(10000);//传送带工件IO检测
        System.out.println("ConveyorIODetect: rtn   " + rtn);

        robot.ConveyorGetTrackData(1);//配置传送带跟踪抓取
        rtn = robot.ConveyorTrackStart(1);//跟踪开始
        System.out.println("ConveyorTrackStart: rtn  " + rtn);

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100.0, 0.0, 100.0, -1.0);
        System.out.println("ConveyorTrackMoveL: rtn  " + rtn);

        rtn = robot.MoveGripper(1, 60, 60, 30, 30000, 0);
        System.out.println("MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100.0, 0.0, 100.0, -1.0);
        System.out.println("ConveyorTrackMoveL: rtn   " + rtn);

        rtn = robot.ConveyorTrackEnd();//传送带跟踪停止
        System.out.println("ConveyorTrackEnd: rtn  " + rtn);

        rtn = robot.MoveCart(pos2, 1, 0, 30.0, 180.0, 100.0, -1.0, -1);
        System.out.println("MoveCart: rtn  " + rtn);

        rtn = robot.MoveGripper(1, 100, 60, 30, 30000, 0);
        System.out.println("MoveGripper: rtn  " + rtn);
    } 