機器人外設
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
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int SetGripperConfig(int company, int device, int softvesion, int bus);

獲取夾爪配置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪配置
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

激活夾爪
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  激活夾爪
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

獲取夾爪運動狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪運動狀態
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] staus  0-運動未完成，1-運動完成
    * @return  錯誤碼
    */
    int GetGripperMotionDone(ref int fault, ref int status); 

獲取夾爪激活狀態
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪激活狀態
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] status  bit0~bit15對應夾爪編號0~15，bit=0爲未激活，bit=1爲激活
    * @return  錯誤碼
    */
    int GetGripperActivateStatus(ref int fault, ref int status);

獲取夾爪位置
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪位置
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] position  位置百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurPosition(ref int fault, ref int position);

獲取夾爪速度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪速度
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] speed  速度百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurSpeed(ref int fault, ref int speed);
     
獲取夾爪電流
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪電流
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] current  電流百分比，範圍0~100%
    * @return  錯誤碼
    */
    int GetGripperCurCurrent(ref int fault, ref int current);

獲取夾爪電壓
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪電壓
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] voltage  電壓,單位0.1V
    * @return  錯誤碼
    */
    int GetGripperVoltage(ref int fault, ref int voltage);

獲取夾爪溫度
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取夾爪溫度
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] temp  溫度，單位℃
    * @return  錯誤碼
    */
    int GetGripperTemp(ref int fault, ref int temp);

計算預抓取點-視覺
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算預抓取點-視覺 
    * @param [in] desc_pos 抓取點笛卡爾位姿 
    * @param [in] zlength z軸偏移量 
    * @param [in] zangle 繞z軸旋轉偏移量
    * @param [out] pre_pos 預抓取點
    * @return 錯誤碼 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, ref DescPose pre_pos);

計算撤退點-視覺
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算撤退點-視覺 
    * @param [in] desc_pos 撤退點笛卡爾位姿 
    * @param [in] zlength z軸偏移量 
    * @param [in] zangle 繞z軸旋轉偏移量
    * @param [out] post_pos 撤退點
    * @return 錯誤碼 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, ref DescPose post_pos);

機器人夾爪操作代碼示例
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button36_Click(object sender, EventArgs e)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status=0;
        int fault=0;
        int active_status = 0;
        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        robot.SetGripperConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.GetGripperConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine("gripper config:{0},{1},{2},{3}\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        Thread.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        Thread.Sleep(1000);

        robot.MoveGripper(index, 90, 50, 50, max_time, block, 0, 0, 0, 0);
        Thread.Sleep(1000);
        robot.MoveGripper(index, 30, 50, 0, max_time, block, 0, 0, 0, 0);

        robot.GetGripperMotionDone(ref fault, ref status);
        Console.WriteLine("motion status:{0},{1}\n", fault, status);

        robot.GetGripperActivateStatus(ref fault, ref active_status);
        Console.WriteLine("gripper active fault is: {0}, status is: {1}\n", fault, active_status);

        robot.GetGripperCurPosition(ref fault, ref current_pos);
        Console.WriteLine("fault is:{0}, current position is: {1}\n", fault, current_pos);

        robot.GetGripperCurCurrent(ref fault, ref current);
        Console.WriteLine("fault is:{0}, current current is: {1}\n", fault, current);

        robot.GetGripperVoltage(ref fault, ref voltage);
        Console.WriteLine("fault is:{0}, current voltage is: {1} \n", fault, voltage);

        robot.GetGripperTemp(ref fault, ref temp);
        Console.WriteLine("fault is:{0}, current temperature is: {1}\n", fault, temp);

        robot.GetGripperCurSpeed(ref fault, ref speed);
        Console.WriteLine("fault is:{0}, current speed is: {1}\n", fault, speed);

        int retval = 0;
        DescPose prepick_pose = new DescPose();
        DescPose postpick_pose = new DescPose();

        DescPose p1Desc = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose p2Desc = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        retval = robot.ComputePrePick(p1Desc, 10, 0, ref prepick_pose);
        Console.WriteLine("ComputePrePick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z,
            prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);

        retval = robot.ComputePostPick( p2Desc, -10, 0, ref postpick_pose);
        Console.WriteLine("ComputePostPick retval is: {0}\n", retval);
        Console.WriteLine("xyz is: {0}, {1}, {2}; rpy is: {3}, {4}, {5}\n",
            postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z,
            postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);

    }

獲取旋轉夾爪的旋轉圈數
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉圈數
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] num  旋轉圈數
    * @return  錯誤碼
    */
    int GetGripperRotNum(ref UInt16 fault, ref double num);

獲取旋轉夾爪的旋轉速度百分比
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉速度百分比
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] speed  旋轉速度百分比
    * @return  錯誤碼
    */
    int GetGripperRotSpeed(ref UInt16 fault, ref int speed);

獲取旋轉夾爪的旋轉力矩百分比
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉力矩百分比
    * @param  [out] fault  0-無錯誤，1-有錯誤
    * @param  [out] torque  旋轉力矩百分比
    * @return  錯誤碼
    */
    int GetGripperRotTorque(ref UInt16 fault, ref int torque);

