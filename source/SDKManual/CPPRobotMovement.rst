機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog點動
    * @param  [in]  ref 0-關節點動，2-基座標系下點動，4-工具座標系下點動，8-工件座標系下點動
    * @param  [in]  nb 1-關節1(或x軸)，2-關節2(或y軸)，3-關節3(或z軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param  [in]  dir 0-負方向，1-正方向
    * @param  [in]  vel 速度百分比，[0~100]
    * @param  [in]  acc 加速度百分比， [0~100]
    * @param  [in]  max_dis 單次點動最大角度，單位[°]或距離，單位[mm]
    * @return  錯誤碼
    */
    errno_t  StartJOG(uint8_t ref, uint8_t nb, uint8_t dir, float vel, float acc, float max_dis);

jog點動減速停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  jog點動減速停止
    * @param  [in]  ref  1-關節點動停止，3-基座標系下點動停止，5-工具座標系下點動停止，9-工件座標系下點動停止
    * @return  錯誤碼
    */
    errno_t  StopJOG(uint8_t ref);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    errno_t  ImmStopJOG(); 

機器人點動控制代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestJOG(void)
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
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.ImmStopJOG();
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.ImmStopJOG();
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.StopJOG(5);
             robot.Sleep(1000);
         }
         for (int i = 0; i < 6; i++)
         {
             robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0);
             robot.Sleep(1000);
             robot.StopJOG(9);
             robot.Sleep(1000);
         }
         robot.CloseRPC();
         return 0;
     }

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    errno_t  MoveJ(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos *epos, float blendT, uint8_t offset_flag, DescPose *offset_pos);

關節空間運動(自動正運動學計算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節空間運動(自動正運動學計算)
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] epos 擴充軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @return 錯誤碼
    */
    errno_t MoveJ(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos* epos, float blendT, uint8_t offset_flag, DescPose* offset_pos);
   
笛卡爾空間直線運動
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief   笛卡爾空間直線運動
    * @param [in] joint_pos 目標關節位置，單位deg
    * @param [in] desc_pos 目標笛卡爾位姿
    * @param [in] tool 工具座標系編號，範圍[0~14]
    * @param [in] user 工件/使用者座標系編號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100]（暫不開放）
    * @param [in] ovl 速度縮放因子[0~100] / 物理速度(mm/s)
    * @param [in] blendR [-1.0]-運動到位（阻塞），[0~1000.0]-平滑半徑（非阻塞），單位mm
    * @param [in] blendMode 過渡方式；0-內切過渡；1-角落過渡
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] search 0-不進行焊絲尋位，1-進行焊絲尋位
    * @param [in] offset_flag 0-不偏移，1-在基座標系/工件座標系下偏移，2-在工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] oacc 加速度縮放因子[0-100] / 物理加速度(mm/s²)
    * @param [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s²)
    * @param [in] overSpeedStrategy 超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認為0
    * @param [in] speedPercent 允許降速閾值百分比[0-100]，默認10%
    * @return 錯誤碼
    */
    errno_t MoveL(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos *epos, uint8_t search, uint8_t offset_flag, DescPose *offset_pos, float oacc = 100.0, int velAccParamMode = 0, int overSpeedStrategy = 0, int speedPercent = 10);

笛卡爾空間直線運動(自動逆運動學計算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡爾空間直線運動(自動逆運動學計算)
    * @param [in] desc_pos  目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] blendMode 過渡方式；0-內切過渡；1-角點過渡
    * @param [in] epos 擴充軸位置，單位mm
    * @param [in] search 0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param [in] overSpeedStrategy 超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，預設為0
    * @param [in] speedPercent 允許降速閾值百分比[0-100]，預設10%
    * @return 錯誤碼
    */
    errno_t MoveL(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos* epos, uint8_t search, uint8_t offset_flag, DescPose* offset_pos, int config = -1, int overSpeedStrategy = 0, int speedPercent = 10);

