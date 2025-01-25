機器人週邊
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  配置夾爪
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    errno_t  SetGripperConfig(int company, int device, int softvesion, int bus);

取得夾爪配置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  取得夾爪配置
    * @param  [in] company  夾爪廠商，待定
    * @param  [in] device  設備號，暫不使用，預設為0
    * @param  [in] softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    errno_t  GetGripperConfig(int *company, int *device, int *softvesion, int *bus);

啟動夾爪
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  啟動夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    errno_t  ActGripper(int index, uint8_t act);

控制夾爪
++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
	 * @brief  控制夾爪
	 * @param  [in] index  夾爪編號
	 * @param  [in] pos  位置百分比，範圍[0~100]
	 * @param  [in] vel  速度百分比，範圍[0~100]
	 * @param  [in] force  力矩百分比，範圍[0~100]
	 * @param  [in] max_time  最大等待時間，範圍[0~30000]，單位ms
	 * @param  [in] block  0-阻塞，1-非阻塞
	 * @param  [in] type 夾爪類型，0-平行夾爪；1-旋轉夾爪
	 * @param  [in] rotNum 旋轉圈數
	 * @param  [in] rotVel 旋轉速度百分比[0-100]
	 * @param  [in] rotTorque 旋轉力矩百分比[0-100]
	 * @return  錯誤碼
	 */
	errno_t MoveGripper(int index, int pos, int vel, int force, int max_time, uint8_t block, int type, double rotNum, int rotVel, int rotTorque);



取得夾爪運動狀態
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪運動狀態
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] staus  0-運動未完成，1-運動完成
     * @return  錯誤碼
     */
    errno_t  GetGripperMotionDone(uint16_t *fault, uint8_t *status);

取得夾爪啟動狀態
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪啟動狀態
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] status  bit0~bit15对应夾爪編號0~15，bit=0為未激活，bit=1為激活
     * @return  錯誤碼
     */
    errno_t  GetGripperActivateStatus(uint16_t *fault, uint16_t *status);

取得夾爪位置
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪位置
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] position  位置百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurPosition(uint16_t *fault, uint8_t *position);

取得夾爪速度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪速度
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] speed  速度百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurSpeed(uint16_t *fault, int8_t *speed);

取得夾爪電流
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪電流
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] current  電流百分比，範圍0~100%
     * @return  錯誤碼
     */
    errno_t  GetGripperCurCurrent(uint16_t *fault, int8_t *current);

取得夾爪電壓
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪電壓
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] voltage  電壓,單位0.1V
     * @return  錯誤碼
     */
    errno_t  GetGripperVoltage(uint16_t *fault, int *voltage);

取得夾爪溫度
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  取得夾爪溫度
     * @param  [out] fault  0-無錯誤，1-有錯誤
     * @param  [out] temp  溫度，單位℃
     * @return  錯誤碼
     */
    errno_t  GetGripperTemp(uint16_t *fault, int *temp);

計算預抓取點-視覺
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算預抓取點-視覺
     * @param  [in] desc_pos  抓取點笛卡爾位姿
     * @param  [in] zlength   z軸偏移量
     * @param  [in] zangle    繞z軸旋轉偏移量
     * @return  錯誤碼 
     */
    errno_t  ComputePrePick(DescPose *desc_pos, double zlength, double zangle, DescPose *pre_pos);

計算撤退點-視覺
++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief  計算撤退點-視覺
     * @param  [in] desc_pos  抓取點笛卡爾位姿
     * @param  [in] zlength   z軸偏移量
     * @param  [in] zangle    繞z軸旋轉偏移量
     * @return  錯誤碼 
     */
    errno_t  ComputePostPick(DescPose *desc_pos, double zlength, double zangle, DescPose *post_pos);

