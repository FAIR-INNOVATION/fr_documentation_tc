機器人常用設定
=================

.. toctree:: 
    :maxdepth: 5

設定全域速度
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定全域速度
    * @param  [in]  vel  速度百分比，範圍[0~100]
    * @return  錯誤碼
    */
    errno_t  SetSpeed(int vel);

設定係統變數值
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定係統變數值
    * @param  [in]  id  變數編號，範圍[1~20]
    * @param  [in]  value 變數值
    * @return  錯誤碼
    */
    errno_t  SetSysVarValue(int id, float value);

設定工具參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定工具參考點-六點法
     * @param [in] point_num 點編號,範圍[1~6] 
     * @return 錯誤碼
     */
    errno_t SetToolPoint(int point_num);

計算工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算工具座標系
     * @param [out] tcp_pose 工具座標系
     * @return 錯誤碼
     */
    errno_t ComputeTool(DescPose *tcp_pose);

設定工具參考點-四點法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定工具參考點-四點法
     * @param [in] point_num 點編號,範圍[1~4] 
     * @return 錯誤碼
     */
    errno_t SetTcp4RefPoint(int point_num);

計算工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算工具座標系
     * @param [out] tcp_pose 工具座標系
     * @return 錯誤碼
     */
    errno_t ComputeTcp4(DescPose *tcp_pose);

設定工具坐標系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  設定工具坐標系
	 * @param  [in] id 座標系編號，範圍[0~14]
	 * @param  [in] coord  工具中心點相對於末端法蘭中心位姿
	 * @param  [in] type  0-工具坐標系，1-感測器座標系
	 * @param  [in] install 安裝位置，0-機器人末端，1-機器人外部
	 * @param  [in] toolID 工具ID
	 * @param  [in] loadNum 負載編號
	 * @return  錯誤碼
	 */
	errno_t SetToolCoord(int id, DescPose *coord, int type, int install, int toolID, int loadNum);

設定工具坐標系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
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
	errno_t SetToolList(int id, DescPose *coord, int type, int install, int loadNum);

設定外部工具參考點-六點法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定外部工具參考點-六點法
     * @param [in] point_num 點編號,範圍[1~4] 
     * @return 錯誤碼
     */
    errno_t SetExTCPPoint(int point_num);

计算外部工具座標系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算外部工具座標系
     * @param [out] tcp_pose 外部工具座標系
     * @return 錯誤碼
     */
    errno_t ComputeExTCF(DescPose *tcp_pose);  

設定外部工具坐標系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  設定外部工具坐標系
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    errno_t  SetExToolCoord(int id, DescPose *etcp, DescPose *etool);

設定外部工具坐標系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  設定外部工具坐標系列表
    * @param  [in] id 座標系編號，範圍[0~14]
    * @param  [in] etcp  工具中心點相對末端法蘭中心位姿
    * @param  [in] etool  待定
    * @return  錯誤碼
    */
    errno_t  SetExToolList(int id, DescPose *etcp, DescPose *etool);

設定工件參考點-三點法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定工件參考點-三點法
     * @param [in] point_num 點編號,範圍[1~3] 
     * @return 錯誤碼
     */
    errno_t SetWObjCoordPoint(int point_num);

計算工件座標系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  計算工件座標系
	 * @param [in] method 計算方法 0：原點-x軸-z軸  1：原點-x軸-xy平面
	 * @param [in] refFrame 參考座標系
	 * @param [out] wobj_pose 工件座標系
	 * @return 錯誤碼
	 */
	errno_t ComputeWObjCoord(int method, int refFrame, DescPose *wobj_pose);

設定工件座標系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  設定工件座標系
	 * @param  [in] id 座標系編號，範圍[0~14]
	 * @param  [in] coord  工件坐標系相對於末端法蘭中心位姿
	 * @param  [in] refFrame 參考座標系
	 * @return  錯誤碼
	 */
	errno_t SetWObjCoord(int id, DescPose *coord, int refFrame);

設定工件座標系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	 * @brief  設定工件座標系列表
	 * @param  [in] id 座標系編號，範圍[0~14]
	 * @param  [in] coord  工件坐標系相對於末端法蘭中心位姿
	 * @param  [in] refFrame 參考座標系
	 * @return  錯誤碼
	 */
	errno_t SetWObjList(int id, DescPose *coord, int refFrame);

