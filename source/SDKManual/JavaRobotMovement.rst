機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief jog 點動 
    * @param [in] refType 0-關節點動，2-基座標系下點動，4-工具坐標係下點動，8-工件坐標係下點動
    * @param [in] nb 1-關節1(或x軸)，2-關節2(或y軸)，3-關節3(或z軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param [in] dir 0-負方向，1-正方向
    * @param [in] vel 速度百分比，[0~100]
    * @param [in] acc 加速度百分比， [0~100]
    * @param [in] max_dis 單次點動最大角度，單位[°]或距離，單位[mm]
    * @return 錯誤碼 
    */ 
    int StartJOG(int refType, int nb, int dir, double vel, double acc, double max_dis);

jog點動减速停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  jog點動减速停止
    * @param  [in]  stopType  1-關節點動停止，3-基座標系下點動停止，5-工具坐標系下點動停止，9-工件坐標係下點動停止
    * @return  錯誤碼
    */
    int StopJOG(int stopType);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    int ImmStopJOG(); 

代碼範例
+++++++++++++++++++++++++++++
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
        robot.StartJOG(0, 1, 0, 30, 100, 90);//關節點動
        robot.Sleep(3000);
        robot.StopJOG(1);//點動減速停止
        robot.StartJOG(0, 1, 0, 30, 100, 90);//關節點動
        robot.Sleep(3000);
        robot.ImmStopJOG();//點動立即停止
    }    

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos  目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

笛卡兒空間直線運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡兒空間直線運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @param  [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，預設為0
    * @param  [in] speedPercent  允許降速閾值百分比[0-100]，預設為10%
    * @return  錯誤碼
    */   
    int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int overSpeedStrategy, int speedPercent);

笛卡兒空間圓弧運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡兒空間圓弧運動
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos_p  位元位偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos_t  位元位偏移量
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm 
    * @return  錯誤碼
    */      
    int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR);

笛卡兒空間整圓運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡兒空間整圓運動
    * @param  [in] joint_pos_p  路徑點1關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點1笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] joint_pos_t  路徑點2關節位置,單位deg
    * @param  [in] desc_pos_t   路徑點2笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */      
    int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos);

代碼範例
+++++++++++++++++++++++++++++
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
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        JointPos JP2=new JointPos(72.515,-86.774,81.525,-87.724,-91.964,92.958);
        DescPose DP2=new DescPose(-63.512,-529.698,517.946,-178.192,3.07,69.554);
        JointPos JP3=new JointPos(89.281,-102.959,81.527,-69.955,-86.755,92.958);
        DescPose DP3=new DescPose();
        robot.GetForwardKin(JP3,DP3);

        robot.MoveJ(JP1, DP1,0, 0, 30, 30, 100, epos, -1, 0, offset_pos);//關節空間運動
        robot.MoveL(JP2, DP2,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);//直線運動
        robot.MoveC(JP3, DP3, 0, 0, 30, 100, epos, 0, offset_pos, JP1, DP1, 0, 0, 100, 100, epos, 0, offset_pos, 100, -1);
        robot.Circle(JP3, DP3, 0, 0, 10, 100.0, epos, JP2, DP2, 0, 0, 100.0, 100.0, epos, 100.0, 0, offset_pos);

    }    

笛卡兒空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡兒空間螺旋線運動 
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡兒位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos  位元位偏移量
    * @return 錯誤碼 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param);

代碼範例
+++++++++++++++++++++++++++++
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
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        JointPos JP1=new JointPos(117.408,-86.777,81.499,-87.788,-92.964,92.959);
        DescPose DP1 =new DescPose(327.359,-420.973,518.377,-177.199,3.209,114.449);
        SpiralParam param = new SpiralParam(5,10.0,30.0,10.0,5.0,0);//螺旋线
        robot.NewSpiral(JP1, DP1, 0, 0, 50, 100, epos, 100, 0, offset_pos, param);
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveStart();

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveEnd();

關節空間伺服模式運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] axisPos  外部軸位置,單位mm
    * @param  [in] acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @return  錯誤碼
    */
    int ServoJ(JointPos joint_pos, ExaxisPos axisPos, double acc, double vel, double cmdT, double filterT, double gain);

