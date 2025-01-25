機器人軌跡復現
=================

.. toctree:: 
    :maxdepth: 5

設定TPD軌跡記錄參數
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定TPD軌跡記錄參數
    * @param  [in] type  記錄資料類型，1-關節位置
    * @param  [in] name  軌跡檔名
    * @param  [in] period_ms  資料採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    errno_t  SetTPDParam(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose);

開始TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  開始TPD軌跡記錄
    * @param  [in] type  記錄資料類型，1-關節位置
    * @param  [in] name  軌跡檔名
    * @param  [in] period_ms  資料採樣週期，固定值2ms或4ms或8ms
    * @param  [in] di_choose  DI選擇,bit0~bit7對應控制箱DI0~DI7，bit8~bit9對應末端DI0~DI1，0-不選擇，1-選擇
    * @param  [in] do_choose  DO選擇,bit0~bit7對應控制箱DO0~DO7，bit8~bit9對應末端DO0~DO1，0-不選擇，1-選擇
    * @return  錯誤碼
    */
    errno_t  SetTPDStart(int type, char name[30], int period_ms, uint16_t di_choose, uint16_t do_choose); 

停止TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  停止TPD軌跡記錄
    * @return  錯誤碼
    */
    errno_t  SetWebTPDStop();

删除TPD軌跡記錄
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  删除TPD軌跡記錄
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */   
    errno_t  SetTPDDelete(char name[30]);

代碼範例
++++++++++++++
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

        int type = 1;
        char name[30] = "tpd2023";
        int period_ms = 4;
        uint16_t di_choose = 0;
        uint16_t do_choose = 0;

        robot.SetTPDParam(type, name, period_ms, di_choose, do_choose);

        robot.Mode(1);
        sleep(1);
        robot.DragTeachSwitch(1);
        robot.SetTPDStart(type, name, period_ms, di_choose, do_choose);
        sleep(30);
        robot.SetWebTPDStop();
        robot.DragTeachSwitch(0);

        //robot.SetTPDDelete(name);

        return 0;
    }

TPD軌跡預載
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD軌跡預載
    * @param  [in] name  軌跡檔名
    * @return  錯誤碼
    */      
    errno_t  LoadTPD(char name[30]);

TPD軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  TPD軌跡復現
    * @param  [in] name  軌跡檔名
    * @param  [in] blend 0-不平滑，1-平滑
    * @param  [in] ovl  速度縮放百分比，範圍[0~100]
    * @return  錯誤碼
    */
    errno_t  MoveTPD(char name[30], uint8_t blend, float ovl);

獲取TPD起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TPD起始位姿
     * @param  [in] name TPD文件名,不需要文件後綴
     * @return  錯誤碼
     */     
    errno_t  GetTPDStartPose(char name[30], DescPose *desc_pose);

代碼範例
++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

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

        char name[30] = "tpd2023";
        int tool = 0;
        int user = 0;
        float vel = 50.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        int config = -1;
        uint8_t blend = 0;
        int retval = 0;

        DescPose desc_pose;
        memset(&desc_pose, 0, sizeof(DescPose));
        DescPose start_pose;
        memset(&start_pose, 0, sizeof(DescPose));

        desc_pose.tran.x = 358.820099;
        desc_pose.tran.y = -419.684113;
        desc_pose.tran.z = 525.055115;
        desc_pose.rpy.rx = -85.994499;
        desc_pose.rpy.ry = -28.797600;
        desc_pose.rpy.rz = -133.960007;

        retval = robot.LoadTPD(name);
        printf("LoadTPD retval is: %d\n", retval);
        //robot.MoveCart(&desc_pose, tool, user, vel, acc, ovl, blendT, config);
        
        robot.GetTPDStartPose(name, &start_pose);
        printf("start pose, xyz is: %f %f %f. rpy is: %f %f %f \n", start_pose.tran.x, start_pose.tran.y, start_pose.tran.z, start_pose.rpy.rx, start_pose.rpy.ry, start_pose.rpy.rz);
        std::this_thread::sleep_for(std::chrono::milliseconds(5000));
        
        retval = robot.MoveTPD(name, blend, ovl);
        printf("MoveTPD retval is: %d\n", retval);
        std::this_thread::sleep_for(std::chrono::milliseconds(5000));
        return 0;
    }

軌跡預處理
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  軌跡預處理
     * @param  [in] name  軌跡檔名
     * @param  [in] ovl 速度縮放百分比，範圍[0~100]
     * @param  [in] opt 1-控制點，預設為1
     * @return  錯誤碼
     */     
    errno_t  LoadTrajectoryJ(char name[30], float ovl, int opt);

軌跡復現
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  軌跡復現
     * @return  錯誤碼
     */     
    errno_t  MoveTrajectoryJ();

取得軌跡起始位姿
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得軌跡起始位姿
     * @param  [in] name 軌跡檔名
     * @return  錯誤碼
     */     
    errno_t  GetTrajectoryStartPose(char name[30], DescPose *desc_pose);

取得軌跡點編號
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得軌跡點編號
     * @return  錯誤碼
     */     
    errno_t  GetTrajectoryPointNum(int *pnum);

