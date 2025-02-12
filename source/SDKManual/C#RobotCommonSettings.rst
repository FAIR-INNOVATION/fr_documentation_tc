機器人常用設定
=================

.. toctree:: 
    :maxdepth: 5

設定全域速度
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定全域速度
    * @param  [in]  vel  速度百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int SetSpeed(int vel); 

設定係統變數值
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定係統變數值
    * @param  [in]  id  變數編號，範圍[1~20]
    * @param  [in]  value 變數值
    * @return  錯誤碼
    */
    int SetSysVarValue(int id, double value); 

設定工具參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定工具參考點-六點法 
    * @param [in] point_num 點編號,範圍[1~6] 
    * @return 錯誤碼 
    */ 
    int SetToolPoint(int point_num); 

計算工具座標系--六點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算工具座標系
    * @param [out] tcp_pose 工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeTool(ref DescPose tcp_pose); 

設定工具參考點-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定工具參考點-四點法 
    * @param [in] point_num 點編號,範圍[1~4] 
    * @return 錯誤碼 
    */ 

計算工具座標系-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 計算工具座標系
    * @param [out] tcp_pose 工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeTcp4(ref DescPose tcp_pose);

設定工具坐標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工具坐標系
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param  [in] type  0-工具坐標系，1-感測器座標系
    * @param  [in] install 安裝位置，0-機器人末端，1-機器人外部
    * param   [in] toolID 工具ID
    * @param  [in] loadNum 負載編號
    * @return  錯誤碼
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);  

設定工具坐標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工具坐標系列表
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param  [in] type  0-工具坐標系，1-感測器座標系
    * @param  [in] install 安裝位置，0-機器人末端，1-機器人外部
    * @param  [in] loadNum 負載編號
    * @return  錯誤碼
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

設定外部工具座標參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定外部工具參考點-三點法
    * @param [in] point_num 點編號,範圍[1~3] 
    * @return 錯誤碼 
    */ 
    int SetExTCPPoint(int point_num); 

計算外部工具坐標系-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 計算外部工具坐標系-三點法
    * @param [out] tcp_pose 外部工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

設定外部工具坐標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定外部工具坐標系 
    * @param [in] id 座標系編號，範圍[0~14] 
    * @param [in] etcp 工具中心點相對末端法蘭中心位姿 
    * @param [in] etool 待定 
    * @return 錯誤碼 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

設定外部工具坐標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定外部工具坐標系列表
    * @param  [in] id 座標系編號，範圍[0~14] 
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

設定工件座標系參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設定工件參考點-三點法 
    * @param [in] point_num 點編號,範圍[1~3]  
    * @return 錯誤碼 
    */ 
    int SetWObjCoordPoint(int point_num); 

計算工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  計算工件座標系
    * @param [in] method 計算方法 0：原點-x軸-z軸  1：原點-x軸-xy平面
    * @param [in] refFrame 參考座標系
    * @param [out] wobj_pose 工件座標系
    * @return 錯誤碼
    */
    int ComputeWObjCoord(int method, int refFrame, ref DescPose wobj_pose); 

設定工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工件座標系
    * @param  [in] id 座標系編號，範圍[1~15]
    * @param  [in] coord  工件坐標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */
    int SetWObjCoord(int id, DescPose coord, int refFrame);

設定工件座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定工件座標系列表
    * @param  [in] id 座標系編號，範圍[0~14] 
    * @param  [in] coord  工件坐標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

設定末端負載重量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定末端負載重量
    * @param  [in] weight  負載重量，單位kg
    * @return  錯誤碼
    */
    int SetLoadWeight(float weight);

設定末端負載質心座標
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定末端負載質心座標
    * @param  [in] coord 質心座標，單位mm
    * @return  錯誤碼
    */
    int SetLoadCoord(DescTran coord); 

設定機器人安裝方式
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定機器人安裝方式
    * @param  [in] install  安裝方式，0-正裝，1-側裝，2-倒裝
    * @return  錯誤碼
    */
    int SetRobotInstallPos(byte install); 

