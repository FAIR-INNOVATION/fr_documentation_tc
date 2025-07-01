機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief jog 點動 
    * @param [in] refType 點動類型：0-關節點動，2-基座標系下點動，4-工具坐標系下點動，8-工件坐標系下點動
    * @param [in] nb 1-關節1(或x 軸)，2-關節2(或y 軸)，3-關節3(或z 軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param [in] dir 0-負方向，1-正方向 
    * @param [in] vel 速度百分比，[0~100] 
    * @param [in] acc 加速度百分比， [0~100] 
    * @param [in] max_dis 單次點動最大角度，單位[°]或距離，單位[mm]
    * @return 錯誤碼 
    */ 
    int StartJOG(byte refType, byte nb, byte dir, float vel, float acc, float max_dis);

jog點動减速停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  jog點動减速停止
    * @param  [in]  ref  1-關節點動停止，3-基座標系下點動停止，5-工具坐標系下點動停止，9-工件坐標係下點動停止
    * @return  錯誤碼
    */
    int StopJOG(byte stopType);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    int ImmStopJOG(); 

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJOG_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        robot.SetSpeed(35);
        robot.StartJOG(0, 1, 0, 15, 20.0f, 30.0f);   //單關節運動，StartJOG為非阻塞指令，運動狀態下接收其他運動指令（包含StartJOG）会被丢弃
        Thread.Sleep(1000);
        robot.StopJOG(1);  //機器人單軸點動減速停止
        //robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(0, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(0, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(2, 1, 0, 15, 20.0f, 30.0f);   //基座標系下點動
        Thread.Sleep(1000);
        robot.StopJOG(3);  //機器人單軸點動減速停止
        //robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(2, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(2, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(4, 1, 0, 15, 20.0f, 30.0f);   //工具座標系下點動
        Thread.Sleep(1000);
        robot.StopJOG(5);  //機器人單軸點動減速停止
        //robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(4, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(4, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();

        robot.StartJOG(8, 1, 0, 15, 20.0f, 30.0f);   //工件座標系下點動
        Thread.Sleep(1000);
        robot.StopJOG(9);  //機器人單軸點動減速停止
        //robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(8, 2, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 3, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 4, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 5, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
        robot.StartJOG(8, 6, 1, 15, 20.0f, 30.0f);
        Thread.Sleep(1000);
        robot.ImmStopJOG();
    }

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  關節空間運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos); 

笛卡兒空間直線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos, int overSpeedStrategy = 0, int speedPercent = 10); 

笛卡兒空間圓弧運動
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, byte poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, byte toffset_flag, DescPose offset_pos_t, float ovl, float blendR); 

笛卡兒空間整圓運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
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
    * @param  [in] oacc 加速度百分比
    * @param  [in] blendR -1：阻塞；0~1000：平滑半徑，單位mm
    * @return  錯誤碼
    */      
    int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, float ovl, byte offset_flag, DescPose offset_pos);