設定末端負載重量
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
    * @brief  設定末端負載重量
    * @param  [in] loadNum 負載編號
    * @param  [in] weight  負載重量，單位kg
    * @return  錯誤碼
    */
    errno_t SetLoadWeight(int loadNum = 0, float weight);

設定末端負載質心座標
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定末端負載質心座標
    * @param  [in] coord 質心座標，單位mm
    * @return  錯誤碼
    */
    errno_t  SetLoadCoord(DescTran *coord);

設定機器人安裝方式
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定機器人安裝方式
    * @param  [in] install  安裝方式，0-正裝，1-側裝，2-倒裝
    * @return  錯誤碼
    */
    errno_t  SetRobotInstallPos(uint8_t install);   

設定機器人安裝角度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定機器人安裝角度，自由安裝
    * @param  [in] yangle  傾斜角
    * @param  [in] zangle  旋轉角
    * @return  錯誤碼
    */
    errno_t  SetRobotInstallAngle(double yangle, double zangle);

等待指定時間
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  等待指定時間
    * @param  [in]  t_ms  單位ms
    * @return  錯誤碼
    */
    errno_t  WaitMs(int t_ms);

代碼範例
+++++++++++++++
.. code-block:: c++
    :linenos:

    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #include "FRRobot.h"
    #include "RobotTypes.h"

    using namespace std;

    int main(void)
    {
        FRRobot robot;                 //實例化機器人對象
        robot.RPC("192.168.58.2");     //與機器人控制器建立通信连接

        int i;
        float value;
        int id;
        int type;
        int install;

        DescTran coord;
        DescPose t_coord, etcp, etool, w_coord;
        memset(&coord, 0, sizeof(DescTran));
        memset(&t_coord, 0, sizeof(DescPose));
        memset(&etcp, 0, sizeof(DescPose));
        memset(&etool, 0, sizeof(DescPose));
        memset(&w_coord, 0, sizeof(DescPose));

        robot.SetSpeed(20);

        for(i = 1; i < 21; i++)
        {
            robot.SetSysVarValue(i, i+0.5);
            robot.WaitMs(1000);
        }

        for(i = 1; i < 21; i++)
        {
            robot.GetSysVarValue(i, &value);
            printf("sys value:%f\n", value);
        }

        robot.SetLoadWeight(2.5);

        coord.x = 3.0;
        coord.y = 4.0;
        coord.z = 5.0;

        robot.SetLoadCoord(&coord);

        id = 10;
        t_coord.tran.x = 1.0;
        t_coord.tran.y = 2.0;
        t_coord.tran.z = 3.0;
        t_coord.rpy.rx = 4.0;
        t_coord.rpy.ry = 5.0;
        t_coord.rpy.rz = 6.0;
        type = 0;
        install = 0;
        robot.SetToolCoord(id, &t_coord, type, install);
        robot.SetToolList(id, &t_coord, type, install);

        etcp.tran.x = 1.0;
        etcp.tran.y = 2.0;
        etcp.tran.z = 3.0;
        etcp.rpy.rx = 4.0;
        etcp.rpy.ry = 5.0;
        etcp.rpy.rz = 6.0;
        etool.tran.x = 11.0;
        etool.tran.y = 22.0;
        etool.tran.z = 33.0;
        etool.rpy.rx = 44.0;
        etool.rpy.ry = 55.0;
        etool.rpy.rz = 66.0;
        id = 11;
        robot.SetExToolCoord(id, &etcp, &etool);
        robot.SetExToolList(id, &etcp, &etool);

        w_coord.tran.x = 11.0;
        w_coord.tran.y = 12.0;
        w_coord.tran.z = 13.0;
        w_coord.rpy.rx = 14.0;
        w_coord.rpy.ry = 15.0;
        w_coord.rpy.rz = 16.0;   
        id = 12;
        robot.SetWObjCoord(id, &w_coord);
        robot.SetWObjList(id, &w_coord);

        robot.SetRobotInstallPos(0);
        robot.SetRobotInstallAngle(15.0,25.0);

        return 0;
    }