獲取旋轉夾爪狀態代碼示例
++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    int MoveRotGripper(int pos, double rotPos)
    {
        robot.ResetAllError();
        robot.ActGripper(1, 1);
        Thread.Sleep(1000);
        int rtn = robot.MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
        Console.WriteLine($"move gripper rtn is {rtn}" );
        UInt16 fault = 0;
        double rotNum = 0.0;
        int rotSpeed = 0;
        int rotTorque = 0;
        robot.GetGripperRotNum(ref fault, ref rotNum);
        robot.GetGripperRotSpeed(ref fault, ref rotSpeed);
        robot.GetGripperRotTorque(ref fault, ref rotTorque);
        Console.WriteLine($"gripper rot num :{ rotNum}, gripper rotSpeed :{rotSpeed}, gripper rotTorque : { rotTorque}");
        return 0;
    }

傳動帶啓動、停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動帶啓動、停止 
    * @param [in] status 狀態，1-啓動，0-停止
    * @return 錯誤碼 
    */ 
    int ConveyorStartEnd(byte status); 

記錄IO檢測點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄IO檢測點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointIORecord(); 

記錄A點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄A點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointARecord();

記錄參考點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄參考點 
    * @return 錯誤碼 
    */ 
    int ConveyorRefPointRecord(); 

記錄B點
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 記錄B點 
    * @return 錯誤碼 
    */ 
    int ConveyorPointBRecord();

傳送帶工件IO檢測
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳送帶工件IO檢測 
    * @param [in] max_t 最大檢測時間，單位ms
    * @return 錯誤碼 
    */ 
    int ConveyorIODetect(int max_t);

獲取物體當前位置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取物體當前位置 
    * @param [in] mode 1-跟蹤抓取，2-跟蹤運動，3-TPD跟蹤
    * @return 錯誤碼 
    */ 
    int ConveyorGetTrackData(int mode);

傳動帶跟蹤開始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動帶跟蹤開始 
    * @param [in] status 狀態，1-啓動，0-停止
    * @return 錯誤碼 
    */
    int ConveyorTrackStart(byte status);

傳動帶跟蹤停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳動帶跟蹤停止 
    * @return 錯誤碼 
    */
    int ConveyorTrackEnd();

傳動帶參數配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 傳動帶參數配置
    * @param [in] para[0] 編碼器通道 1~2
    * @param [in] para[1] 編碼器轉一圈的脈衝數
    * @param [in] para[2] 編碼器轉一圈傳送帶行走距離
    * @param [in] para[3] 工件座標系編號 針對跟蹤運動功能選擇工件座標系編號，跟蹤抓取、TPD跟蹤設爲0
    * @param [in] para[4] 是否配視覺  0 不配  1 配
    * @param [in] para[5] 速度比  針對傳送帶跟蹤抓取選項（1-100）  其他選項默認爲1 
    * @param [in] followType 跟蹤運動類型，0-跟蹤運動；1-追檢運動
    * @param [in] startDis 追檢抓取需要設置， 跟蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 默認值0
    * @param [in] endDis 追檢抓取需要設置，跟蹤終止距離， 單位mm， 默認值100
    * @return 錯誤碼
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis=0, int endDis=100);

設置傳動帶抓取點補償
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置傳動帶抓取點補償 
    * @param [in] cmp 補償位置 double[3]{x, y, z}
    * @return 錯誤碼 
    */
    int ConveyorCatchPointComp(double[] cmp);

傳送帶跟蹤直線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 傳送帶跟蹤直線運動 
    * @param [in] name 運動點名稱
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] wobj 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm  
    * @return 錯誤碼 
    */
    int ConveyorTrackMoveL(string name, int tool, int wobj, float vel, float acc, float ovl, float blendR);

傳送帶通訊輸入檢測
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測
    * @param [in] timeout 等待超時時間ms
    * @return 錯誤碼
    */
    int ConveyorComDetect(int timeout);

傳送帶通訊輸入檢測觸發
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測觸發
    * @return 錯誤碼
    */
    int ConveyorComDetectTrigger();