代碼範例
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
.. code-block:: c#
    :linenos:


    private void btnMovetest_Click(object sender, EventArgs e)
    {
        int rtn = 0;
        DescPose middescPoseCir1 = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosCir1 = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseCir1 = new DescPose(-524.862, -217.402, 308.459, -171.425, -4.810, 156.088);
        JointPos endjointPosCir1 = new JointPos(11.399, -78.055, 104.603, -125.421, -85.770, -54.721);

        DescPose middescPoseCir2 = new DescPose(-482.691, -587.899, 318.594, -171.001, -4.999, -172.996);
        JointPos midjointPosCir2 = new JointPos(42.314, -53.600, 67.296, -112.969, -85.533, -54.721);
        DescPose enddescPoseCir2 = new DescPose(-403.942, -489.061, 317.038, -163.189, -10.425, -175.627);
        JointPos endjointPosCir2 = new JointPos(39.959, -70.616, 96.679, -134.243, -82.276, -54.721);

        DescPose middescPoseMoveC = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosMoveC = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseMoveC = new DescPose(-524.862, -217.402, 308.459, -171.425, -4.810, 156.088);
        JointPos endjointPosmoveC = new JointPos(11.399, -78.055, 104.603, -125.421, -85.770, -54.721);

        DescPose middescPoseCir3 = new DescPose(-435.414, -342.926, 309.205, -171.382, -4.513, 171.520);
        JointPos midjointPosCir3 = new JointPos(26.804, -79.866, 106.642, -125.433, -85.562, -54.721);
        DescPose enddescPoseCir3 = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos endjointPosCir3 = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose middescPoseCir4 = new DescPose(-482.691, -587.899, 318.594, -171.001, -4.999, -172.996);
        JointPos midjointPosCir4 = new JointPos(42.314, -53.600, 67.296, -112.969, -85.533, -54.721);
        DescPose enddescPoseCir4 = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos endjointPosCir4 = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose startdescPose = new DescPose(-569.505, -405.378, 357.596, -172.862, -10.939, 171.108);
        JointPos startjointPos = new JointPos(27.138, -63.750, 78.586, -117.861, -90.588, -54.721);

        DescPose linedescPose = new DescPose(-403.942, -489.061, 317.038, -163.189, -10.425, -175.627);
        JointPos linejointPos = new JointPos(39.959, -70.616, 96.679, -134.243, -82.276, -54.721);


        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);


        robot.MoveJ(startjointPos, startdescPose, 3, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.Circle(midjointPosCir1, middescPoseCir1, 3, 0, 100, 100, exaxisPos, endjointPosCir1, enddescPoseCir1, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle1" + rtn);



        rtn = robot.Circle(midjointPosCir2, middescPoseCir2, 3, 0, 100, 100, exaxisPos, endjointPosCir2, enddescPoseCir2, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle2" + rtn);

        robot.MoveC(midjointPosMoveC, middescPoseMoveC, 3, 0, 100, 100, exaxisPos, 0, offdese, endjointPosmoveC, enddescPoseMoveC, 3, 0, 100, 100, exaxisPos, 0, offdese, 100, 20);
        rtn = robot.Circle(midjointPosCir3, middescPoseCir3, 3, 0, 100, 100, exaxisPos, endjointPosCir3, enddescPoseCir3, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle3" + rtn);
        rtn = robot.MoveL(linejointPos, linedescPose, 3, 0, 100, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        Console.WriteLine("MoveL " + rtn);
        rtn = robot.Circle(midjointPosCir4, middescPoseCir4, 3, 0, 100, 100, exaxisPos, endjointPosCir4, enddescPoseCir4, 3, 0, 100, 100, exaxisPos, 100, -1, offdese, 100, 20);
        Console.WriteLine("Circle4" + rtn);
    }

笛卡兒空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡兒空間螺旋線運動 
    * @param [in] joint_pos 目標關節位置,單位 deg 
    * @param [in] desc_pos 目標笛卡兒位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] epos 擴展軸位置，單位 mm 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移 
    * @param [in] offset_pos 位元位偏移量 
    * @param [in] spiral_param 螺旋參數 
    * @return 錯誤碼 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, ExaxisPos epos, float ovl, byte offset_flag, DescPose offset_pos, SpiralParam spiral_param); 

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescSpiral_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        JointPos j;
        DescPose desc_pos;
        DescPose offset_pos1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos2 = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp;

        j = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        offset_pos1.tran.x = 50.0;
        offset_pos1.rpy.rx = -30.0;
        offset_pos2.tran.x = 50.0;
        offset_pos2.rpy.rx = -5.0;

        sp.circle_num = 5;
        sp.circle_angle = 1.0f;
        sp.rad_init = 10.0f;
        sp.rad_add = 40.0f;
        sp.rotaxis_add = 10.0f;
        sp.rot_direction = 0;

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        byte flag = 2;

        robot.SetSpeed(20);
        int ret = robot.GetForwardKin(j, ref desc_pos);  //只有關節位置的情况下，可用正運動学接口求解笛卡兒空间座標
        if (ret == 0)
        {
            int err = -1;
            err = robot.MoveJ(j, desc_pos, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
            Console.WriteLine($"movej errcode:  {err}");

            err = robot.NewSpiral(j, desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp);
            Console.WriteLine($"newspiral errcode:  {err}");
        }
        else
        {
            Console.WriteLine($"GetForwardKin errcode: {ret}");
        }
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveStart();

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveEnd();

關節空間伺服模式運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @param  [in] id servoJ指令ID,默認爲0
    * @return  錯誤碼
    */
    int ServoJ(JointPos joint_pos, float acc, float vel, float cmdT, float filterT, float gain);

代碼範例
++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void btnJointServoMove_Click(object sender, EventArgs e)
    {
        JointPos j = new JointPos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 500;
        float dt = 0.1f;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, ref j);
        if (ret == 0)
        {
            robot.ServoMoveStart();

            try
            {
                while (count > 0)
                {

                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID);


                    j.jPos[0] += dt;
                    count--;


                    robot.WaitMs((int)(cmdT * 1000));
                }
            }
            finally
            {

                robot.ServoMoveEnd();
            }
        }
        else
        {
            Console.WriteLine($"GetActualJointPosDegree error code: {ret}");

        }
    }

笛卡兒空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡兒空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基底座標系)，1-增量運動(基底座標系)，2-增量運動(工具坐標系)
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位元姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @return  錯誤碼
    */
    int ServoCart(int mode, DescPose desc_pos, double[] pos_gain, float acc, float vel, float cmdT, float filterT, float gain);

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescServoMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose desc_pos_dt = new DescPose(0, 0, 0, 0, 0, 0);
        desc_pos_dt.tran.z = -0.5;
        double[] pos_gain = new double[6]{ 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 };
        int mode = 2;
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        int flag = 0;
        int count = 500;

        robot.SetSpeed(20);
        while (count > 0)
        {
            robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            robot.WaitMs((int)(cmdT * 1000));
        }
    }

