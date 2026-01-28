機器人力控
============

.. toctree:: 
    :maxdepth: 5

配置力傳感器
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置力傳感器
    * @param  config company:力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI傳感器，21-中科米點，22-偉航敏芯，23-NBIT，24-鑫精誠(XJC)，26-NSR
    * @param  config device: 設備號，坤維(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精誠XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)
    * @param  config softvesion:軟件版本號，暫不使用，默認爲0
    * @param  config bus:設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int FT_SetConfig(DeviceConfig config); 

獲取力傳感器配置 
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取力傳感器配置 
    * @param [out] config company:力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI傳感器，21-中科米點，22-偉航敏芯
    * @param [out] config device:設備號，坤維(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A)
    * @param [out] config softvesion:軟件版本號，暫不使用，默認爲0
    * @param [out] config bus:設備掛在末端總線位置，暫不使用，默認爲0
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

設置力傳感器參考座標系
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置力傳感器參考座標系
    * @param  [in] type  0-工具座標系，1-基座標系, 2-自由座標系
    * @param  [in] coord  自由座標系值
    * @return  錯誤碼
    */
    int FT_SetRCS(int type, DescPose coord);

設置力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置力傳感器下負載重量
    * @param [in] weight 負載重量 kg
    * @return 錯誤碼
    */
    int SetForceSensorPayLoad(double weight);

設置力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置力傳感器下負載質心
    * @param [in] cog 負載質心 mm
    * @return 錯誤碼
    */
    int SetForceSensorPayLoadCog(DescTran cog);

獲取力傳感器下負載重量
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取力傳感器下負載重量
    * @return List[0]:錯誤碼; List[1] : weight 負載重量 kg
    */
    List<Number> GetForceSensorPayLoad();

獲取力傳感器下負載質心
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取力傳感器下負載質心
    * @param [out] cog 負載質心 mm
    * @return 錯誤碼
    */
    int GetForceSensorPayLoadCog(DescTran cog);

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力傳感器自動校零
    * @param [in] massCenter 傳感器質量(kg) 及 質心(mm)
    * @return 錯誤碼
    */
    int ForceSensorAutoComputeLoad(MassCenter massCenter);

獲取參考座標系下力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取參考座標系下力/扭矩數據
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueRCS(int flag, ForceTorque ft); 

獲取力傳感器原始力/扭矩數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取力傳感器原始力/扭矩數據
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    int FT_GetForceTorqueOrigin(int flag, ForceTorque ft); 

力傳感器配置及自動校零代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTInit(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company,device,softversion,bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose ftCoord = new DescPose();
        robot.FT_SetRCS(0, ftCoord);

        robot.SetForceSensorPayload(0.824);

        DescTran tr=new DescTran(0.778, 2.554, 48.765);
        robot.SetForceSensorPayloadCog(tr);
        List<Number> weight = new ArrayList<>();
        double x = 0, y = 0, z = 0;
        weight=robot.GetForceSensorPayload();
        robot.GetForceSensorPayloadCog(tr);
        tr.x=0;
        tr.y=0;
        tr.z=0;
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr);

        double computeWeight = 0;
        DescTran tran = new DescTran();
        MassCenter mass=new MassCenter();
        mass.weight=weight.get(1).doubleValue();
        mass.cog=tran;
        robot.ForceSensorAutoComputeLoad(mass);
        return 0;
    }

負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
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
    * @param  [in] id  傳感器座標系編號，範圍[1~14]
    * @param  [in] index 點編號，範圍[1~3]
    * @return  錯誤碼
    */
    int FT_PdCogIdenRecord(int id, int index); 

負載質心辨識計算
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  負載質心辨識計算
    * @param  [out] cog  負載質心，單位mm
    * @return  錯誤碼
    */   
    int FT_PdCogIdenCompute(DescTran cog);

