機器人常用設置
=================

.. toctree:: 
    :maxdepth: 5

設置工具參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置工具參考點-六點法
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

設置工具參考點-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置工具參考點-四點法
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

根據點位信息計算工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 根據點位信息計算工具座標系
    * @param [in] method 計算方法；0-四點法；1-六點法
    * @param [in] pos 關節位置組，四點法時數組長度爲4個，六點法時數組長度爲6個
    * @param [out] tool_pose 輸出的工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeToolCoordWithPoints(int method, JointPos[] pos,DescPose tool_pose);

設置工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置工具座標系 
    * @param [in] id 座標系編號，範圍[0~14]
    * @param [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param [in] type  0-工具座標系，1-傳感器座標系
    * @param [in] install 安裝位置，0-機器人末端，1-機器人外部
    * @param [in] toolID  工具ID
    * @param [in] loadNum  負載編號
    * @return 錯誤碼 
    */ 
    int SetToolCoord(int id, DescPose coord, int type, int install, int toolID, int loadNum);  

設置工具座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置工具座標系列表
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param  [in] type  0-工具座標系，1-傳感器座標系
    * @param  [in] install 安裝位置，0-機器人末端，1-機器人外部
    * @param  [in] loadNum 負載編號
    * @return  錯誤碼
    */
    int SetToolList(int id, DescPose coord, int type, int install, int loadNum);  

獲取當前工具座標系
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工具座標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具座標系位姿
    * @return  錯誤碼
    */
    int GetTCPOffset(int flag, DescPose desc_pos); 

機器人工具座標系操作代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestTCPCompute(Robot robot)
    {
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint=new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);

        DescPose p2Desc=new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint=new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);

        DescPose p3Desc=new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint=new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);

        DescPose p4Desc=new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint=new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);

        DescPose p5Desc=new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint=new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);

        DescPose p6Desc=new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint=new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
        DescPose coordRtn =new DescPose() {};
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, coordRtn);

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
        rtn = robot.ComputeTool(coordRtn);
        robot.SetToolList(3, coordRtn, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(coordRtn);

        robot.SetToolCoord(4, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose(){};
        rtn = robot.GetTCPOffset(0, getCoord);
        return 0;
    }

設置外部工具座標參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置外部工具參考點-三點法 
    * @param [in] point_num 點編號,範圍[1~3]
    * @return 錯誤碼 
    */ 
    int SetExTCPPoint(int point_num); 

計算外部工具座標系-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
    * @brief 計算外部工具座標系-三點法
    * @param [out] tcp_pose 外部工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeExTCF(DescPose tcp_pose); 

設置外部工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置外部工具座標系 
    * @param [in] id 座標系編號，範圍[0~14]
    * @param [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param [in] etool  待定
    * @return 錯誤碼 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

設置外部工具座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置外部工具座標系列表
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

機器人外部工具座標系操作代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExtCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = { p1Desc , p2Desc , p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(coordRtn);

        robot.SetExToolCoord(1, coordRtn, offdese);
        robot.SetExToolList(1, coordRtn, offdese);
        return 0;
    }

設置工件座標系參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置工件參考點-三點法 
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
    * @param [in]  method 計算方式 0：原點-x軸-z軸  1：原點-x軸-xy平面
    * @param [in]  refFrame 參考座標系
    * @param [out]  wobj_pose 工件座標系
    * @return 錯誤碼 
    */ 
    int ComputeWObjCoord(int method, int refFrame, DescPose wobj_pose); 

設置工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置工件座標系
    * @param  [in] id 座標系編號，範圍[1~15]
    * @param  [in] coord  工件座標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */    
    int SetWObjCoord(int id, DescPose coord, int refFrame);

設置工件座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置工件座標系列表
    * @param  [in] id 座標系編號，範圍[1~15]
    * @param  [in] coord  工件座標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

根據點位信息計算工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 根據點位信息計算工件座標系
    * @param [in] method 計算方法；0：原點-x軸-z軸  1：原點-x軸-xy平面
    * @param [in] pos 三個TCP位置組
    * @param [in] refFrame 參考座標系
    * @param [in] tcp_pose 輸出工件座標系
    * @return 錯誤碼 
    */ 
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame,DescPose tcp_pose);

獲取當前工件座標系
++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前工件座標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件座標系位姿
    * @return  錯誤碼
    */   
    int GetWObjOffset(int flag, DescPose desc_pos);

機器人工件座標系操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWobjCoord(Robot robot)
    {
        DescPose p1Desc=new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint=new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc=new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint=new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc=new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint=new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);
        robot.GetForwardKin(p3Joint,p3Desc);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP =new DescPose[]{p1Desc , p2Desc , p3Desc };
        DescPose coordRtn =new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);

        robot.MoveJ(p1Joint, p1Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 1, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, coordRtn);

        robot.SetWObjCoord(1, coordRtn, 0);
        robot.SetWObjList(1, coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, getWobjDesc);
        return 0;
    }
    
