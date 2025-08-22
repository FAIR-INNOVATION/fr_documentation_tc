機器人外設
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置夾爪
    * @param  [in] config .company  夾爪廠商，1-Robotiq，2-慧靈，3-天機，4-大寰，5-知行
    * @param  [in] config .device  設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [in] config .softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [in] config .bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int SetGripperConfig(DeviceConfig config);

獲取夾爪配置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪配置
    * @param  [out] config .company  夾爪廠商，1-Robotiq，2-慧靈，3-天機，4-大寰，5-知行
    * @param  [out] config .device  設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [out] config .softvesion  軟件版本號，暫不使用，默認爲0
    * @param  [out] config .bus 設備掛在末端總線位置，暫不使用，默認爲0
    * @return  錯誤碼
    */
    int GetGripperConfig(DeviceConfig config);

激活夾爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  激活夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    int ActGripper(int index, int act); 

控制夾爪
++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    * @return 錯誤碼
    */
    int MoveGripper(int index, int pos, int vel, int force, int max_time, int block, int type, double rotNum, int rotVel, int rotTorque); 

獲取夾爪運動狀態
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪運動狀態
    * @return List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: staus  0-運動未完成，1-運動完成
    */
    List<Integer> GetGripperMotionDone(); 

獲取夾爪激活狀態
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪激活狀態
    * @return  List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: status  bit0~bit15對應夾爪編號0~15，bit=0爲未激活，bit=1爲激活
    */
    List<Number> GetGripperActivateStatus()

獲取夾爪位置
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪位置
    * @return  List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: position  位置百分比，範圍0~100%
    */
    List<Number> GetGripperCurPosition()

獲取夾爪速度
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪速度
    * @return  List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: speed  速度百分比，範圍0~100%
    */
    List<Number> GetGripperCurSpeed()

獲取夾爪電流
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪電流
    * @return  List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: current  電流百分比，範圍0~100%
    */
    List<Number> GetGripperCurCurrent()

獲取夾爪電壓
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪電壓
    * @return List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]:voltage  電壓,單位0.1V
    */
    List<Number> GetGripperVoltage()

獲取夾爪溫度
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取夾爪溫度
    * @return List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]:temp  溫度，單位℃
    */
    List<Number> GetGripperTemp()

計算預抓取點-視覺
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算預抓取點-視覺 
    * @param [in] desc_pos  抓取點笛卡爾位姿
    * @param [in] zlength   z軸偏移量
    * @param [in] zangle    繞z軸旋轉偏移量
    * @param [out] pre_pos  獲取點
    * @return 錯誤碼 
    */ 
    int ComputePrePick(DescPose desc_pos, double zlength, double zangle, DescPose pre_pos);

計算撤退點-視覺
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 計算撤退點-視覺 
    * @param [in] desc_pos  抓取點笛卡爾位姿
    * @param [in] zlength   z軸偏移量 
    * @param [in] zangle    繞z軸旋轉偏移量
    * @param [out] post_poss 撤退點
    * @return 錯誤碼 
    */ 
    int ComputePostPick(DescPose desc_pos, double zlength, double zangle, DescPose post_pos);

機器人夾爪操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestGripper(Robot robot)
    {
        int company = 4;
        int device = 0;
        int softversion = 0;
        int bus = 2;
        int index = 2;
        int act = 0;
        int max_time = 30000;
        int block = 0;

        int current_pos = 0;
        int current = 0;
        int voltage = 0;
        int temp = 0;
        int speed = 0;

        DeviceConfig cnn=new DeviceConfig(company,device,softversion,bus);
        robot.SetGripperConfig(cnn);
        robot.GetGripperConfig(cnn);

        robot.ActGripper(index, act);
        robot.Sleep(1000);
        act = 1;
        robot.ActGripper(index, act);
        robot.Sleep(1000);

        robot.MoveGripper(index, 100, 50, 50, max_time, block, 0, 0, 0, 0);
        robot.Sleep(1000);
        robot.MoveGripper(index, 0, 50, 0, max_time, block, 0, 0, 0, 0);

        List<Integer> stat=new ArrayList<>();
        stat=robot.GetGripperMotionDone();

        List<Number> list=new ArrayList<>();
        list=robot.GetGripperActivateStatus();

        list=robot.GetGripperCurPosition();

        list=robot.GetGripperCurCurrent();

        list=robot.GetGripperVoltage();

        list=robot.GetGripperTemp();

        list=robot.GetGripperCurSpeed();

        int retval = 0;
        DescPose prepick_pose = new DescPose(){};
        DescPose postpick_pose = new DescPose(){};

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        retval = robot.ComputePrePick(p1Desc, 10, 0, prepick_pose);

        retval = robot.ComputePostPick(p2Desc, -10, 0, postpick_pose);
        return 0;
    }

