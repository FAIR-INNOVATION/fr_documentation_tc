机器人安全设置
=================

.. toctree:: 
    :maxdepth: 5

设置碰撞等级
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 设置碰撞等级
    * @param  [in]  mode  0-等级，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应范围[],百分比对应范围[0~1]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  错误码
    */
    int SetAnticollision(int mode, double[] level, int config); 

设置碰撞后策略
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置碰撞后策略
    * @param  [in] strategy  0-报错停止，1-继续运行
    * @param  [in] safeTime  安全停止时间[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距离[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全系数[1-10]
    * @return  错误码
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int[] safetyMargin); 

设置正限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置正限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitPositive(double[] limit); 

设置负限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置负限位
    * @param  [in] limit 六个关节位置，单位deg
    * @return  错误码
    */
    int SetLimitNegative(double[] limit); 

错误状态清除
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  错误状态清除
    * @return  错误码
    */
    int ResetAllError(); 

关节摩擦力补偿开关
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 关节摩擦力补偿开关 
    * @param [in] state 0-关，1-开 
    * @return 错误码 
    */ 
    int FrictionCompensationOnOff(byte state); 

设置关节摩擦力补偿系数-正装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-正装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_level(double[] coeff);

设置关节摩擦力补偿系数-侧装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-侧装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_wall(double[] coeff); 

设置关节摩擦力补偿系数-倒装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-倒装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_ceiling(double[] coeff);

设置关节摩擦力补偿系数-自由安装
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置关节摩擦力补偿系数-自由安装
    * @param  [in]  coeff 六个关节补偿系数，范围[0~1]
    * @return  错误码
    */
    int SetFrictionValue_freedom(double[] coeff);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int mode = 0;
        int config = 1;
        double[] level1 = new double[6] { 1.0, 2.0, 3.0, 4.0, 5.0, 6.0 };
        double[] level2 = new double[6] { 0.5, 0.2, 0.3, 0.4, 0.5, 0.12 };

        robot.SetAnticollision(mode, level1, config);
        mode = 1;
        robot.SetAnticollision(mode, level2, config);
        robot.SetCollisionStrategy(2);

        double[] plimit = new double[6] { 170.0, 80.0, 150.0, 80.0, 170.0, 160.0 };
        int rtn = robot.SetLimitPositive(plimit);
        Console.WriteLine($"SetLimitPositive  rtn  {rtn}");
        double[] nlimit = new double[6] { -170.0, -260.0, -150.0, -260.0, -170.0, -160.0 };
        rtn = robot.SetLimitNegative(nlimit);
        Console.WriteLine($"SetLimitNegative  rtn  {rtn}");

        robot.ResetAllError();

        double[] lcoeff = new double[6] { 0.9, 0.9, 0.9, 0.9, 0.9, 0.9 };
        double[] wcoeff = new double[6] { 0.4, 0.4, 0.4, 0.4, 0.4, 0.4 };
        double[] ccoeff = new double[6] { 0.6, 0.6, 0.6, 0.6, 0.6, 0.6 };
        double[] fcoeff = new double[6] { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        robot.FrictionCompensationOnOff(1);
        rtn = robot.SetFrictionValue_level(lcoeff);
        Console.WriteLine($"SetFrictionValue_level  rtn  {rtn}");
        rtn = robot.SetFrictionValue_wall(wcoeff);
        Console.WriteLine($"SetFrictionValue_wall  rtn  {rtn}");
        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        Console.WriteLine($"SetFrictionValue_ceiling  rtn  {rtn}");
        rtn = robot.SetFrictionValue_freedom(fcoeff);
        Console.WriteLine($"SetFrictionValue_freedom  rtn  {rtn}");
    }
