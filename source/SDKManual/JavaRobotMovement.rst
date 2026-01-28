機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief jog 點動 
    * @param [in] refType 0-關節點動，2-基座標系下點動，4-工具座標系下點動，8-工件座標系下點動
    * @param [in] nb 1-關節1(或x軸)，2-關節2(或y軸)，3-關節3(或z軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param [in] dir 0-負方向，1-正方向
    * @param [in] vel 速度百分比，[0~100]
    * @param [in] acc 加速度百分比， [0~100]
    * @param [in] max_dis 單次點動最大角度，單位[°]或距離，單位[mm]
    * @return 錯誤碼 
    */ 
    int StartJOG(int refType, int nb, int dir, double vel, double acc, double max_dis);

jog點動減速停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  jog點動減速停止
    * @param  [in]  stopType  1-關節點動停止，3-基座標系下點動停止，5-工具座標系下點動停止，9-工件座標系下點動停止
    * @return  錯誤碼
    */
    int StopJOG(int stopType);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    int ImmStopJOG(); 

機器人點動控制代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static  int TestJOG(Robot robot)
    {
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
        return 0;
    }

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos  目標笛卡爾位姿
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos);

關節空間運動(自動正運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /** 
    * @brief  關節空間運動(自動正運動學計算)
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return 錯誤碼 
    */ 
    int MoveJ(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl, ExaxisPos epos, double blendT, int offset_flag, DescPose offset_pos)

笛卡爾空間直線運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動 (重載函數1 增加 blendMode)
    * @param  joint_pos  目標關節位置, 單位 deg
    * @param  desc_pos   目標笛卡爾位姿
    * @param  tool  工具座標號，範圍 [1~15]
    * @param  user  工件座標號，範圍 [1~15]
    * @param  vel  速度百分比，範圍 [0~100]
    * @param  acc  加速度百分比，範圍 [0~100], 暫不開放
    * @param  ovl  速度縮放因子 [0~100] / 物理速度 (mm/s)
    * @param  blendR  [-1.0]-運動到位 (阻塞)，[0~1000.0]-平滑半徑 (非阻塞)，單位 mm
    * @param  blendMode  過渡方式；0-內切過渡；1-角點過渡
    * @param  epos  擴展軸位置，單位 mm
    * @param  search  0-不焊絲尋位，1-焊絲尋位
    * @param  offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  offset_pos  位姿偏移量
    * @param  oacc  加速度縮放因子 [0-100] / 物理加速度 (mm/s²)
    * @param  velAccParamMode  速度加速度參數模式；0-百分比；1-物理速度 (mm/s) 加速度 (mm/s²)
    * @param  overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認為 0
    * @param  speedPercent  允許降速閾值百分比 [0-100]，默認 10%
    * @return  錯誤碼
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, double oacc,int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡爾空間直線運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動(自動逆運動學計算)
    * @param [in] desc_pos   目標笛卡爾位姿
    * @param [in] tool  工具座標號，範圍[1~15]
    * @param [in] user  工件座標號，範圍[1~15]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] blendMode 過渡方式；0-內切過渡；1-角點過渡
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @param [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認爲0
    * @param [in] speedPercent  允許降速閾值百分比[0-100]，默認10%
    * @return  錯誤碼
    */
    int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int overSpeedStrategy, int speedPercent)

笛卡爾空間直線運動（增加速度加速度參數模式velAccParamMode參數）
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動（增加速度加速度參數模式velAccParamMode參數）
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[1~15]
    * @param  [in] user  工件座標號，範圍[1~15]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認爲0
    * @param  [in] speedPercent  允許降速閾值百分比[0-100]，默認10%
    * @return  錯誤碼
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡爾空間直線運動(重載函數1 增加blendMode)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動(重載函數1 增加blendMode)
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[1~15]
    * @param  [in] user  工件座標號，範圍[1~15]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] blendMode 過渡方式；0-內切過渡；1-角點過渡
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認爲0
    * @param  [in] speedPercent  允許降速閾值百分比[0-100]，默認10%
    * @return  錯誤碼
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡爾空間直線運動(重載函數2 不需要輸入關節位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間直線運動(重載函數2 不需要輸入關節位置)
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[1~15]
    * @param  [in] user  工件座標號，範圍[1~15]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] blendMode 過渡方式；0-內切過渡；1-角點過渡
    * @param  [in] epos  擴展軸位置，單位mm
    * @param  [in] search  0-不焊絲尋位，1-焊絲尋位
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param  [in] overSpeedStrategy  超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，默認爲0
    * @param  [in] speedPercent  允許降速閾值百分比[0-100]，默認10%
    * @return  錯誤碼
    */
    public int MoveL(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, int config, int velAccParamMode, int overSpeedStrategy, int speedPercent)