獲取旋轉夾爪的旋轉圈數
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉圈數
    * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉圈數
    */
    List<Number> GetGripperRotNum(); 

獲取旋轉夾爪的旋轉速度百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉速度百分比
    * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉速度百分比
    */
    List<Number> GetGripperRotSpeed(); 

獲取旋轉夾爪的旋轉力矩百分比
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取旋轉夾爪的旋轉力矩百分比
    * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉力矩百分比
    */
    List<Number> GetGripperRotTorque(); 

代碼示獲取旋轉夾爪狀態代碼示例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestRotGripperState(Robot robot)
    {
        int fault = 0;
        List<Number> rotNum=new ArrayList<>();
        List<Number> rotSpeed=new ArrayList<>();
        List<Number> rotTorque=new ArrayList<>();

        rotNum=robot.GetGripperRotNum();
        rotSpeed=robot.GetGripperRotSpeed();
        rotTorque=robot.GetGripperRotTorque();
        System.out.println("gripper rot num :"+rotNum.get(2)+ ", gripper rotSpeed :"+rotSpeed.get(2)+",gripper rotTorque : "+rotTorque.get(2));

        return 0;
    }

傳動帶啓動、停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  傳動帶啓動、停止
    * @param  [in] status 狀態，1-啓動，0-停止
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

獲取物體當前位置
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取物體當前位置
    * @param [in] mode 1-跟蹤抓取，2-跟蹤運動，3-TPD跟蹤
    * @return 錯誤碼 
    */ 
    int ConveyorGetTrackData(int mode);

傳動帶跟蹤開始
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳動帶跟蹤開始
    * @param [in] status 狀態，1-啓動，0-停止
    * @return 錯誤碼 
    */ 
    int ConveyorTrackStart(int status);

傳動帶跟蹤停止
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 傳動帶跟蹤停止
    * @return 錯誤碼 
    */ 
    int ConveyorTrackEnd();

傳動帶參數配置
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief  傳動帶參數配置
    * @param [in] encChannel 編碼器通道 1~2
    * @param [in] resolution 編碼器轉一圈的脈衝數
    * @param [in] lead 編碼器轉一圈傳送帶行走距離
    * @param [in] wpAxis 工件座標系編號 針對跟蹤運動功能選擇工件座標系編號，跟蹤抓取、TPD跟蹤設爲0
    * @param [in] vision 是否配視覺  0 不配  1 配
    * @param [in] speedRadio 速度比  針對傳送帶跟蹤抓取選項（1-100）  其他選項默認爲1
    * @param [in] followType 跟蹤運動類型，0-跟蹤運動；1-追檢運動
    * @param [in] startDis 追檢抓取需要設置， 跟蹤起始距離， -1：自動計算(工件到達機器人下方後自動追檢)，單位mm， 默認值0
    * @param [in] endDis 追檢抓取需要設置，跟蹤終止距離， 單位mm， 默認值100
    * @return 錯誤碼
    */
    int ConveyorSetParam(int encChannel, int resolution, double lead, int wpAxis, int vision, double speedRadio, int followType, int startDis, int endDis); 

設置傳動帶抓取點補償
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置傳動帶抓取點補償
    * @param [in] cmp 補償位置 double[3]{x, y, z}
    * @return 錯誤碼 
    */ 
    int ConveyorCatchPointComp(Object[] cmp);

傳動帶直線運動
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