設定機器人安裝角度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設定機器人安裝角度，自由安裝
    * @param  [in] yangle  傾斜角
    * @param  [in] zangle  旋轉角
    * @return  錯誤碼
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代碼範例
++++++++++
.. code-block:: c#
    :linenos:

    private void btnCommonSets_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");

        int i;
        double value = 0;
        int id;
        int type;
        int install;

        DescTran coord = new DescTran();
        DescPose t_coord, etcp, etool, w_coord;
        t_coord = new DescPose();
        etcp = new DescPose();
        w_coord = new DescPose();

        robot.SetSpeed(20);

        for (i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, (float)(i + 0.5));
            robot.WaitMs(100);
        }

        for (i = 1; i < 21; i++)
        {
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value : {value}");
        }

        robot.SetLoadWeight((float)2.5);
        coord.x = 3.0;
        coord.y = 4.0;
        coord.z = 5.0;
        robot.SetLoadCoord(coord);
                
        id = 3;
        t_coord.tran.x = 1.0;
        t_coord.tran.y = 2.0;
        t_coord.tran.z = 300.0;
        t_coord.rpy.rx = 4.0;
        t_coord.rpy.ry = 5.0;
        t_coord.rpy.rz = 6.0;
        type = 0;
        install = 0;

        int rtn1 = -1;
        int rtn2 = -1;
        rtn1 = robot.SetToolCoord(id, t_coord, type, install);
        rtn2 = robot.SetToolList(id, t_coord, type, install);
        Console.WriteLine($"set tool coord result {rtn1}, set tool list rtn{rtn2}");
            
        etcp.tran.x = 1.0;
        etcp.tran.y = 2.0;
        etcp.tran.z = 3.0;
        etcp.rpy.rx = 4.0;
        etcp.rpy.ry = 5.0;
        etcp.rpy.rz = 6.0;
        etool.tran.x = 11.0;
        etool.tran.y = 22.0;
        etool.tran.z = 330.0;
        etool.rpy.rx = 44.0;
        etool.rpy.ry = 55.0;
        etool.rpy.rz = 66.0;
        id = 5;
        robot.SetExToolCoord(id, etcp, etool);
        robot.SetExToolList(id, etcp, etool);

        w_coord.tran.x = 110.0;
        w_coord.tran.y = 12.0;
        w_coord.tran.z = 13.0;
        w_coord.rpy.rx = 14.0;
        w_coord.rpy.ry = 15.0;
        w_coord.rpy.rz = 16.0;
        id = 12;
        robot.SetWObjCoord(id, w_coord);
        //robot.SetWObjList(id, w_coord);

        double yangle = 0, zangle = 0;
        robot.SetRobotInstallPos(1);//側裝
        robot.SetRobotInstallAngle(15.0, 25.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
        robot.SetRobotInstallAngle(10.0, 10.0);
        Thread.Sleep(1000);
        robot.GetRobotInstallAngle(ref yangle, ref zangle);
        Console.WriteLine($"yangle  {yangle}   zangle  {zangle}");
    }

等待指定時間
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待指定時間
    * @param  [in]  t_ms  單位ms
    * @return  錯誤碼
    */
    int WaitMs(int t_ms);

設定機器人加速度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設定機器人加速度
    * @param [in] acc 機器人加速度百分比
    * @return 錯誤碼
    */
    int SetOaccScale(double acc)

根據點位資訊計算工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據點位資訊計算工具座標系
    * @param [in] method 計算方法；0-四點法；1-六點法
    * @param [in] pos 關節位置組，四點法時數組長度為4個，六點法時數組長度為6個
    * @return 錯誤碼
    */

    int ComputeToolCoordWithPoints(int method, JointPos[] pos, ref DescPose coordRtn)

根據點位資訊計算工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    /**
    * @brief 根據點位資訊計算工件座標系
    * @param [in] method 計算方法；0：原點-x軸-z軸 1：原點-x軸-xy平面
    * @param [in] pos 三個TCP位置組
    * @param [in] refFrame 參考座標系
    * @return 錯誤碼
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, ref DescPose coordRtn)

代碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    private void TestTCP_Click(object sender, EventArgs e)
    {
      DescPose p1Desc = new DescPose(-394.073, -276.405, 399.451, -133.692, 7.657, -139.047);
      JointPos p1Joint = new JointPos(15.234, -88.178, 96.583, -68.314, -52.303, -122.926);

      DescPose p2Desc = new DescPose( -187.141, -444.908, 432.425, 148.662, 15.483, -90.637);
      JointPos p2Joint = new JointPos(61.796, -91.959, 101.693, -102.417, -124.511, -122.767);

      DescPose p3Desc = new DescPose(-368.695, -485.023, 426.640, -162.588, 31.433, -97.036);
      JointPos p3Joint = new JointPos(43.896, -64.590, 60.087, -50.269, -94.663, -122.652);

      DescPose p4Desc = new DescPose(-291.069, -376.976, 467.560, -179.272, -2.326, -107.757);
      JointPos p4Joint = new JointPos(39.559, -94.731, 96.307, -93.141, -88.131, -122.673);

      DescPose p5Desc = new DescPose(-284.140, -488.041, 478.579, 179.785, -1.396, -98.030);
      JointPos p5Joint = new JointPos(49.283, -82.423, 81.993, -90.861, -89.427, -122.678);

      DescPose p6Desc = new DescPose(-296.307, -385.991, 484.492, -178.637, -0.057, -107.059);
      JointPos p6Joint = new JointPos(40.141, -92.742, 91.410, -87.978, -88.824, -122.808);

      ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
      DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

      JointPos[] posJ = new JointPos[6]{ p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint };
      DescPose coordRtn = new DescPose(0, 0, 0, 0, 0, 0); 
      int rtn = robot.ComputeToolCoordWithPoints(0, posJ,ref coordRtn);
      Console.WriteLine("ComputeToolCoordWithPoints {0}  coord is {1} {2} {3} {4} {5} {6}", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);


      robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(1);
      robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(2);
      robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(3);
      robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      robot.SetTcp4RefPoint(4);
      robot.ComputeTcp4(ref coordRtn);
      Console.WriteLine("ComputeTcp4 {0}  coord is {1} {2} {3} {4} {5} {6}", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
      //robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
      //robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
    }