力傳感器負載辨識代碼示例
+++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTLoadCompute(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        robot.FT_GetForceTorqueOrigin(0, ft);
        robot.FT_SetZero(1);
        robot.Sleep(1000);

        DescPose tcoord = new DescPose();
        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, tcoord, 1, 0, 0, 0);

        robot.FT_PdIdenRecord(10);
        robot.Sleep(1000);

        List<Number> weight =new ArrayList<>();
        weight=robot.FT_PdIdenCompute();

        DescPose desc_p1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_p3=new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);

        robot.MoveCart(desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(desc_p2, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(desc_p3, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.Sleep(1000);
        robot.FT_PdCogIdenRecord(10, 3);
        robot.Sleep(1000);
        DescTran cog=new DescTran(0,0,0);
        robot.FT_PdCogIdenCompute(cog);

        robot.CloseRPC();
        return 0;
    }

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int FT_Guard(int flag, int sensor_id, Object[] select, ForceTorque ft, Object[] max_threshold, Object[] min_threshold); 

碰撞守護代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設置重連次數、間隔
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
        Object[] select = { 1, 0, 0, 0, 0, 0 };//只啓用x軸碰撞守護
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
    * @param  flag 0-關閉恆力控制，1-開啓恆力控制
    * @param  sensor_id 力傳感器編號
    * @param  select  選擇六個自由度是否檢測碰撞，0-不檢測，1-檢測
    * @param  ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  ft_pid 力pid參數，力矩pid參數
    * @param  adj_sign 自適應啓停控制，0-關閉，1-開啓
    * @param  ILC_sign ILC啓停控制， 0-停止，1-訓練，2-實操
    * @param  max_dis 最大調整距離，單位mm
    * @param  max_ang 最大調整角度，單位deg
    * @param  M rx、ry質量參數[0.1-10], 預設2
    * @param  B rx、ry阻尼參數[0.1-50], 預設8
    * @param  threshold rx、ry啟動閾值[0-10], 預設0.2
    * @param  adjustCoeff rx、ry力矩調節係數[0-1], 預設1
    * @param  polishRadio 打磨半徑，單位mm
    * @param  filter_Sign 濾波開啓標誌 0-關；1-開，默認關閉
    * @param  posAdapt_sign 姿態順應開啓標誌 0-關；1-開，默認關閉
    * @param  isNoBlock 阻塞標誌，0-阻塞；1-非阻塞
    * @return  錯誤碼
    */
    public int FT_Control(int flag, int sensor_id, int[] select, ForceTorque ft, double[] ft_pid, int adj_sign, int ILC_sign, double max_dis, double max_ang,double[] M,double[] B, double[] threshold, double[] adjustCoeff, double polishRadio,int filter_Sign, int posAdapt_sign, int isNoBlock)

具有阻尼的恆力控制代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFTControlWithAdjustCoeff(Robot robot)
    {
        int sensor_id = 10;
        int[] select = { 0,0,1,0,0,0 };
        double[] ft_pid = { 0.0008, 0.0, 0.0, 0.0, 0.0, 0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 1000.0;
        double max_ang = 20;
        ForceTorque ft = new ForceTorque(0.0,0,0,0,0,0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        JointPos j1=new JointPos(80.765, -98.795, 106.548, -97.734, -89.999, 94.842);
        JointPos j2=new JointPos(43.067, -84.429, 92.620, -98.175, -90.011, 57.144);
        DescPose desc_p1=new DescPose(5.009, -547.463, 262.053, -179.999, -0.019, 75.923);
        DescPose desc_p2=new DescPose(-347.966, -547.463, 262.048, -180.000, -0.019, 75.923);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        double[] M = { 2.0, 2.0 };
        double[] B = { 15.0, 15.0 };
        double[] threshold = {1.0, 1.0};
        double[] adjustCoeff = {1.0, 0.8};
        double polishRadio = 0.0;
        int filter_Sign = 0;
        int posAdapt_sign = 1;
        int isNoBlock;
        ft.fz = -10.0;
        while(true)
        {
            int rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control start rtn is %d\n", rtn);
            robot.MoveL(j1, desc_p1, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            robot.MoveL(j2, desc_p2, 1, 0, 100.0, 100.0, 100.0, -1.0, 0, epos, 0, 0, offset_pos, 0,0, 0,10);
            rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold, adjustCoeff, 0, 0, 1, 0);
            System.out.printf("FT_Control end rtn is %d\n", rtn);
        }
    }

旋轉插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 旋轉插入
    * @param rcs 參考座標系，0-工具座標系，1-基座標系
    * @param angVelRot 旋轉角速度，單位deg/s
    * @param ft  力/扭矩閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param max_angle 最大旋轉角度，單位deg
    * @param orn 力/扭矩方向，1-沿z軸方向，2-繞z軸方向
    * @param max_angAcc 最大旋轉加速度，單位deg/s^2，暫不使用，預設為0
    * @param rotorn  旋轉方向，1-順時針，2-逆時針
    * @param strategy 未偵測到力/力矩的處理策略，0-報錯；1-警告，繼續運動
    * @return  錯誤碼
    */
    public int FT_RotInsertion(int rcs, double angVelRot, double ft, double max_angle, int orn, double max_angAcc, int rotorn, int strategy)

機器人力感測器旋轉插入程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn=-1;
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4=new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4=new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

柔順控制開啓
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  柔順控制開啓
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啓力閾值，單位N
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

柔順控制代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCompliance(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        int company = 24;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;

        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);

        robot.Sleep(1000);

        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);

        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);

        int flag = 1;
        int sensor_id = 1;
        Object[] select =new Object[] { 1,1,1,0,0,0 };
        Object[] ft_pid =new Object[] { 0.0005,0.0,0.0,0.0,0.0,0.0 };
        int adj_sign = 0;
        int ILC_sign = 0;
        double max_dis = 100.0;
        double max_ang = 0.0;

        ForceTorque ft=new ForceTorque(0,0,0,0,0,0);
        DescPose  offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);


        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_p1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_p2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);
        double p = 0.00005;
        double force = 30.0;
        int rtn = robot.FT_ComplianceStart(p, force);

        int count = 15;
        while (count>0)
        {
            robot.MoveL(j1, desc_p1, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 1, offset_pos,0,10);
            robot.MoveL(j2, desc_p2, 0, 0, 100.0, 180.0, 100.0, -1.0,0, epos, 0, 0, offset_pos,0,10);
            count -= 1;
        }
        robot.FT_ComplianceStop();
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0);

        robot.CloseRPC();
        return 0;
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

