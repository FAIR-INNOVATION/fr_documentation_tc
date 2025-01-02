机器人基础
=============

.. toctree:: 
    :maxdepth: 5

实例化机器人
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  机器人接口类构造函数
    */
    Robot(); 

与控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  与机器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出场默认为192.168.58.2
    * @return 错误码
    */
    int RPC(string ip);

与机器人断开通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 与机器人控制器断开通信 
    * @return 错误码 
    */ 
    int CloseRPC(); 

查询SDK版本号
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 查询 SDK 版本号 
    * @param [out] version SDK 版本号 
    * @return 错误码 
    */  
    int GetSDKVersion(ref string version);

获取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制器IP
    * @param  [out] ip  控制器IP
    * @return  错误码
    */
    int GetControllerIP(ref string ip);

控制机器人进入或退出拖动示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制机器人进入或退出拖动示教模式
    * @param  [in] state 0-退出拖动示教模式，1-进入拖动示教模式
    * @return  错误码
    */
    int DragTeachSwitch(byte state);

查询机器人是否处于拖动模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查询机器人是否处于拖动示教模式
    * @param  [out] state 0-非拖动示教模式，1-拖动示教模式
    * @return  错误码
    */
    int IsInDragTeach(ref byte state); 

控制机器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制机器人上使能或下使能，机器人上电后默认自动上使能
    * @param  [in] state  0-下使能，1-上使能
    * @return  错误码
    */
    int RobotEnable(byte state); 

控制机器人手自动模式切换
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制机器人手自动模式切换
    * @param [in] mode 0-自动模式，1-手动模式
    * @return 错误码
    */
    int Mode(int mode);

代码示例
+++++++++++++
.. code-block:: c#
    :linenos:

    private void btnStandard_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        string ip = "";
        string version = "";
        byte state = 0;

        robot.GetSDKVersion(ref version);
        Console.WriteLine($"SDK version : {version}");
        robot.GetControllerIP(ref ip);
        Console.WriteLine($"controller ip : {ip}");

        robot.Mode(1);
        Thread.Sleep(1000);
        robot.DragTeachSwitch(1);
        int rtn = robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.DragTeachSwitch(0);
        Thread.Sleep(1000);
        robot.IsInDragTeach(ref state);
        Console.WriteLine($"drag state : {state}");
        Thread.Sleep(3000);
        robot.RobotEnable(0);
        Thread.Sleep(3000);
        robot.RobotEnable(1);

        robot.Mode(0);
        Thread.Sleep(1000);
        robot.Mode(1);
    }
