机器人焊接
======================

.. toctree:: 
    :maxdepth: 5

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

    
設定機器人焊接電弧意外中斷偵測參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設定機器人焊接電弧意外中斷偵測參數
	 * @param [in] checkEnable 是否使能檢測；0-不使能；1-使能
	 * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
	 * @return 錯誤碼
    */
	errno_t WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

取得機器人焊接電弧意外中斷偵測參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 取得機器人焊接電弧意外中斷偵測參數
	 * @param [out] checkEnable 是否使能檢測；0-不使能；1-使能
	 * @param [out] arcInterruptTimeLength 電弧中斷確認時長(ms)
	 * @return 錯誤碼
    */
	errno_t WeldingGetCheckArcInterruptionParam(int* checkEnable, int* arcInterruptTimeLength);

設定機器人焊接中斷恢復參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設定機器人焊接中斷恢復參數
	 * @param [in] enable 是否使能焊接中斷恢復
	 * @param [in] length 焊縫重疊距離(mm)
	 * @param [in] velocity 機器人回到再起弧點速度百分比(0-100)
	 * @param [in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
	 * @return 錯誤碼
    */
	errno_t WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);
    
取得機器人焊接中斷恢復參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 取得機器人焊接中斷恢復參數
	 * @param [out] enable 是否使能焊接中斷恢復
	 * @param [out] length 焊縫重疊距離(mm)
	 * @param [out] velocity 機器人回到再起弧點速度百分比(0-100)
	 * @param [out] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
	 * @return 錯誤碼
    */
	errno_t WeldingGetReWeldAfterBreakOffParam(int* enable, double* length, double* velocity, int* moveType);

設定機器人焊接中斷後恢復焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設定機器人焊接中斷後恢復焊接
	 * @return 錯誤碼
    */
	errno_t WeldingStartReWeldAfterBreakOff();

設定機器人焊接中斷後退出焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設定機器人焊接中斷後退出焊接
	 * @return 錯誤碼
    */
	errno_t WeldingAbortWeldAfterBreakOff();

