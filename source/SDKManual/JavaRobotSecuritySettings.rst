机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置碰撞等级
    * @param  [in]  mode  0-等级，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应范围[1 - 10对应等级1-10， 100-关闭],百分比对应范围[0~10 对应 0% - 100%]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  错误码
    */
    int SetAnticollision(int mode, Object[] level, int config); 

设置碰撞后策略
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置碰撞后策略
    * @param  [in] strategy  0-报错停止，1-继续运行
    * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距离[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全系数[1-10]
    * @return  错误码  
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]); 

设置正限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置正限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitPositive(Object[] limit); 

设置负限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置负限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitNegative(Object[] limit); 

错误状态清除
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  错误状态清除
    * @return  错误码
    */
    int ResetAllError(); 

代码示例
++++++++++++++++++++++++++++++++
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
        Object[] config = {2.0, 2.0, 2.0, 2.0, 2.0, 2.0};
        robot.SetAnticollision(0, config, 1);
        int safetyMargin[]={10,10,10,10,10,10};
        robot.SetCollisionStrategy(0,1000,10,safetyMargin);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();//运行lua文件

        Object[] plimit = { 170.0, 80.0, 150.0, 80.0, 170.0, 160.0 };
        robot.SetLimitPositive(plimit);

        Object[] nlimit = { -170.0, -260.0, -150.0, -260.0, -170.0, -160.0 };
        robot.SetLimitNegative(nlimit);

        robot.SetLoadWeight(123.0);
        robot.Sleep(3000);
        robot.ResetAllError();
    }

关节摩擦力补偿开关
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 关节摩擦力补偿开关 
    * @param [in] state  0-关，1-开
    * @return 错误码 
    */ 
    int FrictionCompensationOnOff(int state); 

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-正装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_level(Object[] coeff);

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-侧装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_wall(Object[] coeff); 

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-倒装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_ceiling(Object[] coeff);

设置关节摩擦力补偿系数-自由安装
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-自由安装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_freedom(Object[] coeff);

代码示例
++++++++++++++++++++++++++++++++
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
        Object[] lcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] wcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] ccoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] fcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };

        robot.FrictionCompensationOnOff(1);

        robot.SetFrictionValue_level(lcoeff);//正装

        robot.SetFrictionValue_wall(wcoeff);//侧装

        robot.SetFrictionValue_ceiling(ccoeff);//倒装

        robot.SetFrictionValue_freedom(fcoeff);//自由安装
    }

开始奇异位姿保护
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  开始奇异位姿保护
    * @param  [in]  protectMode 奇异保护模式，0：关节模式；1-笛卡尔模式
    * @param  [in]  minShoulderPos 肩奇异调整范围(mm), 默认100
    * @param  [in]  minElbowPos 肘奇异调整范围(mm), 默认50
    * @param  [in]  minWristPos 腕奇异调整范围(°), 默认10
    * @return  错误码
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇异位姿保护
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  停止奇异位姿保护
    * @return  错误码
    */
    int SingularAvoidEnd();

代码示例
++++++++++++++++++++++++++++++++
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
        DescPose startdescPose=new DescPose(-402.473, -185.876, 103.985, -175.367, 59.682, 94.221);
        JointPos startjointPos=new JointPos(-0.095, -50.828, 109.737, -150.708, -30.225, -0.623);

        DescPose enddescPose=new DescPose(-399.264, -184.434, 296.022, -4.402, 58.061, -94.161);
        JointPos endjointPos=new JointPos(-0.095, -65.547, 105.145, -131.397, 31.851, -0.622);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveL(startjointPos, startdescPose, 0, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.SingularAvoidStart(0, 150, 50, 20);
        robot.MoveL(endjointPos, enddescPose, 0, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.SingularAvoidEnd();
    }
