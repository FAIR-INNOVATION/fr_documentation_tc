機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  機器人介面類別建構函數
    */
    Robot robot = new Robot(); 

與控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  與機器人控制器建立通信
    * @param  [in] ip  控制器IP位址，出場預設為192.168.58.2
    * @return 錯誤碼
    */
    int RPC(String ip);

與機器人斷開通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 與機器人控制器斷開通信 
    * @return 錯誤碼 
    */ 
    int CloseRPC(); 

查詢SDK版本號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 查詢 SDK 版本號 
    * @return 版本號 
    */  
    String GetSDKVersion();

獲取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取控制器IP
    * @param  [out] ip  控制器IP
    * @return  錯誤碼
    */
    int GetControllerIP(String[] ip);

控制機器人進入或退出拖曳示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制機器人進入或退出拖曳示教模式
    * @param  [in] state 0-退出拖曳示教模式，1-進入拖曳示教模式
    * @return  錯誤碼
    */
    int DragTeachSwitch(int state);

控制機器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制機器人上使能或下使能，機器人上電後預設自動上啟用
    * @param  [in] state  0-下使能，1-上使能
    * @return  錯誤碼
    */
    int RobotEnable(int state); 

控制機器人手自動模式切換
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制機器人手自動模式切換
    * @param [in] mode 0-自動模式，1-手動模式
    * @return 錯誤碼
    */
    int Mode(int mode);

代碼範例
++++++++++++++++++++++++++++++++++
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
        String[] ip={""};
        String version = "";
        version=robot.GetSDKVersion();
        System.out.println("SDK version : " + version);
        int rtn = robot.GetControllerIP(ip);
        System.out.println("controller ip : " +  ip[0] + "  " + rtn);
        robot.Mode(1);//1-手動模式 0-自動模式
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);//進入拖曳模式
        robot.Sleep(1000);
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        robot.Sleep(1000);
        robot.DragTeachSwitch(0);//退出拖曳模式
        robot.Sleep(1000);
        pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        
        if (pkg.robot_state ==4){
           System.out.println("拖曳模式");
        }else {
           System.out.println("非拖曳模式");
        }
    }