笛卡爾空間圓弧運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴充軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴充軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_t  位姿偏移量   
    * @param [in] ovl 速度縮放因子[0~100] / 物理速度(mm/s)
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] oacc 加速度縮放因子[0-100] / 物理加速度(mm/s²)
    * @param [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s²)
    * @return 錯誤碼
    */
    errno_t MoveC(JointPos *joint_pos_p, DescPose *desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos *epos_p, uint8_t poffset_flag, DescPose *offset_pos_p, JointPos *joint_pos_t, DescPose *desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos *epos_t, uint8_t toffset_flag, DescPose *offset_pos_t, float ovl, float blendR, float oacc = 100.0, int velAccParamMode = 0);

笛卡爾空間圓弧運動 (自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡爾空間圓弧運動 (自動逆運動學計算)
    * @param [in] desc_pos_p  路徑點笛卡爾位姿
    * @param [in] ptool 工具座標號，範圍[0~14]
    * @param [in] puser 工件座標號，範圍[0~14]
    * @param [in] pvel 速度百分比，範圍[0~100]
    * @param [in] pacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p 擴充軸位置，單位mm
    * @param [in] poffset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_p 位姿偏移量
    * @param [in] desc_pos_t  目標點笛卡爾位姿
    * @param [in] ttool 工具座標號，範圍[0~14]
    * @param [in] tuser 工件座標號，範圍[0~14]
    * @param [in] tvel 速度百分比，範圍[0~100]
    * @param [in] tacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t 擴充軸位置，單位mm
    * @param [in] toffset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_t 位姿偏移量
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t MoveC(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, uint8_t poffset_flag, DescPose* offset_pos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, uint8_t toffset_flag, DescPose* offset_pos_t, float ovl, float blendR, int config = -1);

笛卡爾空間整圓運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     *@brief  笛卡爾空間整圓運動
     *@param  [in] joint_pos_p  路徑點1關節位置,單位deg
     *@param  [in] desc_pos_p   路徑點1笛卡爾位姿
     *@param  [in] ptool  工具座標號，範圍[1~15]
     *@param  [in] puser  工件座標號，範圍[1~15]
     *@param  [in] pvel  速度百分比，範圍[0~100]
     *@param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
     *@param  [in] epos_p  擴充軸位置，單位mm
     *@param  [in] joint_pos_t  路徑點2關節位置,單位deg
     *@param  [in] desc_pos_t   路徑點2笛卡爾位姿
     *@param  [in] ttool  工具座標號，範圍[1~15]
     *@param  [in] tuser  工件座標號，範圍[1~15]
     *@param  [in] tvel  速度百分比，範圍[0~100]
     *@param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
     *@param  [in] epos_t  擴充軸位置，單位mm
     * @param [in] ovl 速度縮放因子[0~100] / 物理速度(mm/s)
     * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
     * @param [in] offset_pos 位姿偏移量
     * @param [in] oacc 加速度縮放因子[0-100] / 物理加速度(mm/s²)
     *@param  [in] blendR -1：阻塞；0~1000：平滑半徑
    * @param [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s²)
    * @return 錯誤碼
    */
    errno_t Circle(JointPos* joint_pos_p, DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, JointPos* joint_pos_t, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int velAccParamMode = 0);

笛卡爾空間整圓運動(自動逆運動學計算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡爾空間整圓運動(自動逆運動學計算)
    * @param [in] desc_pos_p  路徑點1笛卡爾位姿
    * @param [in] ptool 工具座標號，範圍[0~14]
    * @param [in] puser 工件座標號，範圍[0~14]
    * @param [in] pvel 速度百分比，範圍[0~100]
    * @param [in] pacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p 擴充軸位置，單位mm
    * @param [in] desc_pos_t  路徑點2笛卡爾位姿
    * @param [in] ttool 工具座標號，範圍[0~14]
    * @param [in] tuser 工件座標號，範圍[0~14]
    * @param [in] tvel 速度百分比，範圍[0~100]
    * @param [in] tacc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t 擴充軸位置，單位mm
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] oacc 加速度百分比
    * @param [in] blendR -1：阻塞；0~1000：平滑半徑
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t Circle(DescPose* desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos* epos_p, DescPose* desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos* epos_t, float ovl, uint8_t offset_flag, DescPose* offset_pos, double oacc = 100.0, double blendR = -1, int config = -1);
    
笛卡爾空間點到點運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡爾空間點到點運動
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms 
    * @param [in] config 關節空間配置，[-1]-參考目前關節位置解算，[0~7]-參考特定關節空間配置解算，預設為-1   
    * @return 錯誤碼
    */
    errno_t MoveCart(DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

機器人基本運動指令程式碼範例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestMove(void)
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

        JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0;
        float acc = 100.0;
        float ovl = 100.0;
        float oacc = 100.0;
        float blendT = 0.0;
        float blendR = 0.0;
        uint8_t flag = 0;
        uint8_t search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&j2, &desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, oacc, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&j3, &desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &j4, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, oacc, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&j3, &desc_pos3, tool, user, vel, acc, &epos, &j1, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(&desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(&desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, &epos, search, flag, &offset_pos, -1, velAccMode);
        printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(&desc_pos3, tool, user, vel, acc, &epos, flag, &offset_pos, &desc_pos4, tool, user, vel, acc, &epos, flag, &offset_pos, ovl, blendR, -1, velAccMode);
        printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(&j2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
        printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(&desc_pos3, tool, user, vel, acc, &epos, &desc_pos1, tool, user, vel, acc, &epos, ovl, flag, &offset_pos, oacc, blendR, -1, velAccMode);
        printf("circle errcode:%d\n", rtn);
        robot.CloseRPC();
        return 0;
    }

笛卡爾空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡爾空間螺旋線運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos  擴充軸位置，單位mm
    * @param  [in] ovl  速度縮放因子，範圍[0~100]    
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] spiral_param  螺旋參數
    * @return  錯誤碼
    */
    errno_t NewSpiral(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, ExaxisPos *epos, float ovl, uint8_t offset_flag, DescPose *offset_pos, SpiralParam spiral_param);  

笛卡爾空間螺旋線運動 (自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 笛卡爾空間螺旋線運動 (自動逆運動學計算)
    * @param [in] desc_pos  目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos 擴充軸位置，單位mm
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] spiral_param 螺旋參數
    * @param [in] config 逆解關節空間配置，[-1]-參考目前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t NewSpiral(DescPose* desc_pos, int tool, int user, float vel, float acc, ExaxisPos* epos, float ovl, uint8_t offset_flag, DescPose* offset_pos, SpiralParam spiral_param, int config = -1);

螺旋線運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestSpiral(void)
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
      JointPos j(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
      DescPose desc_pos(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
      DescPose offset_pos1(50, 0, 0, -30, 0, 0);
      DescPose offset_pos2(50, 0, 0, -5, 0, 0);
      ExaxisPos epos(0, 0, 0, 0);
      SpiralParam sp;
      sp.circle_num = 5;
      sp.circle_angle = 5.0;
      sp.rad_init = 50.0;
      sp.rad_add = 10.0;
      sp.rotaxis_add = 10.0;
      sp.rot_direction = 0;
      int tool = 0;
      int user = 0;
      float vel = 100.0;
      float acc = 100.0;
      float ovl = 100.0;
      float blendT = 0.0;
      uint8_t flag = 2;
      robot.SetSpeed(20);
      rtn = robot.MoveJ(&j, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos1);
      printf("movej errcode:%d\n", rtn);
      rtn = robot.NewSpiral(&desc_pos, tool, user, vel, acc, &epos, ovl, flag, &offset_pos2, sp);
      printf("newspiral errcode:%d\n", rtn);
      robot.CloseRPC();
      return 0;
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼
    */
    errno_t ServoMoveStart();

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼
    */
    errno_t ServoMoveEnd();

關節空間伺服模式運動
+++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，默認爲0
    * @return  錯誤碼
    */
    errno_t  ServoJ(JointPos *joint_pos, float acc, float vel, float cmdT, float filterT, float gain);

關節空間伺服模式運動示例程序
++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoJ(void)
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
        JointPos j(0, 0, 0, 0, 0, 0);
        ExaxisPos epos(0, 0, 0, 0);
        float vel = 0.0;
        float acc = 0.0;
        float cmdT = 0.008;
        float filterT = 0.0;
        float gain = 0.0;
        uint8_t flag = 0;
        int count = 500;
        float dt = 0.1;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, &j);
        if (ret == 0)
        {
            robot.ServoMoveStart();
            while (count)
            {
                robot.ServoJ(&j, &epos, acc, vel, cmdT, filterT, gain, cmdID);
                j.jPos[0] += dt;
                count -= 1;
                robot.WaitMs(cmdT * 1000);
            }
            robot.ServoMoveEnd();
        }
        else
        {
            printf("GetActualJointPosDegree errcode:%d\n", ret);
        }
        robot.CloseRPC();
        return 0;
    }

關節扭矩控制開始
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制開始
    * @return 錯誤碼
    */
    errno_t ServoJTStart();

關節扭矩控制
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制
    * @param  [in] torque j1~j6關節扭矩，單位Nm
    * @param  [in] interval 指令週期，單位s，範圍[0.001~0.008]
    * @param  [in] checkFlag 檢測策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同時限制
    * @param  [in] jPowerLimit 關節最大功率限制(W)
    * @param  [in] jVelLimit 關節最大速度(°/s)
    * @return  錯誤碼
    */
    errno_t ServoJT(float torque[], double interval);

關節扭矩控制結束
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 關節扭矩控制結束
    * @return 錯誤碼
    */
    errno_t ServoJTEnd();

關節扭矩控制代碼示例
+++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    int TestServoJT(void)
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
         robot.DragTeachSwitch(1);
         float torques[] = { 0, 0, 0, 0, 0, 0 };
         robot.GetJointTorques(1, torques);
         int count = 100;
         robot.ServoJTStart(); 
         int error = 0;
         while (count > 0)
         {
             error = robot.ServoJT(torques, 0.001);
             count = count - 1;
             robot.Sleep(1);
         }
         error = robot.ServoJTEnd();
         robot.DragTeachSwitch(0);
         robot.CloseRPC();
         return 0;
     }

具有超速保護的關節扭矩控制程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int ServoJTWithSafety(FRRobot* robot)
    {
        robot->ResetAllError();
        robot->Sleep(500);
        float torques[] = { 0, 0, 0, 0, 0, 0 };
        robot->GetJointTorques(1, torques);
        robot->ServoJTStart(); 
        ROBOT_STATE_PKG pkg = {};
        robot->DragTeachSwitch(1);
        int checkFlag = 3;
        //double jPowerLimit[6] = {1, 1, 1, 1, 1, 1}; 
        double jPowerLimit[6] = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 };
        double jVelLimit[6] = { 181, 80, 80, 80, 80, 80 };
        int count = 800000;
        int error = 0;
        while (count > 0)
        {
            torques[2] = torques[2] + 0.01;
            error = robot->ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit); 
            if (error != 0)
            {
                robot->ServoJTEnd();
            }
            printf("ServoJT rtn is %d\n", error);
            count = count - 1;
            robot->Sleep(1);
            robot->GetRobotRealTimeState(&pkg);
            printf("maincode %d, subcode %d\n", pkg.main_code, pkg.sub_code);
        }
        robot->DragTeachSwitch(0);
        error = robot->ServoJTEnd();  
        return 0;
    }

