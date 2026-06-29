機器人焊接
=============

.. toctree:: 
    :maxdepth: 5

設置焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  設置焊接工藝曲線參數
    * @param  [in] id 焊接工藝編號(1-99)
    * @param  [in] startCurrent 起弧電流(A)
    * @param  [in] startVoltage 起弧電壓(V)
    * @param  [in] startTime 起弧時間(ms)
    * @param  [in] weldCurrent 焊接電流(A)
    * @param  [in] weldVoltage 焊接電壓(V)
    * @param  [in] endCurrent 收弧電流(A)
    * @param  [in] endVoltage 收弧電壓(V)
    * @param  [in] endTime 收弧時間(ms)
    * @return  錯誤碼
    */
    int WeldingSetProcessParam(int id, double startCurrent, double startVoltage, double startTime, double weldCurrent, double weldVoltage, double endCurrent, double endVoltage, double endTime);

獲取焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取焊接工藝曲線參數
    * @param  [in] id 焊接工藝編號(1-99)
    * @param  [out] startCurrent 起弧電流(A)
    * @param  [out] startVoltage 起弧電壓(V)
    * @param  [out] startTime 起弧時間(ms)
    * @param  [out] weldCurrent 焊接電流(A)
    * @param  [out] weldVoltage 焊接電壓(V)
    * @param  [out] endCurrent 收弧電流(A)
    * @param  [out] endVoltage 收弧電壓(V)
    * @param  [out] endTime 收弧時間(ms)
    * @return  錯誤碼
    */
    int WeldingGetProcessParam(int id, ref double startCurrent, ref double startVoltage, ref double startTime, ref double weldCurrent, ref double weldVoltage, ref double endCurrent, ref double endVoltage, ref double endTime);

設置焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電流與輸出模擬量對應關係
    * @param [in] currentMin 焊接電流-模擬量輸出線性關係左側點電流值(A)
    * @param [in] currentMax 焊接電流-模擬量輸出線性關係右側點電流值(A)
    * @param [in] outputVoltageMin 焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

設置焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電壓與輸出模擬量對應關係
    * @param [in] weldVoltageMin 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(A)
    * @param [in] weldVoltageMax 焊接電壓-模擬量輸出線性關係右側點焊接電壓值(A)
    * @param [in] outputVoltageMin 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電壓-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

獲取焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取焊接電流與輸出模擬量對應關係
    * @param [out] currentMin 焊接電流-模擬量輸出線性關係左側點電流值(A)
    * @param [out] currentMax 焊接電流-模擬量輸出線性關係右側點電流值(A)
    * @param [out] outputVoltageMin 焊接電流-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電流-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingGetCurrentRelation(ref double currentMin, ref double currentMax, ref double outputVoltageMin, ref double outputVoltageMax);

獲取焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取焊接電壓與輸出模擬量對應關係
    * @param [out] weldVoltageMin 焊接電壓-模擬量輸出線性關係左側點焊接電壓值(A)
    * @param [out] weldVoltageMax 焊接電壓-模擬量輸出線性關係右側點焊接電壓值(A)
    * @param [out] outputVoltageMin 焊接電壓-模擬量輸出線性關係左側點模擬量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電壓-模擬量輸出線性關係右側點模擬量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingGetVoltageRelation(ref double weldVoltageMin, ref double weldVoltageMax, ref double outputVoltageMin, ref double outputVoltageMax);

設置焊接電流
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱模擬量輸出端口(0-1)
    * @return 錯誤碼
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex);

設置焊接電壓
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] voltage 焊接電壓值(A)
    * @param [in] AOIndex 焊接電壓控制箱模擬量輸出端口(0-1)
    * @return 錯誤碼
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex);

設置擺動參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    * @return 錯誤碼 
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle, double weaveRotAngle=0);

設置焊接參數代碼示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
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

        robot.WeldingGetProcessParam(1, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 1 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);
        robot.WeldingGetProcessParam(2, ref startCurrent, ref startVoltage, ref startTime, ref weldCurrent, ref weldVoltage, ref endCurrent, ref endVoltage, ref endTime);
        Console.WriteLine("the Num 2 process param is " + startCurrent + " " + startVoltage + " " + startTime + " " + weldCurrent + " " + weldVoltage + " " + endCurrent + " " + endVoltage + " " + endTime);

        int rtn = robot.WeldingSetCurrentRelation(0, 400, 0, 10, 0);
        Console.WriteLine("WeldingSetCurrentRelation rtn is: " + rtn);

        rtn = robot.WeldingSetVoltageRelation(0, 40, 0, 10, 1);
        Console.WriteLine("WeldingSetVoltageRelation rtn is: " + rtn);

        double current_min = 0;
        double current_max = 0;
        double vol_min = 0;
        double vol_max = 0;
        double output_vmin = 0;
        double output_vmax = 0;
        int curIndex = 0;
        int volIndex = 0;
        rtn = robot.WeldingGetCurrentRelation(ref current_min, ref current_max, ref output_vmin, ref output_vmax, ref curIndex);
        Console.WriteLine("WeldingGetCurrentRelation rtn is: " + rtn);
        Console.WriteLine("current min " + current_min + " current max " + current_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingGetVoltageRelation(ref vol_min, ref vol_max, ref output_vmin, ref output_vmax, ref volIndex);
        Console.WriteLine("WeldingGetVoltageRelation rtn is: " + rtn);
        Console.WriteLine("vol min " + vol_min + " vol max " + vol_max + " output vol min " + output_vmin + " output vol max " + output_vmax);

        rtn = robot.WeldingSetCurrent(1, 100, 0, 0);
        Console.WriteLine("WeldingSetCurrent rtn is: " + rtn);

        System.Threading.Thread.Sleep(3000);

        rtn = robot.WeldingSetVoltage(1, 10, 0, 0);
        Console.WriteLine("WeldingSetVoltage rtn is: " + rtn);

        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000);
        Console.WriteLine("rtn is: " + rtn);

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);

        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        Console.WriteLine("WeldingSetCheckArcInterruptionParam    " + rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        Console.WriteLine("WeldingSetReWeldAfterBreakOffParam    " + rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(ref checkEnable, ref arcInterruptTimeLength);
        Console.WriteLine("WeldingGetCheckArcInterruptionParam  checkEnable  " + checkEnable + "   arcInterruptTimeLength  " + arcInterruptTimeLength);
        rtn = robot.WeldingGetReWeldAfterBreakOffParam(ref enable, ref length, ref velocity, ref moveType);
        Console.WriteLine("WeldingGetReWeldAfterBreakOffParam  enable = " + enable + ", length = " + length + ", velocity = " + velocity + ", moveType = " + moveType);

        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            Thread.Sleep(1000);
            robot.SetWeldMachineCtrlMode(1);
            Thread.Sleep(1000);
        }

    }