笛卡爾空間圓弧運動
+++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動
    * @param  joint_pos_p  路徑點關節位置, 單位 deg
    * @param  desc_pos_p   路徑點笛卡爾位姿
    * @param  ptool  工具座標號，範圍 [1~15]
    * @param  puser  工件座標號，範圍 [1~15]
    * @param  pvel  速度百分比，範圍 [0~100]
    * @param  pacc  加速度百分比，範圍 [0~100], 暫不開放
    * @param  epos_p  擴展軸位置，單位 mm
    * @param  poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  offset_pos_p  位姿偏移量
    * @param  joint_pos_t  目標點關節位置, 單位 deg
    * @param  desc_pos_t   目標點笛卡爾位姿
    * @param  ttool  工具座標號，範圍 [1~15]
    * @param  tuser  工件座標號，範圍 [1~15]
    * @param  tvel  速度百分比，範圍 [0~100]
    * @param  tacc  加速度百分比，範圍 [0~100], 暫不開放
    * @param  epos_t  擴展軸位置，單位 mm
    * @param  toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  offset_pos_t  位姿偏移量
    * @param  ovl  速度縮放因子 [0~100] / 物理速度 (mm/s)
    * @param  blendR [-1.0]-運動到位 (阻塞)，[0~1000.0]-平滑半徑 (非阻塞)，單位 mm
    * @param  oacc 加速度縮放因子 [0-100] / 物理加速度 (mm/s²)
    * @param  velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度 (mm/s) 加速度 (mm/s²)
    * @return  錯誤碼
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, double oacc, int velAccParamMode)

