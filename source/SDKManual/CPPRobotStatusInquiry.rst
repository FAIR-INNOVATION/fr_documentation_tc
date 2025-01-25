機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

取得機器人安裝角度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得機器人安裝角度
    * @param  [out] yangle 傾斜角
    * @param  [out] zangle 旋轉角
    * @return  錯誤碼
    */
    errno_t  GetRobotInstallAngle(float *yangle, float *zangle);

取得系統變數值
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得系統變數值
    * @param  [in] id 系統變數編號，範圍[1~20]
    * @param  [out] value  系統變數值
    * @return  錯誤碼
    */
    errno_t  GetSysVarValue(int id, float *value);

取得目前關節位置(角度)
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前關節位置(角度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位deg
    * @return  錯誤碼
    */
    errno_t  GetActualJointPosDegree(uint8_t flag, JointPos *jPos);

取得目前關節位置(弧度)
+++++++++++++++++++++++++++++++++

.. deprecated:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前關節位置(弧度)
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] jPos 六個關節位置，單位rad
    * @return  錯誤碼
    */   
    errno_t  GetActualJointPosRadian(uint8_t flag, JointPos *jPos);

取得關節回饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得關節回饋速度-deg/s
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed 六個關節速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualJointSpeedsDegree(uint8_t flag, float speed[6]);

取得關節回饋加速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得關節回饋加速度-deg/s^2
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] acc 六個關節加速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualJointAccDegree(uint8_t flag, float acc[6]);   

取得TCP指令速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得TCP指令速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] tcp_speed 線性速度
     * @param  [out] ori_speed 姿態速度
     * @return  錯誤碼 
     */
    errno_t  GetTargetTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

獲取TCP回饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP回饋速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] tcp_speed 線性速度
     * @param  [out] ori_speed 姿態速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualTCPCompositeSpeed(uint8_t flag, float *tcp_speed, float *ori_speed);

取得TCP指令速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得TCP指令速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed [x,y,z,rx,ry,rz]速度
     * @return  錯誤碼 
     */ 
    errno_t  GetTargetTCPSpeed(uint8_t flag, float speed[6]);

獲取TCP回饋速度
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  獲取TCP回饋速度
     * @param  [in] flag 0-阻塞，1-非阻塞
     * @param  [out] speed [x,y,z,rx,ry,rz]速度
     * @return  錯誤碼 
     */ 
    errno_t  GetActualTCPSpeed(uint8_t flag, float speed[6]);

取得當前工具位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得當前工具位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  工具位姿
    * @return  錯誤碼
    */
    errno_t  GetActualTCPPose(uint8_t flag, DescPose *desc_pos);

取得目前工具坐標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前工具坐標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工具座標系編號
    * @return  錯誤碼
    */
    errno_t  GetActualTCPNum(uint8_t flag, int *id);

取得目前工件坐標系編號
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前工件坐標系編號
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] id  工件座標系編號
    * @return  錯誤碼
    */
    errno_t  GetActualWObjNum(uint8_t flag, int *id);  

取得目前末端法蘭位姿
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前末端法蘭位姿
    * @param  [in] flag  0-阻塞，1-非阻塞
    * @param  [out] desc_pos  法蘭位姿
    * @return  錯誤碼
    */
    errno_t  GetActualToolFlangePose(uint8_t flag, DescPose *desc_pos);  

逆運動學求解
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] config 關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */
    errno_t  GetInverseKin(int type, DescPose *desc_pos, int config, JointPos *joint_pos);

逆運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置求解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] joint_pos 關節位置
    * @return  錯誤碼
    */   
    errno_t  GetInverseKinRef(int type, DescPose *desc_pos, JointPos *joint_pos_ref, JointPos *joint_pos);

逆運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  逆運動學求解，參考指定關節位置判断是否有解
    * @param  [in] type 0-絕對位姿(基底座標系)，1-增量位姿(基底座標系)，2-增量位姿(工具座標系)
    * @param  [in] desc_pos 笛卡兒位姿
    * @param  [in] joint_pos_ref 參考關節位置
    * @param  [out] result 0-無解，1-有解
    * @return  錯誤碼
    */   
    errno_t  GetInverseKinHasSolution(int type, DescPose *desc_pos, JointPos *joint_pos_ref, uint8_t *result);

正運動學求解
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  正運動學求解
    * @param  [in] joint_pos 關節位置
    * @param  [out] desc_pos 笛卡兒位姿
    * @return  錯誤碼
    */
    errno_t  GetForwardKin(JointPos *joint_pos, DescPose *desc_pos);

