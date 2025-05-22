機器人力控
============

.. toctree:: 
    :maxdepth: 5

力感測器配置
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置力感測器
    * @param  [in] company  力傳感器廠商，17-坤維科技
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int FT_SetConfig(int company, int device, int softvesion, int bus); 

取得力傳感器配置 
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 取得力傳感器配置 
    * @param [out] deviceID 力傳感器編號 
    * @param [out] company 力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI 傳感器，21-中科米點，22-伟航敏芯
    * @param [out] device  設備號，坤維(0-KWR75B)，航太十一院(0-MCS6A-200-4)，ATI (0-AXIA80 -M8)，中科米點(0-MST2010)，偉航敏芯(0 -WHC6L-YB-10A)
    * @param [out] softvesion 軟體版本號，暫不使用，預設為 0 
    * @return 錯誤碼 
    */ 
    int FT_GetConfig(ref int deviceID, ref int company, ref int device, ref int softvesion); 

力傳感器激活
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力傳感器激活
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    int FT_Activate(byte act); 

力傳感器校零
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  力傳感器校零
    * @param  [in] act  0-去除零點，1-零點矯正
    * @return  錯誤碼
    */
    int FT_SetZero(byte act); 

代碼範例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFT_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        byte act = 0;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        company = 0;
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config : {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(act);
        Thread.Sleep(1000);
        act = 1;
        robot.FT_Activate(act);
        Thread.Sleep(1000);

        robot.SetLoadWeight(0.0f);
        Thread.Sleep(1000);
        DescTran coord = new DescTran(0, 0, 0);
                
        robot.SetLoadCoord(coord);
        Thread.Sleep(1000);
        robot.FT_SetZero(0);//0去除零點  1零點矫正
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        int rtn = robot.FT_GetForceTorqueOrigin(1, ref ft);
        Console.WriteLine($"ft origin : {ft.fx}, {ft.fy}, { ft.fz}, { ft.tx}, { ft.ty}, { ft.tz}    rtn   {rtn}");
        rtn = robot.FT_SetZero(1);//零點矫正
        //Console.WriteLine($"set zero rtn {rtn}");

        Thread.Sleep(2000);
        rtn = robot.FT_GetForceTorqueOrigin(1, ref ft);
        Console.WriteLine($"ft rcs : {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}  rtn  {rtn}");

        robot.FT_GetForceTorqueRCS(1, ref ft);
        Console.WriteLine($"FT_GetForceTorqueRCS rcs : {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}");
    }

設定力傳感器參考座標系
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定力傳感器參考座標系
    * @param  [in] ref  0-工具座標系，1-基坐標系
    * @return  錯誤碼
    */
    int FT_SetRCS(byte type); 

負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id   傳感器座標系編號，範圍[1~14]
    * @return  錯誤碼
    */
    int FT_PdIdenRecord(int id);

負載重量辨識計算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  負載重量辨識計算
    * @param  [out] weight  負載重量，單位kg
    * @return  錯誤碼
    */   
    int FT_PdIdenCompute(ref double weight);

負載質心辨識記錄
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  負載質心辨識記錄
    * @param  [in] id   傳感器座標系編號，範圍[1~14]
    * @param  [in] index 點編號，範圍[1~3]
    * @return  錯誤碼
    */
    int FT_PdCogIdenRecord(int id, int index); 

負載質心辨識計算
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  負載質心辨識計算
    * @param  [out] cog  負載質心，單位mm
    * @return  錯誤碼
    */   
    int FT_PdCogIdenCompute(ref DescTran cog);

代碼範例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTPdCog_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        double weight = 0.1;
        int rtn = -1;
        DescPose tcoord, desc_p1, desc_p2, desc_p3;
        tcoord = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.FT_SetRCS(0);
        Thread.Sleep(1000);

        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, tcoord, 1, 0);
        Thread.Sleep(1000);
        robot.FT_PdIdenRecord(10);
        Thread.Sleep(1000);
        robot.FT_PdIdenCompute(ref weight);
        Console.WriteLine($"payload weight : {weight}");

        desc_p1.tran.x = -47.805;
        desc_p1.tran.y = -362.266;
        desc_p1.tran.z = 317.754;
        desc_p1.rpy.rx = -179.496;
        desc_p1.rpy.ry = -0.255;
        desc_p1.rpy.rz = 34.948;

        desc_p2.tran.x = -77.805;
        desc_p2.tran.y = -312.266;
        desc_p2.tran.z = 317.754;
        desc_p2.rpy.rx = -179.496;
        desc_p2.rpy.ry = -0.255;
        desc_p2.rpy.rz = 34.948;

        desc_p3.tran.x = -167.805;
        desc_p3.tran.y = -312.266;
        desc_p3.tran.z = 387.754;
        desc_p3.rpy.rx = -179.496;
        desc_p3.rpy.ry = -0.255;
        desc_p3.rpy.rz = 34.948;

        rtn = robot.MoveCart(desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Console.WriteLine($"MoveCart rtn  {rtn}");
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);
        Thread.Sleep(1000);
        DescTran cog = new DescTran(0, 0, 0);

        robot.FT_PdCogIdenCompute(ref cog);
        Console.WriteLine($"cog : {cog.x}, {cog.y}, {cog.z}");
    }

