機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  機器人介面類別建構函數
    */
    Robot(); 

與控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  與機器人控制器建立通信
    * @param  [in] ip  控制器IP地址，出場預設為192.168.58.2
    * @return 錯誤碼
    */
    int RPC(string ip);

與機器人斷開通信
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 與機器人控制器斷開通信 
    * @return 錯誤碼 
    */ 
    int CloseRPC(); 

查詢SDK版本號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 查詢 SDK 版本號 
    * @param [out] version SDK 版本號 
    * @return 錯誤碼 
    */  
    int GetSDKVersion(ref string version);

獲取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取控制器IP
    * @param  [out] ip  控制器IP
    * @return  錯誤碼
    */
    int GetControllerIP(ref string ip);

控制機器人進入或退出拖曳示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制機器人進入或退出拖曳示教模式
    * @param  [in] state 0-退出拖曳示教模式，1-進入拖曳示教模式
    * @return  錯誤碼
    */
    int DragTeachSwitch(byte state);

查詢機器人是否處於拖曳模式
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查詢機器人是否處於拖曳示教模式
    * @param  [out] state 0-非拖曳示教模式，1-拖曳示教模式
    * @return  錯誤碼
    */
    int IsInDragTeach(ref byte state); 

控制機器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制機器人上使能或下使能，機器人上電後預設自動上啟用
    * @param  [in] state  0-下使能，1-上使能
    * @return  錯誤碼
    */
    int RobotEnable(byte state); 

控制機器人手自動模式切換
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制機器人手自動模式切換
    * @param [in] mode 0-自動模式，1-手動模式
    * @return 錯誤碼
    */
    int Mode(int mode);

代碼範例
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