設置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置全局速度
    * @param  [in]  vel  速度百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int SetSpeed(int vel); 

設置機器人加速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置機器人加速度
    * @param [in] acc 機器人加速度百分比
    * @return 錯誤碼
    */
    int SetOaccScale(double acc);

獲取機器人默認速度
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人默認速度
    * @return  List[0]:int 錯誤碼; List[1]: double vel 速度，單位mm/s
    */   
    List<Number> GetDefaultTransVel(); 

設置末端負載重量
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置末端負載重量
    * @param  [in] loadNum 負載編號
    * @param  [in] weight  負載重量，單位kg
    * @return  錯誤碼
    */
    int SetLoadWeight(int loadNum,double weight);

設置末端負載質心座標
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置末端負載質心座標
    * @param  [in] coord 質心座標，單位mm
    * @return  錯誤碼
    */
    int SetLoadCoord(DescTran coord); 

設置末端負載質心座標
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief  設置末端負載質心座標
     * @param  [in] loadNum 負載編號
     * @param  [in] coord 質心座標，單位mm
     * @return  錯誤碼
     */
    public int SetLoadCoord(int loadNum, DescTran coord)

獲取當前負載的重量
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前負載的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @return  List[0]:int 錯誤碼; List[1]: double weight  負載重量，單位kg
    */
    List<Number> GetTargetPayload(int flag); 

獲取當前負載的質心
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取當前負載的質心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 負載質心，單位mm
    * @return  錯誤碼
    */   
    int GetTargetPayloadCog(int flag, DescTran cog);

設置機器人安裝方式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置機器人安裝方式
    * @param  [in]  install  安裝方式，0-正裝，1-側裝，2-倒裝
    * @return  錯誤碼
    */
    int SetRobotInstallPos(int install); 

設置機器人安裝角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置機器人安裝角度，自由安裝
    * @param  [in] yangle  傾斜角
    * @param  [in] zangle  旋轉角
    * @return  錯誤碼
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

獲取機器人安裝角度
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取機器人安裝角度
    * @return  List[0]:錯誤碼; List[1]:double yangle 傾斜角; List[2]:double zangle 旋轉角
    */
    public List<Number> GetRobotInstallAngle()

設置系統變量值
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置系統變量值
    * @param  [in]  id  變量編號，範圍[1~20]
    * @param  [in]  value 變量值
    * @return  錯誤碼
    */
    int SetSysVarValue(int id, double value); 

獲取系統變量值
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取系統變量值
    * @param  [in] id 系統變量編號，範圍[1~20]
    * @return  List[0]:錯誤碼; List[1]:double value 系統變量值
    */
    List<Number> GetSysVarValue(int id); 

機器人常用設置代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestLoadInstall(Robot robot)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            robot.Sleep(30);
        }

        List<Number> defaultVel=new ArrayList<>();

        defaultVel=robot.GetDefaultTransVel();
        System.out.println("GetDefaultTransVel is:"+ defaultVel.get(1));

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5);
            robot.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            float value = 0;
            defaultVel=robot.GetSysVarValue(i);
            System.out.println("sys value :"+i+", is :"+defaultVel.get(1));
            robot.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0;
        loadCoord.y = 4.0;
        loadCoord.z = 5.0;
        robot.SetLoadCoord(loadCoord);

        robot.Sleep(1000);

        List<Number> getLoad = new ArrayList<>();

        getLoad=robot.GetTargetPayload(0);

        DescTran getLoadTran =new DescTran();
        robot.GetTargetPayloadCog(0, getLoadTran);
        System.out.println("get load is:"+getLoad.get(1)+", get load cog is: "+getLoadTran.x+","+getLoadTran.y+","+getLoadTran.z);

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0, 25.0);

        List<Number> angle=new ArrayList<>();
        angle=robot.GetRobotInstallAngle();
        System.out.println("GetRobotInstallAngle x:"+angle.get(1)+";  y:"+angle.get(2));

        robot.CloseRPC();
        return 0;
    }