取得參考坐標系下力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得參考坐標系下力/扭力數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueRCS(byte flag, ref ForceTorque ft); 

取得力傳感器原始力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  取得力傳感器原始力/扭力數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueOrigin(byte flag, ref ForceTorque ft); 

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  碰撞守護
    * @param  [in] flag 0-關閉碰撞守護，1-開啟碰撞守護
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否偵測碰撞，0-不偵測，1-偵測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大閾值
    * @param  [in] min_threshold 最小閾值
    * @note   力/扭力檢測範圍：(ft-min_threshold, ft+max_threshold)
    * @return  錯誤碼
    */   
    int FT_Guard(int flag, int sensor_id, int[] select, ForceTorque ft, double[] max_threshold, double[] min_threshold); 

代碼範例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTGuard_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        byte sensor_id = 1;
        int[] select = new int[6]{ 1, 0, 0, 0, 0, 0 };//只啟用x軸碰撞守護
        double[] max_threshold = new double[6]{ 5.0f, 0.01f, 0.01f, 0.01f, 0.01f, 0.01f };
        double[] min_threshold = new double[6]{ 3.0f, 0.01f, 0.01f, 0.01f, 0.01f, 0.01f };

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        DescPose desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;

        desc_p3.tran.x = 157.233;
        desc_p3.tran.y = -550.088;
        desc_p3.tran.z = 112.485;
        desc_p3.rpy.rx = -176.579;
        desc_p3.rpy.ry = -2.819;
        desc_p3.rpy.rz = -148.415;
        robot.SetSpeed(5);

        int rtn =  robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        Console.WriteLine($"FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 1, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        flag = 0;
        rtn = robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        Console.WriteLine($"FT_Guard end rtn {rtn}");
    }

恆力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恆力控制
    * @param  [in] flag 0-關閉恆力控制，1-開啟恆力控制
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否偵測碰撞，0-不偵測，1-偵測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid參數，力矩pid參數
    * @param  [in] adj_sign 自適應啟動停止控制，0-關閉，1-開啟
    * @param  [in] ILC_sign ILC啟停控制， 0-停止，1-訓練，2-實操
    * @param  [in] 最大調整距離，單位mm
    * @param  [in] 最大調整角度，單位deg
    * @return  錯誤碼
    */   
    int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang);   

