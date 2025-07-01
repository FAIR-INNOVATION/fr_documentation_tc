機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

取得機器人安裝角度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得機器人安裝角度
    * @param  [out] yangle 傾斜角
    * @param  [out] zangle 旋轉角
    * @return  錯誤碼
    */
    int GetRobotInstallAngle(ref double yangle, ref double zangle); 

取得系統變數值
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得系統變數值
    * @param  [in] id 系統變數編號，範圍[1~20]
    * @param  [out] value  系統變數值
    * @return  錯誤碼
    */
    int GetSysVarValue(int id, ref double value); 

取得目前關節位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前關節位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位deg
    * @return  錯誤碼
    */
    int GetActualJointPosDegree(byte flag, ref JointPos jPos); 

取得目前關節位置(弧度)
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前關節位置(弧度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位rad
    * @return  錯誤碼
    */   
    int GetActualJointPosRadian(byte flag, ref JointPos jPos);

取得關節回饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得關節回饋速度-deg/s 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed 六個關節速度 
    * @return 錯誤碼 
    */
    int GetActualJointSpeedsDegree(byte flag, ref double[] speed);

取得關節回饋加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得關節回饋加速度-deg/s^2 
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] acc 六個關節加速度 
    * @return 錯誤碼 
    */
    int GetActualJointAccDegree(byte flag, ref double[] acc); 

取得TCP指令速度-合速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得TCP指令速度-合速度 
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

取得TCP指令速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得TCP指令速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 錯誤碼 
    */
    int GetTargetTCPSpeed(byte flag, ref double[] speed);

取得TCP回饋速度-分速度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得TCP回饋速度-分速度
    * @param [in] flag 0-阻塞，1-非阻塞 
    * @param [out] speed [x,y,z,rx,ry,rz]速度 
    * @return 錯誤碼 
    */
    int GetActualTCPSpeed(byte flag, ref double[] speed);

取得當前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得當前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    int GetActualTCPPose(byte flag, ref DescPose desc_pos); 

取得目前工具坐標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前工具坐標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具座標系編號
    * @return  錯誤碼
    */
    int GetActualTCPNum(byte flag, ref int id);  

取得目前工件坐標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前工件坐標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件座標系編號
    * @return  錯誤碼
    */
    int GetActualWObjNum(byte flag, ref int id);

取得目前末端法蘭位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前末端法蘭位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法蘭位姿
    * @return  錯誤碼
    */
    int GetActualToolFlangePose(byte flag, ref DescPose desc_pos);   

逆運動學求解
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] config 關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos);

逆運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置求解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */   
    int GetInverseKin(int type, DescPose desc_pos, int config, ref JointPos joint_pos); 

逆運動學求解（參考指定關節位置）
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判断是否有解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] result 0-無解，1-有解
    * @return  錯誤碼
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, ref JointPos joint_pos); 

判斷逆運動學是否有解
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 逆運動學求解，判斷指定參考關節位置是否有解
    * @param [in] posMode 0絕對位姿，1相對位姿-基座標系，2相對位姿-工具坐標系 
    * @param [in] desc_pos 笛卡兒位姿 
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
    * @param  [out] desc_pos 笛卡兒位姿
    * @return  錯誤碼
    */
    int GetForwardKin(JointPos joint_pos, ref DescPose desc_pos); 

取得當前關節轉矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 取得當前關節轉矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 關節轉矩
    * @return  錯誤碼
    */
    int GetJointTorques(byte flag, float[] torques); 

取得目前負載的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前負載的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 負載重量，單位kg
    * @return  錯誤碼
    */
    int GetTargetPayload(byte flag, ref double weight); 

取得目前負載的質心
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得目前負載的質心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 負載質心，單位mm
    * @return  錯誤碼
    */   
    int GetTargetPayloadCog(byte flag, ref DescTran cog);

獲取當前工具坐標系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工具坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐標系位姿
    * @return  錯誤碼
    */
    int GetTCPOffset(byte flag, ref DescPose desc_pos); 

取得當前工件坐標系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得當前工件坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件座標系位姿
    * @return  錯誤碼
    */   
    int GetWObjOffset(byte flag, ref DescPose desc_pos); 

取得關節軟限位角度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得關節軟限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞    
    * @param  [out] negative  負限位角度，單位deg
    * @param  [out] positive  正限位角度，單位deg
    * @return  錯誤碼
    */
    int GetJointSoftLimitDeg(byte flag, ref double[] negative, ref double[] positive); 

取得系統時間
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得系統時間
    * @param  [out] t_ms 單位ms
    * @return  錯誤碼
    */
    int GetSystemClock(ref double t_ms);

取得機器人當前關節配置
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得機器人當前關節位置
    * @param  [out]  config  關節空間配置，範圍[0~7]
    * @return  錯誤碼
    */
    int GetRobotCurJointsConfig(ref int config);

取得當前速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得機器人當前速度
    * @param  [out]  vel  速度，單位mm/s
    * @return  錯誤碼
    */   
    int GetDefaultTransVel(ref double vel); 

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

