机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  机器人接口类构造函数
    */
    Robot robot = new Robot(); 

与控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  与机器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出场默认为192.168.58.2
    * @return 错误码
    */
    int RPC(String ip);

与机器人断开通信
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 与机器人控制器断开通信 
    * @return 错误码 
    */ 
    int CloseRPC(); 

查询SDK版本号
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 查询 SDK 版本号 
    * @return 版本号 
    */  
    String GetSDKVersion();

获取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  获取控制器IP
    * @param  [out] ip  控制器IP
    * @return  错误码
    */
    int GetControllerIP(String[] ip);

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制机器人进入或退出拖动示教模式
    * @param  [in] state 0-退出拖动示教模式，1-进入拖动示教模式
    * @return  错误码
    */
    int DragTeachSwitch(int state);

控制机器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  控制机器人上使能或下使能，机器人上电后默认自动上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  错误码
    */
    int RobotEnable(int state); 

控制机器人手自动模式切换
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制机器人手自动模式切换
    * @param [in] mode 0-自动模式，1-手动模式
    * @return 错误码
    */
    int Mode(int mode);

代码示例
++++++++++++++++++++++++++++++++++
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
        String[] ip={""};
        String version = "";
        version=robot.GetSDKVersion();
        System.out.println("SDK version : " + version);
        int rtn = robot.GetControllerIP(ip);
        System.out.println("controller ip : " +  ip[0] + "  " + rtn);
        robot.Mode(1);//1-手动模式  0-自动模式
        robot.Sleep(1000);
        robot.DragTeachSwitch(1);//进入拖动模式
        robot.Sleep(1000);
        ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        robot.Sleep(1000);
        robot.DragTeachSwitch(0);//退出拖动模式
        robot.Sleep(1000);
        pkg = robot.GetRobotRealTimeState();
        System.out.println("drag state : " + pkg.robot_state);
        
        if (pkg.robot_state ==4){
           System.out.println("拖动模式");
        }else {
           System.out.println("非拖动模式");
        }
    }