代碼範例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTConttol_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        byte sensor_id = 1;
        int[] select = new int[6]{ 0, 0, 1, 0, 0, 0 };
        double[] ft_pid = new double[6]{ 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;

        ForceTorque ft = new ForceTorque(0, 0, 0, 0 ,0 ,0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1, j2;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        j2 = new JointPos(0, 0, 0, 0, 0, 0);
        j1 = new JointPos(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;
        ft.fz = -10.0;

        robot.GetInverseKin(0, desc_p1, -1, ref j1);
        robot.GetInverseKin(0, desc_p2, -1, ref j2);

        robot.MoveJ(j1, desc_p1, 1, 0, 100.0f, 180.0f, 100.0f, epos, -1.0f, 0, offset_pos);
        int rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        Console.WriteLine($"FT_Control start rtn {rtn}");

        robot.MoveL(j2, desc_p2, 1, 0, 100.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos);
        flag = 0;
        rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        Console.WriteLine($"FT_Control end rtn {rtn}");
    }

柔順控制開啟
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔順控制開啟
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啟力閾值，單位N
    * @return  錯誤碼
    */   
    int FT_ComplianceStart(float p, float force);

柔順控制關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔順控制關閉
    * @return  錯誤碼
    */   
    int FT_ComplianceStop(); 

代碼範例
+++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnComplience_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        byte flag = 1;
        int sensor_id = 1;
        int[] select = new int[6]{ 1, 1, 1, 0, 0, 0 };
        double[] ft_pid = new double[6] { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1, j2;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        j2 = new JointPos(0, 0, 0, 0, 0, 0);
        j1 = new JointPos(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = 1.299;
        desc_p1.tran.y = -719.159;
        desc_p1.tran.z = 141.314;
        desc_p1.rpy.rx = 177.999;
        desc_p1.rpy.ry = -0.715;
        desc_p1.rpy.rz = -161.937;

        desc_p2.tran.x = 245.047;
        desc_p2.tran.y = -675.509;
        desc_p2.tran.z = 139.538;
        desc_p2.rpy.rx = 177.987;
        desc_p2.rpy.ry = -0.129;
        desc_p2.rpy.rz = -142.238;
        ft.fz = -10.0;

        robot.GetInverseKin(0, desc_p1, -1, ref j1);
        robot.GetInverseKin(0, desc_p2, -1, ref j2);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        float p = 0.00005f;
        float force = 30.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        Console.WriteLine($"FT_ComplianceStart rtn {rtn}");
        int count = 15;
        while (count > 0)
        {
            robot.MoveL(j1, desc_p1, 1, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 1, offset_pos);
            robot.MoveL(j2, desc_p2, 1, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 0, offset_pos);
            count -= 1;
        }
        rtn = robot.FT_ComplianceStop();
        Console.WriteLine($"FT_ComplianceStop rtn {rtn}");
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
    }

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 負載辨識初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynFilterInit();

負載辨識變數初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 負載辨識變數初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynVarInit();

負荷辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 負荷辨識主程序
    * @param [in] joint_torque 關節扭矩
    * @param [in] joint_pos 關節位置
    * @param [in] t 採樣週期
    * @return 錯誤碼
    */
    int LoadIdentifyMain(double[] joint_torque, double[] joint_pos, double t);

獲取負荷辨識結果
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取負荷辨識結果
    * @param [in] gain  重力項係數double[6]，離心項係數double[6]
    * @param [out] weight 負載重量
    * @param [out] cog 負載質心
    * @return 錯誤碼
    */
    int LoadIdentifyGetResult(double[] gain, ref double weight, ref DescTran cog);

力道感測器輔助拖曳
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 力道感應器輔助拖曳
 * @param [in] status 控制狀態，0-關閉；1-開啟
 * @param [in] asaptiveFlag 自適應開啟標誌，0-關閉；1-開啟
 * @param [in] interfereDragFlag 干涉區拖曳標誌，0-關閉；1-開啟
 * @param [in] ingularityConstraintsFlag 奇異點策略：0-規避；1-穿越
 * @param [in] M 慣性係數
 * @param [in] B 阻尼係數
 * @param [in] K 剛度係數
 * @param [in] F 拖曳六維力閾值
 * @param [in] Fmax 最大拖曳限制 Nm
 * @param [in] Vmax 最大關節速度限制 °/s
 * @return 錯誤碼
 */
 int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);

取得力道感測器拖曳開關狀態
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得力感應器拖曳開關狀態
 * @param [out] dragState 力傳感器輔助拖曳控制狀態，0-關閉；1-開啟
 * @param [out] sixDimensionalDragState 六維力輔助拖曳控制狀態，0-關閉；1-開啟
 * @return 錯誤碼
 */
 int GetForceAndTorqueDragState(ref int dragState, ref int sixDimensionalDragState);

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 力傳感器自動校零
 * @param [out] weight 感測器質量 kg
 * @param [out] pos 感測器質心 mm
 * @return 錯誤碼
 */
 int ForceSensorAutoComputeLoad(ref double weight, ref DescTran pos);

設定六維力和關節阻抗混合拖曳開關及參數
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定六維力和關節阻抗混合拖曳開關及參數
 * @param [in] status 控制狀態，0-關閉；1-開啟
 * @param [in] impedanceFlag 阻抗開啟標誌，0-關閉；1-開啟
 * @param [in] lamdeDain 拖曳增益
 * @param [in] KGain 剛度增益
 * @param [in] BGain 阻尼增益
 * @param [in] dragMaxTcpVel 拖曳末端最大線速度限制
 * @param [in] dragMaxTcpOriVel 拖曳末端最大角速度限制
 * @return 錯誤碼
 */
 int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, double[] lamdeDain, double[] KGain, double[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);


設定力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定力道感測器下負載重量
 * @param [in] weight 負載重量 kg
 * @return 錯誤碼
 */
 int SetForceSensorPayLoad(double weight);

設定力道感測器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定力道感測器下負載質心
 * @param [in] x 負載質心x mm
 * @param [in] y 負載質心y mm
 * @param [in] z 負載質心z mm
 * @return 錯誤碼
 */
 int SetForceSensorPayLoadCog(double x, double y, double z);

取得力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得力傳感器下負載重量
 * @param [in] weight 負載重量 kg
 * @return 錯誤碼
 */
 int GetForceSensorPayLoad(ref double weight);

取得力道感測器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得力感測器下負載質心
 * @param [out] x 負載質心x mm
 * @param [out] y 負載質心y mm
 * @param [out] z 負載質心z mm
 * @return 錯誤碼
 */
 int GetForceSensorPayLoadCog(ref double x, ref double y, ref double z);
 
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

代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button3_Click(object sender, EventArgs e)
    {

        // 禁用按鈕防止重複點擊
        button3.Enabled = false;

        // 在後台線程中執行耗時操作
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
