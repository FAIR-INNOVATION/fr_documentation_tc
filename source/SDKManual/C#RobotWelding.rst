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

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 焊絲尋位開始
 * @param [in] refPos 1-基準點 2-接觸點
 * @param [in] searchVel 尋位速度 %
 * @param [in] searchDis 尋位距離 mm
 * @param [in] autoBackFlag 自動返回標誌，0-不自動；-自動
 * @param [in] autoBackVel 自動回傳速度 %
 * @param [in] autoBackDis 自動返回距離 mm
 * @param [in] offectFlag 1-帶偏移量尋位；2-示教點尋位
 * @return 錯誤碼
 */
 int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊絲尋位結束
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 焊絲尋位結束
 * @param [in] refPos 1-基準點 2-接觸點
 * @param [in] searchVel 尋位速度 %
 * @param [in] searchDis 尋位距離 mm
 * @param [in] autoBackFlag 自動返回標誌，0-不自動；-自動
 * @param [in] autoBackVel 自動回傳速度 %
 * @param [in] autoBackDis 自動返回距離 mm
 * @param [in] offectFlag 1-帶偏移量尋位；2-示教點尋位
 * @return 錯誤碼
 */
 int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

計算焊絲尋位偏移量
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 計算焊絲尋位偏移量
 * @param [in] seamType 焊縫類型
 * @param [in] method 計算方法
 * @param [in] varNameRef 基準點1-6，「#」表示無點變數
 * @param [in] varNameRes 接觸點1-6，「#」表示無點變數
 * @param [out] offectFlag 0-偏移量直接疊加到指令點；1-偏移量需要對指令點進行座標變換
 * @param [out] offect 偏移位姿[x, y, z, a, b, c]
 * @return 錯誤碼
 */
 int GetWireSearchOffset(int seamType, int method, string[] varNameRef, string[] varNameRes, ref int offsetFlag, ref DescPose offset);

等待焊絲尋位完成
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 等待焊絲尋位完成
 * @return 錯誤碼
 */
 int WireSearchWait(string name);

焊絲尋位接觸點寫入資料庫
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 焊絲尋位接觸點寫入資料庫
 * @param [in] varName 接觸點名稱 “RES0” ~ “RES99”
 * @param [in] pos 接觸點資料[x, y, x, a, b, c]
 * @return 錯誤碼
 */
 int SetPointToDatabase(string varName, DescPose pos);

