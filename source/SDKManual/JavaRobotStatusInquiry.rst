機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

獲取當前關節位置(角度)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前關節位置(角度)
    * @param  [out] jPos 獲取的六個關節位置，單位deg
    * @return  錯誤碼
    */
    int GetActualJointPosDegree(JointPos jPos); 

獲取關節反饋速度-deg/s
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取關節反饋速度-deg/s 
    * @param [out] speed 六個關節速度
    * @return 錯誤碼 
    */
    int GetActualJointSpeedsDegree(Object[] speed);

獲取關節反饋加速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取關節反饋加速度-deg/s^2
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] acc 六個關節加速度
    * @return  錯誤碼
    */
    public int GetActualJointAccDegree(int flag, Object[] acc)

獲取TCP指令合速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取TCP指令速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] tcp_speed 線性速度
    * @param  [out] ori_speed 姿態速度
    * @return  錯誤碼
    */
    public int GetTargetTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

獲取TCP反饋合速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取TCP反饋合速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] tcp_speed 線性速度
    * @param  [out] ori_speed 姿態速度
    * @return  錯誤碼
    */
    public int GetActualTCPCompositeSpeed(int flag, double tcp_speed, double ori_speed)

獲取TCP指令速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取TCP指令速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] speed [x,y,z,rx,ry,rz]速度
    * @return  錯誤碼
    */
    public int GetTargetTCPSpeed(int flag, Object[] speed)

獲取TCP反饋速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取TCP反饋速度
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] speed [x,y,z,rx,ry,rz]速度
    * @return  錯誤碼
    */
    public int GetActualTCPSpeed(int flag, Object[] speed)

獲取當前工具位姿
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工具位姿
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    int GetActualTCPPose(DescPose desc_pos); 

獲取當前工具座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工具座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具座標系編號
    * @return  錯誤碼
    */
    int GetActualTCPNum(int flag, int[] id)

獲取當前工件座標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工件座標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件座標系編號
    * @return  錯誤碼
    */
    public int GetActualWObjNum(int flag, int[] id)

獲取當前末端法蘭位姿
+++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前末端法蘭位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法蘭位姿
    * @return  錯誤碼
    */
    public int GetActualToolFlangePose(int flag, DescPose desc_pos)

獲取當前關節轉矩
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取當前關節轉矩
    * @param  [in]  flag 0-阻塞，1-非阻塞
    * @param  [out]  torques 關節轉矩
    * @return  錯誤碼
    */
    int GetJointTorques(int flag, Object[] torques);

獲取系統時間
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取系統時間
    * @return  List[0]:int 錯誤碼; List[1]:double t_ms 單位ms
    */
    List<Number> GetSystemClock();

查詢機器人運動是否完成
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查詢機器人運動是否完成
    * @param   [out] state  0-未完成，1-完成
    * @return  錯誤碼
    */
    public int GetRobotMotionDone(int[] state)

查詢機器人運動隊列緩存長度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  查詢機器人運動隊列緩存長度
    * @param   [out] len  緩存長度
    * @return  錯誤碼
    */
    public int GetMotionQueueLength(int[] len)

獲取機器人急停狀態
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人急停狀態
    * @param [out] state 急停狀態，0-非急停，1-急停
    * @return 錯誤碼
    */
    public int GetRobotEmergencyStopState(int[] state)

獲取SDK與機器人的通訊狀態
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取SDK與機器人的通訊狀態
    * @return state 通訊狀態，0-通訊正常，1-通訊異常
    */
    public int GetSDKComState()

獲取安全停止信號
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取安全停止信號
    * @param  [out] si0_state 安全停止信號SI0，0-無效，1-有效
    * @param  [out] si1_state 安全停止信號SI1，0-無效，1-有效
    * @return 錯誤碼
    */
    public int GetSafetyStopState(int[] si0_state, int[] si1_state)

獲取機器人關節驅動器溫度(℃)
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器溫度(℃)
    * @param  [out] temperature 溫度
    * @return 錯誤碼
    */
    public int GetJointDriverTemperature(double[] temperature)

獲取機器人關節驅動器扭矩(Nm)
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人關節驅動器扭矩(Nm)
    * @param  [out] torque 扭矩
    * @return 錯誤碼
    */
    public int GetJointDriverTorque(double[] torque)

獲取機器人實時狀態結構體
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人實時狀態結構體
    * @return 實時狀態結構體
    */
    public ROBOT_STATE_PKG GetRobotRealTimeState()