取得當前關節轉矩
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 取得當前關節轉矩
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] torques 關節轉矩
    * @return  錯誤碼
    */
    errno_t  GetJointTorques(uint8_t flag, float torques[6]);

取得目前負載的重量
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前負載的重量
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] weight 負載重量，單位kg
    * @return  錯誤碼
    */
    errno_t  GetTargetPayload(uint8_t flag, float *weight);

取得目前負載的質心
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得目前負載的質心
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] cog 負載質心，單位mm
    * @return  錯誤碼
    */   
    errno_t  GetTargetPayloadCog(uint8_t flag, DescTran *cog);

獲取當前工具坐標系
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取當前工具坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工具坐標系位姿
    * @return  錯誤碼
    */
    errno_t  GetTCPOffset(uint8_t flag, DescPose *desc_pos);

取得當前工件坐標系
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得當前工件坐標系
    * @param  [in] flag 0-阻塞，1-非阻塞
    * @param  [out] desc_pos 工件座標系位姿
    * @return  錯誤碼
    */   
    errno_t  GetWObjOffset(uint8_t flag, DescPose *desc_pos);

取得關節軟限位角度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得關節軟限位角度
    * @param  [in] flag 0-阻塞，1-非阻塞    
    * @param  [out] negative  負限位角度，單位deg
    * @param  [out] positive  正限位角度，單位deg
    * @return  錯誤碼
    */
    errno_t  GetJointSoftLimitDeg(uint8_t flag, float negative[6], float positive[6]);

取得系統時間
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得系統時間
    * @param  [out] t_ms 單位ms
    * @return  錯誤碼
    */
    errno_t  GetSystemClock(float *t_ms);

取得機器人當前關節配置
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得機器人當前關節位置
    * @param  [out]  config  關節空間配置，範圍[0~7]
    * @return  錯誤碼
    */
    errno_t  GetRobotCurJointsConfig(int *config);

取得當前速度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得機器人預設速度
    * @param  [out]  vel  速度，單位mm/s
    * @return  錯誤碼
    */   
    errno_t  GetDefaultTransVel(float *vel);

查詢機器人運動是否完成
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢機器人運動是否完成
    * @param  [out]  state  0-未完成，1-完成
    * @return  錯誤碼
    */   
    errno_t  GetRobotMotionDone(uint8_t *state);