即時設置擺動參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

設置機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人焊接電弧意外中斷檢測參數
    * @param [in] checkEnable 是否使能檢測；0-不使能；1-使能
    * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
    * @return 錯誤碼
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength)

獲取機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人焊接電弧意外中斷檢測參數
    * @param [out] checkEnable 是否使能檢測；0-不使能；1-使能
    * @param [out] arcInterruptTimeLength 電弧中斷確認時長(ms)
    * @return 錯誤碼
    */
    int WeldingGetCheckArcInterruptionParam(ref int checkEnable, ref int arcInterruptTimeLength)

設置機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人焊接中斷恢復參數
    * @param[in] enable 是否使能焊接中斷恢復
    * @param[in] length 焊縫重疊距離(mm)
    * @param[in] velocity 機器人回到再起弧點速度百分比(0-100)
    * @param[in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
    * @return 錯誤碼
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType)

獲取機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取機器人焊接中斷恢復參數
    * @param [out] enable 是否使能焊接中斷恢復
    * @param [out] length 焊縫重疊距離(mm)
    * @param [out] velocity 機器人回到再起弧點速度百分比(0-100)
    * @param [out] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
    * @return 錯誤碼
    */
    int WeldingGetReWeldAfterBreakOffParam(ref int enable, ref double length, ref double velocity, ref int moveType)

設置焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊機控制模式擴展DO端口
    * @param DONum 焊機控制模式DO端口(0-127)
    * @return 錯誤碼
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

設置焊機控制模式
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊機控制模式
    * @param [in] mode 焊機控制模式;0-直流一元模式；1-脈衝一元模式；2-JOB模式；3-近控模式；4-分別模式；5-CC/CV模式；6-TIG；7-CMT
    * @param [in] ioType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @return 錯誤碼
    */
    public int SetWeldMachineCtrlMode(int mode,int ioType = 1)

焊接開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接開始
    * @param [in] ioType io類型 0-控制器IO； 1-擴展IO
    * @param [in] arcNum 焊機配置文件編號
    * @param [in] timeout 起弧超時時間
    * @return 錯誤碼
    */
    int ARCStart(int ioType, int arcNum, int timeout);

焊接結束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接結束
    * @param [in] ioType io類型 0-控制器IO； 1-擴展IO
    * @param [in] arcNum 焊機配置文件編號
    * @param [in] timeout 熄弧超時時間
    * @return 錯誤碼
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

擺動開始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 擺動開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveStart(int weaveNum);

擺動結束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 擺動結束
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveEnd(int weaveNum);

正向送絲
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 正向送絲
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

反向送絲
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 反向送絲
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

送氣
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 送氣
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    int SetAspirated(int ioType, int airControl);

設置機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人焊接中斷後恢復焊接
    * @return 錯誤碼
    */
    int WeldingStartReWeldAfterBreakOff()

設置機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置機器人焊接中斷後退出焊接
    * @return 錯誤碼
    */
    int WeldingAbortWeldAfterBreakOff()

代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL (p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(1, 0, 10000);
        robot.WeaveEnd(0);
    }

段焊開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    * @param [in] tool 工具號
    * @param [in] user 工件號
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm	 
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 錯誤碼 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout,bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos);

機器人段焊代碼示例
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        robot.WeldingSetCurrent(1, 230, 0, 0);
        robot.WeldingSetVoltage(1, 24, 0, 1);

        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.SegmentWeldStart( p1Desc,  p2Desc,  p1Joint,  p2Joint, 20, 20, 0, 0, 5000, false, 0, 0, 0, 100, 100, 100, -1,  exaxisPos, 0, 0,  offdese);
        Console.WriteLine("SegmentWeldStart rtn is {0}", rtn);
    }

仿真擺動開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真擺動開始
    * @param  [in] weaveNum  擺動參數編號
    * @return  錯誤碼
    */
    int WeaveStartSim(int weaveNum);

仿真擺動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  仿真擺動結束
    * @param  [in] weaveNum  擺動參數編號
    * @return  錯誤碼
    */
    int WeaveEndSim(int weaveNum);