笛卡爾空間圓弧運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動(自動逆運動學計算)
    * @param [in] desc_pos_p   路徑點笛卡爾位姿
    * @param [in] ptool  工具座標號，範圍[1~15]
    * @param [in] puser  工件座標號，範圍[1~15]
    * @param [in] pvel  速度百分比，範圍[0~100]
    * @param [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p  擴展軸位置，單位mm
    * @param [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] desc_pos_t   目標點笛卡爾位姿
    * @param [in] ttool  工具座標號，範圍[1~15]
    * @param [in] tuser  工件座標號，範圍[1~15]
    * @param [in] tvel  速度百分比，範圍[0~100]
    * @param [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t  擴展軸位置，單位mm
    * @param [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos_t  位姿偏移量
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return  錯誤碼
    */
    int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config)

笛卡爾空間圓弧運動(增加速度加速度參數模式velAccParamMode參數)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動(增加速度加速度參數模式velAccParamMode參數)
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[1~15]
    * @param  [in] puser  工件座標號，範圍[1~15]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[1~15]
    * @param  [in] tuser  工件座標號，範圍[1~15]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  錯誤碼
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int velAccParamMode)

笛卡爾空間圓弧運動(重載函數1 不需要輸入關節位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動 (重載函數1 不需要輸入關節位置)
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[1~15]
    * @param  [in] puser  工件座標號，範圍[1~15]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[1~15]
    * @param  [in] tuser  工件座標號，範圍[1~15]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_t  位姿偏移量
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  錯誤碼
    */
    public int MoveC(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, double ovl, double blendR, int config, int velAccParamMode)

笛卡爾空間整圓運動
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間整圓運動
    * @param  joint_pos_p  路徑點1關節位置, 單位 deg
    * @param  desc_pos_p   路徑點1笛卡爾位姿
    * @param  ptool  工具座標號，範圍 [1~15]
    * @param  puser  工件座標號，範圍 [1~15]
    * @param  pvel  速度百分比，範圍 [0~100]
    * @param  pacc  加速度百分比，範圍 [0~100], 暫不開放
    * @param  epos_p  擴展軸位置，單位 mm
    * @param  joint_pos_t  路徑點2關節位置, 單位 deg
    * @param  desc_pos_t   路徑點2笛卡爾位姿
    * @param  ttool  工具座標號，範圍 [1~15]
    * @param  tuser  工件座標號，範圍 [1~15]
    * @param  tvel  速度百分比，範圍 [0~100]
    * @param  tacc  加速度百分比，範圍 [0~100], 暫不開放
    * @param  epos_t  擴展軸位置，單位 mm
    * @param  ovl  速度縮放因子 [0~100] / 物理速度 (mm/s)
    * @param  offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  offset_pos  位姿偏移量
    * @param  oacc 加速度縮放因子 [0-100] / 物理加速度 (mm/s²)
    * @param  blendR -1：阻塞；0~1000：平滑半徑
    * @param  velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度 (mm/s) 加速度 (mm/s²)
    * @return  錯誤碼
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

笛卡爾空間整圓運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
     * @brief  笛卡爾空間整圓運動(自動逆運動學計算)
     * @param  [in] desc_pos_p   路徑點1笛卡爾位姿
     * @param  [in] ptool  工具座標號，範圍[0~14]
     * @param  [in] puser  工件座標號，範圍[0~14]
     * @param  [in] pvel  速度百分比，範圍[0~100]
     * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
     * @param  [in] epos_p  擴展軸位置，單位mm
     * @param  [in] desc_pos_t   路徑點2笛卡爾位姿
     * @param  [in] ttool  工具座標號，範圍[0~14]
     * @param  [in] tuser  工件座標號，範圍[0~14]
     * @param  [in] tvel  速度百分比，範圍[0~100]
     * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
     * @param  [in] epos_t  擴展軸位置，單位mm
     * @param  [in] ovl  速度縮放因子，範圍[0~100]
     * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
     * @param  [in] offset_pos  位姿偏移量
     * @param  [in] oacc 加速度百分比
     * @param  [in] blendR -1：阻塞；0~1000：平滑半徑
     * @param  [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
     * @return  錯誤碼
     */
    int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR,int config)

笛卡爾空間整圓運動（增加速度加速度參數模式velAccParamMode參數）
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    *@brief  笛卡爾空間整圓運動（增加速度加速度參數模式velAccParamMode參數）
    *@param  [in] joint_pos_p  路徑點1關節位置,單位deg
    *@param  [in] desc_pos_p   路徑點1笛卡爾位姿
    *@param  [in] ptool  工具座標號，範圍[1~15]
    *@param  [in] puser  工件座標號，範圍[1~15]
    *@param  [in] pvel  速度百分比，範圍[0~100]
    *@param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    *@param  [in] epos_p  擴展軸位置，單位mm
    *@param  [in] joint_pos_t  路徑點2關節位置,單位deg
    *@param  [in] desc_pos_t   路徑點2笛卡爾位姿
    *@param  [in] ttool  工具座標號，範圍[1~15]
    *@param  [in] tuser  工件座標號，範圍[1~15]
    *@param  [in] tvel  速度百分比，範圍[0~100]
    *@param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    *@param  [in] epos_t  擴展軸位置，單位mm
    *@param  [in] ovl  速度縮放因子，範圍[0~100]
    *@param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    *@param  [in] offset_pos  位姿偏移量
    *@param  [in] oacc 加速度百分比
    *@param  [in] blendR -1：阻塞；0~1000：平滑半徑
    *@param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    *@return  錯誤碼
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

笛卡爾空間整圓運動 (重載函數1 不需要輸入關節位置)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間整圓運動 (重載函數1 不需要輸入關節位置)
    * @param  [in] desc_pos_p   路徑點1笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] desc_pos_t   路徑點2笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] oacc 加速度百分比
    * @param  [in] blendR -1：阻塞；0~1000：平滑半徑
    * @param  [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  錯誤碼
    */
    public int Circle(DescPose desc_pos_p, int ptool, int puser, double pvel, double pacc, ExaxisPos epos_p, DescPose desc_pos_t, int ttool, int tuser, double tvel, double tacc, ExaxisPos epos_t, double ovl, int offset_flag, DescPose offset_pos, double oacc, double blendR, int config, int velAccParamMode)

笛卡爾空間點到點運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 笛卡爾空間點到點運動 
    * @param [in] desc_pos  目標笛卡爾位姿或位姿增量
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] config  關節空間配置，[-1]-參考當前關節位置解算，[0~7]-參考特定關節空間配置解算，默認爲-1
    * @return 錯誤碼 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendT, int config);