笛卡爾空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  笛卡爾空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基座標系)，1-增量運動(基座標系)，2-增量運動(工具座標系)
    * @param  [in]  desc_pos  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，默認爲0
    * @return  錯誤碼
    */
    errno_t  ServoCart(int mode, DescPose *desc_pose, float pos_gain[6], float acc, float vel, float cmdT, float filterT, float gain);

笛卡爾空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestServoCart(void)
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
         DescPose desc_pos_dt;
         memset(&desc_pos_dt, 0, sizeof(DescPose));
         desc_pos_dt.tran.z = -0.5;
         float pos_gain[6] = { 0.0,0.0,1.0,0.0,0.0,0.0 };
         int mode = 2;
         float vel = 0.0;
         float acc = 0.0;
         float cmdT = 0.008;
         float filterT = 0.0;
         float gain = 0.0;
         uint8_t flag = 0;
         int count = 100;
         robot.SetSpeed(20);
         while (count)
         {
             robot.ServoCart(mode, &desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
             count -= 1;
             robot.WaitMs(cmdT * 1000);
         }
         robot.CloseRPC();
         return 0;
     }

樣條運動開始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    errno_t  SplineStart();

關節空間樣條運動(自動正運動學計算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 關節空間樣條運動(自動正運動學計算)
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @return 錯誤碼
    */
    errno_t SplinePTP(JointPos* joint_pos, int tool, int user, float vel, float acc, float ovl);

樣條運動PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  關節空間樣條運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]   
    * @return  錯誤碼
    */
    errno_t  SplinePTP(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl);

樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    errno_t  SplineEnd();

樣條運動代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestSpline(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
         JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
         DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         printf("movej errcode:%d\n", err1);
         robot.SplineStart();
         robot.SplinePTP(&j1, &desc_pos1, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j2, &desc_pos2, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j3, &desc_pos3, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j4, &desc_pos4, tool, user, vel, acc, ovl);
         robot.SplineEnd();
         err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         printf("movej errcode:%d\n", err1);
         robot.SplineStart();
         robot.SplinePTP(&j1, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j2, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j3, tool, user, vel, acc, ovl);
         robot.SplinePTP(&j4, tool, user, vel, acc, ovl);
         robot.SplineEnd();
         robot.CloseRPC();
         return 0;
     }

新樣條運動開始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 新樣條運動開始
    * @param [in] type  0-圓弧過渡，1-給定點位爲路徑點
    * @param [in] averageTime 全局平均銜接時間(ms)(10 ~ )，默認2000
    * @return 錯誤碼
    */
    errno_t NewSplineStart(int type, int averageTime=2000);

新樣條指令點
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 新樣條指令點
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] desc_pos  目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm 
    * @param  [in] lastFlag 是否爲最後一個點，0-否，1-是
    * @return 錯誤碼
    */ 
    errno_t NewSplinePoint(JointPos *joint_pos, DescPose *desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新樣條指令點(自動逆運動學計算)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief 新樣條指令點(自動逆運動學計算)
    * @param [in] desc_pos  目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag 是否為最後一個點，0-否，1-是
    * @param [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼
    */
    errno_t NewSplinePoint(DescPose* desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag, int config = -1);

新樣條運動結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 新樣條運動結束
    * @return 錯誤碼
    */
    errno_t NewSplineEnd();

新樣條運動代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestNewSpline(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         JointPos j3(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
         JointPos j4(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
         JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose desc_pos3(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
         DescPose desc_pos4(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
         DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         int err1 = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         printf("movej errcode:%d\n", err1);
         robot.NewSplineStart(1, 2000);
         robot.NewSplinePoint(&j1, &desc_pos1, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&j2, &desc_pos2, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&j3, &desc_pos3, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&j4, &desc_pos4, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&j5, &desc_pos5, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplineEnd();
         err1 = robot.MoveJ(&j1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         printf("movej errcode:%d\n", err1);
         robot.NewSplineStart(1, 2000);
         robot.NewSplinePoint(&desc_pos1, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&desc_pos2, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&desc_pos3, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&desc_pos4, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplinePoint(&desc_pos5, tool, user, vel, acc, ovl, -1, 0);
         robot.NewSplineEnd();
         robot.CloseRPC();
         return 0;
     }

終止運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    errno_t  StopMotion();

暫停運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 暫停運動
    * @return 錯誤碼
    */
    errno_t PauseMotion(); 

恢復運動
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:
    
    /**
    * @brief 恢復運動
    * @return 錯誤碼
    */
    errno_t ResumeMotion();

運動暫停、恢復、停止代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestPause(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j5(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos5(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         rtn = robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         rtn = robot.MoveJ(&j5, &desc_pos5, tool, user, vel, acc, ovl, &epos, 1, flag, &offset_pos);
         robot.Sleep(1000);
         robot.PauseMotion();
         robot.Sleep(1000);
         robot.ResumeMotion();
         robot.Sleep(1000);
         robot.StopMotion();
         robot.Sleep(1000);
         robot.CloseRPC();
         return 0;
     }

點位整體偏移開始
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    errno_t  PointsOffsetEnable(int flag, DescPose *offset_pos);

點位整體偏移結束
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    errno_t  PointsOffsetDisable();

點位偏移代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestOffset(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         DescPose offset_pos1(0, 0, 50, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 100.0;
         float acc = 100.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.Sleep(1000);
         robot.PointsOffsetEnable(0, &offset_pos1);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.PointsOffsetDisable();
         robot.CloseRPC();
         return 0;
     }

控制箱AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飛拍開始
    * @param [in] AONum 控制箱AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
    * @return 錯誤碼
    */
    errno_t MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飛拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    errno_t MoveAOStop();
    
末端AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飛拍開始
    * @param [in] AONum 末端AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
    * @return 錯誤碼
    */
    errno_t MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飛拍停止
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0
   
.. code-block:: c++
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    errno_t MoveToolAOStop();

AO飛拍代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

     int TestMoveAO(void)
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
         JointPos j1(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos j2(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose desc_pos1(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose desc_pos2(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose offset_pos(0, 0, 0, 0, 0, 0);
         DescPose offset_pos1(0, 0, 50, 0, 0, 0);
         ExaxisPos epos(0, 0, 0, 0);
         int tool = 0;
         int user = 0;
         float vel = 20.0;
         float acc = 20.0;
         float ovl = 100.0;
         float blendT = -1.0;
         uint8_t flag = 0;
         robot.SetSpeed(20);
         robot.MoveAOStart(0, 100, 100, 20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveAOStop();
         robot.Sleep(1000);
         robot.MoveToolAOStart(0, 100, 100, 20);
         robot.MoveJ(&j1, &desc_pos1, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveJ(&j2, &desc_pos2, tool, user, vel, acc, ovl, &epos, blendT, flag, &offset_pos);
         robot.MoveToolAOStop();
         robot.CloseRPC();
         return 0;
     }

開始Ptp運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 開始Ptp運動FIR濾波
    * @param [in] maxAcc 最大加速度極值(deg/s2)
    * @param [in] maxJek 統一關節急動度極值(deg/s3)
    * @return 錯誤碼
    */
    errno_t PtpFIRPlanningStart(double maxAcc, double maxJek = 1000);

關閉Ptp運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 關閉Ptp運動FIR濾波
	* @return 錯誤碼
	*/
	errno_t PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 開始LIN、ARC運動FIR濾波
	* @param [in] maxAccLin 線加速度極值(mm/s2)
	* @param [in] maxAccDeg 角加速度極值(deg/s2)
	* @param [in] maxJerkLin 線加加速度極值(mm/s3)
	* @param [in] maxJerkDeg 角加加速度極值(deg/s3)
	* @return 錯誤碼
	*/
	errno_t LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

關閉LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. versionadded:: V3.7.7

.. code-block:: c++
    :linenos:

    /**
	* @brief 關閉LIN、ARC運動FIR濾波
	* @return 錯誤碼
	*/
	errno_t LinArcFIRPlanningEnd();

FIR濾波代碼示例
+++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

     int TestFIR(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos midjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         JointPos endjointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose middescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         DescPose enddescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.PtpFIRPlanningStart(1000, 1000);
         cout << "PtpFIRPlanningStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.PtpFIRPlanningEnd();
         cout << "PtpFIRPlanningEnd rtn is " << rtn << endl;
         robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
         cout << "LinArcFIRPlanningStart rtn is " << rtn << endl;
         robot.MoveL(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, -1, &exaxisPos, 0, 0, &offdese, 1, 1);
         robot.MoveC(&midjointPos, &middescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, &endjointPos, &enddescPose, 0, 0, 100, 100, &exaxisPos, 0, &offdese, 100, -1);
         robot.LinArcFIRPlanningEnd();
         cout << "LinArcFIRPlanningEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

加速度平滑開啓
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑開啓
    * @param [in] saveFlag 是否斷電保存
    * @return 錯誤碼
    */
    errno_t AccSmoothStart(bool saveFlag);

加速度平滑關閉
+++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.2.1-3.8.1

.. code-block:: c++
    :linenos:

    /**
    * @brief 加速度平滑關閉
    * @param [in] saveFlag 是否斷電保存
    * @return 錯誤碼
    */
    errno_t AccSmoothEnd(bool saveFlag);

加速度平滑代碼示例
+++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestAccSmooth(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.AccSmoothStart(0);
         cout << "AccSmoothStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.AccSmoothEnd(0);
         cout << "AccSmoothEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }


指定姿態速度開啓
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿態速度開啓
    * @param [in] ratio 姿態速度百分比[0-300]
    * @return 錯誤碼
    */
    errno_t AngularSpeedStart(int ratio);

指定姿態速度關閉
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief 指定姿態速度關閉
    * @return 錯誤碼
    */
    errno_t AngularSpeedEnd();

機器人指定姿態速度代碼示例
++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.AngularSpeedStart(50);
         cout << "AngularSpeedStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.AngularSpeedEnd();
         cout << "AngularSpeedEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }

開始奇異位姿保護
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 開始奇異位姿保護
	* @param [in] protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
	* @param [in] minShoulderPos 肩奇異調整範圍(mm), 默認100
	* @param [in] minElbowPos 肘奇異調整範圍(mm), 默認50
	* @param [in] minWristPos 腕奇異調整範圍(°), 默認10
	* @return 錯誤碼
	*/
	errno_t SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇異位姿保護
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

	/**
	* @brief 停止奇異位姿保護
	* @return 錯誤碼
	*/
	errno_t SingularAvoidEnd();

機器人奇異位姿保護代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAngularSpeed(void)
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
         JointPos startjointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
         JointPos endjointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
         DescPose startdescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
         DescPose enddescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
         ExaxisPos exaxisPos(0, 0, 0, 0);
         DescPose offdese(0, 0, 0, 0, 0, 0);
         rtn = robot.SingularAvoidStart(2, 10, 5, 5);
         cout << "SingularAvoidStart rtn is " << rtn << endl;
         robot.MoveJ(&startjointPos, &startdescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         robot.MoveJ(&endjointPos, &enddescPose, 0, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
         rtn = robot.SingularAvoidEnd();
         cout << "SingularAvoidEnd rtn is " << rtn << endl;
         robot.CloseRPC();
         return 0;
     }
    
清空運動指令隊列
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 清空運動指令隊列
    * @return 錯誤碼
    */
    errno_t MotionQueueClear();

移動到相貫線起始點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 移動到相貫線起始點
    * @param [in] mainPoint 主管6個示教點的笛卡爾位姿
    * @param [in] mainExaxisPos 主管6個示教點擴展軸位置
    * @param [in] piecePoint 支管6個示教點的笛卡爾位姿
    * @param [in] pieceExaxisPos 支管6個示教點擴展軸位置
    * @param [in] extAxisFlag 是否啟用擴展軸；0-不啟用；1-啟用
    * @param [in] exaxisPos 起點擴展軸位置
    * @param [in] tool 工具座標系編號
    * @param [in] wobj 工件座標系編號
    * @param [in] vel 速度百分比
    * @param [in] acc 加速度百分比
    * @param [in] ovl 速度縮放因子
    * @param [in] oacc 加速度縮放因子
    * @param [in] moveType 運動類型; 0-PTP；1-LIN
    * @param [in] moveDirection 運動方向；0-順時針；1-逆時針
    * @param [in] offset 偏移量
    * @return 錯誤碼
    */
    errno_t MoveToIntersectLineStart(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);
            
相貫線運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 相貫線運動
    * @param [in] mainPoint 主管6個示教點的笛卡爾位姿
    * @param [in] mainExaxisPos 主管6個示教點擴展軸位置
    * @param [in] piecePoint 支管6個示教點的笛卡爾位姿
    * @param [in] pieceExaxisPos 支管6個示教點擴展軸位置
    * @param [in] extAxisFlag 是否啟用擴展軸；0-不啟用；1-啟用
    * @param [in] exaxisPos 起點擴展軸位置
    * @param [in] tool 工具座標系編號
    * @param [in] wobj 工件座標系編號
    * @param [in] vel 速度百分比
    * @param [in] acc 加速度百分比
    * @param [in] ovl 速度縮放因子
    * @param [in] oacc 加速度縮放因子
    * @param [in] moveDirection 運動方向; 0-順時針；1-逆時針
    * @param [in] offset 偏移量
    * @return 錯誤碼
    */
    errno_t MoveIntersectLine(DescPose mainPoint[6], ExaxisPos mainExaxisPos[6], DescPose piecePoint[6], ExaxisPos pieceExaxisPos[6], int extAxisFlag, ExaxisPos exaxisPos[4], int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);
                
機器人相貫線運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    void TestIntersectLineMove()
    {
        ROBOT_STATE_PKG pkg = {};
        FRRobot robot;
        robot.LoggerInit();
        robot.SetLoggerLevel(3);
        int rtn = robot.RPC("192.168.58.2");
        if (rtn != 0)
        {
            return ;
        }
        robot.SetReConnectParam(true, 30000, 500);
        DescPose mainPoint[6] = {};
        DescPose piecePoint[6] = {};
        ExaxisPos mainExaxisPos[6] = {};
        ExaxisPos pieceExaxisPos[6] = {};
        int extAxisFlag = 1;
        ExaxisPos exaxisPos[4] = {};
        DescPose offset = { 0.0, 2.0 ,30.0, -2.0, 0.0, 0.0 };
        mainPoint[0] = {490.004, -383.194, 402.735, -9.332, -1.528, 69.594};
        mainPoint[1] = {444.950, -407.117, 389.011, -5.546, -2.196, 65.279};
        mainPoint[2] = {445.168, -463.605, 355.759, -1.544, -10.886, 57.104};
        mainPoint[3] = {507.529, -485.385, 343.013, -0.786, -4.834, 61.799};
        mainPoint[4] = {554.390, -442.647, 367.701, -4.761, -10.181, 64.925};
        mainPoint[5] = {532.552, -394.003, 396.467, -13.732, -13.592, 67.411};
        mainExaxisPos[0] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[1] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[2] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[3] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[4] = { -29.996, 0.000, 0.000, 0.000 };
        mainExaxisPos[5] = { -29.996, 0.000, 0.000, 0.000 };
        piecePoint[0] = { 505.571, -192.408, 316.759, 38.098, 37.051, 139.447 };
        piecePoint[1] = {533.837, -201.558, 332.340, 34.644, 42.339, 137.748};
        piecePoint[2] = {530.386, -225.085, 373.808, 35.431, 45.111, 137.560};
        piecePoint[3] = {485.646, -229.195, 383.778, 33.870, 45.173, 137.064};
        piecePoint[4] = {460.551, -212.161, 354.256, 28.856, 45.602, 135.930};
        piecePoint[5] = {474.217, -197.124, 324.611, 42.469, 41.133, 148.167};
        pieceExaxisPos[0] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[1] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[2] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[3] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[4] = { -29.996, -0.000, 0.000, 0.000 };
        pieceExaxisPos[5] = { -29.996, -0.000, 0.000, 0.000 };
        exaxisPos[0] = {-29.996, -0.000, 0.000, 0.000};
        exaxisPos[1] = {-44.994, 90.000, 0.000, 0.000};
        exaxisPos[2] = {-59.992, 0.002, 0.000, 0.000};
        exaxisPos[3] = {-44.994, -89.997, 0.000, 0.000};
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0; 
        int moveType = 1;
        int moveDirection = 1;
        rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return ;
    }