機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

獲取當前關節位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前關節位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int GetActualJointPosDegree(byte flag, ref JointPos jPos); 

獲取當前關節位置(弧度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前關節位置(弧度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位rad
    * @return  錯誤碼
    */   
    int GetActualJointPosRadian(byte flag, ref JointPos jPos);

獲取關節反饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取關節反饋速度-deg/s 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed 六個關節速度 
    * @return 錯誤碼 
    */
    int GetActualJointSpeedsDegree(byte flag, ref double[] speed);

獲取關節反饋加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取關節反饋加速度-deg/s^2 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] acc 六個關節加速度 
    * @return 錯誤碼 
    */
    int GetActualJointAccDegree(byte flag, ref double[] acc); 

獲取TCP指令速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取TCP指令速度-合速度 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 線性速度 
    * @param [out] ori_speed 姿態速度 
    * @return 錯誤碼 
    */
    int GetTargetTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed); 

獲取TCP反饋速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 獲取TCP反饋速度-合速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] tcp_speed 線性速度 
    * @param [out] ori_speed 姿態速度 
    * @return 錯誤碼 
    */
    int GetActualTCPCompositeSpeed(byte flag, ref double tcp_speed, ref double ori_speed);

獲取TCP指令速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取TCP指令速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 錯誤碼 
    */
    int GetTargetTCPSpeed(byte flag, ref double[] speed);

獲取TCP反饋速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取TCP反饋速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 錯誤碼 
    */
    int GetActualTCPSpeed(byte flag, ref double[] speed);

獲取當前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    int GetActualTCPPose(byte flag, ref DescPose desc_pos); 

獲取當前工具座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工具座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具座標系編號
    * @return  錯誤碼
    */
    int GetActualTCPNum(byte flag, ref int id);  

獲取當前工件座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工件座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件座標系編號
    * @return  錯誤碼
    */
    int GetActualWObjNum(byte flag, ref int id);

獲取當前末端法蘭位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前末端法蘭位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法蘭位姿
    * @return  錯誤碼
    */
    int GetActualToolFlangePose(byte flag, ref DescPose desc_pos);   

獲取當前關節轉矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取當前關節轉矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 關節轉矩
    * @return  錯誤碼
    */
    int GetJointTorques(byte flag, float[] torques); 

獲取系統時間
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取系統時間
    * @param  [out] t_ms 單位ms,可按照UTC時間轉換,機器人故障狀態下獲取CLock為0並返回錯誤碼
    * @return  錯誤碼
    */
    public int GetSystemClock(ref double t_ms)

同步系統時間至機器人
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取目前上位機系統時間並發送給機器人，同步系統時間（由於QNX系統限制，同步精度為分鐘級）
    * @return 錯誤碼
    */
    public int SetRobottime()

同步系統時間至機器人代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void testSetAndGetRobotTime()
    {
        double t_ms = 0.0;

        int ret = robot.GetSystemClock(ref t_ms);
        if (ret == 0)
        {
            Console.WriteLine($"system clock : {t_ms}");
            // 將毫秒時間戳轉換為DateTime（UTC時間）
            DateTime utcTime = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc).AddMilliseconds(t_ms);
            Console.WriteLine($"BEFORE UTC Time   : {utcTime:yyyy-MM-dd HH:mm:ss}");
        }
        else
        {
            Console.WriteLine($"GetSystemClock failed,ret:{ret}");
        }

        robot.SetRobottime();

        // 設定後獲取機器人時間
        double t_ms_after = 0;
        ret = robot.GetSystemClock(ref t_ms_after);
        if (ret == 0)
        {
            Console.WriteLine($"system clock : {t_ms}");
            DateTime robotTimeAfter = DateTimeOffset.FromUnixTimeMilliseconds((long)t_ms_after).UtcDateTime;

            // 獲取設定前的PC時間（作為預期值）
            DateTime pcTimeBefore = DateTime.Now;

            // 將預期時間（PC時間）和機器人時間都截斷至分鐘
            DateTime pcMinute = new DateTime(pcTimeBefore.Year, pcTimeBefore.Month, pcTimeBefore.Day,
                                                pcTimeBefore.Hour, pcTimeBefore.Minute, 0, DateTimeKind.Utc);
            DateTime robotMinute = new DateTime(robotTimeAfter.Year, robotTimeAfter.Month, robotTimeAfter.Day,
                                                robotTimeAfter.Hour, robotTimeAfter.Minute, 0, DateTimeKind.Utc);

            // 比較一致性
            bool isConsistent = (pcMinute == robotMinute);
            if (isConsistent)
            {
                Console.WriteLine($"Consistent     | PC time: {pcMinute:yyyy-MM-dd HH:mm}  | Robot time: {robotMinute:yyyy-MM-dd HH:mm}");
            }
            else
            {
                Console.WriteLine($"[Inconsistent | PC time: {pcMinute:yyyy-MM-dd HH:mm}  | Robot time: {robotMinute:yyyy-MM-dd HH:mm}");
            }
        }
        else
        {
            Console.WriteLine($"GetSystemClock failed,ret:{ret}");
        }
    }    