範例程式
********************
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    void TestReWeld(FRRobot* robot)
    {
        int rtn = -1;
        rtn = robot->WeldingSetCheckArcInterruptionParam(1, 200);
        printf("WeldingSetCheckArcInterruptionParam    %d\n", rtn);
        rtn = robot->WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        printf("WeldingSetReWeldAfterBreakOffParam    %d\n", rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot->WeldingGetCheckArcInterruptionParam(&checkEnable, &arcInterruptTimeLength);
        printf("WeldingGetCheckArcInterruptionParam  checkEnable  %d   arcInterruptTimeLength  %d\n", checkEnable, arcInterruptTimeLength);
        rtn = robot->WeldingGetReWeldAfterBreakOffParam(&enable, &length, &velocity, &moveType);
        printf("WeldingGetReWeldAfterBreakOffParam  enable = %d, length = %lf, velocity = %lf, moveType = %d\n", enable, length, velocity, moveType);

        robot->ProgramLoad("/fruser/test.lua");
        robot->ProgramRun();

        robot->Sleep(5000);

        while (true)
        {
            ROBOT_STATE_PKG pkg = {};
            robot->GetRobotRealTimeState(&pkg);
            printf("welding breakoff state is     %d\n", pkg.weldingBreakOffState.breakOffState);
            if (pkg.weldingBreakOffState.breakOffState == 1)
            {
                printf("welding breakoff ! \n");
                robot->Sleep(2000);
                rtn = robot->WeldingStartReWeldAfterBreakOff();
                printf("WeldingStartReWeldAfterBreakOff    %d\n", rtn);
                break;
            }
            robot->Sleep(100);
        }
    }

焊絲尋位開始
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  焊絲尋位開始
    * @param  [in] refPos  1-基準點 2-接觸點
    * @param  [in] searchVel   尋位速度 %
    * @param  [in] searchDis 尋位距離 mm
    * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param  [in] autoBackVel 自動返回速度 %
    * @param  [in] autoBackDis 自動返回距離 mm
    * @param  [in] offectFlag  1-帶偏移量尋位；2-示教點尋位
    * @return  錯誤碼
    */
    errno_t WireSearchStart(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

焊絲尋位結束
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  焊絲尋位結束
      * @param  [in] refPos  1-基準點 2-接觸點
      * @param  [in] searchVel   尋位速度 %
      * @param  [in] searchDis 尋位距離 mm
      * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
      * @param  [in] autoBackVel 自動返回速度 %
      * @param  [in] autoBackDis 自動返回距離 mm
      * @param  [in] offectFlag  1-帶偏移量尋位；2-示教點尋位
      * @return  錯誤碼
      */
     errno_t WireSearchEnd(int refPos, float searchVel, int searchDis, int autoBackFlag, float autoBackVel, int autoBackDis, int offectFlag);

計算焊絲尋位偏移量
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  計算焊絲尋位偏移量
      * @param  [in] seamType 焊縫類型
      * @param  [in] method   計算方法
      * @param  [in] varNameRef 基準點1-6，「#」表示無點變數
      * @param  [in] varNameRes 接觸點1-6，「#」表示無點變數
      * @param  [out] offectFlag 0-偏移量直接疊加到指令點；1-偏移量需要對指令點進行座標變換
      * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
      * @return  錯誤碼
      */
     errno_t GetWireSearchOffset(int seamType, int method, std::vector<std::string> varNameRef, std::vector<std::string> varNameRes, int& offectFlag, DescPose& offect);

等待焊絲尋位完成
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

     /**
      * @brief  等待焊絲尋位完成
      * @return  錯誤碼
      */
     errno_t WireSearchWait(std::string varName);

焊絲尋位接觸點寫入資料庫
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  焊絲尋位接觸點寫入資料庫
      * @param  [in] varName  接觸點名稱 “RES0” ~ “RES99”
      * @param  [in] pos 接觸點數據[x, y, x, a, b, c]
      * @return  錯誤碼
      */
     errno_t SetPointToDatabase(std::string varName, DescPose pos);

範例程式
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
    robot->MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
    robot->MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
    rtn1 = robot->WireSearchWait("REF0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
    robot->MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
    rtn1 = robot->WireSearchWait("REF1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
    robot->MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
    rtn1 = robot->WireSearchWait("RES0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);  //起點
    robot->MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);  //方向點
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

電弧追蹤控制
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  電弧追蹤控制
      * @param  [in] flag 開關，0-關；1-開
      * @param  [in] dalayTime 滯後時間，單位ms
      * @param  [in] isLeftRight 左右偏差補償
      * @param  [in] klr 左右調節係數(靈敏度);
      * @param  [in] tStartLr 左右開始補償時間cyc
      * @param  [in] stepMaxLr 左右每次最大補償量 mm
      * @param  [in] sumMaxLr 左右總計最大補償量 mm
      * @param  [in] isUpLow 上下偏差補償
      * @param  [in] kud 上下調節係數(靈敏度);
      * @param  [in] tStartUd 上下開始補償時間cyc
      * @param  [in] stepMaxUd 上下每次最大補償量 mm
      * @param  [in] sumMaxUd 上下总计最大补偿量
      * @param  [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
      * @param  [in] referenceType 上下基準電流設定方式，0-回饋；1-常數
      * @param  [in] referSampleStartUd 上下基準電流取樣開始計數(回饋);，cyc
      * @param  [in] referSampleCountUd 上下基準電流取樣循環計數(回饋);，cyc
      * @param  [in] referenceCurrent 上下基準電流mA
      * @return  錯誤碼
      */
     errno_t ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent);

設定電弧追蹤輸入訊號端口
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設定電弧追蹤輸入訊號端口
      * @param  [in] channel 電弧追蹤AI通帶選擇,[0-3]
      * @return  錯誤碼
      */
     errno_t ArcWeldTraceExtAIChannelConfig(int channel);

範例程式
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

擺動漸變開始
+++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  擺動漸變開始
     * @param  [in] weaveNum 擺動編號
     * @return  錯誤碼
     */
    errno_t WeaveChangeStart(int weaveNum);

擺動漸變結束
+++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.0-3.8.0

.. code-block:: c++
    :linenos:

    /**
     * @brief  擺動漸變結束
     * @return  錯誤碼
     */
    errno_t WeaveChangeEnd();

程式碼範例
********************

.. code-block:: c++
    :linenos:
    
    void TestWeaveChange(FRRobot* robot)
    {
        DescPose p1Desc(-72.912, -587.664, 31.849, 43.283, -6.731, 15.068);
        JointPos p1Joint(74.620, -80.903, 94.608, -109.882, -90.436, -13.432);

        DescPose p2Desc(-104.915, -483.712, -25.231, 42.228, -6.572, 18.433);
        JointPos p2Joint(66.431, -92.875, 116.362, -120.516, -88.627, -24.731);

        DescPose p3Desc(-240.651, -483.840, -7.161, 46.577, -5.286, 8.318);
        JointPos p3Joint(56.457, -84.796, 104.618, -114.497, -92.422, -25.430);

        ExaxisPos exaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot->WeldingSetVoltage(1, 19, 0, 0);
        robot->WeldingSetCurrent(1, 190, 0, 0);
        robot->MoveJ(&p1Joint, &p1Desc, 1, 1, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
        robot->MoveL(&p2Joint, &p2Desc, 1, 1, 100, 100, 50, -1, &exaxisPos, 0, 0, &offdese);
        robot->ARCStart(1, 0, 10000);
        robot->ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot->WeaveStart(0);
        robot->WeaveChangeStart(1);
        robot->MoveL(&p3Joint, &p3Desc, 1, 1, 100, 100, 1, -1, &exaxisPos, 0, 0, &offdese);
        robot->WeaveChangeEnd();
        robot->WeaveEnd(0);
        robot->ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot->ARCEnd(1, 0, 10000);
    }