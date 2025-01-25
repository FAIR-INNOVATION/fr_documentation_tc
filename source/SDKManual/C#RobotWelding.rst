機器人焊接
=============

.. toctree:: 
    :maxdepth: 5

焊接開始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 焊接開始
    * @param [in] ioType io 類型 0-控制器IO；1-擴展IO
    * @param [in] arcNum 焊機設定檔編號
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
    * @param [in] ioType io 類型 0-控制器IO；1-擴展IO
    * @param [in] arcNum 焊機設定檔編號
    * @param [in] timeout 熄弧超時時間
    * @return 錯誤碼
    */
    int ARCEnd(int ioType, int arcNum, int timeout);

設定焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊接電流與輸出模擬量對應關係
    * @param [in] currentMin 焊接電流-類比量輸出線性關係左點電流值(A)
    * @param [in] currentMax 焊接電流-類比量輸出線性關係右側點電流值(A)
    * @param [in] outputVoltageMin 焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingSetCurrentRelation(double currentMin, double currentMax, double outputVoltageMin, double outputVoltageMax);

設定焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊接電壓與輸出模擬量對應關係
    * @param [in] weldVoltageMin 焊接電壓-類比輸出線性關係左點焊接電壓值(A)
    * @param [in] weldVoltageMax 焊接電壓-類比輸出線性關係右側點焊接電壓值(A)
    * @param [in] outputVoltageMin 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    * @param [in] outputVoltageMax 焊接電壓-類比輸出線性關係右側點類比輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingSetVoltageRelation(double weldVoltageMin, double weldVoltageMax, double outputVoltageMin, double outputVoltageMax);

取得焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 取得焊接電流與輸出模擬量對應關係
    * @param [out] currentMin 焊接電流-類比量輸出線性關係左點電流值(A)
    * @param [out] currentMax 焊接電流-類比量輸出線性關係右側點電流值(A)
    * @param [out] outputVoltageMin 焊接電流-類比輸出線性關係左側點類比量輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電流-類比輸出線性關係右側點類比量輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingGetCurrentRelation(ref double currentMin, ref double currentMax, ref double outputVoltageMin, ref double outputVoltageMax);

取得焊接電壓與輸出類比對應關係
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 取得焊接電壓與輸出類比對應關係
    * @param [out] weldVoltageMin 焊接電壓-類比輸出線性關係左點焊接電壓值(A)
    * @param [out] weldVoltageMax 焊接電壓-類比輸出線性關係右側點焊接電壓值(A)
    * @param [out] outputVoltageMin 焊接電壓-類比輸出線性關係左側點類比輸出電壓值(V)
    * @param [out] outputVoltageMax 焊接電壓-類比輸出線性關係右側點類比輸出電壓值(V)
    * @return 錯誤碼
    */
    int WeldingGetVoltageRelation(ref double weldVoltageMin, ref double weldVoltageMax, ref double outputVoltageMin, ref double outputVoltageMax);

設定焊接電流
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱類比輸出端口(0-1)
    * @return 錯誤碼
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex);

設定焊接電壓
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 設定焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] voltage 焊接電壓值(A)
    * @param [in] AOIndex 焊接電壓控制箱類比輸出端口(0-1)
    * @return 錯誤碼
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex);

設定擺動參數
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

即时設定擺動參數
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

擺盪開始
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 擺盪開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveStart(int weaveNum);

擺盪結束
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    /**
    * @brief 擺盪結束
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
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] wireFeed 送絲控制 0-停止送絲；1-送絲
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
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] wireFeed 送絲控制 0-停止送絲；1-送絲
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
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    int SetAspirated(int ioType, int airControl);

段焊
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
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
    * @param [in] tool 工具號
    * @param [in] user 工件號
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm	 
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件坐標系下偏移，2-工具坐標系下偏移
    * @param [in] offset_pos  位元位偏移量
    * @return 錯誤碼 
    */
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType, int arcNum, int weldTimeout,bool isWeave, int weaveNum, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, byte search, byte offset_flag, DescPose offset_pos);

代碼範例
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.0.4

.. code-block:: c#
    :linenos:

    private void btnWeldStart_Click(object sender, EventArgs e)
    {
        Robot robot = new Robot();
        robot.RPC("192.168.58.2");
        DescPose startdescPose = new DescPose(-525.55, 562.3, 417.199, -178.325, 0.847, 31.109);
        JointPos startjointPos = new JointPos(-58.978, -76.817, 112.494, -127.348, -89.145, -0.063);
        DescPose enddescPose = new DescPose(-345.155, 535.733, 421.269, 179.475, 0.571, 18.332);
        JointPos endjointPos = new JointPos(-71.746, -87.177, 123.953, -126.25, -89.429, -0.089);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        robot.WeldingSetCurrentRelation(0, 400, 0, 10);
        robot.WeldingSetVoltageRelation(0, 40, 0, 10);
        double curmin = 0;
        double curmax = 0;
        double vurvolmin = 0;
        double curvolmax = 0;
        double volmax = 0;
        double volmin = 0;
        double volvolmin = 0;
        double volvolmax = 0;

        robot.WeldingGetCurrentRelation(ref curmin, ref curmax, ref vurvolmin, ref curvolmax);
        robot.WeldingGetVoltageRelation(ref volmin, ref volmax, ref volvolmin, ref volvolmax);

        robot.WeldingSetCurrent(0, 100, 0); 
        robot.WeldingSetVoltage(0, 19, 1);

        robot.WeaveSetPara(0,0,1,0,10,100,100,0,0);

        robot.SetForwardWireFeed(0, 1);
        Thread.Sleep(1000);
        robot.SetForwardWireFeed(0, 0);
        robot.SetReverseWireFeed(0, 1);
        Thread.Sleep(1000);
        robot.SetReverseWireFeed(0, 0);
        robot.SetAspirated(0, 1);
        Thread.Sleep(1000);
        robot.SetAspirated(0, 0);

        robot.SetSpeed(5);
        robot.MoveL(startjointPos, startdescPose, 1, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        robot.ARCStart(0, 0, 1000);
        robot.WeaveStart(0);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 100, 0, exaxisPos, 0, 0, offdese);
        robot.ARCEnd(0, 0, 1000);
        robot.WeaveEnd(0);
    }



