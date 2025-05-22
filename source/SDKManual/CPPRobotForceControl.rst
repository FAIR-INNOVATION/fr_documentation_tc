機器人力控
============

.. toctree:: 
    :maxdepth: 5

力感測器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
	 * @brief  配置力感測器
	 * @param  [in] company  力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI传感器，21-中科米點，22-伟航敏芯，23-NBIT，24-鑫精诚(XJC)，26-NSR
	 * @param  [in] device  設備號，坤維(0-KWR75B)，航太十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0 -WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精誠XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)
	 * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
	 * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
	 * @return  錯誤碼
	 */
    errno_t FT_SetConfig(int company, int device, int softvesion, int bus);

取得力傳感器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得力傳感器配置
    * @param  [in] company  力传感器廠商，待定
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    errno_t  FT_GetConfig(int *company, int *device, int *softvesion, int *bus);

力傳感器激活
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力傳感器激活
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    errno_t  FT_Activate(uint8_t act);

力傳感器校零
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力傳感器校零
    * @param  [in] act  0-去除零點，1-零點矯正
    * @return  錯誤碼
    */
    errno_t  FT_SetZero(uint8_t act);   

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

        int company = 17;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        int act = 0;

        robot.FT_SetConfig(company, device, softversion, bus);
        sleep(1);
        robot.FT_GetConfig(&company, &device, &softversion, &bus);
        printf("FT config:%d,%d,%d,%d\n", company, device, softversion, bus);
        sleep(1);

        robot.FT_Activate(act);
        sleep(1);
        act = 1;
        robot.FT_Activate(act);
        sleep(1);

        robot.SetLoadWeight(0.0);
        sleep(1);
        DescTran coord;
        memset(&coord, 0, sizeof(DescTran));
        robot.SetLoadCoord(&coord);
        sleep(1);
        robot.FT_SetZero(0);
        sleep(1);

        ForceTorque ft;
        memset(&ft, 0, sizeof(ForceTorque));
        robot.FT_GetForceTorqueOrigin(&ft);
        printf("ft origin:%f,%f,%f,%f,%f,%f\n", ft.fx,ft.fy,ft.fz,ft.tx,ft.ty,ft.tz);
        robot.FT_SetZero(1);
        sleep(1);
        memset(&ft, 0, sizeof(ForceTorque));
        printf("ft rcs:%f,%f,%f,%f,%f,%f\n",ft.fx,ft.fy,ft.fz,ft.tx,ft.ty,ft.tz);

        return 0;
    }

設定力道感測器參考座標系
+++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定力道感測器參考座標系
    * @param  [in] ref  0-工具座標系，1-基坐標系
    * @return  錯誤碼
    */
    errno_t  FT_SetRCS(uint8_t ref); 

負載重量辨識記錄
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載重量辨識記錄
    * @param  [in] id  传感器座標系編號，範圍[1~14]
    * @return  錯誤碼
    */
    errno_t  FT_PdIdenRecord(int id);   

負載重量辨識計算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載重量辨識計算
    * @param  [out] weight  負載重量，單位kg
    * @return  錯誤碼
    */   
    errno_t  FT_PdIdenCompute(float *weight);

負載質心辨識記錄
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載質心辨識記錄
    * @param  [in] id  传感器座標系編號，範圍[1~14]
    * @param  [in] index 點編號，範圍[1~3]
    * @return  錯誤碼
    */
    errno_t  FT_PdCogIdenRecord(int id, int index);    

負載質心辨識計算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  負載質心辨識計算
    * @param  [out] cog  負載質心，單位mm
    * @return  錯誤碼
    */   
    errno_t  FT_PdCogIdenCompute(DescTran *cog); 

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

        float weight;

        DescPose tcoord, desc_p1, desc_p2, desc_p3;
        memset(&tcoord, 0, sizeof(DescPose));
        memset(&desc_p1, 0, sizeof(DescPose));
        memset(&desc_p2, 0, sizeof(DescPose));
        memset(&desc_p3, 0, sizeof(DescPose));

        robot.FT_SetRCS(0);
        sleep(1);

        tcoord.tran.z = 35.0;
        robot.SetToolCoord(10, &tcoord, 1, 0);
        sleep(1);
        robot.FT_PdIdenRecord(10);
        sleep(1);
        robot.FT_PdIdenCompute(&weight);
        printf("payload weight:%f\n", weight);

        desc_p1.tran.x = -160.619;
        desc_p1.tran.y = -586.138;
        desc_p1.tran.z = 384.988;
        desc_p1.rpy.rx = -170.166;
        desc_p1.rpy.ry = -44.782;
        desc_p1.rpy.rz = 169.295;

        desc_p2.tran.x = -87.615;
        desc_p2.tran.y = -606.209;
        desc_p2.tran.z = 556.119;
        desc_p2.rpy.rx = -102.495;
        desc_p2.rpy.ry = 10.118;
        desc_p2.rpy.rz = 178.985;

        desc_p3.tran.x = 41.479;
        desc_p3.tran.y = -557.243;
        desc_p3.tran.z = 484.407;
        desc_p3.rpy.rx = -125.174;
        desc_p3.rpy.ry = 46.995;
        desc_p3.rpy.rz = -132.165;

        robot.MoveCart(&desc_p1, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
        sleep(1);
        robot.FT_PdCogIdenRecord(10, 1);
        robot.MoveCart(&desc_p2, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
        sleep(1);
        robot.FT_PdCogIdenRecord(10, 2);
        robot.MoveCart(&desc_p3, 9, 0, 100.0, 100.0, 100.0, -1.0, -1);
        sleep(1);
        robot.FT_PdCogIdenRecord(10, 3);
        sleep(1);
        DescTran cog;
        memset(&cog, 0, sizeof(DescTran));
        robot.FT_PdCogIdenCompute(&cog);
        printf("cog:%f,%f,%f\n",cog.x, cog.y, cog.z);

        return 0;
    }

取得參考坐標系下力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得參考坐標系下力/扭力數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    errno_t  FT_GetForceTorqueRCS(ForceTorque *ft); 

取得力感測器原始力/扭力數據
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得力感測器原始力/扭力數據
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  錯誤碼
    */   
    errno_t  FT_GetForceTorqueOrigin(ForceTorque *ft); 

碰撞守護
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  碰撞守護
    * @param  [in] flag 0-關閉碰撞守護，1-開啟碰撞守護
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否偵測碰撞，0-不偵測，1-偵測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大閾值
    * @param  [in] min_threshold 最小閾值
    * @note   力/扭力檢測範圍：(ft-min_threshold, ft+max_threshold)
    * @return  錯誤碼
    */   
    errno_t  FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]); 

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

        uint8_t flag = 1;
        uint8_t sensor_id = 1;
        uint8_t select[6] = {1,1,1,1,1,1};
        float max_threshold[6] = {10.0,10.0,10.0,10.0,10.0,10.0};
        float min_threshold[6] = {5.0,5.0,5.0,5.0,5.0,5.0};

        ForceTorque ft;
        DescPose desc_p1, desc_p2, desc_p3;
        memset(&ft, 0, sizeof(ForceTorque));
        memset(&desc_p1, 0, sizeof(DescPose));
        memset(&desc_p2, 0, sizeof(DescPose));
        memset(&desc_p3, 0, sizeof(DescPose));

        desc_p1.tran.x = -160.619;
        desc_p1.tran.y = -586.138;
        desc_p1.tran.z = 384.988;
        desc_p1.rpy.rx = -170.166;
        desc_p1.rpy.ry = -44.782;
        desc_p1.rpy.rz = 169.295;

        desc_p2.tran.x = -87.615;
        desc_p2.tran.y = -606.209;
        desc_p2.tran.z = 556.119;
        desc_p2.rpy.rx = -102.495;
        desc_p2.rpy.ry = 10.118;
        desc_p2.rpy.rz = 178.985;

        desc_p3.tran.x = 41.479;
        desc_p3.tran.y = -557.243;
        desc_p3.tran.z = 484.407;
        desc_p3.rpy.rx = -125.174;
        desc_p3.rpy.ry = 46.995;
        desc_p3.rpy.rz = -132.165;

        robot.FT_Guard(flag, sensor_id, select, &ft, max_threshold, min_threshold);
        robot.MoveCart(&desc_p1,9,0,100.0,100.0,100.0,-1.0,-1);
        robot.MoveCart(&desc_p2,9,0,100.0,100.0,100.0,-1.0,-1);
        robot.MoveCart(&desc_p3,9,0,100.0,100.0,100.0,-1.0,-1);
        flag = 0;
        robot.FT_Guard(flag, sensor_id, select, &ft, max_threshold, min_threshold);

        return 0;
    }

恆力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  恆力控制
    * @param  [in] flag 0-關閉恆力控制，1-開啟恆力控制
    * @param  [in] sensor_id 力傳感器編號
    * @param  [in] select  選擇六個自由度是否偵測碰撞，0-不偵測，1-偵測
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid參數，力矩pid參數
    * @param  [in] adj_sign 自適應啟動停止控制，0-關閉，1-開啟
    * @param  [in] ILC_sign ILC啟停控制， 0-停止，1-訓練，2-實操
    * @param  [in] 最大調整距離，單位mm
    * @param  [in] 最大調整角度，單位deg
    * @return  錯誤碼
    */   
    errno_t  FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float ft_pid[6], uint8_t adj_sign, uint8_t ILC_sign, float max_dis, float max_ang);   

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

        uint8_t flag = 1;
        uint8_t sensor_id = 1;
        uint8_t select[6] = {0,0,1,0,0,0};
        float ft_pid[6] = {0.0005,0.0,0.0,0.0,0.0,0.0};
        uint8_t adj_sign = 0;
        uint8_t ILC_sign = 0;
        float max_dis = 100.0;
        float max_ang = 0.0;

        ForceTorque ft;
        DescPose desc_p1, desc_p2, offset_pos;
        JointPos j1,j2;
        ExaxisPos epos;
        memset(&ft, 0, sizeof(ForceTorque));
        memset(&desc_p1, 0, sizeof(DescPose));
        memset(&desc_p2, 0, sizeof(DescPose));
        memset(&offset_pos, 0, sizeof(DescPose));
        memset(&epos, 0, sizeof(ExaxisPos));
        memset(&j1, 0, sizeof(JointPos));
        memset(&j2, 0, sizeof(JointPos));

        j1 = {-68.987,-96.414,-111.45,-61.105,92.884,11.089};
        j2 = {-107.596,-109.154,-104.735,-56.176,90.739,11.091};

        desc_p1.tran.x = 62.795;
        desc_p1.tran.y = -511.979;
        desc_p1.tran.z = 291.697;
        desc_p1.rpy.rx = -179.545;
        desc_p1.rpy.ry = 3.027;
        desc_p1.rpy.rz = -170.039;

        desc_p2.tran.x = -294.768;
        desc_p2.tran.y = -503.708;
        desc_p2.tran.z = 233.158;
        desc_p2.rpy.rx = 179.799;
        desc_p2.rpy.ry = 0.713;
        desc_p2.rpy.rz = 151.309;

        ft.fz = -10.0;

        robot.MoveJ(&j1,&desc_p1,9,0,100.0,180.0,100.0,&epos,-1.0,0,&offset_pos);
        robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);
        robot.MoveL(&j2,&desc_p2,9,0,100.0,180.0,20.0,-1.0,&epos,0,0,&offset_pos);
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);

        return 0;
    }

