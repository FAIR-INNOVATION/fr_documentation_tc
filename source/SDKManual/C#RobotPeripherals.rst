機器人週邊
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置夾爪
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int SetGripperConfig(int company, int device, int softvesion, int bus);

取得夾爪配置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪配置
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

啟動夾爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  啟動夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    int ActGripper(int index, byte act); 

控制夾爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  控制夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] pos  位置百分比，範圍[0~100]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] force  力矩百分比，範圍[0~100]
    * @param  [in] max_time  最大等待時間，範圍[0~30000]，單位ms
    * @param  [in] block  0-阻塞，1-非阻塞
    * @param  [in] type 夾爪類型，0-平行夾爪；1-旋轉夾爪
    * @param  [in] rotNum 旋轉圈數
    * @param  [in] rotVel 旋轉速度百分比[0-100]
    * @param  [in] rotTorque 旋轉力矩百分比[0-100]
    * @return  錯誤碼
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, byte block, int type, double rotNum, int rotVel, int rotTorque);

取得夾爪運動狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪運動狀態
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] staus  0-運動未完成，1-運動完成
    * @return  錯誤碼
    */
    int GetGripperMotionDone(ref int fault, ref int status); 

取得夾爪啟動狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪啟動狀態
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] status  bit0~bit15对应夾爪編號0~15，bit=0為未激活，bit=1為激活
    * @return  錯誤碼
    */
    int GetGripperActivateStatus(ref int fault, ref int status);

取得夾爪位置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪位置
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] position  位置百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurPosition(ref int fault, ref int position);

取得夾爪速度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪速度
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] speed  速度百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurSpeed(ref int fault, ref int speed);
     
取得夾爪電流
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪電流
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] current  電流百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurCurrent(ref int fault, ref int current);

取得夾爪電壓
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪電壓
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] voltage  電壓,單位0.1V
    * @return  錯誤碼
    */
    int GetGripperVoltage(ref int fault, ref int voltage);

取得夾爪溫度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得夾爪溫度
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] temp  溫度，單位℃
    * @return  錯誤碼
    */
    int GetGripperTemp(ref int fault, ref int temp);

代碼範例
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

計算預抓取點-視覺
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算預抓取點-視覺 
    * @param [in] desc_pos 抓取點笛卡爾位姿 
    * @param [in] zlength z軸偏移量 
    * @param [in] zangle 繞z軸旋轉偏移量
    * @param [out] pre_pos 预抓取點
    * @return 錯誤碼 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, ref DescPose pre_pos);

計算撤退點-視覺
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算撤退點-視覺 
    * @param [in] desc_pos 撤退點笛卡兒位姿 
    * @param [in] zlength z軸偏移量 
    * @param [in] zangle 繞z軸旋轉偏移量
    * @param [out] post_pos 撤退點
    * @return 錯誤碼 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, ref DescPose post_pos);
