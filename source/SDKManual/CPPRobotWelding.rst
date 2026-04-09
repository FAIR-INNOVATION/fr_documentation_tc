機器人焊接
======================

.. toctree:: 
    :maxdepth: 5

設置焊接工藝曲線參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設置焊接工藝曲線參數
     * @param [in] id 焊接工藝編號(1-99)
     * @param [in] startCurrent 起弧電流(A)
     * @param [in] startVoltage 起弧電壓(V)
     * @param [in] startTime 起弧時間(ms)
     * @param [in] weldCurrent 焊接電流(A)
     * @param [in] weldVoltage 焊接電壓(V)
     * @param [in] endCurrent 收弧電流(A)
     * @param [in] endVoltage 收弧電壓(V)
     * @param [in] endTime 收弧時間(ms)
     * @return 錯誤碼
     */
    errno_t WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

獲取焊接工藝曲線參數
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 獲取焊接工藝曲線參數
     * @param [in] id 焊接工藝編號(1-99)
     * @param [out] startCurrent 起弧電流(A)
     * @param [out] startVoltage 起弧電壓(V)
     * @param [out] startTime 起弧時間(ms)
     * @param [out] weldCurrent 焊接電流(A)
     * @param [out] weldVoltage 焊接電壓(V)
     * @param [out] endCurrent 收弧電流(A)
     * @param [out] endVoltage 收弧電壓(V)
     * @param [out] endTime 收弧時間(ms)
     * @return 錯誤碼
     */
    errno_t WeldingGetProcessParam(int id, double& startCurrent, double& startVoltage, double& startTime, double& weldCurrent, double& weldVoltage, double& endCurrent, double& endVoltage, double& endTime);

設置焊接電流與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊接電流與輸出模擬量對應關係
    * @param [in] currentMin 焊接電流-模擬量輸出線性關係左側點電流值(A)
    * @param [in] currentMax 焊接電流-模擬量輸出線性關係右側點電流值(A)
    * @param [in] outputVoltageMin 焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

設置焊接電壓與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊接電壓與輸出模擬量對應關係
    * @param [in] weldVoltageMin 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(A)
    * @param [in] weldVoltageMax 焊接電壓-模擬量輸出線性關係右側點焊接電壓值(A)
    * @param [in] outputVoltageMin 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電壓-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

獲取焊接電流與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取焊接電流與輸出模擬量對應關係
    * @param [out] currentMin 焊接電流-模擬量輸出線性關係左側點電流值(A)
    * @param [out] currentMax 焊接電流-模擬量輸出線性關係右側點電流值(A)
    * @param [out] outputVoltageMin 焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingGetCurrentRelation(double *currentMin, double *currentMax, double *outputVoltageMin, double *outputVoltageMax);

獲取焊接電壓與輸出模擬量對應關係
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取焊接電壓與輸出模擬量對應關係
    * @param [out] weldVoltageMin 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(A)
    * @param [out] weldVoltageMax 焊接電壓-模擬量輸出線性關係右側點焊接電壓值(A)
    * @param [out] outputVoltageMin 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電壓-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    errno_t WeldingGetVoltageRelation(double *weldVoltageMin, double *weldVoltageMax, double *outputVoltageMin, double *outputVoltageMax);

設置焊接電流
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱模擬量輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    errno_t WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

設置焊接電壓
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] voltage 焊接電壓值(V)
    * @param [in] AOIndex 焊接電壓控制箱模擬量輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    errno_t WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

設置擺動參數
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief 設置擺動參數
     * @param [in] weaveNum 擺焊參數配置編號
     * @param [in] weaveType 擺動類型 0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
     * @param [in] weaveFrequency 擺動頻率(Hz)
     * @param [in] weaveIncStayTime 等待模式 0-週期不包含等待時間；1-週期包含等待時間
     * @param [in] weaveRange 擺動幅度(mm)
     * @param [in] weaveLeftRange 垂直三角擺動左弦長度(mm)
     * @param [in] weaveRightRange 垂直三角擺動右弦長度(mm)
     * @param [in] additionalStayTime 垂直三角擺動垂三角點停留時間(mm)
     * @param [in] weaveLeftStayTime 擺動左停留時間(ms)
     * @param [in] weaveRightStayTime 擺動右停留時間(ms)
     * @param [in] weaveCircleRadio 圓形擺動-回調比率(0-100%)
     * @param [in] weaveStationary 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止
     * @param [in] weaveYawAngle 擺動方向方位角(繞擺動Z軸旋轉)，單位°
     * @param [in] weaveRotAngle 擺動方向側傾角(繞擺動X軸偏轉)，單位°
     * @return 錯誤碼
     */
      errno_t WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle = 0);