笛卡兒空間點到點運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 笛卡兒空間點到點運動 
    * @param [in] desc_pos 基坐標系下目標笛卡兒位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位 ms 
    * @param [in] config 關節空間配置，[-1]-參考目前關節位置解算，[0~7]-參考特定關節空間配置解算，預設為-1 
    * @return 錯誤碼 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescPTPMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        DescPose desc_pos1, desc_pos2, desc_pos3;
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);
        desc_pos3 = new DescPose(-345.155, 535.733, 421.269, 179.475, 0.571, 18.332);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendT1 = 0.0f;
        int config = -1;

        robot.SetSpeed(20);
        robot.MoveCart(desc_pos1, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(desc_pos2, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(desc_pos3, tool, user, vel, acc, ovl, blendT1, config);
    }

樣條運動開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    int SplineStart();

樣條運動PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl);

樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    int SplineEnd(); 

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSplineMove_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        JointPos j1, j2, j3, j4;
        DescPose desc_pos1, desc_pos2, desc_pos3, desc_pos4, offset_pos;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        j2 = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);

        j3 = new JointPos(-49.129, -68.49, 103.297, -128.898, -91.478, -0.062);
        desc_pos3 = new DescPose(-680.308, 547.378, 399.189, -175.909, -1.479, 40.827);

        j4 = new JointPos(-56.126, -54.093, 80.686, -121.655, -91.428, -0.064);
        desc_pos4 = new DescPose(-719.201, 790.816, 389.118, -174.939, -1.428, 33.809);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;
        robot.SetSpeed(20);
        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");
                
        robot.SplineStart();
        robot.SplinePTP(j1, desc_pos1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, desc_pos2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, desc_pos3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, desc_pos4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
    }

新樣條運動開始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @param [in] type  0-圓弧過渡，1-給定點位為路徑點
    * @param [in] averageTime  全域平均銜接時間(ms)(10 ~ )，預設2000
    * @return 錯誤碼 
    */ 
    int NewSplineStart(int type, int averageTime=2000);
    
新樣條指令點
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 增加樣條運動指令點 
    * @param [in] joint_pos 目標關節位置,單位 deg 
    * @param [in] desc_pos 目標笛卡兒位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag  是否為最後一個點，0-否，1-是
    * @return 錯誤碼 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 新樣條運動結束 
    * @return 錯誤碼 
    */ 
    int NewSplineEnd();
    