關節摩擦力補償開關
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 關節摩擦力補償開關 
    * @param [in] state  0-關，1-開
    * @return 錯誤碼 
    */ 
    int FrictionCompensationOnOff(int state); 

設置關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-正裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_level(Object[] coeff);

設置關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-側裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_wall(Object[] coeff); 

設置關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-倒裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_ceiling(Object[] coeff);

設置關節摩擦力補償係數-自由安裝
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-自由安裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_freedom(Object[] coeff);

機器人設置關節摩擦力補償代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFriction(Robot robot)
    {

        Object[] lcoeff = { 0.9,0.9,0.9,0.9,0.9,0.9 };
        Object[] wcoeff = { 0.4,0.4,0.4,0.4,0.4,0.4 };
        Object[] ccoeff = { 0.6,0.6,0.6,0.6,0.6,0.6 };
        Object[] fcoeff = { 0.5,0.5,0.5,0.5,0.5,0.5 };

        int rtn = robot.FrictionCompensationOnOff(1);
        System.out.println("FrictionCompensationOnOff rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_level(lcoeff);
        System.out.println("SetFrictionValue_level rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_wall(wcoeff);
        System.out.println("SetFrictionValue_wall rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        System.out.println("SetFrictionValue_ceiling rtn is:"+ rtn);

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        System.out.println("SetFrictionValue_freedom rtn is:"+ rtn);

        robot.CloseRPC();
        return 0;
    }

查詢機器人錯誤碼
++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief  查詢機器人錯誤碼
     * @param  [out]  maincode  主錯誤碼
     * @param  [out]  subcode   子錯誤碼
     * @return  錯誤碼
     */ 
    int GetRobotErrorCode(int[] maincode, int[] subcode);

錯誤狀態清除
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  錯誤狀態清除
    * @return  錯誤碼
    */
    int ResetAllError(); 

機器人故障狀態獲取及清除錯誤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGetError(Robot robot)
    {
        int[] maincode={0}, subcode={0};
        robot.GetRobotErrorCode(maincode, subcode);

        robot.ResetAllError();

        robot.Sleep(1000);

        robot.GetRobotErrorCode(maincode, subcode);
        return 0;
    }

設置寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置寬電壓控制箱溫度及風扇轉速監控參數
    * @param [in] enable 0-不使能監測；1-使能監測
    * @param [in] period 監測週期(s),範圍1-100
    * @return 錯誤碼
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

獲取寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取寬電壓控制箱溫度及風扇轉速監控參數
    * @return List[0]-錯誤碼,List[1]-enable 0-不使能監測；1-使能監測,List[2]-period 監測週期(s),範圍1-100
    */
    List<Number> GetWideBoxTempFanMonitorParam()

寬電壓控制箱溫度和風扇電流狀態獲取代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestWideVoltageCtrlBoxtemp(Robot robot)
    {
        robot.SetWideBoxTempFanMonitorParam(1, 2);
        List<Number> list=robot.GetWideBoxTempFanMonitorParam();
        System.out.println("GetWideBoxTempFanMonitorParam enable is:"+list.get(1)+", period is:"+list.get(2));
        ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+",fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);

        list=robot.GetWideBoxTempFanMonitorParam();
        for (int i = 0; i < 100; i++)
        {
            pkg=robot.GetRobotRealTimeState();
            System.out.println("robot ctrl box temp is:"+pkg.wideVoltageCtrlBoxTemp+" ,fan current is:"+pkg.wideVoltageCtrlBoxFanCurrent);
            robot.Sleep(100);
        }

        robot.CloseRPC();
        robot.Sleep(2000);
        return 0;
    }

設置焦點標定點
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焦點標定點
    * @param [in] pointNum 焦點標定點編號 1-8
    * @param [in] point    標定點座標
    * @return 錯誤碼
    */
    int SetFocusCalibPoint(int pointNum, DescPose point)

計算焦點標定結果
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 計算焦點標定結果
    * @param [in] pointNum  標定點個數
    * @param [in] resultPos 標定結果XYZ
    * @param [out] accuracy  標定精度誤差
    * @return 錯誤碼
    */
    int ComputeFocusCalib(int pointNum, DescTran resultPos, double[] accuracy)

開啓焦點跟隨
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 開啓焦點跟隨
    * @param [in] kp       比例參數，默認50.0
    * @param [in] kpredict 前饋參數，默認19.0
    * @param [in] aMax     最大角加速度限制，默認1440°/s^2
    * @param [in] vMax     最大角速度限制，默認180°/s
    * @param [in] type     鎖定X軸指向(0-參考輸入矢量；1-水平；2-垂直)
    * @return 錯誤碼
    */
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type)

停止焦點跟隨
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:

    /**
    * @brief 停止焦點跟隨
    * @return 錯誤碼
    */
    int FocusEnd()

設置焦點座標
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.7-3.8.4

.. code-block:: Java
    :linenos:
    
    /**
    * @brief 設置焦點座標
    * @param pos 焦點座標XYZ
    * @return 錯誤碼
    */
    public int SetFocusPosition(DescTran pos)

焦點跟隨代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestFocus(Robot robot){
        DescPose p1Desc=new DescPose(186.331, 487.913, 209.850, 149.030, 0.688, -114.347);
        JointPos p1Joint = new JointPos(-127.876, -75.341, 115.417, -122.741, -59.820, 74.300);

        DescPose p2Desc = new DescPose(69.721, 535.073, 202.882, -144.406, -14.775, -89.012);
        JointPos p2Joint = new JointPos(-101.780, -69.828, 110.917, -125.740, -127.841, 74.300);

        DescPose p3Desc = new DescPose(146.861, 578.426, 205.598, 175.997, -36.178, -93.437);
        JointPos p3Joint = new JointPos(-112.851, -60.191, 86.566, -80.676, -97.463, 74.300);

        DescPose p4Desc = new DescPose(136.284, 509.876, 225.613, 178.987, 1.372, -100.696);
        JointPos p4Joint = new JointPos(-116.397, -76.281, 113.845, -128.611, -88.654, 74.299);

        DescPose p5Desc = new DescPose(138.395, 505.972, 298.016, 179.134, 2.147, -101.110);
        JointPos p5Joint = new JointPos(-116.814, -82.333, 109.162, -118.662, -88.585, 74.302);

        DescPose p6Desc = new DescPose(105.553, 454.325, 232.017, -179.426, 0.444, -99.952);
        JointPos p6Joint = new JointPos(-115.649, -84.367, 122.447, -128.663, -90.432, 74.303);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 100, 0, 0, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint,  p2Desc);
        robot.GetForwardKin(p3Joint,  p3Desc);
        robot.GetForwardKin(p4Joint,  p4Desc);
        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);

        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4( coordRtn);

        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);

        robot.GetForwardKin(p1Joint, p1Desc);
        robot.GetForwardKin(p2Joint, p2Desc);
        robot.GetForwardKin(p3Joint, p3Desc);

        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);

        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double[] accuracy = {0.0};
        rtn = robot.ComputeFocusCalib(3,  resultPos,  accuracy);
        rtn = robot.SetFocusPosition(resultPos);

        robot.GetForwardKin(p5Joint,  p5Desc);
        robot.GetForwardKin(p6Joint,  p6Desc);

        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);

        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese,0,100);
        robot.FocusEnd();
    }