代碼範例
++++++++++++++++
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

    using namespace std;

    int main(void)
    {
        FRRobot robot; 
        robot.RPC("192.168.58.2"); 

        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int index = 1;
        int act = 0;
        int max_time = 30000;
        uint8_t block = 0;
        uint8_t status;
        uint16_t fault;
        uint16_t active_status = 0;
        uint8_t current_pos = 0;
        int8_t current = 0;
        int voltage = 0;
        int temp = 0;
        int8_t speed = 0;

        robot.SetGripperConfig(company, device, softversion, bus);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        robot.GetGripperConfig(&company, &device, &softversion, &bus);
        printf("gripper config:%d,%d,%d,%d\n", company, device, softversion, bus);

        robot.ActGripper(index, act);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        act = 1;
        robot.ActGripper(index, act);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));

        robot.MoveGripper(index, 100, 50, 50, max_time, block);
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        robot.MoveGripper(index, 0, 50, 0, max_time, block);

        robot.GetGripperMotionDone(&fault, &status);
        printf("motion status:%u,%u\n", fault, status);

        robot.GetGripperActivateStatus(&fault, &active_status);
        printf("gripper active fault is: %u, status is: %u\n", fault, active_status);

        robot.GetGripperCurPosition(&fault, &current_pos);
        printf("fault is:%u, current position is: %u\n", fault, current_pos);

        robot.GetGripperCurCurrent(&fault, &current);
        printf("fault is:%u, current current is: %d\n", fault, current);

        robot.GetGripperVoltage(&fault, &voltage);
        printf("fault is:%u, current voltage is: %d \n", fault, voltage);

        robot.GetGripperTemp(&fault, &temp);
        printf("fault is:%u, current temperature is: %d\n", fault, temp);

        robot.GetGripperCurSpeed(&fault, &speed);
        printf("fault is:%u, current speed is: %d\n", fault, speed);

        int retval = 0;
        DescPose prepick_pose;
        DescPose postpick_pose;
        memset(&prepick_pose, 0, sizeof(DescPose));
        memset(&postpick_pose, 0, sizeof(DescPose));

        DescPose desc_p1;
        desc_p1.tran.x = -351.553;
        desc_p1.tran.y = 87.913;
        desc_p1.tran.z = 354.175;
        desc_p1.rpy.rx = -179.680;
        desc_p1.rpy.ry = -0.133;
        desc_p1.rpy.rz = 2.472;

        DescPose desc_p2;
        desc_p2.tran.x = -351.535;
        desc_p2.tran.y = -247.222;
        desc_p2.tran.z = 354.173;
        desc_p2.rpy.rx = -179.680;
        desc_p2.rpy.ry = -0.137;
        desc_p2.rpy.rz = 2.473;

        retval = robot.ComputePrePick(&desc_p1, 10, 0, &prepick_pose);
        printf("ComputePrePick retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", prepick_pose.tran.x, prepick_pose.tran.y, prepick_pose.tran.z, prepick_pose.rpy.rx, prepick_pose.rpy.ry, prepick_pose.rpy.rz);

        retval = robot.ComputePostPick(&desc_p2, -10, 0, &postpick_pose);
        printf("ComputePostPick retval is: %d\n", retval);
        printf("xyz is: %f, %f, %f; rpy is: %f, %f, %f\n", postpick_pose.tran.x, postpick_pose.tran.y, postpick_pose.tran.z, postpick_pose.rpy.rx, postpick_pose.rpy.ry, postpick_pose.rpy.rz);

        return 0;
    }

焊接開始
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接開始
    * @param [in] ioType io 類型 0-控制器IO；1-擴展IO
    * @param [in] arcNum 焊機設定檔編號
    * @param [in] timeout 起弧超時時間
    * @return 錯誤碼
    */
    errno_t ARCStart(int ioType, int arcNum, int timeout);

焊接結束
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接結束
    * @param [in] ioType io 類型 0-控制器IO；1-擴展IO
    * @param [in] arcNum 焊機設定檔編號
    * @param [in] timeout 熄弧超時時間
    * @return 錯誤碼
    */
    errno_t ARCEnd(int ioType, int arcNum, int timeout);

設定焊接電流與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定焊接電流與輸出模擬量對應關係
    * @param [in] currentMin 焊接電流-類比量輸出線性關係左點電流值(A)
    * @param [in] currentMax 焊接電流-類比量輸出線性關係右側點電流值(A)
    * @param [in] outputVoltageMin 焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

設定焊接電壓與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定焊接電壓與輸出模擬量對應關係
    * @param [in] weldVoltageMin 焊接電壓-類比輸出線性關係左點焊接電壓值(A)
    * @param [in] weldVoltageMax 焊接電壓-類比輸出線性關係右側點焊接電壓值(A)
    * @param [in] outputVoltageMin 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電壓-類比輸出線性關係右側點類比輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

