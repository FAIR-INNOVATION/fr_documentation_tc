機器人焊接
=============

.. toctree:: 
    :maxdepth: 5


設置焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置焊接工藝曲線參數
    * @param [in] id 焊接工藝編號(1-99)
    * @param [in] param 焊接工藝參數
    * @return 錯誤碼 
    */
    int WeldingSetProcessParam(int id, WeldingProcessParam param);

獲取焊接工藝曲線參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取焊接工藝曲線參數
    * @param [in] id 焊接工藝編號(1-99)
    * @param [out] param 焊接工藝參數
    * @return 錯誤碼 
    */
    int WeldingGetProcessParam(int id, WeldingProcessParam param);

設置焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電流與輸出模擬量對應關係
    * @param [in] relation 關係值
    * @return 錯誤碼
    */
    int WeldingSetCurrentRelation(WeldCurrentAORelation relation);

設置焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電壓與輸出模擬量對應關係
    * @param [in] relation 焊接電壓-模擬量輸出關係值
    * @return 錯誤碼
    */
    int WeldingSetVoltageRelation(WeldVoltageAORelation relation);

獲取焊接電流與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取焊接電流與輸出模擬量對應關係
    * @param [out] relation 關係值
    * @return 錯誤碼
    */
    int WeldingGetCurrentRelation(WeldCurrentAORelation relation);

獲取焊接電壓與輸出模擬量對應關係
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取焊接電壓與輸出模擬量對應關係
    * @param [out] relation 焊接電壓-模擬量輸出關係值
    * @return 錯誤碼
    */
    int WeldingGetVoltageRelation(WeldVoltageAORelation relation);

設置焊接電流
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電流
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] current 焊接電流值(A)
    * @param [in] AOIndex 焊接電流控制箱模擬量輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetCurrent(int ioType, double current, int AOIndex, int blend);