查詢機器人運動是否完成
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  查詢機器人運動是否完成
    * @param  [out]  state  0-未完成，1-完成
    * @return  錯誤碼
    */   
    int GetRobotMotionDone(ref byte state);

查詢機器人運動隊列緩存長度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查詢機器人運動隊列緩存長度 
    * @param [out] len   緩存長度
    * @return 錯誤碼 
    */
    int GetMotionQueueLength(ref int len);

獲取機器人急停狀態
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人急停狀態
    * @param [out] state 急停狀態，0-非急停，1-急停
    * @return 錯誤碼  
    */
    int GetRobotEmergencyStopState(ref byte state);

獲取SDK與機器人的通訊狀態
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取SDK與機器人的通訊狀態
    * @param [out]  state 通訊狀態，0-通訊正常，1-通訊異常
    */
    int GetSDKComState(ref int state);

獲取安全停止信號
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取安全停止信號
    * @param [out]  si0_state 安全停止信號SI0，0-無效，1-有效
    * @param [out]  si1_state 安全停止信號SI1，0-無效，1-有效
    */
    int GetSafetyStopState(ref byte si0_state, ref byte si1_state);

獲取機器人關節驅動器溫度(℃)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器溫度(℃)
    * @return 錯誤碼
    */
    int GetJointDriverTemperature(double[] temperature);

獲取機器人關節驅動器扭矩(Nm)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器扭矩(Nm)
    * @return 錯誤碼
    */
    int GetJointDriverTorque(double torque[]);

獲取最新一幀的機器人即時狀態數據（內部機制改動）
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取最新一幀的機器人即時狀態數據（內部執行緒持續更新，此介面直接返回快取數據）
    * @param [out] pkg 引用參數，用於接收機器人狀態數據（ROBOT_STATE_PKG 結構體）
    * @return 成功返回 0；失敗返回負錯誤碼（例如網路通訊錯誤）
    */
    public int GetRobotRealTimeState(ref ROBOT_STATE_PKG pkg)