螺旋線探索
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  螺旋線探索
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基坐標系
    * @param  [in] dr 每圈半徑進給量
    * @param  [in] ft 力/扭力閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] max_t_ms 最大探索時間，單位ms
    * @param  [in] max_vel 最大線速度，單位mm/s
    * @return  錯誤碼
    */   
    errno_t  FT_SpiralSearch(int rcs, float dr, float ft, float max_t_ms, float max_vel);  

旋轉插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  旋轉插入
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基坐標系
    * @param  [in] angVelRot 旋轉角速度，單位deg/s
    * @param  [in] ft  力/扭力閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] max_angle 最大旋轉角度，單位deg
    * @param  [in] orn 力/扭力方向，1-沿z軸方向，2-繞z軸方向
    * @param  [in] max_angAcc 最大旋轉加速度，單位deg/s^2，暫不使用，預設為0
    * @param  [in] rotorn  旋轉方向，1-順時針，2-逆時針
    * @return  錯誤碼
    */   
    errno_t  FT_RotInsertion(int rcs, float angVelRot, float ft, float max_angle, uint8_t orn, float max_angAcc, uint8_t rotorn);    

直線插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  直線插入
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基坐標系
    * @param  [in] ft  力/扭力閾值，fx,fy,fz,tx,ty,tz，範圍[0~100]
    * @param  [in] lin_v 直線速度，單位mm/s
    * @param  [in] lin_a 直線加速度，單位mm/s^2，暫不使用
    * @param  [in] max_dis 最大插入距離，單位mm
    * @param  [in] linorn  插入方向，0-負方向，1-正方向
    * @return  錯誤碼
    */   
    errno_t  FT_LinInsertion(int rcs, float ft, float lin_v, float lin_a, float max_dis, uint8_t linorn);    

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

        //恒力參數
        uint8_t status = 1;  //恆力控制開啟标志，0-關，1-開
        int sensor_num = 1; //力傳感器編號
        float gain[6] = {0.0001,0.0,0.0,0.0,0.0,0.0};  //最大閾值
        uint8_t adj_sign = 0;  //自適應啟動停止狀態，0-關閉，1-開啟
        uint8_t ILC_sign = 0;  //ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
        float max_dis = 100.0;  //最大調整距離
        float max_ang = 5.0;  //最大調整角度

        ForceTorque ft;
        memset(&ft, 0, sizeof(ForceTorque));

        //螺旋線探索參數
        int rcs = 0;  //參考座標系，0-工具座標系，1-基坐標系
        float dr = 0.7;  //每圈半徑進給量，單位mm
        float fFinish = 1.0; //力或力矩閾值（0~100），單位N或Nm
        float t = 60000.0; //最大探索時間，單位ms
        float vmax = 3.0; //線速度最大值，單位mm/s

        //直線插入參數
        float force_goal = 20.0;  //力或力矩閾值（0~100），單位N或Nm
        float lin_v = 0.0; //直線速度，單位mm/s
        float lin_a = 0.0; //直線加速度，單位mm/s^2,暫不使用
        float disMax = 100.0; //最大插入距離，單位mm
        uint8_t linorn = 1; //插入方向，1-正方向，2-負方向

        //旋轉插入參數
        float angVelRot = 2.0;  //旋轉角速度，單位°/s
        float forceInsertion = 1.0; //力或力矩閾值（0~100），單位N或Nm
        int angleMax= 45; //最大旋轉角度，單位°
        uint8_t orn = 1; //力的方向，1-fz,2-mz
        float angAccmax = 0.0; //最大旋轉角加速度，單位°/s^2,暫不使用
        uint8_t rotorn = 1; //旋轉方向，1-順時針，2-逆時針

        uint8_t select1[6] = {0,0,1,1,1,0}; //六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        ft.fz = -10.0;
        robot.FT_Control(status,sensor_num,select1,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_SpiralSearch(rcs,dr,fFinish,t,vmax);
        status = 0;
        robot.FT_Control(status,sensor_num,select1,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select2[6] = {1,1,1,0,0,0};  //六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        gain[0] = 0.00005;
        ft.fz = -30.0;
        status = 1;
        robot.FT_Control(status,sensor_num,select2,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_LinInsertion(rcs,force_goal,lin_v,lin_a,disMax,linorn);
        status = 0;
        robot.FT_Control(status,sensor_num,select2,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select3[6] = {0,0,1,1,1,0};  //六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        ft.fz = -10.0;
        gain[0] = 0.0001;
        status = 1;
        robot.FT_Control(status,sensor_num,select3,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_RotInsertion(rcs,angVelRot,forceInsertion,angleMax,orn,angAccmax,rotorn);
        status = 0;
        robot.FT_Control(status,sensor_num,select3,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select4[6] = {1,1,1,0,0,0};  //六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        ft.fz = -30.0;
        status = 1;
        robot.FT_Control(status,sensor_num,select4,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_LinInsertion(rcs,force_goal,lin_v,lin_a,disMax,linorn);
        status = 0;
        robot.FT_Control(status,sensor_num,select4,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        return 0;
    }

表面定位
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  表面定位
    * @param  [in] rcs 參考座標系，0-工具座標系，1-基坐標系
    * @param  [in] dir  移動方向，1-正方向，2-負方向 
    * @param  [in] axis 移動軸，1-x軸，2-y軸，3-z軸
    * @param  [in] lin_v 探索直線速度，單位mm/s
    * @param  [in] lin_a 探索直線加速度，單位mm/s^2，暫不使用，默認為0
    * @param  [in] max_dis 最大探索距離，單位mm
    * @param  [in] ft  動作终止力/扭力閾值，fx,fy,fz,tx,ty,tz  
    * @return  錯誤碼
    */   
    errno_t  FT_FindSurface(int rcs, uint8_t dir, uint8_t axis, float lin_v, float lin_a, float max_dis, float ft);   

計算中間平面位置開始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  計算中間平面位置開始
    * @return  錯誤碼
    */   
    errno_t  FT_CalCenterStart();

計算中間平面位置結束
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  計算中間平面位置結束
    * @param  [out] pos 中間平面位姿
    * @return  錯誤碼
    */      
    errno_t  FT_CalCenterEnd(DescPose *pos);

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

        int rcs = 0;
        uint8_t dir = 1;
        uint8_t axis = 1;
        float lin_v = 3.0;
        float lin_a = 0.0;
        float maxdis = 50.0;
        float ft_goal = 2.0;

        DescPose desc_pos, xcenter, ycenter;
        ForceTorque ft;
        memset(&desc_pos, 0, sizeof(DescPose));
        memset(&xcenter, 0, sizeof(DescPose));
        memset(&ycenter, 0, sizeof(DescPose));
        memset(&ft, 0, sizeof(ForceTorque));

        desc_pos.tran.x = -230.959;
        desc_pos.tran.y = -364.017;
        desc_pos.tran.z = 217.5;
        desc_pos.rpy.rx = -179.004;
        desc_pos.rpy.ry = 0.002;
        desc_pos.rpy.rz = 89.999;

        ft.fx = -2.0;

        robot.MoveCart(&desc_pos, 9,0,100.0,100.0,100.0,-1.0,-1);

        robot.FT_CalCenterStart();
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.MoveCart(&desc_pos, 9,0,100.0,100.0,100.0,-1.0,-1);
        robot.WaitMs(1000);

        dir = 2;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.FT_CalCenterEnd(&xcenter);
        printf("xcenter:%f,%f,%f,%f,%f,%f\n",xcenter.tran.x,xcenter.tran.y,xcenter.tran.z,xcenter.rpy.rx,xcenter.rpy.ry,xcenter.rpy.rz);
        robot.MoveCart(&xcenter, 9,0,60.0,50.0,50.0,-1.0,-1);

        robot.FT_CalCenterStart();
        dir = 1;
        axis = 2;
        lin_v = 6.0;
        maxdis = 150.0;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);
        robot.MoveCart(&desc_pos, 9,0,100.0,100.0,100.0,-1.0,-1);
        robot.WaitMs(1000);

        dir = 2;
        robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal);  
        robot.FT_CalCenterEnd(&ycenter);
        printf("ycenter:%f,%f,%f,%f,%f,%f\n",ycenter.tran.x,ycenter.tran.y,ycenter.tran.z,ycenter.rpy.rx,ycenter.rpy.ry,ycenter.rpy.rz);
        robot.MoveCart(&ycenter, 9,0,60.0,50.0,50.0,0.0,-1);   

        return 0;
    }

柔順控制開啟
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔順控制開啟
    * @param  [in] p 位置調節係數或柔順係數
    * @param  [in] force 柔順開啟力閾值，單位N
    * @return  錯誤碼
    */   
    errno_t  FT_ComplianceStart(float p, float force); 

柔順控制關閉
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔順控制關閉
    * @return  錯誤碼
    */   
    errno_t  FT_ComplianceStop(); 

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 負載辨識初始化
     * @return 錯誤碼
     */
    errno_t LoadIdentifyDynFilterInit();

負載辨識初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 負載辨識初始化
     * @return 錯誤碼
     */
    errno_t LoadIdentifyDynVarInit();

負荷辨識主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 負荷辨識主程序
     * @param [in] joint_torque 關節扭矩
     * @param [in] joint_pos 關節位置
     * @param [in] t 採樣週期
     * @return 錯誤碼
     */
    errno_t LoadIdentifyMain(double joint_torque[6], double joint_pos[6], double t);

獲取負荷辨識結果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 獲取負荷辨識結果
     * @param [in] gain  
     * @param [out] weight 負載重量
     * @param [out] cog 負載質心
     * @return 錯誤碼
     */
    errno_t LoadIdentifyGetResult(double gain[12], double *weight, DescTran *cog);

傳動皮帶啟動、停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 傳動皮帶啟動、停止
     * @param [in] status 狀態，1-啟動，0-停止 
     * @return 錯誤碼
     */
    errno_t ConveyorStartEnd(uint8_t status);

記錄IO檢測點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 記錄IO檢測點
     * @return 錯誤碼
     */
    errno_t ConveyorPointIORecord();

記錄A點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 記錄A點
     * @return 錯誤碼
     */
    errno_t ConveyorPointARecord();

記錄參考點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 記錄參考點
     * @return 錯誤碼
     */
    errno_t ConveyorRefPointRecord();

記錄B點
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 記錄B點
     * @return 錯誤碼
     */
    errno_t ConveyorPointBRecord();

傳送帶工件IO檢測
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 傳送帶工件IO檢測
     * @param [in] max_t 最大檢測時間，單位ms
     * @return 錯誤碼
     */
    errno_t ConveyorIODetect(int max_t);

取得物體目前位置
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得物體目前位置
     * @param [in] mode 
     * @return 錯誤碼
     */
    errno_t ConveyorGetTrackData(int mode);

傳動皮帶追蹤開始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 傳動皮帶追蹤開始
     * @param [in] status 狀態，1-啟動，0-停止 
     * @return 錯誤碼
     */
    errno_t ConveyorTrackStart(uint8_t status);

傳動皮帶追蹤停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 傳動皮帶追蹤停止
     * @return 錯誤碼
     */
    errno_t ConveyorTrackEnd();

傳送帶參數配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶參數配置
    * @param [in] para[0] 編碼器通道 1~2
    * @param [in] para[1] 編碼器轉一圈的脈衝數
    * @param [in] para[2] 編碼器轉一圈傳送帶行走距離
    * @param [in] para[3] 工件坐標系編號 針對跟蹤運動功能選擇工件坐標系編號，跟蹤抓取、TPD跟蹤設為0
    * @param [in] para[4] 是否配視覺 0 不配 1 配
    * @param [in] para[5] 速度比 針對傳送帶跟蹤抓取選項（1-100） 其他選項默認為1 
    * @param [in] followType 跟蹤運動類型，0-跟蹤運動；1-追檢運動
    * @param [in] startDis 追檢抓取需要設置， 跟蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 默認值0
    * @param [in] endDis 追檢抓取需要設置，跟蹤終止距離， 單位mm， 默認值100
    * @return 錯誤碼
    */
    errno_t ConveyorSetParam(float para[6], int followType = 0, int startDis = 0, int endDis = 100);

傳動帶抓取點補償
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief 傳動帶抓取點補償
	 * @param [in] cmp 補償位置 double[3]{x, y, z}
	 * @return 錯誤碼
	 */
    errno_t ConveyorCatchPointComp(double cmp[3]);

直線運動
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 直線運動
     * @param [in] status 狀態，1-啟動，0-停止 
     * @return 錯誤碼
     */
    errno_t TrackMoveL(char name[32], int tool, int wobj, float vel, float acc, float ovl, float blendR, uint8_t flag, uint8_t type);

取得SSH公鑰
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得SSH公鑰
     * @param [out] keygen 公鑰
     * @return 錯誤碼
     */
    errno_t GetSSHKeygen(char keygen[1024]);

下發SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 下發SCP指令
     * @param [in] mode 0-上傳（上位機->控制器），1-下載（控制器->上位機）
     * @param [in] sshname 上位機用戶名
     * @param [in] sship 上位機ip位址
     * @param [in] usr_file_url 上位機檔案路徑
     * @param [in] robot_file_url 機器人控制器檔案路徑
     * @return 錯誤碼
     */
    errno_t SetSSHScpCmd(int mode, char sshname[32], char sship[32], char usr_file_url[128], char robot_file_url[128]);

計算指定路徑下檔案的MD5值
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 計算指定路徑下檔案的MD5值
     * @param [in] file_path 檔案路徑包含檔名，預設Traj資料夾路徑為:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
     * @param [out] md5 文件MD5值
     * @return 錯誤碼
     */
    errno_t ComputeFileMD5(char file_path[256], char md5[256]);

取得機器人急停狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得機器人急停狀態
     * @param [out] state 急停狀態，0-非急停，1-急停
     * @return 錯誤碼  
     */
    errno_t GetRobotEmergencyStopState(uint8_t *state);

取得SDK與機器人的通訊狀態
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得SDK與機器人的通訊狀態
     * @param [out]  state 通訊狀態，0-通訊正常，1-通訊異常
     */
    errno_t GetSDKComState(int *state);

取得安全停止訊號
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得安全停止訊號
     * @param [out]  si0_state 安全停止訊號SI0，0-無效，1-有效
     * @param [out]  si1_state 安全停止訊號SI1，0-無效，1-有效
     */
    errno_t GetSafetyStopState(uint8_t *si0_state, uint8_t *si1_state);

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

        uint8_t flag = 1;
        int sensor_id = 1;
        uint8_t select[6] = {1,1,1,0,0,0};
        float ft_pid[6] = {0.0005,0.0,0.0,0.0,0.0,0.0};
        uint8_t adj_sign = 0;
        uint8_t ILC_sign = 0;
        float max_dis = 100.0;
        float max_ang = 0.0;

        ForceTorque ft;
        DescPose desc_p1, desc_p2, offset_pos;
        ExaxisPos epos;
        JointPos j1, j2;
        memset(&ft, 0, sizeof(ForceTorque));
        memset(&desc_p1, 0, sizeof(DescPose));
        memset(&desc_p2, 0, sizeof(DescPose));
        memset(&offset_pos, 0, sizeof(DescPose));
        memset(&j1, 0, sizeof(JointPos));
        memset(&j2, 0, sizeof(JointPos));
        memset(&epos, 0, sizeof(ExaxisPos));

        j1 = {-105.3,-68.0,-127.9,-75.5,90.8,77.8};
        j2 = {-105.3,-97.9,-101.5,-70.3,90.8,77.8};

        desc_p1.tran.x = -208.9;
        desc_p1.tran.y = -274.5;
        desc_p1.tran.z = 334.6;
        desc_p1.rpy.rx = 178.8;
        desc_p1.rpy.ry = -1.3;
        desc_p1.rpy.rz = 86.7;

        desc_p2.tran.x = -264.8;
        desc_p2.tran.y = -480.5;
        desc_p2.tran.z = 341.8;
        desc_p2.rpy.rx = 179.2;
        desc_p2.rpy.ry = 0.3;
        desc_p2.rpy.rz = 86.7;

        ft.fx = -10.0;
        ft.fy = -10.0;
        ft.fz = -10.0;
        robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);  
        float p = 0.00005;
        float force = 30.0; 
        robot.FT_ComplianceStart(p, force); 
        int count = 15;
        while (count)
        {
            robot.MoveL(&j1,&desc_p1,9,0,100.0,180.0,100.0,-1.0,&epos,0,1,&offset_pos);
            robot.MoveL(&j2,&desc_p2,9,0,100.0,180.0,100.0,-1.0,&epos,0,0,&offset_pos);
            count -= 1;
        }
        robot.FT_ComplianceStop();
        flag = 0;
        robot.FT_Control(flag, sensor_id, select, &ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang);

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

        int retval = 0;

        retval = robot.LoadIdentifyDynFilterInit();
        printf("LoadIdentifyDynFilterInit retval is: %d \n", retval);

        retval = robot.LoadIdentifyDynVarInit();
        printf("LoadIdentifyDynVarInit retval is: %d \n", retval);

        double joint_toq[6] = {0};
        double joint_pos[6] = {0};
        retval = robot.LoadIdentifyMain(joint_toq, joint_pos,1);
        printf("LoadIdentifyMain retval is: %d \n", retval);

        double gain[12] = {0};
        double weight = 0;
        DescTran load_pos;
        memset(&load_pos, 0, sizeof(DescTran));
        retval = robot.LoadIdentifyGetResult(gain, &weight, &load_pos);
        printf("LoadIdentifyGetResult retval is: %d \n", retval);
        printf("weight is: %f, load pose is: %f, %f, %f\n", weight, load_pos.x, load_pos.y, load_pos.z);

        retval = robot.WaitMs(10);
        printf("WaitMs retval is: %d \n", retval);
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

        int retval = 0;

        retval = robot.ConveyorStartEnd(1);
        printf("ConveyorStartEnd retval is: %d\n", retval);

        retval = robot.ConveyorPointIORecord();
        printf("ConveyorPointIORecord retval is: %d\n", retval);

        retval = robot.ConveyorPointARecord();
        printf("ConveyorPointARecord retval is: %d\n", retval);

        retval = robot.ConveyorRefPointRecord();
        printf("ConveyorRefPointRecord retval is: %d\n", retval);

        retval = robot.ConveyorPointBRecord();
        printf("ConveyorPointBRecord retval is: %d\n", retval);

        retval = robot.ConveyorStartEnd(0);
        printf("ConveyorStartEnd retval is: %d\n", retval);
        
        retval = 0;
        float param[6] ={1,10000,200,0,0,20};
        retval = robot.ConveyorSetParam(param);
        printf("ConveyorSetParam retval is: %d\n", retval);
        
        double cmp[3] = {0.0, 0.0, 0.0};
        retval = robot.ConveyorCatchPointComp(cmp);
        printf("ConveyorCatchPointComp retval is: %d\n", retval);

        int index = 1;
        int max_time = 30000;
        uint8_t block = 0;
        retval = 0;
        
        /* 下面是一個传送带抓取流程 */
        DescPose desc_p1;
        desc_p1.tran.x = -351.553;
        desc_p1.tran.y = 87.913;
        desc_p1.tran.z = 354.175;
        desc_p1.rpy.rx = -179.680;
        desc_p1.rpy.ry =  -0.133;
        desc_p1.rpy.rz = 2.472;

        DescPose desc_p2;
        desc_p2.tran.x = -351.535;
        desc_p2.tran.y = -247.222;
        desc_p2.tran.z = 354.173;
        desc_p2.rpy.rx = -179.680;
        desc_p2.rpy.ry =  -0.137;
        desc_p2.rpy.rz = 2.473;


        retval = robot.MoveCart(&desc_p1, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);
        printf("MoveCart retval is: %d\n", retval);

        retval = robot.WaitMs(1);
        printf("WaitMs retval is: %d\n", retval);

        retval = robot.ConveyorIODetect(10000);
        printf("ConveyorIODetect retval is: %d\n", retval);

        retval = robot.ConveyorGetTrackData(1);
        printf("ConveyorGetTrackData retval is: %d\n", retval);

        retval = robot.ConveyorTrackStart(1);
        printf("ConveyorTrackStart retval is: %d\n", retval);

        retval = robot.TrackMoveL("cvrCatchPoint",  1, 0, 100, 100, 100, -1.0, 0, 0);
        printf("TrackMoveL retval is: %d\n", retval);

        retval = robot.MoveGripper(index, 51, 40, 30, max_time, block);
        printf("MoveGripper retval is: %d\n", retval);

        retval = robot.TrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0, 0, 0);
        printf("TrackMoveL retval is: %d\n", retval);

        retval = robot.ConveyorTrackEnd();
        printf("ConveyorTrackEnd retval is: %d\n", retval);

        robot.MoveCart(&desc_p2, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.MoveGripper(index, 100, 40, 10, max_time, block);
        printf("MoveGripper retval is: %d\n", retval);

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

        char file_path[256] = "/fruser/traj/test_computermd5.txt.txt";
        char md5[256] = {0};
        uint8_t emerg_state = 0;
        uint8_t si0_state = 0;
        uint8_t si1_state = 0;
        int sdk_com_state = 0;

        char ssh_keygen[1024] = {0};
        int retval = robot.GetSSHKeygen(ssh_keygen);
        printf("GetSSHKeygen retval is: %d\n", retval);
        printf("ssh key is: %s \n", ssh_keygen);

        char ssh_name[32] = "fr";
        char ssh_ip[32] = "192.168.58.44";
        char ssh_route[128] = "/home/fr";
        char ssh_robot_url[128] = "/root/robot/dhpara.config";
        retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url);
        printf("SetSSHScpCmd retval is: %d\n", retval);
        printf("robot url is: %s\n", ssh_robot_url);

        robot.ComputeFileMD5(file_path, md5);
        printf("md5 is: %s \n", md5);

        robot.GetRobotEmergencyStopState(&emerg_state);
        printf("emergency state is: %u \n", emerg_state);

        robot.GetSafetyStopState(&si0_state, &si1_state);
        printf("safety stop state is: %u, %u \n", si0_state, si1_state);

        robot.GetSDKComState(&sdk_com_state);
        printf("sdk com state is: %d", sdk_com_state);
        return 0;
    }

力道感測器輔助拖曳
+++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.0-3.8.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  力道感測器輔助拖曳
      * @param  [in] status 控制狀態，0-關閉；1-開啟
      * @param  [in] asaptiveFlag 自適應開啟標誌，0-關閉；1-開啟
      * @param  [in] interfereDragFlag 干涉區拖曳標誌，0-關閉；1-開啟
      * @param  [in] singularityConstraintsFlag 奇異點策略，0-規避；1-穿越
      * @param  [in] M 慣性係數
      * @param  [in] B 阻尼係數
      * @param  [in] K 剛度係數
      * @param  [in] F 拖曳六維力閾值
      * @param  [in] Fmax 最大拖動力限制
      * @param  [in] Vmax 最大關節速度限制
      * @return  錯誤碼
      */
     errno_t EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, int ingularityConstraintsFlag, std::vector<double> M, std::vector<double> B, std::vector<double> K, std::vector<double> F, double Fmax, double Vmax);

