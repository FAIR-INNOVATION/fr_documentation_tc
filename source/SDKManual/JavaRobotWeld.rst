機器人焊接
=============

.. toctree:: 
    :maxdepth: 5

焊接開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電流與輸出模擬量對應關係
    * @param [in] relation 關系值
    * @return 錯誤碼
    */
    int WeldingSetCurrentRelation(WeldCurrentAORelation relation);

設定焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電壓與輸出模擬量對應關係
    * @param [in] relation 焊接電壓-類比量輸出關系值
    * @return 錯誤碼
    */
    int WeldingSetVoltageRelation(WeldVoltageAORelation relation);

取得焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得焊接電流與輸出模擬量對應關係
    * @param [out] relation 關系值
    * @return 錯誤碼
    */
    int WeldingGetCurrentRelation(WeldCurrentAORelation relation);

取得焊接電壓與輸出類比對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 取得焊接電壓與輸出類比對應關係
    * @param [out] relation 焊接電壓-類比量輸出關系值
    * @return 錯誤碼
    */
    int WeldingGetVoltageRelation(WeldVoltageAORelation relation);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        DescPose  desc_p1, desc_p2;
        desc_p1 = new DescPose(0, 0, 0, 0, 0, 0);
        desc_p2 = new DescPose(0, 0, 0, 0, 0, 0);

        JointPos j1 = new JointPos(-28.529,-140.397,-81.08,-30.934,92.34,-5.629);
        JointPos j2 = new JointPos(-11.045,-130.984,-104.495,-12.854,92.475,-5.547);

        robot.GetForwardKin(j1,desc_p1);
        robot.GetForwardKin(j2,desc_p2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();
        robot.MoveL(j1, desc_p1,0, 0, 20, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCStart(0, 0, 10000);//焊接開始
        robot.MoveL(j2, desc_p2,0, 0, 20, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCEnd(0, 0, 10000);//焊接結束

        WeldCurrentAORelation currentRelation = new WeldCurrentAORelation(0, 1000, 0, 10, 0);
        robot.WeldingSetCurrentRelation(currentRelation);
        WeldVoltageAORelation voltageAORelation = new WeldVoltageAORelation(0, 100, 0, 10, 1);
        robot.WeldingSetVoltageRelation(voltageAORelation);

        WeldCurrentAORelation tmpCur = new WeldCurrentAORelation();
        WeldVoltageAORelation tmpVol = new WeldVoltageAORelation();
        robot.WeldingGetCurrentRelation(tmpCur);
        robot.WeldingGetVoltageRelation(tmpVol);
    } 

設定焊接電流
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱類比輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

設定焊接電壓
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴充IO
    * @param [in] voltage 焊接電壓值(A)
    * @param [in] AOIndex 焊接電壓控制箱類比輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

設定擺動參數
++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2
.. code-block:: Java
    :linenos:

    /**
    * @brief 設定擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in] weaveType 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    * @param [in] weaveFrequency 擺動頻率(Hz)
    * @param [in] weaveIncStayTime 等待模式 0-週期不包含等待時間；1-週期包含等待時間
    * @param [in] weaveRange 擺動幅度(mm)
    * @param [in] weaveLeftRange 垂直三角摆動左弦長度(mm)
    * @param [in] weaveRightRange 垂直三角摆動右弦長度(mm)
    * @param [in] additionalStayTime 垂直三角摆動垂三角點停留時間(mm)
    * @param [in] weaveLeftStayTime 擺動左停留時間(ms)
    * @param [in] weaveRightStayTime 擺動右停留時間(ms)
    * @param [in] weaveCircleRadio 圓形擺動-回調比率(0-100%)
    * @param [in] weaveStationary 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止
    * @param [in] weaveYawAngle 摆動方向方位角(绕摆動Z軸旋转)，單位°
    * @param [in] weaveRotAngle 擺動方向方位角（繞擺動X軸旋轉），單位°
    * @return 錯誤碼
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle,double weaveRotAngle)

即时設定擺動參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 即时設定擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in]weaveType 擺動類型0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
    * @param [in]weaveFrequency 擺動頻率(Hz)
    * @param [in]weaveIncStayTime 等待模式 0-週期不包含等待時間；1-週期包含等待時間
    * @param [in]weaveRange 擺動幅度(mm)
    * @param [in]weaveLeftStayTime 擺動左停留時間(ms)
    * @param [in]weaveRightStayTime 擺動右停留時間(ms)
    * @param [in]weaveCircleRadio 圓形擺動-回調比率(0-100%)
    * @param [in]weaveStationary 擺動位置等待，0-等待時間內位置繼續移動；1-等待時間內位置靜止
    * @return 錯誤碼
    */
    int WeaveOnlineSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary);

擺盪開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 擺盪開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveStart(int weaveNum);

擺盪結束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 擺盪結束
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveEnd(int weaveNum);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.WeldingSetCurrent(0, 500, 0, 0);
        robot.WeldingSetVoltage(0, 60, 1, 0);
        robot.WeaveSetPara(0,0, 2.0, 0, 0.0, 0, 0, 0, 100, 100, 50, 50,1);

        DescPose desc_p1 = new DescPose(688.259,-566.358,-139.354,-158.206,0.324,-117.817);
        DescPose desc_p2 = new DescPose(700.078,-224.752,-149.191,-158.2,0.239,-94.978);


        JointPos j1 = new JointPos(0,0,0,0,0,0);
        JointPos j2 = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, desc_p1, -1, j1);
        robot.GetInverseKin(0, desc_p2, -1, j2);

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveL(j1, desc_p1,3, 0, 30, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.WeaveSetPara(0,0, 1.0, 0, 10.0, 0, 0, 0, 100, 100, 50, 50,1);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2,3, 0, 10, 100, 100, -1, epos, 0, 0, offset_pos, 0, 100);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
    } 