設定軌跡運行中的速度
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運行中的速度
     * @param  [in] ovl 速度百分比
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJSpeed(float ovl);

設定軌跡运行中的力和扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡运行中的力和扭矩
     * @param  [in] ft 三個方向的力和扭矩，單位N和Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceTorque(ForceTorque *ft);

設定軌跡運行中的沿x方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運行中的沿x方向的力
     * @param  [in] fx 沿x方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFx(double fx);

設定軌跡運行中的沿y方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運行中的沿y方向的力
     * @param  [in] fy 沿y方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFy(double fy);

設定軌跡運行中的沿z方向的力
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運行中的沿z方向的力
     * @param  [in] fz 沿x方向的力，單位N
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJForceFz(double fz);

設定軌跡運轉中的繞x軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運轉中的繞x軸的扭矩
     * @param  [in] tx 繞x軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTx(double tx);

設定軌跡運轉中的繞y軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運轉中的繞y軸的扭矩
     * @param  [in] ty 繞y軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTy(double ty);

設定軌跡運轉中的繞z軸的扭矩
++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定軌跡運轉中的繞z軸的扭矩
     * @param  [in] tz 繞z軸的扭矩，單位Nm
     * @return  錯誤碼
     */     
    errno_t  SetTrajectoryJTorqueTz(double tz);

代碼範例
++++++++++++++++++
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

        int retval = 0;
        char traj_file_name[30] = "/fruser/traj/tra我.txt";
        retval = robot.LoadTrajectoryJ(traj_file_name, 100, 1);
        printf("LoadTrajectoryJ %s, retval is: %d\n",traj_file_name, retval);

        DescPose traj_start_pose;
        memset(&traj_start_pose, 0, sizeof(DescPose));
        retval = robot.GetTrajectoryStartPose(traj_file_name, &traj_start_pose);
        printf("GetTrajectoryStartPose is: %d\n", retval);
        printf("desc_pos:%f,%f,%f,%f,%f,%f\n",traj_start_pose.tran.x,traj_start_pose.tran.y,traj_start_pose.tran.z,	traj_start_pose.rpy.rx,traj_start_pose.rpy.ry,traj_start_pose.rpy.rz);

        std::this_thread::sleep_for(std::chrono::seconds(5));

        robot.SetSpeed(50);
        robot.MoveCart(&traj_start_pose, 0, 0, 100, 100, 100, -1, -1);

        int traj_num = 0;
        retval = robot.GetTrajectoryPointNum(&traj_num);
        printf("GetTrajectoryStartPose retval is: %d, traj num is: %d\n", retval, traj_num);

        retval = robot.SetTrajectoryJSpeed(50.0);
        printf("SetTrajectoryJSpeed is: %d\n", retval);

        ForceTorque traj_force;
        memset(&traj_force, 0, sizeof(ForceTorque));
        traj_force.fx = 10;
        retval = robot.SetTrajectoryJForceTorque(&traj_force);
        printf("SetTrajectoryJForceTorque retval is: %d\n", retval);

        retval = robot.SetTrajectoryJForceFx(10.0);
        printf("SetTrajectoryJForceFx retval is: %d\n", retval);

        retval = robot.SetTrajectoryJForceFy(0.0);
        printf("SetTrajectoryJForceFy retval is: %d\n", retval);

        retval = robot.SetTrajectoryJForceFz(0.0);
        printf("SetTrajectoryJForceFz retval is: %d\n", retval);

        retval = robot.SetTrajectoryJTorqueTx(10.0);
        printf("SetTrajectoryJTorqueTx retval is: %d\n", retval);

        retval = robot.SetTrajectoryJTorqueTy(10.0);
        printf("SetTrajectoryJTorqueTy retval is: %d\n", retval);

        retval = robot.SetTrajectoryJTorqueTz(10.0);
        printf("SetTrajectoryJTorqueTz retval is: %d\n", retval);

        retval = robot.MoveTrajectoryJ();
        printf("MoveTrajectoryJ retval is: %d\n", retval);
    }

上傳軌跡J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 上傳軌跡J文件
	 * @param [in] filePath 上傳軌跡檔案的全路徑名   C://test/testJ.txt
	 * @return 錯誤碼
	 */
	errno_t TrajectoryJUpLoad(const std::string& filePath);

刪除軌跡J文件
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	 * @brief 刪除軌跡J文件
	 * @param [in] fileName 文件名稱 testJ.txt
	 * @return 錯誤碼
	 */
	errno_t TrajectoryJDelete(const std::string& fileName);

代碼範例
******************
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    void TrajectoryJUpload(FRRobot* robot)
    {
        int rtn = -1;
        rtn = robot->TrajectoryJUpLoad("D://zUP/testA.txt");
        printf("Upload TrajectoryJ A %d\n", rtn);
        rtn = robot->TrajectoryJUpLoad("D://zUP/testB.txt");
        printf("Upload TrajectoryJ B %d\n", rtn);

        rtn = robot->TrajectoryJDelete("testA.txt");
        printf("Delete TrajectoryJ A %d\n", rtn);
        rtn = robot->TrajectoryJDelete("testB.txt");
        printf("Delete TrajectoryJ B %d\n", rtn);
    }