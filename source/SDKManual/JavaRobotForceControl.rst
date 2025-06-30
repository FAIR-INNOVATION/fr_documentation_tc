機器人力控
============

.. toctree:: 
    :maxdepth: 5

配置力感測器
+++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    /**
    * @brief  配置力感測器
    * @param config company:力感測器廠商，17-坤維科技，19-航太十一院，20-ATI感測器，21-中科米點，22-偉航敏芯，23-NBIT，24-鑫精誠(XJC)，26-NSR
    * @param config device: 設備號，坤維(0-KWR75B)，航太十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10-MST2010)，偉航敏芯(0-WHC6L-YB-10A)， C-6F-D82)，NSR(0-NSR-FTSensorA)
    * @param config softvesion:軟體版本號，暫不使用，預設為0
    * @param config bus:設備掛在末端匯流排位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int FT_SetConfig(DeviceConfig config); 

取得力傳感器配置 
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得力傳感器配置 
    * @param [out] config company:力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI传感器，21-中科米點，22-伟航敏芯
    * @param [out] config device:設備號，坤維(0-KWR75B)，航太十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0 -WHC6L-YB-10A)
    * @param [out] config softvesion:軟體版本號，暫不使用，預設為0
    * @param [out] config bus:設備掛在末端總線位置，暫不使用，預設為0
    * @return 錯誤碼 
    */ 
    int FT_GetConfig(DeviceConfig config); 

力傳感器激活
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力傳感器激活
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    int FT_Activate(int act); 

力傳感器校零
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  力傳感器校零
    * @param  [in] act  0-去除零點，1-零點矯正
    * @return  錯誤碼
    */
    int FT_SetZero(int act); 

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        DeviceConfig config = new DeviceConfig();
        config.company = 24;
        config.device = 0;
        config.softwareVersion = 0;
        config.bus = 0;

        robot.FT_SetConfig(config);
        robot.Sleep(1000);
        config.company = 0;
        robot.FT_GetConfig(config);
        System.out.println("FT config : " + config.company + ", " + config.device + ", " + config.softwareVersion + ", " + config.bus);

        robot.FT_Activate(0);  //复位
        robot.Sleep(2000);

        robot.FT_Activate(1);  //激活
        robot.Sleep(2000);

        robot.FT_SetZero(0);//0去除零點
        robot.Sleep(2000);

        robot.FT_SetZero(1);//1零點矫正
    }

設定力道感測器參考座標系
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定力道感測器參考座標系
    * @param  [in] type  0-工具座標系，1-基坐標系, 2-自由座標系
    * @param  [in] coord  自由座標系值
    * @return  錯誤碼
    */
    int FT_SetRCS(int type, DescPose coord); 

負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id  传感器座標系編號，範圍[1~14]
    * @return  錯誤碼
    */
    int FT_PdIdenRecord(int id);

負載重量辨識計算
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載重量辨識計算
    * @return  List[0]:錯誤碼; List[1] : double weight  負載重量，單位kg
    */   
    List<Number> FT_PdIdenCompute();

負載質心辨識記錄
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載質心辨識記錄
    * @param  [in] id  传感器座標系編號，範圍[1~14]
    * @param  [in] index 點編號，範圍[1~3]
    * @return  錯誤碼
    */
    int FT_PdCogIdenRecord(int id, int index); 

負載質心辨識計算
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載質心辨識計算
    * @param  [out] cog  負載質心，單位mm
    * @return  錯誤碼
    */   
    int FT_PdCogIdenCompute(DescTran cog);

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        DeviceConfig config = new DeviceConfig();
        config.company = 24;
        config.device = 0;
        config.softwareVersion = 0;
        config.bus = 0;

        robot.FT_SetConfig(config);
        robot.Sleep(1000);
        DescPose tcoord, desc_p1, desc_p2, desc_p3;
        tcoord = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p1 = new DescPose(-14.404,-455.283,319.847,-172.935,25.141,-68.097);
        desc_p2 = new DescPose(-107.999,-599.174,285.939,153.472,12.686,-71.284);
        desc_p3 = new DescPose(6.586,-704.897,309.638,178.909,-27.759,-70.479);

        DescPose coord = new DescPose(0, 0 ,0, 1, 0, 0);
        robot.FT_SetRCS(0, coord);
        robot.Sleep(1000);

        tcoord.tran.z = 35.0;
        robot.SetToolCoord(8, tcoord, 1, 0);
        robot.Sleep(1000);
        robot.FT_PdIdenRecord(10);
        robot.Sleep(1000);
        List<Number> rtnArray =  robot.FT_PdIdenCompute();
        System.out.println("payload weight : " + rtnArray.get(1));

        robot.MoveCart(desc_p1, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 1);
        robot.MoveCart(desc_p2, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 2);
        robot.MoveCart(desc_p3, 0, 0, 20.0f, 100.0f, 100.0f, -1.0f, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(2, 3);
        robot.Sleep(1000);

        DescTran rtnCog = new DescTran();
        robot.FT_PdCogIdenCompute(rtnCog);
        System.out.println("cog : " + rtnCog.x + ", " + rtnCog.y + ", " + rtnCog.z);
    }