機器人狀態查詢代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button29_Click(object sender, EventArgs e)
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        double yangle = 0, zangle = 0;
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle:{yangle},zangle:{zangle}");

        JointPos j_deg = new JointPos(0,0,0,0,0,0);
        robot.GetActualJointPosDegree(0, ref j_deg);
        Console.WriteLine($"joint pos deg:{j_deg.jPos[0]},{j_deg.jPos[1]},{j_deg.jPos[2]},{j_deg.jPos[3]},{j_deg.jPos[4]},{j_deg.jPos[5]}");

        double[] jointSpeed = new double[6];
        robot.GetActualJointSpeedsDegree(0, ref jointSpeed);
        Console.WriteLine($"joint speeds deg:{jointSpeed[0]},{jointSpeed[1]},{jointSpeed[2]},{jointSpeed[3]},{jointSpeed[4]},{jointSpeed[5]}");

        double[] jointAcc = new double[6];
        robot.GetActualJointAccDegree(0, ref jointAcc);
        Console.WriteLine($"joint acc deg:{jointAcc[0]},{jointAcc[1]},{jointAcc[2]},{jointAcc[3]},{jointAcc[4]},{jointAcc[5]}");

        double tcp_speed = 0, ori_speed = 0;
        robot.GetTargetTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetTargetTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        robot.GetActualTCPCompositeSpeed(0, ref tcp_speed, ref ori_speed);
        Console.WriteLine($"GetActualTCPCompositeSpeed tcp {tcp_speed}; ori {ori_speed}");

        double[] targetSpeed = new double[6];
        robot.GetTargetTCPSpeed(0,ref targetSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {targetSpeed[0]},{targetSpeed[1]},{targetSpeed[2]},{targetSpeed[3]},{targetSpeed[4]},{targetSpeed[5]}");

        double[] actualSpeed = new double[6];
        robot.GetActualTCPSpeed(0, ref actualSpeed);
        Console.WriteLine($"GetTargetTCPSpeed {actualSpeed[0]},{actualSpeed[1]},{actualSpeed[2]},{actualSpeed[3]},{actualSpeed[4]},{actualSpeed[5]}");

        DescPose tcp = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualTCPPose(0, ref tcp);
        Console.WriteLine($"tcp pose:{tcp.tran.x},{tcp.tran.y},{tcp.tran.z},{tcp.rpy.rx},{tcp.rpy.ry},{tcp.rpy.rz}");

        DescPose flange = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetActualToolFlangePose(0, ref flange);
        Console.WriteLine($"flange pose:{flange.tran.x},{flange.tran.y},{flange.tran.z},{flange.rpy.rx},{flange.rpy.ry},{flange.rpy.rz}");

        int id = 0;
        robot.GetActualTCPNum(0, ref id);
        Console.WriteLine($"tcp num:{id}");

        robot.GetActualWObjNum(0, ref id);
        Console.WriteLine($"wobj num:{id}");

        double[] jtorque = new double[6];
        robot.GetJointTorques(0, jtorque);
        Console.WriteLine($"torques:{jtorque[0]},{jtorque[1]},{jtorque[2]},{jtorque[3]},{jtorque[4]},{jtorque[5]}");

        double t_ms = 0;
        robot.GetSystemClock(ref t_ms);
        Console.WriteLine($"system clock:{t_ms}");

        int config = 0;
        robot.GetRobotCurJointsConfig(ref config);
        Console.WriteLine($"joint config:{config}");

        byte motionDone = 0;
        robot.GetRobotMotionDone(ref motionDone);
        Console.WriteLine($"GetRobotMotionDone :{motionDone}");

        int len = 0;
        robot.GetMotionQueueLength(ref len);
        Console.WriteLine($"GetMotionQueueLength :{len}");

        byte emergState = 0;
        robot.GetRobotEmergencyStopState(ref emergState);
        Console.WriteLine($"GetRobotEmergencyStopState :{emergState}");

        int comstate = 0;
        robot.GetSDKComState(ref comstate);
        Console.WriteLine($"GetSDKComState :{comstate}");

        byte si0_state = 0, si1_state = 0;
        robot.GetSafetyStopState(ref si0_state, ref si1_state);
        Console.WriteLine($"GetSafetyStopState :{si0_state} {si1_state}");

        double[] temp = new double[6];
        robot.GetJointDriverTemperature(temp);
        Console.WriteLine($"Temperature:{temp[0]},{temp[1]},{temp[2]},{temp[3]},{temp[4]},{temp[5]}");

        double[] torque = new double[6];
        robot.GetJointDriverTorque(torque);
        Console.WriteLine($"torque:{torque[0]},{torque[1]},{torque[2]},{torque[3]},{torque[4]},{torque[5]}");

        robot.GetRobotRealTimeState(ref pkg);
    }

逆運動學求解
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] config 關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos);

逆運動學求解(參考位置)
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判斷是否有解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] result 0-無解，1-有解
    * @return  錯誤碼
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref JointPos joint_pos); 

