機器人安全設定
=================

.. toctree:: 
    :maxdepth: 5

設定碰撞等級
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定碰撞等級
    * @param  [in]  mode  0-等級，1-百分比
    * @param  [in]  level 碰撞閾值，等級對應範圍[],百分比對應範圍[0~1]
    * @param  [in]  config 0-不更新設定文件，1-更新設定文件
    * @return  錯誤碼
    */
    int SetAnticollision(int mode, double[] level, int config); 

設定碰撞後策略
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定碰撞後策略
    * @param  [in] strategy  0-報錯停止，1-繼續運行
    * @param  [in] safeTime  安全停止時間[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距離[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全係數[1-10]
    * @return  錯誤碼
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int[] safetyMargin); 

設定正限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定正限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitPositive(double[] limit); 

設定負限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定負限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitNegative(double[] limit); 

錯誤狀態清除
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  錯誤狀態清除
    * @return  錯誤碼
    */
    int ResetAllError(); 

關節摩擦力補償開關
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 關節摩擦力補償開關 
    * @param [in] state 0-關，1-開 
    * @return 錯誤碼 
    */ 
    int FrictionCompensationOnOff(byte state); 

設定關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-正裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_level(double[] coeff);

設定關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-側裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_wall(double[] coeff); 

設定關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-倒裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_ceiling(double[] coeff);

設定關節摩擦力補償係數-自由安裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-自由安裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_freedom(double[] coeff);

代碼範例
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