傳送帶通訊輸入檢測觸發示例程序
+++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button3_Click(object sender, EventArgs e)
    {

        // 禁用按鈕防止重複點擊
        button3.Enabled = false;

        // 在後臺線程中執行耗時操作
        Thread conveyorThread = new Thread(ConveyorTest);
        conveyorThread.IsBackground = true;
        conveyorThread.Start();
    }

    private void button4_Click(object sender, EventArgs e)
    {
        // 獲取用戶輸入
        string input = texBox.Text;
        Console.WriteLine($"please input a number to trigger:{input}");
    
        int rtn = robot.ConveyorComDetectTrigger();
        Console.WriteLine($"ConveyorComDetectTrigger 返回值: {rtn}");
        
    }

    private void ConveyorTest()
    {
        // 使用Invoke來更新UI線程上的控件
        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("開始傳送帶測試...");
        });

        int retval = 0;
        int index = 1;
        int max_time = 30000;
        bool block = false;
        retval = 0;

        /* 傳送帶抓取流程 */
        DescPose startdescPose = new DescPose(139.176f, 4.717f, 9.088f, -179.999f, -0.004f, -179.990f);
        JointPos startjointPos = new JointPos(-34.129f, -88.062f, 97.839f, -99.780f, -90.003f, -34.140f);

        DescPose homePose = new DescPose(139.177f, 4.717f, 69.084f, -180.000f, -0.004f, -179.989f);
        JointPos homejointPos = new JointPos(-34.129f, -88.618f, 84.039f, -85.423f, -90.003f, -34.140f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        // 移動到安全位置
        retval = robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        Console.WriteLine($"MoveL 到安全位置返回值: {retval}");

        // 傳送帶檢測
        retval = robot.ConveryComDetect(1000 * 10);
        Console.WriteLine($"ConveyorComDetect 返回值: {retval}");

        // 獲取跟蹤數據
        retval = robot.ConveyorGetTrackData(2);
        Console.WriteLine($"ConveyorGetTrackData 返回值: {retval}");

        // 開始跟蹤
        retval = robot.ConveyorTrackStart(2);
        Console.WriteLine($"ConveyorTrackStart 返回值: {retval}");

        // 移動到起始位置
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveL(startjointPos, startdescPose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        // 結束跟蹤
        retval = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd 返回值: {retval}");

        // 返回安全位置
        robot.MoveL(homejointPos, homePose, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);

        this.Invoke((MethodInvoker)delegate {
            Console.WriteLine("傳送帶測試完成!");
            button3.Enabled = true;
        });
    }

機器人傳送帶操作示例程序
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnConvert_Click(object sender, EventArgs e)
        {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose pos1 = new DescPose(0, 0, 0, 0 ,0 ,0);
        DescPose pos2 = new DescPose(0, 0, 0, 0, 0, 0);

        pos1.tran.x = -351.175;
        pos1.tran.y = 3.389;
        pos1.tran.z = 431.172;
        pos1.rpy.rx = -179.111;
        pos1.rpy.ry = -0.241;
        pos1.rpy.rz = 90.388;

        pos2.tran.x = -333.654;
        pos2.tran.y = -229.003;
        pos2.tran.z = 404.335;
        pos2.rpy.rx = -179.139;
        pos2.rpy.ry = -0.779;
        pos2.rpy.rz = 91.269;
        int rtn = -1;

        double[] cmp = new double[3] { 0, 9.99, 0};
        rtn = robot.ConveyorCatchPointComp(cmp);
        if(rtn != 0)
        {
            return;
        }
        Console.WriteLine($"ConveyorCatchPointComp: rtn  {rtn}");

        rtn = robot.MoveCart(pos1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.ConveyorIODetect(10000);
        Console.WriteLine($"ConveyorIODetect: rtn  {rtn}");

        robot.ConveyorGetTrackData(1);
        rtn = robot.ConveyorTrackStart(1);
        Console.WriteLine($"ConveyorTrackStart: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 59, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 0, 0, 100.0f, 0.0f, 100.0f, -1.0f, 0, 0);
        Console.WriteLine($"ConveyorTrackMoveL: rtn  {rtn}");

        rtn = robot.ConveyorTrackEnd();
        Console.WriteLine($"ConveyorTrackEnd: rtn  {rtn}");

        rtn = robot.MoveCart(pos2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart: rtn  {rtn}");

        rtn = robot.MoveGripper(1, 100, 43, 21, 30000, 0);
        Console.WriteLine($"MoveGripper: rtn  {rtn}");
    }

末端傳感器配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端傳感器配置
    * @param  [in] idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param  [in] idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @param  [in] idSoftware 軟件版本，0-J1.0/HuiDe1.0(暫未開放)
    * @param  [in] idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    * @return  錯誤碼
    */
    int AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

獲取末端傳感器配置
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取末端傳感器配置
    * @param  [out] idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param  [out] idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @return  錯誤碼
    */
    int AxleSensorConfigGet(ref int idCompany, ref int idDevice);

末端傳感器激活
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端傳感器激活
    * @param  [in] actFlag 0-復位；1-激活
    * @return  錯誤碼
    */
    int AxleSensorActivate(int actFlag);

末端傳感器寄存器寫入
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  末端傳感器寄存器寫入
    * @param  [in] devAddr  設備地址編號 0-255
    * @param  [in] regHAddr 寄存器地址高8位
    * @param  [in] regLAddr 寄存器地址低8位
    * @param  [in] regNum  寄存器個數 0-255
    * @param  [in] data1 寫入寄存器數值1
    * @param  [in] data2 寫入寄存器數值2
    * @param  [in] isNoBlock 0-阻塞；1-非阻塞
    * @return  錯誤碼
    */
     int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端傳感器代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button2_Click_1(object sender, EventArgs e)
    {
        robot.AxleSensorConfig(18, 0, 0, 1);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(ref company, ref type);
        Console.WriteLine("company is " + company + ", type is " + type);

        int rtn = robot.AxleSensorActivate(1);
        Console.WriteLine("AxleSensorActivate rtn is " + rtn);

        Thread.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        Console.WriteLine("AxleSensorRegWrite rtn is " + rtn);   
    }

獲取機器人外設協議
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取機器人外設協議
    * @param [out] protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int GetExDevProtocol(ref int protocol);

設置機器人外設協議
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置機器人外設協議
    * @param [in] protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int SetExDevProtocol(int protocol);

設置機器人外設協議示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSetProto_Click(object sender, EventArgs e)
    {
      int protocol = 4096;
      int rtn = robot.SetExDevProtocol(protocol);
      Console.WriteLine("SetExDevProtocol rtn " + rtn);
      rtn = robot.GetExDevProtocol(ref protocol);
      Console.WriteLine("GetExDevProtocol rtn " + rtn + " protocol is: " + protocol);
    }

獲取末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取末端通訊參數
    * @param param 末端通訊參數
    * @return  錯誤碼
    */
    int GetAxleCommunicationParam(ref AxleComParam getParam);

設置末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置末端通訊參數
    * @param param  末端通訊參數
    * @return  錯誤碼
    */
    int SetAxleCommunicationParam(AxleComParam param);

設置末端文件傳輸類型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置末端文件傳輸類型
    * @param type 1-MCU升級文件；2-LUA文件
    * @return  錯誤碼
    */
    int SetAxleFileType(int type);

設置啓用末端LUA執行
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置啓用末端LUA執行
    * @param enable 0-不啓用；1-啓用
    * @return  錯誤碼
    */
    int SetAxleLuaEnable(int enable);

末端LUA文件異常錯誤恢復
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 末端LUA文件異常錯誤恢復
    * @param status 0-不恢復；1-恢復
    * @return  錯誤碼
    */
    int SetRecoverAxleLuaErr(int status);

獲取末端LUA執行使能狀態
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取末端LUA執行使能狀態
    * @param [out] status 0-未使能；1-已使能
    * @return  錯誤碼
    */
    int GetAxleLuaEnableStatus(ref int status);

設置末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置末端LUA末端設備啓用類型
    * @param [in] forceSensorEnable 力傳感器啓用狀態，0-不啓用；1-啓用
    * @param [in] gripperEnable 夾爪啓用狀態，0-不啓用；1-啓用
    * @param [in] IOEnable IO設備啓用狀態，0-不啓用；1-啓用
    * @return  錯誤碼
    */
    int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable);

獲取末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取末端LUA末端設備啓用類型
    * @param [out] forceSensorEnable 力傳感器啓用狀態，0-不啓用；1-啓用
    * @param [out] gripperEnable 夾爪啓用狀態，0-不啓用；1-啓用
    * @param [out] IOEnable IO設備啓用狀態，0-不啓用；1-啓用
    * @return  錯誤碼
    */
    int GetAxleLuaEnableDeviceType(ref int forceSensorEnable, ref int gripperEnable, ref int IOEnable);

獲取當前配置的末端設備
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取當前配置的末端設備
    * @param [out] forceSensorEnable 力傳感器啓用設備編號 0-未啓用；1-啓用
    * @param [out] gripperEnable 夾爪啓用設備編號，0-不啓用；1-啓用
    * @param [out] IODeviceEnable IO設備啓用設備編號，0-不啓用；1-啓用
    * @return  錯誤碼
    */
    int GetAxleLuaEnableDevice(ref int[] forceSensorEnable, ref int[] gripperEnable, ref int[] IODeviceEnable);

設置啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置啓用夾爪動作控制功能
    * @param [in] id 夾爪設備編號
    * @param [in] func func[0]-夾爪使能；func[1]-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩
    * @return  錯誤碼
    */
    int SetAxleLuaGripperFunc(int id, int[] func);

獲取啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取啓用夾爪動作控制功能
    * @param [in] id 夾爪設備編號
    * @param [out] func func[0]-夾爪使能；func[1]-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩
    * @return  錯誤碼
    */
    int GetAxleLuaGripperFunc(int id, ref int[] func);

機器人Ethercat從站文件寫入
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 機器人Ethercat從站文件寫入
    * @param [in] type 從站文件類型，1-升級從站文件；2-升級從站配置文件
    * @param [in] slaveID 從站號
    * @param [in] fileName 上傳文件名
    * @return  錯誤碼
    */
    int SlaveFileWrite(int type, int slaveID, string fileName);

上傳末端Lua開放協議文件
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 上傳末端Lua開放協議文件
    * @param filePath 本地lua文件路徑名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 錯誤碼 
    */
    int AxleLuaUpload(string filePath);

機器人Ethercat從站進入boot模式
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 機器人Ethercat從站進入boot模式
    * @return  錯誤碼
    */
    int SetSysServoBootMode();

機器人末端LUA文件操作代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button41_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_JunDuo_Xinjingcheng.lua");

        AxleComParam param = new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        AxleComParam getParam = new AxleComParam();
        robot.GetAxleCommunicationParam(ref getParam);
        Console.WriteLine("GetAxleCommunicationParam param is {0} {1} {2} {3} {4} {5} {6}",
            getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify,
            getParam.timeout, getParam.timeoutTimes, getParam.period);

        robot.SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot.GetAxleLuaEnableStatus(ref luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        robot.GetAxleLuaEnableDeviceType(ref forceEnable, ref gripperEnable, ref ioEnable);
        Console.WriteLine("GetAxleLuaEnableDeviceType param is {0} {1} {2}", forceEnable, gripperEnable, ioEnable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = new int[16];
        robot.GetAxleLuaGripperFunc(1, ref getFunc);
        int[] getforceEnable = new int[16];
        int[] getgripperEnable = new int[16];
        int[] getioEnable = new int[16];
        robot.GetAxleLuaEnableDevice(ref getforceEnable, ref getgripperEnable, ref getioEnable);
        Console.WriteLine("\ngetforceEnable status : ");
        foreach (int i in getforceEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetgripperEnable status : ");
        foreach (int i in getgripperEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine("\ngetioEnable status : ");
        foreach (int i in getioEnable)
        {
            Console.Write(i + ",");
        }
        Console.WriteLine();
        robot.ActGripper(1, 0);
        Thread.Sleep(2000);
        robot.ActGripper(1, 1);
        Thread.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("gripper pos is " + pkg.gripper_position);
            Thread.Sleep(100);
        }
    }

獲取SmartTool按鈕狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取SmartTool按鈕狀態
    * @param [out] state SmartTool手柄按鈕狀態;(bit0:0-通信正常；1-通信掉線；bit1-撤銷操作；bit2-清空程序；
        bit3-A鍵；bit4-B鍵；bit5-C鍵；bit6-D鍵；bit7-E鍵；bit8-IO鍵；bit9-手自動；bit10開始)
    * @return 錯誤碼
    */
    int GetSmarttoolBtnState(ref int state);

代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button11_Click(object sender, EventArgs e)
    {

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        int state = 0;
        while (true)
        {
            int rtn = robot.GetSmarttoolBtnState(ref state);
            string binaryString = Convert.ToString(state, 2).PadLeft(32, '0');
            Console.WriteLine($"GetSmarttoolBtnState rtn (binary): {binaryString}");
            Thread.Sleep(100);
        }

    }


上傳開放協議的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 上傳開放協議的Lua文件
    * @param  filePath 本地開放協議lua文件路徑名
    * @return 錯誤碼
    */
    public int OpenLuaUpload(String filePath)


獲取從站板卡參數
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取從站板卡參數
    * @param  type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  version  協議版本
    * @param  connState  0-未連接 1-已連接
    * @return  錯誤碼
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

寫入從站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  寫入從站DO
    * @param   DOIndex  DO編號
    * @param   wirteNum  寫入的數量
    * @param   status 寫入的數值，最多寫8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveWriteDO(int DOIndex, int wirteNum, int[] status)

寫入從站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  寫入從站AO
    * @param [in] AOIndex AO編號
    * @param [in] writeNum 寫入數量
    * @param [in] status 寫入數值陣列（最多8個）,AO0~AO15為整型，AO16~AO31為浮點
    * @return 錯誤碼
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int writeNum, double[] status)

讀取從站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  讀取從站DI
    * @param  DOIndex  DI編號
    * @param  readNum  讀取的數量
    * @param  status 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveReadDI(int DOIndex, int readNum, int[] status)

讀取從站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief  讀取從站AI
    * @param  AIIndex  AI編號
    * @param  readNum  讀取的數量
    * @param  status 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveReadAI(int AIIndex, int readNum, double[] status)

等待擴展DI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待擴展DI輸入
    * @param  DIIndex DI編號
    * @param  status 0-低電平；1-高電平
    * @param  waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待擴展AI輸入
    * @param  AIIndex AI編號
    * @param  waitType 0-大於；1-小於
    * @param  value AI值
    * @param  waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

從站模式相關接口指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button101_Click(object sender, EventArgs e)
    {
        int rtn = 0;
    
        int type = 0, version = 0, connState = 0;
        int[] ctrl = new int[8];
        double[] ctrlAO = new double[8];
        int[] DI = new int[8];
        double[] AI = new double[8];
        if (rtn != 0)
        {
            return;
        }
        // Upload and load open protocol file
        robot.OpenLuaUpload("E://temp/CtrlDev_field.lua");
        Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        Thread.Sleep(8000);
    
        // Get protocol type, software version, and connection status with PLC
        robot.GetFieldBusConfig(ref type, ref version, ref connState);
        Console.WriteLine($"type is {type}, version is {version}, connState is {connState}");
    
        // Write DO0 = 1, DO1 = 0, DO2 = 1
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
    
        // Write AO2 = 0x1000
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);

        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, ref DI);
            Console.WriteLine($"DI0 is {DI[0]}, DI1 is {DI[1]}, DI2 is {DI[2]}, DI3 is {DI[3]}");
            robot.FieldBusSlaveReadAI(0, 3, ref AI);
            Console.WriteLine($"AI0 is {AI[0]}, AI1 is {AI[1]}, AI2 is {AI[2]}");
            Thread.Sleep(10);
        }
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        Console.WriteLine($"FieldBusSlaveWaitDI result is {ret}");

        ret = robot.FieldBusSlaveWaitAI(0, 0, 400.00f, 100);
        Console.WriteLine($"FieldBusSlaveWaitAI result is {ret}"); 
    }

控制陣列式吸盤
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 控制陣列式吸盤
    * @param  slaveID 從站號
    * @param  len 長度
    * @param  ctrlValue 控制值 1-按最大真空度吸取 2-按設定真空度吸取 3-停止吸取
    * @return 錯誤碼
    */
    public int SetSuckerCtrl(int slaveID, int len, int[] ctrlValue)

獲取陣列式吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取陣列式吸盤狀態
    * @param  slaveID 從站號
    * @param  state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param  pressValue 當前真空度 單位kpa
    * @param  error 吸盤當前的錯誤碼
    * @return 錯誤碼
    */
    public int GetSuckerState(int slaveID, int[] state, int[] pressValue, int[] error)

等待吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    /**
    * @brief 等待吸盤狀態
    * @param  slaveID 從站號
    * @param  state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param  ms 等待最大時間
    * @return 錯誤碼
    */
    public int WaitSuckerState(int slaveID, int state, int ms)

陣列式吸盤控制指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void TestSucker(Robot robot)
    {
    
        int[] ctrl = new int[20];
        int state=0;
        int pressValue=0;
        int error=0;
        int rtn;
    
    
        // Upload and load open protocol file
        robot.OpenLuaUpload(@"C:\SDK\CtrlDev_sucker.lua");
        Thread.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        Thread.Sleep(1000);
    
        // Control sucker in broadcast mode with maximum adsorption capacity
        ctrl[0] = 1;
        robot.SetSuckerCtrl(0, 1, ctrl);
    
        // Monitor states of sucker 1 and sucker 12 in a loop
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker1 state is {state}, pressValue is {pressValue}, error num is {error}");
            robot.GetSuckerState(12, ref state, ref pressValue, ref error);
            Console.WriteLine($"sucker12 state is {state}, pressValue is {pressValue}, error num is {error}");
            Thread.Sleep(100);
        }
        // Wait for sucker 1 to reach adsorbed state, timeout 100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        Console.WriteLine($"WaitSuckerState result is {ret}");
    
        // Unicast mode to turn off sucker 1 and 12
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
    
        robot.CloseRPC();
    }