範例程式
+++++++++++++++
.. versionchanged:: C++SDK-v2.2.0-3.8.0
    
.. code-block:: c++
    :linenos:

    int DragControl(FRRobot* robot)
    {
    vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
    vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
    vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
    vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
    robot->EndForceDragControl(1, 0, 0, M, B, K, F, 50, 100);

    robot->Sleep(5000);

    robot->EndForceDragControl(0, 0, 0, M, B, K, F, 50, 100);
    }

報錯清除後力感知器自動開啟
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  報錯清除後力感知器自動開啟
      * @param  [in] status 控制狀態，0-關閉；1-開啟
      * @return  錯誤碼
      */
     errno_t SetForceSensorDragAutoFlag(int status);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int FTAutoOn(FRRobot* robot)
    {
    robot->SetForceSensorDragAutoFlag(1);
    vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
    vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
    vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
    vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
    robot->EndForceDragControl(1, 0, 0, M, B, K, F, 50, 100);
    return 0;
    }

設定六維力和關節阻抗混合拖曳開關及參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定六維力和關節阻抗混合拖曳開關及參數
      * @param  [in] status 控制狀態，0-關閉；1-開啟
      * @param  [in] impedanceFlag 阻抗開啟標誌，0-關閉；1-開啟
      * @param  [in] lamdeDain 拖曳增益
      * @param  [in] KGain 剛度增益
      * @param  [in] BGain 阻尼增益
      * @param  [in] dragMaxTcpVel 拖曳末端最大線速度限制
      * @param  [in] dragMaxTcpOriVel 拖曳末端最大角速度限制
      * @return  錯誤碼
      */
     errno_t ForceAndJointImpedanceStartStop(int status, int impedanceFlag, std::vector<double> lamdeDain, std::vector<double> KGain, std::vector<double> BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int SixDiaDrag(FRRobot* robot)
    {
    robot->DragTeachSwitch(1);
    vector <double> lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
    vector <double> KGain = { 0, 0, 0, 0, 0, 0 };
    vector <double> BGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
    robot->ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000, 180);

    robot->Sleep(5000);

    robot->DragTeachSwitch(0);
    robot->ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000, 180);

    return 0;
    }