設置焊接參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestSetWeldParam(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.WeldingSetProcessParam(1, 177, 27, 1000, 178, 28, 176, 26, 1000);
      robot.WeldingSetProcessParam(2, 188, 28, 555, 199, 29, 133, 23, 333);
      double startCurrent = 0;
      double startVoltage = 0;
      double startTime = 0;
      double weldCurrent = 0;
      double weldVoltage = 0;
      double endCurrent = 0;
      double endVoltage = 0;
      double endTime = 0;
      robot.WeldingGetProcessParam(1, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
      cout << "the Num 1 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
      robot.WeldingGetProcessParam(2, startCurrent, startVoltage, startTime, weldCurrent, weldVoltage, endCurrent, endVoltage, endTime);
      cout << "the Num 2 process param is " << startCurrent << " " << startVoltage << " " << startTime << " " << weldCurrent << " " << weldVoltage << " " << endCurrent << " " << endVoltage << " " << endTime << endl;
      rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
      cout << "WeldingSetCurrentRelation rtn is: " << rtn << endl;
      rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
      cout << "WeldingSetVoltageRelation rtn is: " << rtn << endl;
      double current_min = 0;
      double current_max = 0;
      double vol_min = 0;
      double vol_max = 0;
      double output_vmin = 0;
      double output_vmax = 0;
      int curIndex = 0;
      int volIndex = 0;
      rtn = robot.WeldingGetCurrentRelation(&current_min, &current_max, &output_vmin, &output_vmax, &curIndex);
      cout << "WeldingGetCurrentRelation rtn is: " << rtn << endl;
      cout << "current min " << current_min << " current max " << current_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
      rtn = robot.WeldingGetVoltageRelation(&vol_min, &vol_max, &output_vmin, &output_vmax, &volIndex);
      cout << "WeldingGetVoltageRelation rtn is: " << rtn << endl;
      cout << "vol min " << vol_min << " vol max " << vol_max << " output vol min " << output_vmin << " output vol max " << output_vmax << endl;
      rtn = robot.WeldingSetCurrent(1, 100, 0, 0);
      cout << "WeldingSetCurrent rtn is: " << rtn << endl;
      this_thread::sleep_for(chrono::seconds(3));
      rtn = robot.WeldingSetVoltage(1, 10, 0, 0);
      cout << "WeldingSetVoltage rtn is: " << rtn << endl;
      rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
      cout << "rtn is: " << rtn << endl;
      robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);
      rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
      printf("WeldingSetCheckArcInterruptionParam  %d\n", rtn);
      rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
      printf("WeldingSetReWeldAfterBreakOffParam  %d\n", rtn);
      int enable = 0;
      double length = 0;
      double velocity = 0;
      int moveType = 0;
      int checkEnable = 0;
      int arcInterruptTimeLength = 0;
      rtn = robot.WeldingGetCheckArcInterruptionParam(&checkEnable, &arcInterruptTimeLength);
      printf("WeldingGetCheckArcInterruptionParam checkEnable %d  arcInterruptTimeLength %d\n", checkEnable, arcInterruptTimeLength);
      rtn = robot.WeldingGetReWeldAfterBreakOffParam(&enable, &length, &velocity, &moveType);
      printf("WeldingGetReWeldAfterBreakOffParam enable = %d, length = %lf, velocity = %lf, moveType = %d\n", enable, length, velocity, moveType);
      robot.SetWeldMachineCtrlModeExtDoNum(17);
      for (int i = 0; i < 5; i++)
      {
        robot.SetWeldMachineCtrlMode(0);
        robot.Sleep(1000);
        robot.SetWeldMachineCtrlMode(1);
        robot.Sleep(1000);
      }
      robot.CloseRPC();
      return 0;
    }

即時設置擺動參數
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 即時設置擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in] weaveType 擺動類型 0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
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

設置機器人焊接電弧意外中斷檢測參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設置機器人焊接電弧意外中斷檢測參數
	 * @param [in] checkEnable 是否使能檢測；0-不使能；1-使能
	 * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
	 * @return 錯誤碼
    */
	errno_t WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

獲取機器人焊接電弧意外中斷檢測參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 獲取機器人焊接電弧意外中斷檢測參數
	 * @param [out] checkEnable 是否使能檢測；0-不使能；1-使能
	 * @param [out] arcInterruptTimeLength 電弧中斷確認時長(ms)
	 * @return 錯誤碼
    */
	errno_t WeldingGetCheckArcInterruptionParam(int* checkEnable, int* arcInterruptTimeLength);

設置機器人焊接中斷恢復參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設置機器人焊接中斷恢復參數
	 * @param [in] enable 是否使能焊接中斷恢復
	 * @param [in] length 焊縫重疊距離(mm)
	 * @param [in] velocity 機器人回到再起弧點速度百分比(0-100)
	 * @param [in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
	 * @return 錯誤碼
    */
	errno_t WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);
    