取得焊接電流與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得焊接電流與輸出模擬量對應關係
    * @param [out] currentMin 焊接電流-類比量輸出線性關係左點電流值(A)
    * @param [out] currentMax 焊接電流-類比量輸出線性關係右側點電流值(A)
    * @param [out] outputVoltageMin 焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingGetCurrentRelation(double *currentMin, double *currentMax, double *outputVoltageMin, double *outputVoltageMax);

取得焊接電壓與輸出類比對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得焊接電壓與輸出類比對應關係
    * @param [out] weldVoltageMin 焊接電壓-類比輸出線性關係左點焊接電壓值(A)
    * @param [out] weldVoltageMax 焊接電壓-類比輸出線性關係右側點焊接電壓值(A)
    * @param [out] outputVoltageMin 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電壓-類比輸出線性關係右側點類比輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingGetVoltageRelation(double *weldVoltageMin, double *weldVoltageMax, double *outputVoltageMin, double *outputVoltageMax);

設定焊接電流
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱類比輸出端口(0-1)
    * @return 錯誤碼
    */
    errno_t WeldingSetCurrent(int ioType, double current, int AOIndex);

設定焊接電壓
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] voltage 焊接電壓值(A)
    * @param [in] AOIndex 焊接電壓控制箱類比輸出端口(0-1)
    * @return 錯誤碼
    */
    errno_t WeldingSetVoltage(int ioType, double voltage, int AOIndex);

設定擺動參數
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in] weaveType 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    * @param [in] weaveFrequency 擺動頻率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-週期不包含等待時間；1-週期包含等待時間
    * @param [in] weaveRange 擺動幅度(mm)
    * @param [in] weaveLeftStayTime 擺動左停留時間(ms)
    * @param [in] weaveRightStayTime 擺動右停留時間(ms)
    * @param [in] weaveCircleRadio 圓形擺動-回調比率(0-100%)
    * @param [in] weaveStationary 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止
    * @return 錯誤碼
    */
    errno_t WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

即时設定擺動參數
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 即时設定擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in] weaveType 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    * @param [in] weaveFrequency 擺動頻率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-週期不包含等待時間；1-週期包含等待時間
    * @param [in] weaveRange 擺動幅度(mm)
    * @param [in] weaveLeftStayTime 擺動左停留時間(ms)
    * @param [in] weaveRightStayTime 擺動右停留時間(ms)
    * @param [in] weaveCircleRadio 圓形擺動-回調比率(0-100%)
    * @param [in] weaveStationary 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止
    * @return 錯誤碼
    */
    errno_t WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

擺盪開始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 擺盪開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    errno_t WeaveStart(int weaveNum);

擺盪結束
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 擺盪結束
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    errno_t WeaveEnd(int weaveNum);

正向送絲
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 正向送絲
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] wireFeed 送絲控制 0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    errno_t SetForwardWireFeed(int ioType, int wireFeed);

反向送絲
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 反向送絲
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] wireFeed 送絲控制 0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    errno_t SetReverseWireFeed(int ioType, int wireFeed);

送氣
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 送氣
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    errno_t SetAspirated(int ioType, int airControl);

