机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置控制箱数字量输出
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetDO(int id, byte status, byte smooth, byte block); 

设置工具数字量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具数字量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolDO(int id, byte status, byte smooth, byte block); 

设置控制箱模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置控制箱模拟量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetAO(int id, float value, byte block); 

设置工具模拟量输出
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  设置工具模拟量输出
    * @param  [in] id  io编号，范围[0]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolAO(int id, float value, byte block); 

获取控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    int GetDI(int id, byte block, ref byte level);

获取工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  0-低电平，1-高电平
    * @return  错误码
    */   
    int GetToolDI(int id, byte block, ref byte level); 

等待控制箱数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱数字量输入
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitDI(int id, byte status, int max_time, int opt); 

等待控制箱多路数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱多路数字量输入
    * @param  [in] mode 0-多路与，1-多路或
    * @param  [in] id  io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitMultiDI(int mode, int id, byte status, int max_time, int opt); 

等待工具数字量输入
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具数字量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolDI(int id, byte status, int max_time, int opt); 

获取控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    int GetAI(int id, byte block, ref float persent); 

获取工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [out] result  输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @return  错误码
    */   
    int GetToolAI(int id, byte block, ref float persent);    

获取机器人末端记录按钮状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人末端记录按钮状态
    * @param [out] state 按钮状态，0-按下，1-松开
    * @return 错误码 
    */ 
    int GetAxlePointRecordBtnState(ref byte state); 

等待控制箱模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待控制箱模拟量输入
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitAI(int id, int sign, float value, int max_time, int opt);   

等待工具模拟量输入
+++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 等待工具模拟量输入
    * @param  [in] id  io编号，范围[0]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolAI(int id, int sign, float value, int max_time, int opt); 

获取机器人末端DO输出状态
++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人末端DO输出状态 
    * @param [out] do_state DO输出状态，do0~do1对应bit1~bit2,从bit0开始 
    * @return 错误码 
    */ 
    int GetToolDO(ref byte do_state);

获取机器控制器DO输出状态
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人控制器DO输出状态 
    * @param [out] do_state_h DO输出状态，co0~co7对应bit0~bit7 
    * @param [out] do_state_l DO输出状态，do0~do7对应bit0~bit7
    * @return 错误码 
    */ 
    int GetDO(ref int do_state_h, ref int do_state_l);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnIOTest_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte status = 1;
        byte smooth = 0;
        byte block = 0;
        byte di = 0, tool_di = 0;
        float ai = 0.0f, tool_ai = 0.0f;
        float value = 0.0f;
        int i;

        for (i = 0; i < 16; i++)//所有控制器IO输出置 1
        {
            robot.SetDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        status = 0;

        for (i = 0; i < 16; i++)//所有控制器IO输出置 0
        {
            robot.SetDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        status = 1;

        for (i = 0; i < 2; i++)//所有工具端IO输出置 1
        {
            robot.SetToolDO(i, status, smooth, block);
            robot.WaitMs(500);
        }
        status = 0;
        for (i = 0; i < 2; i++)//所有工具端IO输出置 0
        {
            robot.SetToolDO(i, status, smooth, block);
            robot.WaitMs(500);
        }

        value = 50.0f;
        robot.SetAO(0, value, block);//设置控制器0号模拟量输出50%
        value = 100.0f;
        robot.SetAO(1, value, block);//设置控制器1号模拟量输出100%
        robot.WaitMs(300);
        value = 0.0f;
        robot.SetAO(0, value, block);//设置控制器0号模拟量输出0%
        value = 0.0f;
        robot.SetAO(1, value, block);//设置控制器1号模拟量输出0%

        value = 100.0f;
        robot.SetToolAO(0, value, block);//设置工具端0号模拟量输出100%
        robot.WaitMs(1000);
        value = 0.0f;
        robot.SetToolAO(0, value, block);//设置工具端0号模拟量输出0%

        robot.GetDI(0, block, ref di);//获取数字输入
        Console.WriteLine($"di0 : {di}");
        robot.WaitDI(0, 1, 0, 2);       //等待0号端口数字量输入1，一直等待
        Console.WriteLine("wait di success");
        robot.WaitMultiDI(0, 3, 0, 10000, 2);   //等待多路与， 0和1端口，输入置1，等待时间10000ms， 一直等待
        Console.WriteLine("wait multi di success");
        robot.GetToolDI(1, block, ref tool_di);//获取工具端数字量输入
        Console.WriteLine($"tool_di1 : {tool_di}");
        robot.WaitToolDI(1, 0, 0, 2);          //一直等待
        Console.WriteLine("wait tool di success");
        robot.GetAI(0, block, ref ai);
        Console.WriteLine($"ai0 : {ai}");
        robot.GetAI(1, block, ref ai);
        Console.WriteLine($"ai1 : {ai}");
        robot.WaitAI(0, 1, 50.0f, 0, 2);    //等待0号口， 小于 ， %50， 一直等待
        Console.WriteLine("wait ai success");
        robot.WaitToolAI(0, 1, 50, 0, 2);   //一直等待
        Console.WriteLine("wait tool ai success");
        robot.GetToolAI(0, block, ref tool_ai);
        Console.WriteLine($"tool_ai0 : {tool_ai}");
    }
    
获取机器人软件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人软件版本信息
    * @param [out] robotModel 机器人型号
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 错误码 
    */ 
    int GetSoftwareVersion(ref string robotModel, ref string webVersion, ref string controllerVersion);
    
获取机器人硬件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人硬件版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱载板硬件版本
    * @param [out] driver1Version 驱动器1硬件版本
    * @param [out] driver1Version 驱动器2硬件版本
    * @param [out] driver1Version 驱动器3硬件版本
    * @param [out] driver1Version 驱动器4硬件版本
    * @param [out] driver1Version 驱动器5硬件版本
    * @param [out] driver1Version 驱动器6硬件版本
    * @param [out] endBoardVersion 末端板硬件版本
    * @return 错误码 
    */ 
    int GetHardwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

获取机器人固件版本
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 获取机器人固件版本信息
    * @param [out] ctrlBoxBoardVersion 控制箱载板固件版本
    * @param [out] driver1Version 驱动器1固件版本
    * @param [out] driver1Version 驱动器2固件版本
    * @param [out] driver1Version 驱动器3固件版本
    * @param [out] driver1Version 驱动器4固件版本
    * @param [out] driver1Version 驱动器5固件版本
    * @param [out] driver1Version 驱动器6固件版本
    * @param [out] endBoardVersion 末端板固件版本
    * @return 错误码 
    */ 
    int GetFirmwareVersion(ref string ctrlBoxBoardVersion, ref string driver1Version, ref string driver2Version, ref string driver3Version,ref string driver4Version, ref string driver5Version, ref string driver6Version, ref string endBoardVersion);

代码示例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnGetVersions_Click(object sender, EventArgs e)
    {
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