開始軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  開始軌跡檢測預警(不運動)
    * @param  [in] weaveNum   擺動參數編號
    * @return  錯誤碼
    */
    int WeaveInspectStart(int weaveNum);

結束軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 結束軌跡檢測預警(不運動)
    * @param  [in] weaveNum   擺動參數編號
    * @return  錯誤碼
    */
    int WeaveInspectEnd(int weaveNum);

擺動漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  擺動漸變開始
    * @param [in] weaveChangeFlag 1-變擺動參數；2-變擺動參數+焊接速度
    * @param [in] weaveNum 擺動編號 
    * @param [in] velStart 焊接開始速度，(cm/min)
    * @param [in] velEnd 焊接結束速度，(cm/min)
    * @return  錯誤碼
    */
    int WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd);

擺動漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  擺動漸變結束
    * @return  錯誤碼
    */
    int WeaveChangeEnd()

機器人擺動漸變焊接代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose p1Desc = new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint = new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc = new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint = new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveStartSim(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveEndSim(0);
        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveInspectStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese);
        robot.WeaveInspectEnd(0);

        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveL( p1Joint,  p1Desc, 1, 1, 100, 100, 50, -1,  exaxisPos, 0, 0,  offdese);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1, 0, 50, 30);
        robot.MoveL( p2Joint,  p2Desc, 1, 1, 100, 100, 1, -1,  exaxisPos, 0, 0,  offdese);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
    }

擴展IO-配置焊機氣體檢測信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機氣體檢測信號
    * @param  [in] DONum  氣體檢測信號擴展DO編號
    * @return  錯誤碼
    */
    int SetAirControlExtDoNum(int DONum);

擴展IO-配置焊機起弧信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機起弧信號
    * @param  [in] DONum  焊機起弧信號擴展DO編號
    * @return  錯誤碼
    */
    int SetArcStartExtDoNum(int DONum);

擴展IO-配置焊機反向送絲信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機反向送絲信號
    * @param  [in] DONum  反向送絲信號擴展DO編號
    * @return  錯誤碼
    */
    int SetWireReverseFeedExtDoNum(int DONum);

擴展IO-配置焊機正向送絲信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機正向送絲信號
    * @param  [in] DONum  正向送絲信號擴展DO編號
    * @return  錯誤碼
    */
    int SetWireForwardFeedExtDoNum(int DONum);

擴展IO-配置焊機起弧成功信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機起弧成功信號
    * @param  [in] DINum  起弧成功信號擴展DI編號
    * @return  錯誤碼
    */
    int SetArcDoneExtDiNum(int DINum);

擴展IO-配置焊機準備信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊機準備信號
    * @param  [in] DINum  焊機準備信號擴展DI編號
    * @return  錯誤碼
    */
    int SetWeldReadyExtDiNum(int DINum);

擴展IO-配置焊接中斷恢復信號
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 擴展IO-配置焊接中斷恢復信號
    * @param  [in] reWeldDINum  焊接中斷後恢復焊接信號擴展DI編號
    * @param  [in] abortWeldDINum  焊接中斷後退出焊接信號擴展DI編號
    * @return  錯誤碼
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

設置擴展IO焊接信號代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button51_Click(object sender, EventArgs e)
    {
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);

        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);
    }

電弧跟蹤控制
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  電弧跟蹤控制
    * @param  [in] flag 開關，0-關；1-開
    * @param  [in] dalayTime 滯後時間，單位ms
    * @param  [in] isLeftRight 左右偏差補償
    * @param  [in] klr 左右調節係數(靈敏度)
    * @param  [in] tStartLr 左右開始補償時間cyc
    * @param  [in] stepMaxLr 左右每次最大補償量 mm
    * @param  [in] sumMaxLr 左右總計最大補償量 mm
    * @param  [in] isUpLow 上下偏差補償
    * @param  [in] kud 上下調節係數(靈敏度)
    * @param  [in] tStartUd 上下開始補償時間cyc
    * @param  [in] stepMaxUd 上下每次最大補償量 mm
    * @param  [in] sumMaxUd 上下總計最大補償量
    * @param  [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
    * @param  [in] referenceType 上下基準電流設定方式，0-反饋；1-常數
    * @param  [in] referSampleStartUd 上下基準電流採樣開始計數(反饋)，cyc
    * @param  [in] referSampleCountUd 上下基準電流採樣循環計數(反饋)，cyc
    * @param  [in] referenceCurrent 上下基準電流mA
    *  @param  [in] offsetType 偏置跟蹤類型，0-不偏置；1-採樣；2-百分比  /version 3.7.9
    * @param  [in] offsetParameter 偏置參數；採樣(偏置採樣開始時間，默認採一週期)；百分比(偏置百分比(-100 ~ 100)) /version 3.7.9
    * @return  錯誤碼
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

電弧跟蹤AI通帶選擇
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  電弧跟蹤AI通帶選擇
    * @param  [in] channel 電弧跟蹤AI通帶選擇,[0-3]
    * @return  錯誤碼
    */
    int ArcWeldTraceExtAIChannelConfig(int channel);

電弧追蹤 + 多層多道補償開啓
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 電弧追蹤 + 多層多道補償開啓
    * @return 錯誤碼
    */
    int ArcWeldTraceReplayStart();

電弧追蹤 + 多層多道補償關閉
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

        /**
         * @brief 電弧追蹤 + 多層多道補償關閉
         * @return 錯誤碼
         */
    int ArcWeldTraceReplayEnd();

偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
     * @brief 偏移量座標變化-多層多道焊
     * @param [in] pointO 基準點笛卡爾位姿
     * @param [in] pointX 基準點X向偏移方向點笛卡爾位姿
     * @param [in] pointZ 基準點Z向偏移方向點笛卡爾位姿
     * @param [in] dx x方向偏移量(mm)
     * @param [in] z方向偏移量(mm)
     * @param [in] 繞y軸偏移量(°)
     * @param [out] 計算結果偏移量
     * @return 錯誤碼
     */
    int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dy, double db, ref DescPose offset);

