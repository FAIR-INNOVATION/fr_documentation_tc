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
    * @param [in] refType 點動類型：0-關節點動，2-基座標系下點動，4-工具座標系下點動，8-工件座標系下點動 
    * @param [in] nb 1-關節 1(或 x 軸)，2-關節 2(或 y 軸)，3-關節 3(或 z 軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param [in] dir 0-負方向，1-正方向 
    * @param [in] vel 速度百分比，[0~100] 
    * @param [in] acc 加速度百分比， [0~100] 
    * @param [in] max_dis 單次點動最大角度，單位[°]或距離，單位[mm] 
    * @return 錯誤碼 
    */ 
    int StartJOG(byte refType, byte nb, byte dir, float vel, float acc, float max_dis);

jog點動減速停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  jog點動減速停止
    * @param  [in]  ref  1-關節點動停止，3-基座標系下點動停止，5-工具座標系下點動停止，9-工件座標系下點動停止
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

機器人點動控制代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJOG_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2"); 

        robot.SetSpeed(35);
        robot.StartJOG(0, 1, 0, 15, 20.0f, 30.0f);   //單關節運動，StartJOG爲非阻塞指令，運動狀態下接收其他運動指令（包含StartJOG）會被丟棄
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
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos); 

笛卡爾空間直線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm    
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認爲0
    * @param  [in] speedPercent  允許降速閾值百分比[0-100]，默認10%
    * @return  錯誤碼
    */   
    int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos, int overSpeedStrategy = 0, int speedPercent = 10); 

笛卡爾空間圓弧運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_t  位姿偏移量   
    * @param  [in] ovl  速度縮放因子，範圍[0~100]    
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm    
    * @return  錯誤碼
    */      
    int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, byte poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, byte toffset_flag, DescPose offset_pos_t, float ovl, float blendR); 

笛卡爾空間點到點運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 笛卡爾空間點到點運動 
    * @param [in] desc_pos 基座標系下目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位 ms 
    * @param [in] config 關節空間配置，[-1]-參考當前關節位置解算，[0~7]-參考特定關節空間配置解算，默認爲-1 
    * @return 錯誤碼 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

笛卡爾空間整圓運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間整圓運動
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
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量   
    * @param  [in] oacc 加速度百分比
    * @param  [in] blendR -1：阻塞；0~1000：平滑半徑，單位mm
    * @return  錯誤碼
    */      
    int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, float ovl, int offset_flag, DescPose offset_pos, double oacc=100, double blendR=-1);

笛卡爾空間整圓運動代碼示例
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

機器人基本運動指令代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMovetest_Click(object sender, EventArgs e)
    {
        JointPos j1= new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4 = new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4 = new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;

        robot.SetSpeed(20);
        int rtn;
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"MoveJ errcode:{rtn}" );

        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR,epos, search, flag, offset_pos);
        Console.WriteLine($"MoveL errcode:{rtn}");

        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR);
        Console.WriteLine($"MoveC errcode:{rtn}");

        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine("MoveJ errcode:%d\n", rtn);

        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos);
        Console.WriteLine($"Circle errcode:{rtn}");

        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        Console.WriteLine($"MoveCart errcode:{rtn}");

    }

笛卡爾空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間螺旋線運動 
    * @param [in] joint_pos 目標關節位置,單位 deg 
    * @param [in] desc_pos 目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] epos 擴展軸位置，單位 mm 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移 
    * @param [in] offset_pos 位姿偏移量 
    * @param [in] spiral_param 螺旋參數 
    * @return 錯誤碼 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, ExaxisPos epos, float ovl, byte offset_flag, DescPose offset_pos, SpiralParam spiral_param); 

螺旋線運動代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescSpiral_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos j = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose offset_pos1 = new DescPose(50, 0, 0, -30, 0, 0);
        DescPose offset_pos2 = new DescPose(50, 0, 0, -5, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp;
        sp.circle_num = 5;
        sp.circle_angle = 5.0f;
        sp.rad_init = 50.0f;
        sp.rad_add = 10.0f;
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

        rtn = robot.MoveJ(j, desc_pos, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
        Console.WriteLine($"MoveJ errcode:{rtn}");

        rtn = robot.NewSpiral(j, desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp);
        Console.WriteLine($"NewSpiral errcode:{rtn}");
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
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，默認爲0
    * @param  [in] id servoJ指令ID,默認爲0
    * @return  錯誤碼
    */
    int ServoJ(JointPos joint_pos, float acc, float vel, float cmdT, float filterT, float gain,int id=0);

關節空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

關節扭矩控制開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制開始
    * @return  錯誤碼
    */
    int ServoJTStart();

關節扭矩控制
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制
    * @param  [in] torque j1~j6關節扭矩，單位Nm
    * @param  [in] interval 指令週期，單位s，範圍[0.001~0.008]
    * @return  錯誤碼
    */
    int ServoJT(double[] torque, double interval);

關節扭矩控制結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制結束
    * @return  錯誤碼
    */
    int ServoJTEnd();

關節扭矩控制代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button27_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }

笛卡爾空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基座標系)，1-增量運動(基座標系)，2-增量運動(工具座標系)
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，默認爲0
    * @return  錯誤碼
    */
    int ServoCart(int mode, DescPose desc_pos, double[] pos_gain, float acc, float vel, float cmdT, float filterT, float gain);