機器人傳送帶操作示例程序
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestConveyor(Robot robot)
    {
        int retval = 0;

        retval = robot.ConveyorStartEnd(1);

        retval = robot.ConveyorPointIORecord();

        retval = robot.ConveyorPointARecord();

        retval = robot.ConveyorRefPointRecord();

        retval = robot.ConveyorPointBRecord();

        retval = robot.ConveyorStartEnd(0);

        retval = 0;

        retval = robot.ConveyorSetParam(1,10000,200,0,0,20,0,0,100);

        Object[] cmp = new Object[]{ 0.0, 0.0, 0.0 };
        retval = robot.ConveyorCatchPointComp(cmp);

        int index = 1;
        int max_time = 30000;
        int block = 0;
        retval = 0;

        DescPose p1Desc=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose p2Desc=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);


        retval = robot.MoveCart(p1Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.WaitMs(1);

        retval = robot.ConveyorTrackStart(1);

        retval = robot.ConveyorTrackMoveL("cvrCatchPoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.MoveGripper(index, 51, 40, 30, max_time, block, 0, 0, 0, 0);

        retval = robot.ConveyorTrackMoveL("cvrRaisePoint", 1, 0, 100, 100, 100, -1.0);

        retval = robot.ConveyorTrackEnd();

        robot.MoveCart(p2Desc, 1, 0, 100.0, 100.0, 100.0, -1.0, -1);

        retval = robot.MoveGripper(index, 100, 40, 10, max_time, block, 0, 0, 0, 0);

        return 0;
    }

末端傳感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端傳感器配置
    * @param [in] config idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param [in] config idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware 軟件版本，0-J1.0/HuiDe1.0(暫未開放)
    * @param [in] config idBus 掛載位置，1-末端1號口；2-末端2號口...8-末端8號口(暫未開放)
    * @return 錯誤碼
    */
    int AxleSensorConfig(DeviceConfig config);

獲取末端傳感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取末端傳感器配置
    * @param [out] config idCompany 廠商，18-JUNKONG；25-HUIDE
    * @param [out] config idDevice 類型，0-JUNKONG/RYR6T.V1.0
    * @return 錯誤碼
    */
    int AxleSensorConfigGet(DeviceConfig config);

末端傳感器激活
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端傳感器激活
    * @param [in] actFlag 0-復位；1-激活
    * @return 錯誤碼
    */
    int AxleSensorActivate(int actFlag);

末端傳感器寄存器寫入
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端傳感器寄存器寫入
    * @param [in] devAddr  設備地址編號 0-255
    * @param [in] regHAddr 寄存器地址高8位
    * @param [in] regLAddr 寄存器地址低8位
    * @param [in] regNum  寄存器個數 0-255
    * @param [in] data1 寫入寄存器數值1
    * @param [in] data2 寫入寄存器數值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 錯誤碼
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

末端傳感器代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleSensor(Robot robot)
    {
        DeviceConfig con=new DeviceConfig(18,0,0,1);
        robot.AxleSensorConfig(con);
        int company = -1;
        int type = -1;
        robot.AxleSensorConfigGet(con);

        int rtn = robot.AxleSensorActivate(1);

        robot.Sleep(1000);

        rtn = robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
        return 0;
    }

獲取機器人外設協議
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取機器人外設協議
    * @return List[0]:錯誤碼; List[1] : int protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

設置機器人外設協議
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置機器人外設協議
    * @param [in] protocol 機器人外設協議號 4096-擴展軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼 
    */
    int SetExDevProtocol(int protocol);

設置機器人外設協議示例程序
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestExDevProtocol(Robot robot)
    {
        int protocol = 4096;
        int rtn = robot.SetExDevProtocol(protocol);
        List<Integer> integer=new ArrayList<>();
        integer = robot.GetExDevProtocol();

        return 0;
    }

獲取末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 獲取末端通訊參數
    * @param [out] param 末端通訊參數
    * @return 錯誤碼 
    */
    int GetAxleCommunicationParam(AxleComParam param)

設置末端通訊參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 設置末端通訊參數
    * @param [in] param 末端通訊參數
    * @return 錯誤碼 
    */
    int SetAxleCommunicationParam(AxleComParam param)

設置末端文件傳輸類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置末端文件傳輸類型
    * @param [in] type 1-MCU升級文件；2-LUA文件
    * @return  錯誤碼
    */
    public int SetAxleFileType(int type)

設置啓用末端LUA執行
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置啓用末端LUA執行
    * @param [in] enable 0-不啓用；1-啓用
    * @return  錯誤碼
    */
    public int SetAxleLuaEnable(int enable)

末端LUA文件異常錯誤恢復
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端LUA文件異常錯誤恢復
    * @param [in] status 0-不恢復；1-恢復
    * @return  錯誤碼
    */
    public int SetRecoverAxleLuaErr(int status)

獲取末端LUA執行使能狀態
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取末端LUA執行使能狀態
    * @param [out] status[0]: 0-未使能；1-已使能
    * @return  錯誤碼
    */
    int GetAxleLuaEnableStatus(int[] status)

設置末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置末端LUA末端設備啓用類型
    * @param forceSensorEnable 力傳感器啓用狀態，0-不啓用；1-啓用
    * @param gripperEnable 夾爪啓用狀態，0-不啓用；1-啓用
    * @param IOEnable IO設備啓用狀態，0-不啓用；1-啓用
    * @return  錯誤碼
    */
    public int SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable)