設置焊接電壓
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電壓
    * @param [in] ioType 控制IO類型 0-控制箱IO；1-擴展IO
    * @param [in] voltage 焊接電壓值(A)
    * @param [in] AOIndex 焊接電壓控制箱模擬量輸出端口(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetVoltage(int ioType, double voltage, int AOIndex, int blend);

設置擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
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
    * @param [in] weaveRotAngle 擺動方向方位角(繞擺動X軸旋轉)，單位°
    * @return 錯誤碼
    */
    int WeaveSetPara(int weaveNum, int weaveType, double weaveFrequency, int weaveIncStayTime, double weaveRange, double weaveLeftRange, double weaveRightRange, int additionalStayTime, int weaveLeftStayTime, int weaveRightStayTime, int weaveCircleRadio, int weaveStationary, double weaveYawAngle,double weaveRotAngle)

設置焊接參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static int TestSetWeldParam(Robot robot) {
        // 1. 設置焊接工藝參數
        WeldingProcessParam para1 = new WeldingProcessParam(177, 27, 1000, 178, 28, 176, 26, 1000);
        WeldingProcessParam para2 = new WeldingProcessParam(188, 28, 555, 199, 29, 133, 23, 333);
        robot.WeldingSetProcessParam(1, para1);
        robot.WeldingSetProcessParam(2, para2);

        // 2. 獲取並打印第1組參數
        WeldingProcessParam param = new WeldingProcessParam(0, 0, 0, 0, 0, 0, 0, 0);
        robot.WeldingGetProcessParam(1, param);
        System.out.println("the Num 1 process param is "
                + param.startCurrent + " " + param.startVoltage + " "
                + param.startTime + " " + param.weldCurrent + " "
                + param.weldVoltage + " " + param.endCurrent + " "
                + param.endVoltage + " " + param.endTime);

        // 3. 獲取並打印第2組參數
        robot.WeldingGetProcessParam(2, param);
        System.out.println("the Num 2 process param is "
                + param.startCurrent + " " + param.startVoltage + " "
                + param.startTime + " " + param.weldCurrent + " "
                + param.weldVoltage + " " + param.endCurrent + " "
                + param.endVoltage + " " + param.endTime);

        // 4. 設置電流/電壓關係並打印返回值
        WeldCurrentAORelation rela1 = new WeldCurrentAORelation(0, 400, 0, 10, 0);
        int rtn = robot.WeldingSetCurrentRelation(rela1);
        System.out.println("WeldingSetCurrentRelation rtn is: " + rtn);

        WeldVoltageAORelation rela2 = new WeldVoltageAORelation(0, 40, 0, 10, 1);
        rtn = robot.WeldingSetVoltageRelation(rela2);
        System.out.println("WeldingSetVoltageRelation rtn is: " + rtn);

        // 5. 獲取並打印電流關係
        WeldCurrentAORelation rela3 = new WeldCurrentAORelation(0, 0, 0, 0, 0);
        rtn = robot.WeldingGetCurrentRelation(rela3);
        System.out.println("WeldingGetCurrentRelation rtn is: " + rtn);
        System.out.println("current min " + rela3.currentMin
                + " current max " + rela3.currentMax
                + " output vol min " + rela3.outputVoltageMin
                + " output vol max " + rela3.outputVoltageMax);

        // 6. 獲取並打印電壓關係
        WeldVoltageAORelation rela4 = new WeldVoltageAORelation(0, 0, 0, 0, 0);
        rtn = robot.WeldingGetVoltageRelation(rela4);
        System.out.println("WeldingGetVoltageRelation rtn is: " + rtn);
        System.out.println("vol min " + rela4.weldVoltageMin
                + " vol max " + rela4.weldVoltageMax
                + " output vol min " + rela4.outputVoltageMin
                + " output vol max " + rela4.outputVoltageMax);

        // 7. 設置電流/電壓並打印返回值
        rtn = robot.WeldingSetCurrent(0, 100, 0, 0);
        System.out.println("WeldingSetCurrent rtn is: " + rtn);

        robot.Sleep(3000);  // 對應 this_thread::sleep_for(chrono::seconds(3))

        rtn = robot.WeldingSetVoltage(0, 10, 0, 0);
        System.out.println("WeldingSetVoltage rtn is: " + rtn);

        // 8. 設置擺動參數
        rtn = robot.WeaveSetPara(0, 0, 2.000000, 0, 10.000000, 0.000000, 0.000000, 0, 0, 0, 0, 0, 60.000000,0);
        System.out.println("rtn is: " + rtn);

        robot.WeaveOnlineSetPara(0, 0, 1, 0, 20, 0, 0, 0, 0);

        // 9. 設置斷弧檢測和重焊參數
        rtn = robot.WeldingSetCheckArcInterruptionParam(1, 200);
        System.out.println("WeldingSetCheckArcInterruptionParam  " + rtn);

        rtn = robot.WeldingSetReWeldAfterBreakOffParam(1, 5.7, 98.2, 0);
        System.out.println("WeldingSetReWeldAfterBreakOffParam  " + rtn);

        // 10. 獲取並打印斷弧檢測參數
        List<Integer> inter = robot.WeldingGetCheckArcInterruptionParam();
        int checkEnable = inter.get(0);
        int arcInterruptTimeLength = inter.get(1);
        System.out.println("WeldingGetCheckArcInterruptionParam checkEnable " + checkEnable
                + "  arcInterruptTimeLength " + arcInterruptTimeLength);

        // 11. 獲取並打印重焊參數（返回 List<Number>）
        List<Number> num = robot.WeldingGetReWeldAfterBreakOffParam();
        int enable = num.get(0).intValue();
        double length = num.get(1).doubleValue();
        double velocity = num.get(2).doubleValue();
        int moveType = num.get(3).intValue();
        System.out.printf("WeldingGetReWeldAfterBreakOffParam enable = %d, length = %f, velocity = %f, moveType = %d%n",
                enable, length, velocity, moveType);

        // 12. 設置擴展 DO 並循環控制
        robot.SetWeldMachineCtrlModeExtDoNum(17);
        for (int i = 0; i < 5; i++) {
            int[] mode = new int[1];   // 用於接收輸出值

            robot.SetWeldMachineCtrlMode(0);
            rtn = robot.GetWeldMachineCtrlMode(mode);
            if (rtn == 0) {
                System.out.println("GetWeldMachineCtrlMode " + mode[0]);
            } else {
                System.out.println("GetWeldMachineCtrlMode failed, err: " + rtn);
            }
            robot.Sleep(1000);

            robot.SetWeldMachineCtrlMode(1);
            rtn = robot.GetWeldMachineCtrlMode(mode);
            if (rtn == 0) {
                System.out.println("GetWeldMachineCtrlMode " + mode[0]);
            } else {
                System.out.println("GetWeldMachineCtrlMode failed, err: " + rtn);
            }
            robot.Sleep(1000);
        }

        return 0;
    }

即時設置擺動參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 即時設置擺動參數
    * @param [in] weaveNum 擺焊參數配置編號
    * @param [in]weaveType 擺動類型 0-平面三角波擺動；1-垂直L型三角波擺動；2-順時針圓形擺動；3-逆時針圓形擺動；4-平面正弦波擺動；5-垂直L型正弦波擺動；6-垂直三角波擺動；7-垂直正弦波擺動
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

設置機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人焊接電弧意外中斷檢測參數
    * @param [in] checkEnable 是否使能檢測；0-不使能；1-使能
    * @param [in] arcInterruptTimeLength 電弧中斷確認時長(ms)
    * @return 錯誤碼 
    */
    int WeldingSetCheckArcInterruptionParam(int checkEnable, int arcInterruptTimeLength);

獲取機器人焊接電弧意外中斷檢測參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人焊接電弧意外中斷檢測參數
    * @return List[0]:錯誤碼; List[1]:double 是否使能檢測；0-不使能；1-使能; List[2]:電弧中斷確認時長(ms) 
    */
    List<Integer> WeldingGetCheckArcInterruptionParam();

設置機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人焊接中斷恢復參數
    * @param [in] enable 是否使能焊接中斷恢復
    * @param [in] length 焊縫重疊距離(mm)
    * @param [in] velocity 機器人回到再起弧點速度百分比(0-100)
    * @param [in] moveType 機器人運動到再起弧點方式；0-LIN；1-PTP
    * @return 錯誤碼 
    */
    int WeldingSetReWeldAfterBreakOffParam(int enable, double length, double velocity, int moveType);

獲取機器人焊接中斷恢復參數
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人焊接中斷恢復參數
    * @return List[0]:錯誤碼; List[1]:int 是否使能焊接中斷恢復; List[2]:double 焊縫重疊距離(mm);
    * @return List[3]:double 機器人回到再起弧點速度百分比(0-100);List[4]:int 機器人運動到再起弧點方式；0-LIN；1-PTP 
    */
    List<Number> WeldingGetReWeldAfterBreakOffParam();

設置焊機控制模式擴展DO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置焊機控制模式擴展DO端口
    * @param [in] DONum 焊機控制模式DO端口(0-127)
    * @return 錯誤碼 
    */
    int SetWeldMachineCtrlModeExtDoNum(int DONum);

設置焊機控制模式
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊機控制模式
    * @param mode 焊機控制模式; 0-直流一元模式；1-脈衝一元模式；2-JOB模式；3-近控模式；4-分別模式；5-CC/CV模式；6-TIG；7-CMT
    * @param ioType 控制類型；0-控制箱IO;1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @return 錯誤碼
    */
    public int SetWeldMachineCtrlMode(int mode, int ioType)

獲取焊機控制模式
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取焊機控制模式
    * @param mode 焊機控制模式;0-直流一元模式；1-脈衝一元模式；2-JOB模式；3-近控模式；4-分別模式；5-CC/CV模式；6-TIG；7-CMT
    * @return 錯誤碼
    */
    public int GetWeldMachineCtrlMode(int[] mode)

獲取擴展DI功能配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取擴展DI功能配置
    * @param DIConfig 擴展DI輸入配置；DIConfig[0]-焊機準備擴展DI端口；
    * DIConfig[1]-起弧成功擴展DI端口；
    * DIConfig[2]-焊接中斷恢復擴展DI端口；
    * DIConfig[3]-焊接中斷退出擴展DI端口；
    * DIConfig[4]-焊絲尋位成功擴展DI端口；
    * DIConfig[5]-雷射焊機運行狀態擴展DI端口；
    * DIConfig[6]-雷射焊機故障狀態擴展DI端口；
    * DIConfig[7-15]-預留
    * @return  錯誤碼
    */
    public int GetExtDIConfig(int[] DIConfig)

獲取擴展DO功能配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取擴展DO功能配置
    * @param DOConfig 擴展DO輸入配置；DOConfig[0]-焊機起弧擴展DO端口；
    * DOConfig[1]-氣體檢測擴展DO端口；
    * DOConfig[2]-正向送絲擴展DO端口；
    * DOConfig[3]-反向送絲擴展DO端口；
    * DOConfig[4]-焊絲尋位擴展DO端口；
    * DOConfig[5]-焊機控制模式擴展DO端口；
    * DOConfig[6]-雷射焊機使能擴展DO端口；
    * DOConfig[7]-雷射焊機啟動(出光)擴展DO端口；
    * DOConfig[8]-雷射焊機復位擴展DO端口；
    * DOConfig[9-15]-預留
    * @return  錯誤碼
    */
    public int GetExtDOConfig(int[] DOConfig)    

焊接開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
.. code-block:: Java
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
.. code-block:: Java
    :linenos:

    /**
    * @brief 擺動開始
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveStart(int weaveNum);

擺動結束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 擺動結束
    * @param [in] weaveNum 擺焊參數配置編號
    * @return 錯誤碼
    */
    int WeaveEnd(int weaveNum);

正向送絲
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 正向送絲
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    int SetForwardWireFeed(int ioType, int wireFeed); 	

反向送絲
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 反向送絲
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] wireFeed 送絲控制  0-停止送絲；1-送絲
    * @return 錯誤碼
    */
    int SetReverseWireFeed(int ioType, int wireFeed);

送氣
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 送氣
    * @param [in] ioType io類型  0-控制器IO；1-擴展IO
    * @param [in] airControl 送氣控制  0-停止送氣；1-送氣
    * @return 錯誤碼
    */
    int SetAspirated(int ioType, int airControl);

設置機器人焊接中斷後恢復焊接
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人焊接中斷後恢復焊接
    * @return 錯誤碼 
    */
    int WeldingStartReWeldAfterBreakOff();

設置機器人焊接中斷後退出焊接
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人焊接中斷後退出焊接
    * @return 錯誤碼 
    */
    int WeldingAbortWeldAfterBreakOff();

機器人焊接控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWelding(Robot robot)
    {
        robot.WeldingSetCurrent(0, 230, 0, 0);
        robot.WeldingSetVoltage(0, 24, 0, 1);

        DescPose p1Desc=new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint=new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc=new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint=new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.ARCStart(1, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese,0,10);
        robot.ARCEnd(1, 0, 10000);
        robot.WeaveEnd(0);
        return 0;
    }

段焊開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SegmentWeldStart(DescPose startDesePos, DescPose endDesePos, JointPos startJPos, JointPos endJPos, double weldLength, double noWeldLength, int weldIOType,int arcNum, int weldTimeout, boolean isWeave, int weaveNum, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos);