獲取機器人焊接中斷恢復參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 獲取機器人焊接中斷恢復參數
	 * @param [out] enable 是否使能焊接中斷恢復
	 * @param [out] length 焊縫重疊距離(mm)
	 * @param [out] velocity 機器人回到再起弧點速度百分比(0-100)
	 * @param [out] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
	 * @return 錯誤碼
    */
	errno_t WeldingGetReWeldAfterBreakOffParam(int* enable, double* length, double* velocity, int* moveType);

設置焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊機控制模式擴展DO端口
    * @param DONum 焊機控制模式DO端口(0-127)
    * @return 錯誤碼
    */
    errno_t SetWeldMachineCtrlModeExtDoNum(int DONum);

設置焊機控制模式
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊機控制模式
    * @param [in] mode 焊機控制模式;0-直流一元模式；1-脈衝一元模式；2-JOB模式；3-近控模式；4-分別模式；5-CC/CV模式；6-TIG；7-CMT
    * @param [in] ioType 控制類型；0-控制箱IO;1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @return 錯誤碼
    */
    errno_t SetWeldMachineCtrlMode(int mode, int ioType = 1);

焊接開始
++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 焊接開始
    * @param [in] ioType io類型 0-控制器IO； 1-擴展IO
    * @param [in] arcNum 焊機配置文件編號
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
    * @param [in] ioType io類型 0-控制器IO； 1-擴展IO
    * @param [in] arcNum 焊機配置文件編號
    * @param [in] timeout 熄弧超時時間
    * @return 錯誤碼
    */
    errno_t ARCEnd(int ioType, int arcNum, int timeout);

擺動開始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 擺動開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    errno_t WeaveStart(int weaveNum);

擺動結束
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 擺動結束
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
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
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
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
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
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    errno_t SetAspirated(int ioType, int airControl);

設置機器人焊接中斷後恢復焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設置機器人焊接中斷後恢復焊接
	 * @return 錯誤碼
    */
	errno_t WeldingStartReWeldAfterBreakOff();

設置機器人焊接中斷後退出焊接
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.8-3.7.8

.. code-block:: c++
    :linenos:

    /**
	 * @brief 設置機器人焊接中斷後退出焊接
	 * @return 錯誤碼
	 */
	errno_t WeldingAbortWeldAfterBreakOff();

機器人焊接控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestWelding(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SetForwardWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetForwardWireFeed(0, 0);
      robot.SetReverseWireFeed(0, 1);
      robot.Sleep(1000);
      robot.SetReverseWireFeed(0, 0);
      robot.SetAspirated(0, 1);
      robot.Sleep(1000);
      robot.SetAspirated(0, 0);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.WeaveStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.ARCEnd(1, 0, 10000);
      robot.WeaveEnd(0);
      robot.WeldingStartReWeldAfterBreakOff();
      robot.WeldingAbortWeldAfterBreakOff();
      robot.CloseRPC();
      return 0;
    }


段焊開始
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 段焊開始
    * @param [in] startDesePos 起始點笛卡爾位置
    * @param [in] endDesePos 結束點笛卡爾位姿
    * @param [in] startJPos 起始點關節位姿
    * @param [in] endJPos 結束點關節位姿
    * @param [in] weldLength 焊接段長度(mm)
    * @param [in] noWeldLength 非焊接段長度(mm)
    * @param [in] weldIOType 焊接IO類型(0-控制箱IO；1-擴展IO)
    * @param [in] arcNum 焊機配置文件編號
    * @param [in] weldTimeout 起/收弧超時時間
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
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 錯誤碼
    */
    errno_t SegmentWeldStart(DescPose *startDesePos, DescPose *endDesePos, JointPos *startJPos, JointPos *endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout, bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos);

