机器人力控
============

.. toctree:: 
    :maxdepth: 5

力传感器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  配置力传感器
    * @param  [in] company  力传感器厂商，17-坤维科技
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  FT_SetConfig(int company, int device, int softvesion, int bus);

获取力传感器配置
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取力传感器配置
    * @param  [in] company  力传感器厂商，待定
    * @param  [in] device  设备号，暂不使用，默认为0
    * @param  [in] softvesion  软件版本号，暂不使用，默认为0
    * @param  [in] bus 设备挂在末端总线位置，暂不使用，默认为0
    * @return  错误码
    */
    errno_t  FT_GetConfig(int *company, int *device, int *softvesion, int *bus);

力传感器激活
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力传感器激活
    * @param  [in] act  0-复位，1-激活
    * @return  错误码
    */
    errno_t  FT_Activate(uint8_t act);

力传感器校零
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  力传感器校零
    * @param  [in] act  0-去除零点，1-零点矫正
    * @return  错误码
    */
    errno_t  FT_SetZero(uint8_t act);   

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

设置力传感器参考坐标系
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置力传感器参考坐标系
    * @param  [in] ref  0-工具坐标系，1-基坐标系
    * @return  错误码
    */
    errno_t  FT_SetRCS(uint8_t ref); 

负载重量辨识记录
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  负载重量辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @return  错误码
    */
    errno_t  FT_PdIdenRecord(int id);   

负载重量辨识计算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  负载重量辨识计算
    * @param  [out] weight  负载重量，单位kg
    * @return  错误码
    */   
    errno_t  FT_PdIdenCompute(float *weight);

负载质心辨识记录
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  负载质心辨识记录
    * @param  [in] id  传感器坐标系编号，范围[1~14]
    * @param  [in] index 点编号，范围[1~3]
    * @return  错误码
    */
    errno_t  FT_PdCogIdenRecord(int id, int index);    

负载质心辨识计算
+++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  负载质心辨识计算
    * @param  [out] cog  负载质心，单位mm
    * @return  错误码
    */   
    errno_t  FT_PdCogIdenCompute(DescTran *cog); 

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

获取参考坐标系下力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取参考坐标系下力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    errno_t  FT_GetForceTorqueRCS(ForceTorque *ft); 

获取力传感器原始力/扭矩数据
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取力传感器原始力/扭矩数据
    * @param  [out] ft  力/扭矩，fx,fy,fz,tx,ty,tz
    * @return  错误码
    */   
    errno_t  FT_GetForceTorqueOrigin(ForceTorque *ft); 

碰撞守护
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  碰撞守护
    * @param  [in] flag 0-关闭碰撞守护，1-开启碰撞守护
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] max_threshold 最大阈值
    * @param  [in] min_threshold 最小阈值
    * @note   力/扭矩检测范围：(ft-min_threshold, ft+max_threshold)
    * @return  错误码
    */   
    errno_t  FT_Guard(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float max_threshold[6], float min_threshold[6]); 

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

恒力控制
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  恒力控制
    * @param  [in] flag 0-关闭恒力控制，1-开启恒力控制
    * @param  [in] sensor_id 力传感器编号
    * @param  [in] select  选择六个自由度是否检测碰撞，0-不检测，1-检测
    * @param  [in] ft  碰撞力/扭矩，fx,fy,fz,tx,ty,tz
    * @param  [in] ft_pid 力pid参数，力矩pid参数
    * @param  [in] adj_sign 自适应启停控制，0-关闭，1-开启
    * @param  [in] ILC_sign ILC启停控制， 0-停止，1-训练，2-实操
    * @param  [in] 最大调整距离，单位mm
    * @param  [in] 最大调整角度，单位deg
    * @return  错误码
    */   
    errno_t  FT_Control(uint8_t flag, int sensor_id, uint8_t select[6], ForceTorque *ft, float ft_pid[6], uint8_t adj_sign, uint8_t ILC_sign, float max_dis, float max_ang);   

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

螺旋线探索
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  螺旋线探索
    * @param  [in] rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param  [in] dr 每圈半径进给量
    * @param  [in] ft 力/扭矩阈值，fx,fy,fz,tx,ty,tz，范围[0~100]
    * @param  [in] max_t_ms 最大探索时间，单位ms
    * @param  [in] max_vel 最大线速度，单位mm/s
    * @return  错误码
    */   
    errno_t  FT_SpiralSearch(int rcs, float dr, float ft, float max_t_ms, float max_vel);  

旋转插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  旋转插入
    * @param  [in] rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param  [in] angVelRot 旋转角速度，单位deg/s
    * @param  [in] ft  力/扭矩阈值，fx,fy,fz,tx,ty,tz，范围[0~100]
    * @param  [in] max_angle 最大旋转角度，单位deg
    * @param  [in] orn 力/扭矩方向，1-沿z轴方向，2-绕z轴方向
    * @param  [in] max_angAcc 最大旋转加速度，单位deg/s^2，暂不使用，默认为0
    * @param  [in] rotorn  旋转方向，1-顺时针，2-逆时针
    * @return  错误码
    */   
    errno_t  FT_RotInsertion(int rcs, float angVelRot, float ft, float max_angle, uint8_t orn, float max_angAcc, uint8_t rotorn);    