機器人段焊代碼示例
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSegWeld(Robot robot)
    {
        robot.WeldingSetCurrent(0, 230, 0, 0);
        robot.WeldingSetVoltage(0, 24, 0, 1);

        DescPose p1Desc=new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint=new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc=new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint=new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        robot.GetForwardKin(p1Joint,p1Desc);
        robot.GetForwardKin(p2Joint,p2Desc);

        int rtn = robot.SegmentWeldStart(p1Desc, p2Desc, p1Joint, p2Joint, 20, 20, 0, 0, 5000, true,0, 1, 0, 30, 100, 100, -1, exaxisPos, 0, 0, offdese);
        return 0;
    }

仿真擺動開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真擺動開始
    * @param [in] weaveNum  擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveStartSim(int weaveNum);

仿真擺動結束
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 仿真擺動結束
    * @param [in] weaveNum  擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveEndSim(int weaveNum);

開始軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 開始軌跡檢測預警(不運動)
    * @param [in] weaveNum   擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveInspectStart(int weaveNum);

結束軌跡檢測預警(不運動)
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 結束軌跡檢測預警(不運動)
    * @param [in] weaveNum   擺動參數編號
    * @return 錯誤碼 
    */
    int WeaveInspectEnd(int weaveNum);

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

機器人擺動漸變焊接代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWeave(Robot robot)
    {
        DescPose p1Desc=new DescPose(228.879, -503.594, 453.984, -175.580, 8.293, 171.267);
        JointPos p1Joint=new JointPos(102.700, -85.333, 90.518, -102.365, -83.932, 22.134);

        DescPose p2Desc=new DescPose(-333.302, -435.580, 449.866, -174.997, 2.017, 109.815);
        JointPos p2Joint=new JointPos(41.862, -85.333, 90.526, -100.587, -90.014, 22.135);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveStartSim(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese,0,10);
        robot.WeaveEndSim(0);
        robot.MoveJ(p1Joint, p1Desc, 13, 0, 20, 100, 100, exaxisPos, -1, 0, offdese);
        robot.WeaveInspectStart(0);
        robot.MoveL(p2Joint, p2Desc, 13, 0, 20, 100, 100, -1, 0, exaxisPos, 0, 0, offdese,0,10);
        robot.WeaveInspectEnd(0);

        robot.WeldingSetVoltage(1, 19, 0, 0);
        robot.WeldingSetCurrent(1, 190, 0, 0);
        robot.MoveL(p1Joint, p1Desc, 1, 1, 100, 100, 50, -1,0, exaxisPos, 0, 0, offdese,0,10);
        robot.ARCStart(1, 0, 10000);
        robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(1, 0, 50, 30);
        robot.MoveL(p2Joint, p2Desc, 1, 1, 100, 100, 1, -1, 0,exaxisPos, 0, 0, offdese,0,10);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 60, 1, 0.06, 5, 5, 80, 0, 0, 4, 1, 10, 0, 0);
        robot.ARCEnd(1, 0, 10000);
        return 0;
    }

擺動漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.2-3.7.9

.. code-block:: Java
    :linenos:

    /**
    * @brief 擺動漸變結束
    * @return 錯誤碼
    */
    int WeaveChangeEnd(); 

擴展IO-配置焊機氣體檢測信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機氣體檢測信號
    * @param [in] DONum  氣體檢測信號擴展DO編號
    * @return 錯誤碼 
    */
    int SetAirControlExtDoNum(int DONum);

擴展IO-配置焊機起弧信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機起弧信號
    * @param [in] DONum  焊機起弧信號擴展DO編號
    * @return 錯誤碼 
    */
    int SetArcStartExtDoNum(int DONum);

擴展IO-配置焊機反向送絲信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機反向送絲信號
    * @param [in] DONum  反向送絲信號擴展DO編號
    * @return 錯誤碼 
    */
    int SetWireReverseFeedExtDoNum(int DONum);

擴展IO-配置焊機正向送絲信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機正向送絲信號
    * @param [in] DONum  正向送絲信號擴展DO編號
    * @return 錯誤碼 
    */
    int SetWireForwardFeedExtDoNum(int DONum);

擴展IO-配置焊機起弧成功信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機起弧成功信號
    * @param [in] DINum  起弧成功信號擴展DI編號
    * @return 錯誤碼 
    */
    int SetArcDoneExtDiNum(int DINum);

擴展IO-配置焊機準備信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊機準備信號
    * @param [in] DINum  焊機準備信號擴展DI編號
    * @return 錯誤碼 
    */
    int SetWeldReadyExtDiNum(int DINum);

擴展IO-配置焊接中斷恢復信號
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 擴展IO-配置焊接中斷恢復信號
    * @param [in] reWeldDINum  焊接中斷後恢復焊接信號擴展DI編號
    * @param [in] abortWeldDINum  焊接中斷後退出焊接信號擴展DI編號
    * @return 錯誤碼 
    */
    int SetExtDIWeldBreakOffRecover(int reWeldDINum, int abortWeldDINum);

設置擴展IO焊接信號代碼示例
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExtDIConfig(Robot robot)
    {
        robot.SetArcStartExtDoNum(10);
        robot.SetAirControlExtDoNum(20);
        robot.SetWireForwardFeedExtDoNum(30);
        robot.SetWireReverseFeedExtDoNum(40);

        robot.SetWeldReadyExtDiNum(50);
        robot.SetArcDoneExtDiNum(60);
        robot.SetExtDIWeldBreakOffRecover(70, 80);
        robot.SetWireSearchExtDIONum(0, 1);

        int[] DIConfig = new int[16];
        int[] DOConfig = new int[16];
        int rtn = robot.GetExtDIConfig(DIConfig);
        System.out.printf("GetExtDIConfig rtn is %d\n welder ready %d\narc done %d\nreweld start %d\nabort reweld %d\nwiresearch done %d\nLaser welding State %d\nlaser welding error state %d\n",
            rtn, DIConfig[0], DIConfig[1], DIConfig[2], DIConfig[3], DIConfig[4], DIConfig[5], DIConfig[6]);

        rtn = robot.GetExtDOConfig(DOConfig);
        System.out.printf("GetExtDOConfig rtn is %d\n Arc Start %d\nAir Test %d\nWire forward %d\nWire Inverse %d\nwiresearch %d\nWeld Mode %d\nlaser Enable %d\nLaser On %d\nLaser Reset Error %d\n",
            rtn, DOConfig[0], DOConfig[1], DOConfig[2], DOConfig[3], DOConfig[4], DOConfig[5], DOConfig[6], DOConfig[7], DOConfig[8]);



        return 0;
    }

電弧跟蹤控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.2-3.7.9

.. code-block:: Java
    :linenos:

    /** 
    * @brief 電弧跟蹤控制
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
    * @param [in] sumMaxUd 上下總計最大補償量
    * @param [in] axisSelect 上下座標系選擇，0-擺動；1-工具；2-基座
    * @param [in] referenceType 上下基準電流設定方式，0-反饋；1-常數
    * @param [in] referSampleStartUd 上下基準電流採樣開始計數(反饋)，cyc
    * @param [in] referSampleCountUd 上下基準電流採樣循環計數(反饋)，cyc
    * @param [in] referenceCurrent 上下基準電流mA
    * @param [in] offsetType 偏置跟蹤類型，0-不偏置；1-採樣；2-百分比
    * @param [in] offsetParameter 偏置參數；採樣(偏置採樣開始時間，默認採一週期)；百分比(偏置百分比(-100 ~ 100))
    * @return 錯誤碼 
    */
    int ArcWeldTraceControl(int flag, double delaytime, int isLeftRight, double klr, double tStartLr, double stepMaxLr, double sumMaxLr, int isUpLow, double kud, double tStartUd, double stepMaxUd, double sumMaxUd, int axisSelect, int referenceType, double referSampleStartUd, double referSampleCountUd, double referenceCurrent,int offsetType, int offsetParameter);