機器人基本運動指令代碼示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMove(Robot robot)
    {
        int rtn=-1;
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);
        JointPos j4=new JointPos(-31.154, -95.317, 94.276, -88.079, -89.740, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);
        DescPose desc_pos4=new DescPose(-443.165, 147.881, 480.951, 179.511, -0.775, -15.409);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double oacc = 100.0;
        double blendT = 0.0;
        double blendR = 0.0;
        int flag = 0;
        int search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos, j1, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        System.out.printf("MoveCart errcode:%d\n", rtn);
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode,0,10);
        System.out.printf("movel errcode:%d\n", rtn);
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, -1, velAccMode);
        System.out.printf("movec errcode:%d\n", rtn);
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.printf("movej errcode:%d\n", rtn);
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos, ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        System.out.printf("circle errcode:%d\n", rtn);
        return 0;
    }

笛卡爾空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡爾空間螺旋線運動 
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡爾位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 錯誤碼 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param);

笛卡爾空間螺旋線運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡爾空間螺旋線運動 (自動逆運動學計算)
    * @param [in] desc_pos   目標笛卡爾位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos  位姿偏移量
    * @param [in] spiral_param  螺旋參數
    * @param [in] config  逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return 錯誤碼 
    */
    int NewSpiral(DescPose desc_pos, int tool, int user, double vel, double acc, ExaxisPos epos, double ovl, int offset_flag, DescPose offset_pos, SpiralParam spiral_param,int config)

螺旋線運動代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpiral(Robot robot)
    {
        int rtn=-1;
        JointPos j=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose offset_pos1=new DescPose(50, 0, 0, -30, 0, 0);
        DescPose offset_pos2=new DescPose(50, 0, 0, -5, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);
        SpiralParam sp=new SpiralParam(1,5.0,50.0,10.0,10.0,0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = 0.0;
        int flag = 2;

        rtn = robot.MoveJ(j, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos1);
        System.out.println("movej errcode:"+ rtn);

        rtn = robot.NewSpiral(desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp,-1);
        System.out.println("newspiral errcode:"+ rtn);

        return 0;
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveStart();

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
    * @return 錯誤碼 
    */ 
    int ServoMoveEnd();

關節空間伺服模式運動
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.6-3.8.3

.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] axisPos  外部軸位置,單位mm
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，默認爲0
    * @param  [in] id  servoJ指令ID,默認爲0
    * @return  錯誤碼
    */
    int ServoJ(JointPos joint_pos, ExaxisPos axisPos, double acc, double vel, double cmdT, double filterT, double gain, int id);

關節空間伺服模式運動示例程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestServoJ()
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//設置重連次數、間隔
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
        JointPos j5 = new JointPos();
        ExaxisPos ePos=new ExaxisPos();
        int ret = robot.GetActualJointPosDegree(j5);
        if (ret == 0)
        {
            int count = 200;
            while (count > 0)
            {
                robot.ServoJ(j5, ePos,100, 100, 0.008, 0, 0);
                j5.J1 += 0.2;//1關節位置增加
                count -= 1;
                robot.WaitMs((int)(8));
            }
        }
    }

關節扭矩控制開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節扭矩控制開始
    * @return  錯誤碼
    */
    int ServoJTStart()

關節扭矩控制
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關節扭矩控制
    * @param torque j1~j6關節扭矩，單位Nm
    * @param interval 指令週期，單位s，範圍[0.001~0.008]
    * @param checkFlag 檢測策略
    *                  0-不限制；
    *                  1-限制功率；
    *                  2-限制速度；
    *                  3-功率和速度同時限制
    * @param jPowerLimit 各關節最大功率限制(W)
    * @param jVelLimit 各關節最大速度(°/s)
    * @return 錯誤碼
    */
    public int ServoJT(double[] torque, double interval, int checkFlag, double[] jPowerLimit, double[] jVelLimit)

關節扭矩控制結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  關節扭矩控制結束
    * @return  錯誤碼
    */
    int ServoJTEnd()