獲取末端LUA末端設備啓用類型
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取末端LUA末端設備啓用類型
     * @param enable enable[0]:forceSensorEnable 力傳感器啓用狀態，0-不啓用；1-啓用
     * @param enable enable[1]:gripperEnable 夾爪啓用狀態，0-不啓用；1-啓用
     * @param enable enable[2]:IOEnable IO設備啓用狀態，0-不啓用；1-啓用
     * @return  錯誤碼
     */
    public int GetAxleLuaEnableDeviceType(int[] enable)

獲取當前配置的末端設備
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前配置的末端設備
     * @param forceSensorEnable 力傳感器啓用設備編號 0-未啓用；1-啓用
     * @param gripperEnable 夾爪啓用設備編號，0-不啓用；1-啓用
     * @param IODeviceEnable IO設備啓用設備編號，0-不啓用；1-啓用
     * @return  錯誤碼
     */
    public int GetAxleLuaEnableDevice(int[] forceSensorEnable, int[] gripperEnable, int[] IODeviceEnable)

設置啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 設置啓用夾爪動作控制功能
     * @param id 夾爪設備編號
     * @param func func[0]-夾爪使能；func[1]-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩
     * @return  錯誤碼
     */
    public int SetAxleLuaGripperFunc(int id, int[] func)

獲取啓用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取啓用夾爪動作控制功能
     * @param id 夾爪設備編號
     * @param func func[0]-夾爪使能；func[1]-夾爪初始化；2-位置設置；3-速度設置；4-力矩設置；6-讀夾爪狀態；7-讀初始化狀態；8-讀故障碼；9-讀位置；10-讀速度；11-讀力矩
     * @return  錯誤碼
     */
    public int GetAxleLuaGripperFunc(int id, int[] func)

機器人Ethercat從站文件寫入
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 機器人Ethercat從站文件寫入
     * @param type 從站文件類型，1-升級從站文件；2-升級從站配置文件
     * @param slaveID 從站號
     * @param fileName 上傳文件名
     * @return  錯誤碼
     */
    public int SlaveFileWrite(int type, int slaveID, String fileName)

上傳末端Lua開放協議文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 上傳末端Lua開放協議文件
     * @param filePath 本地lua文件路徑名 ".../AXLE_LUA_End_DaHuan.lua"
     * @return 錯誤碼
     */
    public int AxleLuaUpload(String filePath)

機器人Ethercat從站進入boot模式
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 機器人Ethercat從站進入boot模式
     * @return  錯誤碼
     */
    public int SetSysServoBootMode()

機器人末端LUA文件操作代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAxleLua(Robot robot)
    {
        robot.AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");

        AxleComParam param=new AxleComParam(7, 8, 1, 0, 5, 3, 1);
        robot.SetAxleCommunicationParam(param);

        robot.GetAxleCommunicationParam(param);

        robot.SetAxleLuaEnable(1);
        int[] luaEnableStatus = new int[]{0};
        robot.GetAxleLuaEnableStatus(luaEnableStatus);
        robot.SetAxleLuaEnableDeviceType(0, 1, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        int [] enable=new int[]{0,0,0};
        robot.GetAxleLuaEnableDeviceType(enable);

        int[] func = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot.SetAxleLuaGripperFunc(1, func);
        int[] getFunc = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        robot.GetAxleLuaGripperFunc(1, getFunc);
        int[] getforceEnable = { 0,0,0,0,0,0,0,0};
        int[] getgripperEnable = { 0,0,0,0,0,0,0,0};
        int[] getioEnable = { 0,0,0,0,0,0,0,0};
        robot.GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getforceEnable[i]);
        }
        System.out.println("getgripperEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getgripperEnable[i]);
        }
        System.out.println("getioEnable status : ");
        for (int i = 0; i < 8; i++)
        {
            System.out.println(getioEnable[i]);
        }
        robot.ActGripper(1, 0);
        robot.Sleep(2000);
        robot.ActGripper(1, 1);
        robot.Sleep(2000);
        robot.MoveGripper(1, 90, 10, 100, 50000, 0, 0, 0, 0, 0);
        int pos = 0;
        while (true)
        {
            ROBOT_STATE_PKG pkg=new ROBOT_STATE_PKG();
            pkg=robot.GetRobotRealTimeState();
            System.out.println("gripper pos is:"+pkg.gripper_position);
            robot.Sleep(100);
        }

    }