電弧跟蹤AI通帶選擇
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  電弧跟蹤AI通帶選擇
    * @param  channel 電弧跟蹤AI通帶選擇,[0-3]
    * @return  錯誤碼
    */
    public int ArcWeldTraceExtAIChannelConfig(int channel)

電弧追蹤 + 多層多道補償開啓
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤 + 多層多道補償開啓
    * @return 錯誤碼
    */
    public int ArcWeldTraceReplayStart()

電弧追蹤 + 多層多道補償關閉
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧追蹤 + 多層多道補償關閉
    * @return 錯誤碼
    */
    public int ArcWeldTraceReplayEnd()

偏移量座標變化-多層多道焊
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 偏移量座標變化-多層多道焊
    * @param pointO 基準點笛卡爾位姿
    * @param pointX 基準點X向偏移方向點笛卡爾位姿
    * @param pointZ 基準點Z向偏移方向點笛卡爾位姿
    * @param dx x方向偏移量(mm)
    * @param dz z方向偏移量(mm)
    * @param dry 繞y軸偏移量(°)
    * @param offset 計算結果偏移量
    * @return 錯誤碼
    */
    public int MultilayerOffsetTrsfToBase(DescTran pointO, DescTran pointX, DescTran pointZ, double dx, double dz, double dry, DescPose offset)

多層多道焊電弧跟蹤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestArcWeldTrace(Robot robot)
    {
        JointPos mulitilineorigin1_joint=new JointPos(-24.090, -63.501, 84.288, -111.940, -93.426, 57.669);
        DescPose mulitilineorigin1_desc=new DescPose(-677.559, 190.951, -1.205, 1.144, -41.482, -82.577);

        DescTran mulitilineX1_desc=new DescTran(0,0,0);
        mulitilineX1_desc.x = -677.556;
        mulitilineX1_desc.y = 211.949;
        mulitilineX1_desc.z = -1.206;

        DescTran mulitilineZ1_desc=new DescTran(0,0,0);
        mulitilineZ1_desc.x = -677.564;
        mulitilineZ1_desc.y = 190.956;
        mulitilineZ1_desc.z = 19.817;

        JointPos mulitilinesafe_joint=new JointPos(-25.734, -63.778, 81.502, -108.975, -93.392, 56.021);
        DescPose mulitilinesafe_desc=new DescPose(-677.561, 211.950, 19.812, 1.144, -41.482, -82.577);
        JointPos mulitilineorigin2_joint=new JointPos(-29.743, -75.623, 101.241, -116.354, -94.928, 55.735);
        DescPose mulitilineorigin2_desc=new DescPose(-563.961, 215.359, -0.681, 2.845, -40.476, -87.443);

        DescTran mulitilineX2_desc=new DescTran(0,0,0);
        mulitilineX2_desc.x = -563.965;
        mulitilineX2_desc.y = 220.355;
        mulitilineX2_desc.z = -0.680;

        DescTran mulitilineZ2_desc=new DescTran(0,0,0);
        mulitilineZ2_desc.x = -563.968;
        mulitilineZ2_desc.y = 215.362;
        mulitilineZ2_desc.z = 4.331;

        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        DescPose offset=new DescPose(0, 0, 0, 0, 0, 0);

        robot.Sleep(10);
        int error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0,epos, 0, 0, offset, 0, 100);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 10, 100, 100, -1, 0,epos, 0, 0, offset, 0, 100);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,0, epos, 0, 0, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.WeaveStart(0);

        error = robot.ArcWeldTraceControl(1, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0);

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 1, 100, 100, -1, 0,epos, 0, 0,offset, 0, 100);

        error = robot.ArcWeldTraceControl(0, 0, 1, 0.06, 5, 5, 50, 1, 0.06, 5, 5, 55, 0, 0, 4, 1, 10,0,0);

        error = robot.WeaveEnd(0);

        error = robot.ARCEnd(1, 0, 10000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 10.0, 0.0, 0.0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1, 0,epos, 0, 1, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 10, 0, 0, offset);

        error = robot.ArcWeldTraceReplayStart();

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1, 0,epos, 0, 1, offset, 0, 100);

        error = robot.ArcWeldTraceReplayEnd();

        error = robot.ARCEnd(1, 0, 10000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin1_desc.tran, mulitilineX1_desc, mulitilineZ1_desc, 0, 10, 0, offset);

        error = robot.MoveL(mulitilineorigin1_joint, mulitilineorigin1_desc, 13, 0, 10, 100, 100, -1,0, epos, 0, 1, offset, 0, 100);

        error = robot.ARCStart(1, 0, 3000);

        error = robot.MultilayerOffsetTrsfToBase(mulitilineorigin2_desc.tran, mulitilineX2_desc, mulitilineZ2_desc, 0, 10, 0, offset);

        error = robot.ArcWeldTraceReplayStart();

        error = robot.MoveL(mulitilineorigin2_joint, mulitilineorigin2_desc, 13, 0, 2, 100, 100, -1,0, epos, 0, 1, offset, 0, 100);

        error = robot.ArcWeldTraceReplayEnd();

        error = robot.ARCEnd(1, 0, 3000);

        error = robot.MoveJ(mulitilinesafe_joint, mulitilinesafe_desc, 13, 0, 10, 100, 100, epos, -1, 0, offset);

        robot.CloseRPC();
        return 0;
    }

電弧跟蹤焊機電流反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電流反饋AI通道選擇
    * @param  [in] channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelCurrent(int channel)

電弧跟蹤焊機電壓反饋AI通道選擇
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電壓反饋AI通道選擇
    * @param  [in] channel 通道；0-擴展AI0；1-擴展AI1；2-擴展AI2；3-擴展AI3；4-控制箱AI0；5-控制箱AI1
    * @return 錯誤碼
    */
    int ArcWeldTraceAIChannelVoltage(int channel)

電弧跟蹤焊機電流反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電流反饋轉換參數
    * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
    * @param [in] currentLow AI通道下限對應焊機電流值，默認值0V，範圍[0-200V]
    * @param [in] currentHigh AI通道上限對應焊機電流值，默認值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    int ArcWeldTraceCurrentPara(double AILow, double AIHigh, double currentLow, double currentHigh)

電弧跟蹤焊機電壓反饋轉換參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 電弧跟蹤焊機電壓反饋轉換參數
    * @param [in] AILow AI通道下限，默認值0V，範圍[0-10V]
    * @param [in] AIHigh AI通道上限，默認值10V，範圍[0-10V]
    * @param [in] voltageLow AI通道下限對應焊機電壓值，默認值0V，範圍[0-200V]
    * @param [in] voltageHigh AI通道上限對應焊機電壓值，默認值100V，範圍[0-200V]
    * @return 錯誤碼
    */
    int ArcWeldTraceVoltagePara(double AILow, double AIHigh, double voltageLow, double voltageHigh)