擺動漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief  擺動漸變開始
    * @param  [in] weaveChangeFlag 1-變擺動參數；2-變擺動參數+焊接速度
    * @param  [in] weaveNum 擺動編號
    * @param  [in] velStart 焊接開始速度，(cm/min)
    * @param  [in] velEnd 焊接結束速度，(cm/min)
    * @return 錯誤碼
    */
    int WeaveChangeStart(int weaveChangeFlag, int weaveNum, double velStart, double velEnd)

擺動漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.2-3.8.0

.. code-block:: Java
    :linenos:

    /**
    * @brief 擺動漸變結束
    * @return 錯誤碼
    */
    int WeaveChangeEnd(); 

正向送絲
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /**
    * @brief 送氣
    * @param [in] ioType io類型 0-控制器IO；1-擴充IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    int SetAspirated(int ioType, int airControl);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.SetForwardWireFeed(0, 1);
        robot.Sleep(2000);
        robot.SetForwardWireFeed(0, 0);
        robot.Sleep(2000);
        robot.SetReverseWireFeed(0, 1);
        robot.Sleep(2000);
        robot.SetReverseWireFeed(0, 0);
        robot.Sleep(2000);

        robot.SetAspirated(0,1);
        robot.Sleep(2000);
        robot.SetAspirated(0,0);
    }

段焊
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType,int arcNum, int weldTimeout, boolean isWeave, int weaveNum, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        DescPose startdescPose = new DescPose(185.859,-520.154,193.129,-177.129,1.339,-137.789);
        JointPos startjointPos = new JointPos(-60.989,-94.515,-89.479,-83.514,91.957,-13.124);

        DescPose enddescPose = new DescPose( -243.7033,-543.868,143.199,-177.954,1.528,177.758);
        JointPos endjointPos = new JointPos(-105.479,-101.919,-87.979,-78.455,91.955,-13.183);

        ExaxisPos exaxisPos = new ExaxisPos( 0, 0, 0, 0 );
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0 );

        robot.SegmentWeldStart(startdescPose, enddescPose, startjointPos, endjointPos, 80, 40, 0, 0, 5000, true, 0, 3, 0, 30, 30, 100, -1, exaxisPos, 0, 0, offdese);
    }

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊絲尋位開始
    * @param [in] refPos  1-基準點 2-接觸點
    * @param [in] searchVel   尋位速度 %
    * @param [in] searchDis  尋位距離 mm
    * @param [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param [in] autoBackVel  自動返回速度 %
    * @param [in] autoBackDis  自動返回距離 mm
    * @param [in] offectFlag  1-帶偏移量尋位；2-示教點尋位
    * @return 錯誤碼 
    */
    int WireSearchStart(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

焊絲尋位結束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊絲尋位結束
    * @param [in] refPos  1-基準點 2-接觸點
    * @param [in] searchVel   尋位速度 %
    * @param [in] searchDis  尋位距離 mm
    * @param [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param [in] autoBackVel  自動返回速度 %
    * @param [in] autoBackDis  自動返回距離 mm
    * @param [in] offectFlag  1-帶偏移量尋位；2-示教點尋位
    * @return 錯誤碼 
    */
    int WireSearchEnd(int refPos, double searchVel, int searchDis, int autoBackFlag, double autoBackVel, int autoBackDis, int offectFlag);

計算焊絲尋位偏移量
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算焊絲尋位偏移量
    * @param [in] seamType  焊缝類型
    * @param [in] method   計算方法
    * @param [in] varNameRef 基準點1-6，「#」表示無點變數
    * @param [in] varNameRes 接觸點1-6，「#」表示無點變數
    * @param [out] offset 偏移位姿[x, y, z, a, b, c]及偏移方式
    * @return 錯誤碼 
    */
    int GetWireSearchOffset(int seamType, int method, String[] varNameRef, String[] varNameRes, DescOffset offset);

等待焊絲尋位完成
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 等待焊絲尋位完成
    * @return 錯誤碼 
    */
    int WireSearchWait(String name);

焊絲尋位接觸點寫入資料庫
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊絲尋位接觸點寫入資料庫
    * @param [in] varName  接觸點名稱 “RES0” ~ “RES99”
    * @param [in] pos  接触點數據[x, y, x, a, b, c]
    * @return 錯誤碼 
    */
    int SetPointToDatabase(String varName, DescPose pos);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        DescPose descStart = new DescPose(153.736,-715.249,-295.037,-179.829,2.613,-155.615);
        JointPos jointStart = new JointPos(0,0,0,0,0,0);

        DescPose descEnd = new DescPose(73.748,-645.825,-295.016,-179.828,2.608,-155.614);
        JointPos jointEnd = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, descStart, -1, jointStart);
        robot.GetInverseKin(0, descEnd, -1, jointEnd);

        robot.MoveL(jointStart, descStart, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese,0, 100);

        DescPose descREF0A = new DescPose(273.716,-723.539,-295.075,-179.829,2.608,-155.614);
        JointPos jointREF0A = new JointPos(0,0,0,0,0,0);

        DescPose descREF0B = new DescPose(202.588,-723.543,-295.039,-179.829,2.609,-155.614);
        JointPos jointREF0B = new JointPos(0,0,0,0,0,0);

        DescPose descREF1A = new DescPose(75.265,-525.091,-295.059,-179.83,2.609,-155.616);
        JointPos jointREF1A = new JointPos(0,0,0,0,0,0);

        DescPose descREF1B = new DescPose(75.258,-601.157,-295.075,-179.834,2.609,-155.616);
        JointPos jointREF1B = new JointPos(0,0,0,0,0,0);

        robot.GetInverseKin(0, descREF0A, -1, jointREF0A);
        robot.GetInverseKin(0, descREF0B, -1, jointREF0B);
        robot.GetInverseKin(0, descREF1A, -1, jointREF1A);
        robot.GetInverseKin(0, descREF1B, -1, jointREF1B);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF0B, descREF0B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        robot.WireSearchWait("REF0");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF1B, descREF1B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        robot.WireSearchWait("REF1");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);


        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF0B, descREF0B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        robot.WireSearchWait("RES0");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 3, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF1B, descREF1B, 3, 0, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        robot.WireSearchWait("RES1");
        robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef = { "REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = { "RES0", "RES1", "#", "#", "#", "#" };

        DescOffset offectPos = new DescOffset();
        robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectPos);
        robot.PointsOffsetEnable(offectPos.offsetFlag, offectPos.offset);
        robot.MoveL(jointStart, descStart, 3, 1, 30, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 3, 1, 30, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);
        robot.PointsOffsetDisable();
    }