逆運動學求解，笛卡爾空間包含擴展軸位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 逆運動學求解，笛卡爾空間包含擴展軸位置
    * @param [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param [in] desc_pos 笛卡爾位姿
    * @param [in] exaxis 擴展軸位置
    * @param [in] tool 工具號
    * @param [in] workPiece 工件號
    * @param [out] joint_pos 關節位置
    * @param [in] config -1：自動求解，0-7對應八組解
    * @return 錯誤碼
    */
    public int GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, ref JointPos joint_pos, int config = -1);

逆運動學求解包含擴展軸位置程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestInverseKinExaxis()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pkg);
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;

        DescPose desc = new DescPose(-547.469, -47.361, 184.149, 169.843, 4.579, 82.557);
        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        JointPos jointPos = new JointPos(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, ref jointPos, 0);
        Console.WriteLine($"GetInverseKinExaxis joint is {jointPos.jPos[0]}, {jointPos.jPos[1]}, {jointPos.jPos[2]}, {jointPos.jPos[3]}, {jointPos.jPos[4]}, {jointPos.jPos[5]}");
    }

獲取逆運動學是否有解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 逆運動學求解，判斷指定參考關節位置是否有解
    * @param [in] posMode 0絕對位姿，1相對位姿-基座標系，2相對位姿-工具座標系 
    * @param [in] desc_pos 笛卡爾位姿 
    * @param [in] joint_pos_ref 參考關節位置 
    * @param [out] hasResult 0-無解，1-有解 
    * @return 錯誤碼 
    */ 
    int GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref bool hasResult);  

正運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  正運動學求解
    * @param  [in] joint_pos 關節位置
    * @param  [out] desc_pos 笛卡爾位姿
    * @return  錯誤碼
    */
    int GetForwardKin(JointPos joint_pos, ref DescPose desc_pos); 

機器人正逆運動學計算代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button30_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);

        JointPos inverseRtn = new JointPos(0, 0, 0, 0, 0, 0);

        robot.GetInverseKin(0, desc_pos1, -1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKin rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");
        robot.GetInverseKinRef(0,  desc_pos1, j1, ref inverseRtn);
        Console.WriteLine($"dcs1 GetInverseKinRef rtn is {inverseRtn.jPos[0]} {inverseRtn.jPos[1]} {inverseRtn.jPos[2]} {inverseRtn.jPos[3]} {inverseRtn.jPos[4]} {inverseRtn.jPos[5]}");

        bool hasResut = false;
        robot.GetInverseKinHasSolution(0,  desc_pos1,  j1, ref hasResut);
        Console.WriteLine($"dcs1 GetInverseKinRef result {hasResut}");

        DescPose forwordResult = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(j1, ref forwordResult);
        Console.WriteLine($"jpos1 forwordResult rtn is {forwordResult.tran.x} {forwordResult.tran.y} {forwordResult.tran.z} {forwordResult.rpy.rx} {forwordResult.rpy.ry} {forwordResult.rpy.rz}");
    }

查詢機器人示教管理點數據
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查詢機器人示教管理點位數據 
    * @param [in] name    點位名
    * @param [out] data   點位數據double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool, wobj,speed,acc,e1,e2,e3,e4}
    * @return 錯誤碼 
    */ 
    int GetRobotTeachingPoint(string name, ref double[] data); 

獲取機器人DH參數補償值 
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取機器人DH參數補償值 
    * @param [out] dhCompensation 機器人DH參數補償值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 錯誤碼 
    */
    int GetDHCompensation(ref double[] dhCompensation);


獲取控制箱SN碼
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取控制箱SN碼
    * @param [out] SNCode 控制箱SN碼
    * @return 錯誤碼
    */
    int GetRobotSN(ref string SNCode);