代碼範例
+++++++++++
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

        float yangle, zangle;
        int flag = 0;
        JointPos j_deg, j_rad;
        DescPose tcp, flange, tcp_offset, wobj_offset;
        DescTran cog;
        int id;
        float torques[6] = {0.0};
        float weight;
        float neg_deg[6]={0.0},pos_deg[6]={0.0};
        float t_ms;
        int config;
        float vel;

        memset(&j_deg, 0, sizeof(JointPos));
        memset(&j_rad, 0, sizeof(JointPos));
        memset(&tcp, 0, sizeof(DescPose));
        memset(&flange, 0, sizeof(DescPose));
        memset(&tcp_offset, 0, sizeof(DescPose));
        memset(&wobj_offset, 0, sizeof(DescPose));
        memset(&cog, 0, sizeof(DescTran));

        robot.GetRobotInstallAngle(&yangle, &zangle);
        printf("yangle:%f,zangle:%f\n", yangle, zangle);

        robot.GetActualJointPosDegree(flag, &j_deg);
        printf("joint pos deg:%f,%f,%f,%f,%f,%f\n", j_deg.jPos[0],j_deg.jPos[1],j_deg.jPos[2],j_deg.jPos[3],j_deg.jPos[4],j_deg.jPos[5]);

        robot.GetActualJointPosRadian(flag, &j_rad);
        printf("joint pos rad:%f,%f,%f,%f,%f,%f\n", j_rad.jPos[0],j_rad.jPos[1],j_rad.jPos[2],j_rad.jPos[3],j_rad.jPos[4],j_rad.jPos[5]);   

        robot.GetActualTCPPose(flag, &tcp);
        printf("tcp pose:%f,%f,%f,%f,%f,%f\n", tcp.tran.x, tcp.tran.y, tcp.tran.z, tcp.rpy.rx, tcp.rpy.ry, tcp.rpy.rz); 

        robot.GetActualToolFlangePose(flag, &flange);
        printf("flange pose:%f,%f,%f,%f,%f,%f\n", flange.tran.x, flange.tran.y, flange.tran.z, flange.rpy.rx, flange.rpy.ry, flange.rpy.rz); 

        robot.GetActualTCPNum(flag, &id);
        printf("tcp num:%d\n", id);

        robot.GetActualWObjNum(flag, &id);
        printf("wobj num:%d\n", id);  

        robot.GetJointTorques(flag, torques);
        printf("torques:%f,%f,%f,%f,%f,%f\n", torques[0],torques[1],torques[2],torques[3],torques[4],torques[5]); 

        robot.GetTargetPayload(flag, &weight);
        printf("payload weight:%f\n", weight);

        robot.GetTargetPayloadCog(flag, &cog);
        printf("payload cog:%f,%f,%f\n",cog.x, cog.y, cog.z);

        robot.GetTCPOffset(flag, &tcp_offset);
        printf("tcp offset:%f,%f,%f,%f,%f,%f\n", tcp_offset.tran.x,tcp_offset.tran.y,tcp_offset.tran.z,tcp_offset.rpy.rx,tcp_offset.rpy.ry,tcp_offset.rpy.rz);

        robot.GetWObjOffset(flag, &wobj_offset);
        printf("wobj offset:%f,%f,%f,%f,%f,%f\n", wobj_offset.tran.x,wobj_offset.tran.y,wobj_offset.tran.z,wobj_offset.rpy.rx,wobj_offset.rpy.ry,wobj_offset.rpy.rz);

        robot.GetJointSoftLimitDeg(flag, neg_deg, pos_deg);
        printf("neg limit deg:%f,%f,%f,%f,%f,%f\n",neg_deg[0],neg_deg[1],neg_deg[2],neg_deg[3],neg_deg[4],neg_deg[5]);
        printf("pos limit deg:%f,%f,%f,%f,%f,%f\n",pos_deg[0],pos_deg[1],pos_deg[2],pos_deg[3],pos_deg[4],pos_deg[5]);

        robot.GetSystemClock(&t_ms);
        printf("system clock:%f\n", t_ms);

        robot.GetRobotCurJointsConfig(&config);
        printf("joint config:%d\n", config);

        robot.GetDefaultTransVel(&vel);
        printf("trans vel:%f\n", vel);

        return 0;
    }

查詢機器人錯誤碼
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查詢機器人錯誤碼
     * @param  [out]  maincode  主錯誤碼
     * @param  [out]  subcode   子錯誤碼
     * @return  錯誤碼
     */ 
    errno_t  GetRobotErrorCode(int *maincode, int *subcode);

查詢機器人示教管理點位數據
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查詢機器人示教管理點位數據
     * @param  [in]  name  點位名
     * @param  [out]  data   點位數據
     * @return  錯誤碼
     */ 
    errno_t  GetRobotTeachingPoint(char name[64], float data[20]);

查詢機器人運動隊列緩存長度
++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  查詢機器人運動隊列緩存長度
     * @param  [out]  len 緩存長度
     * @return  錯誤碼
     */ 
    errno_t  GetMotionQueueLength(int *len);