機器人狀態查詢代碼示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetStatus(Robot robot)
    {
        List<Number> angle=new ArrayList<>();
        angle=robot.GetRobotInstallAngle();
        System.out.println("yangle:"+angle.get(1)+",zangle:"+angle.get(2));

        JointPos j_deg =new JointPos(){};
        robot.GetActualJointPosDegree( j_deg);

        Object[] jointSpeed =new Object[] { 0,0,0,0,0,0 };
        robot.GetActualJointSpeedsDegree(jointSpeed);

        Object[] jointAcc = new Object[]{0,0,0,0,0,0 };
        robot.GetActualJointAccDegree(0, jointAcc);

        double tcp_speed = 0.0;
        double ori_speed = 0.0;
        robot.GetTargetTCPCompositeSpeed(0, tcp_speed, ori_speed);

        robot.GetActualTCPCompositeSpeed(0, tcp_speed, ori_speed);

        Object[] targetSpeed =new Object[] { 0,0,0,0,0,0 };
        robot.GetTargetTCPSpeed(0, targetSpeed);

        Object[] actualSpeed =new Object[] {0,0,0,0,0,0 };
        robot.GetActualTCPSpeed(0, actualSpeed);

        DescPose tcp = new DescPose(){};
        robot.GetActualTCPPose(tcp);

        DescPose flange = new DescPose(){};
        robot.GetActualToolFlangePose(0, flange);

        int[] id = {};
        robot.GetActualTCPNum(0, id);

        robot.GetActualWObjNum(0, id);

        List<Number> jtorque=new ArrayList<>();
        jtorque=robot.GetJointTorques(0);

        List<Number> t_ms = new ArrayList<>();
        t_ms=robot.GetSystemClock();

        List<Integer> config = new ArrayList<>();
        config=robot.GetRobotCurJointsConfig();

        int motionDone = 0;
        robot.GetRobotMotionDone(motionDone);

        int[] len ={0 };
        robot.GetMotionQueueLength(len);

        int[] emergState = {0};
        robot.GetRobotEmergencyStopState(emergState);

        int comstate = 0;
        comstate=robot.GetSDKComState();

        int[] si0_state=new int[]{0}, si1_state=new int[]{0};
        robot.GetSafetyStopState(si0_state, si1_state);

        double[] temp =new double[] { 0,0,0,0,0,0 };
        robot.GetJointDriverTemperature(temp);

        double[] torque = new double[]{ 0,0,0,0,0,0 };
        robot.GetJointDriverTorque(torque);

        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        pkg=robot.GetRobotRealTimeState();

        return 0;
    }

逆運動學求解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] config 關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */ 
    int GetInverseKin(int type, DescPose desc_pos, int config, JointPos joint_pos);

逆運動學求解(參考位置)
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置求解
    * @param  [in] posMode 0絕對位姿， 1相對位姿-基座標系   2相對位姿-工具座標系
    * @param  [in] desc_pos 笛卡爾位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */   
    int GetInverseKinRef(int posMode, DescPose desc_pos, JointPos joint_pos_ref, JointPos joint_pos); 

逆運動學求解，笛卡爾空間包含擴展軸位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 逆運動學求解，笛卡爾空間包含擴展軸位置
    * @param  type 0-絕對位姿(基座標系)，1-增量位姿(基座標系)，2-增量位姿(工具座標系)
    * @param  desc_pos 笛卡爾位姿
    * @param  exaxis 擴展軸位置
    * @param  tool 工具號
    * @param  workPiece 工件號
    * @param  joint_pos 關節位置
    * @return 錯誤碼
    */
    public int GetInverseKinExaxis(int type, DescPose desc_pos, ExaxisPos exaxis, int tool, int workPiece, JointPos joint_pos)
    
逆運動學求解包含擴展軸位置程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void  TestInverseKinExaxis(Robot robot)
    {
        DescPose desc=new DescPose(99.957, -0.002, 29.994, -176.569, -6.757, -167.462);
        ExaxisPos exaxis=new ExaxisPos(100.0, 0.0, 0.0, 0.0);
        JointPos jointPos =new JointPos();
        DescPose offsetPos =new DescPose();
        ROBOT_STATE_PKG pkg=robot.GetRobotRealTimeState();
        int toolnum = pkg.tool;
        int workPcsNum = pkg.user;
        robot.GetInverseKinExaxis(0, desc, exaxis, toolnum, workPcsNum, jointPos);
        System.out.printf("GetInverseKinExaxis joint is %f, %f, %f, %f, %f, %f\n", jointPos.J1, jointPos.J2, jointPos.J3, jointPos.J4, jointPos.J5, jointPos.J6);
        robot.ExtAxisMove(exaxis, 100, -1);
        robot.MoveJ(jointPos, desc, toolnum, workPcsNum, 100.0, 100.0, 100.0, exaxis, -1, 0, offsetPos);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }

獲取逆運動學是否有解
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判斷是否有解
    * @param  [in] posMode 0絕對位姿， 1相對位姿-基座標系   2相對位姿-工具座標系
    * @param  [in] desc_pos 笛卡爾位姿
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
    * @param  [out] desc_pos 笛卡爾位姿
    * @return  錯誤碼
    */
    int GetForwardKin(JointPos joint_pos, DescPose desc_pos); 

機器人正逆運動學計算代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestInverseKin(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        JointPos inverseRtn = new JointPos(){};

        robot.GetInverseKin(0, desc_pos1, -1, inverseRtn);
        robot.GetInverseKinRef(0, desc_pos1, j1, inverseRtn);

        int hasResut = 0;
        robot.GetInverseKinHasSolution(0, desc_pos1, j1);

        DescPose forwordResult = new DescPose(){};
        robot.GetForwardKin(j1, forwordResult);

        return 0;
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

獲取機器人DH參數補償值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人DH參數補償值
    * @param dhCompensation 機器人DH參數補償值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 錯誤碼
    */
    public int GetDHCompensation(Object[] dhCompensation)

獲取控制箱SN碼
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取控制箱SN碼
    * @param [out] SNCode 控制箱SN碼
    * @return 錯誤碼
    */
    int GetRobotSN(String[] SNCode);

查詢機器人示教管理點位數據代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetTeachPoint(Robot robot)
    {
        String name = "P1";
        List<Number> data=new ArrayList<>();
        data = robot.GetRobotTeachingPoint(name);
        System.out.println(name+" name is: "+data.get(0));
        for (int i = 0; i < 20; i++)
        {
            System.out.println("data is: "+ data.get(i+1));
        }

        int[] que_len = {0};
        int rtn = robot.GetMotionQueueLength(que_len);
        System.out.println("GetMotionQueueLength rtn is:"+rtn+", queue length is:"+ que_len[0]);

        Object[] dh = new Object[]{ 0,0,0,0,0,0 };
        int retval = 0;
        retval = robot.GetDHCompensation(dh);
        System.out.println("retval is: "+retval);

        String[] SN = new String[]{""};
        robot.GetRobotSN(SN);
        System.out.println("robot SN is "+SN[0]);
        return 0;
    }

根據編號獲取工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-V3.9.8

.. code-block:: Java
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
    int GetToolCoordWithID(int id, DescPose coord, int[] type, int[] install, int[] toolID, int[] loadNo)

根據編號獲取工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-V3.9.8

.. code-block:: Java
    :linenos:

    /**
    * @brief 根據編號獲取工件座標系
    * @param [in] id 工件座標系編號
    * @param [out] coord 座標系數值
    * @param [out] refFrame 參考座標系
    * @return 錯誤碼
    */
    public int GetWObjCoordWithID(int id, DescPose coord, int[] refFrame)

根據編號獲取外部工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-V3.9.8

.. code-block:: Java
    :linenos:

    /**
    * @brief 根據編號獲取外部工具座標系
    * @param [in] id 外部工具座標系編號，20-39對應外部工具座標系0-19
    * @param [out] coord 機器人外部固定工具TCP位姿
    * @param [out] tcoord 機器人末端安裝工件座標系位姿
    * @return 錯誤碼
    */
    public int GetExToolCoordWithID(int id, DescPose coord, DescPose tcoord)

根據編號獲取擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-V3.9.8

.. code-block:: Java
    :linenos:

    /**
    * @brief 根據編號獲取擴展軸座標系
    * @param [in] id 外部工具座標系編號
    * @param [out] coord 座標系數值
    * @param [out] axisCoordNum 擴展軸號；bit0-bit3對應擴展軸1-擴展軸4；如axisCoordNum值為3，對應應用擴展軸[1，2]
    * @param [out] calibFlag 標定標誌；0-未標定；1-已標定
    * @return 錯誤碼
    */
    public int GetExAxisCoordWithID (int id, DescPose coord, int[] axisCoordNum, int[] calibFlag)

獲取當前工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前工具座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurToolCoord(DescPose coord)

獲取當前工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前工件座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurWObjCoord(DescPose coord)

獲取當前外部工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前外部工具座標系
     * @param  [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurExToolCoord(DescPose coord)

獲取當前擴展軸座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前擴展軸座標系
     * @param [out] coord 座標系數值
     * @return 錯誤碼
     */
    public int GetCurExAxisCoord(DescPose coord)

獲取機器人座標系及負載代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestCoord(Robot robot)
    {
        int id = 1;
        DescPose toolCoord = new DescPose();
        DescPose extoolCoord = new DescPose();
        DescPose exworkpieceCoord = new DescPose();
        DescPose wobjCoord = new DescPose();
        DescPose exAxisCoord = new DescPose();
        int[] type = new int[1];
        int[] install = new int[1];
        int[] toolID = new int[1];
        int[] loadNo = new int[1];
        robot.GetToolCoordWithID(id, toolCoord, type, install, toolID, loadNo);
        System.out.printf("GetToolCoordWithID %d, %f %f %f %f %f %f,  type = %d, install = %d, toolID = %d, loadNo = %d\n", id,
            toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz, type[0], install[0], toolID[0], loadNo[0]);
        int[] refFrame = new int[1];
        robot.GetWObjCoordWithID(id, wobjCoord, refFrame);
        System.out.printf("GetWObjCoordWithID %d, %f %f %f %f %f %f, refFrame = %d\n", id,
            wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz, refFrame[0]);


        robot.GetExToolCoordWithID(21, extoolCoord, exworkpieceCoord);
        System.out.printf("GetExToolCoordWithID %d, %f %f %f %f %f %f\n", id,
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz,
            exworkpieceCoord.tran.x, exworkpieceCoord.tran.y, exworkpieceCoord.tran.z,
            exworkpieceCoord.rpy.rx, exworkpieceCoord.rpy.ry, exworkpieceCoord.rpy.rz);

        int[] axisCoordNum = new int[1];
        int[] calibFlag = new int[1];
        robot.GetExAxisCoordWithID(id, exAxisCoord, axisCoordNum, calibFlag);
        System.out.printf("GetExAxisCoordWithID %d, %f %f %f %f %f %f, axisCoordNum = %d, calibFlag = %d\n", id,
            exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz, axisCoordNum[0], calibFlag[0]);

        double[] weight = new double[1];
        DescTran cog = new DescTran();
        robot.GetTargetPayloadWithID(id, weight, cog);
        System.out.println("GetTargetPayload is " + weightT.get(0) + " cogT is  " + cogT.x + "  " + cogT.y + "  " + cogT.z);
        robot.GetCurToolCoord(toolCoord);
        System.out.printf("GetCurToolCoord %f %f %f %f %f %f\n",
            toolCoord.tran.x, toolCoord.tran.y, toolCoord.tran.z,
            toolCoord.rpy.rx, toolCoord.rpy.ry, toolCoord.rpy.rz);
        robot.GetCurWObjCoord(wobjCoord);
        System.out.printf("GetCurWObjCoord %f %f %f %f %f %f\n",
            wobjCoord.tran.x, wobjCoord.tran.y, wobjCoord.tran.z,
            wobjCoord.rpy.rx, wobjCoord.rpy.ry, wobjCoord.rpy.rz);
        robot.GetCurExToolCoord(extoolCoord);
        System.out.printf("GetExToolCoordWithID %f %f %f %f %f %f\n",
            extoolCoord.tran.x, extoolCoord.tran.y, extoolCoord.tran.z,
            extoolCoord.rpy.rx, extoolCoord.rpy.ry, extoolCoord.rpy.rz);
        robot.GetCurExAxisCoord(exAxisCoord);
        System.out.printf("GetCurExAxisCoord %f %f %f %f %f %f\n",
            exAxisCoord.tran.x, exAxisCoord.tran.y, exAxisCoord.tran.z,
            exAxisCoord.rpy.rx, exAxisCoord.rpy.ry, exAxisCoord.rpy.rz);
        DescTran cogT = new DescTran();
        List<Number> weightT = robot.GetTargetPayload(0);
        robot.GetTargetPayloadCog(0, cogT);
        System.out.printf("GetTargetPayload %f %f %f %f\n", weightT.get(0),
            cogT.x, cogT.y, cogT.z);
        DescPose coordSet = new DescPose(0, 1, 2, 3, 4, 5);
        robot.SetToolCoord(1, coordSet, 0, 0, 1, 0);
        robot.SetWObjCoord(1, coordSet, 0);
        robot.SetLoadWeight(1, 1.3);
        cog.x = 10;
        cog.y = 20;
        cog.z = 30;
        robot.SetLoadCoord(1, cog);
        DescPose etcp = new DescPose(0, 0, 100, 0, 0, 0);
        DescPose etool = new DescPose(0, 0, 50, 0, 0, 0);
        int rtn = robot.SetExToolCoord(21, etcp, etool);
        System.out.printf("SetExToolCoord rtn is %d\n", rtn);
        robot.ExtAxisActiveECoordSys(1, 1, coordSet, 1);
        return 0;
    }