負載辨識變量初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 負載辨識變量初始化
    * @return 錯誤碼
    */
    int LoadIdentifyDynVarInit();

負載辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 負載辨識主程序
    * @param [in] joint_torque 關節扭矩
    * @param [in] joint_pos 關節位置
    * @param [in] t 採樣週期
    * @return 錯誤碼
    */
    int LoadIdentifyMain(Object[] joint_torque, Object[] joint_pos, double t);

獲取負載辨識結果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取負載辨識結果
    * @param [in] gain
    * @return List[0]:錯誤碼; List[1] : double weight 負載重量; List[2]: x 負載質心X mm; List[3] : y 負載質心Y mm; List[2]: z 負載質心Z mm
    */
    List<Number> LoadIdentifyGetResult(Object[] gain);

機器人負載辨識代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestIdentify(Robot robot)
    {
        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();

        retval = robot.LoadIdentifyDynVarInit();

        JointPos posJ = new JointPos(0,0,0,0,0,0);
        DescPose posDec = new DescPose(0,0,0,0,0,0);
        List<Number> joint_toq=new ArrayList<>();
        robot.GetActualJointPosDegree( posJ);
        posJ.J2 = posJ.J2 + 10;
        joint_toq=robot.GetJointTorques(0);

        Object[] gain =new Object[] { 0,0.05,0,0,0,0,0,0.02,0,0,0,0 };
        double weight = 0;
        DescTran load_pos=new DescTran(0,0,0);
        List<Number> num=new ArrayList<>();
        num = robot.LoadIdentifyGetResult(gain);

        robot.CloseRPC();
        return 0;

    }

力傳感器輔助拖動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief 力傳感器輔助拖動
    * @param [in] status 控制狀態，0-關閉；1-開啓
    * @param [in] asaptiveFlag 自適應開啓標誌，0-關閉；1-開啓
    * @param [in] interfereDragFlag 干涉區拖動標誌，0-關閉；1-開啓
    * @param [in] ingularityConstraintsFlag 奇異點策略，0-規避；1-穿越
    * @param [in] forceCollisionFlag 輔助拖動時機器人碰撞檢測標誌；0-關閉；1-開啓
    * @param [in] M 慣性系數
    * @param [in] B 阻尼係數
    * @param [in] K 剛度係數
    * @param [in] F 拖動六維力閾值
    * @param [in] Fmax 最大拖動力限制 Nm
    * @param [in] Vmax 最大關節速度限制 °/s
    * @return 錯誤碼
    */
    int EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag,int ingularityConstraintsFlag, int forceCollisionFlag, Object[] M, Object[] B, Object[] K, Object[] F, double Fmax, double Vmax)

獲取力傳感器拖動開關狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取力傳感器拖動開關狀態
    * @return List[0]:錯誤碼; List[1] : dragState 力傳感器輔助拖動控制狀態，0-關閉；1-開啓; List[1] : sixDimensionalDragState 六維力輔助拖動控制狀態，0-關閉；1-開啓
    */
    List<Integer> GetForceAndTorqueDragState();