多層多道焊電弧跟蹤代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c#
    :linenos:

    private void button52_Click(object sender, EventArgs e)
    {
        JointPos mulitilineorigin1_joint = new JointPos(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
        DescPose mulitilineorigin1_desc = new DescPose(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);

        DescTran mulitilineX1_desc = new DescTran();
        mulitilineX1_desc.x = -677.556;
        mulitilineX1_desc.y = 211.949;
        mulitilineX1_desc.z = -1.206;

        DescTran mulitilineZ1_desc = new DescTran();
        mulitilineZ1_desc.x = -677.564;
        mulitilineZ1_desc.y = 190.956;
        mulitilineZ1_desc.z = 19.817;

        JointPos mulitilinesafe_joint = new JointPos(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
        DescPose mulitilinesafe_desc = new DescPose(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
        JointPos mulitilineorigin2_joint = new JointPos(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
        DescPose mulitilineorigin2_desc = new DescPose(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);

        DescTran mulitilineX2_desc = new DescTran();
        mulitilineX2_desc.x = -563.965;
        mulitilineX2_desc.y = 220.355;
        mulitilineX2_desc.z = -0.680;

        DescTran mulitilineZ2_desc = new DescTran();
        mulitilineZ2_desc.x = -563.968;
        mulitilineZ2_desc.y = 215.362;
        mulitilineZ2_desc.z = 4.331;

        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset = new DescPose(0, 0, 0, 0, 0, 0);

        Thread.Sleep(10);
        int error = robot.MoveJ( mulitilinesafe_joint,  mulitilinesafe_desc, 13, 0, 10, 100, 100,  epos, -1, 0,  offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.WeaveStart(0);
        Console.WriteLine("WeaveStart return: {0}", error);

        error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1,  epos, 0, 0,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10);
        Console.WriteLine("ArcWeldTraceControl return: {0}", error);

        error = robot.WeaveEnd(0);
        Console.WriteLine("WeaveEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("ArcWeldTraceReplayStart return: {0}", error);

        error = robot.MoveL( mulitilineorigin2_joint,  mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 10000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.MoveL( mulitilineorigin1_joint,  mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,  epos, 0, 1,  offset, 0, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ARCStart(1, 0, 3000);
        Console.WriteLine("ARCStart return: {0}", error);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, ref offset);
        Console.WriteLine("MultilayerOffsetTrsfToBase return: {0}  offect is {1} {2} {3}", error, offset.tran.x, offset.tran.y, offset.tran.z);

        error = robot.ArcWeldTraceReplayStart();
        Console.WriteLine("MoveJ return: {0}", error);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 1, 2, 100, 100, -1, epos, 1, 1, offset, 1, 100);
        Console.WriteLine("MoveL return: {0}", error);

        error = robot.ArcWeldTraceReplayEnd();
        Console.WriteLine("ArcWeldTraceReplayEnd return: {0}", error);

        error = robot.ARCEnd(1, 0, 3000);
        Console.WriteLine("ARCEnd return: {0}", error);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);
        Console.WriteLine("MoveJ return: {0}", error);
    }

電弧跟蹤焊機電流反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:
    
    /**
    * @brief 電弧跟蹤焊機電流反饋AI通道選擇
    * @param [in]  channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelCurrent(int channel);

電弧跟蹤焊機電壓反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電壓反饋AI通道選擇
    * @param [in]  channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelVoltage(int channel);

電弧跟蹤焊機電流反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電流反饋轉換參數
    * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
    * @param [in] currentLow AI通道下限對應焊機電流值，默認值0V，範圍[0-200V]
    * @param [in] currentHigh AI通道上限對應焊機電流值，默認值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    public int ArcWeldTraceCurrentPara(double AILow, double AIHigh, double currentLow, double currentHigh)

電弧跟蹤焊機電壓反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電壓反饋轉換參數
    * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
    * @param [in] voltageLow AI通道下限對應焊機電壓值，默認值0V，範圍[0-200V]
    * @param [in] voltageHigh AI通道上限對應焊機電壓值，默認值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    public int ArcWeldTraceVoltagePara(double AILow, double AIHigh, double voltageLow, double voltageHigh)

電弧跟蹤代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void button8_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(441.901, 416.508, -51.979, -179.234, 0.718, -115.305);
        JointPos startjointPos = new JointPos(-146.22, -60.551, 104.859, -135.317, -90.289, 59.088);

        DescPose enddescPose = new DescPose(441.901, 615.317, -51.979, -179.234, 0.718, -115.305);
        JointPos endjointPos = new JointPos(-133.22, -44.193, 74.934, -121.661, -90.509, 72.087);

        DescPose safetydescPose = new DescPose(441.901, 416.508, -51.979, -179.234, 0.718, -115.305);
        JointPos safetyjointPos = new JointPos(-146.22, -60.551, 104.859, -135.317, -90.289, 59.088);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);
        robot.WeldingSetVoltage(0, 25, 1, 0); 
        robot.WeldingSetCurrent(0, 260, 0, 0); 

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        Console.WriteLine("ArcWeldTraceAIChannelCurrent rtn is " + rtn);
        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        Console.WriteLine("ArcWeldTraceAIChannelVoltage rtn is " + rtn);
        rtn = robot.ArcWeldTraceCurrentPara((double)0, (double)5, (double)0, (double)500);
        Console.WriteLine("ArcWeldTraceCurrentPara rtn is " + rtn);
        rtn = robot.ArcWeldTraceVoltagePara((double)1.018, (double)10, (double)0, (double)50);
        Console.WriteLine("ArcWeldTraceVoltagePara rtn is " + rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
            robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, 0,exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.MoveJ(safetyjointPos, safetydescPose, 1, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);

    }

設置焊絲尋位擴展IO端口
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊絲尋位擴展IO端口
    * @param searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param searchStartDONum 焊絲尋位啓停控制DO端口(0-127)
    * @return 錯誤碼
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊絲尋位開始
    * @param  [in] refPos  1-基準點 0-接觸點
    * @param  [in] searchVel   尋位速度 %
    * @param  [in] searchDis  尋位距離 mm
    * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param  [in] autoBackVel  自動返回速度 %
    * @param  [in] autoBackDis  自動返回距離 mm
    * @param  [in] offectFlag  1-帶偏移量尋位；0-示教點尋位
    * @return  錯誤碼
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊絲尋位結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊絲尋位結束
    * @param  [in] refPos  1-基準點 2-接觸點
    * @param  [in] searchVel   尋位速度 %
    * @param  [in] searchDis  尋位距離 mm
    * @param  [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param  [in] autoBackVel  自動返回速度 %
    * @param  [in] autoBackDis  自動返回距離 mm
    * @param  [in] offectFlag  1-帶偏移量尋位；2-示教點尋位
    * @return  錯誤碼
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

計算焊絲尋位偏移量
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  計算焊絲尋位偏移量
    * @param  [in] seamType  焊縫類型
    * @param  [in] method   計算方法
    * @param  [in] varNameRef 基準點1-6，“#”表示無點變量
    * @param  [in] varNameRes 接觸點1-6，“#”表示無點變量
    * @param  [out] offectFlag 0-偏移量直接疊加到指令點；1-偏移量需要對指令點進行座標變換
    * @param  [out] offect 偏移位姿[x, y, z, a, b, c]
    * @return  錯誤碼
    */
    int GetWireSearchOffset(int seamType, int method, string[] varNameRef, string[] varNameRes, ref int offsetFlag, ref DescPose offset);

等待焊絲尋位完成
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  等待焊絲尋位完成
    * @return  錯誤碼
    */
    int WireSearchWait(string name);

焊絲尋位接觸點寫入數據庫
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  焊絲尋位接觸點寫入數據庫
    * @param  [in] varName  接觸點名稱 “RES0” ~ “RES99”
    * @param  [in] pos  接觸點數據[x, y, x, a, b, c]
    * @return  錯誤碼
    */
    int SetPointToDatabase(string varName, DescPose pos);

機器人焊絲尋位代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button53_Click(object sender, EventArgs e)
    {
        DescPose toolCoord=new DescPose(0, 0, 200, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);
        DescPose wobjCoord=new DescPose(0, 0, 0, 0, 0, 0);
        robot.SetWObjCoord(1, wobjCoord, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(216.543, 445.175, 93.465, 179.683, 1.757, -112.641);
        JointPos jointStart = new JointPos(-128.345, -86.660, 114.679, -119.625, -89.219, 74.303);

        DescPose descEnd = new DescPose(111.143, 523.384, 87.659, 179.703, 1.835, -97.750);
        JointPos jointEnd = new JointPos(-113.454, -81.060, 109.328, -119.954, -89.218, 74.302);

        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);

        DescPose descREF0A = new DescPose(142.135, 367.604, 86.523, 179.728, 1.922, -111.089);
        JointPos jointREF0A = new JointPos(-126.794, -100.834, 128.922, -119.864, -89.218, 74.302);

        DescPose descREF0B = new DescPose(254.633, 463.125, 72.604, 179.845, 2.341, -114.704);
        JointPos jointREF0B = new JointPos(-130.413, -81.093, 112.044, -123.163, -89.217, 74.303);

        DescPose descREF1A = new DescPose(92.556, 485.259, 47.476, -179.932, 3.130, -97.512);
        JointPos jointREF1A = new JointPos(-113.231, -83.815, 119.877, -129.092, -89.217, 74.303);

        DescPose descREF1B = new DescPose(203.103, 583.836, 63.909, 179.991, 2.854, -103.372);
        JointPos jointREF1B = new JointPos(-119.088, -69.676, 98.692, -121.761, -89.219, 74.303);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);  //方向點
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        string[] varNameRef = { "REF0", "REF1", "#", "#", "#", "#" };
        string[] varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };
        int offectFlag = 0;
        DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, ref offectFlag, ref offectPos);
        robot.PointsOffsetEnable(0, offectPos);
        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1, exaxisPos, 0, 0, offdese);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, exaxisPos, 1, 0, offdese);
        robot.PointsOffsetDisable();
    }