終止運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    int StopMotion();

暫停運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
      * @brief 暫停運動 
      * @return 錯誤碼 
    */  
    int PauseMotion();

恢復運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 恢復運動 
    * @return 錯誤碼 
    */ 
    int ResumeMotion();

點位整體偏移開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


點位整體偏移結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    int PointsOffsetDisable(); 

代碼範例
++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnPointOffect_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        JointPos j1, j2;
        DescPose desc_pos1, desc_pos2, offset_pos, offset_pos1;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-58.982, -90.717, 127.647, -129.041, -87.989, -0.062);
        desc_pos1 = new DescPose(-437.039, 411.064, 426.189, -177.886, 2.007, 31.155);

        j2 = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        desc_pos2 = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos1 = new DescPose(50.0, 50.0, 50.0, 5.0, 5.0, 5.0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        float blendR = 0.0f;
        byte flag = 0;
        int type = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetEnable(type, offset_pos1);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.PointsOffsetDisable();
    }

控制箱AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    int MoveAOStop();
    
末端AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    int MoveToolAOStop();

代碼範例
************
.. code-block:: c#
    :linenos:

    private void btnMoveAO_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose();
        JointPos startjointPos = new JointPos();
        DescPose enddescPose = new DescPose();
        JointPos endjointPos = new JointPos();
        DescPose CPose = new DescPose();
        JointPos CJPos = new JointPos();
        DescPose DPose = new DescPose();
        JointPos DJPos = new JointPos();            
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.MoveToolAOStart(0, 100, 80, 1);
        //int rtn = robot.MoveAOStart(0, 100, 80, 1);
        Console.WriteLine(rtn);

        rtn = robot.MoveL(startjointPos, startdescPose, 0, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        //robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, 0, 0, offdese);
        //robot.MoveC(startjointPos, startdescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, 0);
        //robot.Circle(startjointPos, startdescPose, 0, 0, 100, 100, exaxisPos, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 100, 0, offdese);
        //robot.SplineStart();
        //robot.SplinePTP(startjointPos, startdescPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(endjointPos, enddescPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(CJPos, CPose, 0, 0, 100, 100, 100);
        //robot.SplinePTP(DJPos, DPose, 0, 0, 100, 100, 100);
        //robot.SplineEnd();

        //robot.NewSplineStart(0, 5000);
        //robot.NewSplinePoint(startjointPos, startdescPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(endjointPos, enddescPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(CJPos, CPose, 0, 0, 100, 100, 100, 5, 0);
        //robot.NewSplinePoint(DJPos, DPose, 0, 0, 100, 100, 100, 5, 1);
        //robot.NewSplineEnd();
        //int count = 1000;
        //while (count > 0)
        //{
        //    robot.ServoJ(startjointPos, 0, 0, 0.008f, 0, 0);
        //    startjointPos.jPos[0] += 0.01;//0關節位置增加
        //    count -= 1;
        //}
        rtn = robot.MoveToolAOStop();
        //rtn = robot.MoveAOStop();
        Console.WriteLine(rtn);
    }

開始奇異位姿保護
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 開始奇異位姿保護
    * @param [in] protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
    * @param [in] minShoulderPos 肩奇異調整範圍(mm), 默認100
    * @param [in] minElbowPos 肘奇異調整範圍(mm), 默認50
    * @param [in] minWristPos 腕奇異調整範圍(°), 默認10
    * @return 錯誤碼
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇異位姿保護
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 停止奇異位姿保護
    * @return 錯誤碼
    */
    int SingularAvoidEnd();

代碼範例
************
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void btnTestSingularAvoidEArc_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(-352.437, -88.350, 226.471, 177.222, 4.924, 86.631);
        JointPos startjointPos = new JointPos(-3.463, -84.308, 105.579, -108.475, -85.087, -0.334);

        DescPose middescPose = new DescPose(-518.339, -23.706, 207.899, -178.420, 0.171, 71.697);
        JointPos midjointPos = new JointPos(-8.587, -51.805, 64.914, -104.695, -90.099, 9.718);

        DescPose enddescPose = new DescPose(-273.934, 323.003, 227.224, 176.398, 2.783, 66.064);
        JointPos endjointPos = new JointPos(-63.460, -71.228, 88.068, -102.291, -90.149, -39.605);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveL(startjointPos, startdescPose, 0, 0, 50, 100, 100, -1, exaxisPos, 0, 0, offdese, 1, 1);
        robot.SingularAvoidStart(1, 100, 50, 10);
        robot.MoveC(midjointPos, middescPose, 0, 0, 50, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1);
        robot.SingularAvoidEnd();
    }