獲取SmartTool按鈕狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1

.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取SmartTool按鈕狀態
    * @param [out] state SmartTool手柄按鈕狀態;(bit0:0-通信正常；1-通信掉線；bit1-撤銷操作；bit2-清空程序；bit3-A鍵；bit4-B鍵；bit5-C鍵；bit6-D鍵；bit7-E鍵；bit8-IO鍵；bit9-手自動；bit10開始)
    * @return 錯誤碼
    */
    int GetSmarttoolBtnState(int[] state)

SmartTool按鈕代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args) 
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true, 100, 500);//設置重連次數、間隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn == 0) {
            System.out.println("rpc連接 success");
        } else {
            System.out.println("rpc連接 fail");
            return;
        }

        int[] state = {0};
        while (true)
        {
            robot.GetSmarttoolBtnState(state);

            String binaryString = String.format("%32s", Integer.toBinaryString(state[0])).replace(' ', '0');
            System.out.println("GetSmarttoolBtnState:"+binaryString);
            robot.Sleep(100);
        }
    }


上傳開放協議的Lua文件
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 上傳開放協議的Lua文件
    * @param  filePath 本地開放協議lua文件路徑名
    * @return 錯誤碼
    */
    public int OpenLuaUpload(String filePath)


獲取從站板卡參數
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  獲取從站板卡參數
    * @param  type  0-Ethercat，1-CClink, 3-Ethercat, 4-EIP
    * @param  version  協議版本
    * @param  connState  0-未連接 1-已連接
    * @return  錯誤碼
    */
    public int GetFieldBusConfig(int[] type, int[] version, int[] connState)

寫入從站DO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  寫入從站DO
    * @param   DOIndex  DO編號
    * @param   wirteNum  寫入的數量
    * @param   status 寫入的數值，最多寫8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveWriteDO(int DOIndex, int wirteNum, int[] status)

寫入從站AO
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  寫入從站AO
    * @param  AOIndex  AO編號
    * @param  wirteNum  寫入的數量
    * @param  status 寫入的數值，最多寫8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveWriteAO(int AOIndex, int wirteNum, int[] status)

讀取從站DI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  讀取從站DI
    * @param  DOIndex  DI編號
    * @param  readNum  讀取的數量
    * @param  status 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveReadDI(int DOIndex, int readNum, int[] status)

讀取從站AI
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  讀取從站AI
    * @param  AIIndex  AI編號
    * @param  readNum  讀取的數量
    * @param  status 讀取到的數值，最多讀8個
    * @return  錯誤碼
    */
    public int FieldBusSlaveReadAI(int AIIndex, int readNum, double[] status)

等待擴展DI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待擴展DI輸入
    * @param  DIIndex DI編號
    * @param  status 0-低電平；1-高電平
    * @param  waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    public int FieldBusSlaveWaitDI(int DIIndex, int status, int waitMs)

等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待擴展AI輸入
    * @param  AIIndex AI編號
    * @param  waitType 0-大於；1-小於
    * @param  value AI值
    * @param  waitMs 最大等待時間(ms)
    * @return 錯誤碼
    */
    public int FieldBusSlaveWaitAI(int AIIndex, int waitType, double value, int waitMs)

