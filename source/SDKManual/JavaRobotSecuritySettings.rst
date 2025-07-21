機器人安全設置
=================

.. toctree:: 
    :maxdepth: 5

設置碰撞等級
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置碰撞等級
    * @param  [in]  mode  0-等級，1-百分比
    * @param  [in]  level 碰撞閾值，等級對應範圍[1 - 10對應等級1-10， 100-關閉],百分比對應範圍[0~10 對應 0% - 100%]
    * @param  [in]  config 0-不更新配置文件，1-更新配置文件
    * @return  錯誤碼
    */
    int SetAnticollision(int mode, Object[] level, int config); 

設置碰撞後策略
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置碰撞後策略
    * @param  [in] strategy  0-報錯停止，1-繼續運行
    * @param  [in] safeTime  安全停止時間[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距離[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全係數[1-10]
    * @return  錯誤碼  
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]); 

自定義碰撞檢測閾值功能開始
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自定義碰撞檢測閾值功能開始，設置關節端和TCP端的碰撞檢測閾值
    * @param  [in] flag 1-僅關節檢測開啓；2-僅TCP檢測開啓；3-關節和TCP檢測同時開啓
    * @param  [in] jointDetectionThreshould 關節碰撞檢測閾值 j1-j6
    * @param  [in] tcpDetectionThreshould  TCP碰撞檢測閾值，xyzabc
    * @param  [in] block 0-非阻塞；1-阻塞
    * @return  錯誤碼
    */   
    public int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

自定義碰撞檢測閾值功能關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自定義碰撞檢測閾值功能關閉
    * @return  錯誤碼
    */   
    public int CustomCollisionDetectionEnd();

機器人碰撞等級設置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollision(Robot robot)
    {
        int mode = 0;
        int config = 1;
        Object[] level1 = new Object[]{ 1.0,2.0,3.0,4.0,5.0,6.0 };
        Object[] level2 = new Object[]{ 50.0,20.0,30.0,40.0,50.0,60.0 };

        int rtn = robot.SetAnticollision(mode, level1, config);
        System.out.println("SetAnticollision mode 0 rtn is: "+ rtn);
        mode = 1;
        rtn = robot.SetAnticollision(mode, level2, config);
        System.out.println("SetAnticollision mode 1 rtn is :"+ rtn);

        JointPos p1Joint=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos p2Joint=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese=new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, 2,0, exaxisPos, 0, 0, offdese,0,10);
        robot.ResetAllError();
        int[] safety = new int[]{ 5,5,5,5,5,5 };
        rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        System.out.println("SetCollisionStrategy rtn is:"+ rtn);

        double[] jointDetectionThreshould = new double[]{ 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 };
        double[] tcpDetectionThreshould =new double[] { 60,60,60,60,60,60 };
        rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        System.out.println("CustomCollisionDetectionStart rtn is :"+ rtn);

        robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        rtn = robot.CustomCollisionDetectionEnd();
        System.out.println("CustomCollisionDetectionEnd rtn is: "+ rtn);
        return 0;
    }

設置正限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置正限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitPositive(Object[] limit); 

設置負限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置負限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitNegative(Object[] limit); 

獲取關節軟限位角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取關節軟限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] negative  負限位角度，單位deg
    * @param  [out] positive  正限位角度，單位deg
    * @return  錯誤碼
    */
    int GetJointSoftLimitDeg(int flag, Object[] negative, Object[] positive); 

機器人限位設置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLimit(Robot robot)
    {
        Object[] plimit =new Object[] { 170.0,80.0,150.0,80.0,170.0,160.0 };
        robot.SetLimitPositive(plimit);
        Object[] nlimit =new Object[] { -170.0,-260.0,-150.0,-260.0,-170.0,-160.0 };
        robot.SetLimitNegative(nlimit);

        Object[] neg_deg =new Object[] {0, 0 , 0, 0, 0, 0}, pos_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        robot.GetJointSoftLimitDeg(1,  neg_deg,  pos_deg);
        System.out.println("neg limit deg:"+ neg_deg[0]+","+ neg_deg[1]+","+ neg_deg[2]+","+ neg_deg[3]+","+ neg_deg[4]+","+ neg_deg[5]);
        System.out.println("pos limit deg:"+pos_deg[0]+","+ pos_deg[1]+","+ pos_deg[2]+","+ pos_deg[3]+","+ pos_deg[4]+","+pos_deg[5]);
        return 0;
    }

設置機器人碰撞檢測方法
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置機器人碰撞檢測方法
    * @param [in] method 碰撞檢測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啓
    * @param [in] thresholdMode 碰撞等級閾值方式；0-碰撞等級固定閾值方式；1-自定義碰撞檢測閾值
    * @return 錯誤碼
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode)

設置靜態下碰撞檢測開始關閉
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置靜態下碰撞檢測開始關閉
    * @param  [in] status 0-關閉；1-開啓
    * @return  錯誤碼
    */
    public int SetStaticCollisionOnOff(int status)

設置機器人碰撞檢測方法代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCollisionMethod(Robot robot)
    {
        int rtn = robot.SetCollisionDetectionMethod(0);

        rtn = robot.SetStaticCollisionOnOff(1);
        System.out.println("SetStaticCollisionOnOff On rtn is:"+ rtn);
        robot.Sleep(5000);
        rtn = robot.SetStaticCollisionOnOff(0);
        System.out.println("SetStaticCollisionOnOff Off rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

關節扭矩功率檢測
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關節扭矩功率檢測
    * @param  [in] status 0-關閉；1-開啓
    * @param  [in] power 設定最大功率(W)
    * @return  錯誤碼
    */
    public int SetPowerLimit(int status, double power)

關節扭矩功率檢測代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPowerLimit(Robot robot)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        List<Number> joint_toq=new ArrayList<>();
        joint_toq=robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); //   #servoJT開始
        int error = 0;
        while (count > 0)
        {
            count = count - 1;
            robot.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);

        robot.CloseRPC();
        return 0;
    }