關節空間伺服模式運動示例程序
+++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoJT(Robot robot)
    {

        robot.DragTeachSwitch(1);
        List<Number> joint_toq=new ArrayList<>();
        joint_toq=robot.GetJointTorques(1);

        int count = 100;
        robot.ServoJTStart(); //   #servoJT開始
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
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void ServoJTWithSafety(Robot robot)
    {
        robot.ResetAllError();
        robot.Sleep(500);
        List<Number> torques;
        torques = robot.GetJointTorques(1);
        robot.ServoJTStart(); // 開始servoJT
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
        robot.DragTeachSwitch(1);
        int checkFlag = 3; // -1,3 - 功率和速度同時限制
        // double[] jPowerLimit = {1.0,1.0,1.0,1.0,1.0,1.0}; // 5001
        double[] jPowerLimit = { 10.0, 10.0, 10.0, 10.0, 10.0, 10.0 }; // 各關節功率限制(W)
        double[] jVelLimit = { 50, 50, 50, 50, 50, 50 }; // 180.1,-1 - 各關節速度限制(°/s)
        int count = 800000;
        int error = 0;
        double[] tor = new double[]{(double)torques.get(1), (double)torques.get(2), (double)torques.get(3),
                                   (double)torques.get(4), (double)torques.get(5), (double)torques.get(6)};
        while (count > 0)
        {
            tor[2] = tor[2] + 0.01; // 每次1軸增加0.01NM，運動100次
            error = robot.ServoJT(tor, 0.01, checkFlag, jPowerLimit, jVelLimit);  // 關節空間伺服模式運動
            System.out.printf("ServoJT 返回值為 %d\n", error);
            count = count - 1;
            robot.Sleep(1);
            pkg = robot.GetRobotRealTimeState();
            System.out.printf("主代碼 %d, 子代碼 %d\n", pkg.main_code, pkg.sub_code);
        }
        robot.DragTeachSwitch(0);
        error = robot.ServoJTEnd();  // 伺服運動結束
    }

笛卡爾空間伺服模式運動
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  笛卡爾空間伺服模式運動
    * @param  [in]  mode  0-絕對運動(基座標系)，1-增量運動(基座標系)，2-增量運動(工具座標系)
    * @param  [in]  desc_pose  目標笛卡爾位姿或位姿增量
    * @param  [in]  pos_gain  位姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param  [in]  acc  加速度百分比，範圍[0~100],暫不開放，默認爲0
    * @param  [in]  vel  速度百分比，範圍[0~100]，暫不開放，默認爲0
    * @param  [in]  cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in]  filterT 濾波時間，單位s，暫不開放，默認爲0
    * @param  [in]  gain  目標位置的比例放大器，暫不開放，默認爲0
    * @return  錯誤碼
    */
    int ServoCart(int mode, DescPose desc_pose, Object[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain);

笛卡爾空間伺服模式運動代碼示例
+++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestServoCart(Robot robot)
    {
        DescPose desc_pos_dt=new DescPose(0,0,0,0,0,0);

        desc_pos_dt.tran.z = -0.5;
        Object[] pos_gain = { 0.0,0.0,1.0,0.0,0.0,0.0 };
        int mode = 2;
        double vel = 0.0;
        double acc = 0.0;
        double cmdT = 0.008;
        double filterT = 0.0;
        double gain = 0.0;
        int flag = 0;
        int count = 100;

        robot.SetSpeed(20);

        while (count>0)
        {
            robot.ServoCart(mode, desc_pos_dt, pos_gain, acc, vel, cmdT, filterT, gain);
            count -= 1;
            double time=cmdT*1000;
            robot.WaitMs((int)time);
        }

        return 0;
    }

樣條運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    int SplineStart();

關節運動PTP
+++++++++++++++++++++++++++++
.. code-block:: Java
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl);