代碼範例
+++++++++++++++++++++++++++++
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
        JointPos j5 = new JointPos();
        ExaxisPos ePos=new ExaxisPos();
        int ret = robot.GetActualJointPosDegree(j5);
        if (ret == 0)
        {
            int count = 200;
            while (count > 0)
            {
                robot.ServoJ(j5, ePos,100, 100, 0.008, 0, 0);
                j5.J1 += 0.2;//1關節位置增加
                count -= 1;
                robot.WaitMs((int)(8));
            }
        }
    }


笛卡兒空間伺服模式運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡兒空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基底座標系)，1-增量運動(基底座標系)，2-增量運動(工具坐標系)
    * @param  [in]  desc_pose  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位元姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in]  acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in]  vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in]  cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in]  filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in]  gain  目標位置的比例放大器，暫不開放，預設為0
    * @return  錯誤碼
    */
    int ServoCart(int mode, DescPose desc_pose, Object[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain);

代碼範例
+++++++++++++++++++++++++++++
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
        DescPose desc_pos_dt = new DescPose(0, 0, 0, 0, 0, 0);
        desc_pos_dt.tran.z = -0.5;
        Object[] pos_gain = { 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 };//仅z軸增加
        int mode = 2;//工具座標系下增量運動
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        int count = 200;

        robot.SetSpeed(20);

        while (count > 0)
        {
            robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            robot.WaitMs((int)(cmdT * 1000));
        }
    }

笛卡兒空間點到點運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 笛卡兒空間點到點運動 
    * @param [in] desc_pos  目標笛卡爾位姿或位姿增量
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] config  關節空間配置，[-1]-參考目前關節位置解算，[0~7]-參考特定關節空間配置解算，預設為-1
    * @return 錯誤碼 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendT, int config);

代碼範例
+++++++++++++++++++++++++++++
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
        DescPose DP2=new DescPose(-63.512,-529.698,517.946,-178.192,3.07,69.554);
        robot.MoveCart(DP2, 0, 0, 30.0, 100.0, 100.0, -1.0, -1);
    }

樣條運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    int SplineStart();

關節空間樣條運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間樣條運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @return  錯誤碼
    */
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl);

樣條運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    int SplineEnd(); 

代碼範例
+++++++++++++++++++++++++++++
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
        DescPose  desc_p1, desc_p2, desc_p3, desc_p4;//笛卡兒空間位置与姿态
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p4 = new DescPose(0, 0, 0, 0, 0, 0);

        desc_p1.tran.x = -104.846;
        desc_p1.tran.y = 309.573;
        desc_p1.tran.z = 336.647;
        desc_p1.rpy.rx = 179.681;
        desc_p1.rpy.ry = -0.419;
        desc_p1.rpy.rz = -92.692;

        desc_p2.tran.x = -318.287;
        desc_p2.tran.y = 158.502;
        desc_p2.tran.z = 346.184;
        desc_p2.rpy.rx = 179.602;
        desc_p2.rpy.ry = 1.081;
        desc_p2.rpy.rz = -46.342;

        desc_p3.tran.x = -352.414;
        desc_p3.tran.y = 24.059;
        desc_p3.tran.z = 395.376;
        desc_p3.rpy.rx = 179.755;
        desc_p3.rpy.ry = -1.045;
        desc_p3.rpy.rz = -23.877;

        desc_p4.tran.x = 195.474;
        desc_p4.tran.y = 423.278;
        desc_p4.tran.z = 228.509;
        desc_p4.rpy.rx = -179.199;
        desc_p4.rpy.ry = -0.567;
        desc_p4.rpy.rz = -130.209;

        JointPos j1 = new JointPos();
        JointPos j2 = new JointPos();
        JointPos j3 = new JointPos();
        JointPos j4 = new JointPos();
        robot.GetInverseKin(0, desc_p1, -1, j1);//逆向運動学求解
        robot.GetInverseKin(0, desc_p2, -1, j2);
        robot.GetInverseKin(0, desc_p3, -1, j3);
        robot.GetInverseKin(0, desc_p4, -1, j4);
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveJ(j1, desc_p1,4, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.SplineStart();
        robot.SplinePTP(j4, desc_p4, 0, 0, 100, 100, 100);
        robot.SplinePTP(j1, desc_p1, 0, 0, 100, 100, 100);
        robot.SplinePTP(j2, desc_p2, 0, 0, 100, 100, 100);
        robot.SplinePTP(j3, desc_p3, 0, 0, 100, 100, 100);
        robot.SplineEnd();
    }