取得力道感測器拖曳開關狀態
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  取得力道感測器拖曳開關狀態
      * @param  [out] dragState 力道感測器輔助拖曳控制狀態，0-關閉；1-開啟
      * @param  [out] sixDimensionalDragState 六維力輔助拖曳控制狀態，0-關閉；1-開啟
      * @return  錯誤碼
      */
     errno_t GetForceAndTorqueDragState(int& dragState, int& sixDimensionalDragState);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int RobotGetFTDragState(FRRobot* robot)
    {
    int dragState = 0;
    int sixDimensionalDragState = 0;
    robot->GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
    printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);
    robot->Sleep(1000);
    vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
    vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
    vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
    vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
    robot->EndForceDragControl(1, 0, 0, M, B, K, F, 50, 100);
    robot->GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
    printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);

    robot->Sleep(1000);
    robot->EndForceDragControl(0, 0, 0, M, B, K, F, 50, 100);
    robot->GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
    printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);
    robot->Sleep(1000);

    robot->DragTeachSwitch(1);
    vector <double> lamdeDain = { 3.0, 2.0, 2.0, 2.0, 2.0, 3.0 };
    vector <double> KGain = { 0, 0, 0, 0, 0, 0 };
    vector <double> BGain = { 150, 150, 150, 5.0, 5.0, 1.0 };
    robot->ForceAndJointImpedanceStartStop(1, 0, lamdeDain, KGain, BGain, 1000, 180);
    robot->GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
    printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);
    robot->Sleep(1000);
    robot->DragTeachSwitch(0);
    robot->ForceAndJointImpedanceStartStop(0, 0, lamdeDain, KGain, BGain, 1000, 180);
    robot->GetForceAndTorqueDragState(dragState, sixDimensionalDragState);
    printf("the drag state is %d %d \n", dragState, sixDimensionalDragState);

    return 0;
    }

設定力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定力道感測器下負載重量
      * @param  [in] weight 負載重量 kg
      * @return  錯誤碼
      */
     errno_t SetForceSensorPayload(double weight);

設定力道感測器下負載質心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定力道感測器下負載質心
      * @param  [in] x 負載質心x mm
      * @param  [in] y 負載質心y mm
      * @param  [in] z 負載質心z mm
      * @return  錯誤碼
      */
     errno_t SetForceSensorPayloadCog(double x, double y, double z);

取得力道感測器下負載重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
     /**
      * @brief  取得力道感測器下負載重量
      * @param  [in] weight 負載重量 kg
      * @return  錯誤碼
      */
     errno_t GetForceSensorPayload(double& weight);

取得力感測器下負載質心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  取得力感測器下負載質心
      * @param  [out] x 負載質心x mm
      * @param  [out] y 負載質心y mm
      * @param  [out] z 負載質心z mm
      * @return  錯誤碼
      */
     errno_t GetForceSensorPayloadCog(double& x, double& y, double& z);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int FTLoadSetGet(FRRobot* robot)
    {
    robot->SetForceSensorPayload(0.824);
    robot->SetForceSensorPayloadCog(0.778, 2.554, 48.765);
    double weight = 0;
    double x = 0, y = 0, z = 0;
    robot->GetForceSensorPayload(weight);
    robot->GetForceSensorPayloadCog(x, y, z);
    printf("the FT load is   %lf,  %lf  %lf  %lf\n", weight, x, y, z);

    return 0;
    }

力傳感器自動校零
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  力傳感器自動校零
      * @param  [out] weight 传感器质量 kg
      * @param  [out] pos 传感器质心 mm
      * @return  錯誤碼
      */
     errno_t ForceSensorAutoComputeLoad(double& weight, DescTran& pos);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int FTAutoComputeLoad(FRRobot* robot)
    {
    robot->SetForceSensorPayload(0);
    robot->SetForceSensorPayloadCog(0, 0, 0);
    double weight = 0;
    DescTran tran = {};
    robot->ForceSensorAutoComputeLoad(weight, tran);
    cout << "the result is weight " << weight << " pos is  " << tran.x << "  " << tran.y << "  " << tran.z << endl;
    return 0;
    }

