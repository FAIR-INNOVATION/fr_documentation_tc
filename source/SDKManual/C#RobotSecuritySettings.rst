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
    * @param  [in] safeVel  TCP安全停止速度 [50-250]mm/s
    * @param  [in] safetyMargin  j1-j6安全係數[1-10]
    * @return  錯誤碼
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel,int[] safetyMargin);

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
        int[] safetyMargin = { 1, 1, 1, 1, 1, 1 };
        robot.SetCollisionStrategy(5, 1000, 150,150,safetyMargin);

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

自定義碰撞檢測閾值功能開始
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  自定義碰撞檢測閾值功能開始，設置關節端和TCP端的碰撞檢測閾值
    * @param  [in] flag 1-僅關節檢測開啓；2-僅TCP檢測開啓；3-關節和TCP檢測同時開啓
    * @param  [in] jointDetectionThreshould 關節碰撞檢測閾值 j1-j6
    * @param  [in] tcpDetectionThreshould TCP碰撞檢測閾值，xyzabc
    * @param  [in] block 0-非阻塞；1-阻塞
    * @return  錯誤碼
    */
    int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

自定義碰撞檢測閾值功能關閉
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  自定義碰撞檢測閾值功能關閉
    * @return  錯誤碼
    */
    int CustomCollisionDetectionEnd()

代碼示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        while (true)
        {
            int[] safety = { 5, 5, 5, 5, 5, 5 };
            robot.SetCollisionStrategy(3, 1000, 150, 250, safety);

            double[] jointDetectionThreshold = { 0.3, 0.3, 0.3, 0.3, 0.3, 0.3 };
            double[] tcpDetectionThreshold = { 80, 80, 80, 80, 80, 80 };
            int rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshold, tcpDetectionThreshold, 0);
            Console.WriteLine($"CustomCollisionDetectionStart 返回值為 {rtn}");

            DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
            JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

            DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
            JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

            ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
            DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

            // 假設MoveL方法簽名如下：
            robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
            robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

            rtn = robot.CustomCollisionDetectionEnd();
            Console.WriteLine($"CustomCollisionDetectionEnd 返回值為 {rtn}");
        }
    }