關節扭矩傳感器靈敏度標定功能開啓
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關節扭矩傳感器靈敏度標定功能開啓
    * @param status 0-關閉；1-開啓
    * @return 錯誤碼
    */
    public int JointSensitivityEnable(int status)

關節扭矩傳感器靈敏度數據採集
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關節扭矩傳感器靈敏度數據採集
    * @return 錯誤碼
    */
    public int JointSensitivityCollect()

取得關節扭矩感測器靈敏度標定結果
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得關節扭矩感測器靈敏度標定結果
    * @param calibResult j1~j6 關節靈敏度 [0-1]
    * @param linearity j1~j6 關節線性度 [0-1]
    * @return 錯誤碼
    */
    public int JointSensitivityCalibration(double[] calibResult, double[] linearity)

取得關節扭矩感測器遲滯誤差
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief 取得關節扭矩感測器遲滯誤差
    * @param hysteresisError j1~j6 關節遲滯誤差
    * @return 錯誤碼
    */
    public int JointHysteresisError(double[] hysteresisError);
    
取得關節扭矩感測器重複精度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:
    
    /**
    * @brief 取得關節扭矩感測器重複精度
    * @param repeatability j1~j6 關節扭矩感測器重複精度
    * @return 錯誤碼
    */
    public int JointRepeatability(double[] repeatability);
    