笛卡爾空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnDescServoMove_Click(object sender, EventArgs e)
    {
        DescPose desc_pos_dt = new DescPose(0, 0, 0, 0, 0, 0);

        desc_pos_dt.tran.z = -0.5;
        double[] pos_gain = new double[6]{ 0.0, 0.0, 1.0, 0.0, 0.0, 0.0 };
        int mode = 2;
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        int count = 500;

        robot.SetSpeed(20);

        while (count > 0)
        {
        robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
        count -= 1;
        robot.WaitMs((int)(cmdT * 1000));
        }
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
    * @param  [in] desc_pos   目標笛卡爾位姿
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

樣條運動代碼示例
++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSplineMove_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

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
    * @param [in] type  0-圓弧過渡，1-給定點位爲路徑點
    * @param [in] averageTime  全局平均銜接時間(ms)(10 ~  )，默認2000
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
    * @param [in] desc_pos 目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag  是否爲最後一個點，0-否，1-是
    * @return 錯誤碼 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @return 錯誤碼 
    */ 
    int NewSplineEnd();
    
新樣條運動代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnNewSpline_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

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

        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(j1, desc_pos1, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j2, desc_pos2, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j3, desc_pos3, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j4, desc_pos4, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j5, desc_pos5, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplineEnd();
    }

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

運動暫停、恢復、停止代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMotionPause_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PauseMotion();

        Thread.Sleep(1000);
        robot.ResumeMotion();

        Thread.Sleep(1000);
        robot.StopMotion();

        Thread.Sleep(1000);

    }

點位整體偏移開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
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

點位偏移代碼示例
++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnPointOffect_Click(object sender, EventArgs e)
    {
        JointPos j1, j2;
        DescPose desc_pos1, desc_pos2, offset_pos, offset_pos1;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos1 = new DescPose(50.0, 50.0, 50.0, 5.0, 5.0, 5.0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;
        int type = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetEnable(type, offset_pos1);
        Thread.Sleep(1000);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
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
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
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
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
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

AO飛拍代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMoveAO_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;

        robot.SetSpeed(5);

        robot.MoveAOStart(0,100,100,20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();
    }

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
.. code-block:: c#
    :linenos:

    /**
    * @brief 關閉Ptp運動FIR濾波
    * @return 錯誤碼
    */
    int PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
++++++++++++++++++++++++++++++
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
.. code-block:: c#
    :linenos:

    /**
    * @brief 關閉LIN、ARC運動FIR濾波
    * @return 錯誤碼
    */
    int LinArcFIRPlanningEnd();

FIR濾波代碼示例
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

加速度平滑開啓
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 加速度平滑開啓
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

        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AccSmoothStart(false);
        Console.WriteLine("AccSmoothStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AccSmoothEnd(false);
        Console.WriteLine("AccSmoothEnd rtn is " + rtn);
    }

指定姿態速度開啓
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 指定姿態速度開啓
    * @param [in] ratio 姿態速度百分比[0-300]
    * @return  錯誤碼
    */
    int AngularSpeedStart(int ratio);

指定姿態速度關閉
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
   
    /**
    * @brief 指定姿態速度關閉
    * @return  錯誤碼
    */
    int AngularSpeedEnd();

機器人指定姿態速度代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button71_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AngularSpeedStart(50);
        Console.WriteLine("AngularSpeedStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AngularSpeedEnd();
        Console.WriteLine("AngularSpeedEnd rtn is " + rtn);
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

代碼示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void btnTestSingularAvoidEArc_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.SingularAvoidStart(2, 10, 5, 5);
        Console.WriteLine("SingularAvoidStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.SingularAvoidEnd();
        Console.WriteLine("SingularAvoidEnd rtn is " + rtn);
    }

安全停止觸發
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 安全停止觸發信號
    * @return 錯誤碼
    */
    int GetSafetyCode();