安全停止觸發
++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 安全停止觸發訊號
 * @return 錯誤碼
 */
 int GetSafetyCode();

開始Ptp運動FIR濾波
++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
 :linenos:

 /**
 * @brief 開始Ptp運動FIR濾波
 * @param [in] maxAcc 最大加速度極值(deg/s2)
 * @param [in] maxJek 統一關節急動度極值(deg/s3)
 * @return 錯誤碼
 */
    int PtpFIRPlanningStart(double maxAcc, double maxJek=1000);

關閉Ptp運動FIR濾波
++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 關閉Ptp運動FIR濾波
 * @return 錯誤碼
 */
 int PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 開始LIN、ARC運動FIR濾波
 * @param [in] maxAccLin 線加速度極值(mm/s2)
 * @param [in] maxAccDeg 角加速度極值(deg/s2)
 * @param [in] maxJerkLin 線加加速度極值(mm/s3)
 * @param [in] maxJerkDeg 角加加速度極值(deg/s3)
 * @return 錯誤碼
 */
 int LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

關閉LIN、ARC運動FIR濾波
++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 關閉LIN、ARC運動FIR濾波
 * @return 錯誤碼
 */
 int LinArcFIRPlanningEnd();

程式範例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
 :linenos:


    private void button69_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos midjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos endjointPos = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose middescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose enddescPose = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.PtpFIRPlanningStart(1000,1000);
        Console.WriteLine("PtpFIRPlanningStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.PtpFIRPlanningEnd();
        Console.WriteLine("PtpFIRPlanningEnd rtn is " + rtn);

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        Console.WriteLine("LinArcFIRPlanningStart rtn is " + rtn);
        robot.MoveL( startjointPos,  startdescPose, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese, 1, 1);
        robot.MoveC( midjointPos,  middescPose, 0, 0, 100, 100,  exaxisPos, 0,  offdese,  endjointPos,  enddescPose, 0, 0, 100, 100,  exaxisPos, 0,  offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        Console.WriteLine("LinArcFIRPlanningEnd rtn is " + rtn);
    }

加速度平滑開啟
++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 加速度平滑開啟
    * @param  [in] saveFlag 是否斷電保存
    * @return  錯誤碼
    */
    int AccSmoothStart(bool saveFlag);

加速度平滑關閉
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 加速度平滑關閉
    * @param  [in] saveFlag 是否斷電保存
    * @return  錯誤碼
    */
    int AccSmoothEnd(bool saveFlag);

代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

        private void button1_Click(object sender, EventArgs e)
        {

            bool saveFlag = false;

            int rtn = 0;
            JointPos p1Joint = new JointPos(88.927, -85.834, 80.289, -85.561, -91.388, 108.718);
            DescPose p1Desc = new DescPose(88.739, -527.617, 514.939, -179.039, 1.494, 70.209);

            JointPos p2Joint = new JointPos(27.036, -83.909, 80.284, -85.579, -90.027, 108.604);
            DescPose p2Desc = new DescPose(-433.125, -334.428, 497.139, -179.723, -0.745, 8.437);
            JointPos p3Joint = new JointPos(60.219, -94.324, 62.906, -62.005, -87.159, 108.598);
            DescPose p3Desc = new DescPose(-112.215, -409.323, 686.497, 176.217, 2.338, 41.625);
            ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
            DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
            robot.AccSmoothStart(saveFlag);
            robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);
            robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);
            robot.MoveL(p1Joint, p1Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);
            robot.MoveL(p2Joint, p2Desc, 0, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 10);

            robot.AccSmoothEnd(saveFlag);
        }