電弧跟蹤代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void WeldTraceControlWithCtrlBoxAI(Robot robot)
    {
        DescPose startdescPose = new DescPose(-473.86, 257.879, -20.849, -37.317, -42.021, 2.543);
        JointPos startjointPos = new JointPos(-43.487, -76.526, 95.568, -104.445, -89.356, 3.72);

        DescPose safedescPose = new DescPose(-504.043, 275.181, 40.908, -28.002, -42.025, -14.044);
        JointPos safejointPos = new JointPos(-39.078, -76.732, 87.227, -99.47, -94.301, 18.714);

        DescPose enddescPose = new DescPose(-499.844, 141.225, 7.72, -34.856, -40.17, 13.13);
        JointPos endjointPos = new JointPos(-31.305, -82.998, 99.401, -104.426, -89.35, 3.696);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        //起始運動到安全點
        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 20, 100, exaxisPos, -1, 0, offdese);

        WeldCurrentAORelation current = new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation voltage = new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(current);//電流與輸出模擬量的關係
        robot.WeldingSetVoltageRelation(voltage);//電壓與輸出模擬量的關係
        robot.WeldingSetVoltage(0, 25, 1, 0);//設置電壓
        robot.WeldingSetCurrent(0, 260, 0, 0);//設置電流

        int rtn = robot.ArcWeldTraceAIChannelCurrent(4);
        System.out.println("ArcWeldTraceAIChannelCurrent rtn is " + rtn);

        rtn = robot.ArcWeldTraceAIChannelVoltage(5);
        System.out.println("ArcWeldTraceAIChannelVoltage rtn is " + rtn);

        rtn = robot.ArcWeldTraceCurrentPara(0.0, 5, 0, 500);
        System.out.println("ArcWeldTraceCurrentPara rtn is " + rtn);

        rtn = robot.ArcWeldTraceVoltagePara(1.018, 10, 0, 50);
        System.out.println("ArcWeldTraceVoltagePara rtn is " + rtn);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offdese);
        robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 20, 20, 100, exaxisPos, -1, 0, offdese);
    }

設置焊絲尋位擴展IO端口
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置焊絲尋位擴展IO端口
    * @param [in] searchDoneDINum 焊絲尋位成功DO端口(0-127)
    * @param [in] searchStartDONum 焊絲尋位啓停控制DO端口(0-127)
    * @return 錯誤碼
    */
    int SetWireSearchExtDIONum(int searchDoneDINum, int searchStartDONum);


示例程序
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    private static void TestUDPWireSearch(Robot robot)
    {
        UDPComParam param = new UDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10,0);
        robot.ExtDevSetUDPComParam(param);//udp擴展軸通訊

        robot.SetWireSearchExtDIONum(0, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offdese = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

        DescPose descStart = new DescPose(-158.767, -510.596, 271.709, -179.427, -0.745, -137.349);
        JointPos jointStart = new JointPos(61.667, -79.848, 108.639, -119.682, -89.700, -70.985);

        DescPose descEnd = new DescPose(0.332, -516.427, 270.688, 178.165, 0.017, -119.989);
        JointPos jointEnd = new JointPos(79.021, -81.839, 110.752, -118.298, -91.729, -70.981);

        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);

        DescPose descREF0A = new DescPose(-66.106, -560.746, 270.381, 176.479, -0.126, -126.745);
        JointPos jointREF0A = new JointPos(73.531, -75.588, 102.941, -116.250, -93.347, -69.689);

        DescPose descREF0B = new DescPose(-66.109, -528.440, 270.407, 176.479, -0.129, -126.744);
        JointPos jointREF0B = new JointPos(72.534, -79.625, 108.046, -117.379, -93.366, -70.687);

        DescPose descREF1A = new DescPose(72.975, -473.242, 270.399, 176.479, -0.129, -126.744);
        JointPos jointREF1A = new JointPos(87.169, -86.509, 115.710, -117.341, -92.993, -56.034);

        DescPose descREF1B = new DescPose(31.355, -473.238, 270.405, 176.480, -0.130, -126.745);
        JointPos jointREF1B = new JointPos(82.117, -87.146, 116.470, -117.737, -93.145, -61.090);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 0, 10, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);  //方向點
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef = {"REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = {"RES0", "RES1", "#", "#", "#", "#"};
        int offectFlag = 0;
        //DescPose offectPos = new DescPose(0, 0, 0, 0, 0, 0);
        DescOffset offset = new DescOffset();
        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offset);
        robot.PointsOffsetEnable(0, offset.offset);
        robot.MoveL(jointStart, descStart, 1, 0, 100, 100, 100, -1, exaxisPos, 0, 0, offdese, 0, 100);
        robot.MoveL(jointEnd, descEnd, 1, 0, 100, 100, 100, -1, exaxisPos, 1, 0, offdese, 0, 100);
        robot.PointsOffsetDisable();
    }

焊絲尋位開始
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊絲尋位開始
    * @param [in] refPos  1-基準點 0-接觸點
    * @param [in] searchVel   尋位速度 %
    * @param [in] searchDis  尋位距離 mm
    * @param [in] autoBackFlag 自動返回標誌，0-不自動；-自動
    * @param [in] autoBackVel  自動返回速度 %
    * @param [in] autoBackDis  自動返回距離 mm
    * @param [in] offectFlag  1-帶偏移量尋位；0-示教點尋位
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
    * @param [in] seamType  焊縫類型
    * @param [in] method   計算方法
    * @param [in] varNameRef 基準點1-6，“#”表示無點變量
    * @param [in] varNameRes 接觸點1-6，“#”表示無點變量
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

焊絲尋位接觸點寫入數據庫
++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 焊絲尋位接觸點寫入數據庫
    * @param [in] varName  接觸點名稱 “RES0” ~ “RES99”
    * @param [in] pos  接觸點數據[x, y, x, a, b, c]
    * @return 錯誤碼 
    */
    int SetPointToDatabase(String varName, DescPose pos);