設定焊接製程曲線參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定焊接製程曲線參數
      * @param  [in] id 焊接工藝編號(1-99)
      * @param  [in] startCurrent 起弧電流(A)
      * @param  [in] startVoltage 起弧電壓(V)
      * @param  [in] startTime 起弧時間(ms)
      * @param  [in] weldCurrent 焊接電流(A)
      * @param  [in] weldVoltage 焊接電壓(V)
      * @param  [in] endCurrent 收弧電流(A)
      * @param  [in] endVoltage 收弧電壓(V)
      * @param  [in] endTime 收弧時間(ms)
      * @return  錯誤碼
      */
     errno_t WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

取得焊接製程曲線參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  取得焊接製程曲線參數
      * @param  [in] id 焊接工藝編號(1-99)
      * @param  [out] startCurrent 起弧電流(A)
      * @param  [out] startVoltage 起弧電壓(V)
      * @param  [out] startTime 起弧時間(ms)
      * @param  [out] weldCurrent 焊接電流(A)
      * @param  [out] weldVoltage 焊接電壓(V)
      * @param  [out] endCurrent 收弧電流(A)
      * @param  [out] endVoltage 收弧電壓(V)
      * @param  [out] endTime 收弧時間(ms)
      * @return  錯誤碼
      */
     errno_t WeldingGetProcessParam(int id, double& startCurrent, double& startVoltage, double& startTime, double& weldCurrent, double& weldVoltage, double& endCurrent, double& endVoltage, double& endTime);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int WeldingProcessParamConfig(FRRobot* robot)
    {
    robot->WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000);
    robot->WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333);

    double startCurrent = 0;
    double startVoltage = 0;
    double startTime = 0;
    double weldCurrent = 0;
    double weldVoltage = 0;
    double endCurrent = 0;
    double endVoltage = 0;
    double endTime = 0;

    robot->WeldingGetProcessParam(1, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
    cout << "the Num 1 process param is " << startCurrent << "  " << startVoltage<< "  " <<startTime<<"  " <<weldCurrent<< "  " <<weldVoltage<< "  " <<endCurrent<< "  " <<endVoltage<< "  " <<endTime << endl;

    robot->WeldingGetProcessParam(2, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
    cout << "the Num 2 process param is " << startCurrent << "  " << startVoltage << "  " << startTime << "  " << weldCurrent << "  " << weldVoltage << "  " << endCurrent << "  " << endVoltage << "  " << endTime << endl;
    return 0;
    }

末端感測器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  末端感測器配置
    * @param  [in] idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param  [in] idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @param  [in] idSoftware 軟體版本，0-J1.0/HuiDe1.0(暫未開放)
    * @param  [in] idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    * @return  錯誤碼
    */
    errno_t AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

取得末端傳感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  取得末端傳感器配置
      * @param  [out] idCompany 廠商，18-JUNKONG；25-HUIDE
      * @param  [out] idDevice 類型，0-JUNKONG/RYR6T.V1.0
      * @return  錯誤碼
      */
    errno_t AxleSensorConfigGet(int& idCompany, int& idDevice);

末端感測器激活
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  末端感測器激活
      * @param  [in] actFlag 0-復位；1-激活
      * @return  錯誤碼
      */
    errno_t AxleSensorActivate(int actFlag);

末端感測器暫存器寫入
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  末端感測器暫存器寫入
      * @param  [in] devAddr 設備地址編號 0-255
      * @param  [in] regHAddr 暫存器位址高8位
      * @param  [in] regLAddr 暫存器地址低8位
      * @param  [in] regNum 暫存器數 0-255
      * @param  [in] data1 写入暫存器数值1
      * @param  [in] data2 写入暫存器数值2
      * @param  [in] isNoBlock 0-阻塞；1-非阻塞
      * @return  錯誤碼
      */
    errno_t AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void AxleSensorConfig(FRRobot* robot)
    {
    robot->AxleSensorConfig(18, 0, 0, 1);
    int company = -1;
    int type = -1;
    robot->AxleSensorConfigGet(company, type);
    printf("company is %d, type is %d\n", company, type);

    robot->AxleSensorActivate(1);

    robot->Sleep(5000);

    while (true)
    {
    robot->AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
    }

    }

設定控制箱DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief  設定控制箱DO停止/暫停後輸出是否重設
     * @param  [in] resetFlag  0-不復位；1-復位
     * @return  錯誤碼
     */
    errno_t SetOutputResetCtlBoxDO(int resetFlag);

設定控制箱AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定控制箱AO停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetCtlBoxAO(int resetFlag);

設定末端工具DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定末端工具DO停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetAxleDO(int resetFlag);
 
設定末端工具AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定末端工具AO停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetAxleAO(int resetFlag);
 
設定擴充DO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定擴充DO停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetExtDO(int resetFlag);
 
設定擴充AO停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定擴充AO停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetExtAO(int resetFlag);
 
設定SmartTool停止/暫停後輸出是否重設
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定SmartTool停止/暫停後輸出是否重設
      * @param  [in] resetFlag  0-不復位；1-復位
      * @return  錯誤碼
      */
    errno_t SetOutputResetSmartToolDO(int resetFlag);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int IOReset(FRRobot* robot)
    {
    int resetFlag = 0;
    int rtn = robot->SetOutputResetCtlBoxDO(resetFlag);
    robot->SetOutputResetCtlBoxAO(resetFlag);
    robot->SetOutputResetAxleDO(resetFlag);
    robot->SetOutputResetAxleAO(resetFlag);
    robot->SetOutputResetExtDO(resetFlag);
    robot->SetOutputResetExtAO(resetFlag);
    robot->SetOutputResetSmartToolDO(resetFlag);
    return 0;
    }
 
仿真擺盪開始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  仿真擺盪開始
      * @param  [in] weaveNum  擺動參數編號
      * @return  錯誤碼
      */
    errno_t WeaveStartSim(int weaveNum);
 
仿真擺盪結束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  仿真擺盪結束
      * @param  [in] weaveNum  擺動參數編號
      * @return  錯誤碼
      */
    errno_t WeaveEndSim(int weaveNum);
 
開始軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  開始軌跡偵測預警(不運動)
      * @param  [in] weaveNum   擺動參數編號
      * @return  錯誤碼
      */
    errno_t WeaveInspectStart(int weaveNum);
 
結束軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 結束軌跡偵測預警(不運動)
      * @param  [in] weaveNum   擺動參數編號
      * @return  錯誤碼
      */
    errno_t WeaveInspectEnd(int weaveNum);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     int WeaveSim(FRRobot* robot)
    {
    DescPose startdescPose = { 238.209, -403.633, 251.291, 177.222, -1.433, 133.675 };
    JointPos startjointPos = { -48.728, -86.235, -95.288, -90.025, 92.715, 87.595 };
    DescPose enddescPose = { 238.207, -596.305, 251.294, 177.223, -1.432, 133.675 };
    JointPos endjointPos = { -60.240, -110.743, -66.784, -94.531, 92.351, 76.078 };

    ExaxisPos exaxisPos = { 0, 0, 0, 0 };
    DescPose offdese = { 0, 0, 0, 0, 0, 0 };

    robot->MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->WeaveStartSim(0);
    robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->WeaveEndSim(0);
    return 0;
    }

    int WeaveInspect(FRRobot* robot)
    {
    DescPose startdescPose = { 238.209, -403.633, 251.291, 177.222, -1.433, 133.675 };
    JointPos startjointPos = { -48.728, -86.235, -95.288, -90.025, 92.715, 87.595 };
    DescPose enddescPose = { 238.207, -596.305, 251.294, 177.223, -1.432, 133.675 };
    JointPos endjointPos = { -60.240, -110.743, -66.784, -94.531, 92.351, 76.078 };

    ExaxisPos exaxisPos = { 0, 0, 0, 0 };
    DescPose offdese = { 0, 0, 0, 0, 0, 0 };

    robot->MoveL(&startjointPos, &startdescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->WeaveInspectStart(0);
    robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->WeaveInspectEnd(0);
    return 0;
    }
 
擴展IO-配置焊機氣體偵測訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴展IO-配置焊機氣體偵測訊號
      * @param  [in] DONum  氣體偵測訊號擴展DO編號
      * @return  錯誤碼
      */
    errno_t SetAirControlExtDoNum(int DONum);
 
擴充IO-配置焊接機起弧訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴充IO-配置焊接機起弧訊號
      * @param  [in] DONum  焊机起弧信号扩展DO編號
      * @return  錯誤碼
      */
    errno_t SetArcStartExtDoNum(int DONum);
 
擴充IO-配置焊接機反向送絲訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴充IO-配置焊接機反向送絲訊號
      * @param  [in] DONum  反向送絲信号扩展DO編號
      * @return  錯誤碼
      */
    errno_t SetWireReverseFeedExtDoNum(int DONum);
 
擴充IO-配置焊接機正向送絲訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴充IO-配置焊接機正向送絲訊號
      * @param  [in] DONum  正向送絲信号扩展DO編號
      * @return  錯誤碼
      */
    errno_t SetWireForwardFeedExtDoNum(int DONum);
 
擴充IO-配置焊接機起弧成功訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴充IO-配置焊接機起弧成功訊號
      * @param  [in] DINum  起弧成功訊號擴展DI編號
      * @return  錯誤碼
      */
    errno_t SetArcDoneExtDiNum(int DINum);
 
擴充IO-配置焊接機準備訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴充IO-配置焊接機準備訊號
      * @param  [in] DINum  焊接機準備訊號擴展DI編號
      * @return  錯誤碼
      */
    errno_t SetWeldReadyExtDiNum(int DINum);
 
擴展IO-配置焊接中斷恢復訊號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 擴展IO-配置焊接中斷恢復訊號
      * @param  [in] reWeldDINum  焊接中斷後恢復焊接訊號擴展DI編號
      * @param  [in] abortWeldDINum  焊接中斷後退出焊接訊號擴展DI編號
      * @return  錯誤碼
      */
    errno_t SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int SetExtDIOFuntion(FRRobot* robot)
    {
    robot->SetArcStartExtDoNum(10);
    robot->SetAirControlExtDoNum(20);
    robot->SetWireForwardFeedExtDoNum(30);
    robot->SetWireReverseFeedExtDoNum(40);

    robot->SetWeldReadyExtDiNum(50);
    robot->SetArcDoneExtDiNum(60);
    robot->SetExtDIWeldBreakOffRecover(70, 80);
    return 0;
    }
 
設定機器人碰撞偵測方法
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 設定機器人碰撞偵測方法
      * @param  [in] method 碰撞偵測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啟
      * @return  錯誤碼
      */
    errno_t SetCollisionDetectionMethod(int method);
 
設定靜態下碰撞偵測開始關閉
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 設定靜態下碰撞偵測開始關閉
      * @param  [in] status 0-關閉；1-開啟
      * @return  錯誤碼
      */
    errno_t SetStaticCollisionOnOff(int status);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int StaticCollision(FRRobot* robot)
    {
    robot->SetCollisionDetectionMethod(0);
    robot->SetStaticCollisionOnOff(1);
    robot->Sleep(5000);
    robot->SetStaticCollisionOnOff(0);
    return 0;
    }
 
關節扭力功率檢測
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 關節扭力功率檢測
      * @param  [in] status 0-關閉；1-開啟
      * @param  [in] power 設定最大功率(W);
      * @return  錯誤碼
      */
     errno_t SetPowerLimit(int status, double power);
 
關節扭矩控制開始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制開始
    * @return  錯誤碼
    */
    errno_t ServoJTStart();
 
關節扭矩控制
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制
    * @param  [in] torque j1~j6關節扭矩，單位Nm
    * @param  [in] interval 指令週期，單位s，範圍[0.001~0.008]
    * @return  錯誤碼
    */
    errno_t ServoJT(float torque[], double interval);
 
關節扭矩控制结束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制结束
    * @return  錯誤碼
    */
    errno_t ServoJTEnd();

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int PowerLimitOn(FRRobot* robot)
    {
    robot->DragTeachSwitch(1);
    robot->SetPowerLimit(1, 2);
    float torques[] = { 0, 0, 0, 0, 0, 0 };
    robot->GetJointTorques(1, torques);

    int count = 100;
    robot->ServoJTStart(); //   #servoJT開始
    int error = 0;
    while (count > 0)
    {
    torques[0] = torques[0] + 0.1;//  #每次1軸增加0.1NM，運動100次
    error = robot->ServoJT(torques, 0.001);  //# 關節空間伺服模式運動
    count = count - 1;
    robot->Sleep(1);
    }

    error = robot->ServoJTEnd();  //#伺服運動結束
    return 0;
    }
 
設定機器人 20004 連接埠回饋週期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定機器人 20004 連接埠回饋週期
     * @param [in] period 機器人 20004 連接埠回饋週期(ms)
     * @return  錯誤碼
     */
    errno_t SetRobotRealtimeStateSamplePeriod(int period);
 
取得機器人 20004 連接埠回饋週期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得機器人 20004 連接埠回饋週期
     * @param [out] period 機器人 20004 連接埠回饋週期(ms)
     * @return  錯誤碼
     */
    errno_t GetRobotRealtimeStateSamplePeriod(int& period);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     void TestRealTimePeriod(FRRobot* robot)
     {
     robot->SetRobotRealtimeStateSamplePeriod(10);
     int getPeriod = 0;
     robot->GetRobotRealtimeStateSamplePeriod(getPeriod);
     cout << "period is " << getPeriod << endl;
     robot->Sleep(1000);
     }
 
取得機器人關節驅動器溫度(℃)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 取得機器人關節驅動器溫度(℃)
    * @return 錯誤碼
    */
    errno_t GetJointDriverTemperature(double temperature[]);
 
取得機器人關節驅動器扭矩(Nm)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得機器人關節驅動器扭矩(Nm)
     * @return 錯誤碼
     */
    errno_t GetJointDriverTorque(double torque[]);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     void TestTorue(FRRobot* robot)
     {
     robot->ProgramLoad("/fruser/test2.lua");
     robot->ProgramRun();
     int rtn = 0;
     while (true)
     {
     double temperature[6] = {};
     rtn = robot->GetJointDriverTemperature(temperature);
     double torque[6] = {};
     rtn = robot->GetJointDriverTorque(torque);
     printf("test torque is %f %f %f %f %f %f  temperature is %f %f %f %f %f %f\n", torque[0], torque[1], torque[2], torque[3], torque[4], torque[5], temperature[0], temperature[1], temperature[2], temperature[3], temperature[4], temperature[5]);
     robot->Sleep(100);
     }
     }
 
電弧追蹤 + 多層多道補償開啟
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 電弧追蹤 + 多層多道補償開啟
     * @return 錯誤碼
     */
    errno_t ArcWeldTraceReplayStart();
 
電弧追蹤 + 多層多道補償關閉
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 電弧追蹤 + 多層多道補償關閉
     * @return 錯誤碼
     */
    errno_t ArcWeldTraceReplayEnd();
 
偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 偏移量座標變化-多層多道焊
     * @return 錯誤碼
     */
    errno_t MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, DescPose& offset);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void TestWeldTraceReply(FRRobot* robot)
     {
     JointPos mulitilineorigin1_joint;
     mulitilineorigin1_joint.jPos[0] = -24.090;
     mulitilineorigin1_joint.jPos[1] = -63.501;
     mulitilineorigin1_joint.jPos[2] = 84.288;
     mulitilineorigin1_joint.jPos[3] = -111.940;
     mulitilineorigin1_joint.jPos[4] = -93.426;
     mulitilineorigin1_joint.jPos[5] = 57.669;
     
     DescPose mulitilineorigin1_desc;
     mulitilineorigin1_desc.tran.x = -677.559;
     mulitilineorigin1_desc.tran.y = 190.951;
     mulitilineorigin1_desc.tran.z = -1.205;
     mulitilineorigin1_desc.rpy.rx = 1.144;
     mulitilineorigin1_desc.rpy.ry = -41.482;
     mulitilineorigin1_desc.rpy.rz = -82.577;

     DescTran mulitilineX1_desc;
     mulitilineX1_desc.x = -677.556;
     mulitilineX1_desc.y = 211.949;
     mulitilineX1_desc.z = -1.206;

     DescTran mulitilineZ1_desc;
     mulitilineZ1_desc.x = -677.564;
     mulitilineZ1_desc.y = 190.956;
     mulitilineZ1_desc.z = 19.817;

     JointPos mulitilinesafe_joint;
     mulitilinesafe_joint.jPos[0] = -25.734;
     mulitilinesafe_joint.jPos[1] = -63.778;
     mulitilinesafe_joint.jPos[2] = 81.502;
     mulitilinesafe_joint.jPos[3] = -108.975;
     mulitilinesafe_joint.jPos[4] = -93.392;
     mulitilinesafe_joint.jPos[5] = 56.021;

     DescPose mulitilinesafe_desc;
     mulitilinesafe_desc.tran.x = -677.561;
     mulitilinesafe_desc.tran.y = 211.950;
     mulitilinesafe_desc.tran.z = 19.812;
     mulitilinesafe_desc.rpy.rx = 1.144;
     mulitilinesafe_desc.rpy.ry = -41.482;
     mulitilinesafe_desc.rpy.rz = -82.577;

     JointPos mulitilineorigin2_joint;
     mulitilineorigin2_joint.jPos[0] = -29.743;
     mulitilineorigin2_joint.jPos[1] = -75.623;
     mulitilineorigin2_joint.jPos[2] = 101.241;
     mulitilineorigin2_joint.jPos[3] = -116.354;
     mulitilineorigin2_joint.jPos[4] = -94.928;
     mulitilineorigin2_joint.jPos[5] = 55.735;

     DescPose mulitilineorigin2_desc;
     mulitilineorigin2_desc.tran.x = -563.961;
     mulitilineorigin2_desc.tran.y = 215.359;
     mulitilineorigin2_desc.tran.z = -0.681;
     mulitilineorigin2_desc.rpy.rx = 2.845;
     mulitilineorigin2_desc.rpy.ry = -40.476;
     mulitilineorigin2_desc.rpy.rz = -87.443;
     
     DescTran mulitilineX2_desc;
     mulitilineX2_desc.x = -563.965;
     mulitilineX2_desc.y = 220.355;
     mulitilineX2_desc.z = -0.680;

     DescTran mulitilineZ2_desc;
     mulitilineZ2_desc.x = -563.968;
     mulitilineZ2_desc.y = 215.362;
     mulitilineZ2_desc.z = 4.331;

     ExaxisPos epos;
     epos.ePos[0] = 0;
     epos.ePos[1] = 0;
     epos.ePos[2] = 0;
     epos.ePos[3] = 0;
     DescPose offset;
     offset.tran.x = 0;
     offset.tran.y = 0;
     offset.tran.z = 0;
     offset.rpy.rx = 0;
     offset.rpy.ry = 0;
     offset.rpy.rz = 0;

     robot->Sleep(10);
     int error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ARCStart(1, 0, 3000);
     printf("ARCStart return:  %d\n", error);

     error = robot->WeaveStart(0);
     printf("WeaveStart return:  %d\n", error);

     error = robot->ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
     printf("ArcWeldTraceControl return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
     printf("ArcWeldTraceControl return:  %d\n", error);

     error = robot->WeaveEnd(0);
     printf("WeaveEnd return:  %d\n", error);

     error = robot->ARCEnd(1, 0, 10000);
     printf("ARCEnd return:  %d\n", error);

     error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);

     error = robot->MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);
     printf("MultilayerOffsetTrsfToBase return:  %d   offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);

     error = robot->MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ARCStart(1, 0, 3000);
     printf("ARCStart return:  %d\n", error);

     error = robot->MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);
     printf("MultilayerOffsetTrsfToBase return:  %d   offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);

     error = robot->ArcWeldTraceReplayStart();
     printf("ArcWeldTraceReplayStart return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ArcWeldTraceReplayEnd();
     printf("ArcWeldTraceReplayEnd return:  %d\n", error);

     error = robot->ARCEnd(1, 0, 10000);
     printf("ARCEnd return:  %d\n", error);

     error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);

     error = robot->MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);
     printf("MultilayerOffsetTrsfToBase return:  %d   offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);

     error = robot->MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ARCStart(1, 0, 3000);
     printf("ARCStart return:  %d\n", error);

     error = robot->MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);
     printf("MultilayerOffsetTrsfToBase return:  %d   offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);

     error = robot->ArcWeldTraceReplayStart();
     printf("MoveJ return:  %d\n", error);

     error = robot->MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
     printf("MoveL return:  %d\n", error);

     error = robot->ArcWeldTraceReplayEnd();
     printf("ArcWeldTraceReplayEnd return:  %d\n", error);

     error = robot->ARCEnd(1, 0, 3000);
     printf("ARCEnd return:  %d\n", error);

     error = robot->MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
     printf("MoveJ return:  %d\n", error);
     }
 
指定姿態速度開啟
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿態速度開啟
    * @param [in] ratio 姿態速度百分比[0-300]
    * @return  錯誤碼
    */
    errno_t AngularSpeedStart(int ratio);
 
指定姿態速度關閉
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 指定姿態速度關閉
     * @return  錯誤碼
     */
    errno_t AngularSpeedEnd();
 
代碼範例
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void TestAngular(FRRobot* robot)
     {
     JointPos JP1(-68.030, -63.537, -105.223, -78.368, 72.828, 24.876);
     DescPose DP1(-60.984, -533.958, 279.089, -22.052, -4.777, 172.406);

     JointPos JP2(-80.916, -76.030, -108.901, -70.956, 99.026, -74.533);
     DescPose DP2(36.750, -488.721, 145.781, -37.539, -11.211, -96.491);

     JointPos JP3(-86.898, -95.200, -103.665, -70.570, 98.266, -93.321);
     DescPose DP3(-21.462, -509.234, 25.706, -41.780, -1.042, -83.611);

     JointPos JP4(-85.364, -102.697, -94.674, -70.557, 95.302, -93.116);
     DescPose DP4(-24.075, -580.525, 25.881, -44.818, -2.357, -82.259);

     JointPos JP5(-78.815, -94.279, -105.315, -65.348, 87.328, 3.220);
     DescPose DP5(-29.155, -580.477, 25.884, -44.795, -2.374, -172.261);

     JointPos JP6(-81.057, -94.494, -105.107, -65.241, 87.527, 0.987);
     DescPose DP6(-49.270, -580.460, 25.886, -44.796, -2.374, -172.263);

     JointPos JP7(-76.519, -101.428, -94.915, -76.521, 85.041, 95.758);
     DescPose DP7(-54.189, -580.362, 25.878, -44.779, -2.353, 97.740);

     JointPos JP8(-74.406, -90.991, -106.574, -75.480, 85.150, 97.875);
     DescPose DP8(-54.142, -503.358, 25.865, -44.780, -2.353, 97.740);

     ExaxisPos epos(0, 0, 0, 0);
     DescPose offset(0, 0, 0, 0, 0, 0);

     int tool = 7;
     int user = 0;
     double vel = 100.0;
     double acc = 100.0;
     double ovl = 50.0;
     int blend = -1;
     int offsetFlag = 0;

     int error = robot->MoveJ(&JP1, &DP1, tool, user, vel, acc, ovl, &epos, blend, offsetFlag, &offset);
     error = robot->MoveJ(&JP2, &DP2, tool, user, vel, acc, ovl, &epos, blend, offsetFlag, &offset);
     error = robot->MoveL(&JP3, &DP3, tool, user, vel, acc, ovl, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     robot->SetOaccScale(100);
     error = robot->MoveL(&JP4, &DP4, tool, user, vel, acc, ovl * 0.1, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     robot->AngularSpeedStart(50);
     error = robot->MoveL(&JP5, &DP5, tool, user, vel, acc, ovl * 0.1, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     robot->AngularSpeedEnd();
     error = robot->MoveL(&JP6, &DP6, tool, user, vel, acc, ovl * 0.1, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     robot->AngularSpeedStart(50);
     error = robot->MoveL(&JP7, &DP7, tool, user, vel, acc, ovl * 0.1, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     robot->AngularSpeedEnd();
     error = robot->MoveL(&JP8, &DP8, tool, user, vel, acc, ovl * 0.1, blend, &epos, 0, offsetFlag, &offset, 0, 100);
     }
 
機器人軟體升級
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 機器人軟體升級
     * @param [in] filePath 軟體升級包全路徑
     * @param [in] block是否阻塞至升級完成 true:阻塞；false:非阻塞
     * @return  錯誤碼
     */
    errno_t SoftwareUpgrade(std::string filePath, bool block);
 
取得機器人軟體升級狀態
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得機器人軟體升級狀態
    * @param [out] state 機器人軟體包升級狀態(0-空閒或上傳升級包中；1~100：升級完成百分比；-1:升級軟體失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓縮失敗；-5：使用者配置升級失敗；-6：週邊配置升級失敗；-7：擴展軸配置升級失敗；-8：機器人配置升級失敗；-9：DH參數配置升級失敗)
    * @return  錯誤碼
    */
    errno_t GetSoftwareUpgradeState(int &state);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     void TestUpgrade(FRRobot* robot)
     {
     robot->SoftwareUpgrade("D://test/software.tar.gz", false);
     while (true)
     {
     int curState = -1;
     robot->GetSoftwareUpgradeState(curState);
     printf("upgrade state is %d\n", curState);
     robot->Sleep(300);
     }
     }
 
設定485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定485擴展軸運動加減速度
     * @param [in] acc 485擴展軸運動加速度
     * @param [in] dec 485擴展軸運動减速度
     * @return  錯誤碼
     */
    errno_t AuxServoSetAcc(double acc, double dec);
 
設定485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定485擴展軸急停加減速度
     * @param [in] acc 485擴展軸急停加速度
     * @param [in] dec 485擴展軸急停减速度
     * @return  錯誤碼
     */
    errno_t AuxServoSetEmergencyStopAcc(double acc, double dec);
 
取得485擴展軸運動加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得485擴展軸運動加減速度
     * @param [out] acc 485擴展軸運動加速度
     * @param [out] dec 485擴展軸運動减速度
     * @return  錯誤碼
     */
    errno_t AuxServoGetAcc(double& acc, double& dec);
 
取得485擴展軸急停加減速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 取得485擴展軸急停加減速度
     * @param [out] acc 485擴展軸急停加速度
     * @param [out] dec 485擴展軸急停减速度
     * @return  錯誤碼
     */
    errno_t AuxServoGetEmergencyStopAcc(double& acc, double& dec);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
        
    void TestAuxservo(FRRobot* robot)
     {
     robot->AuxServoSetParam(1, 1, 1, 1, 130172, 15.45);
     robot->AuxServoEnable(1, 0);
     robot->Sleep(1000);
     robot->AuxServoSetControlMode(1, 1);
     robot->Sleep(1000);
     robot->AuxServoEnable(1, 1);
     robot->Sleep(1000);
     robot->AuxServoHoming(1, 1, 10, 10, 100);
     robot->Sleep(4000);
     robot->AuxServoSetAcc(3000, 3000);
     robot->AuxServoSetEmergencyStopAcc(5000, 5000);
     robot->Sleep(1000);
     double emagacc = 0;
     double emagdec = 0;
     robot->AuxServoGetEmergencyStopAcc(emagacc, emagdec);
     printf("emergency acc is %f  dec is %f \n", emagacc ,emagdec);

     robot->AuxServoSetTargetSpeed(1, 500, 100);

     robot->ProgramLoad("/fruser/testPTP.lua");
     robot->ProgramRun();
     int i = 0;
     while (true)
     {
     i++;
     if (i > 400)
     {
     robot->ResetAllError();
     i = 0;

     robot->AuxServoSetTargetSpeed(1, 500, 100);
     }
     ROBOT_STATE_PKG pkg;
     robot->GetRobotRealTimeState(&pkg);
     printf("%d:%d  cur velocity is %f   cur 485 axis emergency state is %d   robot collision state is %d  robot emergency state is %d\n",
     pkg.robotTime.second,pkg.robotTime.millisecond,pkg.aux_state.servoVel, ((pkg.aux_state.servoState >> 7) & 0x01), pkg.collisionState, pkg.EmergencyStop);
     robot->Sleep(5);
     ROBOT_STATE_PKG pkg;
     robot->GetRobotRealTimeState(&pkg);
     printf("cur velocity is %f   cur emergency state is %d \n", pkg.aux_state.servoVel, ((pkg.aux_state.servoState >> 7) & 0x01));
     robot->Sleep(20);
    robot->AuxServoSetAcc(5000, 5000);
    robot->AuxServoSetTargetPos(1, 1000, 500, 100);
    robot->Sleep(2000);
    robot->AuxServoSetTargetPos(1, 0, 500, 100);
    robot->Sleep(3000);
    robot->AuxServoSetAcc(500, 500);
    robot->AuxServoSetTargetPos(1, 1000, 500, 100);
    robot->Sleep(2000);
    robot->AuxServoSetTargetPos(1, 0, 500, 100);
    robot->Sleep(3000);
    robot->AuxServoSetTargetPos(1, 1000, 500, 10);
    robot->Sleep(5000);
    robot->AuxServoSetTargetPos(1, 0, 500, 10);
    robot->Sleep(5000);

    robot->AuxServoSetTargetSpeed(1, 500, 100);
    robot->Sleep(2000);
    robot->AuxServoSetTargetSpeed(1, 0, 100);
    robot->Sleep(2000);
    robot->AuxServoSetTargetSpeed(1, 500, 10);
    robot->Sleep(2000);
    robot->AuxServoSetTargetSpeed(1, 0, 10);
    robot->Sleep(2000);
     }
     }
 
可移動裝置使能
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移動裝置使能
     * @param enable false-去使能；true-使能
     * @return 錯誤碼
     */
    errno_t TractorEnable(bool enable);
 
可移動裝置回零
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移動裝置回零
     * @return 錯誤碼
     */
    errno_t TractorHoming();
 
可移動裝置直線運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
     * @brief 可移動裝置直線運動
     * @param distance 直線運動距離（mm）
     * @param vel 直線運動速度百分比（0-100）
     * @return 錯誤碼
     */
    errno_t TractorMoveL(double distance, double vel);
 
可移動裝置圓弧運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移動裝置圓弧運動
     * @param radio 圓弧運動半徑（mm）
     * @param angle 圓弧運動角度（°）
     * @param vel 直線運動速度百分比（0-100）
     * @return 錯誤碼
     */
    errno_t TractorMoveC(double radio, double angle, double vel);
 
可移動裝置停止運動
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移動裝置停止運動
     * @return 錯誤碼
     */
    errno_t TractorStop();

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void TestTractorMove(FRRobot* robot)
     {
     robot->ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10);
     robot->ExtDevLoadUDPDriver();
     robot->ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
     robot->ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
     robot->SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);

     robot->TractorEnable(false);
     robot->Sleep(2000);
     robot->TractorEnable(true);
     robot->Sleep(2000);
     robot->TractorHoming();
     robot->Sleep(2000);
     robot->TractorMoveL(100, 2);
     robot->Sleep(5000);
     robot->TractorStop();
     robot->TractorMoveL(-100, 20);
     robot->Sleep(5000);
     robot->TractorMoveC(300, 90, 20);
     robot->Sleep(10000);
     robot->TractorMoveC(300, -90, 20);
     robot->Sleep(1);
     }
 
設定焊絲尋位擴充IO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定焊絲尋位擴充IO端口
     * @param searchDoneDINum 焊絲尋位成功DO端口(0-127)
     * @param searchStartDONum 焊絲尋位啟動停止控制DO端口(0-127)
     * @return 錯誤碼
     */
    errno_t SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     void TestUDPWireSearch(FRRobot* robot)
     {
     robot->ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
     robot->ExtDevLoadUDPDriver();

     robot->SetWireSearchExtDIONum(0, 0);

     int rtn0, rtn1, rtn2 = 0;
     ExaxisPos exaxisPos = { 0.0, 0.0, 0.0, 0.0 };
     DescPose offdese = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
     
     DescPose descStart = { -158.767, -510.596, 271.709, -179.427, -0.745, -137.349 };
     JointPos jointStart = { 61.667, -79.848, 108.639, -119.682, -89.700, -70.985 };
     
     DescPose descEnd = { 0.332, -516.427, 270.688, 178.165, 0.017, -119.989 };
     JointPos jointEnd = { 79.021, -81.839, 110.752, -118.298, -91.729, -70.981 };

     robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
     robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
     
     DescPose descREF0A = { -66.106, -560.746, 270.381, 176.479, -0.126, -126.745 };
     JointPos jointREF0A = { 73.531, -75.588, 102.941, -116.250, -93.347, -69.689 };
     
     DescPose descREF0B = { -66.109, -528.440, 270.407, 176.479, -0.129, -126.744 };
     JointPos jointREF0B = { 72.534, -79.625, 108.046, -117.379, -93.366, -70.687 };
     
     DescPose descREF1A = { 72.975, -473.242, 270.399, 176.479, -0.129, -126.744 };
     JointPos jointREF1A = { 87.169, -86.509, 115.710, -117.341, -92.993, -56.034 };
     
     DescPose descREF1B = { 31.355, -473.238, 270.405, 176.480, -0.130, -126.745 };
     JointPos jointREF1B = { 82.117, -87.146, 116.470, -117.737, -93.145, -61.090 };

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
     robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
     rtn1 = robot->WireSearchWait("REF0");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
     robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
     rtn1 = robot->WireSearchWait("REF1");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
     robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
     rtn1 = robot->WireSearchWait("RES0");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
     robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
     rtn1 = robot->WireSearchWait("RES1");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
     vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
     int offectFlag = 0;
     DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
     rtn0 = robot->GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
     robot->PointsOffsetEnable(0, &offectPos);
     robot->MoveL(&jointStart, &descStart, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
     robot->MoveL(&jointEnd, &descEnd, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
     robot->PointsOffsetDisable();
     }
 
設定焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定焊機控制模式擴展DO端口
     * @param DONum 焊機控制模式DO端口(0-127)
     * @return 錯誤碼
     */
    errno_t SetWeldMachineCtrlModeExtDoNum(int DONum);
 
設定焊機控制模式
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設定焊機控制模式
     * @param mode 焊接機控制模式;0-一元化
     * @return 錯誤碼
     */
    errno_t SetWeldMachineCtrlMode(int mode);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void TestWeldmechineMode(FRRobot* robot)
     {
     robot->ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
     robot->ExtDevLoadUDPDriver();

     robot->SetWeldMachineCtrlModeExtDoNum(17);
     for (int i = 0; i < 5; i++)
     {
     robot->SetWeldMachineCtrlMode(0);
     robot->Sleep(1000);
     robot->SetWeldMachineCtrlMode(1);
     robot->Sleep(1000);
     }

     robot->SetWeldMachineCtrlModeExtDoNum(18);
     for (int i = 0; i < 5; i++)
     {
     robot->SetWeldMachineCtrlMode(0);
     robot->Sleep(1000);
     robot->SetWeldMachineCtrlMode(1);
     robot->Sleep(1000);
     }

     robot->SetWeldMachineCtrlModeExtDoNum(19);
     for (int i = 0; i < 5; i++)
     {
     robot->SetWeldMachineCtrlMode(0);
     robot->Sleep(1000);
     robot->SetWeldMachineCtrlMode(1);
     robot->Sleep(1000);
     }
     }
 
設定與機器人通訊重連參數
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定與機器人通訊重連參數
    * @param  [in] enable  網路故障時使能重連 true-使能 false-不使能
    * @param  [in] reconnectTime 重連時間，單位ms
    * @param  [in] period 重連週期，單位ms
    * @return  錯誤碼
    */
    errno_t SetReConnectParam(bool enable, int reconnectTime = 30000, int period = 50);

範例程式
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     int main(void)
     {
     ROBOT_STATE_PKG pkg = {};
     FRRobot robot;

     robot.LoggerInit();
     robot.SetLoggerLevel(1);
     int rtn = robot.RPC("192.168.58.2");
     robot.SetReConnectParam(true, 30000, 500);

     while (true)
     {
     int rtn = robot.GetRobotRealTimeState(&pkg);
     printf("the robot motiondone state is %d\n", pkg.jt_cur_pos[0]);
     robot.Sleep(200);
     }
     return 0;
     }
 
開始奇異位姿保護
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 開始奇異位姿保護
	* @param [in] protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
	* @param [in] minShoulderPos 肩奇異調整範圍(mm), 默認100
	* @param [in] minElbowPos 肘奇異調整範圍(mm), 默認50
	* @param [in] minWristPos 腕奇異調整範圍(°), 預設10
	* @return 錯誤碼
	*/
	errno_t SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);
 
停止奇異位姿保護
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 停止奇異位姿保護
	* @return 錯誤碼
	*/
	errno_t SingularAvoidEnd();

代碼範例
+++++++++++++++
.. code-block:: c++
    :linenos:

    void TestSingularAvoidWLin(FRRobot* robot)
    {
        DescPose startdescPose(-402.473, -185.876, 103.985, -175.367, 59.682, 94.221);
        JointPos startjointPos(-0.095, -50.828, 109.737, -150.708, -30.225, -0.623);

        DescPose enddescPose(-399.264, -184.434, 296.022, -4.402, 58.061, -94.161);
        JointPos endjointPos(-0.095, -65.547, 105.145, -131.397, 31.851, -0.622);

        ExaxisPos exaxisPos(0, 0, 0, 0);
        DescPose offdese(0, 0, 0, 0, 0, 0);

        robot->MoveL(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
        robot->SingularAvoidStart(0, 150, 50, 20);
        robot->MoveL(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
        robot->SingularAvoidEnd();
    }

傳送帶通訊輸入檢測
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測
    * @param [in] timeout 等待超時時間ms
    * @return 錯誤碼
    */
    errno_t ConveyorComDetect(int timeout);

傳送帶通訊輸入檢測觸發
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 傳送帶通訊輸入檢測觸發
    * @return 錯誤碼
    */
    errno_t ConveyorComDetectTrigger();

代碼示例
************************
    
.. code-block:: c++
    :linenos:

    void Trigger(FRRobot* robot)
    {
      int i;
      cout << "請輸入數字觸發:" << endl;
      std::cin >> i;
      int rtn = robot->ConveyorComDetectTrigger();
      printf("ConveyorComDetectTrigger retval is: %d\n", rtn);
    }

    int ConveyorTest(FRRobot * robot)
    {
      int retval = 0;
      float param[6] = { 1,10000,200,0,0,20 };
      retval = robot->ConveyorSetParam(param, 1, 0, 0);
      printf("ConveyorSetParam retval is: %d\n", retval);
      int index = 1;
      int max_time = 30000;
      uint8_t block = 0;
      retval = 0;
      DescPose startdescPose(139.176, 4.717, 9.088, -179.999, -0.004, -179.990);
      JointPos startjointPos(-34.129, -88.062, 97.839, -99.780, -90.003, -34.140);
        DescPose homePose(139.177, 4.717, 69.084, -180.000, -0.004, -179.989);
      JointPos homejointPos(-34.129, -88.618, 84.039, -85.423, -90.003, -34.140);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      retval = robot->MoveL(&homejointPos, &homePose, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
      printf("MoveL to safety retval is: %d\n", retval);
     std::thread textT(Trigger, robot);
      textT.detach();

      retval = robot->ConveyorComDetect(1000 * 10);
      printf("ConveyorComDetect retval is: %d\n", retval);

      retval = robot->ConveyorGetTrackData(2);
      printf("ConveyorGetTrackData retval is: %d\n", retval);

      retval = robot->ConveyorTrackStart(2);
      printf("ConveyorTrackStart retval is: %d\n", retval);

      robot->MoveL(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
      robot->MoveL(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);

      retval = robot->ConveyorTrackEnd();
      printf("ConveyorTrackEnd retval is: %d\n", retval);
      robot->MoveL(&homejointPos, &homePose, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
        return 0;
    }