電弧追蹤控制
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 電弧追蹤控制
 * @param [in] flag 開關，0-關；1-開
 * @param [in] dalayTime 滯後時間，單位ms
 * @param [in] isLeftRight 左右偏誤補償
 * @param [in] klr 左右調節係數(靈敏度)
 * @param [in] tStartLr 左右開始補償時間cyc
 * @param [in] stepMaxLr 左右每次最大補償量 mm
 * @param [in] sumMaxLr 左右總計最大補償量 mm
 * @param [in] isUpLow 上下偏差補償
 * @param [in] kud 上下調節係數(靈敏度)
 * @param [in] tStartUd 上下開始補償時間cyc
 * @param [in] stepMaxUd 上下每次最大補償量 mm
 * @param [in] sumMaxUd 上下總計最大補償量
 * @param [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
 * @param [in] referenceType 上下基準電流設定方式，0-回饋；1-常數
 * @param [in] referSampleStartUd 上下基準電流採樣開始計數(反饋)，cyc
 * @param [in] referSampleCountUd 上下基準電流採樣循環計數(反饋)，cyc
 * @param [in] referenceCurrent 上下基準電流mA
 * @param  [in] offsetType 偏移追蹤類型，0-不偏移；1-取樣；2-百分比  /version 3.8.0
 * @param  [in] offsetParameter 偏移參數；取樣(偏移取樣開始時間，預設取一週期)；百分比(偏移百分比(-100 ~ 100))
 * @return  錯誤碼
 */
 int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

程式碼範例
++++++++++++++++++++++++++++++++++

.. versionadded:: C#SDK-v1.1.0

.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {

        //電弧追蹤
        DescPose p1Desc = new DescPose(-72.912, -587.664, 31.849, 43.283, -6.731, 15.068);
        JointPos p1Joint = new JointPos(74.620, -80.903, 94.608, -109.882, -90.436, -13.432);

        DescPose p2Desc = new DescPose(-104.915, -483.712, -25.231, 42.228, -6.572, 18.433);
        JointPos p2Joint = new JointPos(66.431, -92.875, 116.362, -120.516, -88.627, -24.731);

        DescPose p3Desc = new DescPose(-242.834, -498.697, -23.681, 46.576, -5.286, 8.318);
        JointPos p3Joint = new JointPos(57.153, -82.046, 104.060, -116.659, -92.478, -24.735);
        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveJ(p1Joint, p1Desc, 1, 1, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveL(p2Joint, p2Desc, 1, 1, 100, 100, 50, -1, exaxisPos, 0, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 60, 0, 0, 4, 1, 10, 2, 2);
        robot.WeaveStart(0);
        robot.MoveL(p3Joint, p3Desc, 1, 1, 100, 100, 1, -1, exaxisPos, 0, 0, offdese);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 60, 0, 0, 4, 1, 10, 2, 2);
        robot.ARCEnd(1, 0, 10000);
    }

電弧追蹤AI通帶選擇
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 電弧追蹤AI通帶選擇
 * @param [in] channel 電弧追蹤AI通帶選擇,[0-3]
 * @return 錯誤碼
 */
 int ArcWeldTraceExtAIChannelConfig(int channel);

仿真擺動開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 仿真擺動開始
 * @param [in] weaveNum 擺動參數編號
 * @return 錯誤碼
 */
 int WeaveStartSim(int weaveNum);

仿真擺動結束
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 仿真擺動結束
 * @param [in] weaveNum 擺動參數編號
 * @return 錯誤碼
 */
 int WeaveEndSim(int weaveNum);

開始軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 開始軌跡偵測預警(不動作)
 * @param [in] weaveNum 擺動參數編號
 * @return 錯誤碼
 */
 int WeaveInspectStart(int weaveNum);

結束軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 結束軌跡偵測預警(不動作)
 * @param [in] weaveNum 擺動參數編號
 * @return 錯誤碼
 */
 int WeaveInspectEnd(int weaveNum);

擴展IO-配置焊機氣體偵測訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機氣體偵測訊號
 * @param [in] DONum 氣體偵測訊號擴展DO編號
 * @return 錯誤碼
 */
 int SetAirControlExtDoNum(int DONum);

擴充IO-配置焊接機起弧訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機起弧訊號
 * @param [in] DONum 焊機起弧訊號擴展DO編號
 * @return 錯誤碼
 */
 int SetArcStartExtDoNum(int DONum);

擴充IO-配置焊接機反向送絲訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機反向送絲訊號
 * @param [in] DONum 反向送絲訊號擴充DO編號
 * @return 錯誤碼
 */
 int SetWireReverseFeedExtDoNum(int DONum);

擴充IO-配置焊接機正向送絲訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機正向送線訊號
 * @param [in] DONum 正向送絲訊號擴展DO編號
 * @return 錯誤碼
 */
 int SetWireForwardFeedExtDoNum(int DONum);

擴充IO-配置焊接機起弧成功訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機起弧成功訊號
 * @param [in] DINum 起弧成功訊號擴展DI編號
 * @return 錯誤碼
 */
 int SetArcDoneExtDiNum(int DINum);

擴充IO-配置焊接機準備訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴充IO-配置焊接機準備訊號
 * @param [in] DINum 焊接機準備訊號擴充DI編號
 * @return 錯誤碼
 */
 int SetWeldReadyExtDiNum(int DINum);

擴展IO-配置焊接中斷恢復訊號
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 擴展IO-配置焊接中斷恢復訊號
 * @param [in] reWeldDINum 焊接中斷後恢復焊接訊號擴展DI編號
 * @param [in] abortWeldDINum 焊接中斷後退出焊接訊號擴展DI編號
 * @return 錯誤碼
 */
 nt SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

電弧追蹤 + 多層多道補償開啟
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 電弧追蹤 + 多層多道補償開啟
 * @return 錯誤碼
 */
 int ArcWeldTraceReplayStart();

電弧追蹤 + 多層多道補償關閉
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 電弧追蹤 + 多層多道補償關閉
 * @return 錯誤碼
 */
 int ArcWeldTraceReplayEnd();

偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 偏移量座標變化-多層多道焊
 * @param [in] pointO 基準點笛卡爾位姿
 * @param [in] pointX 基準點X向偏移方向點笛卡爾位姿
 * @param [in] pointZ 基準點Z向偏移方向點笛卡爾位姿
 * @param [in] dx x方向偏移量(mm)
 * @param [in] dz z方向偏移量(mm)
 * @param [in] dry 繞y軸偏移量(°)
 * @param [out] offset 計算結果偏移量
 * @return 錯誤碼
 */
 int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dz, double dry, ref DescPose offset);

設定機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定機器人焊接電弧意外中斷偵測參數
 * @param [in] checkEnable 是否使能偵測；0-不使能；1-使能
 * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
 * @return 錯誤碼
 */
 int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength)