機器人焊絲尋位代碼示例
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestWireSearch(Robot robot)
    {
        DescPose toolCoord=new DescPose(0, 0, 200, 0, 0, 0);
        robot.SetToolCoord(1, toolCoord, 0, 0, 1, 0);
        DescPose wobjCoord=new DescPose(0, 0, 0, 0, 0, 0);
        robot.SetWObjCoord(1, wobjCoord, 0);

        int rtn0, rtn1, rtn2 = 0;
        ExaxisPos exaxisPos = new ExaxisPos( 0, 0, 0, 0 );
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);


        DescPose descStart = new DescPose(216.543, 445.175, 93.465, 179.683, 1.757, -112.641);
        JointPos jointStart = new JointPos(-128.345, -86.660, 114.679, -119.625, -89.219, 74.303);

        DescPose descEnd =new DescPose(111.143, 523.384, 87.659, 179.703, 1.835, -97.750);
        JointPos jointEnd =new JointPos(-113.454, -81.060, 109.328, -119.954, -89.218, 74.302 );

        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,100);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese,0,100);

        DescPose descREF0A = new DescPose(142.135, 367.604, 86.523, 179.728, 1.922, -111.089);
        JointPos jointREF0A =new JointPos(-126.794, -100.834, 128.922, -119.864, -89.218, 74.302);

        DescPose descREF0B = new DescPose(254.633, 463.125, 72.604, 179.845, 2.341, -114.704);
        JointPos jointREF0B = new JointPos(-130.413, -81.093, 112.044, -123.163, -89.217, 74.303);

        DescPose descREF1A =new DescPose(92.556, 485.259, 47.476, -179.932, 3.130, -97.512);
        JointPos jointREF1A =new JointPos(-113.231, -83.815, 119.877, -129.092, -89.217, 74.303);

        DescPose descREF1B =new DescPose(203.103, 583.836, 63.909, 179.991, 2.854, -103.372);
        JointPos jointREF1B = new JointPos(-119.088, -69.676, 98.692, -121.761, -89.219, 74.303);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1,0, exaxisPos, 1, 0, offdese,0,10);  //方向點
        rtn1 = robot.WireSearchWait("REF0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese,0,10);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1,0, exaxisPos, 1, 0, offdese,0,10);  //方向點
        rtn1 = robot.WireSearchWait("REF1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF0A, descREF0A, 1, 1, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);  //起點
        robot.MoveL(jointREF0B, descREF0B, 1, 1, 100, 100, 100, -1,0, exaxisPos, 1, 0, offdese,0,10);  //方向點
        rtn1 = robot.WireSearchWait("RES0");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        rtn0 = robot.WireSearchStart(0, 10, 100, 0, 10, 100, 0);
        robot.MoveL(jointREF1A, descREF1A, 1, 1, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese,0,10);  //起點
        robot.MoveL(jointREF1B, descREF1B, 1, 1, 100, 100, 100, -1, 0,exaxisPos, 1, 0, offdese,0,10);  //方向點
        rtn1 = robot.WireSearchWait("RES1");
        rtn2 = robot.WireSearchEnd(0, 10, 100, 0, 10, 100, 0);

        String[] varNameRef =new String[]{"REF0", "REF1", "#", "#", "#", "#"};
        String[] varNameRes = new String[]{ "RES0", "RES1", "#", "#", "#", "#" };
        int offectFlag = 0;

        DescPose pos = new DescPose(0,0,0,0,0,0);
        DescOffset offectPos=new DescOffset();
        offectPos.offset=pos;
        offectPos.offsetFlag=0;

        rtn0 = robot.GetWireSearchOffset(0, 0, varNameRef, varNameRes, offectPos);
        robot.PointsOffsetEnable(0, pos);
        robot.MoveL(jointStart, descStart, 1, 1, 100, 100, 100, -1,0, exaxisPos, 0, 0, offdese,0,10);
        robot.MoveL(jointEnd, descEnd, 1, 1, 100, 100, 100, -1, 0,exaxisPos, 1, 0, offdese,0,10);
        robot.PointsOffsetDisable();

        robot.CloseRPC();
        return 0;
    }

設置焊接電壓漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
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
    int WeldingSetVoltageGradualChangeStart(int IOType, double voltageStart, double voltageEnd, int AOIndex, int blend)

設置焊接電壓漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電壓漸變結束
    * @return 錯誤碼
    */
    int WeldingSetVoltageGradualChangeEnd()

設置焊接電流漸變開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電流漸變開始
    * @param [in] IOType 控制類型；0-控制箱IO；1-數字通信協議(UDP);2-數字通信協議(ModbusTCP)
    * @param [in] currentStart 起始焊接電流(A)
    * @param [in] currentEnd 終止焊接電流(A)
    * @param [in] AOIndex 控制箱AO端口號(0-1)
    * @param [in] blend 是否平滑 0-不平滑；1-平滑
    * @return 錯誤碼
    */
    int WeldingSetCurrentGradualChangeStart(int IOType, double currentStart, double currentEnd, int AOIndex, int blend)

設置焊接電流漸變結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 設置焊接電流漸變結束
    * @return 錯誤碼
    */
    int WeldingSetCurrentGradualChangeEnd()

機器人焊接電流電壓漸變代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void WeldparamChange(Robot robot) 
    {
        DescPose startdescPose = new DescPose(-484.707, 276.996, -14.013, -37.657, -40.508, -1.548);
        JointPos startjointPos = new JointPos(-45.421, -75.673, 93.627, -104.302, -87.938, 6.005);

        DescPose enddescPose = new DescPose(-508.767, 137.109, -13.966, -37.639, -40.508, -1.559);
        JointPos endjointPos = new JointPos(-32.768, -80.947, 100.254, -106.201, -87.201, 18.648);

        DescPose safedescPose = new DescPose(-484.709, 294.436, 13.621, -37.660, -40.508, -1.545);
        JointPos safejointPos = new JointPos(-46.604, -75.410, 89.109, -100.003, -88.012, 4.823);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        WeldCurrentAORelation cur = new WeldCurrentAORelation(0, 495, 1, 10, 0);
        WeldVoltageAORelation vol = new WeldVoltageAORelation(10, 45, 1, 10, 1);
        robot.WeldingSetCurrentRelation(cur);
        robot.WeldingSetVoltageRelation(vol);

        robot.WeldingSetVoltage(0, 25, 1, 0);// ----設置電壓
        robot.WeldingSetCurrent(0, 260, 0, 0);// ----設置電流

        robot.MoveJ(safejointPos, safedescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);

        robot.WeldingSetCurrentGradualChangeStart(0, 260, 220, 0, 0);
        robot.WeldingSetVoltageGradualChangeStart(0, 25, 22, 1, 0);
        int rtn = robot.ArcWeldTraceControl(1, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);

        robot.MoveJ(startjointPos, startdescPose, 1, 0, 5, 100, 100, exaxisPos, -1, 0, offdese);
        System.out.println("ArcWeldTraceControl rtn is " + rtn);

        robot.ARCStart(0, 0, 10000);
        robot.WeaveStart(0);
        robot.WeaveChangeStart(2, 1, 24, 36);
        robot.MoveL(endjointPos, enddescPose, 1, 0, 100, 100, 2, -1, 0, exaxisPos, 0, 0, offdese, 0, 10);
        robot.ARCEnd(0, 0, 10000);
        robot.WeaveChangeEnd();
        robot.WeaveEnd(0);
        robot.ArcWeldTraceControl(0, 0, 1, 0.08, 5, 5, 300, 1, 0.06, 4, 4, 300, 1, 0, 4, 1, 10, 0, 0);
        robot.WeldingSetCurrentGradualChangeEnd();
        robot.WeldingSetVoltageGradualChangeEnd();
    }

設置自定義擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
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
    public int CustomWeaveSetPara(int id, int pointNum, DescTran[] point, double[] stayTime, double frequency, int incStayType, int stationary)

獲取自定義擺動參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.9-3.8.6

.. code-block:: Java
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
    public int CustomWeaveGetPara(int id, int[] pointNum, DescTran[] point, double[] stayTime, double[] frequency, int[] incStayType, int[] stationary)

自定義擺動參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestCustomWeaveSetPara(Robot robot)
    {
        DescTran[] point = new DescTran[10];
        point[0]=new DescTran();
        point[0].x = -3;
        point[0].y = -3;
        point[0].z = 0;

        point[1]=new DescTran();
        point[1].x = -6;
        point[1].y = 0;
        point[1].z = 0;

        point[2]=new DescTran();
        point[2].x = -3;
        point[2].y = 3;
        point[2].z = 0;

        point[3]=new DescTran();
        point[3].x = 0;
        point[3].y = 0;
        point[3].z = 0;
        point[4]=new DescTran(0,0,0);
        point[5]=new DescTran(0,0,0);
        point[6]=new DescTran(0,0,0);
        point[7]=new DescTran(0,0,0);
        point[8]=new DescTran(0,0,0);
        point[9]=new DescTran(0,0,0);

        double[] stayTime =new double[] { 0,0,0,0,0,0,0,0,0,0 };
        int rtn = robot.CustomWeaveSetPara(2, 4, point, stayTime, 1.000, 0, 0);
        System.out.println("CustomWeaveSetPara rtn is :"+ rtn);
        robot.Sleep(1000);

        int[] pointNum = new int[1];
        double[] frequency=new double[1];
        int[] incStayType=new int[1];
        int[] stationary=new int[1];
        robot.CustomWeaveGetPara(2, pointNum, point, stayTime, frequency, incStayType, stationary);
        System.out.println("pointNum is :"+ pointNum[0]);
        for (int i = 0; i < pointNum[0]; i++)
        {
            System.out.println("point:"+i+", "+ point[i].x+", "+ point[i].y+", "+ point[i].z);
        }
        System.out.println("fre is :"+ frequency[0]+", stay is:"+ incStayType[0]+", "+ stationary[0]);

        robot.WeaveSetPara(0, 9, 1.000000, 1, 5.000000,
                6.000000, 5.000000, 50, 100, 100,
                0, 1, 0.000000, 0.000000);

        DescPose desc_p1 =new DescPose(-288.650, 367.807, 288.404, 0.000, -0.001, 0.001 );
        DescPose desc_p2 = new DescPose( -431.714, 367.815, 288.415, 0.001, 0.001, 0.000 );
        DescPose desc_p3 = new DescPose( -348.666, 427.798, 288.404, -0.000, -0.000, 0.001 );
        JointPos j1 = new JointPos( 140.656, -84.560, -91.707, -93.734, 90.000, 50.655 );
        JointPos j2 = new JointPos( 149.873, -98.298, -77.599, -94.103, 90.000, 59.873 );
        JointPos j3 = new JointPos( 139.773, -96.173, -80.014, -93.814, 90.000, 49.772 );

        ExaxisPos epos = new ExaxisPos();
        DescPose offset_pos = new DescPose();

        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100,100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.Circle(j3, desc_p3, 3, 0, 100, 100, epos, j2, desc_p2, 3, 0, 100, 100, epos, 10, -1, offset_pos,0,-1,0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveC(j3, desc_p3, 3, 0, 100, 100, epos, 0, offset_pos, j2, desc_p2, 3, 0, 100, 100, epos, 0, offset_pos, 10, -1,0);
        robot.WeaveEnd(0);
        robot.MoveJ(j1, desc_p1, 3, 0, 100, 100, 100, epos, -1, 0, offset_pos);
        robot.WeaveStart(0);
        robot.MoveL(j2, desc_p2, 3, 0, 100, 100, 10, -1,epos, 0, 0, offset_pos, 0,0, 100);
        robot.WeaveEnd(0);

        robot.CloseRPC();
    }

雷射焊機參數配置
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機參數配置
    * @param  io_type 通訊類型 0-IO 1-UDP
    * @param  num 需要設置的組號（1~10）
    * @param  scanSpeed 掃描速度
    * @param  scanWidth 掃描寬度
    * @param  peakPower 峰值功率
    * @param  dutyCycle 佔空比
    * @param  freq 頻率
    * @return 錯誤碼
    */
    public int SetLaserWeldingParam(int io_type, int num, int scanSpeed, int scanWidth, int peakPower, int dutyCycle, int freq);

設置雷射焊接開始停止
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置雷射焊接開始停止
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param status 控制字 0-收光 1-出光
    * @param max_waittime 最大等待時間，單位毫秒，默認10000
    * @return 錯誤碼
    */
    public int SetLaserWeldingStartEnd(int io_type, int status, int max_waittime)

雷射焊機使能去使能
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機使能去使能
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param status 0-去使能 1-使能
    * @return 錯誤碼
    */
    public int SetLaserWeldingEnable(int io_type, int status)

雷射焊機故障復位
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機故障復位
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param status 控制字 0-無效 1-故障復位
    * @return 錯誤碼
    */
    public int ResetLaserWeldingErr(int io_type, int status)

獲取雷射焊機運行狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取雷射焊機運行狀態
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param  status 控制字 0-停機 1-運行
    * @return 錯誤碼
    */
    public int GetLaserWeldingRunningState(int io_type, int[] status)

獲取雷射焊機故障狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取雷射焊機故障狀態
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param  status 0-無故障 1-存在故障
    * @return 錯誤碼
    */
    public int GetLaserWeldingErrState(int io_type, int[] status)

獲取雷射焊機配置參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取雷射焊機10個工藝組中某一個的配置參數
    * @param num 需要設置的組號（1~10）
    * @param params 輸出參數數組：[scanSpeed, scanWidth, peakPower, dutyCycle, freq]
    * @return 錯誤碼
    */
    public int GetLaserWeldingParamTarget(int num, int[] params)

獲取當前雷射焊機生效的配置參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取當前雷射焊機生效的配置參數
    * @param io_type 通訊類型 0-IO 1-UDP
    * @param params 輸出參數數組：[scanSpeed, scanWidth, peakPower, dutyCycle, freq]
    * @return 錯誤碼
    */
    public int GetLaserWeldingParamActual(int io_type, int[] params)

配置雷射焊機擴展IO使能DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，使能的DO端口
    * @param ctrlModeDONum 雷射焊機使能的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingEnableExtDoNum(int ctrlModeDONum)

配置雷射焊機擴展IO啟動DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，啟動的DO端口
    * @param ctrlModeDONum 雷射焊機啟動（出光收光）的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingStartExtDoNum(int ctrlModeDONum)

配置雷射焊機擴展IO故障復位DO端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 雷射焊機設置擴展IO，故障復位的DO端口
    * @param ctrlModeDONum 雷射焊機故障復位的擴展DO端口號
    * @return 錯誤碼
    */
    public int SetLaserWeldingErrResetExtDoNum(int ctrlModeDONum)

配置雷射焊機擴展IO運行狀態（出光狀態）DI端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 配置雷射焊機擴展IO運行狀態（出光狀態）DI端口
    * @param diNum 配置雷射焊機運行狀態（出光狀態）擴展DI端口
    * @return 錯誤碼，0表示成功，非0表示失敗
    */
    public int SetLaserWeldingRunningStateExtDiNum(int diNum);

配置雷射焊機擴展IO故障狀態DI端口
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 配置雷射焊機擴展IO故障狀態DI端口
    * @param diNum 配置雷射焊機故障狀態擴展DI端口
    * @return 錯誤碼，0表示成功，非0表示失敗
    */
    public int SetLaserWeldingErrStateExtDiNum(int diNum);

雷射焊接代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int testLsaerWeld(Robot robot) {
        int rtn = -1;
        rtn = robot.ExtDevLoadUDPDriver();
        if (rtn != 0) {
            System.out.println("加載UDP驅動失敗，錯誤碼：" + rtn);
        }
        robot.Sleep(1000);
        rtn = robot.SetLaserWeldingParam(1, 3, 2000, 3, 1500, 100, 1000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingParam失敗，錯誤碼：" + rtn);
        } else {
            System.out.println("SetLaserWeldingParam成功");
        }
        rtn = robot.SetLaserWeldingStartExtDoNum(1);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartExtDoNum失敗，錯誤碼：" + rtn);
        }
        rtn = robot.Mode(0);
        if (rtn != 0) {
            System.out.println("設置模式0失敗，錯誤碼：" + rtn);
        }
        robot.Sleep(1000);
        DescPose desc_pos1 = new DescPose(-303.721, -206.960, 297.105, 152.209, 19.857, 109.166);
        DescPose desc_pos2 = new DescPose(-301.575, -254.888, 284.786, 155.919, 26.946, 111.629);
        DescPose desc_safe = new DescPose(-344.386, -280.830, 435.073, 173.835, 15.333, 124.931);

        JointPos jointPos1 = new JointPos(9.827, -99.740, 120.088, -78.900, -77.241, -17.904);
        JointPos jointPos2 = new JointPos(15.251, -96.456, 120.138, -84.664, -68.542, -17.843);
        JointPos jointSafe = new JointPos(19.142, -98.078, 101.493, -83.078, -77.070, -17.794);

        ExaxisPos exaxis = new ExaxisPos(0.0, 0.0, 0.0, 0.0);
        DescPose offset = new DescPose(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        int error = robot.MoveL(desc_pos1, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0,0);
        System.out.println("MoveL到pos1返回：" + error);
        rtn = robot.SetLaserWeldingStartEnd(1, 1, 10000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartEnd（啟動）失敗，錯誤碼：" + rtn);
        } else {
            System.out.println("雷射已啟動");
        }
        rtn = robot.MoveL(desc_pos2, 0, 0, 30, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0, 0);
        System.out.println("MoveL到pos2返回：" + rtn);
        rtn = robot.SetLaserWeldingStartEnd(1, 0, 10000);
        if (rtn != 0) {
            System.out.println("SetLaserWeldingStartEnd（停止）失敗，錯誤碼：" + rtn);
        } else {
            System.out.println("雷射已停止");
        }
        robot.Sleep(500);
        rtn = robot.MoveL(desc_safe, 0, 0, 100, 100, 100, -1, 0, exaxis, 0, 0, offset, -1, 0,0,0);
        System.out.println("MoveL到安全位置返回：" + rtn);
        rtn = robot.Mode(1);
        if (rtn != 0) {
            System.out.println("設置模式1失敗，錯誤碼：" + rtn);
        }
        robot.Sleep(1000);
        robot.CloseRPC();
        robot.Sleep(1000);

        System.out.println("測試完成");

        return 0;
    }

設置擺動結束回週期零點
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置擺動結束回週期零點
    * @param flag 擺動結束是否回週期零點；0-不回週期零點；1-回週期零點
    * @return 錯誤碼
    */
    public int SetWeaveBackCenterConfig(int flag)
        
獲取擺動結束回週期零點參數
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取擺動結束回週期零點參數
    * @param flag 擺動結束是否回週期零點；0-不回週期零點；1-回週期零點
    * @return 錯誤碼
    */
    public int GetWeaveBackCenterConfig(int[] flag)
            
擺動結束回週期零點代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestSplineWeave(Robot robot)
    {
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
        float oacc = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;

        robot.WeaveEnd(0);
        robot.SetSpeed(1);

        robot.SetWeaveBackCenterConfig(1);
        int[] weaveBackConfig = new int[1];
        robot.GetWeaveBackCenterConfig(weaveBackConfig);
        System.out.printf("GetWeaveBackCenterConfig:  %d \n", weaveBackConfig[0]);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, 100.0f, epos, blendT, flag, offset_pos);

        robot.WeaveStart(0);
        robot.NewSplineStart(0, 6000);
        robot.NewSplinePoint(j1, desc_pos1, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j2, desc_pos2, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j3, desc_pos3, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j4, desc_pos4, tool, user, vel, acc, ovl, -1, 1);
        robot.NewSplineEnd();
        robot.WeaveEnd(0);
    }
                
即時設置速度(指令幀，低延遲)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置速度(指令幀，低延遲)
    * @param vel 速度百分比，範圍[0~100]
    * @return 錯誤碼
    */
    public int SetSpeedInstant(int vel)
                    
設置擺動實時偏移
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置擺動實時偏移
    * @param [in] offset 實時偏移量[mm，°]
    * @return 錯誤碼
    */
    public int SetWeaveOffsetRT(DescPose offset)
                        
擺動調速與實時偏移測試代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: Java
    :linenos:

    public static void TestWeaveSpeedAndOffset(Robot robot) {
    if (robot == null) {
        System.out.println("ERROR: connect fail");
        return;
    }
    int rtn;
    ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
     ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
     DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

     JointPos j1 = new JointPos(5.027, -84.331, -75.139, -103.690, 86.379, 20.794);
     DescPose d1 = new DescPose(324.752, -83.339, 366.314, -172.321, -0.936, -106.047);

     JointPos j2 = new JointPos(-35.335, -117.598, -57.174, -95.234, 90.001, -19.560);
     DescPose d2 = new DescPose(324.999, -355.439, 260.000, 179.995, 0.003, -105.775);

     JointPos j3 = new JointPos(59.787, -117.594, -57.183, -95.222, 90.006, 75.562);
     DescPose d3 = new DescPose(324.998, 355.441, 260.002, 179.995, 0.003, -105.775);

     System.out.println("\nStep 1: MoveJ to start point");
     rtn = robot.MoveJ(j1, d1, 1, 0, 100, 100, 50, epos, -1, 0, offset_pos);
     System.out.println("  MoveJ(j1) rtn=" + rtn);
     try {
         Thread.sleep(500);
     } catch (InterruptedException e) {
         Thread.currentThread().interrupt();
     }

     System.out.println("\nStep 2: MoveJ to weave entry point");
     rtn = robot.MoveJ(j2, d2, 1, 0, 100, 100, 50, epos, -1, 0, offset_pos);
     System.out.println("  MoveJ(j2) rtn=" + rtn);
     try {
         Thread.sleep(500);
     } catch (InterruptedException e) {
         Thread.currentThread().interrupt();
     }

     System.out.println("\nStep 3: WeaveStart + MoveL in background thread");
     robot.WeaveStart(0);

     final boolean[] weaveRunning = {true};
     final int[] threadRtn = {0};
     Thread weaveThread = new Thread(new Runnable() {
         @Override
         public void run() {
             threadRtn[0] = robot.MoveL(j3, d3, 1, 0, 100, 100, 5, -1, 0, epos, 0, 0, offset_pos, 5, 0, 0, 10);
             System.out.println("  MoveL(weave) thread finished, rtn=" + threadRtn[0]);
             weaveRunning[0] = false;
         }
     });
     weaveThread.setDaemon(true);
     weaveThread.start();
     try {
         Thread.sleep(500);
     } catch (InterruptedException e) {
         Thread.currentThread().interrupt();
     }

     System.out.println("\nStep 4: SetSpeed test during weaving");
     int[] speedValues = { 20, 50, 80, 30, 60, 10 };
     for (int speed : speedValues) {
         if (!weaveRunning[0]) break;
         rtn = robot.SetSpeedInstant(speed);
         pkg = robot.GetRobotRealTimeState();
         System.out.println("  SetSpeed(" + speed + ") -> rtn=" + rtn + ", TCP_CmpSpeed=" + pkg.target_TCP_CmpSpeed);
         try {
             Thread.sleep(5000);
         } catch (InterruptedException e) {
             Thread.currentThread().interrupt();
         }
     }

     try {
         Thread.sleep(5000);
     } catch (InterruptedException e) {
         Thread.currentThread().interrupt();
     }

     System.out.println("\nStep 5: SetWeaveOffsetRT test (50 iterations, delta=0.1)");
     double accumOffset = 0.0;
     for (int i = 0; i < 50 && weaveRunning[0]; i++) {
         accumOffset += 0.1;
         DescPose weaveOffset = new DescPose(0, 0, accumOffset, 0, 0, 0);
         rtn = robot.SetWeaveOffsetRT(weaveOffset);
         pkg = robot.GetRobotRealTimeState();
         System.out.printf("  [%d/50] SetWeaveOffsetRT(x=%.1f) -> rtn=%d, TCP_pos=(%.2f,%.2f,%.2f)\n",
             i + 1, accumOffset, rtn,
             pkg.tl_cur_pos[0], pkg.tl_cur_pos[1], pkg.tl_cur_pos[2]);
         try {
             Thread.sleep(100);
         } catch (InterruptedException e) {
             Thread.currentThread().interrupt();
         }
     }

     System.out.println("\nStep 6: Wait for weave MoveL, then WeaveEnd");
      try {
          weaveThread.join();
      } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
      }
      robot.WeaveEnd(0);
      try {
          Thread.sleep(500);
      } catch (InterruptedException e) {
          Thread.currentThread().interrupt();
      }

      System.out.println("\nStep 7: MoveL back to start");
      rtn = robot.MoveL(j1, d1, 1, 0, 100, 100, 50, -1, 0, epos, 0, 0, offset_pos, 50, 0, 0, 10);
      System.out.println("  MoveL(back) rtn=" + rtn);

      pkg = robot.GetRobotRealTimeState();
      System.out.println("\n  Final robot state: main_code=" + pkg.main_code + ", sub_code=" + pkg.sub_code);
    }