代碼範例
+++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:
    
    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的頭文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的頭文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>
    using namespace std;

    int main(void)
    {
        FRRobot robot;
        robot.RPC("192.168.58.2");

        int i;
        float value;
        int tool_id, etool_id, user_id;
        int type;
        int install;
        int retval = 0;

        DescTran coord;
        DescPose t_coord, etcp, etool, w_coord;
        memset(&coord, 0, sizeof(DescTran));
        memset(&t_coord, 0, sizeof(DescPose));
        memset(&etcp, 0, sizeof(DescPose));
        memset(&etool, 0, sizeof(DescPose));
        memset(&w_coord, 0, sizeof(DescPose));

        DescPose tool0_pose;
        memset(&tool0_pose, 0, sizeof(DescPose));
        printf("SetToolPoint start\n");
        std::this_thread::sleep_for(std::chrono::seconds(3));
        for (int i = 1; i < 7; i++)
        {
            retval = robot.SetToolPoint(i);
            printf("SetToolPoint retval is: %d\n", retval);
        }
        printf("SetToolPoint end\n");

        retval = robot.ComputeTool(&tool0_pose);
        printf("ComputeTool retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", tool0_pose.tran.x, tool0_pose.tran.y, tool0_pose.tran.z, tool0_pose.rpy.rx, tool0_pose.rpy.ry, tool0_pose.rpy.rz);

        DescPose tcp4_0_pose;
        memset(&tcp4_0_pose, 0, sizeof(DescPose));
        for (int i = 1; i < 5; i++)
        {
            retval = robot.SetTcp4RefPoint(i);
            printf("SetTcp4RefPoint retval is: %d\n", retval);
        }
        retval = robot.ComputeTcp4(&tcp4_0_pose);
        printf("ComputeTcp4 retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", tcp4_0_pose.tran.x, tcp4_0_pose.tran.y, tcp4_0_pose.tran.z, tcp4_0_pose.rpy.rx, tcp4_0_pose.rpy.ry, tcp4_0_pose.rpy.rz);

        DescPose extcp_0_pose;
        memset(&extcp_0_pose, 0, sizeof(DescPose));
        printf("SetExTCPPoint start\n");
        for (int i = 1; i < 7; i++)
        {
            retval = robot.SetExTCPPoint(i);
            printf("SetExTCPPoint retval is: %d\n", retval);
        }
        printf("SetExTCPPoint end\n");

        retval = robot.ComputeExTCF(&extcp_0_pose);
        printf("ComputeExTCF retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", extcp_0_pose.tran.x, extcp_0_pose.tran.y, extcp_0_pose.tran.z, extcp_0_pose.rpy.rx, extcp_0_pose.rpy.ry, extcp_0_pose.rpy.rz);

        DescPose wobj_0_pose;
        memset(&wobj_0_pose, 0, sizeof(DescPose));
        for (int i = 1; i < 4; i++)
        {
            retval = robot.SetWObjCoordPoint(i);
            printf("SetWObjCoordPoint retval is: %d\n", retval);
        }
        retval = robot.ComputeWObjCoord(0, &wobj_0_pose);
        printf("ComputeWObjCoord retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", wobj_0_pose.tran.x, wobj_0_pose.tran.y, wobj_0_pose.tran.z, wobj_0_pose.rpy.rx, wobj_0_pose.rpy.ry, wobj_0_pose.rpy.rz);
    }

設定機器人加速度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

	/**
	 * @brief 設定機器人加速度
	 * @param [in] acc 機器人加速度百分比
	 * @return 錯誤碼
	 */
	errno_t SetOaccScale(double acc);

根據點位資訊計算工具座標系
+++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 根據點位資訊計算工具座標系
	 * @param [in] method 計算方法；0-四點法；1-六點法
	 * @param [in] pos 關節位置組，四點法時數組長度為4個，六點法時數組長度為6個
	 * @param [out] coord 工具座標系結果
	 * @return 錯誤碼
    */
	errno_t ComputeToolCoordWithPoints(int method, JointPos pos[], DescPose& coord);
    