關節空間樣條運動 (自動正運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief  關節空間樣條運動 (自動正運動學計算)
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @return  錯誤碼
    */
    int SplinePTP(JointPos joint_pos, int tool, int user, double vel, double acc, double ovl)

樣條運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    int SplineEnd(); 

樣條運動代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestSpline(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3=new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4=new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:"+ err1);
        robot.SplineStart();
        robot.SplinePTP(j1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
        return 0;
    }

新樣條運動開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @param [in] type   0-圓弧過渡，1-給定點位爲路徑點
    * @param [in] averageTime  全局平均銜接時間(ms)(10 ~  )，默認2000
    * @return 錯誤碼 
    */ 
    int NewSplineStart(int type, int averageTime);
    
新樣條指令點
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 增加樣條運動指令點 
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡爾位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag 是否爲最後一個點，0-否，1-是
    * @return 錯誤碼 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag);

新樣條指令點(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.8-3.8.5

.. code-block:: Java
    :linenos:

    /**
    * @brief 新樣條指令點(自動逆運動學計算)
    * @param  [in] desc_pos   目標笛卡爾位姿
    * @param  [in] tool  工具座標號，範圍[0~14]
    * @param  [in] user  工件座標號，範圍[0~14]
    * @param  [in] vel  速度百分比，範圍[0~100]
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] ovl  速度縮放因子，範圍[0~100]
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param  [in] lastFlag 是否爲最後一個點，0-否，1-是
    * @param  [in] config 逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解
    * @return  錯誤碼
    */
    int NewSplinePoint(DescPose desc_pos, int tool, int user, double vel, double acc, double ovl, double blendR, int lastFlag,int config)

新樣條運動結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @return 錯誤碼 
    */ 
    int NewSplineEnd();
    
新樣條運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestNewSpline(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3=new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4=new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5=new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);


        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;


        int err1 = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        System.out.println("movej errcode:"+ err1);
        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(desc_pos1, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos2, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos3, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos4, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplinePoint(desc_pos5, tool, user, vel, acc, ovl, -1, 0,-1);
        robot.NewSplineEnd();
        return 0;
    }

終止運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    int StopMotion();

暫停運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:
    
    /** 
      * @brief 暫停運動 
      * @return 錯誤碼 
    */  
    int PauseMotion();

恢復運動
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 恢復運動 
    * @return 錯誤碼 
    */ 
    int ResumeMotion();

運動暫停、恢復、停止代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestPause(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5=new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5=new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);
        int rtn=-1;
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        robot.Sleep(1000);
        robot.PauseMotion();

        robot.Sleep(1000);
        robot.ResumeMotion();

        robot.Sleep(1000);
        robot.StopMotion();

        robot.Sleep(1000);

        return 0;
    }

點位整體偏移開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in]  offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


點位整體偏移結束
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    int PointsOffsetDisable(); 

點位偏移代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestOffset(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1=new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.Sleep(1000);
        robot.PointsOffsetEnable(0, offset_pos1);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.PointsOffsetDisable();

        return 0;
    }

控制箱AO飛拍開始
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飛拍開始
    * @param [in] AONum 控制箱AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
    * @return 錯誤碼
    */
    int MoveAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);

控制箱AO飛拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    int MoveAOStop();
    
末端AO飛拍開始
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飛拍開始
    * @param [in] AONum 末端AO編號
    * @param [in] maxTCPSpeed 最大TCP速度值[1-5000mm/s]，默認1000
    * @param [in] maxAOPercent 最大TCP速度值對應的AO百分比，默認100%
    * @param [in] zeroZoneCmp 死區補償值AO百分比，整形，默認爲20%，範圍[0-100]
    * @return 錯誤碼
    */
    int MoveToolAOStart(int AONum, int maxTCPSpeed, int maxAOPercent, int zeroZoneCmp);
    
末端AO飛拍停止
+++++++++++++++++++++++++++++   
.. code-block:: Java
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    int MoveToolAOStop();

AO飛拍代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestMoveAO(Robot robot)
    {
        JointPos j1=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose desc_pos1=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        DescPose offset_pos=new DescPose(0, 0, 0, 0, 0, 0);
        DescPose offset_pos1=new DescPose(0, 0, 50, 0, 0, 0);
        ExaxisPos epos=new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        double vel = 20.0;
        double acc = 20.0;
        double ovl = 100.0;
        double blendT = -1.0;
        int flag = 0;

        robot.SetSpeed(20);

        robot.MoveAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.Sleep(1000);

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();

        return 0;
    }

開始Ptp運動FIR濾波
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.5-3.8.2

.. code-block:: Java
    :linenos:

    /**
    * @brief 開始Ptp運動FIR濾波
    * @param [in] maxAcc 最大加速度極值(deg/s2)
    * @param [in] maxJek 統一關節急動度極值(deg/s3)
    * @return 錯誤碼
    */
    int PtpFIRPlanningStart(double maxAcc,double maxJek);