電弧追蹤控制
++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.2-3.8.0

.. code-block:: Java
    :linenos:

    /** 
    * @brief 電弧追蹤控制
    * @param [in] flag 開關，0-關；1-開
    * @param [in] delaytime 滯後時間，單位ms
    * @param [in] isLeftRight 左右偏差補償
    * @param [in] klr 左右調節係數(靈敏度)
    * @param [in] tStartLr 左右開始補償時間cyc
    * @param [in] stepMaxLr 左右每次最大補償量 mm
    * @param [in] sumMaxLr 左右總計最大補償量 mm
    * @param [in] isUpLow 上下偏差補償
    * @param [in] kud 上下調節係數(靈敏度)
    * @param [in] tStartUd 上下開始補償時間cyc
    * @param [in] stepMaxUd 上下每次最大補償量 mm
    * @param [in] sumMaxUd 上下总计最大补偿量
    * @param [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
    * @param [in] referenceType 上下基準電流設定方式，0-回饋；1-常數
    * @param [in] referSampleStartUd 上下基準電流取樣開始計數(回饋)，cyc
    * @param [in] referSampleCountUd 上下基準電流取樣循環計數(回饋)，cyc
    * @param [in] referenceCurrent 上下基準電流mA
    * @param [in] offsetType 偏移追蹤類型，0-不偏移；1-取樣；2-百分比
    * @param [in] offsetParameter 偏移參數；取樣(偏移取樣開始時間，預設取一週期)；百分比(偏移百分比(-100 ~ 100))
    * @return 錯誤碼 
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent, int offsetType, int offsetParameter);

仿真擺盪開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真擺盪開始
    * @param [in] weaveNum  擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveStartSim(int weaveNum);

仿真擺盪結束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真擺盪結束
    * @param [in] weaveNum  擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveEndSim(int weaveNum);

開始軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 開始軌跡偵測預警(不運動)
    * @param [in] weaveNum   擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveInspectStart(int weaveNum);

結束軌跡偵測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 結束軌跡偵測預警(不運動)
    * @param [in] weaveNum   擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveInspectEnd(int weaveNum);

設定焊接製程曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定焊接製程曲線參數
    * @param [in] id 焊接工藝編號(1-99)
    * @param [in] param 焊接製程參數
    * @return 錯誤碼 
    */
    int WeldingSetProcessParam(int id, WeldingProcessParam param);