代碼範例
++++++++++++++++++++++++++++++++++++
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

    using namespace std;

    int main(void)
    {
        FRRobot robot;
        robot.RPC("192.168.58.2");

        uint8_t result = 0;
        int retval = 0;
        float joint_speed_deg[6] = {0};

        retval = robot.GetActualJointSpeedsDegree(1, joint_speed_deg);
        printf("GetActualJointSpeedsDegree retval is: %d \n", retval);
        printf("joint degree speed is: %f, %f, %f, %f, %f, %f \n", joint_speed_deg[0], joint_speed_deg[1], joint_speed_deg[2], joint_speed_deg[3], joint_speed_deg[4], joint_speed_deg[5]);

        float joint_acc_deg[6] = {0};
        retval = robot.GetActualJointAccDegree(1, joint_acc_deg);
        printf("GetActualJointAccDegree retval is: %d \n", retval);
        printf("joint degree acc is: %f, %f, %f, %f, %f, %f \n", joint_acc_deg[0], joint_acc_deg[1], joint_acc_deg[2], joint_acc_deg[3], joint_acc_deg[4], joint_acc_deg[5]);

        float tcp_speed = 0;
        float ori_speed = 0;
        retval = robot.GetTargetTCPCompositeSpeed(1, &tcp_speed, &ori_speed);
        printf("GetTargetTCPCompositeSpeed retval is: %d \n", retval);
        printf("tcp_speed is:%f, ori_speed is: %f \n", tcp_speed, ori_speed);

        retval = robot.GetActualTCPCompositeSpeed(1, &tcp_speed, &ori_speed);
        printf("GetActualTCPCompositeSpeed retval is: %d \n", retval);
        printf("tcp_speed is:%f, ori_speed is: %f \n", tcp_speed, ori_speed);

        float targer_tcp_speed[6] = {0};
        retval = robot.GetTargetTCPSpeed(1, targer_tcp_speed);
        printf("GetTargetTCPSpeed retval is: %d \n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", targer_tcp_speed[0], targer_tcp_speed[1], targer_tcp_speed[2], targer_tcp_speed[3], targer_tcp_speed[4], targer_tcp_speed[5]);

        float actual_tcp_speed[6] = {0};
        robot.GetActualTCPSpeed(1, actual_tcp_speed);
        printf("GetActualTCPSpeed retval is: %d \n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", actual_tcp_speed[0], actual_tcp_speed[1], actual_tcp_speed[2], actual_tcp_speed[3], actual_tcp_speed[4], actual_tcp_speed[5]);

        JointPos j;
        DescPose desc_pos, offset_pos1, offset_pos2;

        memset(&j, 0, sizeof(JointPos));
        memset(&desc_pos, 0, sizeof(DescPose));
        memset(&offset_pos1, 0, sizeof(DescPose));
        memset(&offset_pos2, 0, sizeof(DescPose));

        j = {{-39.666, -96.491, -79.531, -94.251, 90.961, -58.714}};
        offset_pos1.tran.x = 10.0;
        offset_pos1.rpy.rx = -10.0;
        offset_pos2.tran.x = 30.0;
        offset_pos2.rpy.rx = -5.0;

        retval = 0;
        retval = robot.GetForwardKin(&j, &desc_pos); // 只有關節位置的情况下，可用正運動学接口求解笛卡兒空间座標
        printf("GetForwardKin ret is: %d \n", retval);
        printf("GetForwardKin result:%f,%f,%f,%f,%f,%f\n", desc_pos.tran.x, desc_pos.tran.y, desc_pos.tran.z, desc_pos.rpy.rx, desc_pos.rpy.ry, desc_pos.rpy.rz);

        retval = 0;
        JointPos start_joint_pose;
        memset(&start_joint_pose, 0, sizeof(JointPos));
        retval = robot.GetInverseKinRef(0, &desc_pos, &j, &start_joint_pose);
        printf("GetInverseKinRef retval is: %d \n", retval);
        printf("joint is: %f, %f, %f,%f, %f, %f\n", start_joint_pose.jPos[0], start_joint_pose.jPos[1], start_joint_pose.jPos[2], start_joint_pose.jPos[3], start_joint_pose.jPos[4], start_joint_pose.jPos[5]);

        retval = 0;
        retval = robot.GetInverseKinHasSolution(1, &offset_pos1, &j, &result); // 根据參考關節座標，判断目標位姿是否有解
        printf("GetInverseKinHasSolution ret: %d\n", result);
        if (0 == result)
        {
            printf("pose1 can not be solved\n");
        }

        retval = 0;
        retval = robot.GetInverseKin(1, &offset_pos1, -1, &start_joint_pose);
        printf("GetInverseKin retval is: %d \n", retval);
        printf("GetInverseKin result is: %f, %f, %f, %f, %f, %f\n", start_joint_pose.jPos[0], start_joint_pose.jPos[1], start_joint_pose.jPos[2], start_joint_pose.jPos[3], start_joint_pose.jPos[4], start_joint_pose.jPos[5]);

        int main_code = 0;
        int sub_code = 0;
        retval = 0;
        retval = robot.GetRobotErrorCode(&main_code, &sub_code);
        printf("GetRobotMotionDone retval is: %d , amin code is:%d, sub code is: %d\n", retval, main_code, sub_code);

        char name[64] = "F1";
        float data[20] = {0};
        int ret = robot.GetRobotTeachingPoint(name, data);
        printf(" %d name is: %s \n", ret, name);
        for (int i = 0; i < 20; i++)
        {
            printf("data is: %f \n", data[i]);
        }

        int que_len = 0;
        retval = 0;
        retval = robot.GetMotionQueueLength(&que_len);
        printf("GetMotionQueueLength retval is: %d, queue length is: %d \n", retval, que_len);
    }