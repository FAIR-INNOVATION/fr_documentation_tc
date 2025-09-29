機器人力控
============

.. toctree:: 
    :maxdepth: 5

力傳感器配置
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  配置力傳感器
    * @param  [in] company  力傳感器廠商，17-坤維科技
    * @param  [in] device  設備號，暫不使用，默認爲0
    * @param  [in] softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int FT_SetConfig(int company, int device, int softvesion, int bus); 

獲取力傳感器配置 
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 獲取力傳感器配置 
    * @param [out] deviceID 力傳感器編號 
    * @param [out] company 力傳感器廠商，，力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI傳感器，21-中科米點，22-偉航敏芯
    * @param [out] device  設備號，坤維(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI (0-AXIA80 -M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A) 
    * @param [out] softvesion 軟件版本號，暫不使用，默認爲 0 
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

設置力傳感器參考座標系
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置力傳感器參考座標系
    * @param  [in] ref  0-工具座標系，1-基座標系
    * @return  錯誤碼
    */
    int FT_SetRCS(byte type); 

設置力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  設置力傳感器下負載重量
    * @param  [in] weight 負載重量 kg
    * @return  錯誤碼
    */
    int SetForceSensorPayLoad(double weight);

設置力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  設置力傳感器下負載質心
    * @param  [in] x 負載質心x mm 
    * @param  [in] y 負載質心y mm
    * @param  [in] z 負載質心z mm
    * @return  錯誤碼
    */
    int SetForceSensorPayLoadCog(double x, double y, double z);

獲取力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取力傳感器下負載重量
    * @param  [in] weight 負載重量 kg
    * @return  錯誤碼
    */
    int GetForceSensorPayLoad(ref double weight);

獲取力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取力傳感器下負載質心
    * @param  [out] x 負載質心x mm 
    * @param  [out] y 負載質心y mm
    * @param  [out] z 負載質心z mm
    * @return  錯誤碼
    */
    int GetForceSensorPayLoadCog(ref double x, ref double y, ref double z);

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  力傳感器自動校零
    * @param  [out] weight 傳感器質量 kg 
    * @param  [out] pos 傳感器質心 mm
    * @return  錯誤碼
    */
    int ForceSensorAutoComputeLoad(ref double weight, ref DescTran pos);

獲取參考座標系下力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取參考座標系下力/扭矩數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueRCS(byte flag, ref ForceTorque ft); 

獲取力傳感器原始力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取力傳感器原始力/扭矩數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueOrigin(byte flag, ref ForceTorque ft); 

力傳感器配置及自動校零代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button54_Click(object sender, EventArgs e)
    {
        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0, 0, 0, 0, 0, 0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin:{ft.fx},{ft.fy},{ft.fz},{ft.tx},{ft.ty},{ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose ftCoord = new DescPose(0, 0, 0, 0, 0, 0);
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayLoad(0.824);
        robot.SetForceSensorPayLoadCog(0.778, 2.554, 48.765);
        double weight = 0;
        double x = 0, y = 0, z = 0;
        robot.GetForceSensorPayLoad(ref weight);
        robot.GetForceSensorPayLoadCog(ref x, ref y, ref z);
        Console.WriteLine($"the FT load is {weight}, {x} {y} {z}");

        robot.SetForceSensorPayLoad(0);
        robot.SetForceSensorPayLoadCog(0, 0, 0);

        double computeWeight = 0;
        DescTran tran = new DescTran(0, 0, 0);
        robot.ForceSensorAutoComputeLoad(ref weight, ref tran);
        Console.WriteLine($"the result is weight {weight} pos is {tran.x} {tran.y} {tran.z}");

    } 

負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
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
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
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

力傳感器負載辨識代碼示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTPdCog_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        ForceTorque ft = new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ref ft);
        Console.WriteLine($"ft origin: {ft.fx}, {ft.fy}, {ft.fz}, {ft.tx}, {ft.ty}, {ft.tz}");
        robot.FT_SetZero(1);
        Thread.Sleep(1000);

        DescPose tcoord = new DescPose(0, 0, 35.0, 0, 0, 0);
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        Thread.Sleep(1000);

        double weight = 0.0f;
        robot.FT_PdIdenCompute(ref weight);
        Console.WriteLine($"payload weight: {weight}");

        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        Thread.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);

        DescTran cog = new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(ref cog);
        Console.WriteLine($"cog: {cog.x}, {cog.y}, {cog.z}");
    }

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  碰撞守護
    * @param  [in] flag 0-關閉碰撞守護，1-開啓碰撞守護
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否檢測碰撞，0-不檢測，1-檢測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大閾值
    * @param  [in] min_threshold 最小閾值
    * @note   力/扭矩檢測範圍：(ft-min_threshold, ft+max_threshold)
    * @return  錯誤碼
    */   
    int FT_Guard(int flag, int sensor_id, int[] select, ForceTorque ft, double[] max_threshold, double[] min_threshold); 