查詢機器人示教管理點位數據代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button31_Click(object sender, EventArgs e)
    {
        string name = "A0";
        double[] data = new double[20];
        int rtn = robot.GetRobotTeachingPoint(name, ref data);
        Console.WriteLine(" {0} name is: {1} \n", rtn, name);
        for (int i = 0; i < 20; i++)
        {
            Console.WriteLine("data is: {0} \n", data[i]);
        }

        int que_len = 0;
        rtn = robot.GetMotionQueueLength(ref que_len);
        Console.WriteLine("GetMotionQueueLength rtn is: {0}, queue length is: {1} \n", rtn, que_len);

        double[] dh = { 0, 0, 0, 0, 0, 0 };
        int retval = 0;
        retval = robot.GetDHCompensation(ref dh);
        Console.WriteLine($"retval is  {retval}");
        Console.WriteLine($"dh is {dh[0]}, {dh[1]}, {dh[2]}, {dh[3]}, {dh[4]}, {dh[5]}");
        string SN = "";
        robot.GetRobotSN(ref SN);
        Console.WriteLine($"robot SN is  {SN}");
    }

根據編號獲取工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據編號獲取工具座標系
    * @param [in] id 工具座標系編號
    * @param [out] coord 座標系數值
    * @param [out] type 工具類型 0-工具；1-感測器
    * @param [out] install 安裝位置 0-機器人末端；1-機器人外部
    * @param [out] toolID 工具ID 
    * @param [out] loadNo 負載編號
    * @return 錯誤碼
    */
    int GetToolCoordWithID(int id, ref DescPose coord, ref int type, ref int install, ref int toolID, ref int loadNo)

根據編號獲取工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據編號獲取工件座標系
    * @param [in] id 工件座標系編號
    * @param [out] coord 座標系數值
    * @param [out] refFrame 參考座標系
    * @return 錯誤碼
    */
    public int GetWObjCoordWithID(int id, ref DescPose coord, ref int refFrame)

根據編號獲取外部工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據編號獲取外部工具座標系
    * @param [in] id 外部工具座標系編號，20-39對應外部工具座標系0-19
    * @param [out] coord 機器人外部固定工具TCP位姿
    * @param [out] tcoord 機器人末端安裝工件座標系位姿
    * @return 錯誤碼
    */
    public int GetExToolCoordWithID(int id, ref DescPose coord, ref DescPose tcoord)

根據編號獲取擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據編號獲取擴展軸座標系
    * @param [in] id 外部工具座標系編號
    * @param [out] coord 座標系數值
    * @param [out] axisCoordNum 擴展軸號；bit0-bit3對應擴展軸1-擴展軸4；如axisCoordNum值為3，對應應用擴展軸[1，2]
    * @param [out] calibFlag 標定標誌；0-未標定；1-已標定
    * @return 錯誤碼
    */
    public int GetExAxisCoordWithID(int id, ref DescPose coord, ref int axisCoordNum, ref int calibFlag)

獲取當前工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取當前工具座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurToolCoord(ref DescPose coord)

獲取當前工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取當前工件座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurWObjCoord(ref DescPose coord)

