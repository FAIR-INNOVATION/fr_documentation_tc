機器人常用設置
=================

.. toctree:: 
    :maxdepth: 5

設置工具參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置工具參考點-六點法 
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

設置工具參考點-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置工具參考點-四點法 
    * @param [in] point_num 點編號,範圍[1~4] 
    * @return 錯誤碼 
    */ 
    int SetTcp4RefPoint(int point_num);

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

設置工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置工具座標系
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] coord  工具中心點相對於末端法蘭中心位姿
    * @param  [in] type  0-工具座標系，1-傳感器座標系
    * @param  [in] install 安裝位置，0-機器人末端，1-機器人外部
    * param   [in] toolID 工具ID
    * @param  [in] loadNum 負載編號
    * @return  錯誤碼
    */
    int SetToolCoord(int id, DescPose coord, int type, int install,int toolID, int loadNum);

根據點位信息計算工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 根據點位信息計算工具座標系
    * @param [in] method 計算方法；0-四點法；1-六點法
    * @param [in] pos 關節位置組，四點法時數組長度爲4個，六點法時數組長度爲6個
    * @return 錯誤碼
    */

    int ComputeToolCoordWithPoints(int method, JointPos[] pos, ref DescPose coordRtn)  

設置工具座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工具座標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具座標系位姿
    * @return  錯誤碼
    */
    int GetTCPOffset(byte flag, ref DescPose desc_pos); 