碰撞守護代碼示例
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTGuard_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;

        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte sensor_id = 1;
        int[] select = { 1, 1, 1, 1, 1, 1 };
        double[] max_threshold = { 10.0f, 10.0f, 10.0f, 10.0f, 10.0f, 10.0f };
        double[] min_threshold = { 5.0f, 5.0f, 5.0f, 5.0f, 5.0f, 5.0f };

        ForceTorque ft = new ForceTorque();
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.FT_Guard(1, sensor_id, select,  ft, max_threshold, min_threshold);
        robot.MoveCart( desc_p1, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p2, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart( desc_p3, 0, 0, 100.0f, 100.0f, 100.0f, -1.0f, -1);

        robot.FT_Guard(0, sensor_id, select, ft, max_threshold, min_threshold);
    }

恆力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  恆力控制
    * @param  [in] flag 0-關閉恆力控制，1-開啓恆力控制
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否檢測碰撞，0-不檢測，1-檢測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid參數，力矩pid參數
    * @param  [in] adj_sign 自適應啓停控制，0-關閉，1-開啓
    * @param  [in] ILC_sign ILC啓停控制， 0-停止，1-訓練，2-實操
    * @param  [in] 最大調整距離，單位mm
    * @param  [in] 最大調整角度，單位deg
    * @return  錯誤碼
    */   
    int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang);   

