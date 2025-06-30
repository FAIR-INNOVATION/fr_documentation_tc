機器人週邊
============

.. toctree:: 
    :maxdepth: 5

配置夾爪
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  配置夾爪
    * @param  [in] config .company  夹爪廠商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [in] config .device  設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [in] config .softvesion  軟體版本號，暫不使用，預設為0
    * @param  [in] config .bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int SetGripperConfig(DeviceConfig config);

取得夾爪配置
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得夾爪配置
    * @param  [out] config .company  夹爪廠商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行
    * @param  [out] config .device  設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)
    * @param  [out] config .softvesion  軟體版本號，暫不使用，預設為0
    * @param  [out] config .bus 設備掛在末端總線位置，暫不使用，預設為0
    * @return  錯誤碼
    */
    int GetGripperConfig(DeviceConfig config);

啟動夾爪
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  啟動夾爪
    * @param  [in] index  夾爪編號
    * @param  [in] act  0-復位，1-激活
    * @return  錯誤碼
    */
    int ActGripper(int index, int act); 

控制夾爪
++++++++++++++++++++++++++
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

取得夾爪運動狀態
++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  取得夾爪運動狀態
    * @return List[0]:錯誤碼; List[1] : fault  0-無錯誤，1-有錯誤; List[2]: staus  0-運動未完成，1-運動完成
    */
    List<Integer> GetGripperMotionDone(); 

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
        int company = 3;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int deviceID = -1;

        DeviceConfig gripperConfig = new DeviceConfig(company, device, softversion, bus);

        robot.SetGripperConfig(gripperConfig);
        robot.Sleep(1000);

        DeviceConfig getConfig = new DeviceConfig();
        robot.GetGripperConfig(getConfig);
        System.out.println("gripper 廠商:" + getConfig.company + " , 類型: " + getConfig.device + " , 軟體版本: " + getConfig.softwareVersion);

        int index = 1;
        byte act = 0;
        int max_time = 30000;
        byte block = 0;
        int status = -1, fault = -1;
        int rtn = -1;

        rtn = robot.ActGripper(index, act);//啟動夾爪
        System.out.println("ActGripper rtn : " + rtn);
        act = 1;
        rtn = robot.ActGripper(index, act);
        System.out.println("ActGripper rtn : " + rtn);

        rtn = robot.MoveGripper(index, 80, 20, 50, max_time,0,0,0,0);//移動夹爪
        System.out.println("MoveGripper rtn : " + rtn);
        robot.Sleep(2000);
        robot.MoveGripper(index, 20, 20, 50, max_time, block,0,0,0,0);//移動夹爪

        robot.Sleep(4000);
        List<Integer> rtnArray = new ArrayList<Integer>() {};
        rtnArray=robot.GetGripperMotionDone();
        System.out.println("gripper motion done : " + rtnArray.get(2) +", " + rtnArray.get(1));
    }

取得旋轉夾爪的旋轉圈數
++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 取得旋轉夾爪的旋轉圈數
 * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉圈數
 */
 List<Number> GetGripperRotNum();

取得旋轉夾爪的旋轉速度百分比
++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 取得旋轉夾爪的旋轉速度百分比
 * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉速度百分比
 */
 List<Number> GetGripperRotSpeed();

取得旋轉夾爪的旋轉力矩百分比
++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 取得旋轉夾爪的旋轉力矩百分比
 * @return List[0]:錯誤碼 List[1]: 0-無錯誤，1-有錯誤 List[2]:旋轉力矩百分比
 */
 List<Number> GetGripperRotTorque();

程式碼範例
++++++++++++++++++++++++++++++++
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

 robot.ResetAllError();
 robot.ActGripper(1, 1);
 robot.Sleep(1000);
 int rtn = robot.MoveGripper(1, pos, 50, 50, 5000, 1, 1, rotPos, 50, 100);
 System.out.println("move gripper rtn is:"+rtn);
 while (true)
 {
 ROBOT_STATE_PKG pkg=robot.GetRobotRealTimeState();
 if (Math.abs(pkg.gripper_position - pos) < 1.5)
 {
 break;
 }
 else
 {
 System.out.println("cur gripper pos is:"+pkg.gripper_position);
 robot.Sleep(10);
 }
 }
 System.out.println("Gripper Motion Done:"+pos);

 while (true){
 ROBOT_STATE_PKG pkg = robot.GetRobotRealTimeState();
 System.out.println("the robot AO0 "+pkg.cl_analog_output[0]/40.96+", AO1 "+pkg.cl_analog_output[1]/40.96+", tool AO0: "+pkg.tl_analog_output/40.96);
 System.out.println("gripper pos "+pkg.gripper_position+"- vel "+pkg.gripper_speed+" - torque "+pkg.gripper_current+" - rotPos "+pkg.gripperRotNum+" - rotvel "+pkg.gripperRotSpeed+" - rotTor "+ pkg.gripperRotTorque);
 robot.Sleep(200);
 }

 }

計算預抓取點-視覺
++++++++++++++++++++++++++
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
++++++++++++++++++++++++++
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
        int company = 3;
        int device = 0;
        int softversion = 0;
        int bus = 1;
        int deviceID = -1;

        DeviceConfig gripperConfig = new DeviceConfig(company, device, softversion, bus);

        robot.SetGripperConfig(gripperConfig);
        robot.Sleep(1000);

        DescPose desc_pos1, desc_pos2;
        desc_pos1 = new DescPose(-228.943, -584.228, 461.958,179.16, 5.559, 125.643);
        robot.ComputePrePick(desc_pos1, 10, 0, desc_pos2);
        System.out.println("ComputePrePick: " + desc_pos2.toString());

        desc_pos2.tran.x = 0;
        robot.ComputePostPick(desc_pos1, 10, 0, desc_pos2);
        System.out.println("ComputePostPick: " + desc_pos2.toString());
    }