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