設置焊接電壓漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend);

設置焊接電壓漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電壓漸變結束
    * @return 錯誤碼
    */
    int WeldingSetVoltageGradualChangeEnd();

設置焊接電流漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
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
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend);

設置焊接電流漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 設置焊接電流漸變結束
    * @return 錯誤碼
    */
    int WeldingSetCurrentGradualChangeEnd();

機器人焊接電流電壓漸變代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        DescPose startdescPose = new DescPose(-319.303, -240.689, 116.379, -175.879, -0.337, 148.239);
        JointPos startjointPos = new JointPos(20.474, -103.554, 126.774, -116.682, -87.746, -37.709);

        DescPose enddescPose = new DescPose(-454.166, -327.159, 62.217, 177.199, -2.276, 154.955);
        JointPos endjointPos = new JointPos(27.176, -74.423, 104.557, -119.315, -93.514, -37.698);

        DescPose safedescPose = new DescPose(-375.533, -543.319, 19.798, 177.486, -2.489, 175.825);
        JointPos safejointPos = new JointPos(48.074, -59.714, 89.955, -119.777, -93.508, -37.683);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.WeldingSetCurrentRelation(0, 495, 1, 10, 0);
        robot.WeldingSetVoltageRelation(10, 45, 1, 10, 1);

        robot.WeldingSetVoltage(0, 25, 1, 0);//
        robot.WeldingSetCurrent(0, 260, 0, 0);// 

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        int rtn = robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        Console.WriteLine($"WeldingSetCurrentGradualChangeStart rtn is {rtn}");
        rtn = robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        Console.WriteLine($"WeldingSetVoltageGradualChangeStart rtn is {rtn}");

        rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        Console.WriteLine($"ArcWeldTraceControl rtn is {rtn}");

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        rtn = robot.WeaveChangeStart(2, 1, 24, 36);
        Console.WriteLine($"WeaveChangeStart rtn is {rtn}");
        //robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }

