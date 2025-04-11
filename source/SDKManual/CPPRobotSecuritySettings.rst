機器人安全設定
=================

.. toctree:: 
    :maxdepth: 5

設定碰撞等級
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 設定碰撞等級
    * @param  [in]  mode  0-等級，1-百分比
    * @param  [in]  level 碰撞閾值，等級對應範圍[],百分比對應範圍[0~1]
    * @param  [in]  config 0-不更新設定文件，1-更新設定文件
    * @return  錯誤碼
    */
    errno_t  SetAnticollision(int mode, float level[6], int config);

設定碰撞後策略
++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  設定碰撞後策略
	 * @param  [in] strategy  0-報錯暫停；1-繼續運轉;2-錯誤停止；3-重力矩模式；4-震盪對應模式；5-碰撞回彈模式
	 * @param  [in] safeTime  安全停止時間[1000 - 2000]ms
	 * @param  [in] safeDistance  安全停止距離[1-150]mm
	 * @param  [in] safetyMargin  j1-j6安全係數[1-10]
	 * @return  錯誤碼
	 */
	errno_t SetCollisionStrategy(int strategy, int safeTime, int safeDistance, int safetyMargin[]);

設定正限位
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定正限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    errno_t  SetLimitPositive(float limit[6]);

設定負限位
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定負限位
    * @param  [in] limit 六個關節位置，單位deg
    * @return  錯誤碼
    */
    errno_t  SetLimitNegative(float limit[6]);   

錯誤狀態清除
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  錯誤狀態清除
    * @return  錯誤碼
    */
    errno_t  ResetAllError();

關節摩擦力補償開關
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節摩擦力補償開關
    * @param  [in]  state  0-關，1-開
    * @return  錯誤碼
    */
    errno_t  FrictionCompensationOnOff(uint8_t state);

設定關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-正裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    errno_t  SetFrictionValue_level(float coeff[6]);

設定關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-側裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    errno_t  SetFrictionValue_wall(float coeff[6]);

設定關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-倒裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    errno_t  SetFrictionValue_ceiling(float coeff[6]);

設定關節摩擦力補償係數-自由安裝
++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  設定關節摩擦力補償係數-自由安裝
    * @param  [in]  coeff 六個關節補償係數，範圍[0~1]
    * @return  錯誤碼
    */
    errno_t  SetFrictionValue_freedom(float coeff[6]);

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

        int mode = 0;
        int config = 1;
        float level1[6] = {1.0,2.0,3.0,4.0,5.0,6.0};
        float level2[6] = {50.0,20.0,30.0,40.0,50.0,60.0};

        robot.SetAnticollision(mode, level1, config);
        mode = 1;
        robot.SetAnticollision(mode, level2, config);
        robot.SetCollisionStrategy(1);

        float plimit[6] = {170.0,80.0,150.0,80.0,170.0,160.0};
        robot.SetLimitPositive(plimit);
        float nlimit[6] = {-170.0,-260.0,-150.0,-260.0,-170.0,-160.0};
        robot.SetLimitNegative(nlimit);

        robot.ResetAllError();

        float lcoeff[6] = {0.9,0.9,0.9,0.9,0.9,0.9};
        float wcoeff[6] = {0.4,0.4,0.4,0.4,0.4,0.4};
        float ccoeff[6] = {0.6,0.6,0.6,0.6,0.6,0.6};
        float fcoeff[6] = {0.5,0.5,0.5,0.5,0.5,0.5};
        robot.FrictionCompensationOnOff(1);
        robot.SetFrictionValue_level(lcoeff);
        robot.SetFrictionValue_wall(wcoeff);
        robot.SetFrictionValue_ceiling(ccoeff);
        robot.SetFrictionValue_freedom(fcoeff);

        return 0;
    }

自訂碰撞檢測閾值功能開始、結束
++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

介面描述
************************

.. code-block:: c++
    :linenos:

    /**
     * @brief  自訂碰撞檢測閾值功能開始，設置關節端和TCP端的碰撞檢測閾值
     * @param  [in] flag 1-僅關節檢測開啟；2-僅TCP檢測開啟；3-關節和TCP檢測同時開啟
     * @param  [in] jointDetectionThreshould 關節碰撞檢測閾值 j1-j6
     * @param  [in] tcpDetectionThreshould TCP碰撞檢測閾值，xyzabc
     * @param  [in] block 0-非阻塞；1-阻塞
     * @return  錯誤碼
     */
    errno_t CustomCollisionDetectionStart(int flag, double jointDetectionThreshould[6], double tcpDetectionThreshould[6], int block);

    /**
     * @brief  自訂碰撞檢測閾值功能關閉
     * @return  錯誤碼
     */
    errno_t CustomCollisionDetectionEnd();

程式碼範例
************************

.. code-block:: c++
    :linenos:

    void CustomCollisionTest(FRRobot* robot)
    {
        DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
        DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
        ExaxisPos exaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot->MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, 2, &exaxisPos, 0, 0, &offdese);
        robot->ResetAllError();
        int safety[6] = { 5,5,5,5,5,5 };
        robot->SetCollisionStrategy(3, 1000, 150, 250, safety);
        double jointDetectionThreshould[6] = { 0.1, 0.1, 0.1, 0.1, 0.1, 0.1};
        double tcpDetectionThreshould[6] = { 60,60,60,60,60,60 };
        int rtn = robot->CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0);
        cout << "CustomCollisionDetectionStart rtn is " << rtn << endl;

        robot->MoveL(&p1Joint, &p1Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
        robot->MoveL(&p2Joint, &p2Desc, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
        rtn = robot->CustomCollisionDetectionEnd();
        cout << "CustomCollisionDetectionEnd rtn is " << rtn << endl;
    }