机器人IO
============

.. toctree:: 
    :maxdepth: 5

设置控制箱数字量输出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置控制箱数字量输出
    * @param  [in] id  io编号，范围[0~15]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetDO(int id, int status, int smooth, int block); 

设置工具数字量输出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工具数字量输出
    * @param  [in] id  io编号，范围[0~1]
    * @param  [in] status 0-关，1-开
    * @param  [in] smooth 0-不平滑， 1-平滑
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolDO(int id, int status, int smooth, int block); 

设置控制箱模拟量输出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置控制箱模拟量输出
    * @param  [in] id  id  io编号，范围[0~1]
    * @param  [in] id  value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] id  block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetAO(int id, double value, int block); 

设置工具模拟量输出
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  设置工具模拟量输出
    * @param  [in] id  io编号，范围[0]
    * @param  [in] value 电流或电压值百分比，范围[0~100]对应电流值[0~20mA]或电压[0~10V]
    * @param  [in] block  0-阻塞，1-非阻塞
    * @return  错误码
    */
    int SetToolAO(int id, double value, int block); 

等待控制箱数字量输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱数字量输入
    * @param  [in]  id  io编号，范围[0~15]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitDI(int id, int status, int max_time, int opt); 

等待控制箱多路数字量输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱多路数字量输入
    * @param  [in] mode 0-多路与，1-多路或
    * @param  [in] id  io编号，bit0~bit7对应DI0~DI7，bit8~bit15对应CI0~CI7
    * @param  [in] status 0-关，1-开
    * @param  [in] max_time  最大等待时间，单位ms
    * @param  [in] opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitMultiDI(int mode, int id, int status, int max_time, int opt); 

等待工具数字量输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具数字量输入
    * @param  [in]  id  io编号，范围[0~1]
    * @param  [in]  status 0-关，1-开
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolDI(int id, int status, int max_time, int opt); 

等待控制箱模拟量输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待控制箱模拟量输入
    * @param  [in]  id  io编号，范围[0~1]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitAI(int id, int sign, double value, int max_time, int opt);   

等待工具模拟量输入
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 等待工具模拟量输入
    * @param  [in]  id  io编号，范围[0]
    * @param  [in]  sign 0-大于，1-小于
    * @param  [in]  value 输入电流或电压值百分比，范围[0~100]对应电流值[0~20mS]或电压[0~10V]
    * @param  [in]  max_time  最大等待时间，单位ms
    * @param  [in]  opt  超时后策略，0-程序停止并提示超时，1-忽略超时提示程序继续执行，2-一直等待
    * @return  错误码
    */
    int WaitToolAI(int id, int sign, double value, int max_time, int opt); 

代码示例
+++++++++++++++++++++++++++++++++++++++++
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
        robot.SetDO(8, 1, 0, 0);
        robot.Sleep(3000);
        robot.SetDO(8, 0, 0, 0);

        robot.SetToolDO(0, 1, 0, 0);
        robot.Sleep(3000);
        robot.SetToolDO(0, 0, 0, 0);

        for(int i = 0; i < 90; i++)
        {
            robot.SetAO(0, i+1, 0);
            robot.SetAO(1, i+1, 0);
            robot.Sleep(50);
        }
        robot.SetAO(0, 0.0, 0);
        robot.SetAO(1, 0.0, 0);

        for(int i = 0; i < 99; i++)
        {
            robot.SetToolAO(0, i+1, 0);
            robot.Sleep(50);
        }
        robot.SetToolAO(0, 0.0, 0);

        System.out.println("wait  start ");
        robot.WaitDI(1, 1, 10000, 0);//WaitDI
        robot.WaitMultiDI(0, 6, 6, 10000, 0);//WaitMultiDI
        robot.WaitToolDI(0, 1, 5000, 0);//WaitToolDI
        robot.WaitAI(0, 0, 8.0, 5000, 0);//WaitAI
        robot.WaitToolAI(0, 0, 20, 5000, 0);//WaitToolAI
        System.out.println("wait  end ");
    }

设置控制箱DO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置控制箱DO停止/暂停后输出是否复位 
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetCtlBoxDO(int resetFlag);

设置控制箱AO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置控制箱AO停止/暂停后输出是否复位 
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetCtlBoxAO(int resetFlag);

设置末端工具DO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置末端工具DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetAxleDO(int resetFlag);

设置末端工具AO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置末端工具AO停止/暂停后输出是否复位 
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetAxleAO(int resetFlag);
    
设置扩展DO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置扩展DO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetExtDO(int resetFlag);
    
设置扩展AO停止/暂停后输出是否复位
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置扩展AO停止/暂停后输出是否复位
    * @param [in] resetFlag  0-不复位；1-复位
    * @return 错误码 
    */ 
    int SetOutputResetExtAO(int resetFlag);

代码示例
+++++++++++++++++++++++++++++++++++++++++
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
        robot.SetOutputResetCtlBoxDO(1);
        robot.SetOutputResetAxleDO(1);//工具
        robot.SetOutputResetCtlBoxAO(1);
        robot.SetOutputResetAxleAO(1);//工具
    }