關閉Ptp運動FIR濾波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關閉Ptp運動FIR濾波
    * @return 錯誤碼
    */
    int PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 開始LIN、ARC運動FIR濾波
    * @param [in] maxAccLin 線加速度極值(mm/s2)
    * @param [in] maxAccDeg 角加速度極值(deg/s2)
    * @param [in] maxJerkLin 線加加速度極值(mm/s3)
    * @param [in] maxJerkDeg 角加加速度極值(deg/s3)
    * @return 錯誤碼
    */
    int LinArcFIRPlanningStart(double maxAccLin, double maxAccDeg, double maxJerkLin, double maxJerkDeg);

關閉LIN、ARC運動FIR濾波
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 關閉LIN、ARC運動FIR濾波
    * @return 錯誤碼
    */
    int LinArcFIRPlanningEnd();

FIR濾波代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestFIR(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos midjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos endjointPos=new JointPos(-29.777, -84.536, 109.275, -114.075, -86.655, 74.257);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose middescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose enddescPose=new DescPose(-487.434, 154.362, 308.576, 176.600, 0.268, -14.061);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);

        int rtn = robot.PtpFIRPlanningStart(1000, 1000);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.PtpFIRPlanningEnd();

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        robot.MoveL(startjointPos, startdescPose, 0, 0, 100, 100, 100, -1, 0,exaxisPos, 0, 0, offdese, 1, 1);
        robot.MoveC(midjointPos, middescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1);
        robot.LinArcFIRPlanningEnd();
        return 0;
    }

加速度平滑開啓
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief 加速度平滑開啓
     * @param [in] saveFlag 是否斷電保存
     * @return  錯誤碼
     */
    public int AccSmoothStart(boolean saveFlag)

加速度平滑關閉
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.4-3.8.1
.. code-block:: Java
    :linenos:

    /**
     * @brief 加速度平滑關閉
     * @param [in] saveFlag 是否斷電保存
     * @return  錯誤碼
     */
    public int AccSmoothEnd(boolean saveFlag)

加速度平滑代碼示例
+++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAccSmooth(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0,0,0,0,0,0);
        int rtn = robot.AccSmoothStart(false);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AccSmoothEnd(false);

        robot.CloseRPC();
        return 0;
    }

指定姿態速度開啓
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 指定姿態速度開啓
     * @param [in] ratio 姿態速度百分比[0-300]
     * @return  錯誤碼
     */
    int AngularSpeedStart(int ratio)

指定姿態速度關閉
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 指定姿態速度關閉
     * @return  錯誤碼
     */
    int AngularSpeedEnd();

機器人指定姿態速度代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

開始奇異位姿保護
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  開始奇異位姿保護
    * @param  [in]  protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
    * @param  [in]  minShoulderPos 肩奇異調整範圍(mm), 默認100
    * @param  [in]  minElbowPos 肘奇異調整範圍(mm), 默認50
    * @param  [in]  minWristPos 腕奇異調整範圍(°), 默認10
    * @return  錯誤碼
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇異位姿保護
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  停止奇異位姿保護
    * @return  錯誤碼
    */
    int SingularAvoidEnd();

機器人奇異位姿保護代碼示例
++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static int TestAngularSpeed(Robot robot)
    {
        JointPos startjointPos=new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos endjointPos=new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        DescPose startdescPose=new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose enddescPose=new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        ExaxisPos exaxisPos=new ExaxisPos(0, 0, 0, 0);
        DescPose offdese=new DescPose(0, 0, 0, 0, 0, 0);
        int rtn = robot.AngularSpeedStart(50);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        rtn = robot.AngularSpeedEnd();

        return 0;
    }

清空運動指令隊列
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 清空運動指令隊列
    * @return 錯誤碼
    */
    public int MotionQueueClear()


移動到相貫線起始點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveToIntersectLineStart(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveType, int moveDirection, DescPose offset);
            
相貫線運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
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
    public int MoveIntersectLine(DescPose[] mainPoint, ExaxisPos[] mainExaxisPos, DescPose[] piecePoint, ExaxisPos[] pieceExaxisPos, int extAxisFlag, ExaxisPos[] exaxisPos, int tool, int wobj, double vel, double acc, double ovl, double oacc, int moveDirection, DescPose offset);
                