取得焊接製程曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得焊接製程曲線參數
    * @param [in] id 焊接工藝編號(1-99)
    * @param [out] param 焊接製程參數
    * @return 錯誤碼 
    */
    int WeldingGetProcessParam(int id, WeldingProcessParam param);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        WeldingProcessParam param = new WeldingProcessParam(177.0,27.0,1000,178.0,28.0,176.0,26.0,1000);
        robot.WeldingSetProcessParam(1, param);

        WeldingProcessParam getParam = new WeldingProcessParam();
        robot.WeldingGetProcessParam(1, getParam);
    }

擴展IO-配置焊機氣體偵測訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機氣體偵測訊號
    * @param [in] DONum  氣體偵測訊號擴展DO編號
    * @return 錯誤碼 
    */
    int SetAirControlExtDoNum(int DONum);

擴充IO-配置焊接機起弧訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴充IO-配置焊接機起弧訊號
    * @param [in] DONum 焊機起弧訊號擴展DO編號
    * @return 錯誤碼 
    */
    int SetArcStartExtDoNum(int DONum);

擴充IO-配置焊接機反向送絲訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴充IO-配置焊接機反向送絲訊號
    * @param [in] DONum  反向送絲信号扩展DO編號
    * @return 錯誤碼 
    */
    int SetWireReverseFeedExtDoNum(int DONum);

