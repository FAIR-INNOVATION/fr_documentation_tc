機器人安全設定
=================

.. toctree:: 
    :maxdepth: 5

設定碰撞等級
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定碰撞等級
    * @param  [in]  mode  0-等級，1-百分比
    * @param  [in]  level 碰撞阈值，等级对应範圍[1 - 10对应等级1-10， 100-關閉],百分比对应範圍[0~10 对应 0% - 100%]
    * @param  [in]  config 0-不更新設定文件，1-更新設定文件
    * @return  錯誤碼
    */
    int SetAnticollision(int mode, Object[] level, int config); 

設定碰撞後策略
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定碰撞後策略
    * @param  [in] strategy  0-報錯停止，1-繼續運行
    * @param  [in] safeTime  安全停止時間[1000 - 2000]ms
    * @param  [in] safeDistance  安全停止距離[1-150]mm
    * @param  [in] safetyMargin  j1-j6安全係數[1-10]
    * @return  錯誤碼  
    */
    int SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]); 

設定正限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定正限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitPositive(Object[] limit); 

設定負限位
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定負限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int SetLimitNegative(Object[] limit); 

錯誤狀態清除
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  錯誤狀態清除
    * @return  錯誤碼
    */
    int ResetAllError(); 

代碼範例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
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

自訂碰撞檢測閾值功能開始
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自訂碰撞檢測閾值功能開始，設定關節端和TCP端的碰撞檢測閾值
    * @param  [in] flag 1-僅關節檢測開啟；2-僅TCP檢測開啟；3-關節和TCP檢測同時開啟
    * @param  [in] jointDetectionThreshould 關節碰撞檢測閾值 j1-j6
    * @param  [in] tcpDetectionThreshould  TCP碰撞檢測閾值，xyzabc
    * @param  [in] block 0-非阻塞；1-阻塞
    * @return  錯誤碼
    */   
    public int CustomCollisionDetectionStart(int flag, double[] jointDetectionThreshould, double[] tcpDetectionThreshould, int block);

自訂碰撞檢測閾值功能關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.3-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief  自訂碰撞檢測閾值功能關閉
    * @return  錯誤碼
    */   
    public int CustomCollisionDetectionEnd();

程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        int[] safety = { 5,5,5,5,5,5 };
        robot.SetCollisionStrategy(3, 1000, 150, 250, safety);
        double[] jointDetectionThreshould= { 0.3, 0.3, 0.3, 0.3, 0.3, 0.3};
        double[] tcpDetectionThreshould = { 60,60,60,60,60,60 };
        int rtn = robot.CustomCollisionDetectionStart(1, jointDetectionThreshould, tcpDetectionThreshould, 1);

        DescPose p1Desc=new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint=new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc=new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint=new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos=new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese=new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        for(int i=0;i<10;++i) {
            robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);
            robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);
        }
        rtn = robot.CustomCollisionDetectionEnd();
    }

關節摩擦力補償開關
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 關節摩擦力補償開關 
    * @param [in] state  0-關，1-開
    * @return 錯誤碼 
    */ 
    int FrictionCompensationOnOff(int state); 

設定關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-正裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_level(Object[] coeff);

設定關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-側裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_wall(Object[] coeff); 

設定關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-倒裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_ceiling(Object[] coeff);

設定關節摩擦力補償係數-自由安裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-自由安裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_freedom(Object[] coeff);

代碼範例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        Object[] lcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] wcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] ccoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };
        Object[] fcoeff = { 0.5, 0.5, 0.5, 0.5, 0.5, 0.5 };

        robot.FrictionCompensationOnOff(1);

        robot.SetFrictionValue_level(lcoeff);//正裝

        robot.SetFrictionValue_wall(wcoeff);//側裝

        robot.SetFrictionValue_ceiling(ccoeff);//倒裝

        robot.SetFrictionValue_freedom(fcoeff);//自由安裝
    }

開始奇異位姿保護
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  開始奇異位姿保護
    * @param  [in]  protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
    * @param  [in]  minShoulderPos 肩奇異調整範圍(mm), 默認100
    * @param  [in]  minElbowPos 肘奇異調整範圍(mm), 默認50
    * @param  [in]  minWristPos 腕奇異調整範圍(°), 預設10
    * @return  錯誤碼
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇異位姿保護
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  停止奇異位姿保護
    * @return  錯誤碼
    */
    int SingularAvoidEnd();

代碼範例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
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