獲取當前外部工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取當前外部工具座標系
     * @param  [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurExToolCoord(ref DescPose coord)

獲取當前擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取當前擴展軸座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurExAxisCoord(ref DescPose coord)

根據編號獲取座標代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-V3.9.8

.. code-block:: c#
    :linenos:

    public int TestCoord()
    {
        int rtn;
        int id = 1;

        // GetToolCoordWithID
        DescPose toolCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int type = 0, install = 0, toolID = 0, loadNo = 0;
        rtn = robot.GetToolCoordWithID(id, ref toolCoord, ref type, ref install, ref toolID, ref loadNo);
        Console.WriteLine("GetToolCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, type={7}, install={8}, toolID={9}, loadNo={10}",
            id, toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz, type, install, toolID, loadNo);

        // GetWObjCoordWithID
        DescPose wobjCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int refFrame = 0;
        rtn = robot.GetWObjCoordWithID(id, ref wobjCoord, ref refFrame);
        Console.WriteLine("GetWObjCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, refFrame={7}",
            id, wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz, refFrame);

        // GetExToolCoordWithID
        DescPose extoolCoord = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose exworkpieceCoord = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.GetExToolCoordWithID(21, ref extoolCoord, ref exworkpieceCoord);
        Console.WriteLine("GetExToolCoordWithID 21, {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);
        Console.WriteLine("  tcoord: {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            exworkpieceCoord.tran.x, exworkpieceCoord.tran.y, exworkpieceCoord.tran.z,
            exworkpieceCoord.rpy.rx, exworkpieceCoord.rpy.ry, exworkpieceCoord.rpy.rz);

        // GetExAxisCoordWithID
        DescPose exAxisCoord = new DescPose(0, 0, 0, 0, 0, 0);
        int axisCoordNum = 0, calibFlag = 0;
        rtn = robot.GetExAxisCoordWithID(id, ref exAxisCoord, ref axisCoordNum, ref calibFlag);
        Console.WriteLine("GetExAxisCoordWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3} {5:F3} {6:F3}, axisCoordNum={7}, calibFlag={8}",
            id, exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz, axisCoordNum, calibFlag);

        // GetTargetPayloadWithID
        double weight = 0.0;
        DescTran cog = new DescTran(0, 0, 0);
        rtn = robot.GetTargetPayloadWithID(id, ref weight, ref cog);
        Console.WriteLine("GetTargetPayloadWithID {0}, {1:F3} {2:F3} {3:F3} {4:F3}",
            id, weight, cog.x, cog.y, cog.z);

        // GetCurToolCoord
        rtn = robot.GetCurToolCoord(ref toolCoord);
        Console.WriteLine("GetCurToolCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz);

        // GetCurWObjCoord
        rtn = robot.GetCurWObjCoord(ref wobjCoord);
        Console.WriteLine("GetCurWObjCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz);

        // GetCurExToolCoord
        rtn = robot.GetCurExToolCoord(ref extoolCoord);
        Console.WriteLine("GetCurExToolCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);

        // GetCurExAxisCoord
        rtn = robot.GetCurExAxisCoord(ref exAxisCoord);
        Console.WriteLine("GetCurExAxisCoord {0:F3} {1:F3} {2:F3} {3:F3} {4:F3} {5:F3}",
            exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz);

        // GetTargetPayload / GetTargetPayloadCog
        double weightT = 0.0;
        DescTran cogT = new DescTran(0, 0, 0);
        robot.GetTargetPayload(0, ref weightT);
        robot.GetTargetPayloadCog(0, ref cogT);
        Console.WriteLine("GetTargetPayload {0:F3} {1:F3} {2:F3} {3:F3}",
            weightT, cogT.x, cogT.y, cogT.z);

        // SetToolCoord
        DescPose coordSet = new DescPose(0, 1, 2, 3, 4, 5);
        rtn = robot.SetToolCoord(1, coordSet, 0, 0, 1, 0);
        Console.WriteLine("SetToolCoord(1) rtn={0}", rtn);

        // SetWObjCoord
        rtn = robot.SetWObjCoord(1, coordSet, 0);
        Console.WriteLine("SetWObjCoord(1) rtn={0}", rtn);

        // SetLoadWeight + SetLoadCoord
        rtn = robot.SetLoadWeight(1, 1.3f);
        Console.WriteLine("SetLoadWeight(1,1.3) rtn={0}", rtn);

        DescTran loadCog = new DescTran(10, 20, 30);
        rtn = robot.SetLoadCoord(1, loadCog);
        Console.WriteLine("SetLoadCoord(1,10,20,30) rtn={0}", rtn);

        // SetExToolCoord
        DescPose etcp = new DescPose(0, 0, 100, 0, 0, 0);
        DescPose etool = new DescPose(0, 0, 50, 0, 0, 0);
        rtn = robot.SetExToolCoord(21, etcp, etool);
        Console.WriteLine("SetExToolCoord(21) rtn={0}", rtn);
        // SetExToolList
        rtn = robot.SetExToolList(21, etcp, etool);
        Console.WriteLine("SetExToolList(21) rtn={0}", rtn);

        // ExtAxisActiveECoordSys
        rtn = robot.ExtAxisActiveECoordSys(1, 1, coordSet, 1);
        Console.WriteLine("ExtAxisActiveECoordSys(1,1,..,1) rtn={0}", rtn);

        return 0;
    }






