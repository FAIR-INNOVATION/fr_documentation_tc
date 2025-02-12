機器人常用設定
=================

.. toctree:: 
    :maxdepth: 5

設定全域速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定全域速度
    * @param  [in]  vel  速度百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int SetSpeed(int vel); 

設定係統變數值
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定工具參考點-六點法
    * @param [in] point_num 點編號,範圍[1~6]
    * @return 錯誤碼 
    */ 
    int SetToolPoint(int point_num); 

計算工具座標系--六點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算工具座標系
    * @param [out] tcp_pose 工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeTool(DescPose tcp_pose); 

設定工具參考點-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定工具參考點-四點法
    * @param [in] point_num 點編號,範圍[1~4]
    * @return 錯誤碼 
    */ 
    int SetTcp4RefPoint(int point_num);

計算工具座標系-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算工具座標系
    * @param [out] tcp_pose 工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeTcp4(DescPose tcp_pose);

設定工具坐標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定工具坐標系 
    * @param [in] id 座標系編號，範圍[0~14]
    * @param [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param [in] type  0-工具坐標系，1-感測器座標系
    * @param [in] install 安裝位置，0-機器人末端，1-機器人外部
    * @param [in] toolID  工具ID
    * @param [in] loadNum  負載編號
    * @return 錯誤碼 
    */ 
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);  

設定工具坐標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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