代碼範例
+++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotState_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        double yangle = 0, zangle = 0;
        byte flag = 0;
        JointPos j_deg = new JointPos(0, 0, 0, 0, 0, 0);
        JointPos j_rad = new JointPos(0, 0, 0, 0, 0, 0);
        DescPose tcp, flange, tcp_offset, wobj_offset;
        DescTran cog;
        tcp = new DescPose();
        flange = new DescPose();
        tcp_offset = new DescPose();
        wobj_offset = new DescPose();
        cog = new DescTran();

        int id = 0;
        float[] torques = new float[6] { 0, 0, 0, 0, 0, 0};
        double weight = 0.0;
        double[] neg_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        double[] pos_deg = new double[6] { 0, 0, 0, 0, 0, 0 };
        double t_ms = 0;
        int config = 0;
        double vel = 0;

        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle:{yangle},zangle:{zangle}");

        robot.GetActualJointPosDegree(flag, ref j_deg);
        Console.WriteLine($"joint pos deg:{j_deg.jPos[0]}, {j_deg.jPos[1]}, {j_deg.jPos[2]}, {j_deg.jPos[3]},{j_deg.jPos[4]},{j_deg.jPos[5]}");
        robot.GetActualJointPosRadian(flag, ref j_rad);
        Console.WriteLine($"joint pos rad:{j_rad.jPos[0]}, {j_rad.jPos[1]}, {j_rad.jPos[2]},{j_rad.jPos[3]},{j_rad.jPos[4]},{j_rad.jPos[5]}");

        robot.GetActualTCPPose(flag, ref tcp);
        Console.WriteLine($"tcp pose:{tcp.tran.x}, {tcp.tran.y}, {tcp.tran.z}, {tcp.rpy.rx}, {tcp.rpy.ry},{tcp.rpy.rz}");

        robot.GetActualToolFlangePose(flag, ref flange);
        Console.WriteLine($"flange pose:{flange.tran.x}, {flange.tran.y}, {flange.tran.z}, {flange.rpy.rx},{flange.rpy.ry},{flange.rpy.rz}");

        robot.GetActualTCPNum(flag, ref id);
        Console.WriteLine($"tcp num : {id}");

        robot.GetActualWObjNum(flag, ref id);
        Console.WriteLine($"wobj num : {id}");

        robot.GetJointTorques(flag, torques);
        Console.WriteLine($"torques:{torques[0]},{torques[1]},{torques[2]},{torques[3]},{torques[4]},{torques[5]}");

        robot.GetTargetPayload(flag, ref weight);
        Console.WriteLine($"payload weight : {weight}");

        robot.GetTargetPayloadCog(flag, ref cog);
        Console.WriteLine($"payload cog:{cog.x},{cog.y},{cog.z}");

        robot.GetTCPOffset(flag, ref tcp_offset);
        Console.WriteLine($"tcp offset:{tcp_offset.tran.x}, {tcp_offset.tran.y}, {tcp_offset.tran.z},{tcp_offset.rpy.rx},{tcp_offset.rpy.ry},{tcp_offset.rpy.rz}");

        robot.GetWObjOffset(flag, ref wobj_offset);
        Console.WriteLine($"wobj offset:{wobj_offset.tran.x}, {wobj_offset.tran.y},{wobj_offset.tran.z},{wobj_offset.rpy.rx},{wobj_offset.rpy.ry},{wobj_offset.rpy.rz}");

        robot.GetJointSoftLimitDeg(flag, ref neg_deg, ref pos_deg);
        Console.WriteLine($"neg limit deg:{neg_deg[0]}, {neg_deg[1]}, {neg_deg[2]}, {neg_deg[3]},{neg_deg[4]},{neg_deg[5]}");
        Console.WriteLine($"pos limit deg:{pos_deg[0]}, {pos_deg[1]}, {pos_deg[2]}, {pos_deg[3]},{pos_deg[4]},{pos_deg[5]}");

        robot.GetSystemClock(ref t_ms);
        Console.WriteLine($"system clock : {t_ms}");

        robot.GetRobotCurJointsConfig(ref config);
        Console.WriteLine($"joint config : {config}");

        robot.GetDefaultTransVel(ref vel);
        Console.WriteLine($"trans vel : {vel}");
    }

查詢機器人錯誤碼
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查詢機器人錯誤碼 
    * @param [out] maincode   主錯誤碼
    * @param [out] subcode    子錯誤碼
    * @return 錯誤碼 
    */ 
    int GetRobotErrorCode(ref int maincode, ref int subcode); 

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

代碼範例
+++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotState2_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte robotMotionState = 255;
        robot.GetRobotMotionDone(ref robotMotionState);
        Console.WriteLine($"robotMotionState  {robotMotionState}");

        int mainErrCode = -1;
        int subErrCode = -1;
        robot.GetRobotErrorCode(ref mainErrCode, ref subErrCode);
        Console.WriteLine($"mainErrCode  {mainErrCode}  subErrCode  {subErrCode} ");

        string name = "a1";
        double[] point = new double[6] {0, 0, 0, 0, 0, 0};
        robot.GetRobotTeachingPoint(name, ref point);
        Console.WriteLine($"GetRobotTeachingPoint:{point[0]},{point[1]},{point[2]},{point[3]},{point[4]},{point[5]}");

        int length = -1;
        robot.GetMotionQueueLength(ref length);
        Console.WriteLine($"GetMotionQueueLength  {length}");
    }

取得機器人即時狀態結構體
++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得機器人即時狀態結構體
    * @param [out] pkg 機器人即時狀態結構體 
    * @return 錯誤碼 
    */
    int GetRobotRealTimeState(ref ROBOT_STATE_PKG pkg);

代碼範例
+++++++++++
.. versionadded:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    private void btnGetState_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        ROBOT_STATE_PKG pKG = new ROBOT_STATE_PKG();
        robot.GetRobotRealTimeState(ref pKG);
        Console.WriteLine($"the state is {pKG.main_code}");
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

代碼範例
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

獲取擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取擴展軸座標系
    * @param [out] coord 擴展軸座標系
    * @return 錯誤碼
    */
    int ExtAxisGetCoord(ref DescPose coord);