設定關節力感測器參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定關節力感測器參數
    * @param 必選參數 M J1-J6 質量係數 []
    * @param 必選參數 B J1-J6 阻尼係數 []
    * @param 必選參數 K J1-J6 剛度係數 []
    * @param 預設參數 threshold 力控制閾值，Nm
    * @param 預設參數 sensitivity 靈敏度, Nm/V, []
    * @param 預設參數 setZeroFlag 功能開啟標誌位；0-關閉；1-開啟；2-位置1記錄零點；3-位置2記錄零點
    * @return 錯誤碼
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

關節扭矩感測器靈敏度自動標定程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSensitivityCalib(Robot robot)
    {
        int rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        JointPos curJPos = new JointPos();
        robot.GetActualJointPosDegree(curJPos);
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos =new DescPose(0,0,0,0,0,0 );
        JointPos jointPos1 = new JointPos(curJPos.J1, 0, 0, -90, 0.02, curJPos.J6);
        DescPose descPos1 = new DescPose();
        robot.GetForwardKin(jointPos1, descPos1);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 1 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos2 =new JointPos( curJPos.J1, -30, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos2 =new DescPose();
        robot.GetForwardKin(jointPos2, descPos2);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 2 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos3 = new JointPos( curJPos.J1, -60, 0, -90, 0.02, curJPos.J6 );
        DescPose descPos3 =new DescPose();
        robot.GetForwardKin(jointPos3, descPos3);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 3 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos4 = new JointPos(curJPos.J1, -90, 0, -90, 0.02, curJPos.J6);
        DescPose descPos4 = new DescPose();
        robot.GetForwardKin(jointPos4, descPos4);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 4 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos5 = new JointPos(curJPos.J1, -120, 0, -90, 0.02, curJPos.J6);
        DescPose descPos5 = new DescPose();
        robot.GetForwardKin(jointPos5, descPos5);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 5 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos6 = new JointPos(curJPos.J1, -150, 0, -90, 0.02, curJPos.J6);
        DescPose descPos6 = new DescPose();
        robot.GetForwardKin(jointPos6, descPos6);
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 6 rtn is %d\n", rtn);
        robot.Sleep(100);
        JointPos jointPos7 = new JointPos(curJPos.J1, -180, 0, -90, 0.02, curJPos.J6);
        DescPose descPos7 = new DescPose();
        robot.GetForwardKin(jointPos7, descPos7);
        robot.MoveJ(jointPos7, descPos7, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 7 rtn is %d\n", rtn);
        robot.Sleep(100);
        // 反向行程
        robot.MoveJ(jointPos6, descPos6, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 8 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos5, descPos5, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 9 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos4, descPos4, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 10 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos3, descPos3, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 11 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos2, descPos2, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(100);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 12 rtn is %d\n", rtn);
        robot.Sleep(100);
        robot.MoveJ(jointPos1, descPos1, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.Sleep(200);
        rtn = robot.JointSensitivityCollect();
        System.out.printf("JointSensitivityCollect 13 rtn is %d\n", rtn);
        robot.Sleep(100);
        double[] calibResult =new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(calibResult, linearity);
        System.out.printf("JointSensitivityCalibration rtn is %d\n", rtn);
        rtn = robot.JointSensitivityEnable(0);
        System.out.printf("JointSensitivityEnable rtn is %d\n", rtn);
        System.out.printf("jointSensor Calib result is %f %f %f %f %f %f\njointSensor linearity is %f %f %f %f %f %f\n",
                calibResult[0], calibResult[1], calibResult[2],
                calibResult[3], calibResult[4], calibResult[5],
                linearity[0], linearity[1], linearity[2],
                linearity[3], linearity[4], linearity[5]);
        double[] hysteresisError = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointHysteresisError(hysteresisError);
        System.out.printf("JointHysteresisError result is %f %f %f %f %f %f\n",
                hysteresisError[0], hysteresisError[1], hysteresisError[2],
                hysteresisError[3], hysteresisError[4], hysteresisError[5]);
        double[] repeatability = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        rtn = robot.JointRepeatability(repeatability);
        System.out.printf("JointRepeatability result is %f %f %f %f %f %f\n",
                repeatability[0], repeatability[1], repeatability[2],
                repeatability[3], repeatability[4], repeatability[5]);
        double[] M = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] B = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        double[] K = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
        double[] threshold = {1.0, 1.0, 1.0, 1.0, 1.0, 1.0};
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        System.out.printf("SetAdmittanceParams rtn is %d\n", rtn);
    }

獲取機器人8個從站端口錯誤幀數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取機器人8個從站端口錯誤幀數
    * @param  inRecvErr 輸入接收錯誤幀數
    * @param  inCRCErr 輸入CRC錯誤幀數
    * @param  inTransmitErr 輸入轉發錯誤幀數
    * @param  inLinkErr 輸入鏈接錯誤幀數
    * @param  outRecvErr 輸出接收錯誤幀數
    * @param  outCRCErr 輸出CRC錯誤幀數
    * @param  outTransmitErr 輸出轉發錯誤幀數
    * @param  outLinkErr 輸出鏈接錯誤幀數
    * @return 錯誤碼
    */
    public int GetSlavePortErrCounter(int[] inRecvErr, int[] inCRCErr, int[] inTransmitErr, int[] inLinkErr, int[] outRecvErr, int[] outCRCErr, int[] outTransmitErr, int[] outLinkErr)

從站端口錯誤幀清零
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 從站端口錯誤幀清零
    * @param slaveID 從站編號0~7
    * @return 錯誤碼
    */
    public int SlavePortErrCounterClear(int slaveID)

獲取從站端口錯誤幀代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSlavePortErr(Robot robot)
    {
        ROBOT_STATE_PKG pkg =new ROBOT_STATE_PKG();
        int[] inRecvErr =new int[8];
        int[] inCRCErr =new int[8];
        int[] inTransmitErr =new int[8];
        int[] inLinkErr =new int[8];
        int[] outRecvErr =new int[8];
        int[] outCRCErr =new int[8];
        int[] outTransmitErr =new int[8];
        int[] outLinkErr =new int[8];
        robot.GetSlavePortErrCounter(inRecvErr,  inCRCErr, inTransmitErr, inLinkErr,
                outRecvErr, outCRCErr, outTransmitErr, outLinkErr);
        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inRecvErr[i]);
            }
            if (inCRCErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inCRCErr[i]);
            }
            if (inTransmitErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inTransmitErr[i]);
            }
            if (inLinkErr[i] != 0)
            {
                System.out.printf("inRecvErr %d is %d\n", i, inLinkErr[i]);
            }
            if (outRecvErr[i] != 0)
            {
                System.out.printf("outRecvErr %d is %d\n", i, outRecvErr[i]);
            }
            if (outCRCErr[i] != 0)
            {
                System.out.printf("outCRCErr %d is %d\n", i, outCRCErr[i]);
            }
            if (outTransmitErr[i] != 0)
            {
                System.out.printf("outTransmitErr %d is %d\n", i, outTransmitErr[i]);
            }
            if (outLinkErr[i] != 0)
            {
                System.out.printf("outLinkErr %d is %d\n", i, outLinkErr[i]);
            }
        }
        System.out.printf("others has no err!\n");
        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }
        robot.CloseRPC();
    }

設置各軸速度前饋係數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置各軸速度前饋係數
    * @param  radio 各軸速度前饋係數
    * @return 錯誤碼
    */
    public int SetVelFeedForwardRatio(double[] radio)

獲取各軸速度前饋係數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取各軸速度前饋係數
    * @param  radio 各軸速度前饋係數
    * @return 錯誤碼
    */
    public int GetVelFeedForwardRatio(double[] radio)

機器人速度前饋係數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestVelFeedForwardRatio(Robot robot)
    {
        double[] setRadio =new double[] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[]{ 0.0 };
        robot.GetVelFeedForwardRatio(getRadio);
        System.out.printf(" %f %f %f %f %f %f\n", getRadio[0], getRadio[1], getRadio[2], getRadio[3], getRadio[4], getRadio[5]);
        robot.CloseRPC();
    }