段焊開始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 段焊開始
    * @param [in] startDesePos 起始點笛卡爾位置
    * @param [in] endDesePos 结束點笛卡兒位姿
    * @param [in] startJPos 起始點關節位姿
    * @param [in] endJPos 結束點關節位姿
    * @param [in] weldLength 焊接段長度(mm)
    * @param [in] noWeldLength 非焊接段長度(mm)
    * @param [in] weldIOType 焊接IO類型(0-控制箱IO；1-擴展IO)
    * @param [in] arcNum 焊機設定檔編號
    * @param [in] weldTimeout 起/收弧逾時時間
    * @param [in] isWeave 是否擺動
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] search 0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos 位元位偏移量
    * @return 錯誤碼
    */
    errno_t SegmentWeldStart(DescPose *startDesePos, DescPose *endDesePos, JointPos *startJPos, JointPos *endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

代碼範例
+++++++++++++++++++++++++++++++++++++++++++++
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

    using namespace std;

    int main(void)
    {
        FRRobot robot;
        robot.RPC("192.168.58.2");

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;

        DescPose start_descpose;
        start_descpose.rpy.rx = 2.243;
        start_descpose.rpy.ry = 0.828;
        start_descpose.rpy.rz = -148.894;
        start_descpose.tran.x = -208.064;
        start_descpose.tran.y = 412.155;
        start_descpose.tran.z = 1.926;

        JointPos start_jointpose;
        start_jointpose.jPos[0] = -51.489;
        start_jointpose.jPos[1] = -105.721;
        start_jointpose.jPos[2] = 130.695;
        start_jointpose.jPos[3] = -108.338;
        start_jointpose.jPos[4] = -91.356;
        start_jointpose.jPos[5] = 62.014;

        DescPose end_descpose;
        end_descpose.rpy.rx = 2.346;
        end_descpose.rpy.ry = -3.633;
        end_descpose.rpy.rz = -106.313;
        end_descpose.tran.x = -425.087;
        end_descpose.tran.y = 389.637;
        end_descpose.tran.z = -9.249;

        JointPos end_jointpose;
        end_jointpose.jPos[0] = -47.137;
        end_jointpose.jPos[1] = -102.345;
        end_jointpose.jPos[2] = 127.607;
        end_jointpose.jPos[3] = -108.526;
        end_jointpose.jPos[4] = -91.407;
        end_jointpose.jPos[5] = 23.537;

        ExaxisPos ex_axis_pose;
        memset(&ex_axis_pose, 0, sizeof(ExaxisPos));
        DescPose offset_pose;
        memset(&offset_pose, 0, sizeof(DescPose));
        int retval = 0;

        retval = robot.WeldingSetCurrentRelation(0, 400, 0, 10);
        cout << "WeldingSetCurrentRelation retval is: " << retval << endl;

        retval = robot.WeldingSetVoltageRelation(0, 40, 0, 10);
        cout << "WeldingSetVoltageRelation retval is: " << retval << endl;

        retval = robot.WeldingGetCurrentRelation(&current_min, &current_max, &output_vmin, &output_vmax);
        cout << "WeldingGetCurrentRelation retval is: " << retval << endl;
        cout << "current min " << current_min << " current max " << current_max << " output vol min " << output_vmin << " output vol max "<< output_vmax<<endl;

        retval = robot.WeldingGetVoltageRelation(&vol_min, &vol_max, &output_vmin, &output_vmax);
        cout << "WeldingGetVoltageRelation retval is: " << retval << endl;
        cout << "vol min " << vol_min << " vol max " << vol_max << " output vol min " << output_vmin << " output vol max "<< output_vmax<<endl;

        retval = robot.WeldingSetCurrent(1, 100, 0);
        cout << "WeldingSetCurrent retval is: " << retval << endl;

        this_thread::sleep_for(chrono::seconds(3));

        retval = robot.WeldingSetVoltage(1, 10, 0);
        cout << "WeldingSetVoltage retval is: " << retval << endl;

        retval = robot.WeaveSetPara(0, 0, 2.0, 0, 10, 0, 0, 0, 0);
        cout << "retval is: " << retval << endl;

        retval = robot.MoveJ(&start_jointpose, &start_descpose, 1, 0, 50, 50, 50, &ex_axis_pose, 0, 0, &offset_pose);
        if (retval != 0)
        {
            cout << "movej fail " << retval << endl;
            return 0;
        }

        retval = robot.WeaveStart(0);
        cout << "retval is: " << retval << endl;

        retval = robot.MoveL(&end_jointpose, &end_descpose, 1, 0, 50, 50, 50, 0, &ex_axis_pose, 0, 0, &offset_pose);
        if (retval != 0)
        {
            cout << "MoveL fail " << retval << endl;
            robot.WeaveEnd(0);
            return 0;
        }

        retval = robot.WeaveEnd(0);
        cout << "retval is: " << retval << endl;

        retval = 0;
        retval = robot.SetForwardWireFeed(1, 1);
        cout << "SetForwardWireFeed retval is: " << retval << endl;

        this_thread::sleep_for(chrono::seconds(3));

        retval = robot.SetForwardWireFeed(1, 0);
        cout << "SetForwardWireFeed retval is: " << retval << endl;

        retval = robot.SetReverseWireFeed(1, 1);
        cout << "SetReverseWireFeed retval is: " << retval << endl;

        this_thread::sleep_for(chrono::seconds(3));

        retval = robot.SetReverseWireFeed(1, 0);
        cout << "SetReverseWireFeed retval is: " << retval << endl;

        retval = robot.SetAspirated(1, 1);
        cout << "SetAspirated retval " << retval << endl;

        this_thread::sleep_for(chrono::seconds(2));

        retval = robot.SetAspirated(1, 0);
        cout << "SetAspirated retval " << retval << endl;

        /* 所有的座標點請以實際工況為準 */
        start_descpose.rpy.rx = 7.178;
        start_descpose.rpy.ry = -0.809;
        start_descpose.rpy.rz = -133.134;
        start_descpose.tran.x = -135.56;
        start_descpose.tran.y = 373.448;
        start_descpose.tran.z = 36.767;

        start_jointpose.jPos[0] = -70.228;
        start_jointpose.jPos[1] = -130.911;
        start_jointpose.jPos[2] = 134.147;
        start_jointpose.jPos[3] = -83.379;
        start_jointpose.jPos[4] = -95.656;
        start_jointpose.jPos[5] = 27.74;

        end_descpose.rpy.rx = -4.586;
        end_descpose.rpy.ry = -10.926;
        end_descpose.rpy.rz = -124.298;
        end_descpose.tran.x = -380.207;
        end_descpose.tran.y = 371.358;
        end_descpose.tran.z = 55.898;

        end_jointpose.jPos[0] = -50.247;
        end_jointpose.jPos[1] = -113.273;
        end_jointpose.jPos[2] = 125.856;
        end_jointpose.jPos[3] = -100.351;
        end_jointpose.jPos[4] = -80.702;
        end_jointpose.jPos[5] = 38.478;

        memset(&ex_axis_pose, 0, sizeof(ExaxisPos));
        memset(&offset_pose, 0, sizeof(DescPose));
        retval = 0;

        retval = robot.SegmentWeldStart(&start_descpose, &end_descpose, &start_jointpose, &end_jointpose, 20, 20, 1, 0, 5000, 1, 0, 1, 0, 20, 50, 50, 0, &ex_axis_pose, 0, 0, &offset_pose);
        if(0 != retval)
        {
            cout << "SegmentWeldStart end " << retval << endl;
        }

        return 0;
    }

取得旋轉夾爪的旋轉圈數
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 3.7.6版本加入

.. code-block:: c++
    :linenos:

    /**
	 * @brief  取得旋轉夾爪的旋轉圈數
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] num  旋轉圈數
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotNum(uint16_t* fault, double* num);

取得旋轉夾爪的旋轉速度
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  取得旋轉夾爪的旋轉速度
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] speed  旋轉速度百分比
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotSpeed(uint16_t* fault, int* speed);

取得旋轉夾爪的旋轉力矩
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    /**
	 * @brief  取得旋轉夾爪的旋轉力矩
	 * @param  [out] fault  0-無錯誤，1-有錯誤
	 * @param  [out] torque  旋轉力矩百分比
	 * @return  錯誤碼
	 */
	errno_t GetGripperRotTorque(uint16_t* fault, int* torque);

範例程式
********************

.. versionadded:: V3.7.6

.. code-block:: c++
    :linenos:

    int MoveRotGripper(FRRobot* robot, int pos, double rotPos)
    {
        robot->ResetAllError();
        robot->ActGripper(1, 1);
        robot->Sleep(1000);
        int rtn = robot->MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
        printf("move gripper rtn is %d\n", rtn);
        uint16_t fault = 0;
        double rotNum = 0.0;
        int rotSpeed = 0;
        int rotTorque = 0;
        robot->GetGripperRotNum(&fault, &rotNum);
        robot->GetGripperRotSpeed (&fault, &rotSpeed);
        robot->GetGripperRotTorque(&fault, &rotTorque);
        printf("gripper rot num : %lf, gripper rotSpeed : %d, gripper rotTorque : %d\n", rotNum, rotSpeed, rotTorque);

        return 0;
    }