代碼範例
++++++++++++++++++++++++++++++++++
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
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//獲取系統變數
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos jp1=new JointPos(-89.407,-148.279,-83.169,-45.689,133.689,41.705);
        JointPos jp2=new JointPos(-67.595,-143.7,-88.006,-48.514,57.073,56.189);
        JointPos jp3=new JointPos(-88.229,-152.355,-67.815,-78.07,129.029,58.739);
        JointPos jp4=new JointPos(-77.528,-141.519,-89.826,-37.184,90.274,41.769);
        JointPos jp5=new JointPos(-76.744,-138.219,-97.714,-32.595,90.255,42.558);
        JointPos jp6=new JointPos(-77.595,-138.454,-90.065,-40.014,90.275,41.709);
        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p4 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p5 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p6 = new DescPose(0, 0, 0, 0, 0, 0);
        robot.GetForwardKin(jp1, desc_p1);
        robot.GetForwardKin(jp2, desc_p2);
        robot.GetForwardKin(jp3, desc_p3);
        robot.GetForwardKin(jp4, desc_p4);
        robot.GetForwardKin(jp5, desc_p5);
        robot.GetForwardKin(jp6, desc_p6);
        robot.MoveJ(jp1, desc_p1,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(1);

        robot.MoveJ(jp2, desc_p2,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(2);

        robot.MoveJ(jp3, desc_p3,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(3);

        robot.MoveJ(jp4, desc_p4,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(4);

        robot.MoveJ(jp5, desc_p5,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(5);

        robot.MoveJ(jp6, desc_p6,0, 0, 30, 100, 100, epos, -1, 0, offset_pos);
        robot.SetToolPoint(6);

        DescPose coord = new DescPose();
        robot.ComputeTool(coord);
        System.out.println("result is " + coord.tran.x + "  " + coord.tran.y + "  " + coord.tran.z + "  " + coord.rpy.rx + "  " + coord.rpy.ry + "  " + coord.rpy.rz);

        robot.SetToolCoord(5, coord, 0, 0,0,0);//設定工具坐標系
        robot.SetToolList(5, coord, 0, 0, 0);
    }

根據點位資訊計算工具座標系
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 根據點位資訊計算工具座標系
 * @param [in] method 計算方法；0-四點法；1-六點法
 * @param [in] pos 關節位置組，四點法時數組長度為4個，六點法時數組長度為6個
 * @param [in] tool_pose 輸出的工具座標系
 * @return 錯誤碼
 */
 int ComputeToolCoordWithPoints(int method, JointPos[] pos,DescPose tool_pose);

根據點位資訊計算工件座標系
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 根據點位資訊計算工件座標系
 * @param [in] method 計算方法；0：原點-x軸-z軸 1：原點-x軸-xy平面
 * @param [in] pos 三個TCP位置組
 * @param [in] refFrame 參考座標系
 * @param [in] tcp_pose 輸出工件座標系
 * @return 錯誤碼
 */
 int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame,DescPose tcp_pose);

程式碼範例
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

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
 System.out.println("rpc連線 success");
 }
 else
 {
 System.out.println("rpc連線 fail");
 return ;
 }

 DescPose p1Desc=new DescPose(-394.073, -276.405, 399.451, -133.692, 7.657, -139.047);
 JointPos p1Joint=new JointPos(15.234, -88.178, 96.583, -68.314, -52.303, -122.926);

 DescPose p2Desc=new DescPose(-187.141, -444.908, 432.425, 148.662, 15.483, -90.637);
 JointPos p2Joint=new JointPos(61.796, -91.959, 101.693, -102.417, -124.511, -122.767);

 DescPose p3Desc=new DescPose(-368.695, -485.023, 426.640, -162.588, 31.433, -97.036);
 JointPos p3Joint=new JointPos(43.896, -64.590, 60.087, -50.269, -94.663, -122.652);

 DescPose p4Desc=new DescPose(-291.069, -376.976, 467.560, -179.272, -2.326, -107.757);
 JointPos p4Joint=new JointPos(39.559, -94.731, 96.307, -93.141, -88.131, -122.673);

 DescPose p5Desc=new DescPose(-284.140, -488.041, 478.579, 179.785, -1.396, -98.030);
 JointPos p5Joint=new JointPos(49.283, -82.423, 81.993, -90.861, -89.427, -122.678);

 DescPose p6Desc=new DescPose(-296.307, -385.991, 484.492, -178.637, -0.057, -107.059);
 JointPos p6Joint=new JointPos(40.141, -92.742, 91.410, -87.978, -88.824, -122.808);

 ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
 DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

 JointPos[] posJ = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
 DescPose coordRtn = new DescPose();
 int rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);
 System.out.println("ComputeToolCoordWithPoints: "+rtn+ ", coord is :"+ coordRtn.tran.x+","+coordRtn.tran.y+","+coordR.tran.z+","+ coordR.R.KtnordR.Atn.


 robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(1);
 robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(2);
 robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(3);
 robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(4);
 robot.MoveJ(p5Joint, p5Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(5);
 robot.MoveJ(p6Joint, p6Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
 robot.SetToolPoint(6);
 robot.ComputeTool(coordRtn);
 System.out.println("ComputeTool :"+rtn+",coord is :"+coordRtn.tran.x+","+ coordRtn.tran.y+","+ coordRtn.tran.z+","+ coordRtn.rpy.rx+","
 }

設定外部工具座標參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定外部工具參考點-三點法
    * @param [in] point_num 點編號,範圍[1~3]
    * @return 錯誤碼 
    */ 
    int SetExTCPPoint(int point_num); 

計算外部工具坐標系-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
    * @brief 計算外部工具坐標系-三點法
    * @param [out] tcp_pose 外部工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeExTCF(DescPose tcp_pose); 

設定外部工具坐標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定外部工具坐標系 
    * @param [in] id 座標系編號，範圍[0~14]
    * @param [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param [in] etool  待定
    * @return 錯誤碼 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

設定外部工具坐標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定外部工具坐標系列表
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

代碼範例
++++++++++++++++++++++++++++++++++
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
        robot.Mode(1);
        robot.SetSpeed(20);
        robot.Mode(0);

        for(int i = 1; i < 10; i++)
        {
            robot.SetSysVarValue(i, i * 10);
        }
        for(int i = 1; i < 10; i++)
        {
            List<Number> rtnArr = robot.GetSysVarValue(i);//獲取系統變數
            System.out.println("SysVarValue " +  i  + " is " + rtnArr.get(1));
        }

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689 , -37.899, 94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);


        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetExTCPPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeExTCF(coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetExToolCoord(5, coordE, coordE);
        robot.SetExToolList(5,coordE, coordE);
    }

設定工件座標系參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定工件參考點-三點法 
    * @param [in] point_num 點編號,範圍[1~3]
    * @return 錯誤碼 
    */ 
    int SetWObjCoordPoint(int point_num); 

計算工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算工件座標系
    * @param [in]  method 計算方式 0：原點-x軸-z軸 1：原點-x軸-xy平面
    * @param [in]  refFrame 參考座標系
    * @param [out]  wobj_pose 工件座標系
    * @return 錯誤碼 
    */ 
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose); 

設定工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定工件座標系列表
    * @param  [in] id 座標系編號，範圍[1~15]
    * @param  [in] coord  工件坐標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

代碼範例
++++++++++++++++++++++++++++++++++
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

        JointPos j1 = new JointPos(-84.787, -152.056,-75.689,-37.899,94.486,41.709);
        JointPos j2 = new JointPos(-79.438,-152.139,-75.634,-37.469,94.065,47.058);
        JointPos j3 = new JointPos(-84.788,-145.179,-77.119,-43.345,94.487,41.709);
        DescPose desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);
        DescPose desc_p3 = new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(j1, desc_p1);
        robot.GetForwardKin(j2, desc_p2);
        robot.GetForwardKin(j3, desc_p3);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(1);

        robot.MoveJ(j2, desc_p2,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(2);

        robot.MoveJ(j3, desc_p3,0, 0, 20, 100, 100, epos, -1, 0, offset_pos);
        robot.SetWObjCoordPoint(3);

        DescPose coordE = new DescPose();
        robot.ComputeWObjCoord(0, coordE);
        System.out.println("result is " + coordE.tran.x + "  " + coordE.tran.y + "  " + coordE.tran.z + "  " + coordE.rpy.rx + "  " + coordE.rpy.ry + "  " + coordE.rpy.rz);

        robot.SetWObjCoord(5, coordE,0);
        robot.SetWObjList(5,coordE,0);
    }

設定末端負載重量
++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 設定末端負載重量
 * @param [in] loadNum 負載編號
 * @param [in] weight 負載重量，單位kg
 * @return 錯誤碼
 */
 int SetLoadWeight(int loadNum,double weight);

設定末端負載質心座標
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定末端負載質心座標
    * @param  [in] coord 質心座標，單位mm
    * @return  錯誤碼
    */
    int SetLoadCoord(DescTran coord); 

設定機器人安裝方式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定機器人安裝方式
    * @param  [in]  install  安裝方式，0-正裝，1-側裝，2-倒裝
    * @return  錯誤碼
    */
    int SetRobotInstallPos(int install); 

設定機器人安裝角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設定機器人安裝角度，自由安裝
    * @param  [in] yangle  傾斜角
    * @param  [in] zangle  旋轉角
    * @return  錯誤碼
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

代碼範例
++++++++++++++++++++++++++++++++++
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
        robot.SetLoadWeight(2);
        robot.SetLoadCoord(new DescTran(1.0, 2.0, 3.0));
        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(0, 0);
    }

等待指定時間
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  等待指定時間
    * @param  [in]  t_ms  單位ms
    * @return  錯誤碼
    */
    int WaitMs(int t_ms);

設定機器人加速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定機器人加速度
    * @param [in] acc 機器人加速度百分比
    * @return 錯誤碼
    */
    int SetOaccScale(double acc);