取得機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得機器人焊接電弧意外中斷偵測參數
 * @param [out] checkEnable 是否啟用偵測；0-不使能；1-使能
 * @param [out] arcInterruptTimeLength 電弧中斷確認時長(ms)
 * @return 錯誤碼
 */
 int WeldingGetCheckArcInterruptionParam(ref int checkEnable, ref int arcInterruptTimeLength)

設定機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定機器人焊接中斷恢復參數
 * @param[in] enable 是否啟用焊接中斷恢復
 * @param[in] length 焊縫重疊距離(mm)
 * @param[in] velocity 機器人回到再起弧點速度百分比(0-100)
 * @param[in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
 * @return 錯誤碼
 */
 int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType)

取得機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 取得機器人焊接中斷恢復參數
 * @param [out] enable 是否使能焊接中斷恢復
 * @param [out] length 焊縫重疊距離(mm)
 * @param [out] velocity 機器人回到再起弧點速度百分比(0-100)
 * @param [out] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
 * @return 錯誤碼
 */
 int WeldingGetReWeldAfterBreakOffParam(ref int enable, ref double length, ref double velocity, ref int moveType)

設定機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定機器人焊接中斷後恢復焊接
 * @return 錯誤碼
 */
 int WeldingStartReWeldAfterBreakOff()

設定機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
 :linenos:

 /**
 * @brief 設定機器人焊接中斷後退出焊接
 * @return 錯誤碼
 */
 int WeldingAbortWeldAfterBreakOff()

程式範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C# SDK-v1.1.0-3.7.8

.. code-block:: c#
    :linenos:

    private void button7_Click(object sender, EventArgs e)
    {
        int rtn = -1;
        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        Console.WriteLine("WeldingSetCheckArcInterruptionParam  {0}", rtn);
        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        Console.WriteLine("WeldingSetReWeldAfterBreakOffParam {0}", rtn);
        int enable = 0;
        double length = 0;
        double velocity = 0;
        int moveType = 0;
        int checkEnable = 0;
        int arcInterruptTimeLength = 0;
        rtn = robot.WeldingGetCheckArcInterruptionParam(ref checkEnable, ref arcInterruptTimeLength);
        Console.WriteLine($"WeldingGetCheckArcInterruptionParam  checkEnable {checkEnable} - arcInterruptTimeLength {arcInterruptTimeLength}");

        rtn = robot.WeldingGetReWeldAfterBreakOffParam(ref enable, ref length, ref velocity,ref moveType);
        Console.WriteLine("WeldingGetReWeldAfterBreakOffParam  enable = {0}, length = {1}, velocity = {2}, moveType = {3}", enable, length, velocity, moveType);

        robot.ProgramLoad("/fruser/test.lua");
        robot.ProgramRun();

        Thread.Sleep(5000);

        while (true)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG { };
            robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine("welding breakoff state is     {0}", pkg.weldingBreakOffState.breakOffState);
            if (pkg.weldingBreakOffState.breakOffState == 1)
            {
                Console.WriteLine("welding breakoff ! \n");
                Thread.Sleep(2000);
                rtn = robot.WeldingStartReWeldAfterBreakOff();
                Console.WriteLine("WeldingStartReWeldAfterBreakOff    %d\n", rtn);
                break;
            }
            Thread.Sleep(100);
        }
    }

擺動漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  擺動漸變開始
    * @param  [in] weaveNum 擺動編號
    * @return  錯誤碼
    */
    int WeaveChangeStart(int weaveNum)

擺動漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  擺動漸變結束
    * @return  錯誤碼
    */
    int WeaveChangeEnd()

程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnweld_Click(object sender, EventArgs e)
    {
        //擺動漸變
        DescPose p1Desc = new DescPose(-72.912, -587.664, 31.849, 43.283, -6.731, 15.068);
        JointPos p1Joint = new JointPos(74.620, -80.903, 94.608, -109.882, -90.436, -13.432);

        DescPose p2Desc = new DescPose(-104.915, -483.712, -25.231, 42.228, -6.572, 18.433);
        JointPos p2Joint = new JointPos(66.431, -92.875, 116.362, -120.516, -88.627, -24.731);

        DescPose p3Desc = new DescPose(-240.651, -483.840, -7.161, 46.577, -5.286, 8.318);
        JointPos p3Joint = new JointPos(56.457, -84.796, 104.618, -114.497, -92.422, -25.430);

        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveJ(p1Joint, p1Desc, 1, 1, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveL(p2Joint, p2Desc, 1, 1, 100, 100, 50, -1, exaxisPos, 0, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1);
        robot.MoveL(p3Joint, p3Desc, 1, 1, 100, 100, 1, -1, exaxisPos, 0, 0, offdese);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
    }