從站模式相關接口指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testFieldBusBoard(Robot robot)
    {
        //上傳並加載開放協議文件
        robot.OpenLuaUpload("D://zUP/1111/CtrlDev_field.lua");
        robot.Sleep(2000);
        robot.SetCtrlOpenLUAName(3, "CtrlDev_field.lua");
        robot.UnloadCtrlOpenLUA(3);
        robot.LoadCtrlOpenLUA(3);
        robot.Sleep(8000);
        int[] type=new int[1];
        int[] version=new int[1];
        int[] connState=new int[1];
        //獲取從站板卡的協議類型、軟件版本、與PLC的連接狀態
        robot.GetFieldBusConfig(type, version, connState);
        System.out.println("type is: "+type[0]+", version is : "+version[0]+", connState is : "+connState[0]);
        //寫入DO0 = 1、DO1 = 0、DO2 = 1
        int[] ctrl =new int[8];
        ctrl[0] = 1;
        ctrl[1] = 0;
        ctrl[2] = 1;
        robot.FieldBusSlaveWriteDO(0, 3, ctrl);
        //寫入AO2 = 0x1000
        int[] ctrlAO =new int[8];
        ctrlAO[0] = 0x1000;
        robot.FieldBusSlaveWriteAO(2, 1, ctrlAO);
        int[] DI=new int[4];
        double[] AI=new double[3];
        //循環監控DI0~DI3 AI0~AI2
        for (int i = 0; i < 100; i++)
        {
            robot.FieldBusSlaveReadDI(0, 4, DI);
            System.out.println("DI0 is: "+DI[0]+", DI1 is: "+DI[1]+",DI2 is: "+DI[2]+",DI3 is: "+DI[3]);
            robot.FieldBusSlaveReadAI(0, 3, AI);
            System.out.println("AI0 is: "+AI[0]+ ",AI1 is: "+AI[1]+",AI2 is: "+AI[2]);
            robot.Sleep(10);
        }
        //等待DI0是否爲1，等待時間100ms，並打印結果
        int ret = robot.FieldBusSlaveWaitDI(0, 1, 100);
        System.out.println("FieldBusSlaveWaitDI result is: "+ ret);
        //等待AI0是否大於400，等待時間100ms，並打印結果
        ret = robot.FieldBusSlaveWaitAI(0,0,400.00,100);
        System.out.println("FieldBusSlaveWaitAI result is: "+ ret);
        robot.CloseRPC();
    }

控制陣列式吸盤
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 控制陣列式吸盤
    * @param  slaveID 從站號
    * @param  len 長度
    * @param  ctrlValue 控制值 1-按最大真空度吸取 2-按設定真空度吸取 3-停止吸取
    * @return 錯誤碼
    */
    public int SetSuckerCtrl(int slaveID, int len, int[] ctrlValue)

獲取陣列式吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 獲取陣列式吸盤狀態
    * @param  slaveID 從站號
    * @param  state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param  pressValue 當前真空度 單位kpa
    * @param  error 吸盤當前的錯誤碼
    * @return 錯誤碼
    */
    public int GetSuckerState(int slaveID, int[] state, int[] pressValue, int[] error)

等待吸盤狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 等待吸盤狀態
    * @param  slaveID 從站號
    * @param  state 吸附狀態 0-釋放物體 1-檢測到工件吸附成功 2-沒有吸附到物體 3-物體脫離
    * @param  ms 等待最大時間
    * @return 錯誤碼
    */
    public int WaitSuckerState(int slaveID, int state, int ms)

陣列式吸盤控制指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void testSucker(Robot robot)
    {
        //上傳並加載開放協議文件
        robot.OpenLuaUpload("C：//項目/外設SDK/CtrlDev_sucker.lua");
        robot.Sleep(2000);
        robot.UnloadCtrlOpenLUA(1);
        robot.LoadCtrlOpenLUA(1);
        robot.Sleep(1000);
        //控制吸盤廣播模式下，按照最大能力吸附
        int[] ctrl = {1};
        robot.SetSuckerCtrl(0, 1, ctrl);
        int[] state=new int[1];
        int[] pressVlaue=new int[1];
        int[] error=new int[1];
        //循環監控1號吸盤和12號吸盤的狀態
        for (int i = 0; i < 100; i++)
        {
            robot.GetSuckerState(1, state,pressVlaue, error);
            System.out.println("sucker1 state is:"+state[0]+",pressVlaue is:"+pressVlaue[0]+",error num is"+error[0]);
            robot.GetSuckerState(12, state, pressVlaue, error);
            System.out.println("sucker12 state is :"+state[0]+", pressVlaue is:"+pressVlaue[0]+",error num is:"+error[0]);
            robot.Sleep(100);
        }
        //等待1號吸盤是否爲吸附到物體的狀態，等待時間100ms
        int ret = robot.WaitSuckerState(1, 1, 100);
        System.out.println("WaitSuckerState result is:"+ ret);
        //單播模式關閉1號和12號吸盤
        ctrl[0] = 3;
        robot.SetSuckerCtrl(1, 1, ctrl);
        robot.SetSuckerCtrl(12, 1, ctrl);
        robot.CloseRPC();
    }