直线插入
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  直线插入
    * @param  [in] rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param  [in] ft  力/扭矩阈值，fx,fy,fz,tx,ty,tz，范围[0~100]
    * @param  [in] lin_v 直线速度，单位mm/s
    * @param  [in] lin_a 直线加速度，单位mm/s^2，暂不使用
    * @param  [in] max_dis 最大插入距离，单位mm
    * @param  [in] linorn  插入方向，0-负方向，1-正方向
    * @return  错误码
    */   
    errno_t  FT_LinInsertion(int rcs, float ft, float lin_v, float lin_a, float max_dis, uint8_t linorn);    

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

        //恒力参数
        uint8_t status = 1;  //恒力控制开启标志，0-关，1-开
        int sensor_num = 1; //力传感器编号
        float gain[6] = {0.0001,0.0,0.0,0.0,0.0,0.0};  //最大阈值
        uint8_t adj_sign = 0;  //自适应启停状态，0-关闭，1-开启
        uint8_t ILC_sign = 0;  //ILC控制启停状态，0-停止，1-训练，2-实操
        float max_dis = 100.0;  //最大调整距离
        float max_ang = 5.0;  //最大调整角度

        ForceTorque ft;
        memset(&ft, 0, sizeof(ForceTorque));

        //螺旋线探索参数
        int rcs = 0;  //参考坐标系，0-工具坐标系，1-基坐标系
        float dr = 0.7;  //每圈半径进给量，单位mm
        float fFinish = 1.0; //力或力矩阈值（0~100），单位N或Nm
        float t = 60000.0; //最大探索时间，单位ms
        float vmax = 3.0; //线速度最大值，单位mm/s

        //直线插入参数
        float force_goal = 20.0;  //力或力矩阈值（0~100），单位N或Nm
        float lin_v = 0.0; //直线速度，单位mm/s
        float lin_a = 0.0; //直线加速度，单位mm/s^2,暂不使用
        float disMax = 100.0; //最大插入距离，单位mm
        uint8_t linorn = 1; //插入方向，1-正方向，2-负方向

        //旋转插入参数
        float angVelRot = 2.0;  //旋转角速度，单位°/s
        float forceInsertion = 1.0; //力或力矩阈值（0~100），单位N或Nm
        int angleMax= 45; //最大旋转角度，单位°
        uint8_t orn = 1; //力的方向，1-fz,2-mz
        float angAccmax = 0.0; //最大旋转角加速度，单位°/s^2,暂不使用
        uint8_t rotorn = 1; //旋转方向，1-顺时针，2-逆时针

        uint8_t select1[6] = {0,0,1,1,1,0}; //六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        ft.fz = -10.0;
        robot.FT_Control(status,sensor_num,select1,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_SpiralSearch(rcs,dr,fFinish,t,vmax);
        status = 0;
        robot.FT_Control(status,sensor_num,select1,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select2[6] = {1,1,1,0,0,0};  //六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        gain[0] = 0.00005;
        ft.fz = -30.0;
        status = 1;
        robot.FT_Control(status,sensor_num,select2,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_LinInsertion(rcs,force_goal,lin_v,lin_a,disMax,linorn);
        status = 0;
        robot.FT_Control(status,sensor_num,select2,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select3[6] = {0,0,1,1,1,0};  //六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
        ft.fz = -10.0;
        gain[0] = 0.0001;
        status = 1;
        robot.FT_Control(status,sensor_num,select3,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);
        robot.FT_RotInsertion(rcs,angVelRot,forceInsertion,angleMax,orn,angAccmax,rotorn);
        status = 0;
        robot.FT_Control(status,sensor_num,select3,&ft,gain,adj_sign,ILC_sign,max_dis,max_ang);

        uint8_t select4[6] = {1,1,1,0,0,0};  //六个自由度选择[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
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
    * @param  [in] rcs 参考坐标系，0-工具坐标系，1-基坐标系
    * @param  [in] dir  移动方向，1-正方向，2-负方向 
    * @param  [in] axis 移动轴，1-x轴，2-y轴，3-z轴
    * @param  [in] lin_v 探索直线速度，单位mm/s
    * @param  [in] lin_a 探索直线加速度，单位mm/s^2，暂不使用，默认为0
    * @param  [in] max_dis 最大探索距离，单位mm
    * @param  [in] ft  动作终止力/扭矩阈值，fx,fy,fz,tx,ty,tz  
    * @return  错误码
    */   
    errno_t  FT_FindSurface(int rcs, uint8_t dir, uint8_t axis, float lin_v, float lin_a, float max_dis, float ft);   

计算中间平面位置开始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  计算中间平面位置开始
    * @return  错误码
    */   
    errno_t  FT_CalCenterStart();

计算中间平面位置结束
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  计算中间平面位置结束
    * @param  [out] pos 中间平面位姿
    * @return  错误码
    */      
    errno_t  FT_CalCenterEnd(DescPose *pos);

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

柔顺控制开启
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔顺控制开启
    * @param  [in] p 位置调节系数或柔顺系数
    * @param  [in] force 柔顺开启力阈值，单位N
    * @return  错误码
    */   
    errno_t  FT_ComplianceStart(float p, float force); 

柔顺控制关闭
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  柔顺控制关闭
    * @return  错误码
    */   
    errno_t  FT_ComplianceStop(); 

负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 负载辨识初始化
     * @return 错误码
     */
    errno_t LoadIdentifyDynFilterInit();

负载辨识初始化
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 负载辨识初始化
     * @return 错误码
     */
    errno_t LoadIdentifyDynVarInit();

负载辨识主程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 负载辨识主程序
     * @param [in] joint_torque 关节扭矩
     * @param [in] joint_pos 关节位置
     * @param [in] t 采样周期
     * @return 错误码
     */
    errno_t LoadIdentifyMain(double joint_torque[6], double joint_pos[6], double t);

获取负载辨识结果
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取负载辨识结果
     * @param [in] gain  
     * @param [out] weight 负载重量
     * @param [out] cog 负载质心
     * @return 错误码
     */
    errno_t LoadIdentifyGetResult(double gain[12], double *weight, DescTran *cog);

传动带启动、停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 传动带启动、停止
     * @param [in] status 状态，1-启动，0-停止 
     * @return 错误码
     */
    errno_t ConveyorStartEnd(uint8_t status);

记录IO检测点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 记录IO检测点
     * @return 错误码
     */
    errno_t ConveyorPointIORecord();

记录A点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 记录A点
     * @return 错误码
     */
    errno_t ConveyorPointARecord();

记录参考点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 记录参考点
     * @return 错误码
     */
    errno_t ConveyorRefPointRecord();

记录B点
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 记录B点
     * @return 错误码
     */
    errno_t ConveyorPointBRecord();

传送带工件IO检测
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 传送带工件IO检测
     * @param [in] max_t 最大检测时间，单位ms
     * @return 错误码
     */
    errno_t ConveyorIODetect(int max_t);

获取物体当前位置
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取物体当前位置
     * @param [in] mode 
     * @return 错误码
     */
    errno_t ConveyorGetTrackData(int mode);

传动带跟踪开始
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 传动带跟踪开始
     * @param [in] status 状态，1-启动，0-停止 
     * @return 错误码
     */
    errno_t ConveyorTrackStart(uint8_t status);

传动带跟踪停止
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 传动带跟踪停止
     * @return 错误码
     */
    errno_t ConveyorTrackEnd();

传动带参数配置
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief 传动带参数配置
	 * @param [in] para[0] 编码器通道 1~2
	 * @param [in] para[1] 编码器转一圈的脉冲数
	 * @param [in] para[2] 编码器转一圈传送带行走距离
	 * @param [in] para[3] 工件坐标系编号 针对跟踪运动功能选择工件坐标系编号，跟踪抓取、TPD跟踪设为0
	 * @param [in] para[4] 是否配视觉  0 不配  1 配
	 * @param [in] para[5] 速度比  针对传送带跟踪抓取选项（1-100）  其他选项默认为1 
	 * @return 错误码
	 */
    errno_t ConveyorSetParam(float param[5]);

传动带抓取点补偿
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

	/**
	 * @brief 传动带抓取点补偿
	 * @param [in] cmp 补偿位置 double[3]{x, y, z}
	 * @return 错误码
	 */
    errno_t ConveyorCatchPointComp(double cmp[3]);

直线运动
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 直线运动
     * @param [in] status 状态，1-启动，0-停止 
     * @return 错误码
     */
    errno_t TrackMoveL(char name[32], int tool, int wobj, float vel, float acc, float ovl, float blendR, uint8_t flag, uint8_t type);

获取SSH公钥
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取SSH公钥
     * @param [out] keygen 公钥
     * @return 错误码
     */
    errno_t GetSSHKeygen(char keygen[1024]);

下发SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 下发SCP指令
     * @param [in] mode 0-上传（上位机->控制器），1-下载（控制器->上位机）
     * @param [in] sshname 上位机用户名
     * @param [in] sship 上位机ip地址
     * @param [in] usr_file_url 上位机文件路径
     * @param [in] robot_file_url 机器人控制器文件路径
     * @return 错误码
     */
    errno_t SetSSHScpCmd(int mode, char sshname[32], char sship[32], char usr_file_url[128], char robot_file_url[128]);

计算指定路径下文件的MD5值
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 计算指定路径下文件的MD5值
     * @param [in] file_path 文件路径包含文件名，默认Traj文件夹路径为:"/fruser/traj/",如"/fruser/traj/trajHelix_aima_1.txt"
     * @param [out] md5 文件MD5值
     * @return 错误码
     */
    errno_t ComputeFileMD5(char file_path[256], char md5[256]);

获取机器人急停状态
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人急停状态
     * @param [out] state 急停状态，0-非急停，1-急停
     * @return 错误码  
     */
    errno_t GetRobotEmergencyStopState(uint8_t *state);

获取SDK与机器人的通讯状态
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取SDK与机器人的通讯状态
     * @param [out]  state 通讯状态，0-通讯正常，1-通讯异常
     */
    errno_t GetSDKComState(int *state);

获取安全停止信号
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取安全停止信号
     * @param [out]  si0_state 安全停止信号SI0，0-无效，1-有效
     * @param [out]  si1_state 安全停止信号SI1，0-无效，1-有效
     */
    errno_t GetSafetyStopState(uint8_t *si0_state, uint8_t *si1_state);

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
        
        /* 下面是一个传送带抓取流程 */
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

焊丝寻位开始
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  焊丝寻位开始
    * @param  [in] refPos  1-基准点 2-接触点
    * @param  [in] searchVel   寻位速度 %
    * @param  [in] searchDis  寻位距离 mm
    * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
    * @param  [in] autoBackVel  自动返回速度 %
    * @param  [in] autoBackDis  自动返回距离 mm
    * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
    * @return  错误码
    */
     errno_t WireSearchStart(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

焊丝寻位结束
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  焊丝寻位结束
      * @param  [in] refPos  1-基准点 2-接触点
      * @param  [in] searchVel   寻位速度 %
      * @param  [in] searchDis  寻位距离 mm
      * @param  [in] autoBackFlag 自动返回标志，0-不自动；-自动
      * @param  [in] autoBackVel  自动返回速度 %
      * @param  [in] autoBackDis  自动返回距离 mm
      * @param  [in] offectFlag  1-带偏移量寻位；2-示教点寻位
      * @return  错误码
      */
     errno_t WireSearchEnd(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

计算焊丝寻位偏移量
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  计算焊丝寻位偏移量
      * @param  [in] seamType  焊缝类型
      * @param  [in] method   计算方法
      * @param  [in] varNameRef 基准点1-6，“#”表示无点变量
      * @param  [in] varNameRes 接触点1-6，“#”表示无点变量
      * @param  [out] offectFlag 0-偏移量直接叠加到指令点；1-偏移量需要对指令点进行坐标变换
      * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
      * @return  错误码
      */
     errno_t GetWireSearchOffset(int seamType, int method, std::vector<std::string> varNameRef, std::vector<std::string> varNameRes, int& offectFlag, DescPose& offect);

等待焊丝寻位完成
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  等待焊丝寻位完成
      * @return  错误码
      */
     errno_t WireSearchWait(std::string varName);

焊丝寻位接触点写入数据库
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  焊丝寻位接触点写入数据库
      * @param  [in] varName  接触点名称 “RES0” ~ “RES99”
      * @param  [in] pos  接触点数据[x, y, x, a, b, c]
      * @return  错误码
      */
     errno_t SetPointToDatabase(std::string varName, DescPose pos);

示例程序
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    void Wiresearch(FRRobot* robot)
    {
    int rtn0, rtn1, rtn2 = 0;
    ExaxisPos exaxisPos = { 0, 0, 0, 0 };
    DescPose offdese = { 0, 0, 0, 0, 0, 0 };

    DescPose descStart = { 203.061, 56.768, 62.719, -177.249, 1.456, -83.597 };
    JointPos jointStart = { -127.012, -112.931, -94.078, -62.014, 87.186, 91.326 };

    DescPose descEnd = { 122.471, 55.718, 62.209, -177.207, 1.375, -76.310 };
    JointPos jointEnd = { -119.728, -113.017, -94.027, -62.061, 87.199, 91.326 };

    robot->MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese );
    robot->MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);

    DescPose descREF0A = { 147.139, -21.436, 60.717, -179.633, -3.051, -83.170 };
    JointPos jointREF0A = { -121.731, -106.193, -102.561, -64.734, 89.972, 96.171 };

    DescPose descREF0B = { 139.247, 43.721, 65.361, -179.634, -3.043, -83.170 };
    JointPos jointREF0B = { -122.364, -113.991, -90.860, -68.630, 89.933, 95.540 };

    DescPose descREF1A = { 289.747, 77.395, 58.390, -179.074, -2.901, -89.790 };
    JointPos jointREF1A = { -135.719, -119.588, -83.454, -70.245, 88.921, 88.819 };

    DescPose descREF1B = { 259.310, 79.998, 64.774, -179.073, -2.900, -89.790 };
    JointPos jointREF1B = { -133.133, -119.029, -83.326, -70.976, 89.069, 91.401 };

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
    robot->MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
    rtn1 = robot->WireSearchWait("REF0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
    robot->MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
    rtn1 = robot->WireSearchWait("REF1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
    robot->MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
    rtn1 = robot->WireSearchWait("RES0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
    robot->MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
    rtn1 = robot->WireSearchWait("RES1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
    vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
    int offectFlag = 0;
    DescPose offectPos = {0, 0, 0, 0, 0, 0};
    rtn0 = robot->GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
    robot->PointsOffsetEnable(0, &offectPos);
    robot->MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);
    robot->PointsOffsetDisable();
    }

电弧跟踪控制
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  电弧跟踪控制
      * @param  [in] flag 开关，0-关；1-开
      * @param  [in] dalayTime 滞后时间，单位ms
      * @param  [in] isLeftRight 左右偏差补偿
      * @param  [in] klr 左右调节系数(灵敏度);
      * @param  [in] tStartLr 左右开始补偿时间cyc
      * @param  [in] stepMaxLr 左右每次最大补偿量 mm
      * @param  [in] sumMaxLr 左右总计最大补偿量 mm
      * @param  [in] isUpLow 上下偏差补偿
      * @param  [in] kud 上下调节系数(灵敏度);
      * @param  [in] tStartUd 上下开始补偿时间cyc
      * @param  [in] stepMaxUd 上下每次最大补偿量 mm
      * @param  [in] sumMaxUd 上下总计最大补偿量
      * @param  [in] axisSelect 上下坐标系选择，0-摆动；1-工具；2-基座
      * @param  [in] referenceType 上下基准电流设定方式，0-反馈；1-常数
      * @param  [in] referSampleStartUd 上下基准电流采样开始计数(反馈);，cyc
      * @param  [in] referSampleCountUd 上下基准电流采样循环计数(反馈);，cyc
      * @param  [in] referenceCurrent 上下基准电流mA
      * @return  错误码
      */
     errno_t ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent);

设置电弧跟踪输入信号端口
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置电弧跟踪输入信号端口
      * @param  [in] channel 电弧跟踪AI通带选择,[0-3]
      * @return  错误码
      */
     errno_t ArcWeldTraceExtAIChannelConfig(int channel);

示例程序
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int WeldTraceControl(FRRobot* robot)
    {
    DescPose startdescPose = { -583.168, 325.637, 1.176, 75.262, 0.978, -3.571 };
    JointPos startjointPos = { -49.049, -77.203, 136.826, -189.074, -79.407, -11.811 };

    DescPose enddescPose = { -559.439, 420.491, 32.252, 77.745, 1.460, -10.130 };
    JointPos endjointPos = { -54.986, -77.639, 131.865, -185.707, -80.916, -12.218 };

    ExaxisPos exaxisPos = { 0, 0, 0, 0 };
    DescPose offdese = { 0, 0, 0, 0, 0, 0 };

    robot->WeldingSetCurrent(1, 230, 0, 0);
    robot->WeldingSetVoltage(1, 24, 0, 1);

    robot->MoveJ(&startjointPos, &startdescPose, 13, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
    robot->ArcWeldTraceControl(1, 0, 0, 0.06, 5, 5, 300, 1, -0.06, 5, 5, 300, 1, 0, 4, 1, 10);
    robot->ARCStart(1, 0, 10000);
    robot->MoveL(&endjointPos, &enddescPose, 13, 0, 5, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
    robot->ARCEnd(1, 0, 10000);

    robot->ArcWeldTraceControl(0, 0, 0, 0.06, 5, 5, 300, 1, -0.06, 5, 5, 300, 1, 0, 4, 1, 10);
    return 0;
    }

力传感器辅助拖动
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  力传感器辅助拖动
      * @param  [in] status 控制状态，0-关闭；1-开启
      * @param  [in] asaptiveFlag 自适应开启标志，0-关闭；1-开启
      * @param  [in] interfereDragFlag 干涉区拖动标志，0-关闭；1-开启
      * @param  [in] M 惯性系数
      * @param  [in] B 阻尼系数
      * @param  [in] K 刚度系数
      * @param  [in] F 拖动六维力阈值
      * @param  [in] Fmax 最大拖动力限制
      * @param  [in] Vmax 最大关节速度限制
      * @return  错误码
      */
     errno_t EndForceDragControl(int status, int asaptiveFlag, int interfereDragFlag, std::vector<double> M, std::vector<double> B, std::vector<double> K, std::vector<double> F, double Fmax, double Vmax);

示例程序
+++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
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

报错清除后力传感器自动开启
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  报错清除后力传感器自动开启
      * @param  [in] status 控制状态，0-关闭；1-开启
      * @return  错误码
      */
     errno_t SetForceSensorDragAutoFlag(int status);

示例程序
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

设置六维力和关节阻抗混合拖动开关及参数
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置六维力和关节阻抗混合拖动开关及参数
      * @param  [in] status 控制状态，0-关闭；1-开启
      * @param  [in] impedanceFlag 阻抗开启标志，0-关闭；1-开启
      * @param  [in] lamdeDain 拖动增益
      * @param  [in] KGain 刚度增益
      * @param  [in] BGain 阻尼增益
      * @param  [in] dragMaxTcpVel 拖动末端最大线速度限制
      * @param  [in] dragMaxTcpOriVel 拖动末端最大角速度限制
      * @return  错误码
      */
     errno_t ForceAndJointImpedanceStartStop(int status, int impedanceFlag, std::vector<double> lamdeDain, std::vector<double> KGain, std::vector<double> BGain, double dragMaxTcpVel, double dragMaxTcpOriVel);

示例程序
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

获取力传感器拖动开关状态
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  获取力传感器拖动开关状态
      * @param  [out] dragState 力传感器辅助拖动控制状态，0-关闭；1-开启
      * @param  [out] sixDimensionalDragState 六维力辅助拖动控制状态，0-关闭；1-开启
      * @return  错误码
      */
     errno_t GetForceAndTorqueDragState(int& dragState, int& sixDimensionalDragState);

示例程序
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

设置力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置力传感器下负载重量
      * @param  [in] weight 负载重量 kg
      * @return  错误码
      */
     errno_t SetForceSensorPayload(double weight);

设置力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置力传感器下负载质心
      * @param  [in] x 负载质心x mm
      * @param  [in] y 负载质心y mm
      * @param  [in] z 负载质心z mm
      * @return  错误码
      */
     errno_t SetForceSensorPayloadCog(double x, double y, double z);

获取力传感器下负载重量
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
     /**
      * @brief  获取力传感器下负载重量
      * @param  [in] weight 负载重量 kg
      * @return  错误码
      */
     errno_t GetForceSensorPayload(double& weight);

获取力传感器下负载质心
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  获取力传感器下负载质心
      * @param  [out] x 负载质心x mm
      * @param  [out] y 负载质心y mm
      * @param  [out] z 负载质心z mm
      * @return  错误码
      */
     errno_t GetForceSensorPayloadCog(double& x, double& y, double& z);

示例程序
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

力传感器自动校零
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  力传感器自动校零
      * @param  [out] weight 传感器质量 kg
      * @param  [out] pos 传感器质心 mm
      * @return  错误码
      */
     errno_t ForceSensorAutoComputeLoad(double& weight, DescTran& pos);

示例程序
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

设置焊接工艺曲线参数
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置焊接工艺曲线参数
      * @param  [in] id 焊接工艺编号(1-99)
      * @param  [in] startCurrent 起弧电流(A)
      * @param  [in] startVoltage 起弧电压(V)
      * @param  [in] startTime 起弧时间(ms)
      * @param  [in] weldCurrent 焊接电流(A)
      * @param  [in] weldVoltage 焊接电压(V)
      * @param  [in] endCurrent 收弧电流(A)
      * @param  [in] endVoltage 收弧电压(V)
      * @param  [in] endTime 收弧时间(ms)
      * @return  错误码
      */
     errno_t WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

获取焊接工艺曲线参数
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  获取焊接工艺曲线参数
      * @param  [in] id 焊接工艺编号(1-99)
      * @param  [out] startCurrent 起弧电流(A)
      * @param  [out] startVoltage 起弧电压(V)
      * @param  [out] startTime 起弧时间(ms)
      * @param  [out] weldCurrent 焊接电流(A)
      * @param  [out] weldVoltage 焊接电压(V)
      * @param  [out] endCurrent 收弧电流(A)
      * @param  [out] endVoltage 收弧电压(V)
      * @param  [out] endTime 收弧时间(ms)
      * @return  错误码
      */
     errno_t WeldingGetProcessParam(int id, double& startCurrent, double& startVoltage, double& startTime, double& weldCurrent, double& weldVoltage, double& endCurrent, double& endVoltage, double& endTime);

示例程序
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

末端传感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  末端传感器配置
    * @param  [in] idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param  [in] idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param  [in] idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param  [in] idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return  错误码
    */
    errno_t AxleSensorConfig(int idCompany, int idDevice, int idSoftware, int idBus);

获取末端传感器配置
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  获取末端传感器配置
      * @param  [out] idCompany 厂商，18-JUNKONG；25-HUIDE
      * @param  [out] idDevice 类型，0-JUNKONG/RYR6T.V1.0
      * @return  错误码
      */
    errno_t AxleSensorConfigGet(int& idCompany, int& idDevice);

末端传感器激活
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  末端传感器激活
      * @param  [in] actFlag 0-复位；1-激活
      * @return  错误码
      */
    errno_t AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  末端传感器寄存器写入
      * @param  [in] devAddr  设备地址编号 0-255
      * @param  [in] regHAddr 寄存器地址高8位
      * @param  [in] regLAddr 寄存器地址低8位
      * @param  [in] regNum  寄存器个数 0-255
      * @param  [in] data1 写入寄存器数值1
      * @param  [in] data2 写入寄存器数值2
      * @param  [in] isNoBlock 0-阻塞；1-非阻塞
      * @return  错误码
      */
    errno_t AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

示例程序
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

设置控制箱DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief  设置控制箱DO停止/暂停后输出是否复位
     * @param  [in] resetFlag  0-不复位；1-复位
     * @return  错误码
     */
    errno_t SetOutputResetCtlBoxDO(int resetFlag);

设置控制箱AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置控制箱AO停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetCtlBoxAO(int resetFlag);

设置末端工具DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置末端工具DO停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetAxleDO(int resetFlag);
 
设置末端工具AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置末端工具AO停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetAxleAO(int resetFlag);
 
设置扩展DO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置扩展DO停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetExtDO(int resetFlag);
 
设置扩展AO停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置扩展AO停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetExtAO(int resetFlag);
 
设置SmartTool停止/暂停后输出是否复位
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  设置SmartTool停止/暂停后输出是否复位
      * @param  [in] resetFlag  0-不复位；1-复位
      * @return  错误码
      */
    errno_t SetOutputResetSmartToolDO(int resetFlag);

示例程序
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
 
仿真摆动开始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  仿真摆动开始
      * @param  [in] weaveNum  摆动参数编号
      * @return  错误码
      */
    errno_t WeaveStartSim(int weaveNum);
 
仿真摆动结束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  仿真摆动结束
      * @param  [in] weaveNum  摆动参数编号
      * @return  错误码
      */
    errno_t WeaveEndSim(int weaveNum);
 
开始轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  开始轨迹检测预警(不运动)
      * @param  [in] weaveNum   摆动参数编号
      * @return  错误码
      */
    errno_t WeaveInspectStart(int weaveNum);
 
结束轨迹检测预警(不运动)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 结束轨迹检测预警(不运动)
      * @param  [in] weaveNum   摆动参数编号
      * @return  错误码
      */
    errno_t WeaveInspectEnd(int weaveNum);

示例程序
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
 
扩展IO-配置焊机气体检测信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机气体检测信号
      * @param  [in] DONum  气体检测信号扩展DO编号
      * @return  错误码
      */
    errno_t SetAirControlExtDoNum(int DONum);
 
扩展IO-配置焊机起弧信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机起弧信号
      * @param  [in] DONum  焊机起弧信号扩展DO编号
      * @return  错误码
      */
    errno_t SetArcStartExtDoNum(int DONum);
 
扩展IO-配置焊机反向送丝信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机反向送丝信号
      * @param  [in] DONum  反向送丝信号扩展DO编号
      * @return  错误码
      */
    errno_t SetWireReverseFeedExtDoNum(int DONum);
 
扩展IO-配置焊机正向送丝信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机正向送丝信号
      * @param  [in] DONum  正向送丝信号扩展DO编号
      * @return  错误码
      */
    errno_t SetWireForwardFeedExtDoNum(int DONum);
 
扩展IO-配置焊机起弧成功信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机起弧成功信号
      * @param  [in] DINum  起弧成功信号扩展DI编号
      * @return  错误码
      */
    errno_t SetArcDoneExtDiNum(int DINum);
 
扩展IO-配置焊机准备信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊机准备信号
      * @param  [in] DINum  焊机准备信号扩展DI编号
      * @return  错误码
      */
    errno_t SetWeldReadyExtDiNum(int DINum);
 
扩展IO-配置焊接中断恢复信号
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 扩展IO-配置焊接中断恢复信号
      * @param  [in] reWeldDINum  焊接中断后恢复焊接信号扩展DI编号
      * @param  [in] abortWeldDINum  焊接中断后退出焊接信号扩展DI编号
      * @return  错误码
      */
    errno_t SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

示例程序
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
 
设置机器人碰撞检测方法
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 设置机器人碰撞检测方法
      * @param  [in] method 碰撞检测方法：0-电流模式；1-双编码器；2-电流和双编码器同时开启
      * @return  错误码
      */
    errno_t SetCollisionDetectionMethod(int method);
 
设置静态下碰撞检测开始关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 设置静态下碰撞检测开始关闭
      * @param  [in] status 0-关闭；1-开启
      * @return  错误码
      */
    errno_t SetStaticCollisionOnOff(int status);

示例程序
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
 
关节扭矩功率检测
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 关节扭矩功率检测
      * @param  [in] status 0-关闭；1-开启
      * @param  [in] power 设定最大功率(W);
      * @return  错误码
      */
     errno_t SetPowerLimit(int status, double power);
 
关节扭矩控制开始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制开始
    * @return  错误码
    */
    errno_t ServoJTStart();
 
关节扭矩控制
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制
    * @param  [in] torque j1~j6关节扭矩，单位Nm
    * @param  [in] interval 指令周期，单位s，范围[0.001~0.008]
    * @return  错误码
    */
    errno_t ServoJT(float torque[], double interval);
 
关节扭矩控制结束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 关节扭矩控制结束
    * @return  错误码
    */
    errno_t ServoJTEnd();

示例程序
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
    robot->ServoJTStart(); //   #servoJT开始
    int error = 0;
    while (count > 0)
    {
    torques[0] = torques[0] + 0.1;//  #每次1轴增加0.1NM，运动100次
    error = robot->ServoJT(torques, 0.001);  //# 关节空间伺服模式运动
    count = count - 1;
    robot->Sleep(1);
    }

    error = robot->ServoJTEnd();  //#伺服运动结束
    return 0;
    }
 
设置机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置机器人 20004 端口反馈周期
     * @param [in] period 机器人 20004 端口反馈周期(ms)
     * @return  错误码
     */
    errno_t SetRobotRealtimeStateSamplePeriod(int period);
 
获取机器人 20004 端口反馈周期
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief  获取机器人 20004 端口反馈周期
     * @param [out] period 机器人 20004 端口反馈周期(ms)
     * @return  错误码
     */
    errno_t GetRobotRealtimeStateSamplePeriod(int& period);

示例程序
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
 
获取机器人关节驱动器温度(℃)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人关节驱动器温度(℃)
    * @return 错误码
    */
    errno_t GetJointDriverTemperature(double temperature[]);
 
获取机器人关节驱动器扭矩(Nm)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取机器人关节驱动器扭矩(Nm)
     * @return 错误码
     */
    errno_t GetJointDriverTorque(double torque[]);

示例程序
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
 
电弧追踪 + 多层多道补偿开启
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 电弧追踪 + 多层多道补偿开启
     * @return 错误码
     */
    errno_t ArcWeldTraceReplayStart();
 
电弧追踪 + 多层多道补偿关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 电弧追踪 + 多层多道补偿关闭
     * @return 错误码
     */
    errno_t ArcWeldTraceReplayEnd();
 
偏移量坐标变化-多层多道焊
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 偏移量坐标变化-多层多道焊
     * @return 错误码
     */
    errno_t MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, DescPose& offset);

示例程序
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
 
指定姿态速度开启
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿态速度开启
    * @param [in] ratio 姿态速度百分比[0-300]
    * @return  错误码
    */
    errno_t AngularSpeedStart(int ratio);
 
指定姿态速度关闭
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 指定姿态速度关闭
     * @return  错误码
     */
    errno_t AngularSpeedEnd();
 
代码示例
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
 
机器人软件升级
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 机器人软件升级
     * @param [in] filePath 软件升级包全路径
     * @param [in] block 是否阻塞至升级完成 true:阻塞；false:非阻塞
     * @return  错误码
     */
    errno_t SoftwareUpgrade(std::string filePath, bool block);
 
获取机器人软件升级状态
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  获取机器人软件升级状态
    * @param [out] state 机器人软件包升级状态(0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败)
    * @return  错误码
    */
    errno_t GetSoftwareUpgradeState(int &state);

示例程序
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
 
设置485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置485扩展轴运动加减速度
     * @param [in] acc 485扩展轴运动加速度
     * @param [in] dec 485扩展轴运动减速度
     * @return  错误码
     */
    errno_t AuxServoSetAcc(double acc, double dec);
 
设置485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置485扩展轴急停加减速度
     * @param [in] acc 485扩展轴急停加速度
     * @param [in] dec 485扩展轴急停减速度
     * @return  错误码
     */
    errno_t AuxServoSetEmergencyStopAcc(double acc, double dec);
 
获取485扩展轴运动加减速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取485扩展轴运动加减速度
     * @param [out] acc 485扩展轴运动加速度
     * @param [out] dec 485扩展轴运动减速度
     * @return  错误码
     */
    errno_t AuxServoGetAcc(double& acc, double& dec);
 
获取485扩展轴急停加减速度
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 获取485扩展轴急停加减速度
     * @param [out] acc 485扩展轴急停加速度
     * @param [out] dec 485扩展轴急停减速度
     * @return  错误码
     */
    errno_t AuxServoGetEmergencyStopAcc(double& acc, double& dec);

示例程序
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
 
可移动装置使能
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移动装置使能
     * @param enable false-去使能；true-使能
     * @return 错误码
     */
    errno_t TractorEnable(bool enable);
 
可移动装置回零
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移动装置回零
     * @return 错误码
     */
    errno_t TractorHoming();
 
可移动装置直线运动
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
     * @brief 可移动装置直线运动
     * @param distance 直线运动距离（mm）
     * @param vel 直线运动速度百分比（0-100）
     * @return 错误码
     */
    errno_t TractorMoveL(double distance, double vel);
 
可移动装置圆弧运动
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移动装置圆弧运动
     * @param radio 圆弧运动半径（mm）
     * @param angle 圆弧运动角度（°）
     * @param vel 直线运动速度百分比（0-100）
     * @return 错误码
     */
    errno_t TractorMoveC(double radio, double angle, double vel);
 
可移动装置停止运动
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 可移动装置停止运动
     * @return 错误码
     */
    errno_t TractorStop();

示例程序
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
 
设置焊丝寻位扩展IO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置焊丝寻位扩展IO端口
     * @param searchDoneDINum 焊丝寻位成功DO端口(0-127)
     * @param searchStartDONum 焊丝寻位启停控制DO端口(0-127)
     * @return 错误码
     */
    errno_t SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

示例程序
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
     robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
     robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
     rtn1 = robot->WireSearchWait("REF0");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
     robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
     rtn1 = robot->WireSearchWait("REF1");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
     robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
     rtn1 = robot->WireSearchWait("RES0");
     rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

     rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
     robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起点
     robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向点
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
 
设置焊机控制模式扩展DO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置焊机控制模式扩展DO端口
     * @param DONum 焊机控制模式DO端口(0-127)
     * @return 错误码
     */
    errno_t SetWeldMachineCtrlModeExtDoNum(int DONum);
 
设置焊机控制模式
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 设置焊机控制模式
     * @param mode 焊机控制模式;0-一元化
     * @return 错误码
     */
    errno_t SetWeldMachineCtrlMode(int mode);

示例程序
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
 
设置与机器人通讯重连参数
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief  设置与机器人通讯重连参数
    * @param  [in] enable  网络故障时使能重连 true-使能 false-不使能
    * @param  [in] reconnectTime 重连时间，单位ms
    * @param  [in] period 重连周期，单位ms
    * @return  错误码
    */
    errno_t SetReConnectParam(bool enable, int reconnectTime = 30000, int period = 50);

示例程序
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
 
开始奇异位姿保护
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 开始奇异位姿保护
	* @param [in] protectMode 奇异保护模式，0：关节模式；1-笛卡尔模式
	* @param [in] minShoulderPos 肩奇异调整范围(mm), 默认100
	* @param [in] minElbowPos 肘奇异调整范围(mm), 默认50
	* @param [in] minWristPos 腕奇异调整范围(°), 默认10
	* @return 错误码
	*/
	errno_t SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);
 
停止奇异位姿保护
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 停止奇异位姿保护
	* @return 错误码
	*/
	errno_t SingularAvoidEnd();

代码示例
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