報錯清除後力傳感器自動開啓
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 報錯清除後力傳感器自動開啓
    * @param [in] status 控制狀態，0-關閉；1-開啓
    * @return 錯誤碼
    */
    int SetForceSensorDragAutoFlag(int status)

力傳感器輔助拖動代碼示例
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestEndForceDragCtrl(Robot robot)
    {
        DescTran tr1=new DescTran(0,0,0);
        robot.SetForceSensorPayload(0);
        robot.SetForceSensorPayloadCog(tr1);

        robot.SetForceSensorDragAutoFlag(1);

        Object[] M =new Object[] { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        Object[] B =new Object[] { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        Object[] K =new Object[] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        Object[] F =new Object[] { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100);

        robot.Sleep(10000);

        int dragState = 0;
        int sixDimensionalDragState = 0;
        List<Integer> state=new ArrayList<>();
        state=robot.GetForceAndTorqueDragState();

        robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100);
        return 0;
    }

設置六維力和關節阻抗混合拖動開關及參數
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置六維力和關節阻抗混合拖動開關及參數
    * @param [in] status 控制狀態，0-關閉；1-開啓
    * @param [in] impedanceFlag 阻抗開啓標誌，0-關閉；1-開啓
    * @param [in] lamdeGain 拖動增益
    * @param [in] KGain 剛度增益
    * @param [in] BGain 阻尼增益
    * @param [in] dragMaxTcpVel 拖動末端最大線速度限制
    * @param [in] dragMaxTcpOriVel 拖動末端最大角速度限制
    * @return 錯誤碼
    */
    int ForceAndJointImpedanceStartStop(int status, int impedanceFlag, Object[] lamdeGain, Object[] KGain, Object[] BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

六維力和關節阻抗混合拖動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestForceAndJointImpedance(Robot robot)
    {
        robot.DragTeachSwitch(1);
        Object[] lamdeDain =new Object[] { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
        Object[] KGain = new Object[]{ 0, 0, 0, 0, 0, 0 };
        Object[] BGain =new Object[] { 150, 150, 150, 5.0, 5.0, 1.0 };
        int rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.Sleep(10000);

        robot.DragTeachSwitch(0);
        rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000.0, 180.0);

        robot.CloseRPC();
        return 0;
    }

阻抗啓停控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    public static int TestImpedanceControl(Robot robot)
    {
        JointPos j1=new JointPos(102.622, -135.990, 120.769, -73.950, -90.848, 35.507);
        JointPos j2=new JointPos(93.674, -80.062, 82.947, -92.199, -90.967, 26.559);
        DescPose desc_pos1=new DescPose(136.552, -149.799, 449.532, 179.817, -1.172, 157.123);
        DescPose desc_pos2=new DescPose(136.540, -561.048, 449.542, 179.819, -1.172, 157.122);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 200.0;
        double ovl = 100.0;
        double blendT = -1.0;
        double blendR = -1.0;
        int flag = 0;
        int search = 0;
        robot.SetSpeed(20);
        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        DeviceConfig con=new DeviceConfig(company, device, softversion, bus);
        robot.FT_SetConfig(con);
        robot.Sleep(1000);
        robot.FT_GetConfig(con);
        System.out.println("FT config:"+con.company+","+con.device+","+con.softwareVersion+"con"+ con.bus);
        robot.Sleep(1000);
        robot.FT_Activate(0);
        robot.Sleep(1000);
        robot.FT_Activate(1);
        robot.Sleep(1000);
        robot.Sleep(1000);
        robot.FT_SetZero(0);
        robot.Sleep(1000);
        robot.FT_SetZero(1);
        robot.Sleep(1000);
        double[] forceThreshold = { 30,30,30,5,5,5 };
        double[] m= { 0.1,0.1,0.1,0.02,0.02,0.02 };
        double[] b = { 1,1,1,0.08,0.08,0.08 };
        double[] k = { 0,0,0,0,0,0 };
        int rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        System.out.println("ImpedanceControlStartStop errcode:"+ rtn);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos1, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, 0, epos, search, flag, offset_pos, -1,0,-1, 1);
        System.out.println("movel errcode:"+ rtn);
        robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100);
        robot.CloseRPC();
        return 0;
    }

開啟力矩補償功能及補償係數
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 開啟力矩補償功能及補償係數
    * @param  status 開關，0-關閉；1-開啟
    * @param  torqueCoeff J1-J6力矩補償係數[0-1]
    * @return 錯誤碼
    */
    public int SerCoderCompenParams(int status, double[] torqueCoeff)