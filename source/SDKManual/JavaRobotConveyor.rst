傳送帶
============

.. toctree:: 
    :maxdepth: 5

傳動皮帶啟動、停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  傳動皮帶啟動、停止
    * @param  [in] status 狀態，1-啟動，0-停止
    * @return  錯誤碼
    */
    int ConveyorStartEnd(int status);

記錄IO檢測點
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  記錄IO檢測點
    * @return  錯誤碼
    */
    int ConveyorPointIORecord();

記錄A點
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  記錄A點
    * @return  錯誤碼
    */
    int ConveyorPointARecord(); 

記錄參考點
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  記錄參考點
    * @return  錯誤碼
    */
    int ConveyorRefPointRecord();

記錄B點
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  記錄B點
    * @return 錯誤碼
    */
    int ConveyorPointBRecord(); 

傳送帶參數配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief  傳送帶參數配置
    * @param [in] encChannel 編碼器通道 1~2
    * @param [in] resolution 編碼器轉一圈的脈衝數
    * @param [in] lead 編碼器轉一圈傳送帶行走距離
    * @param [in] wpAxis 工件坐標系編號 針對追蹤運動功能選擇工件坐標系編號，追蹤抓取、TPD追蹤設為0
    * @param [in] vision 是否配視覺  0 不配  1 配
    * @param [in] speedRadio 速度比  針對傳送帶追蹤抓取選項（1-100）  其他選項預設為1
    * @param [in] followType 追蹤運動類型，0-追蹤運動；1-追檢運動
    * @param [in] startDis 追檢抓取需要設置， 追蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 預設值0
    * @param [in] endDis 追檢抓取需要設置，追蹤終止距離， 單位mm， 預設值100
    * @return 錯誤碼
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis, int endDis); 

設定傳動皮帶抓取點補償
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設定傳動皮帶抓取點補償
    * @param [in] cmp 補償位置 double[3]{x, y, z}
    * @return 錯誤碼 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

傳送帶工件IO檢測
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳送帶工件IO檢測
    * @param [in] max_t 最大檢測時間，單位ms
    * @return 錯誤碼 
    */ 
    int ConveyorIODetect(int max_t);

取得物體目前位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 取得物體目前位置
    * @param [in] mode 1-跟踪抓取，2-跟踪運動，3-TPD跟踪
    * @return 錯誤碼 
    */ 
    int ConveyorGetTrackData(int mode);

傳動皮帶追蹤開始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳動皮帶追蹤開始
    * @param [in] status 狀態，1-啟動，0-停止
    * @return 錯誤碼 
    */ 
    int ConveyorTrackStart(int status);

傳動皮帶追蹤停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳動皮帶追蹤停止
    * @return 錯誤碼 
    */ 
    int ConveyorTrackEnd();

直線運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 直線運動
    * @param [in] name 運動點描述
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] wobj 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @return 錯誤碼 
    */ 
    int ConveyorTrackMoveL(String name, int tool, int wobj, double vel, double acc, double ovl, double blendR);   

代碼範例
+++++++++++++++++++++++++++++++++++++++++
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
        int rtn = -1;
        rtn = robot.ConveyorPointIORecord();//記錄IO切入點
        System.out.println("ConveyorPointIORecord: rtn " + rtn);

        rtn = robot.ConveyorPointARecord();//記錄A點
        System.out.println("ConveyorPointARecord: rtn " + rtn);

        rtn = robot.ConveyorRefPointRecord();//記錄參考點
        System.out.println("ConveyorRefPointRecord: rtn  " + rtn);

        rtn = robot.ConveyorPointBRecord();//記錄B點
        System.out.println("ConveyorPointBRecord: rtn " + rtn);

        //配置傳送帶
        robot.ConveyorSetParam(1, 10000, 2.0, 1, 1, 20);
        System.out.println("ConveyorSetParam: rtn  " + rtn);
        //傳送帶追蹤抓取
        DescPose pos1 = new DescPose(-351.549,87.914,354.176,-179.679,-0.134,2.468);
        DescPose pos2 = new DescPose(-351.203,-213.393,351.054,-179.932,-0.508,2.472);

        Object[] cmp = {0.0, 0.0, 0.0};
        rtn = robot.ConveyorCatchPointComp(cmp);//設定傳動皮帶抓取點補償
        if(rtn != 0)
        {
            return;
        }
        System.out.println("ConveyorCatchPointComp: rtn  " + rtn);

        rtn = robot.MoveCart(pos1, 1, 0, 30.0, 180.0, 100.0, -1.0, -1);
        System.out.println("MoveCart: rtn  " + rtn);

        rtn = robot.ConveyorIODetect(10000);//傳送帶工件IO檢測
        System.out.println("ConveyorIODetect: rtn   " + rtn);

        robot.ConveyorGetTrackData(1);//配置傳送帶追蹤抓取
        rtn = robot.ConveyorTrackStart(1);//追蹤開始
        System.out.println("ConveyorTrackStart: rtn  " + rtn);

        rtn = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100.0, 0.0, 100.0, -1.0);
        System.out.println("ConveyorTrackMoveL: rtn  " + rtn);

        rtn = robot.MoveGripper(1, 60, 60, 30, 30000, 0);
        System.out.println("MoveGripper: rtn  {rtn}");

        rtn = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100.0, 0.0, 100.0, -1.0);
        System.out.println("ConveyorTrackMoveL: rtn   " + rtn);

        rtn = robot.ConveyorTrackEnd();//傳送帶追蹤停止
        System.out.println("ConveyorTrackEnd: rtn  " + rtn);

        rtn = robot.MoveCart(pos2, 1, 0, 30.0, 180.0, 100.0, -1.0, -1);
        System.out.println("MoveCart: rtn  " + rtn);

        rtn = robot.MoveGripper(1, 100, 60, 30, 30000, 0);
        System.out.println("MoveGripper: rtn  " + rtn);
    } 

傳送帶通訊輸入檢測
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳送帶通訊輸入檢測
    * @param [in] timeout 等待超時時間ms
    * @return 錯誤碼
    */
    int ConveyorComDetect(int timeout);

傳送帶通訊輸入檢測觸發
+++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳送帶通訊輸入檢測觸發
    * @param [in] timeout 等待超時時間ms
    * @return 錯誤碼
    */
    int ConveyorComDetectTrigger();