取得參考坐標系下力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得參考坐標系下力/扭力數據
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueRCS(int flag, ForceTorque ft); 

取得力感測器原始力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得力感測器原始力/扭力數據
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueOrigin(int flag, ForceTorque ft); 

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int FT_Guard(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] max_threshold, Object[] min_threshold); 

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 1, 0, 0, 0, 0, 0 };//只啟用x軸碰撞守護
        Object[] max_threshold = { 5.0, 0.01, 0.01, 0.01, 0.01, 0.01 };
        Object[] min_threshold = { 3.0, 0.01, 0.01, 0.01, 0.01, 0.01 };

        ForceTorque ft = new ForceTorque(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        DescPose  desc_p1, desc_p2, desc_p3;
        desc_p1 = new DescPose(-14.404,-455.283,319.847,-172.935,25.141,-68.097);
        desc_p2 = new DescPose(-107.999,-599.174,285.939,153.472,12.686,-71.284);
        desc_p3 = new DescPose(6.586,-704.897,309.638,178.909,-27.759,-70.479);

        int rtn =  robot.FT_Guard(flag, sensor_id, select, ft, max_threshold, min_threshold);
        System.out.println("FT_Guard start rtn {rtn}");
        robot.MoveCart(desc_p1, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p2, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
        robot.MoveCart(desc_p3, 0, 0, 20, 100.0f, 100.0f, -1.0f, -1);
    }

恆力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @param  [in] max_dis 最大調整距離，單位mm
    * @param  [in] max_ang 最大調整角度，單位deg
    * @param  [in] filter_Sign 濾波開啟標誌 0-關；1-開，默認關閉
    * @param  [in] posAdapt_sign 姿態順應開啟標誌 0-關；1-開，默認關閉
    * @param  [in] isNoBlock 阻塞标志，0-阻塞；1-非阻塞
    * @return  錯誤碼
    */   
    int FT_Control(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang, int filter_Sign, int posAdapt_sign, int isNoBlock);   

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        byte flag = 1;
        byte sensor_id = 8;
        Object[] select = { 0,0,1,0,0,0 };
        Object[] ft_pid = { 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0 };
        byte adj_sign = 0;
        byte ILC_sign = 0;
        float max_dis = 100.0f;
        float max_ang = 0.0f;
        ForceTorque ft = new ForceTorque(0, 0, -10, 0 ,0 ,0);

        JointPos j1=new JointPos(-21.724,-136.814,-59.518,-68.853,89.245,-66.35);
        DescPose desc_p1 = new DescPose(703.996,-391.695,240.708,-178.756,-4.709,-45.447);

        JointPos j2=new JointPos(0.079,-130.285,-71.029,-72.115,88.945,-62.736);
        DescPose desc_p2 = new DescPose(738.755,-102.812,226.704,177.488,2.566,-27.209);

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        //關節空間運動
        robot.MoveL(j1, desc_p1, 0, 0, 40.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos, 0, 100);
        int rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        System.out.println("FT_Control start rtn " + rtn);

        robot.MoveL(j2, desc_p2, 0, 0, 10.0f, 180.0f, 20.0f, -1.0f, epos, 0, 0, offset_pos, 0, 100);
        flag = 0;
        rtn = robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0 ,0);
        System.out.println("FT_Control end rtn " + rtn);
    }

柔順控制開啟
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔順控制開啟
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啟力閾值，單位N
    * @return  錯誤碼
    */   
    int FT_ComplianceStart(double p, double force);

柔順控制關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔順控制關閉
    * @return  錯誤碼
    */   
    int FT_ComplianceStop(); 

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        byte flag = 1;
        int sensor_id = 8;
        Object[] select = { 1, 1, 1, 0, 0, 0 };
        Object[] ft_pid = { 0.0005, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 100.0;
        double max_ang = 0.0;

        ForceTorque ft = new ForceTorque(-10.0, -10.0, -10.0, 0.0, 0.0, 0.0);
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1;
        j1=new JointPos(-21.724, -136.814, -59.518, -68.853, 89.245, -66.359);

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        desc_p1 = new DescPose(703.996, -391.695, 240.708, -178.756, -4.709, -45.447);
        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang,0,0,0);
        float p = 0.00005f;
        float force = 10.0f;
        int rtn = robot.FT_ComplianceStart(p, force);
        System.out.println("FT_ComplianceStart rtn " + rtn);

        robot.MoveL(j1, desc_p1, 0, 0, 20.0, 180.0, 100.0, -1.0, epos, 0, 1, offset_pos, 0, 100);

        rtn = robot.FT_ComplianceStop();
        System.out.println("FT_ComplianceStop rtn " + rtn);
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang,0,0,0);
    }

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 負載辨識初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynFilterInit();

負載辨識變數初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 負載辨識變數初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynVarInit();

負荷辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 負荷辨識主程序
    * @param [in] joint_torque 關節扭矩
    * @param [in] joint_pos 關節位置
    * @param [in] t 採樣週期
    * @return 錯誤碼
    */
    int LoadIdentifyMain(Object[] joint_torque, Object[] joint_pos, double t);