機器人段焊代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    int TestSegWeld(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.WeldingSetCurrent(1, 230, 0, 0);
      robot.WeldingSetVoltage(1, 24, 0, 1);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      rtn = robot.SegmentWeldStart(&p1Desc, &p2Desc, &p1Joint, &p2Joint, 20, 20, 0, 0, 5000, 0, 0, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      printf("SegmentWeldStart rtn is %d\n", rtn);
      robot.CloseRPC();
      return 0;
    }


仿真擺動開始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 仿真擺動開始
     * @param [in] weaveNum 擺動參數編號
     * @return 錯誤碼
     */
    errno_t WeaveStartSim(int weaveNum);

仿真擺動結束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 仿真擺動結束
     * @param [in] weaveNum 擺動參數編號
     * @return 錯誤碼
     */
    errno_t WeaveEndSim(int weaveNum);

開始軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 開始軌跡檢測預警(不運動)
     * @param [in] weaveNum  擺動參數編號
     * @return 錯誤碼
     */
    errno_t WeaveInspectStart(int weaveNum);

結束軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 結束軌跡檢測預警(不運動)
     * @param [in] weaveNum  擺動參數編號
     * @return 錯誤碼
     */
    errno_t WeaveInspectEnd(int weaveNum);

擺動漸變開始
+++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
     * @brief 擺動漸變開始
     * @param [in] weaveChangeFlag 1-變擺動參數；2-變擺動參數+焊接速度
     * @param [in] weaveNum 擺動編號 
     * @param [in] velStart 焊接開始速度，(cm/min)
     * @param [in] velEnd 焊接結束速度，(cm/min)
     * @return 錯誤碼
     */
     errno_t WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

機器人擺動漸變焊接代碼示例
+++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    int TestWeave(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose p1Desc(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
      JointPos p1Joint(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);
      DescPose p2Desc(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
      JointPos p2Joint(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);
      ExaxisPos exaxisPos(0, 0, 0, 0);
      DescPose offdese(0, 0, 0, 0, 0, 0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveStartSim(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveEndSim(0);
      robot.MoveJ(&p1Joint, &p1Desc, 13, 0, 20, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot.WeaveInspectStart(0);
      robot.MoveL(&p2Joint, &p2Desc, 13, 0, 20, 100, 100, -1, 0, &exaxisPos, 0, 0, &offdese);
      robot.WeaveInspectEnd(0);
      robot.WeldingSetVoltage(1, 19, 0, 0);
      robot.WeldingSetCurrent(1, 190, 0, 0);
      robot.MoveL(&p1Joint, &p1Desc, 1, 1, 100, 100, 50, -1, &exaxisPos, 0, 0, &offdese);
      robot.ARCStart(1, 0, 10000);
      robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.WeaveStart(0);
      robot.WeaveChangeStart(1, 0, 50, 30);
      robot.MoveL(&p2Joint, &p2Desc, 1, 1, 100, 100, 1, -1, &exaxisPos, 0, 0, &offdese);
      robot.WeaveChangeEnd();
      robot.WeaveEnd(0);
      robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
      robot.ARCEnd(1, 0, 10000);
      robot.CloseRPC();
      return 0;
    }

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

擴展IO-配置焊機氣體檢測信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機氣體檢測信號
     * @param [in] DONum 氣體檢測信號擴展DO編號
     * @return 錯誤碼
     */
    errno_t SetAirControlExtDoNum(int DONum);

擴展IO-配置焊機起弧信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機起弧信號
     * @param [in] DONum 焊機起弧信號擴展DO編號
     * @return 錯誤碼
     */
    errno_t SetArcStartExtDoNum(int DONum);

擴展IO-配置焊機反向送絲信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機反向送絲信號
     * @param [in] DONum 反向送絲信號擴展DO編號
     * @return 錯誤碼
     */
    errno_t SetWireReverseFeedExtDoNum(int DONum);

擴展IO-配置焊機正向送絲信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機正向送絲信號
     * @param [in] DONum 正向送絲信號擴展DO編號
     * @return 錯誤碼
     */
    errno_t SetWireForwardFeedExtDoNum(int DONum);

擴展IO-配置焊機起弧成功信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機起弧成功信號
     * @param [in] DINum 起弧成功信號擴展DI編號
     * @return 錯誤碼
     */
    errno_t SetArcDoneExtDiNum(int DINum);

擴展IO-配置焊機準備信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊機準備信號
     * @param [in] DINum 焊機準備信號擴展DI編號
     * @return 錯誤碼
     */
    errno_t SetWeldReadyExtDiNum(int DINum);

擴展IO-配置焊接中斷恢復信號
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 擴展IO-配置焊接中斷恢復信號
     * @param [in] reWeldDINum 焊接中斷後恢復焊接信號擴展DI編號
     * @param [in] abortWeldDINum 焊接中斷後退出焊接信號擴展DI編號
     * @return 錯誤碼
     */
    errno_t SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

設置擴展IO焊接信號代碼示例
+++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestExtDIConfig(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.SetArcStartExtDoNum(10);
      robot.SetAirControlExtDoNum(20);
      robot.SetWireForwardFeedExtDoNum(30);
      robot.SetWireReverseFeedExtDoNum(40);
      robot.SetWeldReadyExtDiNum(50);
      robot.SetArcDoneExtDiNum(60);
      robot.SetExtDIWeldBreakOffRecover(70, 80);
      robot.SetWireSearchExtDIONum(0, 1);
      robot.CloseRPC();
      return 0;
    }

電弧跟蹤控制
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

      /**
      * @brief  電弧跟蹤控制
   	  * @param  [in] flag 開關，0-關；1-開
  	  * @param  [in] dalayTime 滯後時間，單位ms
  	  * @param  [in] isLeftRight 左右偏差補償
  	  * @param  [in] klr 左右調節係數(靈敏度);
  	  * @param  [in] tStartLr 左右開始補償時間cyc
  	  * @param  [in] stepMaxLr 左右每次最大補償量 mm
  	  * @param  [in] sumMaxLr 左右總計最大補償量 mm
  	  * @param  [in] isUpLow 上下偏差補償
  	  * @param  [in] kud 上下調節係數(靈敏度);
  	  * @param  [in] tStartUd 上下開始補償時間cyc
  	  * @param  [in] stepMaxUd 上下每次最大補償量 mm
  	  * @param  [in] sumMaxUd 上下總計最大補償量
  	  * @param  [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
  	  * @param  [in] referenceType 上下基準電流設定方式，0-反饋；1-常數
  	  * @param  [in] referSampleStartUd 上下基準電流採樣開始計數(反饋);，cyc
  	  * @param  [in] referSampleCountUd 上下基準電流採樣循環計數(反饋);，cyc
  	  * @param  [in] referenceCurrent 上下基準電流mA
  	  * @param  [in] offsetType 偏置跟蹤類型，0-不偏置；1-採樣；2-百分比
  	  * @param  [in] offsetParameter 偏置參數；採樣(偏置採樣開始時間，默認採一週期)；百分比(偏置百分比(-100 ~ 100))
  	  * @return  錯誤碼
  	  */
	 errno_t ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType = 0, int offsetParameter = 0);

設置電弧跟蹤輸入信號端口
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  設置電弧跟蹤輸入信號端口
      * @param  [in] channel 電弧跟蹤AI通帶選擇,[0-3]
      * @return  錯誤碼
      */
     errno_t ArcWeldTraceExtAIChannelConfig(int channel);


電弧追蹤 + 多層多道補償開啓
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 電弧追蹤 + 多層多道補償開啓
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

多層多道焊電弧跟蹤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestArcWeldTrace(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      JointPos mulitilineorigin1_joint(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
      DescPose mulitilineorigin1_desc(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);
      DescTran mulitilineX1_desc;
      mulitilineX1_desc.x = -677.556;
      mulitilineX1_desc.y = 211.949;
      mulitilineX1_desc.z = -1.206;
      DescTran mulitilineZ1_desc;
      mulitilineZ1_desc.x = -677.564;
      mulitilineZ1_desc.y = 190.956;
      mulitilineZ1_desc.z = 19.817;
      JointPos mulitilinesafe_joint(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
      DescPose mulitilinesafe_desc(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
      JointPos mulitilineorigin2_joint(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
      DescPose mulitilineorigin2_desc(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);
      DescTran mulitilineX2_desc;
      mulitilineX2_desc.x = -563.965;
      mulitilineX2_desc.y = 220.355;
      mulitilineX2_desc.z = -0.680;
      DescTran mulitilineZ2_desc;
      mulitilineZ2_desc.x = -563.968;
      mulitilineZ2_desc.y = 215.362;
      mulitilineZ2_desc.z = 4.331;
      ExaxisPos epos(0, 0, 0, 0);
      DescPose offset(0, 0, 0, 0, 0, 0);
      robot.Sleep(10);
      int error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.WeaveStart(0);
      printf("WeaveStart return: %d\n", error);
      error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, &epos, 0, 0, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
      printf("ArcWeldTraceControl return: %d\n", error);
      error = robot.WeaveEnd(0);
      printf("WeaveEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("ArcWeldTraceReplayStart return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 10000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.MoveL(&mulitilineorigin1_joint, &mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ARCStart(1, 0, 3000);
      printf("ARCStart return: %d\n", error);
      error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);
      printf("MultilayerOffsetTrsfToBase return: %d offect is %f %f %f \n", error, offset.tran.x, offset.tran.y, offset.tran.z);
      error = robot.ArcWeldTraceReplayStart();
      printf("MoveJ return: %d\n", error);
      error = robot.MoveL(&mulitilineorigin2_joint, &mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, &epos, 0, 1, &offset, 0, 100);
      printf("MoveL return: %d\n", error);
      error = robot.ArcWeldTraceReplayEnd();
      printf("ArcWeldTraceReplayEnd return: %d\n", error);
      error = robot.ARCEnd(1, 0, 3000);
      printf("ARCEnd return: %d\n", error);
      error = robot.MoveJ(&mulitilinesafe_joint, &mulitilinesafe_desc, 13, 0, 10, 100, 100, &epos, -1, 0, &offset);
      printf("MoveJ return: %d\n", error);
      robot.CloseRPC();
      return 0;
    }

電弧跟蹤焊機電流反饋AI通道選擇
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 電弧跟蹤焊機電流反饋AI通道選擇
     * @param [in]  channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
     * @return 錯誤碼
     */
     errno_t ArcWeldTraceAIChannelCurrent(int channel);

電弧跟蹤焊機電壓反饋AI通道選擇
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 電弧跟蹤焊機電壓反饋AI通道選擇
     * @param [in]  channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
     * @return 錯誤碼
     */
     errno_t ArcWeldTraceAIChannelVoltage(int channel);

電弧跟蹤焊機電流反饋轉換參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
      * @brief 電弧跟蹤焊機電流反饋轉換參數
      * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
      * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
      * @param [in] currentLow AI通道下限對應焊機電流值，默認值0V，範圍[0-200V]
      * @param [in] currentHigh AI通道上限對應焊機電流值，默認值100V，範圍[0-200V]
      * @return 錯誤碼
      */
     errno_t ArcWeldTraceCurrentPara(float AILow, float AIHigh, float currentLow, float currentHigh);

電弧跟蹤焊機電壓反饋轉換參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     /**
    * @brief 電弧跟蹤焊機電壓反饋轉換參數
    * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
    * @param [in] voltageLow AI通道下限對應焊機電壓值，默認值0V，範圍[0-200V]
    * @param [in] voltageHigh AI通道上限對應焊機電壓值，默認值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    errno_t ArcWeldTraceVoltagePara(float AILow, float AIHigh, float voltageLow, float voltageHigh);

電弧跟蹤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int WeldTraceControlWithCtrlBoxAI(FRRobot* robot)
    {
      DescPose startdescPose = { -473.86, 257.879, -20.849, -37.317, -42.021, 2.543 };
      JointPos startjointPos = { -43.487, -76.526, 95.568, -104.445, -89.356, 3.72 };

      DescPose enddescPose = { -499.844, 141.225, 7.72, -34.856, -40.17, 13.13 };
      JointPos endjointPos = { -31.305, -82.998, 99.401, -104.426, -89.35, 3.696 };

      DescPose safedescPose = { -504.043, 275.181, 40.908, -28.002, -42.025, -14.044 };
      JointPos safejointPos = { -39.078, -76.732, 87.227, -99.47, -94.301, 18.714 };

      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);

      robot->WeldingSetVoltage(0, 25, 1, 0);// ----設置電壓
      robot->WeldingSetCurrent(0, 260, 0, 0);// ----設置電流

      int rtn = robot->ArcWeldTraceAIChannelCurrent(4);
      cout << "ArcWeldTraceAIChannelCurrent rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceAIChannelVoltage(5);
      cout << "ArcWeldTraceAIChannelVoltage rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceCurrentPara(0, 5, 0, 500);
      cout << "ArcWeldTraceCurrentPara rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceVoltagePara(1.018, 10, 0, 50);
      cout << "ArcWeldTraceVoltagePara rtn is " << rtn << endl;
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      return 0;
    }

設置焊絲尋位擴展IO端口
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設置焊絲尋位擴展IO端口
    * @param searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param searchStartDONum 焊絲尋位啓停控制DO端口(0-127)
    * @return 錯誤碼
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
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
    rtn1 = robot->WireSearchWait("REF0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
    rtn1 = robot->WireSearchWait("REF1");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF0A, &descREF0A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
    robot->MoveL(&jointREF0B, &descREF0B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
    rtn1 = robot->WireSearchWait("RES0");
    rtn2 = robot->WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

    rtn0 = robot->WireSearchStart(0, 10, 100, 0, 10, 100, 0);
    robot->MoveL(&jointREF1A, &descREF1A, 1, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
    robot->MoveL(&jointREF1B, &descREF1B, 1, 0, 10, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
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

焊絲尋位開始
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief  焊絲尋位開始
    * @param  [in] refPos  1-基準點 0-接觸點
    * @param  [in] searchVel   尋位速度 %
    * @param  [in] searchDis  尋位距離 mm
    * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param  [in] autoBackVel  自動返回速度 %
    * @param  [in] autoBackDis  自動返回距離 mm
    * @param  [in] offectFlag  1-帶偏移量尋位；0-示教點尋位
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
      * @param  [in] searchDis  尋位距離 mm
      * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
      * @param  [in] autoBackVel  自動返回速度 %
      * @param  [in] autoBackDis  自動返回距離 mm
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
      * @param  [in] seamType  焊縫類型
      * @param  [in] method   計算方法
      * @param  [in] varNameRef 基準點1-6，“#”表示無點變量
      * @param  [in] varNameRes 接觸點1-6，“#”表示無點變量
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

焊絲尋位接觸點寫入數據庫
+++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

     /**
      * @brief  焊絲尋位接觸點寫入數據庫
      * @param  [in] varName  接觸點名稱 “RES0” ~ “RES99”
      * @param  [in] pos  接觸點數據[x, y, x, a, b, c]
      * @return  錯誤碼
      */
     errno_t SetPointToDatabase(std::string varName, DescPose pos);

機器人焊絲尋位代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestWireSearch(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescPose toolCoord(0, 0, 200, 0, 0, 0);
      robot.SetToolCoord(1, &toolCoord, 0, 0, 1, 0);
      DescPose wobjCoord(0, 0, 0, 0, 0, 0);
      robot.SetWObjCoord(1, &wobjCoord, 0);
      int rtn0, rtn1, rtn2 = 0;
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      DescPose descStart = { 216.543, 445.175, 93.465, 179.683, 1.757, -112.641 };
      JointPos jointStart = { -128.345, -86.660, 114.679, -119.625, -89.219, 74.303 };
      DescPose descEnd = { 111.143, 523.384, 87.659, 179.703, 1.835, -97.750 };
      JointPos jointEnd = { -113.454, -81.060, 109.328, -119.954, -89.218, 74.302 };
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      DescPose descREF0A = { 142.135, 367.604, 86.523, 179.728, 1.922, -111.089 };
      JointPos jointREF0A = { -126.794, -100.834, 128.922, -119.864, -89.218, 74.302 };
      DescPose descREF0B = { 254.633, 463.125, 72.604, 179.845, 2.341, -114.704 };
      JointPos jointREF0B = { -130.413, -81.093, 112.044, -123.163, -89.217, 74.303 };
      DescPose descREF1A = { 92.556, 485.259, 47.476, -179.932, 3.130, -97.512 };
      JointPos jointREF1A = { -113.231, -83.815, 119.877, -129.092, -89.217, 74.303 };
      DescPose descREF1B = { 203.103, 583.836, 63.909, 179.991, 2.854, -103.372 };
      JointPos jointREF1B = { -119.088, -69.676, 98.692, -121.761, -89.219, 74.303 };
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
      rtn1 = robot.WireSearchWait("REF0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
      rtn1 = robot.WireSearchWait("REF1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF0A, &descREF0A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
      robot.MoveL(&jointREF0B, &descREF0B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
      rtn1 = robot.WireSearchWait("RES0");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
      robot.MoveL(&jointREF1A, &descREF1A, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese); //起點
      robot.MoveL(&jointREF1B, &descREF1B, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese); //方向點
      rtn1 = robot.WireSearchWait("RES1");
      rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);
      vector <string> varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
      vector <string> varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
      int offectFlag = 0;
      DescPose offectPos = { 0, 0, 0, 0, 0, 0 };
      rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectFlag, offectPos);
      robot.PointsOffsetEnable(0, &offectPos);
      robot.MoveL(&jointStart, &descStart, 1, 1, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese);
      robot.MoveL(&jointEnd, &descEnd, 1, 1, 100, 100, 100, -1, &exaxisPos, 1, 0, &offdese);
      robot.PointsOffsetDisable();
      robot.CloseRPC();
      return 0;

設置焊接電壓漸變開始
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
    * @brief 設置焊接電壓漸變開始
    * @param [in] IOType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @param [in] voltageStart 起始焊接電壓(V)
    * @param [in] voltageEnd 終止焊接電壓(V)
    * @param [in] AOIndex 控制箱AO端口號(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    errno_t WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

設置焊接電壓漸變結束
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 設置焊接電壓漸變結束
      * @return 錯誤碼
      */
     errno_t WeldingSetVoltageGradualChangeEnd();

設置焊接電流漸變開始
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

     /**
      * @brief 設置焊接電流漸變開始
      * @param [in] IOType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
      * @param [in] voltageStart 起始焊接電流(A)
      * @param [in] voltageEnd 終止焊接電流(A)
      * @param [in] AOIndex 控制箱AO端口號(0-1)
      * @param [in] blend 是否平滑 0-不平滑；1-平滑
      * @return 錯誤碼
      */
     errno_t WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

設置焊接電流漸變結束
+++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
     * @brief 設置焊接電流漸變結束
     * @return 錯誤碼
     */
    errno_t WeldingSetCurrentGradualChangeEnd();
    
機器人焊接電流電壓漸變代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int WeldparamChange(FRRobot* robot)
    {
      DescPose startdescPose = { -484.707, 276.996, -14.013, -37.657, -40.508, -1.548 };
      JointPos startjointPos = { -45.421, -75.673, 93.627, -104.302, -87.938, 6.005 };
      
      DescPose enddescPose = { -508.767, 137.109, -13.966, -37.639, -40.508, -1.559 };
      JointPos endjointPos = { -32.768, -80.947, 100.254, -106.201, -87.201, 18.648 };

      DescPose safedescPose = { -484.709, 294.436, 13.621, -37.660, -40.508, -1.545 };
      JointPos safejointPos = { -46.604, -75.410, 89.109, -100.003, -88.012, 4.823 };
      ExaxisPos exaxisPos = { 0, 0, 0, 0 };
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };

      robot->WeldingSetCurrentRelation(0, 495, 1, 10, 0);
      robot->WeldingSetVoltageRelation(10, 45, 1, 10, 1);
      robot->MoveJ(&safejointPos, &safedescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      int rtn = robot->WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
      cout << "WeldingSetCurrentGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
      cout << "WeldingSetVoltageGradualChangeStart rtn is " << rtn << endl;
      rtn = robot->ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      cout << "ArcWeldTraceControl rtn is " << rtn << endl;
      robot->MoveJ(&startjointPos, &startdescPose, 1, 0, 5, 100, 100, &exaxisPos, -1, 0, &offdese);
      
      robot->ARCStart(0, 0, 10000);
      robot->WeaveStart(0);
      robot->WeaveChangeStart(2, 1, 24, 36);
      robot->MoveL(&endjointPos, &enddescPose, 1, 0, 100, 100, 2, -1, &exaxisPos, 0, 0, &offdese);
      robot->ARCEnd(0, 0, 10000);
      robot->WeaveChangeEnd();
      robot->WeaveEnd(0);
      robot->ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
      robot->WeldingSetCurrentGradualChangeEnd();
      robot->WeldingSetVoltageGradualChangeEnd();
      return 0;
    }

設定自訂擺動參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 設定自訂擺動參數
    * @param [in] id 自訂擺動編號：0-2
    * @param [in] pointNum 擺動點位個數 0-10
    * @param [in] point 移動端點資料x,y,z
    * @param [in] stayTime 擺動停留時間ms
    * @param [in] frequency 擺動頻率 Hz
    * @param [in] incStayType 等待模式：0-週期不包含等待時間；1-週期包含等待時間
    * @param [in] stationary 擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止
    * @return 錯誤碼
    */
    errno_t CustomWeaveSetPara(int id, int pointNum, DescTran point[10], double stayTime[10], double frequency, int incStayType, int stationary);
                
取得自訂擺動參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 取得自訂擺動參數
    * @param [in] id 自訂擺動編號：0-2
    * @param [out] pointNum 擺動點位個數 0-10
    * @param [out] point 移動端點資料x,y,z
    * @param [out] stayTime 擺動停留時間ms
    * @param [out] frequency 擺動頻率 Hz
    * @param [out] incStayType 等待模式：0-週期不包含等待時間；1-週期包含等待時間
    * @param [out] stationary 擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止
    * @return 錯誤碼
    */
    errno_t CustomWeaveGetPara(int id, int& pointNum, DescTran point[10], double stayTime[10], double& frequency, int& incStayType, int& stationary);
                    
自訂擺動參數程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v3.8.6
    
.. code-block:: c++
    :linenos:

    int TestCustomWeaveSetPara()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return 0;
      }
      robot.SetReConnectParam(true, 30000, 500);
      DescTran point[10] = {}; 
      point[0].x = -3;
      point[0].y = -3;
      point[0].z = 0;
      point[1].x = -6;
      point[1].y = 0;
      point[1].z = 0;
      point[2].x = -3;
      point[2].y = 3;
      point[2].z = 0;
      point[3].x = 0;
      point[3].y = 0;
      point[3].z = 0;
      double stayTime[10] = { 0,0,0,0,0,0,0,0,0,0 };
      rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0);
      printf("CustomWeaveSetPara rtn is %d\n", rtn);
      robot.Sleep(1000);
      int pointNum = 0;
      double frequency;
      int incStayType;
      int stationary;
      robot.CustomWeaveGetPara(2, pointNum, point, stayTime, frequency, incStayType, stationary);
      printf("pointNum is %d\n", pointNum);
      for (int i = 0; i < pointNum; i++)
      {
        printf("point %d, point x y z %f %f %f\n", i, point[i].x, point[i].y, point[i].z);
      }
      printf("fre is %f, stay is %d %d \n", frequency, incStayType, stationary);
      robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
      DescPose desc_p1 = { -288.650, 367.807, 288.404, 0.000, -0.001, 0.001 };
      DescPose desc_p2 = { -431.714, 367.815, 288.415, 0.001, 0.001, 0.000 };
      DescPose desc_p3 = { -348.666, 427.798, 288.404, -0.000, -0.000, 0.001 };
      JointPos j1 = { 140.656, -84.560, -91.707, -93.734, 90.000, 50.655 };
      JointPos j2 = { 149.873, -98.298, -77.599, -94.103, 90.000, 59.873 };
      JointPos j3 = { 139.773, -96.173, -80.014, -93.814, 90.000, 49.772 };
      ExaxisPos epos = {};
      DescPose offset_pos = {};
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.Circle(&j3, &desc_p3, 3, 0, 100, 100, &epos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 10, -1, &offset_pos);
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveC(&j3, &desc_p3, 3, 0, 100, 100, &epos, 0, &offset_pos, &j2, &desc_p2, 3, 0, 100, 100, &epos, 0, &offset_pos, 10, -1); 
      robot.WeaveEnd(0);
      robot.MoveJ(&j1, &desc_p1, 3, 0, 100, 100, 100, &epos, -1, 0, &offset_pos);
      robot.WeaveStart(0);
      robot.MoveL(&j2, &desc_p2, 3, 0, 100, 100, 10, -1, &epos, 0, 0, &offset_pos, 0, 100);
      robot.WeaveEnd(0);
      robot.CloseRPC();
    }