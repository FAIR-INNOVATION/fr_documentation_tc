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

斷線重連
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 斷線重連
    * @param [in] enable 是否開啟 true-使能，false-不使能
    * @param [in] times 重連次數
    * @param [in] period 重連時間間隔（毫秒）
    */
    void SetReconnectParam(bool enable, int times, int period);

獲取機器人軟固件版本代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnStandard_Click(object sender, EventArgs e)
    {
            Robot robot = new Robot();
            robot.SetReconnectParam(true, 100, 1000);
            robot.RPC("192.168.58.2");

            string[] ver = new string[20];
            int rtn = 0;
            rtn = robot.GetSoftwareVersion(ref ver[0], ref ver[1], ref ver[2]);
            rtn = robot.GetHardwareVersion(ref ver[3], ref ver[4], ref ver[5], ref ver[6], ref ver[7], ref ver[8], ref ver[9], ref ver[10]);
            rtn = robot.GetFirmwareVersion(ref ver[11], ref ver[12], ref ver[13], ref ver[14], ref ver[15], ref ver[16], ref ver[17], ref ver[18]);
            Console.WriteLine($"robotmodel  is: {ver[0]}");
            Console.WriteLine($"webVersion  is: {ver[1]}");
            Console.WriteLine($"controllerVersion  is: {ver[2]}");
            Console.WriteLine($"Hard ctrlBox Version  is: {ver[3]}");
            Console.WriteLine($"Hard driver1 Version  is: {ver[4]}");
            Console.WriteLine($"Hard driver2 Version  is: {ver[5]}");
            Console.WriteLine($"Hard driver3 Version  is: {ver[6]}");
            Console.WriteLine($"Hard driver4 Version  is: {ver[7]}");
            Console.WriteLine($"Hard driver5 Version  is: {ver[8]}");
            Console.WriteLine($"Hard driver6 Version  is: {ver[9]}");
            Console.WriteLine($"Hard end Version  is: {ver[10]}");
            Console.WriteLine($"Firm ctrlBox Version  is: {ver[11]}");
            Console.WriteLine($"Firm driver1 Version  is: {ver[12]}");
            Console.WriteLine($"Firm driver2 Version  is: {ver[13]}");
            Console.WriteLine($"Firm driver3 Version  is: {ver[14]}");
            Console.WriteLine($"Firm driver4 Version  is: {ver[15]}");
            Console.WriteLine($"Firm driver5 Version  is: {ver[16]}");
            Console.WriteLine($"Firm driver6 Version  is: {ver[17]}");
            Console.WriteLine($"Firm end Version  is: {ver[18]}");
     }