激光外設打開關閉函數
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外設打開關閉函數
     * @param [in] OnOff 0-關閉 1-打開
     * @param [in] weldId 焊縫ID 默認爲0
     * @return 錯誤碼
     */
    public int LaserTrackingLaserOnOff(int OnOff, int weldId)
    
激光跟蹤開始結束函數
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    
    /**
     * @brief 激光跟蹤開始結束函數
     * @param [in] OnOff 0-結束 1-開始
     * @param [in] coordId 激光外設工具座標系編號
     * @return 錯誤碼
     */
    public int LaserTrackingTrackOnOff(int OnOff, int coordId)

激光尋位-固定反向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光尋位-固定反向
     * @param [in] direction 0-x+ 1-x- 2-y+ 3-y- 4-z+ 5-z-
     * @param [in] vel 速度 單位%
     * @param [in] distance 最大尋位距離 單位mm
     * @param [in] timeout 尋位超時時間 單位ms
     * @param [in] posSensorNum 激光標定的工具座標編號
     * @return 錯誤碼
     */
    public int LaserTrackingSearchStart_xyz(int direction, int vel, int distance, int timeout, int posSensorNum)
    
激光尋位-任意方向
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光尋位-任意方向
     * @param [in] directionPoint 尋位輸入的點的xyz左邊
     * @param [in] vel 速度 單位%
     * @param [in] distance 最大尋位距離 單位mm
     * @param [in] timeout 尋位超時時間 單位ms
     * @param [in] posSensorNum 激光標定的工具座標編號
     * @return 錯誤碼
     */
    public int LaserTrackingSearchStart_point(DescTran directionPoint, int vel, int distance, int timeout, int posSensorNum)
   