擴充IO-配置焊接機正向送絲訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴充IO-配置焊接機正向送絲訊號
    * @param [in] DONum  正向送絲信号扩展DO編號
    * @return 錯誤碼 
    */
    int SetWireForwardFeedExtDoNum(int DONum);

擴充IO-配置焊接機起弧成功訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴充IO-配置焊接機起弧成功訊號
    * @param [in] DINum  起弧成功訊號擴展DI編號
    * @return 錯誤碼 
    */
    int SetArcDoneExtDiNum(int DINum);

擴充IO-配置焊接機準備訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴充IO-配置焊接機準備訊號
    * @param [in] DINum  焊接機準備訊號擴展DI編號
    * @return 錯誤碼 
    */
    int SetWeldReadyExtDiNum(int DINum);

擴展IO-配置焊接中斷恢復訊號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊接中斷恢復訊號
    * @param [in] reWeldDINum  焊接中斷後恢復焊接訊號擴展DI編號
    * @param [in] abortWeldDINum  焊接中斷後退出焊接訊號擴展DI編號
    * @return 錯誤碼 
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        robot.SetArcStartExtDoNum(1);
        robot.SetAirControlExtDoNum(2);
        robot.SetWireForwardFeedExtDoNum(3);
        robot.SetWireReverseFeedExtDoNum(4);

        robot.SetWeldReadyExtDiNum(5);
        robot.SetArcDoneExtDiNum(6);
        robot.SetExtDIWeldBreakOffRecover(7, 8);
    }

設定焊絲尋位擴充IO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定焊絲尋位擴充IO端口
    * @param [in] searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param [in] searchStartDONum 焊絲尋位啟動停止控制DO端口(0-127)
    * @return 錯誤碼
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);

設定焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定焊機控制模式擴展DO端口
    * @param [in] DONum 焊機控制模式DO端口(0-127)
    * @return 錯誤碼 
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

設定焊機控制模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定焊機控制模式
    * @param [in] mode 焊接機控制模式;0-一元化
    * @return 錯誤碼 
    */
    int SetWeldMachineCtrlMode(int mode);

代碼範例
++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc連接 success");
        }
        else
        {
            System.out.println("rpc連接 fail");
            return ;
        }
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 50, 5, 50, 1, 50, 10);
        robot.ExtDevSetUDPComParam(param);//udp擴展軸通訊
        robot.ExtDevLoadUDPDriver();

        robot.SetWeldMachineCtrlModeExtDoNum(17);//DO
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);//設定焊機控制模式
            robot.Sleep(500);
            robot.SetWeldMachineCtrlMode(1);
            robot.Sleep(500);
        }

        robot.SetWeldMachineCtrlModeExtDoNum(18);
        for (int i = 0; i < 5; i++)
        {
            robot.SetWeldMachineCtrlMode(0);
            robot.Sleep(500);
            robot.SetWeldMachineCtrlMode(1);
            robot.Sleep(500);
        }
    }

設定機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 設定機器人焊接電弧意外中斷偵測參數
 * @param [in] checkEnable 是否使能偵測；0-不使能；1-使能
 * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
 * @return 錯誤碼
 */
 int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

取得機器人焊接電弧意外中斷偵測參數
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 取得機器人焊接電弧意外中斷偵測參數
 * @return List[0]:錯誤碼; List[1]:double 是否使能檢測；0-不使能；1-使能; List[2]:電弧中斷確認時長(ms)
 */
 List<Integer> WeldingGetCheckArcInterruptionParam();

設定機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 設定機器人焊接中斷恢復參數
 * @param [in] enable 是否使能焊接中斷恢復
 * @param [in] length 焊縫重疊距離(mm)
 * @param [in] velocity 機器人回到再起弧點速度百分比(0-100)
 * @param [in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
 * @return 錯誤碼
 */
 int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);