設置自定義擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 設置自定義擺動參數
     * @param [in] id 自定義擺動編號：0-2
     * @param [in] pointNum 擺動點位個數 0-10
     * @param [in] point 移動端點數據x,y,z
     * @param [in] stayTime 擺動停留時間ms
     * @param [in] frequency 擺動頻率 Hz
     * @param [in] incStayType 等待模式：0-週期不包含等待時間；1-週期包含等待時間
     * @param [in] stationary 擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止
     * @return  錯誤碼
     */
    public int CustomWeaveSetPara(int id, int pointNum, DescTran[] points, double[] stayTimes, double frequency, int incStayType, int stationary)

獲取自定義擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    /**
     * @brief 獲取自定義擺動參數
     * @param [in] id 自定義擺動編號：0-2
     * @param [out] pointNum 擺動點位個數 0-10
     * @param [out] point 移動端點數據x,y,z
     * @param [out] stayTime 擺動停留時間ms
     * @param [out] frequency 擺動頻率 Hz
     * @param [out] incStayType 等待模式：0-週期不包含等待時間；1-週期包含等待時間
     * @param [out] stationary 擺動位置等待：0-等待時間內繼續運動；1-等待時間內位置靜止
     * @return  錯誤碼
     */
    public int CustomWeaveGetPara(int id, ref int pointNum, ref DescTran[] points, ref double[] stayTimes, ref double frequency, ref int incStayType, ref int stationary)

自定義擺動參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.8  Web-3.8.6