激光尋位結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
    * @brief  激光尋位結束
    * @return 錯誤碼
    */
    public int LaserTrackingSearchStop()

激光IP配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光IP配置
     * @param [in] ip 激光外設的ip地址
     * @param [in] port 激光外設的端口號
     * @return 錯誤碼
     */
    public int LaserTrackingSensorConfig(string ip, int port)

激光外設採樣週期配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外設採樣週期配置
     * @param [in] period 激光外設採樣週期 單位ms
     * @return 錯誤碼
     */
    public int LaserTrackingSensorSamplePeriod(int period)

激光外設驅動加載
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外設驅動加載
     * @param [in] type 激光外設驅動的協議類型 101-睿牛 102-創想 103-全視 104-同舟 105-奧太
     * @return 錯誤碼
     */
    public int LoadPosSensorDriver(int type)

激光外設驅動卸載
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光外設驅動卸載
     * @return 錯誤碼
     */
    public int UnLoadPosSensorDriver()

激光焊縫軌跡記錄
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光焊縫軌跡記錄
     * @param [in] status 0-停止記錄 1-實時跟蹤  2-開始記錄
     * @param [in] delayTime 延時時間 單位ms
     * @return 錯誤碼
     */
    public int LaserSensorRecord1(int status, int delayTime)

激光焊縫軌跡復現
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光焊縫軌跡復現
     * @param [in] delayTime 延時時間 單位ms
     * @param [in] speed 速度 單位%
     * @return 錯誤碼
     */
    public int LaserSensorReplay(int delayTime, double speed)

激光跟蹤復現
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 激光跟蹤復現
     * @return 錯誤碼
     */
    public int MoveLTR()

激光焊縫軌跡復現
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 激光焊縫軌跡復現
    * @param [in] delayMode 模式 0-延時時間 1-延時距離
    * @param [in] delayTime 延時時間 單位ms
    * @param [in] delayDisExAxisNum 擴展軸編號
    * @param [in] delayDis 延時距離 單位mm
    * @param [in] sensitivePara 補償靈敏係數
    * @param [in] trackMode 定點追蹤類型。0-擴展軸非同步運動；1-機器人
    * @param [in] triggerMode 定點追蹤觸發方式。0-追蹤時長；1-IO
    * @param [in] runTime 機器人定點追蹤時長(s)
    * @param [in] speed 速度 單位%
    * @return 錯誤碼
    */
    public int LaserSensorRecordandReplay(int delayMode, int delayTime, int delayDisExAxisNum,double delayDis, double sensitivePara, int trackMode, int triggerMode,double runTime, double speed)
    
運動到焊縫記錄的起點
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 運動到焊縫記錄的起點
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 單位%
     * @return 錯誤碼
     */
    public int MoveToLaserRecordStart(int moveType, double ovl)

運動到焊縫記錄的終點
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 運動到焊縫記錄的終點
     * @param [in] moveType 0-PTP 1-LIN
     * @param [in] ovl 速度 單位%
     * @return 錯誤碼
     */
    public int MoveToLaserRecordEnd(int moveType, double ovl)

運動到激光傳感器尋位點
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 運動到激光傳感器尋位點
     * @param [in] moveFlag 運動類型：0-PTP；1-LIN
     * @param [in] ovl 速度縮放因子，0-100
     * @param [in] dataFlag 焊縫緩存數據選擇：0-執行規劃數據；1-執行記錄數據
     * @param [in] plateType 板材類型：0-波紋板；1-瓦楞板；2-圍欄板；3-油桶；4-波紋甲殼鋼
     * @param [in] trackOffectType 激光傳感器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-激光傳感器原始數據偏移
     * @param [in] offset 偏移量
     * @return 錯誤碼
     */
    public int MoveToLaserSeamPos(int moveFlag, double ovl, int dataFlag, int plateType, int trackOffectType, DescPose offset)
    
獲取激光傳感器尋位點座標信息
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    /**
     * @brief 獲取激光傳感器尋位點座標信息
     * @param [in] trackOffectType 激光傳感器偏移類型：0-不偏移；1-基座標系偏移；2-工具座標系偏移；3-激光傳感器原始數據偏移
     * @param [in] offset 偏移量
     * @param [out] jPos 關節位置[°]
     * @param [out] descPos 笛卡爾位置[mm]
     * @param [out] tool 工具座標系
     * @param [out] user 工件座標系
     * @param [out] exaxis 擴展軸位置[mm]
     * @return 錯誤碼
     */
    public int GetLaserSeamPos(int trackOffectType, DescPose offset, ref JointPos jPos, ref DescPose descPos, ref int tool, ref int user, ref ExaxisPos exaxis)

激光外設傳感器參數配置及調試代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserConfig()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);
        robot.LaserTrackingLaserOnOff(0, 0);
        System.Threading.Thread.Sleep(3000);
        robot.LaserTrackingLaserOnOff(1, 0);
    }

激光軌跡掃描及軌跡復現的代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    void testLaserRecordAndReplay()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i=0;i<10;++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserSensorRecord1(2, 10);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);

            robot.LaserSensorRecord1(0, 10);
            robot.MoveToLaserRecordStart(1, 30);
            robot.LaserSensorReplay(10, 100);
            robot.MoveLTR();
            robot.LaserSensorRecord1(0, 10);
            Console.WriteLine($"Number of completions : {i+1} ");
        }
                
    }

激光尋位及實時跟蹤的代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public static void testLasertrack()
    {
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        robot.OpenLuaUpload("D://zUP/CtrlDev_laser_ruiniu-0117.lua");
        System.Threading.Thread.Sleep(2000);
        robot.SetCtrlOpenLUAName(0, "CtrlDev_laser_ruiniu-0117.lua");
        robot.UnloadCtrlOpenLUA(0);
        robot.LoadCtrlOpenLUA(0);
        System.Threading.Thread.Sleep(8000);
        for (int i = 0; i < 10; ++i)
        {
            JointPos startjointPos = new JointPos(56.205, -117.951, 141.872, -118.149, -94.217, -122.176);
            DescPose startdescPose = new DescPose(-97.552, -282.855, 26.675, 174.182, -1.338, -91.707);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
            DescTran directionPoint = new DescTran();

            robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 3);
            robot.LaserTrackingSearchStop();
            robot.MoveToLaserSeamPos(1, 30, 0, 0, 0, offdese);

            robot.LaserTrackingTrackOnOff(1, 3);

            JointPos endjointPos = new JointPos(68.809, -87.100, 121.120, -127.233, -95.038, -109.555);
            DescPose enddescPose = new DescPose(-103.555, -464.234, 13.076, 174.179, -1.344, -91.709);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, exaxisPos, 0, 0, offdese, 0);
            robot.LaserTrackingTrackOnOff(0, 3);
            Console.WriteLine($"Number of completions : {i + 1} ");
        }
    }