取得機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 取得機器人焊接中斷恢復參數
 * @return List[0]:錯誤碼; List[1]:int 是否使能焊接中斷恢復; List[2]:double 焊縫重疊距離(mm);
 * @return List[3]:double 機器人回到再起弧點速度百分比(0-100);List[4]:int 機器人移動到再起弧點方式；0-LIN；1-PTP
 */
 List<Number> WeldingGetReWeldAfterBreakOffParam();

設定機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 設定機器人焊接中斷後恢復焊接
 * @return 錯誤碼
 */
 int WeldingStartReWeldAfterBreakOff();

設定機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 設定機器人焊接中斷後退出焊接
 * @return 錯誤碼
 */
 int WeldingAbortWeldAfterBreakOff();

程式碼範例
++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 public static void main(String[] args)
 {
 Robot robot = new Robot();
 robot.SetReconnectParam(true,20,500);//設定重連次數、間隔
 robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
 int rtn = robot.RPC("192.168.58.2");
 if(rtn == 0)
 {
 System.out.println("rpc連線 success");
 }
 else
 {
 System.out.println("rpc連線 fail");
 return ;
 }
 int rtn = -1;
 rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
 System.out.println("WeldingSetCheckArcInterruptionParam: "+rtn);
 rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
 System.out.println("WeldingSetReWeldAfterBreakOffParam: "+rtn);
 int enable = 0;
 double length = 0;
 double velocity = 0;
 int moveType = 0;
 int checkEnable = 0;
 int arcInterruptTimeLength = 0;
 List<Integer> rtnArray = new ArrayList<Integer>() {};
 List<Number> rtnArrayWeld = new ArrayList<Number>() {};
 rtnArray = robot.WeldingGetCheckArcInterruptionParam();
 checkEnable=rtnArray.get(1);
 arcInterruptTimeLength=rtnArray.get(2);
 System.out.println("WeldingGetCheckArcInterruptionParam checkEnable:"+checkEnable +", arcInterruptTimeLength : "+ arcInterruptTimeLength);
 rtnArrayWeld = robot.WeldingGetReWeldAfterBreakOffParam();
 enable=(int) rtnArrayWeld.get(1);
 length=(double) rtnArrayWeld.get(2);
 velocity=(double) rtnArrayWeld.get(3);
 moveType=(int) rtnArrayWeld.get(4);
 System.out.println("WeldingGetReWeldAfterBreakOffParam :"+ enable +",length: "+length+",velocity :"+velocity+",moveType :"+moveType);
 //焊接中斷恢復
 robot.ProgramLoad("/fruser/test.lua");
 robot.ProgramRun();

 robot.Sleep(5000);

 while (true)
 {
 ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
 pkg=robot.GetRobotRealTimeState();
 System.out.println("welding breakoff state is "+pkg.weldingBreakOffstate.breakOffState);
 if (pkg.weldingBreakOffstate.breakOffState == 1)
 {
 System.out.println("welding breakoff !");
 robot.Sleep(2000);
 rtn = robot.WeldingStartReWeldAfterBreakOff();
 System.out.println("WeldingStartReWeldAfterBreakOff: "+rtn);
 break;
 }
 robot.Sleep(100);
 }
 }

電弧追蹤焊機電流反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤焊機電流反饋AI通道選擇
    * @param  [in] channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelCurrent(int channel)

電弧追蹤焊機電壓反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤焊機電壓反饋AI通道選擇
    * @param  [in] channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelVoltage(int channel)

電弧追蹤焊機電流反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤焊機電流反饋轉換參數
    * @param [in] AILow AI通道下限，預設值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，預設值10V，範圍[0-10V]
    * @param [in] currentLow AI通道下限對應焊機電流值，預設值0V，範圍[0-200V]
    * @param [in] currentHigh AI通道上限對應焊機電流值，預設值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    int ArcWeldTraceCurrentPara(double AILow, double AIHigh, double currentLow, double currentHigh)

電弧追蹤焊機電壓反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤焊機電壓反饋轉換參數
    * @param [in] AILow AI通道下限，預設值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，預設值10V，範圍[0-10V]
    * @param [in] voltageLow AI通道下限對應焊機電壓值，預設值0V，範圍[0-200V]
    * @param [in] voltageHigh AI通道上限對應焊機電壓值，預設值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    int ArcWeldTraceVoltagePara(double AILow, double AIHigh, double voltageLow, double voltageHigh)