.. code-block:: c#
    :linenos:

    public void TestCoordMain5()
    {  
        DescTran[] points = new DescTran[10];
        for (int i = 0; i < 10; i++)
        {
            points[i] = new DescTran();
        }
        points[0].x = -3;
        points[0].y = -3;
        points[0].z = 0;
        points[1].x = -6;
        points[1].y = 0;
        points[1].z = 0;
        points[2].x = -3;
        points[2].y = 3;
        points[2].z = 0;
        points[3].x = 0;
        points[3].y = 0;
        points[3].z = 0;
        double[] stayTimes = new double[10] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        int rtn = robot.CustomWeaveSetPara(2, 4, points, stayTimes, 1.000, 0, 0);
        Console.WriteLine($"CustomWeaveSetPara rtn is {rtn}");
        System.Threading.Thread.Sleep(1000);
        int pointNum = 0;
        double frequency = 0;
        int incStayType = 0;
        int stationary = 0;
        rtn = robot.CustomWeaveGetPara(2, ref pointNum, ref points, ref stayTimes, ref frequency, ref incStayType, ref stationary);
        Console.WriteLine($"pointNum is {pointNum}");
        for (int i = 0; i < pointNum; i++)
        {
            Console.WriteLine($"point {i}, point x y z {points[i].x:F6} {points[i].y:F6} {points[i].z:F6}");
        }
        Console.WriteLine($"fre is {frequency:F6}, stay is {incStayType} {stationary}");
        robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000, 6.000000, 5.000000, 50, 100, 100, 0, 1, 0.000000, 0.000000);
        DescPose desc_p1 = new DescPose(-288.650, 367.807, 288.404, 0.000, -0.001, 0.001);
        DescPose desc_p2 = new DescPose(-431.714, 367.815, 288.415, 0.001, 0.001, 0.000);    
        DescPose desc_p3 = new DescPose(-348.666, 427.798, 288.404, -0.000, -0.000, 0.001);
        JointPos j1 = new JointPos(140.656,  -84.560,  -91.707, -93.734,  90.000,50.655 );
        JointPos j2 = new JointPos ( 149.873, -98.298, -77.599,  -94.103,  90.000,  59.873 );
        JointPos j3 = new JointPos (139.773,  -96.173, -80.014,  -93.814,  90.000,  49.772 );
        ExaxisPos epos = new ExaxisPos(0,0,0,0);
        DescPose offset_pos = new DescPose(0,0,0,0,0,0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.Circle(j3, desc_p3, 3, 0, 100, 100, epos, j2, desc_p2, 3, 0, 100, 100, epos, 10, -1, offset_pos, 100, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveC(j3, desc_p3, 3, 0, 100, 100, epos, 0, offset_pos, j2, desc_p2, 3, 0, 100, 100, epos, 0, offset_pos, 10, -1, 0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2, 3, 0, 100, 100, 10, -1, epos, 0, 0, offset_pos, 0, 0, 10);
        robot.WeaveEnd(0);
    }

雷射焊機參數配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 寫入雷射焊機10個工藝組中某一個的配置參數並配置給焊機
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[in] num 需要設置的組號（1~10）
    * @param[in] scanSpeed 掃描速度
    * @param[in] scanWidth 掃描寬度
    * @param[in] peakPower 峰值功率
    * @param[in] dutyCycle 占空比
    * @param[in] freq 頻率
    * @return 錯誤碼
    */
    public int SetLaserWeldingParam(int io_type, int num, int scanSpeed, int scanWidth, int peakPower, int dutyCycle, int freq)

設置雷射焊接開始停止
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 設置雷射焊機開啟關閉
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[in] status 控制字 0-收光 1-出光
    * @param[in] max_waittime 最大等待時間
    * @return 錯誤碼
    */
    public int SetLaserWeldingStartEnd(int io_type, int status, int max_waittime)

雷射焊機使能去使能
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 雷射焊機使能去使能
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[in] status 0-去使能 1-使能
    * @return 錯誤碼
    */
    public int SetLaserWeldingEnable(int io_type, int status)

雷射焊機故障復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 雷射焊機故障復位
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[in] status 控制字 0-無效 1-故障復位
    * @return 錯誤碼
    */
    public int ResetLaserWeldingErr(int io_type, int status)

獲取雷射焊機運行狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取雷射焊機運行狀態
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[out] status 控制字 0-停機 1-運行
    * @return 錯誤碼
    */
    public int GetLaserWeldingRunningState(int io_type, ref int status)

獲取雷射焊機故障狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取雷射焊機故障狀態
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[out] status 0-無故障 1-存在故障
    * @return 錯誤碼
    */
    public int GetLaserWeldingErrState(int io_type, ref int status)

獲取雷射焊機配置參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取雷射焊機10個工藝組中某一個的配置參數
    * @param[in] num 需要設置的組號（1~10）
    * @param[out] scanSpeed 掃描速度
    * @param[out] scanWidth 掃描寬度
    * @param[out] peakPower 峰值功率
    * @param[out] dutyCycle 占空比
    * @param[out] freq 頻率
    * @return 錯誤碼
    */
    public int GetLaserWeldingParamTarget(int num, ref int scanSpeed, ref int scanWidth, ref int peakPower, ref int dutyCycle, ref int freq)

獲取當前雷射焊機生效的配置參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取當前雷射焊機生效的配置參數
    * @param[in] io_type 通訊類型 0-IO 1-UDP
    * @param[out] scanSpeed 掃描速度
    * @param[out] scanWidth 掃描寬度
    * @param[out] peakPower 峰值功率
    * @param[out] dutyCycle 占空比
    * @param[out] freq 頻率
    * @return 錯誤碼
    */
    public int GetLaserWeldingParamActual(int io_type, ref int scanSpeed, ref int scanWidth, ref int peakPower, ref int dutyCycle, ref int freq)
    
配置雷射焊機擴展IO使能DO端口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，使能的DO端口
    * @param[in] ctrlModeDONum 雷射焊機使能的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingEnableExtDoNum(int ctrlModeDONum)

配置雷射焊機擴展IO啟動DO端口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，啟動的DO端口
    * @param[in] ctrlModeDONum 雷射焊機啟動（出光收光）的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingStartExtDoNum(int ctrlModeDONum)

雷射焊機設置擴展IO故障復位的DO端口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，故障復位的DO端口
    * @param[in] ctrlModeDONum 雷射焊機故障復位的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingErrResetExtDoNum(int ctrlModeDONum)

配置雷射焊機運行狀態（出光狀態）擴展DI
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 配置雷射焊機運行狀態（出光狀態）擴展DI
    * @param[in] diNum 配置雷射焊機運行狀態（出光狀態）擴展DI端口
    * @return 錯誤碼
    */
    public int SetLaserWeldingRunningStateExtDiNum(int diNum)
    
配置雷射焊機擴展IO故障狀態DI端口
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief 配置雷射焊機故障狀態擴展DI
    * @param[in] diNum 配置雷射焊機故障狀態擴展DI端口
    * @return 錯誤碼
    */
    public int SetLaserWeldingErrStateExtDiNum(int diNum)
        
雷射焊接代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    private void btnLaserWeld_Click(object sender, EventArgs e)
    {

        int rtn = -1;
        // 載入UDP驅動
        rtn = robot.ExtDevLoadUDPDriver();
        if (rtn != 0)
        {
            Console.WriteLine("Failed to load UDP driver, error code: " + rtn);
        }
        Thread.Sleep(1000);

        // 設置雷射焊接參數: io_type=1, num=3, scanSpeed=2000, scanWidth=3, peakPower=1500, dutyCycle=100, freq=1000
        rtn = robot.SetLaserWeldingParam(1, 3, 2000, 3, 1500, 100, 1000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingParam failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("SetLaserWeldingParam success");
        }

        // 設置啟動的DO端口號
        rtn = robot.SetLaserWeldingStartExtDoNum(1);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartExtDoNum failed, error code: " + rtn);
        }

        // 設置為模式0（示教模式）
        rtn = robot.Mode(0);
        if (rtn != 0)
        {
            Console.WriteLine("Set mode 0 failed, error code: " + rtn);
        }
        Thread.Sleep(1000);


        DescPose desc_pos1 = new DescPose(-303.721, -206.960, 297.105, 152.209, 19.857, 109.166);
        DescPose desc_pos2 = new DescPose(-301.575, -254.888, 284.786, 155.919, 26.946, 111.629);
        DescPose desc_safe = new DescPose(-344.386, -280.830, 435.073, 173.835, 15.333, 124.931);


        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offset = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        // 移動到第一個焊接點
        int error = robot.MoveL(desc_pos1, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to pos1 return: " + error);

        // 開啟雷射（出光）
        rtn = robot.SetLaserWeldingStartEnd(1, 1, 10000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartEnd (start) failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("Laser started");
        }

        // 移動到第二個焊接點（焊接過程中）
        rtn = robot.MoveL(desc_pos2, 0, 0, 30, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to pos2 return: " + rtn);

        Thread.Sleep(500);
        // 關閉雷射（收光）
        rtn = robot.SetLaserWeldingStartEnd(1, 0, 10000);
        if (rtn != 0)
        {
            Console.WriteLine("SetLaserWeldingStartEnd (stop) failed, error code: " + rtn);
        }
        else
        {
            Console.WriteLine("Laser stopped");
        }

        // 移動到安全點
        rtn = robot.MoveL(desc_safe, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0);
        Console.WriteLine("MoveL to safe_pos return: " + rtn);

        // 設置為模式1（遠程模式）
        rtn = robot.Mode(1);
        if (rtn != 0)
        {
            Console.WriteLine("Set mode 1 failed, error code: " + rtn);
        }
        Thread.Sleep(1000);

        // 關閉連接
        robot.CloseRPC();
        Thread.Sleep(1000);

        Console.WriteLine("Test completed");

        return ;
    }

設置擺動結束回週期零點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  設置擺動結束回週期零點
    * @param [in] flag 擺動結束是否回週期零點；0-不回週期零點；1-回週期零點
    * @return  錯誤碼
    */
    public int SetWeavebackCenterConfig(int flag) 
           
獲取擺動結束回週期零點參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    /**
    * @brief  獲取擺動結束回週期零點參數
    * @param [out] flag 擺動結束是否回週期零點；0-不回週期零點；1-回週期零點
    * @return  錯誤碼
    */
    public int GetWeavebackCenterConfig(ref int flag)
           
擺動結束回週期零點代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c#
    :linenos:

    public void TestSplineWeave()
    {
        int rtn;

        // 擺動回中心配置
        robot.SetWeavebackCenterConfig(1);
        int weaveBackConfig = 0;
        robot.GetWeavebackCenterConfig(ref weaveBackConfig);
        Console.WriteLine("GetWeavebackCenterConfig: {0}", weaveBackConfig);

        JointPos j1 = new JointPos(9.000, -66.067, 67.706, -103.217, -90.151, 100.669);
        JointPos j2 = new JointPos(-4.660, -107.973, 103.734, -76.214, -89.999, 90.886);
        JointPos j3 = new JointPos(-36.762, -77.380, 91.364, -127.159, -90.024, 54.833);
        JointPos j4 = new JointPos(-62.875, -89.460, 86.437, -77.030, -90.012, 31.539);
        DescPose desc_pos1 = new DescPose(-654.129, -235.344, 246.543, 6.010, -11.535, -176.787);
        DescPose desc_pos2 = new DescPose(-273.710, -100.871, 280.935, 5.692, 9.522, 179.512);
        DescPose desc_pos3 = new DescPose(-566.093, 311.278, 215.008, -10.453, -17.486, -174.209);
        DescPose desc_pos4 = new DescPose(-246.558, 328.240, 292.173, 13.912, 4.437, -179.067);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 2;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 20.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;

        robot.SetSpeed(1);

        // 移動到起始點j1
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, 100.0f, epos, blendT, flag, offset_pos);
        Console.WriteLine("MoveJ to j1 rtn: {0}", rtn);

        // 擺動 + 樣條曲線運動
        robot.WeaveStart(0);
        robot.NewSplineStart(0, 6000);
        robot.NewSplinePoint(j1, desc_pos1, tool, user, vel, acc, ovl, -1.0f, 0);
        robot.NewSplinePoint(j2, desc_pos2, tool, user, vel, acc, ovl, -1.0f, 0);
        robot.NewSplinePoint(j3, desc_pos3, tool, user, vel, acc, ovl, -1.0f, 0);
        robot.NewSplinePoint(j4, desc_pos4, tool, user, vel, acc, ovl, -1.0f, 1);
        robot.NewSplineEnd();

        Console.WriteLine("TestSplineWeave completed");
    }