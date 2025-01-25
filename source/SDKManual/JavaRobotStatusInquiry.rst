機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

取得機器人安裝角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得機器人安裝角度
    * @return  List[0]:錯誤碼; List[1]:double yangle 傾斜角; List[2]:double zangle 旋轉角
    */
    List<Number> GetRobotInstallAngle(); 

取得系統變數值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得系統變數值
    * @param  [in] id 系統變數編號，範圍[1~20]
    * @return  List[0]:錯誤碼; List[1]:double value 系統變數值
    */
    List<Number> GetSysVarValue(int id); 

取得目前關節位置(角度)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得目前關節位置(角度)
    * @param  [out] jPos 獲取的六個關節位置，單位deg
    * @return  錯誤碼
    */
    int GetActualJointPosDegree(JointPos jPos); 

取得關節回饋速度-deg/s
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得關節回饋速度-deg/s 
    * @param [out] speed 六個關節速度
    * @return 錯誤碼 
    */
    int GetActualJointSpeedsDegree(Object[] speed);

取得當前工具位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得當前工具位姿
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    int GetActualTCPPose(DescPose desc_pos); 

逆運動學求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] config 關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, JointPos joint_pos);

逆運動學求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置求解
    * @param  [in] posMode 0絕對位姿， 1相對位姿-基座標系 2相對位姿-工具坐標系
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, JointPos joint_pos); 

逆運動學求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判断是否有解
    * @param  [in] posMode 0絕對位姿， 1相對位姿-基座標系 2相對位姿-工具坐標系
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @return  錯誤碼  List[0]:錯誤碼; List[1]: int hasResult 0-無解，1-有解
    */   
    List<Integer> GetInverseKinHasSolution(int posMode, DescPose desc_pos, JointPos joint_pos_ref);  

正運動學求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  正運動學求解
    * @param  [in] joint_pos 關節位置
    * @param  [out] desc_pos 笛卡兒位姿
    * @return  錯誤碼
    */
    int GetForwardKin(JointPos joint_pos, DescPose desc_pos); 

取得當前關節轉矩
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得當前關節轉矩
    * @param  [in]  flag 0-阻塞，1-非阻塞
    * @param  [out]  torques 關節轉矩
    * @return  錯誤碼
    */
    int GetJointTorques(int flag, Object[] torques); 

取得目前負載的重量
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得目前負載的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @return  List[0]:int 錯誤碼; List[1]: double weight  負載重量，單位kg
    */
    List<Number> GetTargetPayload(int flag); 

取得目前負載的質心
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得目前負載的質心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 負載質心，單位mm
    * @return  錯誤碼
    */   
    int GetTargetPayloadCog(int flag, DescTran cog);

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        robot.SetRobotInstallAngle(23.4, 56.7);
        List<Number> rtnArr =  robot.GetRobotInstallAngle();
        System.out.println("安裝角度: " + rtnArr.get(1) + "  " + rtnArr.get(2));
        robot.SetRobotInstallAngle(0, 0);

        robot.SetLoadWeight(0);
        robot.SetLoadCoord(new DescTran(0.0, 0.0, 0.0));

        DescTran cog = new DescTran();
        robot.GetTargetPayloadCog(1, cog);

        System.out.println("weight is " + rtnArr.get(1) + " cog is  " + cog.x + "  " + cog.y + "  " + cog.z);

        List<Integer> Arr = robot.GetRobotCurJointsConfig();
        System.out.println("config is " + Arr.get(1));

        DescPose  desc_p1=new DescPose();

        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        JointPos JP_test=new JointPos();
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        robot.GetInverseKin(0, DP1, -1, JP_test);
        List<Integer> rtnArrInt =  robot.GetInverseKinHasSolution(0, DP1, JP1);//逆向是否有解
        System.out.println("has Solution ? " + rtnArrInt.get(1));
        robot.GetForwardKin(JP1, desc_p1);//正向運動学
        JointPos j2 = new JointPos();
        robot.GetInverseKinRef(0, DP1, JP1, JP_test);//逆向運動学
    }

獲取當前工具坐標系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工具坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐標系位姿
    * @return  錯誤碼
    */
    int GetTCPOffset(int flag, DescPose desc_pos); 

取得當前工件坐標系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得當前工件坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件座標系位姿
    * @return  錯誤碼
    */   
    int GetWObjOffset(int flag, DescPose desc_pos); 

取得關節軟限位角度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得關節軟限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] negative  負限位角度，單位deg
    * @param  [out] positive  正限位角度，單位deg
    * @return  錯誤碼
    */
    int GetJointSoftLimitDeg(int flag, Object[] negative, Object[] positive); 

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        DescPose offset = new DescPose();
        robot.GetTCPOffset(1, offset);//工具
        System.out.println("offset is " + offset);
        robot.GetWObjOffset(1, offset);//工件
        System.out.println("offset is " + offset);

        Object[] neg_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        Object[] pos_deg = new Object[]{0, 0 , 0, 0, 0, 0};
        robot.GetJointSoftLimitDeg(1,  neg_deg,  pos_deg);
        System.out.println("neg is " + Arrays.toString(neg_deg) + " pos is " + Arrays.toString(pos_deg));
    }