獲取負荷辨識結果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取負荷辨識結果
    * @param [in] gain
    * @return List[0]:錯誤碼; List[1] : double weight 負載重量; List[2]: x 負載質心X mm; List[3] : y 負載質心Y mm; List[2]: z 負載質心Z mm
    */
    List<Number> LoadIdentifyGetResult(Object[] gain);

取得力道感測器拖曳開關狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得力道感測器拖曳開關狀態
    * @return List[0]:錯誤碼; List[1] : dragState 力道感測器輔助拖曳控制狀態，0-關閉；1-開啟; List[1] : sixDimensionalDragState 六維力輔助拖曳控制狀態，0-關閉；1-開啟
    */
    List<Integer> GetForceAndTorqueDragState();

力道感測器輔助拖曳
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.2-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief 力道感測器輔助拖曳
    * @param [in] status 控制狀態，0-關閉；1-開啟
    * @param [in] asaptiveFlag 自適應開啟標誌，0-關閉；1-開啟
    * @param [in] interfereDragFlag 干涉區拖曳標誌，0-關閉；1-開啟
    * @param [in] ingularityConstraintsFlag 奇異點策略：0-規避；1-穿越
    * @param [in] M 慣性係數
    * @param [in] B 阻尼係數
    * @param [in] K 剛度係數
    * @param [in] F 拖曳六維力閾值
    * @param [in] Fmax 最大拖動力限制 Nm
    * @param [in] Vmax 最大關節速度限制 °/s
    * @return 錯誤碼
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag, double[] M, double[] B, double[] K, double[] F, double Fmax, double Vmax);

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        Object[] M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        Object[] B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        Object[] K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        int rtn = robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);
        System.out.println("force drag control start rtn is:"+ rtn);
        robot.Sleep(5000);

        rtn = robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
        System.out.println("force drag control end rtn is:"+ rtn);

        rtn = robot.ResetAllError();
        System.out.println("ResetAllError rtn is:"+ rtn);

        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);
        System.out.println("force drag control start again rtn is:"+ rtn);
        robot.Sleep(5000);

        rtn = robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
        System.out.println("force drag control end again rtn is:"+ rtn);
    }

設定六維力和關節阻抗混合拖曳開關及參數
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定六維力和關節阻抗混合拖曳開關及參數
    * @param [in] status 控制狀態，0-關閉；1-開啟
    * @param [in] impedanceFlag 阻抗開啟標誌，0-關閉；1-開啟
    * @param [in] lamdeGain 拖曳增益
    * @param [in] KGain 剛度增益
    * @param [in] BGain 阻尼增益
    * @param [in] dragMaxTcpVel 拖曳末端最大線速度限制
    * @param [in] dragMaxTcpOriVel 拖曳末端最大角速度限制
    * @return 錯誤碼
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, Object[] lamdeGain, Object[] KGain, Object[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.DragTeachSwitch(1);
        Object[] lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        Object[] KGain = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] BGain = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        List<Integer> rtnArray = robot.GetForceAndTorqueDragState();
        System.out.println("the drag state is  " + rtnArray.get(1) + "  ForceAndJointImpedance state  " + rtnArray.get(2));
    }

設定力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定力道感測器下負載重量
    * @param [in] weight 負載重量 kg
    * @return 錯誤碼
    */
    int SetForceSensorPayLoad(double weight);

設定力道感測器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定力道感測器下負載質心
    * @param [in] cog 負載質心 mm
    * @return 錯誤碼
    */
    int SetForceSensorPayLoadCog(DescTran cog);

取得力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得力道感測器下負載重量
    * @return List[0]:錯誤碼; List[1] : weight 負載重量 kg
    */
    List<Number> GetForceSensorPayLoad();

取得力感測器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得力感測器下負載質心
    * @param [out] cog 負載質心 mm
    * @return 錯誤碼
    */
    int GetForceSensorPayLoadCog(DescTran cog);
    
代碼範例
+++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.SetForceSensorPayLoad(1.34);
        DescTran cog = new DescTran(0.778, 2.554, 48.765);
        robot.SetForceSensorPayLoadCog(cog);
        double weight = 0;

        List<Number> rtnArrays = robot.GetForceSensorPayLoad();
        DescTran getCog = new DescTran(0.0, 0.0, 0.0);
        robot.GetForceSensorPayLoadCog(getCog);
        System.out.println("the FT load is " +  rtnArrays.get(1) + "  cog is  " + getCog.x + "  " + getCog.y + "   " + getCog.z);
    }

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力傳感器自動校零
    * @param [in] massCenter 感測器質量(kg) 及 質心(mm)
    * @return 錯誤碼
    */
    int ForceSensorAutoComputeLoad(MassCenter massCenter);

設定機器人碰撞檢測方法
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定機器人碰撞檢測方法
    * @param [in] method 碰撞檢測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啟
    * @param [in] thresholdMode 碰撞等級閾值方式；0-碰撞等級固定閾值方式；1-自訂碰撞檢測閾值
    * @return 錯誤碼
    */
    int SetCollisionDetectionMethod(int method,int thresholdMode);