程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void WeldTraceControlWithCtrlBoxAI(Robot robot)
    {
        DescPose startdescPose = new DescPose(-473.86,257.879,-20.849,-37.317,-42.021,2.543);
        JointPos startjointPos = new JointPos(-43.487,-76.526,95.568,-104.445,-89.356,3.72);

        DescPose safedescPose = new DescPose(-504.043,275.181,40.908,-28.002,-42.025,-14.044);
        JointPos safejointPos = new JointPos(-39.078,-76.732,87.227,-99.47,-94.301,18.714);

        DescPose enddescPose =new DescPose(-499.844,141.225,7.72,-34.856,-40.17,13.13);
        JointPos endjointPos =new JointPos(-31.305,-82.998,99.401,-104.426,-89.35,3.696);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0 );
        DescPose offdese = new DescPose( 0, 0, 0, 0, 0, 0);
        //起始運動到安全點
        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 20, 100, exaxisPos, -1, 0, offdese);

        WeldCurrentAORelation current=new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation voltage=new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(current);
        robot.WeldingSetVoltageRelation(voltage);
        robot.WeldingSetVoltage(0, 25, 1, 0);
        robot.WeldingSetCurrent(0, 260, 0, 0);

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        System.out.println("ArcWeldTraceAIChannelCurrent rtn is "+rtn);

        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        System.out.println("ArcWeldTraceAIChannelVoltage rtn is "+rtn);

        rtn = robot.ArcWeldTraceCurrentPara(0.0,  5, 0, 500);
        System.out.println("ArcWeldTraceCurrentPara rtn is "+rtn);

        rtn = robot.ArcWeldTraceVoltagePara( 1.018,  10, 0, 50);
        System.out.println("ArcWeldTraceVoltagePara rtn is "+rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese,0,10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offdese);
    }

設定焊接電壓漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電壓漸變開始
    * @param [in] IOType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @param [in] voltageStart 起始焊接電壓(V)
    * @param [in] voltageEnd 終止焊接電壓(V)
    * @param [in] AOIndex 控制箱AO端口號(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend)

設定焊接電壓漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電壓漸變結束
    * @return 錯誤碼
    */
    int WeldingSetVoltageGradualChangeEnd()

設定焊接電流漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電流漸變開始
    * @param [in] IOType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @param [in] currentStart 起始焊接電流(A)
    * @param [in] currentEnd 終止焊接電流(A)
    * @param [in] AOIndex 控制箱AO端口號(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend)

設定焊接電流漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設定焊接電流漸變結束
    * @return 錯誤碼
    */
    int WeldingSetCurrentGradualChangeEnd()

程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void  WeldparamChange(Robot robot)
    {
        DescPose startdescPose = new DescPose(-484.707, 276.996, -14.013, -37.657, -40.508, -1.548);
        JointPos startjointPos =new JointPos(-45.421, -75.673, 93.627, -104.302, -87.938, 6.005);

        DescPose enddescPose = new DescPose(-508.767, 137.109, -13.966, -37.639, -40.508, -1.559);
        JointPos endjointPos =new JointPos(-32.768, -80.947, 100.254, -106.201, -87.201, 18.648);

        DescPose safedescPose = new DescPose( -484.709, 294.436, 13.621, -37.660, -40.508, -1.545);
        JointPos safejointPos = new JointPos( -46.604, -75.410, 89.109, -100.003, -88.012, 4.823);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0 );

        WeldCurrentAORelation cur=new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation vol=new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(cur);
        robot.WeldingSetVoltageRelation(vol);

        robot.WeldingSetVoltage(0, 25, 1, 0);
        robot.WeldingSetCurrent(0, 260, 0, 0);

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        int rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);
        System.out.println("ArcWeldTraceControl rtn is "+rtn);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(2, 1, 24, 36);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, exaxisPos, 0, 0, offdese,0,10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }