機器人安全設置
=================

.. toctree:: 
    :maxdepth: 5

設置碰撞等級
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置碰撞等級
    * @param  [in]  mode  0-等級，1-百分比
    * @param  [in]  level 碰撞閾值，等級對應範圍[],百分比對應範圍[0~1]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  錯誤碼
    */
    int SetAnticollision(int mode, double[] level, int config); 

設置碰撞後策略
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置碰撞後策略
    * @param  [in] strategy  0-報錯暫停；1-繼續運行;2-報錯停止；3-重力矩模式；4-震盪相應模式；5-碰撞回彈模式
    * @param  [in] safeTime  安全停止時間[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距離[1-150]mm
    * @param  [in] safeVel  tcp安全停止速度 [50-250]mm/s
    * @param  [in] safetyMargin  j1-j6安全係數[1-10]
    * @return  錯誤碼
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safeVel,int[] safetyMargin);

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

機器人碰撞等級設置代碼示例
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button24_Click(object sender, EventArgs e)
    {
        int mode = 0;
        int config = 1;
        double[] level1 = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f };
        double[] level2 = { 50.0f, 20.0f, 30.0f, 40.0f, 50.0f, 60.0f };

        int rtn = robot.SetAnticollision(mode, level1, config);
        Console.WriteLine($"SetAnticollision mode 0 rtn is {rtn}");
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        Console.WriteLine($"SetAnticollision mode 1 rtn is {rtn}");

        JointPos p1Joint = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos p2Joint = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0.0f, 0.0f, 0.0f, 0.0f);
        DescPose offdese = new DescPose(0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, 2,  exaxisPos, 0, 0,  offdese);
        robot.ResetAllError();
        int[] safety = { 5, 5, 5, 5, 5, 5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        Console.WriteLine($"SetCollisionStrategy rtn is {rtn}");

        double[] jointDetectionThreshould = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould = { 60, 60, 60, 60, 60, 60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        Console.WriteLine($"CustomCollisionDetectionStart rtn is {rtn}");

        robot.MoveL( p1Joint,  p1Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        robot.MoveL( p2Joint,  p2Desc, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        rtn = robot.CustomCollisionDetectionEnd();
        Console.WriteLine($"CustomCollisionDetectionEnd rtn is {rtn}");
    }

設置正限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置正限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitPositive(double[] limit); 

設置負限位
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置負限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitNegative(double[] limit); 

獲取關節軟限位角度
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取關節軟限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞	 
    * @param  [out] negative  負限位角度，單位deg
    * @param  [out] positive  正限位角度，單位deg
    * @return  錯誤碼
    */
    int GetJointSoftLimitDeg(byte flag, ref double[] negative, ref double[] positive);

機器人限位設置代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] plimit = { 170.0f, 80.0f, 150.0f, 80.0f, 170.0f, 160.0f };
        robot.SetLimitPositive(plimit);
        double[] nlimit = { -170.0f, -260.0f, -150.0f, -260.0f, -170.0f, -160.0f };
        robot.SetLimitNegative(nlimit);

        double[] neg_deg = new double[6] {0,0,0,0,0,0 };
        double[] pos_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        robot.GetJointSoftLimitDeg(0, ref neg_deg,ref pos_deg);
        Console.WriteLine($"neg limit deg:{neg_deg[0]},{neg_deg[1]},{neg_deg[2]},{neg_deg[3]},{neg_deg[4]},{neg_deg[5]}");
        Console.WriteLine($"pos limit deg:{pos_deg[0]},{pos_deg[1]},{pos_deg[2]},{pos_deg[3]},{pos_deg[4]},{pos_deg[5]}");
    }

設置機器人碰撞檢測方法
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人碰撞檢測方法
    * @param  [in] method 碰撞檢測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啓
    * @param [in] thresholdMode 碰撞等級閾值方式；0-碰撞等級固定閾值方式；1-自定義碰撞檢測閾值
    * @return  錯誤碼
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode=0);


設置靜態下碰撞檢測開始關閉
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置靜態下碰撞檢測開始關閉
    * @param  [in] status 0-關閉；1-開啓
    * @return  錯誤碼
    */
    int SetStaticCollisionOnOff(int status);

設置機器人碰撞檢測方法代碼示例
++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        int rtn = robot.SetCollisionDetectionMethod(0, 0);

        rtn = robot.SetStaticCollisionOnOff(1);
        Console.WriteLine($"SetStaticCollisionOnOff On rtn is {rtn}");
        Thread.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        Console.WriteLine($"SetStaticCollisionOnOff Off rtn is {rtn}");
    }

關節扭矩功率檢測
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩功率檢測
    * @param  [in] status 0-關閉；1-開啓
    * @param  [in] power 設定最大功率(W)
    * @return  錯誤碼
    */
    int SetPowerLimit(int status, double power);

關節扭矩功率檢測代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button26_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }
