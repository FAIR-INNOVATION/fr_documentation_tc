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


