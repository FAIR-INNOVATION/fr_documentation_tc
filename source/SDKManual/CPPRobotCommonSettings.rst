机器人常用设置
=================

.. toctree:: 
    :maxdepth: 5

设置全局速度
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置全局速度
    * @param  [in]  vel  速度百分比，范围[0~100]
    * @return  错误码
    */
    errno_t  SetSpeed(int vel);

设置系统变量值
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置系统变量值
    * @param  [in]  id  变量编号，范围[1~20]
    * @param  [in]  value 变量值
    * @return  错误码
    */
    errno_t  SetSysVarValue(int id, float value);

设置工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工具参考点-六点法
     * @param [in] point_num 点编号,范围[1~6] 
     * @return 错误码
     */
    errno_t SetToolPoint(int point_num);

计算工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算工具坐标系
     * @param [out] tcp_pose 工具坐标系
     * @return 错误码
     */
    errno_t ComputeTool(DescPose *tcp_pose);

设置工具参考点-四点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工具参考点-四点法
     * @param [in] point_num 点编号,范围[1~4] 
     * @return 错误码
     */
    errno_t SetTcp4RefPoint(int point_num);

计算工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算工具坐标系
     * @param [out] tcp_pose 工具坐标系
     * @return 错误码
     */
    errno_t ComputeTcp4(DescPose *tcp_pose);

设置工具坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  设置工具坐标系
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工具中心点相对于末端法兰中心位姿
	 * @param  [in] type  0-工具坐标系，1-传感器坐标系
	 * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
	 * @param  [in] toolID 工具ID
	 * @param  [in] loadNum 负载编号
	 * @return  错误码
	 */
	errno_t SetToolCoord(int id, DescPose *coord, int type, int install, int toolID, int loadNum);

设置工具坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  设置工具坐标系列表
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工具中心点相对于末端法兰中心位姿
	 * @param  [in] type  0-工具坐标系，1-传感器坐标系
	 * @param  [in] install 安装位置，0-机器人末端，1-机器人外部
	 * @param  [in] loadNum 负载编号
	 * @return  错误码
	 */
	errno_t SetToolList(int id, DescPose *coord, int type, int install, int loadNum);

设置外部工具参考点-六点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置外部工具参考点-六点法
     * @param [in] point_num 点编号,范围[1~4] 
     * @return 错误码
     */
    errno_t SetExTCPPoint(int point_num);

计算外部工具坐标系
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  计算外部工具坐标系
     * @param [out] tcp_pose 外部工具坐标系
     * @return 错误码
     */
    errno_t ComputeExTCF(DescPose *tcp_pose);  

设置外部工具坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  设置外部工具坐标系
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    errno_t  SetExToolCoord(int id, DescPose *etcp, DescPose *etool);

设置外部工具坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  设置外部工具坐标系列表
    * @param  [in] id 坐标系编号，范围[0~14]
    * @param  [in] etcp  工具中心点相对末端法兰中心位姿
    * @param  [in] etool  待定
    * @return  错误码
    */
    errno_t  SetExToolList(int id, DescPose *etcp, DescPose *etool);

设置工件参考点-三点法
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置工件参考点-三点法
     * @param [in] point_num 点编号,范围[1~3] 
     * @return 错误码
     */
    errno_t SetWObjCoordPoint(int point_num);

计算工件坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief  计算工件坐标系
	 * @param [in] method 计算方法 0：原点-x轴-z轴  1：原点-x轴-xy平面
	 * @param [in] refFrame 参考坐标系
	 * @param [out] wobj_pose 工件坐标系
	 * @return 错误码
	 */
	errno_t ComputeWObjCoord(int method, int refFrame, DescPose *wobj_pose);

设置工件坐标系
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  设置工件坐标系
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
	 * @param  [in] refFrame 参考坐标系
	 * @return  错误码
	 */
	errno_t SetWObjCoord(int id, DescPose *coord, int refFrame);

设置工件坐标系列表
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	 * @brief  设置工件坐标系列表
	 * @param  [in] id 坐标系编号，范围[0~14]
	 * @param  [in] coord  工件坐标系相对于末端法兰中心位姿
	 * @param  [in] refFrame 参考坐标系
	 * @return  错误码
	 */
	errno_t SetWObjList(int id, DescPose *coord, int refFrame);

设置末端负载重量
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置末端负载重量
    * @param  [in] weight  负载重量，单位kg
    * @return  错误码
    */
    errno_t  SetLoadWeight(float weight);

设置末端负载质心坐标
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置末端负载质心坐标
    * @param  [in] coord 质心坐标，单位mm
    * @return  错误码
    */
    errno_t  SetLoadCoord(DescTran *coord);

设置机器人安装方式
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置机器人安装方式
    * @param  [in] install  安装方式，0-正装，1-侧装，2-倒装
    * @return  错误码
    */
    errno_t  SetRobotInstallPos(uint8_t install);   

设置机器人安装角度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置机器人安装角度，自由安装
    * @param  [in] yangle  倾斜角
    * @param  [in] zangle  旋转角
    * @return  错误码
    */
    errno_t  SetRobotInstallAngle(double yangle, double zangle);

等待指定时间
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  等待指定时间
    * @param  [in]  t_ms  单位ms
    * @return  错误码
    */
    errno_t  WaitMs(int t_ms);

代码示例
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
        FRRobot robot;                 //实例化机器人对象
        robot.RPC("192.168.58.2");     //与机器人控制器建立通信连接

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

代码示例
+++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:
    
    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
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

设置机器人加速度
+++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

	/**
	 * @brief 设置机器人加速度
	 * @param [in] acc 机器人加速度百分比
	 * @return 错误码
	 */
	errno_t SetOaccScale(double acc);