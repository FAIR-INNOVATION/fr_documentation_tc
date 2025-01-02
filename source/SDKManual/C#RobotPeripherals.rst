机器人外设
============

.. toctree:: 
    :maxdepth: 5

配置夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置夹爪
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int SetGripperConfig(int company, int device, int softvesion, int bus);

获取夹爪配置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪配置
    * @param  [in] company  夹爪厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    int GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  激活夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    int ActGripper(int index, byte act); 

控制夹爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制夹爪
    * @param  [in] index  夹爪编号
    * @param  [in] pos  位置百分比，范围[0~100]
    * @param  [in] vel  速度百分比，范围[0~100]
    * @param  [in] force  力矩百分比，范围[0~100]
    * @param  [in] max_time  最大等待时间，范围[0~30000]，单位ms
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [in] type 夹爪类型，0-平行夹爪；1-旋转夹爪
    * @param  [in] rotNum 旋转圈数
    * @param  [in] rotVel 旋转速度百分比[0-100]
    * @param  [in] rotTorque 旋转力矩百分比[0-100]
    * @return  错误码
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, byte block, int type, double rotNum, int rotVel, int rotTorque);

获取夹爪运动状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪运动状态
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] staus  0-运动未完成，1-运动完成
    * @return  错误码
    */
    int GetGripperMotionDone(ref int fault, ref int status); 

获取夹爪激活状态
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪激活状态
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] status  bit0~bit15对应夹爪编号0~15，bit=0为未激活，bit=1为激活
    * @return  错误码
    */
    int GetGripperActivateStatus(ref int fault, ref int status);

获取夹爪位置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪位置
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] position  位置百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurPosition(ref int fault, ref int position);

获取夹爪速度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪速度
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] speed  速度百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurSpeed(ref int fault, ref int speed);
     
获取夹爪电流
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪电流
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] current  电流百分比，范围0~100%
    * @return  错误码
    */
    int GetGripperCurCurrent(ref int fault, ref int current);

获取夹爪电压
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪电压
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] voltage  电压,单位0.1V
    * @return  错误码
    */
    int GetGripperVoltage(ref int fault, ref int voltage);

获取夹爪温度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  获取夹爪温度
    * @param  [out] fault  0-无错误，1-有错误
    * @param  [out] temp  温度，单位℃
    * @return  错误码
    */
    int GetGripperTemp(ref int fault, ref int temp);

代码示例
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnOperateGripper_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status = 0, fault = 0;
        int rtn = -1;

        robot.SetGripperConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.GetGripperConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"gripper config : {company}, {device}, {softversion}, {bus}");

        rtn = robot.ActGripper(index, act);
        Console.WriteLine($"ActGripper  {rtn}");
        Thread.Sleep(1000);
        act = 1;
        rtn = robot.ActGripper(index, act);
        Console.WriteLine($"ActGripper  {rtn}");
        Thread.Sleep(4000);

        rtn = robot.MoveGripper(index, 20, 50, 50, max_time, block);
        Console.WriteLine($"MoveGripper  {rtn}");
        Thread.Sleep(2000);
        robot.MoveGripper(index, 10, 50, 0, max_time, block);

        Thread.Sleep(4000);
        robot.GetGripperMotionDone(ref fault, ref status);
        Console.WriteLine($"motion status : {fault}, {status}");

        int current = -1;
        int tempture = -1;
        int voltage = -1;
        int position = -1;
        int activestatus = -2;
        int speed = -1;
        rtn = robot.GetGripperCurCurrent(ref fault, ref current);
        Console.WriteLine($"current { current}  rtn { rtn} fault { fault} ");
        rtn = robot.GetGripperCurPosition(ref fault, ref position);
        Console.WriteLine($"position {position}  rtn {rtn} fault {fault} ");
        rtn = robot.GetGripperActivateStatus(ref fault, ref activestatus);
        Console.WriteLine($"activestatus {activestatus}  rtn {rtn} fault {fault} ");
        rtn = robot.GetGripperCurSpeed(ref fault, ref speed);
        Console.WriteLine($"speed {speed}  rtn {rtn} fault {fault} ");
        rtn = robot.GetGripperVoltage(ref fault, ref voltage);
        Console.WriteLine($"voltage {voltage}  rtn {rtn} fault {fault} ");
        rtn = robot.GetGripperTemp(ref fault, ref tempture);
        Console.WriteLine($"voltage {tempture}  rtn {rtn} fault {fault} ");
    }

计算预抓取点-视觉
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算预抓取点-视觉 
    * @param [in] desc_pos 抓取点笛卡尔位姿 
    * @param [in] zlength z轴偏移量 
    * @param [in] zangle 绕z轴旋转偏移量
    * @param [out] pre_pos 预抓取点
    * @return 错误码 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, ref DescPose pre_pos);

计算撤退点-视觉
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 计算撤退点-视觉 
    * @param [in] desc_pos 撤退点笛卡尔位姿 
    * @param [in] zlength z轴偏移量 
    * @param [in] zangle 绕z轴旋转偏移量
    * @param [out] post_pos 撤退点
    * @return 错误码 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, ref DescPose post_pos);