恆力控制代碼示例
+++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnFTConttol_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte sensor_id = 1;
        int[] select = { 0, 0, 1, 0, 0, 0 };
        double[] ft_pid = { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0, ILC_sign = 0;
        float max_dis = 100.0f, max_ang = 0.0f;

        ForceTorque ft = new ForceTorque( 0.0, 0.0, -10.0, 0.0, 0.0, 0.0 );
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.MoveJ( j1,  desc_p1, 0, 0, 100.0f, 180.0f, 100.0f,  epos, -1.0f, 0,  offset_pos);
        robot.FT_Control(1, sensor_id, select,  ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        rtn = robot.MoveJ(j2, desc_p2, 0, 0, 100.0f, 180.0f, 100.0f, epos, -1.0f, 0, offset_pos);
        robot.FT_Control(0, sensor_id, select,  ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
    }

柔順控制開啓
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  柔順控制開啓
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啓力閾值，單位N
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

柔順控制代碼示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnComplience_Click(object sender, EventArgs e)
    {
        int company = 24, device = 0, softversion = 0, bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config: {company}, {device}, {softversion}, {bus}");
        Thread.Sleep(1000);

        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);

        robot.FT_SetZero(0);
        Thread.Sleep(1000);

        byte flag = 1;
        int sensor_id = 1;
        int[] select = { 1, 1, 1, 0, 0, 0 };
        double[] ft_pid = { 0.0005f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        byte adj_sign = 0, ILC_sign = 0;
        float max_dis = 100.0f, max_ang = 0.0f;

        ForceTorque ft = new ForceTorque { fx = -10.0, fy = -10.0, fz = -10.0 };
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        float p = 0.00005f;
        float force = 30.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        Console.WriteLine($"FT_ComplianceStart rtn is {rtn}");

        int count = 5;
        while (count-- > 0)
        {
        robot.MoveL(j1, desc_p1, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 1, offset_pos);
        robot.MoveL(j2, desc_p2, 0, 0, 100.0f, 180.0f, 100.0f, -1.0f, epos, 0, 0, offset_pos);
        }

        robot.FT_ComplianceStop();
        Console.WriteLine($"FT_ComplianceStop rtn is {rtn}");

        flag = 0;
        robot.FT_Control(flag, (byte)sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
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

負載辨識變量初始化
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 負載辨識變量初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynVarInit();

負載辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 負載辨識主程序
    * @param [in] joint_torque 關節扭矩
    * @param [in] joint_pos 關節位置
    * @param [in] t 採樣週期
    * @return 錯誤碼
    */
    int LoadIdentifyMain(double[] joint_torque, double[] joint_pos, double t);

獲取負載辨識結果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取負載辨識結果
    * @param [in] gain  重力項係數double[6]，離心項係數double[6]
    * @param [out] weight 負載重量
    * @param [out] cog 負載質心
    * @return 錯誤碼
    */
    int LoadIdentifyGetResult(double[] gain, ref double weight, ref DescTran cog);

機器人負載辨識代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button74_Click(object sender, EventArgs e)
    {
        int rtn;
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();
        Console.WriteLine("LoadIdentifyDynFilterInit retval is: " + retval);

        retval = robot.LoadIdentifyDynVarInit();
        Console.WriteLine("LoadIdentifyDynVarInit retval is: " + retval);

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0, 0, 0, 0, 0, 0);
        double[] joint_toq = new double[6] { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        robot.GetActualJointPosDegree(0, ref posJ);
        posJ.jPos[1] = posJ.jPos[1] + 10;
        robot.GetJointTorques(0, joint_toq);
        joint_toq[1] = joint_toq[1] + 2;

        double[] tmpTorque = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        for (int i = 0; i < 6; i++)
        {
            tmpTorque[i] = joint_toq[i];
        }

        retval = robot.LoadIdentifyMain(tmpTorque, posJ.jPos, 1);
        Console.WriteLine("LoadIdentifyMain retval is: " + retval);

        double[] gain = new double[12] { 0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0 };
        double weight = 0;
        DescTran load_pos = new DescTran(0, 0, 0);
        retval = robot.LoadIdentifyGetResult(gain, ref weight, ref load_pos);
        Console.WriteLine("LoadIdentifyGetResult retval is: {0}; weight is {1} cog is {2} {3} {4}", retval, weight, load_pos.x, load_pos.y, load_pos.z);
    }

力傳感器輔助拖動
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  力傳感器輔助拖動
    * @param  [in] status 控制狀態，0-關閉；1-開啓
    * @param  [in] asaptiveFlag 自適應開啓標誌，0-關閉；1-開啓
    * @param  [in] interfereDragFlag 干涉區拖動標誌，0-關閉；1-開啓
    * @param  [in] ingularityConstraintsFlag 奇異點策略，0-規避；1-穿越
    * @param  [in] forceCollisionFlag 輔助拖動時機器人碰撞檢測標誌；0-關閉；1-開啓
    * @param  [in] M 慣性系數
    * @param  [in] B 阻尼係數
    * @param  [in] K 剛度係數
    * @param  [in] F 拖動六維力閾值
    * @param  [in] Fmax 最大拖動力限制 Nm
    * @param  [in] Vmax 最大關節速度限制 °/s
    * @return  錯誤碼
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag,int forceCollisionFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);
    
獲取力傳感器拖動開關狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取力傳感器拖動開關狀態
    * @param  [out] dragState 力傳感器輔助拖動控制狀態，0-關閉；1-開啓
    * @param  [out] sixDimensionalDragState 六維力輔助拖動控制狀態，0-關閉；1-開啓
    * @return  錯誤碼
    */
    int GetForceAndTorqueDragState(ref int dragState, ref int sixDimensionalDragState);

報錯清除後力傳感器自動開啓
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  報錯清除後力傳感器自動開啓
    * @param  [in] status 控制狀態，0-關閉；1-開啓
    * @return  錯誤碼
    */
    int SetForceSensorDragAutoFlag(int status);

力傳感器輔助拖動代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button61_Click(object sender, EventArgs e)
    {
        robot.SetForceSensorDragAutoFlag(1);
        double[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        double[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        double[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };

        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);
        robot.WaitMs(5000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        robot.GetForceAndTorqueDragState(ref dragState, ref sixDimensionalDragState);
        Console.WriteLine($"the drag state is {dragState} {sixDimensionalDragState}");

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
    }

設置六維力和關節阻抗混合拖動開關及參數
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  設置六維力和關節阻抗混合拖動開關及參數
    * @param  [in] status 控制狀態，0-關閉；1-開啓
    * @param  [in] impedanceFlag 阻抗開啓標誌，0-關閉；1-開啓
    * @param  [in] lamdeDain 拖動增益
    * @param  [in] KGain 剛度增益
    * @param  [in] BGain 阻尼增益
    * @param  [in] dragMaxTcpVel 拖動末端最大線速度限制
    * @param  [in] dragMaxTcpOriVel 拖動末端最大角速度限制
    * @return  錯誤碼
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, double[] lamdeDain, double[] KGain, double[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

力傳感器輔助拖動代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button62_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        double[] lambdaGain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        double[] kGain = { 0, 0, 0, 0, 0, 0 };
        double[] bGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
        Thread.Sleep(5000); 
        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lambdaGain, kGain, bGain, 1000, 180);
        Console.WriteLine($"ForceAndJointImpedanceStartStop rtn is {rtn}");
    }

設置焊絲尋位擴展IO端口
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊絲尋位擴展IO端口
    * @param searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param searchStartDONum 焊絲尋位啓停控制DO端口(0-127)
    * @return 錯誤碼
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

阻抗啓停控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
    * @brief 阻抗啓停控制
    * @param [in] status 0：關閉；1-開啓
    * @param [in] workSpace 0-關節空間；1-迪卡爾空間
    * @param [in] forceThreshold 觸發力閾值(N)
    * @param [in] m 質量參數
    * @param [in] b 阻尼參數
    * @param [in] k 剛度參數
    * @param [in] maxV 最大線速度(mm/s)
    * @param [in] maxVA 最大線加速度(mm/s2)
    * @param [in] maxW 最大角速度(°/s)
    * @param [in] maxWA 最大角加速度(°/s2)
    * @return 錯誤碼
    */
    public int ImpedanceControlStartStop(int status, int workSpace, double[] forceThreshold, double[] m, double[] b, double[] k, double maxV, double maxVA, double maxW, double maxWA)

機器人阻抗啓停控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestImpedanceControl()
    { 
        int[] ctrl = new int[20];
        int state;
        int pressValue;
        int error;
        int rtn;
        JointPos j1 = new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2 = new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1 = new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2 = new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
    
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
    
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 200.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendR = -1.0f;
    
        byte flag = 0;
    
        byte search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        robot.FT_SetConfig(company, device, softversion, bus);
        Thread.Sleep(1000);
        robot.FT_GetConfig(ref company, ref device, ref softversion, ref bus);
        Console.WriteLine($"FT config:{company},{device},{softversion},{bus}");
        Thread.Sleep(1000);
    
        robot.FT_Activate(0);
        Thread.Sleep(1000);
        robot.FT_Activate(1);
        Thread.Sleep(1000);
        Thread.Sleep(1000);
        robot.FT_SetZero(0);
        Thread.Sleep(1000);
        robot.FT_SetZero(1);
        Thread.Sleep(1000);
    
        double[] forceThreshold = new double[] { 30, 30, 30, 5, 5, 5 };
        double[] m = new double[] { 0.1, 0.1, 0.1, 0.02, 0.02, 0.02 };
        double[] b = new double[] { 1, 1, 1, 0.08, 0.08, 0.08 };
        double[] k = new double[] { 0, 0, 0, 0, 0, 0 };
        rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        Console.WriteLine($"ImpedanceControlStartStop errcode:{rtn}");
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1, 0);
        Console.WriteLine($"movel errcode:{rtn}");
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
    }
