機器人工具座標系操作代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button18_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(186.331f, 487.913f, 209.850f, 149.030f, 0.688f, -114.347f);
        JointPos p1Joint = new JointPos(-127.876f, -75.341f, 115.417f, -122.741f, -59.820f, 74.300f);

        DescPose p2Desc = new DescPose(69.721f, 535.073f, 202.882f, -144.406f, -14.775f, -89.012f);
        JointPos p2Joint = new JointPos(-101.780f, -69.828f, 110.917f, -125.740f, -127.841f, 74.300f);

        DescPose p3Desc = new DescPose(146.861f, 578.426f, 205.598f, 175.997f, -36.178f, -93.437f);
        JointPos p3Joint = new JointPos(-112.851f, -60.191f, 86.566f, -80.676f, -97.463f, 74.300f);

        DescPose p4Desc = new DescPose(136.284f, 509.876f, 225.613f, 178.987f, 1.372f, -100.696f);
        JointPos p4Joint = new JointPos(-116.397f, -76.281f, 113.845f, -128.611f, -88.654f, 74.299f);

        DescPose p5Desc = new DescPose(138.395f, 505.972f, 298.016f, 179.134f, 2.147f, -101.110f);
        JointPos p5Joint = new JointPos(-116.814f, -82.333f, 109.162f, -118.662f, -88.585f, 74.302f);

        DescPose p6Desc = new DescPose(105.553f, 454.325f, 232.017f, -179.426f, 0.444f, -99.952f);
        JointPos p6Joint = new JointPos(-115.649f, -84.367f, 122.447f, -128.663f, -90.432f, 74.303f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos[] posJ = new JointPos[] { p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeToolCoordWithPoints(1, posJ, ref coordRtn);
        Console.WriteLine($"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(4);
        robot.MoveJ( p5Joint,  p5Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(5);
        robot.MoveJ( p6Joint,  p6Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetToolPoint(6);
        rtn = robot.ComputeTool(ref coordRtn);
        Console.WriteLine($"6 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
        robot.SetToolList(1,  coordRtn, 0, 0, 0);

        robot.MoveJ( p1Joint,  p1Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ( p4Joint,  p4Desc, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetTcp4RefPoint(4);
        rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool        {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0);

        DescPose getCoord = new DescPose();
        rtn = robot.GetTCPOffset(0, ref getCoord);
        Console.WriteLine($"GetTCPOffset    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");
    }

設置外部工具座標參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置外部工具參考點-三點法 
    * @param [in] point_num 點編號,範圍[1~3] 
    * @return 錯誤碼 
    */ 
    int SetExTCPPoint(int point_num); 

計算外部工具座標系-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
    * @brief 計算外部工具座標系-三點法
    * @param [out] tcp_pose 外部工具座標系
    * @return 錯誤碼 
    */ 
    int ComputeExTCF(ref DescPose tcp_pose); 

設置外部工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置外部工具座標系 
    * @param [in] id 座標系編號，20-39對應外部工具座標系0-19
    * @param [in] etcp 工具中心點相對末端法蘭中心位姿 
    * @param [in] etool 待定 
    * @return 錯誤碼 
    */
    int SetExToolCoord(int id, DescPose etcp, DescPose etool); 

設置外部工具座標系列表
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置外部工具座標系列表
    * @param  [in] id 座標系編號，20-39對應外部工具座標系0-19
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    int SetExToolList(int id, DescPose etcp, DescPose etool); 

根據點位信息計算工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 根據點位信息計算工件座標系
    * @param [in] method 計算方法；0：原點-x軸-z軸  1：原點-x軸-xy平面
    * @param [in] pos 三個TCP位置組
    * @param [in] refFrame 參考座標系
    * @return 錯誤碼
    */
    int ComputeWObjCoordWithPoints(int method, DescPose[] pos, int refFrame, ref DescPose coordRtn)

機器人外部工具座標系操作代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button20_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606f, 779.517f, 193.516f, 178.000f, 0.476f, -92.484f);
        JointPos p1Joint = new JointPos(-108.145f, -50.137f, 85.818f, -125.599f, -87.946f, 74.329f);

        DescPose p2Desc = new DescPose(-24.656f, 850.384f, 191.361f, 177.079f, -2.058f, -95.355f);
        JointPos p2Joint = new JointPos(-111.024f, -41.538f, 69.222f, -114.913f, -87.743f, 74.329f);

        DescPose p3Desc = new DescPose(-99.813f, 766.661f, 241.878f, -176.817f, 1.917f, -91.604f);
        JointPos p3Joint = new JointPos(-107.266f, -56.116f, 85.971f, -122.560f, -92.548f, 74.331f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetExTCPPoint(3);
        int rtn = robot.ComputeExTCF(ref coordRtn);
        Console.WriteLine($"ComputeExTCF                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetExToolCoord(1,  coordRtn,  offdese);
        robot.SetExToolList(1,  coordRtn,  offdese);
    }

設置工件座標系參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 設置工件參考點-三點法 
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

設置工件座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置工件座標系列表
    * @param  [in] id 座標系編號，範圍[0~14] 
    * @param  [in] coord  工件座標系相對於末端法蘭中心位姿
    * @param  [in] refFrame 參考座標系
    * @return  錯誤碼
    */    
    int SetWObjList(int id, DescPose coord, int refFrame);

獲取當前工件座標系
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前工件座標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件座標系位姿
    * @return  錯誤碼
    */   
    int GetWObjOffset(byte flag, ref DescPose desc_pos); 

機器人工件座標系操作代碼示例
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button19_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(-89.606, 779.517, 193.516, 178.000, 0.476, -92.484);
        JointPos p1Joint = new JointPos(-108.145, -50.137, 85.818, -125.599, -87.946, 74.329);

        DescPose p2Desc = new DescPose(-24.656, 850.384, 191.361, 177.079, -2.058, -95.355);
        JointPos p2Joint = new JointPos(-111.024, -41.538, 69.222, -114.913, -87.743, 74.329);

        DescPose p3Desc = new DescPose(-99.813, 766.661, 241.878, -176.817, 1.917, -91.604);
        JointPos p3Joint = new JointPos(-107.266, -56.116, 85.971, -122.560, -92.548, 74.331);

        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint,ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose[] posTCP = new DescPose[] { p1Desc, p2Desc, p3Desc };
        DescPose coordRtn = new DescPose();
        int rtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.MoveJ( p1Joint,  p1Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(1);
        robot.MoveJ( p2Joint,  p2Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(2);
        robot.MoveJ( p3Joint,  p3Desc, 1, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.SetWObjCoordPoint(3);
        rtn = robot.ComputeWObjCoord(1, 0, ref coordRtn);
        Console.WriteLine($"ComputeWObjCoord                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");

        robot.SetWObjCoord(1,  coordRtn, 0);
        robot.SetWObjList(1,  coordRtn, 0);

        DescPose getWobjDesc = new DescPose();
        rtn = robot.GetWObjOffset(0, ref getWobjDesc);
        Console.WriteLine($"GetWObjOffset                   {rtn}  coord is {coordRtn.tran.x} {coordRtn.tran.y} {coordRtn.tran.z} {coordRtn.rpy.rx} {coordRtn.rpy.ry} {coordRtn.rpy.rz}");   
    } 

設置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置全局速度
    * @param  [in]  vel  速度百分比，範圍[0~100]
    * @return  錯誤碼
    */
    int SetSpeed(int vel); 

設置機器人加速度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人加速度
    * @param [in] acc 機器人加速度百分比
    * @return 錯誤碼
    */
    int SetOaccScale(double acc)

獲取機器人默認速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取機器人默認速度
    * @param  [out]  vel  速度，單位mm/s
    * @return  錯誤碼
    */   
    int GetDefaultTransVel(ref double vel); 

設置末端負載重量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置末端負載重量
    * @param  [in] loadNum 負載編號
    * @param  [in] weight  負載重量，單位kg
    * @return  錯誤碼
    */
    int SetLoadWeight(int loadNum, float weight)

設置末端負載質心座標
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置末端負載質心座標
    * @param  [in] coord 質心座標，單位mm
    * @return  錯誤碼
    */
    int SetLoadCoord(DescTran coord); 

獲取當前負載的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前負載的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 負載重量，單位kg
    * @return  錯誤碼
    */
    int GetTargetPayload(byte flag, ref double weight); 

獲取當前負載的質心
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取當前負載的質心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 負載質心，單位mm
    * @return  錯誤碼
    */   
    int GetTargetPayloadCog(byte flag, ref DescTran cog);

設置機器人安裝方式
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置機器人安裝方式
    * @param  [in] install  安裝方式，0-正裝，1-側裝，2-倒裝
    * @return  錯誤碼
    */
    int SetRobotInstallPos(byte install); 

設置機器人安裝角度
+++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置機器人安裝角度，自由安裝
    * @param  [in] yangle  傾斜角
    * @param  [in] zangle  旋轉角
    * @return  錯誤碼
    */
    int SetRobotInstallAngle(double yangle, double zangle); 

獲取機器人安裝角度
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取機器人安裝角度
    * @param  [out] yangle 傾斜角
    * @param  [out] zangle 旋轉角
    * @return  錯誤碼
    */
    int GetRobotInstallAngle(ref double yangle, ref double zangle); 

設置系統變量值
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置系統變量值
    * @param  [in]  id  變量編號，範圍[1~20]
    * @param  [in]  value 變量值
    * @return  錯誤碼
    */
    int SetSysVarValue(int id, double value); 

獲取系統變量值
+++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取系統變量值
    * @param  [in] id 系統變量編號，範圍[1~20]
    * @param  [out] value  系統變量值
    * @return  錯誤碼
    */
    int GetSysVarValue(int id, ref double value); 

機器人常用設置代碼示例
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button21_Click(object sender, EventArgs e)
    {
        for (int i = 1; i < 100; i++)
        {
            robot.SetSpeed(i);
            robot.SetOaccScale(i);
            Thread.Sleep(30);
        }

        double defaultVel = 0.0f;
        robot.GetDefaultTransVel(ref defaultVel);
        Console.WriteLine($"GetDefaultTransVel is {defaultVel}");

        for (int i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i + 0.5f);
            Thread.Sleep(100);
        }

        for (int i = 1; i < 21; i++)
        {
            double value = 0;
            robot.GetSysVarValue(i, ref value);
            Console.WriteLine($"sys value  {i} is :{value}");
            Thread.Sleep(100);
        }

        robot.SetLoadWeight(0, 2.5f);

        DescTran loadCoord = new DescTran();
        loadCoord.x = 3.0f;
        loadCoord.y = 4.0f;
        loadCoord.z = 5.0f;
        robot.SetLoadCoord( loadCoord);

        Thread.Sleep(1000);

        double getLoad = 0.0f;
        robot.GetTargetPayload(0, ref getLoad);

        DescTran getLoadTran = new DescTran();
        robot.GetTargetPayloadCog(0, ref getLoadTran);
        Console.WriteLine($"get load is {getLoad}; get load cog is {getLoadTran.x} {getLoadTran.y} {getLoadTran.z}");

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0f, 25.0f);

        double anglex = 0.0f;
        double angley = 0.0f;
        robot.GetRobotInstallAngle(ref anglex, ref angley);
        Console.WriteLine($"GetRobotInstallAngle x:  {anglex};  y:  {angley}");
    }

關節摩擦力補償開關
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 關節摩擦力補償開關 
    * @param [in] state 0-關，1-開 
    * @return 錯誤碼 
    */ 
    int FrictionCompensationOnOff(byte state); 

設置關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-正裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_level(double[] coeff);

設置關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-側裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_wall(double[] coeff); 

設置關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-倒裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_ceiling(double[] coeff);

設置關節摩擦力補償係數-自由安裝
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置關節摩擦力補償係數-自由安裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    int SetFrictionValue_freedom(double[] coeff);
       
機器人設置關節摩擦力補償代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        double[] lcoeff = { 0.9f, 0.9f, 0.9f, 0.9f, 0.9f, 0.9f };
        double[] wcoeff = { 0.4f, 0.4f, 0.4f, 0.4f, 0.4f, 0.4f };
        double[] ccoeff = { 0.6f, 0.6f, 0.6f, 0.6f, 0.6f, 0.6f };
        double[] fcoeff = { 0.5f, 0.5f, 0.5f, 0.5f, 0.5f, 0.5f };

        int rtn = robot.FrictionCompensationOnOff(1);
        Console.WriteLine($"FrictionCompensationOnOff rtn is{rtn}");

        rtn = robot.SetFrictionValue_level(lcoeff);
        Console.WriteLine($"SetFrictionValue_level rtn is {rtn}");

        rtn = robot.SetFrictionValue_wall(wcoeff);
        Console.WriteLine($"SetFrictionValue_wall rtn is{rtn}");

        rtn = robot.SetFrictionValue_ceiling(ccoeff);
        Console.WriteLine($"SetFrictionValue_ceiling rtn is {rtn}");

        rtn = robot.SetFrictionValue_freedom(fcoeff);
        Console.WriteLine($"SetFrictionValue_freedom rtn is {rtn}");
    }

查詢機器人錯誤碼
++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 查詢機器人錯誤碼 
    * @param [out] maincode   主錯誤碼
    * @param [out] subcode    子錯誤碼
    * @return 錯誤碼 
    */ 
    int GetRobotErrorCode(ref int maincode, ref int subcode);

錯誤狀態清除
++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  錯誤狀態清除
    * @return  錯誤碼
    */
    int ResetAllError(); 

機器人故障狀態獲取及清除錯誤代碼示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnRobotSafetySet_Click(object sender, EventArgs e)
    {
        int maincode=0, subcode=0;
        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is {subcode}" );

        robot.ResetAllError();

        Thread.Sleep(1000);

        robot.GetRobotErrorCode(ref maincode, ref subcode);
        Console.WriteLine($"robot maincode is{maincode};  subcode is{subcode}");
    }

設置寬電壓控制箱溫度及風扇轉速監控參數
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置寬電壓控制箱溫度及風扇轉速監控參數
    * @param [in] enable 0-不使能監測；1-使能監測
    * @param [in] period 監測週期(s),範圍1-100
    * @return 錯誤碼
    */
    int SetWideBoxTempFanMonitorParam(int enable, int period);

獲取寬電壓控制箱溫度及風扇轉速監控參數
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取寬電壓控制箱溫度及風扇轉速監控參數
    * @param [out] enable 0-不使能監測；1-使能監測
    * @param [out] period 監測週期(s),範圍1-100
    * @return 錯誤碼
    */
    int GetWideBoxTempFanMonitorParam(ref int enable, ref int period);

代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void button46_Click(object sender, EventArgs e)
    {
        var pkg = new ROBOT_STATE_PKG(); 
        robot.SetWideBoxTempFanMonitorParam(1, 2);    
        int enable = 0;
        int period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }       
        int rtn = robot.SetWideBoxTempFanMonitorParam(0, 2);
        Console.WriteLine($"SetWideBoxTempFanMonitorParam rtn is {rtn}");       
        enable = 0;
        period = 0;
        robot.GetWideBoxTempFanMonitorParam(ref enable, ref period);
        Console.WriteLine($"GetWideBoxTempFanMonitorParam enable is {enable}   period is {period}");  
        for (int i = 0; i < 100; i++)
        {
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($" robot ctrl box temp is {pkg.wideVoltageCtrlBoxTemp}, fan current is {pkg.wideVoltageCtrlBoxFanVel}");
            Thread.Sleep(100);
        }
    }

設置焦點標定點
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焦點標定點
    * @param [in] pointNum 焦點標定點編號 1-8
    * @param [in] point 標定點座標
    * @return 錯誤碼
    */
    int SetFocusCalibPoint(int pointNum, DescPose point);

設置焦點座標
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焦點座標
    * @param [in] pos 焦點座標XYZ
    * @return 錯誤碼
    */
    int SetFocusPosition(DescTran pos);

開啓焦點跟隨
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 開啓焦點跟隨
    * @param [in] kp 比例參數，默認50.0
    * @param [in] kpredict 前饋參數，默認19.0
    * @param [in] aMax 最大角加速度限制，默認1440°/s^2
    * @param [in] vMax 最大角速度限制，默認180°/s
    * @param [in] type 鎖定X軸指向(0-參考輸入矢量；1-水平；2-垂直)
    * @return 錯誤碼
    */
    int FocusStart(double kp, double kpredict, double aMax, double vMax, int type);

停止焦點跟隨
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 停止焦點跟隨
    * @return 錯誤碼
    */
    int FocusEnd();

焦點跟隨代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.5  Web-3.8.4
    
.. code-block:: c#
    :linenos:

    private void button81_Click(object sender, EventArgs e)
    {
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
        robot.GetForwardKin(p1Joint,ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.GetForwardKin(p4Joint, ref p4Desc);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(1);
        robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(2);
        robot.MoveJ(p3Joint, p3Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(3);
        robot.MoveJ(p4Joint, p4Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.SetTcp4RefPoint(4);
        DescPose coordRtn = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int rtn = robot.ComputeTcp4(ref coordRtn);
        Console.WriteLine($"4 Point ComputeTool      {rtn} coord is {coordRtn.tran.x} ,{coordRtn.tran.y} ,{coordRtn.tran.z} ,{coordRtn.rpy.rx} ,{coordRtn.rpy.ry} ,{coordRtn.rpy.rz} ");
        robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0);
        robot.GetForwardKin(p1Joint, ref p1Desc);
        robot.GetForwardKin(p2Joint, ref p2Desc);
        robot.GetForwardKin(p3Joint, ref p3Desc);
        robot.SetFocusCalibPoint(1, p1Desc);
        robot.SetFocusCalibPoint(2, p2Desc);
        robot.SetFocusCalibPoint(3, p3Desc);
        DescTran resultPos = new DescTran(0.0, 0.0, 0.0);
        double accuracy = 0.0;
        rtn = robot.ComputeFocusCalib(3, ref resultPos, ref accuracy);
        Console.WriteLine($"ComputeFocusCalib coord is  {rtn},{ resultPos.x} ,{ resultPos.y}, { resultPos.z}, accuracy is {accuracy} ");
        rtn = robot.SetFocusPosition(resultPos);
        robot.GetForwardKin(p5Joint, ref p5Desc);
        robot.GetForwardKin(p6Joint, ref p6Desc);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusStart(50, 19, 710, 90, 0);
        robot.MoveL(p5Joint, p5Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.MoveL(p6Joint, p6Desc, 1, 0, 10, 100, 100, -1, 0, exaxisPos, 0, 1, offdese);
        robot.FocusEnd();
    }

關節扭矩傳感器靈敏度標定功能開啓
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩傳感器靈敏度標定功能開啓
    * @param [in] status 0-關閉；1-開啓
    * @return  錯誤碼
    */
    public int JointSensitivityEnable(int status);

關節扭矩傳感器靈敏度數據採集
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩傳感器靈敏度數據採集
    * @return 錯誤碼
    */
    public int JointSensitivityCollect();

獲取關節扭矩傳感器靈敏度標定結果
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 取得關節扭矩感測器靈敏度標定結果
    * @param [out] calibResult j1~j6 關節靈敏度 [0-1]
    * @param [out] linearity j1~j6 關節線性度 [0-1]
    * @return 錯誤碼
    */
    public int JointSensitivityCalibration(double calibResult[6], double linearity[6]);

取得關節扭矩感測器遲滯誤差
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 取得關節扭矩感測器遲滯誤差
    * @param [out] hysteresisError j1~j6 關節遲滯誤差
    * @return 錯誤碼
    */
    public int JointHysteresisError(ref double[] hysteresisError);
    
取得關節扭矩感測器重複精度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:
    
    /**
    * @brief 取得關節扭矩感測器重複精度
    * @param [out] repeatability j1~j6 關節扭矩感測器重複精度
    * @return 錯誤碼
    */
    public int JointRepeatability(ref double[] repeatability);
    
設定關節力感測器參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定關節力感測器參數
    * @param [in] M J1-J6 質量係數 [0.001 ~ 10]
    * @param [in] B J1-J6 阻尼係數 [0.001 ~ 10]
    * @param [in] K J1-J6 剛度係數 [0.001 ~ 10]
    * @param [in] threshold 力控制閾值，Nm
    * @param [in] sensitivity 靈敏度, Nm/V, [0 ~ 10]
    * @param [in] setZeroFlag 功能開啟標誌位；0-關閉；1-開啟；2-位置1記錄零點；3-位置2記錄零點
    * @return 錯誤碼
    */
    public int SetAdmittanceParams(double[] M, double[] B, double[] K, double[] threshold, double[] sensitivity, int setZeroFlag);

關節扭矩傳感器靈敏度自動標定代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public int TestSensitivityCalib()
    {
        int rtn; 
        rtn = robot.JointSensitivityEnable(0);
        rtn = robot.JointSensitivityEnable(1);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");

        JointPos curJPos = new JointPos(0, 0, 0, 0, 0, 0);
        robot.GetActualJointPosDegree(0, ref curJPos);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        JointPos[] jointPoses = new JointPos[]
        {
            new JointPos(curJPos.jPos[0], 0, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -30, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -60, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -90, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -120, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -150, 0, -90, 0.02, curJPos.jPos[5]),
            new JointPos(curJPos.jPos[0], -180, 0, -90, 0.02, curJPos.jPos[5])
        };
        for (int i = 0; i < jointPoses.Length; i++)
        {
            DescPose descPos = new DescPose(0, 0, 0, 0, 0, 0);
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            Thread.Sleep(i == 0 ? 200 : 100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {i + 1} rtn is {rtn}");
            Thread.Sleep(100);
        }

        for (int i = jointPoses.Length - 2; i >= 0; i--)
        {
            DescPose descPos = new DescPose();
            robot.GetForwardKin(jointPoses[i], ref descPos);
            robot.MoveJ(jointPoses[i], descPos, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            Thread.Sleep(100);
            rtn = robot.JointSensitivityCollect();
            Console.WriteLine($"JointSensitivityCollect {jointPoses.Length + (jointPoses.Length - 1 - i)} rtn is {rtn}");
            Thread.Sleep(100);
        }
        double[] calibResult = new double[6];
        double[] linearity = new double[6];
        rtn = robot.JointSensitivityCalibration(ref calibResult, ref linearity);
        Console.WriteLine($"JointSensitivityCalibration rtn is {rtn}");
        rtn = robot.JointSensitivityEnable(0);
        Console.WriteLine($"JointSensitivityEnable rtn is {rtn}");
        Console.WriteLine($"jointSensor Calib result is {calibResult[0]:F6} {calibResult[1]:F6} {calibResult[2]:F6} {calibResult[3]:F6} {calibResult[4]:F6} {calibResult[5]:F6}");
        Console.WriteLine($"jointSensor linearity is {linearity[0]:F6} {linearity[1]:F6} {linearity[2]:F6} {linearity[3]:F6} {linearity[4]:F6} {linearity[5]:F6}"); 
        double[] hysteresisError = new double[6];
        rtn = robot.JointHysteresisError(ref hysteresisError);
        Console.WriteLine($"JointHysteresisError result is {hysteresisError[0]:F6} {hysteresisError[1]:F6} {hysteresisError[2]:F6} {hysteresisError[3]:F6} {hysteresisError[4]:F6} {hysteresisError[5]:F6}");   
        double[] repeatability = new double[6];
        rtn = robot.JointRepeatability(ref repeatability);
        Console.WriteLine($"JointRepeatability result is {repeatability[0]:F6} {repeatability[1]:F6} {repeatability[2]:F6} {repeatability[3]:F6} {repeatability[4]:F6} {repeatability[5]:F6}");
        double[] M = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] B = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        double[] K = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        double[] threshold = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        int setZeroFlag = 1;
        rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag);
        Console.WriteLine($"SetAdmittanceParams rtn is {rtn}");
        robot.CloseRPC();
        return 0;
    }


獲取機器人8個從站端口錯誤幀數
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人8個從站端口錯誤幀數
    * @param [out] inRecvErr 輸入接收錯誤幀數 
    * @param [out] inCRCErr 輸入CRC錯誤幀數 
    * @param [out] inTransmitErr 輸入轉發錯誤幀數 
    * @param [out] inLinkErr 輸入鏈接錯誤幀數 
    * @param [out] outRecvErr 輸出接收錯誤幀數
    * @param [out] outCRCErr 輸出CRC錯誤幀數
    * @param [out] outTransmitErr 輸出轉發錯誤幀數
    * @param [out] outLinkErr 輸出鏈接錯誤幀數
    * @return 錯誤碼
    */
    public int GetSlavePortErrCounter(ref int[] inRecvErr,ref int[] inCRCErr,ref int[] inTransmitErr,ref int[] inLinkErr,ref int[] outRecvErr,ref int[] outCRCErr,ref int[] outTransmitErr,ref int[] outLinkErr);

從站端口錯誤幀清零
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 從站端口錯誤幀清零
    * @param [in] slaveID 從站編號0~7
    * @return 錯誤碼
    */
    public int SlavePortErrCounterClear(int slaveID);

獲取從站端口錯誤幀代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    public void TestSlavePortErr()
    {
        int[] inRecvErr = new int[8];
        int[] inCRCErr = new int[8];
        int[] inTransmitErr = new int[8];
        int[] inLinkErr = new int[8];
        int[] outRecvErr = new int[8];
        int[] outCRCErr = new int[8];
        int[] outTransmitErr = new int[8];
        int[] outLinkErr = new int[8];

        robot.GetSlavePortErrCounter(ref inRecvErr, ref inCRCErr, ref inTransmitErr, ref inLinkErr,
            ref outRecvErr, ref outCRCErr, ref outTransmitErr, ref outLinkErr);

        for (int i = 0; i < 8; i++)
        {
            if (inRecvErr[i] != 0)
            {
                Console.WriteLine($"inRecvErr {i} is {inRecvErr[i]}");
            }

            if (inCRCErr[i] != 0)
            {
                Console.WriteLine($"inCRCErr {i} is {inCRCErr[i]}");
            }

            if (inTransmitErr[i] != 0)
            {
                Console.WriteLine($"inTransmitErr {i} is {inTransmitErr[i]}");
            }

            if (inLinkErr[i] != 0)
            {
                Console.WriteLine($"inLinkErr {i} is {inLinkErr[i]}");
            }

            if (outRecvErr[i] != 0)
            {
                Console.WriteLine($"outRecvErr {i} is {outRecvErr[i]}");
            }

            if (outCRCErr[i] != 0)
            {
                Console.WriteLine($"outCRCErr {i} is {outCRCErr[i]}");
            }

            if (outTransmitErr[i] != 0)
            {
                Console.WriteLine($"outTransmitErr {i} is {outTransmitErr[i]}");
            }

            if (outLinkErr[i] != 0)
            {
                Console.WriteLine($"outLinkErr {i} is {outLinkErr[i]}");
            }
        }
        Console.WriteLine("others has no err!");

        for (int i = 0; i < 8; i++)
        {
            robot.SlavePortErrCounterClear(i);
        }

        robot.CloseRPC();
    }

設置各軸速度前饋係數
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置各軸速度前饋係數
    * @param [in] radio 各軸速度前饋係數
    * @return 錯誤碼
    */
    public int SetVelFeedForwardRatio(double radio[6]);

獲取各軸速度前饋係數
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取各軸速度前饋係數
    * @param [out] radio 各軸速度前饋係數
    * @return 錯誤碼
    */
    public int GetVelFeedForwardRatio(ref double radio[6]);

機器人設置速度前饋代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    public void TestVelFeedForwardRatio()
    {

        double[] setRadio = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
        robot.SetVelFeedForwardRatio(setRadio);
        double[] getRadio = new double[6] { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        robot.GetVelFeedForwardRatio(ref getRadio);
        Console.WriteLine($" {getRadio[0]:F6} {getRadio[1]:F6} {getRadio[2]:F6} {getRadio[3]:F6} {getRadio[4]:F6} {getRadio[5]:F6}");
    }

光電感測器TCP標定-計算工具RPY
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定-計算工具RPY
    * @param [in] Btool 機器人笛卡爾位置
    * @param [in] Etool 目前工具座標系數值
    * @param [in] sensor 目前感測器座標系數值(暫未開放)
    * @param [in] radius 圓周運動半徑mm(暫未開放)
    * @param [in] dz 沿基座標系z軸負方向運動距離；當dz = 10000時，函數直接回傳工具RPY
    * @param [out] TCPRPY 工具RPY數值
    * @return 錯誤碼
    */
    public int TCPComputeRPY(DescPose Btool, DescPose Etool, DescPose sensor, double radius, double dz, out Rpy TCPRPY);

光電感測器TCP標定-計算工具XYZ
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定-計算工具XYZ
    * @param [in] select 0-計算工具TCP；1-計算感測器原點；2-計算感測器姿態；3-直接回傳工具TCP；4-記錄目前工件座標系和工具座標系
    * @param [in] originDirection 0-X方向；1-Y方向；2-Z方向
    * @param [in] pos1 機器人笛卡爾位置1
    * @param [in] pos2 機器人笛卡爾位置2
    * @param [in] pos3 機器人笛卡爾位置3
    * @param [in] pos4 機器人笛卡爾位置4
    * @param [out] TCP 工具XYZ數值
    * @return 錯誤碼
    */
    public int TCPComputeXYZ(int select, double originDirection, DescTran pos1, DescTran pos2,DescTran pos3, DescTran pos4, out DescTran TCP);

光電感測器TCP標定-開始記錄末端法蘭中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定-開始記錄末端法蘭中心位置
    * @return 錯誤碼
    */
    public int TCPRecordFlangePosStart();

光電感測器TCP標定-停止記錄末端法蘭中心位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定-停止記錄末端法蘭中心位置
    * @return 錯誤碼
    */
    public int TCPRecordFlangePosEnd();

光電感測器TCP標定-取得末端工具中心點位置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定-取得末端工具中心點位置
    * @param [out] TCP 工具中心點位置(x,y,z)
    * @return 錯誤碼
    */
    public int TCPGetRecordFlangePos(out DescTran TCP);

光電感測器TCP標定
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 光電感測器TCP標定
    * @param [in] luaPath 自動標定lua程式路徑："FR_CalibrateTheToolTcp.lua"
    * @param [in] offsetX 示教點偏移(x,y,z)mm
    * @param [out] TCP 標定後的工具座標系(x,y,z,rx,ry,rz)
    * @return 錯誤碼
    */
    public int PhotoelectricSensorTCPCalibration(string luaPath, DescTran offset, out DescPose TCP);

光電感測器TCP標定程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestPhotoelectricSensorTCPCalib()
    {
        ROBOT_STATE_PKG pkg =new ROBOT_STATE_PKG();
        DescTran offset = new DescTran( 10.0, 10.0, 3.0 );
        DescPose TCP = new DescPose();
        int rtn = robot.PhotoelectricSensorTCPCalibration("FR_CalibrateTheToolTcp.lua", offset, out TCP);
        Console.WriteLine($"PhotoelectricSensorTCPCalibration : {rtn}");
        Console.WriteLine($"工具TCP座標: X={TCP.tran.x:F3}, Y={TCP.tran.y:F3}, Z={TCP.tran.z:F3}");
        Console.WriteLine($"工具RPY姿態: RX={TCP.rpy.rx:F3}, RY={TCP.rpy.ry:F3}, RZ={TCP.rpy.rz:F3}");
    }

即時設置全域速度
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 即時設置全域速度
    * @param [in] vel 速度百分比，範圍[0~100]
    * @return 錯誤碼
    */
    public int SetWeaveOffsetRT(DescPose offset)    