根據點位資訊計算工件座標系
+++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 根據點位資訊計算工件座標系
	 * @param [in] method 計算方法；0：原點-x軸-z軸 1：原點-x軸-xy平面
	 * @param [in] pos 三個TCP位置組
	 * @param [in] refFrame 參考座標系
	 * @param [out] coord 工具座標系結果
	 * @return 錯誤碼
    */
	errno_t ComputeWObjCoordWithPoints(int method, DescPose pos[], int refFrame, DescPose& coord);

代碼範例
+++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    void TestTCP6(FRRobot* robot)
    {
        DescPose p1Desc(-394.073, -276.405, 399.451, -133.692, 7.657, -139.047);
        JointPos p1Joint(15.234, -88.178, 96.583, -68.314, -52.303, -122.926);

        DescPose p2Desc(-187.141, -444.908, 432.425, 148.662, 15.483, -90.637);
        JointPos p2Joint(61.796, -91.959, 101.693, -102.417, -124.511, -122.767);

        DescPose p3Desc(-368.695, -485.023, 426.640, -162.588, 31.433, -97.036);
        JointPos p3Joint(43.896, -64.590, 60.087, -50.269, -94.663, -122.652);

        DescPose p4Desc(-291.069, -376.976, 467.560, -179.272, -2.326, -107.757);
        JointPos p4Joint(39.559, -94.731, 96.307, -93.141, -88.131, -122.673);

        DescPose p5Desc(-284.140, -488.041, 478.579, 179.785, -1.396, -98.030);
        JointPos p5Joint(49.283, -82.423, 81.993, -90.861, -89.427, -122.678);

        DescPose p6Desc(-296.307, -385.991, 484.492, -178.637, -0.057, -107.059);
        JointPos p6Joint(40.141, -92.742, 91.410, -87.978, -88.824, -122.808);

        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);

        JointPos posJ[6] = { p1Joint , p2Joint , p3Joint , p4Joint , p5Joint , p6Joint };
        DescPose coordRtn = {};
        int rtn = robot->ComputeToolCoordWithPoints(1, posJ, coordRtn);
        printf("ComputeToolCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);


        robot->MoveJ(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(1);
        robot->MoveJ(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(2);
        robot->MoveJ(&p3Joint, &p3Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(3);
        robot->MoveJ(&p4Joint, &p4Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(4);
        robot->MoveJ(&p5Joint, &p5Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(5);
        robot->MoveJ(&p6Joint, &p6Desc, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetToolPoint(6);
        robot->ComputeTool(&coordRtn);
        printf("ComputeTool                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);

    }

    void TestWObj(FRRobot* robot)
    {
        DescPose p1Desc(-275.046, -293.122, 28.747, 174.533, -1.301, -112.101);
        JointPos p1Joint(35.207, -95.350, 133.703, -132.403, -93.897, -122.768);

        DescPose p2Desc(-280.339, -396.053, 29.762, 174.621, -3.448, -102.901);
        JointPos p2Joint(44.304, -85.020, 123.889, -134.679, -92.658, -122.768);

        DescPose p3Desc(-270.597, -290.603, 83.034, 179.314, 0.808, -114.171);
        JointPos p3Joint(32.975, -99.175, 125.966, -116.484, -91.014, -122.857);

        

        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);

        DescPose posTCP[3] = { p1Desc , p2Desc , p3Desc };
        DescPose coordRtn = {};
        int rtn = robot->ComputeWObjCoordWithPoints(1, posTCP, 0, coordRtn);
        printf("ComputeToolCoordWithPoints    %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);


        robot->MoveJ(&p1Joint, &p1Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetWObjCoordPoint(1);
        robot->MoveJ(&p2Joint, &p2Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetWObjCoordPoint(2);
        robot->MoveJ(&p3Joint, &p3Desc, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->SetWObjCoordPoint(3);
        robot->ComputeWObjCoord(1, 0, &coordRtn);
        printf("ComputeTool                   %d  coord is %f %f %f %f %f %f \n", rtn, coordRtn.tran.x, coordRtn.tran.y, coordRtn.tran.z, coordRtn.rpy.rx, coordRtn.rpy.ry, coordRtn.rpy.rz);
    }