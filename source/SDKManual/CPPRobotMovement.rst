機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog點動
    * @param  [in]  ref 0-關節點動，2-基座標系下點動，4-工具坐標係下點動，8-工件坐標係下點動
    * @param  [in]  nb 1-關節1(或x軸)，2-關節2(或y軸)，3-關節3(或z軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param  [in]  dir 0-負方向，1-正方向
    * @param  [in]  vel 速度百分比，[0~100]
    * @param  [in]  acc 加速度百分比， [0~100]
    * @param  [in]  max_dis 單次點動最大角度，單位[°]或距離，單位[mm]
    * @return  錯誤碼
    */
    errno_t  StartJOG(uint8_t ref, uint8_t nb, uint8_t dir, float vel, float acc, float max_dis);

jog點動减速停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog點動减速停止
    * @param  [in]  ref  1-關節點動停止，3-基座標系下點動停止，5-工具坐標系下點動停止，9-工件坐標係下點動停止
    * @return  錯誤碼
    */
    errno_t  StopJOG(uint8_t ref);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    errno_t  ImmStopJOG(); 

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

        robot.StartJOG(0,1,0,20.0,20.0,30.0);   //單關節運動，StartJOG為非阻塞指令，運動狀態下接收其他運動指令（包含StartJOG）会被丢弃
        sleep(1);
        //robot.StopJOG(1)  //機器人單軸點動減速停止
        robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(0,2,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(0,3,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();
        robot.StartJOG(0,4,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();  
        robot.StartJOG(0,5,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(0,6,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 

        robot.StartJOG(2,1,0,20.0,20.0,30.0);   //基座標系下點動
        sleep(1);
        //robot.StopJOG(3)  //機器人單軸點動減速停止
        robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(2,2,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(2,3,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();
        robot.StartJOG(2,4,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();  
        robot.StartJOG(2,5,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(2,6,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 

        robot.StartJOG(4,1,0,20.0,20.0,30.0);   //工具座標系下點動
        sleep(1);
        //robot.StopJOG(5)  //機器人單軸點動減速停止
        robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(4,2,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(4,3,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();
        robot.StartJOG(4,4,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();  
        robot.StartJOG(4,5,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(4,6,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 

        robot.StartJOG(8,1,0,20.0,20.0,30.0);   //工件座標系下點動
        sleep(1);
        //robot.StopJOG(9)  //機器人單軸點動減速停止
        robot.ImmStopJOG();  //機器人單軸點動立即停止
        robot.StartJOG(8,2,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(8,3,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();
        robot.StartJOG(8,4,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG();  
        robot.StartJOG(8,5,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 
        robot.StartJOG(8,6,1,20.0,20.0,30.0);
        sleep(1);
        robot.ImmStopJOG(); 

        return 0;
    }

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    errno_t  MoveJ(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos *epos, float blendT, uint8_t offset_flag, DescPose *offset_pos);

笛卡兒空間直線運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間直線運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm    
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */   
    errno_t  MoveL(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

笛卡兒空間圓弧運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間圓弧運動
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos_p  位元位偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos_t  位元位偏移量   
    * @param  [in] ovl  速度縮放因子，範圍[0~100]    
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm    
    * @return  錯誤碼
    */      
    errno_t  MoveC(JointPos *joint_pos_p, DescPose *desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos *epos_p, uint8_t poffset_flag, DescPose *offset_pos_p,JointPos *joint_pos_t, DescPose *desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos *epos_t, uint8_t toffset_flag, DescPose *offset_pos_t,float ovl, float blendR);

笛卡兒空間整圓運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間整圓運動
    * @param  [in] joint_pos_p  路徑點1關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點1笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] joint_pos_t  路徑點2關節位置,單位deg
    * @param  [in] desc_pos_t   路徑點2笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] ovl  速度縮放因子，範圍[0~100]   
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量     
    * @return  錯誤碼
    */      
    errno_t  Circle(JointPos *joint_pos_p, DescPose *desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos *epos_p, JointPos *joint_pos_t, DescPose *desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos *epos_t, float ovl, uint8_t offset_flag, DescPose *offset_pos);

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

        JointPos j1,j2,j3,j4;
        DescPose desc_pos1,desc_pos2,desc_pos3,desc_pos4,offset_pos;
        ExaxisPos  epos;

        memset(&j1, 0, sizeof(JointPos));
        memset(&j2, 0, sizeof(JointPos));
        memset(&j3, 0, sizeof(JointPos));
        memset(&j4, 0, sizeof(JointPos));
        memset(&desc_pos1, 0, sizeof(DescPose));
        memset(&desc_pos2, 0, sizeof(DescPose));
        memset(&desc_pos3, 0, sizeof(DescPose));
        memset(&desc_pos4, 0, sizeof(DescPose));
        memset(&offset_pos, 0, sizeof(DescPose));
        memset(&epos, 0, sizeof(ExaxisPos));

        j1 = {114.578,-117.798,-97.745,-54.436,90.053,-45.216};
        desc_pos1.tran.x = -140.418;
        desc_pos1.tran.y = 619.351;
        desc_pos1.tran.z = 198.369;
        desc_pos1.rpy.rx = -179.948;
        desc_pos1.rpy.ry = 0.023;
        desc_pos1.rpy.rz = 69.793;

        j2 = {121.381,-97.108,-123.768,-45.824,89.877,-47.296};
        desc_pos2.tran.x = -127.772;
        desc_pos2.tran.y = 459.534;
        desc_pos2.tran.z = 221.274;
        desc_pos2.rpy.rx = -177.850;
        desc_pos2.rpy.ry = -2.507;
        desc_pos2.rpy.rz = 78.627;

        j3 = {138.884,-114.522,-103.933,-49.694,90.688,-47.291};
        desc_pos3.tran.x = -360.468;
        desc_pos3.tran.y = 485.600;
        desc_pos3.tran.z = 196.363;
        desc_pos3.rpy.rx = -178.239;
        desc_pos3.rpy.ry = -0.893;
        desc_pos3.rpy.rz = 96.172;

        j4 = {159.164,-96.105,-128.653,-41.170,90.704,-47.290};
        desc_pos4.tran.x = -360.303;
        desc_pos4.tran.y = 274.911;
        desc_pos4.tran.z = 203.968;
        desc_pos4.rpy.rx = -176.720;
        desc_pos4.rpy.ry = -2.514;
        desc_pos4.rpy.rz = 116.407;   

        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;

        robot.SetSpeed(20);
        
        int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        printf("movej errcode:%d\n", err1);

        int err2 = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, &epos,search,flag, &offset_pos);
        printf("movel errcode:%d\n", err2);   

        int err3 = robot.MoveC(&j3,&desc_pos3,tool,user,vel,acc,&epos,flag,&offset_pos,&j4,&desc_pos4,tool,user,vel,acc,&epos,flag,&offset_pos,ovl,blendR);
        printf("movec errcode:%d\n", err3); 

        int err4 = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        printf("movej errcode:%d\n", err4);

        int err5 = robot.Circle(&j3,&desc_pos3,tool,user,vel,acc,&epos,&j4,&desc_pos4,tool,user,vel,acc,&epos,ovl,flag,&offset_pos);
        printf("circle errcode:%d\n", err5);
        
        return 0;
    }

笛卡兒空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間螺旋線運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] ovl  速度縮放因子，範圍[0~100]    
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @param  [in] spiral_param  螺旋參數
    * @return  錯誤碼
    */
    errno_t  NewSpiral(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, ExaxisPos *epos, float ovl, uint8_t offset_flag, DescPose *offset_pos, SpiralParam spiral_param);  

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

        JointPos j;
        DescPose desc_pos, offset_pos1, offset_pos2;
        ExaxisPos  epos;
        SpiralParam sp;

        memset(&j, 0, sizeof(JointPos));
        memset(&desc_pos, 0, sizeof(DescPose));
        memset(&offset_pos1, 0, sizeof(DescPose));
        memset(&offset_pos2, 0, sizeof(DescPose));
        memset(&epos, 0, sizeof(ExaxisPos));
        memset(&sp, 0, sizeof(SpiralParam));

        j = {127.888,-101.535,-94.860,17.836,96.931,-61.325};
        offset_pos1.tran.x = 50.0;
        offset_pos1.rpy.rx = -30.0;
        offset_pos2.tran.x = 50.0;
        offset_pos2.rpy.rx = -5.0;

        sp.circle_num = 5;
        sp.circle_angle = 5.0;
        sp.rad_init = 50.0;
        sp.rad_add = 10.0;
        sp.rotaxis_add = 10.0;
        sp.rot_direction = 0;

        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = 0.0;
        uint8_t flag = 2;

        robot.SetSpeed(20);

        int ret = robot.GetForwardKin(&j, &desc_pos);  //只有關節位置的情况下，可用正運動学接口求解笛卡兒空间座標

        if(ret == 0)
        {
            int err1 = robot.MoveJ(&j, &desc_pos, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos1);
            printf("movej errcode:%d\n", err1);

            int err2 = robot.NewSpiral(&j, &desc_pos, tool, user, vel, acc, &epos, ovl, flag, &offset_pos2, sp);
            printf("newspiral errcode:%d\n", err2);
        }
        else
        {
            printf("GetForwardKin errcode:%d\n", ret);
        }

        return 0;
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
     * @return  錯誤碼
     */
    errno_t ServoMoveStart();

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
     * @return  錯誤碼
     */
    errno_t ServoMoveEnd();

關節空間伺服模式運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @return  錯誤碼
    */
    errno_t  ServoJ(JointPos *joint_pos, float acc, float vel, float cmdT, float filterT, float gain);

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

        JointPos j;

        memset(&j, 0, sizeof(JointPos));

        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.008;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 500;
        float dt = 0.1;

        int ret = robot.GetActualJointPosDegree(flag, &j);
        if(ret == 0)
        {
            while (count)
            {
                robot.ServoJ(&j, acc, vel, cmdT, filterT, gain);
                j.jPos[0] += dt;
                count -= 1;
                robot.WaitMs(cmdT*1000);
            }
        }
        else
        {
            printf("GetActualJointPosDegree errcode:%d\n", ret);
        }

        return 0;
    }

笛卡兒空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基底座標系)，1-增量運動(基底座標系)，2-增量運動(工具坐標系)
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位元姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫時不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @return  錯誤碼
    */
    errno_t  ServoCart(int mode, DescPose *desc_pose, float pos_gain[6], float acc, float vel, float cmdT, float filterT, float gain);

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

        DescPose desc_pos_dt;
        memset(&desc_pos_dt, 0, sizeof(DescPose));

        desc_pos_dt.tran.z = -0.5;
        float pos_gain[6] = {0.0,0.0,1.0,0.0,0.0,0.0};
        int mode = 2;
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.008;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 100;

        robot.SetSpeed(20);

        while (count)
        {
            robot.ServoCart(mode, &desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            robot.WaitMs(cmdT*1000);
        }

        return 0;
    }

笛卡兒空間點到點運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡兒空間點到點運動
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms 
    * @param  [in] config  關節空間配置，[-1]-參考目前關節位置解算，[0~7]-參考特定關節空間配置解算，預設為-1   
    * @return  錯誤碼
    */
    errno_t  MoveCart(DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

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

        DescPose desc_pos1, desc_pos2, desc_pos3;
        memset(&desc_pos1, 0, sizeof(DescPose));
        memset(&desc_pos2, 0, sizeof(DescPose));
        memset(&desc_pos3, 0, sizeof(DescPose));

        desc_pos1.tran.x = 75.414;
        desc_pos1.tran.y = 568.526;
        desc_pos1.tran.z = 338.135;
        desc_pos1.rpy.rx = -178.348;
        desc_pos1.rpy.ry = -0.930;
        desc_pos1.rpy.rz = 52.611;

        desc_pos2.tran.x = -273.856;
        desc_pos2.tran.y = 643.260;
        desc_pos2.tran.z = 259.235;
        desc_pos2.rpy.rx = -177.972;
        desc_pos2.rpy.ry = -1.494;
        desc_pos2.rpy.rz = 80.866;

        desc_pos3.tran.x = -423.044;
        desc_pos3.tran.y = 229.703;
        desc_pos3.tran.z = 241.080;
        desc_pos3.rpy.rx = -173.990;
        desc_pos3.rpy.ry = -5.772;
        desc_pos3.rpy.rz = 123.971;

        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        float blendT1 = 0.0;
        int config = -1;

        robot.SetSpeed(20);
        robot.MoveCart(&desc_pos1, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(&desc_pos2, tool, user, vel, acc, ovl, blendT, config);
        robot.MoveCart(&desc_pos3, tool, user, vel, acc, ovl, blendT1, config);

        return 0;
    }

樣條運動開始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    errno_t  SplineStart();

樣條運動PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間樣條運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡兒位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]   
    * @return  錯誤碼
    */
    errno_t  SplinePTP(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl);

樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    errno_t  SplineEnd();

新樣條運動開始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 新樣條運動開始
    * @param  [in] type   0-圓弧過渡，1-給定點位為路徑點
    * @param  [in] averageTime  全局平均銜接時間(ms)(10 ~  )，默認2000
    * @return  錯誤碼
    */
    errno_t NewSplineStart(int type, int averageTime=2000);

新樣條指令點
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 新樣條指令點
     * @param  [in] joint_pos  目標關節位置,單位deg
     * @param  [in] desc_pos   目標笛卡兒位姿
     * @param  [in] tool  工具座標號，範圍[0~14]
     * @param  [in] user  工件座標號，範圍[0~14]
     * @param  [in] vel  速度百分比，範圍[0~100]
     * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
     * @param  [in] ovl  速度縮放因子，範圍[0~100]
     * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm 
     * @param  [in] lastFlag 是否為最後一個點，0-否，1-是
     * @return  錯誤碼
     */  
    errno_t  NewSplinePoint(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 新樣條運動結束
     * @return  錯誤碼
     */
    errno_t  NewSplineEnd();

終止運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    errno_t  StopMotion();

暫停運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 暫停運動
     * @return  錯誤碼
     */
    errno_t  PauseMotion(); 

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

        JointPos j1,j2,j3,j4;
        DescPose desc_pos1,desc_pos2,desc_pos3,desc_pos4,offset_pos;
        ExaxisPos  epos;

        memset(&j1, 0, sizeof(JointPos));
        memset(&j2, 0, sizeof(JointPos));
        memset(&j3, 0, sizeof(JointPos));
        memset(&j4, 0, sizeof(JointPos));
        memset(&desc_pos1, 0, sizeof(DescPose));
        memset(&desc_pos2, 0, sizeof(DescPose));
        memset(&desc_pos3, 0, sizeof(DescPose));
        memset(&desc_pos4, 0, sizeof(DescPose));
        memset(&offset_pos, 0, sizeof(DescPose));
        memset(&epos, 0, sizeof(ExaxisPos));

        j1 = {114.578,-117.798,-97.745,-54.436,90.053,-45.216};
        desc_pos1.tran.x = -140.418;
        desc_pos1.tran.y = 619.351;
        desc_pos1.tran.z = 198.369;
        desc_pos1.rpy.rx = -179.948;
        desc_pos1.rpy.ry = 0.023;
        desc_pos1.rpy.rz = 69.793;

        j2 = {115.401,-105.206,-117.959,-49.727,90.054,-45.222};
        desc_pos2.tran.x = -95.586;
        desc_pos2.tran.y = 504.143;
        desc_pos2.tran.z = 186.880;
        desc_pos2.rpy.rx = 178.001;
        desc_pos2.rpy.ry = 2.091;
        desc_pos2.rpy.rz = 70.585;

        j3 = {135.609,-103.249,-120.211,-49.715,90.058,-45.219};
        desc_pos3.tran.x = -252.429;
        desc_pos3.tran.y = 428.903;
        desc_pos3.tran.z = 188.492;
        desc_pos3.rpy.rx = 177.804;
        desc_pos3.rpy.ry = 2.294;
        desc_pos3.rpy.rz = 90.782;

        j4 = {154.766,-87.036,-135.672,-49.045,90.739,-45.223};
        desc_pos4.tran.x = -277.255;
        desc_pos4.tran.y = 272.958;
        desc_pos4.tran.z = 205.452;
        desc_pos4.rpy.rx = 179.289;
        desc_pos4.rpy.ry = 1.765;
        desc_pos4.rpy.rz = 109.966;   

        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        uint8_t flag = 0;

        robot.SetSpeed(20);
        
        int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        printf("movej errcode:%d\n", err1);
        robot.SplineStart();
        robot.SplinePTP(&j1, &desc_pos1, tool, user, vel, acc, ovl);
        robot.SplinePTP(&j2, &desc_pos2, tool, user, vel, acc, ovl);
        robot.SplinePTP(&j3, &desc_pos3, tool, user, vel, acc, ovl);
        robot.SplinePTP(&j4, &desc_pos4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
        
        return 0;
    }

恢復運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:
    
    /**
     * @brief 恢復運動
     * @return  錯誤碼
     */
    errno_t  ResumeMotion();

點位整體偏移開始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件坐標系下偏移，2-工具坐標系下偏移
    * @param  [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    errno_t  PointsOffsetEnable(int flag, DescPose *offset_pos);

點位整體偏移結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    errno_t  PointsOffsetDisable();

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

        JointPos j1,j2;
        DescPose desc_pos1,desc_pos2,offset_pos,offset_pos1;
        ExaxisPos  epos;

        memset(&j1, 0, sizeof(JointPos));
        memset(&j2, 0, sizeof(JointPos));
        memset(&desc_pos1, 0, sizeof(DescPose));
        memset(&desc_pos2, 0, sizeof(DescPose));
        memset(&offset_pos, 0, sizeof(DescPose));
        memset(&offset_pos1, 0, sizeof(DescPose));
        memset(&epos, 0, sizeof(ExaxisPos));

        j1 = {114.578,-117.798,-97.745,-54.436,90.053,-45.216};
        desc_pos1.tran.x = -140.418;
        desc_pos1.tran.y = 619.351;
        desc_pos1.tran.z = 198.369;
        desc_pos1.rpy.rx = -179.948;
        desc_pos1.rpy.ry = 0.023;
        desc_pos1.rpy.rz = 69.793;

        j2 = {115.401,-105.206,-117.959,-49.727,90.054,-45.222};
        desc_pos2.tran.x = -95.586;
        desc_pos2.tran.y = 504.143;
        desc_pos2.tran.z = 186.880;
        desc_pos2.rpy.rx = 178.001;
        desc_pos2.rpy.ry = 2.091;
        desc_pos2.rpy.rz = 70.585;

        offset_pos1.tran.x = 100.0;
        offset_pos1.tran.y = 100.0;
        offset_pos1.tran.z = 100.0;
        offset_pos1.rpy.rx = 5.0;
        offset_pos1.rpy.ry = 5.0;
        offset_pos1.rpy.rz = 5.0;    

        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float blendT = -1.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        int type = 0;

        robot.SetSpeed(20);
        
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        sleep(2);
        robot.PointsOffsetEnable(type, &offset_pos1);
        robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT,flag, &offset_pos);
        robot.PointsOffsetDisable();

        return 0;
    }

控制箱AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飛拍開始
    * @param [in] AONum 控制箱AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，預設100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，預設為20%，範圍[0-100]
    * @return 錯誤碼
    */
    errno_t MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飛拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    errno_t MoveAOStop();
    
末端AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飛拍開始
    * @param [in] AONum 末端AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，預設100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，預設為20%，範圍[0-100]
    * @return 錯誤碼
    */
    errno_t MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飛拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    errno_t MoveToolAOStop();

代碼範例
************
.. code-block:: c++
    :linenos:

    int testMoveAO(FRRobot* robot)
    {
        int tool = 0;
        int user = 0;
        float vel = 50.0;
        float acc = 50.0;
        float ovl = 50.0;
        float blendT = -1.0;
        float blendR = -1;
        uint8_t flag = 0;
        int type = 1;

        JointPos j1, j2, j3, j4;
        DescPose desc_pos1, desc_pos2, desc_pos3, desc_pos4, offset_pos = {};
        ExaxisPos  epos = {};

        robot->GetActualJointPosDegree(1, &j1);
        robot->GetActualTCPPose(1, &desc_pos1);

        /*j1.jPos[0] = 50.344;
        j1.jPos[1] = -68.336;
        j1.jPos[2] = 94.778;
        j1.jPos[3] = -117.014;
        j1.jPos[4] = -92.567;
        j1.jPos[5] = 73.231;
        desc_pos1.tran.x = -294.878;
        desc_pos1.tran.y = -552.449;
        desc_pos1.tran.z = 272.138;
        desc_pos1.rpy.rx = -177.393;
        desc_pos1.rpy.ry = -0.216;
        desc_pos1.rpy.rz = 67.096;*/

        j2.jPos[0] = 66.022;
        j2.jPos[1] = -74.633;
        j2.jPos[2] = 104.187;
        j2.jPos[3] = -121.965;
        j2.jPos[4] = -92.643;
        j2.jPos[5] = 73.233;
        desc_pos2.tran.x = -114.128;
        desc_pos2.tran.y = -564.708;
        desc_pos2.tran.z = 271.102;
        desc_pos2.rpy.rx = -176.799;
        desc_pos2.rpy.ry = 1.479;
        desc_pos2.rpy.rz = 82.756;

        j3.jPos[0] = 79.546;
        j3.jPos[1] = -83.13;
        j3.jPos[2] = 113.465;
        j3.jPos[3] = -121.974;
        j3.jPos[4] = -92.635;
        j3.jPos[5] = 73.234;
        desc_pos3.tran.x = 33.176;
        desc_pos3.tran.y = -511.069;
        desc_pos3.tran.z = 277.399;
        desc_pos3.rpy.rx = -177.015;
        desc_pos3.rpy.ry = 0.784;
        desc_pos3.rpy.rz = 96.289;

        j4.jPos[0] = 94.565;
        j4.jPos[1] = -73.426;
        j4.jPos[2] = 103.309;
        j4.jPos[3] = -123.204;
        j4.jPos[4] = -92.3;
        j4.jPos[5] = 73.235;
        desc_pos4.tran.x = 171.039;
        desc_pos4.tran.y = -559.579;
        desc_pos4.tran.z = 268.912;
        desc_pos4.rpy.rx = -176.829;
        desc_pos4.rpy.ry = 2.545;
        desc_pos4.rpy.rz = 111.329;
        
        int err1 = 0;
        err1 = robot->MoveAOStart(0, 100, 80, 1);
        cout << "err num is " << err1 << endl;
        //robot->MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        //robot->MoveL(&j1, &desc_pos1, tool, user, vel, acc, ovl, blendR, &epos, 0, flag, &offset_pos);
        //robot->MoveC(&j1, &desc_pos1, 0, 0, 100, 100, &epos, 0, &offset_pos, &j2, &desc_pos2, 0, 0, 100, 100, &epos, 0, &offset_pos, 100, 0);
        //robot->Circle(&j1, &desc_pos1, 0, 0, 100, 100, &epos, &j2, &desc_pos2, 0, 0, 100, 100, &epos, 100, 0, &offset_pos);
        //robot->SplineStart();
        //robot->SplinePTP(&j1, &desc_pos1, 0, 0, 100, 100, 100);
        //robot->SplinePTP(&j2, &desc_pos2, 0, 0, 100, 100, 100);
        //robot->SplinePTP(&j3, &desc_pos3, 0, 0, 100, 100, 100);
        //robot->SplinePTP(&j4, &desc_pos4, 0, 0, 100, 100, 100);
        //robot->SplineEnd();

        //robot->NewSplineStart(0, 5000);
        //robot->NewSplinePoint(&j1, &desc_pos1, 0, 0, 100, 100, 100, 5, 0);
        //robot->NewSplinePoint(&j2, &desc_pos2, 0, 0, 100, 100, 100, 5, 0);
        //robot->NewSplinePoint(&j3, &desc_pos3, 0, 0, 100, 100, 100, 5, 0);
        //robot->NewSplinePoint(&j4, &desc_pos4, 0, 0, 100, 100, 100, 5, 1);
        //robot->NewSplineEnd();
        int count = 1000;
        while (count > 0)
        {
            robot->ServoJ(&j1, 0, 0, 0.008f, 0, 0);
            j1.jPos[0] += 0.02;//0關節位置增加
            count -= 1;
        }
        robot->MoveAOStop();
        
        return 0;
    }

開始Ptp運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7
    
.. code-block:: c++
    :linenos:

    /**
	* @brief 開始Ptp運動FIR濾波
	* @param [in] maxAcc 最大加速度極值(deg/s2)
	* @return 錯誤碼
	*/
	errno_t PtpFIRPlanningStart(double maxAcc);

關閉Ptp運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 關閉Ptp運動FIR濾波
	* @return 錯誤碼
	*/
	errno_t PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 開始LIN、ARC運動FIR濾波
	* @param [in] maxAccLin 線加速度極值(mm/s2)
	* @param [in] maxAccDeg 角加速度極值(deg/s2)
	* @param [in] maxJerkLin 線加加速度極值(mm/s3)
	* @param [in] maxJerkDeg 角加加速度極值(deg/s3)
	* @return 錯誤碼
	*/
	errno_t LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

關閉LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 關閉LIN、ARC運動FIR濾波
	* @return 錯誤碼
	*/
	errno_t LinArcFIRPlanningEnd();

加速度平滑開啟
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑開啟
    * @param [in] saveFlag 是否斷電保存
    * @return 錯誤碼
    */
    errno_t AccSmoothStart(bool saveFlag);

加速度平滑關閉
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑關閉
    * @param [in] saveFlag 是否斷電保存
    * @return 錯誤碼
    */
    errno_t AccSmoothEnd(bool saveFlag);

代碼示例
*****************************

.. code-block:: c++
    :linenos:

    void TestAccSmoothJ(FRRobot* robot)
    {
      DescPose startdescPose(88.739, -527.617, 514.939, -179.039, 1.494, 70.209);
      JointPos startjointPos(88.927, -85.834, 80.289, -85.561, -91.388, 108.718);

      DescPose enddescPose(-433.125, -334.428, 497.139, -179.723, -0.745, 8.437);
      JointPos endjointPos(27.036, -83.909, 80.284, -85.579, -90.027, 108.604);

      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      int rtn = robot->AccSmoothStart(0);
      cout << "AccSmoothStart rtn is " << rtn << endl;
      robot->MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot->MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
      rtn = robot->AccSmoothEnd(0);
      cout << "AccSmoothEnd rtn is " << rtn << endl;
    }