機器人相貫線運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void TestIntersectLineMove(Robot robot)
    {
        DescPose[] mainPoint = new DescPose[6];
        DescPose[] piecePoint = new DescPose[6];
        ExaxisPos[] mainExaxisPos = new ExaxisPos[6];
        ExaxisPos[] pieceExaxisPos = new ExaxisPos[6];
        int extAxisFlag = 1;
        ExaxisPos[] exaxisPos = new ExaxisPos[4];
        DescPose offset =new DescPose(0.0, 2.0 ,30.0, -2.0, 0.0, 0.0 );
        mainPoint[0] = new DescPose(490.004, -383.194, 402.735, -9.332, -1.528, 69.594);
        mainPoint[1] = new DescPose(444.950, -407.117, 389.011, -5.546, -2.196, 65.279);
        mainPoint[2] = new DescPose(445.168, -463.605, 355.759, -1.544, -10.886, 57.104);
        mainPoint[3] = new DescPose(507.529, -485.385, 343.013, -0.786, -4.834, 61.799);
        mainPoint[4] = new DescPose(554.390, -442.647, 367.701, -4.761, -10.181, 64.925);
        mainPoint[5] = new DescPose(532.552, -394.003, 396.467, -13.732, -13.592, 67.411);
        mainExaxisPos[0] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[1] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[2] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[3] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[4] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        mainExaxisPos[5] = new ExaxisPos(-29.996, 0.000, 0.000, 0.000 );
        piecePoint[0] = new DescPose( 505.571, -192.408, 316.759, 38.098, 37.051, 139.447);
        piecePoint[1] =new DescPose(533.837, -201.558, 332.340, 34.644, 42.339, 137.748);
        piecePoint[2] =new DescPose(530.386, -225.085, 373.808, 35.431, 45.111, 137.560);
        piecePoint[3] =new DescPose(485.646, -229.195, 383.778, 33.870, 45.173, 137.064);
        piecePoint[4] =new DescPose(460.551, -212.161, 354.256, 28.856, 45.602, 135.930);
        piecePoint[5] =new DescPose(474.217, -197.124, 324.611, 42.469, 41.133, 148.167);
        pieceExaxisPos[0] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[1] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[2] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[3] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[4] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        pieceExaxisPos[5] = new ExaxisPos( -29.996, -0.000, 0.000, 0.000);
        exaxisPos[0] = new ExaxisPos(-29.996, -0.000, 0.000, 0.000);
        exaxisPos[1] = new ExaxisPos(-44.994, 90.000, 0.000, 0.000);
        exaxisPos[2] = new ExaxisPos(-59.992, 0.002, 0.000, 0.000);
        exaxisPos[3] = new ExaxisPos(-44.994, -89.997, 0.000, 0.000);
        int tool = 2;
        int wobj = 0;
        double vel = 100.0;
        double acc = 100.0;
        double ovl = 12.0;
        double oacc = 12.0;
        int moveType = 1;
        int moveDirection = 1;
        int  rtn = robot.MoveToIntersectLineStart(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos[0], tool, wobj, vel, acc, ovl, oacc, moveType, moveDirection, offset);
        System.out.printf("MoveToIntersectLineStart rtn is %d\n", rtn);
        rtn = robot.MoveIntersectLine(mainPoint, mainExaxisPos, piecePoint, pieceExaxisPos, extAxisFlag, exaxisPos, tool, wobj, vel, acc, 5.0, 5.0, moveDirection, offset);
        System.out.printf("MoveIntersectLine rtn is %d\n", rtn);
        robot.CloseRPC();
        return ;
    }
 
原地空運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 原地空運動
    * @return 錯誤碼
    */
    public int MoveStationary()

原地空運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void test_RecordandReplay(Robot robot)
    {
        int rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 1, 10, 100);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        rtn = robot.MoveStationary();
        System.out.printf("MoveStationary rtn is %d\n", rtn);
        rtn = robot.LaserSensorRecord1(0, 10);
        System.out.printf("LaserSensorRecordandReplay rtn is %d\n", rtn);
        robot.CloseRPC();
        robot.Sleep(9999999);
    }