新樣條運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @param [in] type   0-圓弧過渡，1-給定點位為路徑點
    * @param [in] averageTime  全域平均銜接時間(ms)(10 ~ )，預設2000
    * @return 錯誤碼 
    */ 
    int NewSplineStart(int type, int averageTime);
    
新樣條指令點
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 增加樣條運動指令點 
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡兒位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag 是否為最後一個點，0-否，1-是
    * @return 錯誤碼 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag);

新樣條運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新樣條運動結束 
    * @return 錯誤碼 
    */ 
    int NewSplineEnd();
    
終止運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    int StopMotion();

暫停運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
      * @brief 暫停運動 
      * @return 錯誤碼 
    */  
    int PauseMotion();

恢復運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 恢復運動 
    * @return 錯誤碼 
    */ 
    int ResumeMotion();

點位整體偏移開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in]  offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


點位整體偏移結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    int PointsOffsetDisable(); 

代碼範例
+++++++++++++++++++++++++++++
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
        DescPose desc_p1 =new DescPose(-104.846, 309.573, 336.647, 179.681, -0.419, -92.692);
        DescPose desc_p2=new DescPose(-194.846, 309.573, 336.647, 179.681,-0.419, -92.692;);
        DescPose desc_p3=new DescPose(-254.846, 259.573,336.647, 179.681, -0.419, -92.692;);
        DescPose desc_p4=new DescPose(-304.846,259.573, 336.647, 179.681, -0.419, -92.692;);
        JointPos j1 = new JointPos();
        JointPos j2 = new JointPos();
        JointPos j3 = new JointPos();
        JointPos j4 = new JointPos();
        robot.GetInverseKin(0, desc_p1, -1, j1);//逆向運動学求解
        robot.GetInverseKin(0, desc_p2, -1, j2);
        robot.GetInverseKin(0, desc_p3, -1, j3);
        robot.GetInverseKin(0, desc_p4, -1, j4);
        robot.MoveCart(desc_p1, 0, 0, 100.0, 100.0, 100.0, -1.0, -1);
        robot.NewSplineStart(0, 5000);//新样条開始
        robot.NewSplinePoint(j1, desc_p1, 0, 0, 100, 100, 100, 50, 0);//新樣條指令點
        robot.NewSplinePoint(j2, desc_p2, 0, 0, 100, 100, 100, 50, 0);
        robot.NewSplinePoint(j3, desc_p3, 0, 0, 100, 100, 100, 50, 0);
        robot.NewSplinePoint(j4, desc_p4, 0, 0, 100, 100, 100, 50, 1);
        robot.NewSplineEnd();//新样条结束

        DescPose off = new DescPose(0, 0, 100, 0, 0, 0);
        robot.PointsOffsetEnable(0, off);
        robot.MoveL(j1, desc_p1,0, 0, 100, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.PointsOffsetDisable();
    }

控制箱AO飛拍開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飛拍開始
    * @param [in] AONum 控制箱AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，預設100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，預設為20%，範圍[0-100]
    * @return 錯誤碼
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飛拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    int MoveAOStop();
    
末端AO飛拍開始
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飛拍開始
    * @param [in] AONum 末端AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，預設100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，預設為20%，範圍[0-100]
    * @return 錯誤碼
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飛拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    int MoveToolAOStop();

代碼範例
+++++++++++++++++++++++++++++
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
        robot.MoveToolAOStart(0, 100, 80, 1);//末端AO飛拍開始
        //robot.MoveAOStart(0, 100, 80, 1);//控制箱AO飛拍
        DescPose  desc_p1, desc_p2;

        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos j1 = new JointPos(-81.684,-106.159,-74.447,-86.33,94.725,41.639);
        JointPos j2 = new JointPos(-102.804,-106.159,-74.449,-86.328,94.715,41.639);

        robot.GetForwardKin(j1,desc_p1);
        robot.GetForwardKin(j2,desc_p2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveL(j1, desc_p1,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.MoveL(j2, desc_p2,0, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.MoveToolAOStop();
        //robot.MoveAOStop();
    }