擴展軸與機器人同步進行激光跟蹤的代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:


    public void TestLaserTrackAndExitAxis()
    {   
        ExaxisPos startexaxisPos = new ExaxisPos(0, 0, 0, 0);
        ExaxisPos seamexaxisPos = new ExaxisPos(-10, 0, 0, 0);
        ExaxisPos endexaxisPos = new ExaxisPos(-30, 0, 0, 0);      
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);     
        JointPos startjointPos = new JointPos(58.337, -119.628, 146.037, -116.358, -92.224, -117.654);
        DescPose startdescPose = new DescPose(-53.375, -255.363, 0.919, 178.054, 1.077, -94.026);
        for (int i=0;i<10;++i)
        {
            robot.ExtAxisSyncMoveJ(startjointPos, startdescPose, 1, 0, 100, 100, 100, startexaxisPos, -1, 0, offdese);
            Console.WriteLine("11111");
            int ret = robot.LaserTrackingSearchStart_xyz(3, 100, 300, 1000, 2);
            robot.LaserTrackingSearchStop();
            Console.WriteLine("2222");
            int tool = 0;
            int user = 0;
            JointPos seamjointPos = new JointPos();
            DescPose seamdescPose = new DescPose();
            robot.GetLaserSeamPos(0, offdese, ref seamjointPos, ref seamdescPose, ref tool, ref user, ref startexaxisPos);
            Console.WriteLine($"{seamjointPos.jPos[0]}, {seamjointPos.jPos[1]}, {seamjointPos.jPos[2]}, " +
                            $"{seamjointPos.jPos[3]}, {seamjointPos.jPos[4]}, {seamjointPos.jPos[5]}, " +
                            $"{seamdescPose.tran.x}, {seamdescPose.tran.y}, {seamdescPose.tran.z}, " +
                            $"{seamdescPose.rpy.rx}, {seamdescPose.rpy.ry}, {seamdescPose.rpy.rz}");
            if (ret == 0)
            {
                robot.ExtAxisSyncMoveJ(seamjointPos, seamdescPose, 1, 0, 100, 100, 100, seamexaxisPos, -1, 0, offdese);
                Console.WriteLine("3333");
                robot.LaserTrackingTrackOnOff(1, 2);
                JointPos endjointPos = new JointPos(70.580, -90.918, 126.593, -125.154, -92.162, -105.403);
                DescPose enddescPose = new DescPose(-53.375, -419.020, 0.920, 178.054, 1.076, -94.026);
                robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 0, 20, 100, 100, -1, endexaxisPos, 0, offdese);
                robot.LaserTrackingTrackOnOff(0, 2);
            }
            Console.WriteLine($"Number of completions : {i + 1} ");
        }     
    }

末端透傳功能打開關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 開啟末端通用透傳功能
    * @param [in] 使能，0-關閉，1-開啟
    * @return 錯誤碼
    */
    public int SetAxleGenComEnable(int mode)

末端透傳功能非週期數據收發
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 末端發送非週期數據並等待應答
    * @param [in]  len_snd，發送的長度
    * @param [in]  sndBuff[]，發送數據
    * @param [in]  len_rcv，選擇接受的長度
    * @param [out]  rcvBuff[]，應答的數據
    * @return 錯誤碼
    */
    public int SndRcvAxleGenComCmdData(int len_snd, int[] sndBuff, int len_rcv, ref int[] rcvdata)

基於末端透傳功能倍益康艾灸頭非週期數據通訊代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

        int[] rcvdata = new int[16];
        int ret = 0;
        int cnt = 1;

        JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
        DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

        JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
        DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        //開啟末端透傳功能
        robot.SetAxleGenComEnable(1);
        robot.SetAxleLuaEnable(1);

        while(cnt<=10)
        { 
            //讀取版本號
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            //讀取艾灸頭在位狀態
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            //開啟艾灸頭激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            //關閉艾灸頭激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }

下載開放協議Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 下載開放協議Lua文件
    * @param [in] fileName 開放協議文件名稱“CtrlDev_XXX.lua”
    * @param [in] savePath 開放協議保存文件路徑
    * @return 錯誤碼
    */
    public int OpenLuaDownload(string fileName, string savePath)
    
刪除開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 刪除開放協議Lua文件
    * @param [in] fileName 要刪除的開放協議lua文件名“CtrlDev_XXX.lua”
    * @return 錯誤碼
    */
    public int OpenLuaDelete(string fileName)
        
刪除所有開放協議Lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 刪除所有開放協議Lua文件
    * @return 錯誤碼
    */
    public int AllOpenLuaDelete()

開放協議Lua文件操作的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public int TestCtrlOpenLuaOperate()
    {
        int rtn;

        // 上傳 Lua 文件到機器人
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");
        rtn = robot.OpenLuaUpload("D://zUP/openlua/CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"OpenLuaUpload rtn is {rtn}");

        // 從機器人下載 Lua 文件
        rtn = robot.OpenLuaDownload("CtrlDev_WELDING_A.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");
        rtn = robot.OpenLuaDownload("CtrlDev_SWDPOLISH.lua", "D://zDOWN/");
        Console.WriteLine($"OpenLuaDownload rtn is {rtn}");

        // 設置控制開放協議 Lua 名稱
        rtn = robot.SetCtrlOpenLUAName(0, "CtrlDev_WELDING_A.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");
        rtn = robot.SetCtrlOpenLUAName(1, "CtrlDev_SWDPOLISH.lua");
        Console.WriteLine($"SetCtrlOpenLUAName rtn is {rtn}");

        // 獲取控制開放協議 Lua 名稱
        string[] name = new string[4];
        rtn = robot.GetCtrlOpenLUAName(ref name);
        Console.WriteLine($"ctrl open lua names : {name[0]}, {name[1]}, {name[2]}, {name[3]}");

        // 加載和卸載開放協議 Lua
        rtn = robot.LoadCtrlOpenLUA(1);
        Console.WriteLine($"LoadCtrlOpenLUA rtn is {rtn}");
        robot.Sleep(2000);
        rtn = robot.UnloadCtrlOpenLUA(1);
        Console.WriteLine($"UnloadCtrlOpenLUA rtn is {rtn}");

        // 刪除指定 Lua 文件和所有 Lua 文件
        rtn = robot.OpenLuaDelete("CtrlDev_WELDING_A.lua");
        Console.WriteLine($"OpenLuaDelete rtn is {rtn}");
        rtn = robot.AllOpenLuaDelete();
        Console.WriteLine($"AllOpenLuaDelete rtn is {rtn}");

        return 0;
    }