取得系統時間
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得系統時間
    * @return  List[0]:int 錯誤碼; List[1]:double t_ms 單位ms
    */
    List<Number> GetSystemClock();

取得機器人當前關節配置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得機器人當前關節配置
    * @return  List[0]:int 錯誤碼; List[1]:int config 關節空間配置，範圍[0~7]
    */
    List<Integer> GetRobotCurJointsConfig();

取得機器人預設速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得機器人預設速度
    * @return  List[0]:int 錯誤碼; List[1]: double vel 速度，單位mm/s
    */   
    List<Number> GetDefaultTransVel(); 

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        List<Integer> rtnArr = robot.GetRobotCurJointsConfig();
        System.out.println("config is " + rtnArr.get(1));

        List<Number> rtnArrN = robot.GetSystemClock();
        System.out.println("systom clock is  " + rtnArrN.get(1));

        rtnArrN = robot.GetDefaultTransVel();
        System.out.println("機器人當前速度為: " + rtnArrN.get(1));
    }

查詢機器人示教管理點數據
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 查詢機器人示教管理點位數據 
    * @param [in]  name  點位名
    * @return  List[0]:錯誤碼; List[1] - List[20] : 點位數據double[20]{x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4} 
    */ 
    List<Number> GetRobotTeachingPoint(String name); 

取得SSH公鑰
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得SSH公鑰 
    * @param [in] keygen 公鑰 
    * @return 錯誤碼    
    */ 
    List<Number> GetRobotTeachingPoint(String name); 

計算指定路徑下檔案的MD5值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算指定路徑下檔案的MD5值 
    * @param [in] file_path 檔案路徑包含檔名，預設Traj資料夾路徑為:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt" 
    * @return 錯誤碼   
    */ 
    int ComputeFileMD5(String file_path, String md5); 

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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

        List<Number> rtnArr = robot.GetRobotTeachingPoint("P1");
        System.out.println("point data  " + rtnArr);

        String[] key = {""};
        robot.GetSSHKeygen(key);
        System.out.println("ssh key  " + key[0]);
    }

取得機器人軟體版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得機器人軟體版本
    * @param [out] robotModel 機器人型號
    * @param [out] webVersion web版本
    * @param [out] controllerVersion 控制器版本
    * @return 錯誤碼 
    */
    int GetSoftwareVersion(String robotModel, String webVersion, String controllerVersion);

取得機器人硬體版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得機器人硬體版本
    * @param [out] ctrlBoxBoardVersion 控制箱載板硬體版本
    * @param [out] driver1Version 驅動器1硬體版本
    * @param [out] driver1Version 驅動器2硬體版本
    * @param [out] driver1Version 驅動器3硬體版本
    * @param [out] driver1Version 驅動器4硬體版本
    * @param [out] driver1Version 驅動器5硬體版本
    * @param [out] driver1Version 驅動器6硬體版本
    * @param [out] endBoardVersion 端板硬體版本
    * @return 錯誤碼 
    */
    int GetHardwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

取得機器人韌體版本
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得機器人韌體版本
    * @param [out] ctrlBoxBoardVersion 控制箱載板韌體版本
    * @param [out] driver1Version 驅動器1韌體版本
    * @param [out] driver1Version 驅動器2韌體版本
    * @param [out] driver1Version 驅動器3韌體版本
    * @param [out] driver1Version 驅動器4韌體版本
    * @param [out] driver1Version 驅動器5韌體版本
    * @param [out] driver1Version 驅動器6韌體版本
    * @param [out] endBoardVersion 末端板韌體版本
    * @return 錯誤碼 
    */
    int GetFirmwareVersion(String ctrlBoxBoardVersion, String driver1Version, String driver2Version, String driver3Version,
                                          String driver4Version, String driver5Version, String driver6Version, String endBoardVersion);

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        String ctrlBoxBoardVersion = "";
        String driver1Version = "";
        String driver2Version = "";
        String driver3Version = "";
        String driver4Version = "";
        String driver5Version = "";
        String driver6Version = "";
        String endBoardVersion = "";
        robot.GetHardwareVersion(ctrlBoxBoardVersion ,driver1Version,  driver2Version,  driver3Version,
                 driver4Version,  driver5Version,  driver6Version,  endBoardVersion);

        robot.GetFirmwareVersion(ctrlBoxBoardVersion, driver1Version, driver2Version, driver3Version,
                driver4Version, driver5Version, driver6Version, endBoardVersion);
    }