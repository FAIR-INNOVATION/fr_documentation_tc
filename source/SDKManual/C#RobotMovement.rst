機器人運動
============

.. toctree:: 
    :maxdepth: 5


jog點動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief jog 點動 
    * @param [in] refType 點動類型：0-關節點動，2-基座標系下點動，4-工具座標系下點動，8-工件座標系下點動 
    * @param [in] nb 1-關節 1(或 x 軸)，2-關節 2(或 y 軸)，3-關節 3(或 z 軸)，4-關節4(或繞x軸旋轉)，5-關節5(或繞y軸旋轉)，6-關節6(或繞z軸旋轉)
    * @param [in] dir 0-負方向，1-正方向 
    * @param [in] vel 速度百分比，[0~100] 
    * @param [in] acc 加速度百分比， [0~100] 
    * @param [in] max_dis 單次點動最大角度，單位[°]或距離，單位[mm] 
    * @return 錯誤碼 
    */ 
    int StartJOG(byte refType, byte nb, byte dir, float vel, float acc, float max_dis);

jog點動減速停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  jog點動減速停止
    * @param  [in]  ref  1-關節點動停止，3-基座標系下點動停止，5-工具座標系下點動停止，9-工件座標系下點動停止
    * @return  錯誤碼
    */
    int StopJOG(byte stopType);

jog點動立即停止
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief jog點動立即停止
    * @return  錯誤碼
    */
    int ImmStopJOG(); 

機器人點動控制代碼示例
++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnJOG_Click(object sender, EventArgs e)
    {
        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(0, i + 1, 0, 20.0f, 20.0f, 30.0f);
            Thread.Sleep(1000);
            robot.ImmStopJOG();
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(2, i + 1, 0, 20.0f, 20.0f, 30.0f);
            Thread.Sleep(1000);
            robot.ImmStopJOG();
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(4, i + 1, 0, 20.0f, 20.0f, 30.0f);
            Thread.Sleep(1000);
            robot.StopJOG(5);
            Thread.Sleep(1000);
        }

        for (int i = 0; i < 6; i++)
        {
            robot.StartJOG(8, i + 1, 0, 20.0f, 20.0f, 30.0f);
            Thread.Sleep(1000);
            robot.StopJOG(9);
            Thread.Sleep(1000);
        }
    }

關節空間運動
+++++++++++++++++++++++++++++
.. code-block:: c#
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
    int MoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos); 

關節空間運動(自動正運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間直線運動
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] desc_pos 目標笛卡爾位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子[0~100]/物理速度(mm/s)
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] blendMode 過渡方式；0-內切過渡；1-角點過渡
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] search 0-不焊絲尋位，1-焊絲尋位
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param [in] offset_pos 位姿偏移量
    * @param [in] oacc 加速度縮放因子[0-100]/物理加速度(mm/s2)
    * @param [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @param [in] overSpeedStrategy 超速處理策略，1-標準；2-超速時報錯停止；3-自適應降速，預設為0
    * @param [in] speedPercent 允許降速閾值百分比[0-100]，預設10%
    * @return 錯誤碼
    */
    public int MoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int blendMode, ExaxisPos epos, int search, int offset_flag, DescPose offset_pos, float oacc, int velAccParamMode, int overSpeedStrategy = 0, int speedPercent = 10)

笛卡爾空間直線運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間圓弧運動
    * @param  [in] joint_pos_p  路徑點關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] poffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_p  位姿偏移量
    * @param  [in] joint_pos_t  目標點關節位置,單位deg
    * @param  [in] desc_pos_t   目標點笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] toffset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos_t  位姿偏移量   
    * @param  [in] ovl  速度縮放因子，範圍[0~100]    
    * @param  [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm    
    * @param  [in] oacc 加速度縮放因子[0-100]/物理加速度(mm/s2)
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  錯誤碼
    */
    public int MoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc,ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p,JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc,ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t,float ovl, float blendR, float oacc, int velAccParamMode)

笛卡爾空間圓弧運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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

笛卡爾空間點到點運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 笛卡爾空間點到點運動 
    * @param [in] desc_pos 基座標系下目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位 ms 
    * @param [in] config 關節空間配置，[-1]-參考當前關節位置解算，[0~7]-參考特定關節空間配置解算，默認爲-1 
    * @return 錯誤碼 
    */ 
    int MoveCart(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendT, int config);

笛卡爾空間整圓運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  笛卡爾空間整圓運動
    * @param  [in] joint_pos_p  路徑點1關節位置,單位deg
    * @param  [in] desc_pos_p   路徑點1笛卡爾位姿
    * @param  [in] ptool  工具座標號，範圍[0~14]
    * @param  [in] puser  工件座標號，範圍[0~14]
    * @param  [in] pvel  速度百分比，範圍[0~100]
    * @param  [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_p  擴展軸位置，單位mm
    * @param  [in] joint_pos_t  路徑點2關節位置,單位deg
    * @param  [in] desc_pos_t   路徑點2笛卡爾位姿
    * @param  [in] ttool  工具座標號，範圍[0~14]
    * @param  [in] tuser  工件座標號，範圍[0~14]
    * @param  [in] tvel  速度百分比，範圍[0~100]
    * @param  [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param  [in] epos_t  擴展軸位置，單位mm
    * @param  [in] ovl  速度縮放因子[0~100]/物理速度(mm/s)
    * @param  [in] offset_flag  0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @param  [in] oacc 加速度縮放因子[0-100]/物理加速度(mm/s2)
    * @param  [in] blendR -1：阻塞；0~1000：平滑半徑
    * @param  [in] velAccParamMode 速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2)
    * @return  錯誤碼
    */
    public int Circle(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc,ExaxisPos epos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser,float tvel, float tacc, ExaxisPos epos_t, float ovl, int offset_flag,DescPose offset_pos, double oacc, double blendR, int velAccParamMode)

笛卡爾空間整圓運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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

機器人基本運動指令代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
    :linenos:

    public void TestMove()
        int rtn;
        JointPos j1 = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos j2 = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos j3 = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);
        JointPos j4 = new JointPos(-31.154f, -95.317f, 94.276f, -88.079f, -89.740f, 74.256f);
        DescPose desc_pos1 = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose desc_pos2 = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose desc_pos3 = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);
        DescPose desc_pos4 = new DescPose(-443.165f, 147.881f, 480.951f, 179.511f, -0.775f, -15.409f);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float oacc = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;
        int blendMode = 0;
        int velAccMode = 0;
        robot.SetSpeed(20);
        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(j2, desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, oacc, velAccMode,0,10);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(j3, desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,j4, desc_pos4, tool, user, vel, acc, epos, flag, offset_pos, ovl, blendR, oacc, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(j3, desc_pos3, tool, user, vel, acc, epos,j1, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
        rtn = robot.MoveCart(desc_pos4, tool, user, vel, acc, ovl, blendT, -1);
        Console.WriteLine($"MoveCart errcode:{rtn}");
        rtn = robot.MoveJ(j1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.MoveL(desc_pos2, tool, user, vel, acc, ovl, blendR, blendMode, epos, search, flag, offset_pos, -1, velAccMode);
        Console.WriteLine($"movel errcode:{rtn}");
        rtn = robot.MoveC(desc_pos3, tool, user, vel, acc, epos, flag, offset_pos,desc_pos4, tool, user, vel, acc, epos, flag, offset_pos,ovl, blendR, -1, velAccMode);
        Console.WriteLine($"movec errcode:{rtn}");
        rtn = robot.MoveJ(j2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:{rtn}");
        rtn = robot.Circle(desc_pos3, tool, user, vel, acc, epos, desc_pos1, tool, user, vel, acc, epos,ovl, flag, offset_pos, oacc, blendR, -1, velAccMode);
        Console.WriteLine($"circle errcode:{rtn}");
    }

笛卡爾空間螺旋線運動
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間螺旋線運動 
    * @param [in] joint_pos 目標關節位置,單位 deg 
    * @param [in] desc_pos 目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] epos 擴展軸位置，單位 mm 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] offset_flag 0-不偏移，1-基座標系/工件座標系下偏移，2-工具座標系下偏移 
    * @param [in] offset_pos 位姿偏移量 
    * @param [in] spiral_param 螺旋參數 
    * @return 錯誤碼 
    */
    int NewSpiral(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, ExaxisPos epos, float ovl, byte offset_flag, DescPose offset_pos, SpiralParam spiral_param); 

笛卡爾空間螺旋線運動(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
.. code-block:: c#
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
         Console.WriteLine("movej errcode:"+ rtn);

        rtn = robot.NewSpiral(desc_pos, tool, user, vel, acc, epos, ovl, flag, offset_pos2, sp,-1);
        Console.WriteLine("newspiral errcode:"+ rtn);

        return 0;
    }

伺服運動開始
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 伺服運動開始，配合ServoJ、ServoCart指令使用
    * @param[in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return 錯誤碼
    */
    public int ServoMoveStart (int comType = 0)

伺服運動結束
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 伺服運動結束，配合ServoJ、ServoCart指令使用
    * @param[in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return 錯誤碼
    */
    public int ServoMoveEnd (int comType = 0)

關節空間伺服模式運動
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    /**
    * @brief  關節空間伺服模式運動
    * @param  [in] joint_pos  目標關節位置,單位deg
    * @param  [in] axisPos  外部軸位置,單位mm
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @param  [in] id servoJ指令ID,預設為0
    * @param  [in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return  錯誤碼
    */
    public int ServoJ(JointPos joint_pos, ExaxisPos axisPos, float acc, float vel, float cmdT, float filterT, float gain, int id = 0, int comType = 0)

基於UDP通訊的ServoJ、ServoMoveStart、ServoMoveEnd SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    public void TestServoJUDP()
    {
        // 訂閱回調
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };

        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 300;
        float dt = 0.1f;
        int cmdID = 0;

        while (true)
        {
            JointPos j = new JointPos(0, -90, 90, 0, 0, 0);
            ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
            DescPose offset_pos = new DescPose(0, -90, 90, 0, 0, 0);
            robot.MoveJ(j, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);
            int ret = robot.GetActualJointPosDegree(flag, ref j);
            if (ret == 0)
            {
                count = 300;
                cmdID += 1;
                robot.ServoMoveStart(1);

                while (count > 0)
                {
                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, 1);
                    j.jPos[0] += dt;
                    j.jPos[1] += dt;
                    j.jPos[3] += dt;
                    j.jPos[4] += dt;
                    j.jPos[5] += dt;
                    epos.ePos[0] += dt;
                    count -= 1;
                    Thread.Sleep(1);
                    robot.GetRobotRealTimeState(ref pkg);
                }
                robot.ServoMoveEnd(1);

                Thread.Sleep(1000);
                count = 300;
                robot.ServoMoveStart(1);
                while (count > 0)
                {
                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID, 1);
                    j.jPos[0] -= dt;
                    j.jPos[1] -= dt;
                    j.jPos[3] -= dt;
                    j.jPos[4] -= dt;
                    j.jPos[5] -= dt;
                    epos.ePos[0] -= dt;
                    count -= 1;
                    Thread.Sleep(1);
                    robot.GetRobotRealTimeState(ref pkg);
                }
                robot.ServoMoveEnd(1);
            }
            else
            {
                Console.WriteLine($"GetActualJointPosDegree errcode:{ret}");
            }
        }
    }

關節空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.4  Web-3.8.3
    
.. code-block:: c#
    :linenos:

    private void btnJointServoMove_Click(object sender, EventArgs e)
    {
        JointPos j = new JointPos(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.008f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 500;
        float dt = 0.1f;
        int cmdID = 0;
        int ret = robot.GetActualJointPosDegree(flag, ref j);
        if (ret == 0)
        {
            robot.ServoMoveStart();

            try
            {
                while (count > 0)
                {

                    robot.ServoJ(j, epos, acc, vel, cmdT, filterT, gain, cmdID);


                    j.jPos[0] += dt;
                    count--;


                    robot.WaitMs((int)(cmdT * 1000));
                }
            }
            finally
            {

                robot.ServoMoveEnd();
            }
        }
        else
        {
            Console.WriteLine($"GetActualJointPosDegree error code: {ret}");

        }
    }

關節扭矩控制開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制開始
    * @param [in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return 錯誤碼
    */
    public int ServoJTStart (int comType = 0)

關節扭矩控制
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制
    * @param [in] torque j1~j6關節扭矩，單位Nm
    * @param [in] interval 指令週期，單位s，範圍[0.001~0.008]
    * @param [in] checkFlag 檢測策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同時限制
    * @param [in] jPowerLimit 關節最大功率限制(W)
    * @param [in] jVelLimit 關節最大速度(°/s)
    * @param [in]  comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return 錯誤碼
    */
    public int ServoJT(double[] torque, double interval, int checkFlag, double[] jPowerLimit, double[] jVelLimit, int comType = 0)

關節扭矩控制結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節扭矩控制結束
    * @param[in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return  錯誤碼
    */
    public int ServoJTEnd (int comType = 0)

基於UDP通訊的ServoJT、ServoJTStart、ServoJTEnd SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoJTWithSafetyUDP()
    {
        // 訂閱回調
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[UDP響應] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };
        while (true)
        {
            robot.ResetAllError();
            Thread.Sleep(500);

            JointPos j = new JointPos(7.053, -89.699, 156.141, -72.751, 7.829, 1.889);
            ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
            DescPose offset_pos = new DescPose(-151.288, -321.186, 221.989, 89.140, 4.361, -0.795);
            robot.MoveJ(j, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            double[] torques = new double[6] { 0, 0, 0, 0, 0, 0 };
            robot.GetJointTorques(1, torques);

            robot.ServoJTStart(1);
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);

            int checkFlag = 0;
            double[] jPowerLimit = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
            double[] jVelLimit = new double[6] { 50, 50, 50, 50, 50, 50 };
            int error = 0;
            while (true)
            {

                torques[0] = 0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 1);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] > 30)
                {
                    break;
                }
            }

            while (true)
            {

                torques[0] = -0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 1);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] < 0)
                {
                    break;
                }
            }

            robot.DragTeachSwitch(0);
            error = robot.ServoJTEnd(1);
        }
        return 0;
    }

關節扭矩控制代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button27_Click(object sender, EventArgs e)
    {
        robot.DragTeachSwitch(1);
        robot.SetPowerLimit(1, 200);
        double[] torques = { 0, 0, 0, 0, 0, 0 };
        robot.GetJointTorques(1, torques);

        int count = 100;
        robot.ServoJTStart();
        int error = 0;
        while (count > 0)
        {
            error = robot.ServoJT(torques, 0.001f);
            count--;
            Thread.Sleep(1);
        }
        error = robot.ServoJTEnd();
        robot.DragTeachSwitch(0);
    }

笛卡爾空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

笛卡爾空間伺服模式運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 笛卡爾空間伺服模式運動
    * @param [in] mode 0-絕對運動(基座標系)，1-增量運動(基座標系)，2-增量運動(工具座標系)
    * @param [in] desc_pos 目標笛卡爾位姿或位姿增量
    * @param [in] exaxis 擴展軸位置
    * @param [in] pos_gain 位姿增量比例係數，僅在增量運動下生效，範圍[0~1]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放，預設為0
    * @param [in] vel 速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param [in] cmdT 指令下發週期，單位s，建議範圍[0.001~0.016]
    * @param [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param [in] gain 目標位置的比例放大器，暫不開放，預設為0
    * @return 錯誤碼
    */
    public int ServoCart(int mode, DescPose desc_pose, ExaxisPos exaxis, double[] pos_gain, double acc, double vel, double cmdT, double filterT, double gain);

笛卡爾空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void TestServoCart()
    {
        ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();

        int rtn;
        DescPose desc_pos_dt = new DescPose(83.00800f, 50.525000f, 29.246f, 179.629f, -7.138f, -166.975f);
        ExaxisPos exaxis = new ExaxisPos(100.0f, 0.0f, 0.0f, 0.0f);
        double[] pos_gain = { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
        int mode = 0;
        float vel = 0.0f;
        float acc = 0.0f;
        float cmdT = 0.001f;
        float filterT = 0.0f;
        float gain = 0.0f;
        byte flag = 0;
        int count = 5000;

        robot.SetSpeed(20);

        while (count > 0)
        {
            rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain);
            Console.WriteLine($"ServoCart rtn is {rtn}");
            count -= 1;
            desc_pos_dt.tran.x += 0.01f;
            exaxis.ePos[0] += 0.01f;
        }
    }

具有超速保護的關節扭矩控制程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoJTWithSafety()
    {
        while (true)
        {
            robot.ResetAllError();
            Thread.Sleep(500);

            JointPos j = new JointPos(7.053, -89.699, 156.141, -72.751, 7.829, 1.889);
            ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
            DescPose offset_pos = new DescPose(-151.288, -321.186, 221.989, 89.140, 4.361, -0.795);
            robot.MoveJ(j, 0, 0, 100, 100, 100, epos, -1, 0, offset_pos);

            double[] torques = new double[6] { 0, 0, 0, 0, 0, 0 };
            robot.GetJointTorques(1, torques);

            robot.ServoJTStart(0);
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);

            int checkFlag = 0;
            double[] jPowerLimit = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
            double[] jVelLimit = new double[6] { 50, 50, 50, 50, 50, 50 };
            int error = 0;
            while (true)
            {

                torques[0] = 0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 0);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] > 30)
                {
                    break;
                }
            }

            while (true)
            {

                torques[0] = -0.1;
                error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit, 0);

                Console.WriteLine($"ServoJT rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                if (pkg.jt_cur_pos[0] < 0)
                {
                    break;
                }
            }

            robot.DragTeachSwitch(0);
            error = robot.ServoJTEnd(0);
        }
    }

樣條運動開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  樣條運動開始
    * @return  錯誤碼
    */
    int SplineStart();

樣條運動PTP
++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
    int SplinePTP(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl);

關節空間樣條運動 (自動正運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  樣條運動結束
    * @return  錯誤碼
    */
    int SplineEnd(); 

樣條運動代碼示例
++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnSplineMove_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");

        robot.SplineStart();
        robot.SplinePTP(j1, desc_pos1, tool, user, vel, acc, ovl);
        robot.SplinePTP(j2, desc_pos2, tool, user, vel, acc, ovl);
        robot.SplinePTP(j3, desc_pos3, tool, user, vel, acc, ovl);
        robot.SplinePTP(j4, desc_pos4, tool, user, vel, acc, ovl);
        robot.SplineEnd();
    }

新樣條運動開始
++++++++++++++++++++++++++++++++++
.. versionchanged:: C#SDK-v1.0.6

.. code-block:: c#
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @param [in] type  0-圓弧過渡，1-給定點位爲路徑點
    * @param [in] averageTime  全局平均銜接時間(ms)(10 ~  )，默認2000
    * @return 錯誤碼 
    */ 
    int NewSplineStart(int type, int averageTime=2000);
    
新樣條指令點
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 增加樣條運動指令點 
    * @param [in] joint_pos 目標關節位置,單位 deg 
    * @param [in] desc_pos 目標笛卡爾位姿 
    * @param [in] tool 工具座標號，範圍[0~14] 
    * @param [in] user 工件座標號，範圍[0~14] 
    * @param [in] vel 速度百分比，範圍[0~100] 
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放 
    * @param [in] ovl 速度縮放因子，範圍[0~100] 
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] lastFlag  是否爲最後一個點，0-否，1-是
    * @return 錯誤碼 
    */ 
    int NewSplinePoint(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, int lastFlag);

新樣條指令點(自動逆運動學計算)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.7  Web-3.8.5

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 新樣條運動開始 
    * @return 錯誤碼 
    */ 
    int NewSplineEnd();
    
新樣條運動代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnNewSpline_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        JointPos j3 = new JointPos(-61.954, -84.409, 108.153, -116.316, -91.283, 74.260);
        JointPos j4 = new JointPos(-89.575, -80.276, 102.713, -116.302, -91.284, 74.267);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose desc_pos3 = new DescPose(-327.622, 402.230, 320.402, -178.067, 2.127, -46.207);
        DescPose desc_pos4 = new DescPose(-104.066, 544.321, 327.023, -177.715, 3.371, -73.818);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        int err = -1;
        err = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Console.WriteLine($"movej errcode:  {err}");

        robot.NewSplineStart(1, 2000);
        robot.NewSplinePoint(j1, desc_pos1, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j2, desc_pos2, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j3, desc_pos3, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j4, desc_pos4, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplinePoint(j5, desc_pos5, tool, user, vel, acc, ovl, -1, 0);
        robot.NewSplineEnd();
    }

終止運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 終止運動
    * @return  錯誤碼
    */
    int StopMotion();

暫停運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
    
    /** 
      * @brief 暫停運動 
      * @return 錯誤碼 
    */  
    int PauseMotion();

恢復運動
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /** 
    * @brief 恢復運動 
    * @return 錯誤碼 
    */ 
    int ResumeMotion();

運動暫停、恢復、停止代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMotionPause_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j5 = new JointPos(-95.228, -54.621, 73.691, -112.245, -91.280, 74.268);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos5 = new DescPose(-33.421, 732.572, 275.103, -177.907, 2.709, -79.482);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;

        robot.SetSpeed(20);

        rtn = robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        rtn = robot.MoveJ(j5, desc_pos5, tool, user, vel, acc, ovl, epos, 1, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PauseMotion();

        Thread.Sleep(1000);
        robot.ResumeMotion();

        Thread.Sleep(1000);
        robot.StopMotion();

        Thread.Sleep(1000);

    }

點位整體偏移開始
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  點位整體偏移開始
    * @param  [in]  flag  0-基座標系下/工件座標系下偏移，2-工具座標系下偏移
    * @param  [in] offset_pos  位姿偏移量
    * @return  錯誤碼
    */
    int PointsOffsetEnable(int flag, DescPose offset_pos); 


點位整體偏移結束
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  點位整體偏移結束
    * @return  錯誤碼
    */
    int PointsOffsetDisable(); 

點位偏移代碼示例
++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnPointOffect_Click(object sender, EventArgs e)
    {
        JointPos j1, j2;
        DescPose desc_pos1, desc_pos2, offset_pos, offset_pos1;
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);

        j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);

        desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);

        offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        offset_pos1 = new DescPose(50.0, 50.0, 50.0, 5.0, 5.0, 5.0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = -1.0f;
        byte flag = 0;
        int type = 0;

        robot.SetSpeed(20);

        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetEnable(type, offset_pos1);
        Thread.Sleep(1000);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        Thread.Sleep(1000);
        robot.PointsOffsetDisable();
    }

控制箱AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7

.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 控制箱AO飛拍停止
    * @return 錯誤碼
    */
    int MoveAOStop();
    
末端AO飛拍開始
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
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
++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.7
   
.. code-block:: c#
    :linenos:

    /**
    * @brief 末端AO飛拍停止
    * @return 錯誤碼
    */
    int MoveToolAOStop();

AO飛拍代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void btnMoveAO_Click(object sender, EventArgs e)
    {
        JointPos j1 = new JointPos(-11.904, -99.669, 117.473, -108.616, -91.726, 74.256);
        JointPos j2 = new JointPos(-45.615, -106.172, 124.296, -107.151, -91.282, 74.255);
        DescPose desc_pos1 = new DescPose(-419.524, -13.000, 351.569, -178.118, 0.314, 3.833);
        DescPose desc_pos2 = new DescPose(-321.222, 185.189, 335.520, -179.030, -1.284, -29.869);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);

        int tool = 0;
        int user = 0;
        float vel = 100.0f;
        float acc = 100.0f;
        float ovl = 100.0f;
        float blendT = 0.0f;
        float blendR = 0.0f;
        byte flag = 0;
        byte search = 0;

        robot.SetSpeed(5);

        robot.MoveAOStart(0,100,100,20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveAOStop();

        robot.MoveToolAOStart(0, 100, 100, 20);
        robot.MoveJ(j1, desc_pos1, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveJ(j2, desc_pos2, tool, user, vel, acc, ovl, epos, blendT, flag, offset_pos);
        robot.MoveToolAOStop();
    }

開始Ptp運動FIR濾波
++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:


    /**
    * @brief 開始Ptp運動FIR濾波
    * @param [in] maxAcc 最大加速度極值(deg/s2)
    * @param [in] maxJek 統一關節急動度極值(deg/s3)
    * @return 錯誤碼
    */
    int PtpFIRPlanningStart(double maxAcc, double maxJek=1000);

關閉Ptp運動FIR濾波
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關閉Ptp運動FIR濾波
    * @return 錯誤碼
    */
    int PtpFIRPlanningEnd();

開始LIN、ARC運動FIR濾波
++++++++++++++++++++++++++++++
.. code-block:: c#
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
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關閉LIN、ARC運動FIR濾波
    * @return 錯誤碼
    */
    int LinArcFIRPlanningEnd();

FIR濾波代碼示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.3  Web-3.8.2
    
.. code-block:: c#
    :linenos:


    private void button69_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos midjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);
        JointPos endjointPos = new JointPos(-29.777f, -84.536f, 109.275f, -114.075f, -86.655f, 74.257f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose middescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);
        DescPose enddescPose = new DescPose(-487.434f, 154.362f, 308.576f, 176.600f, 0.268f, -14.061f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.PtpFIRPlanningStart(1000, 1000);
        Console.WriteLine("PtpFIRPlanningStart rtn is " + rtn);
        robot.MoveJ(startjointPos, startdescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.MoveJ(endjointPos, enddescPose, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
        robot.PtpFIRPlanningEnd();
        Console.WriteLine("PtpFIRPlanningEnd rtn is " + rtn);

        robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000);
        Console.WriteLine("LinArcFIRPlanningStart rtn is " + rtn);
        robot.MoveL(startjointPos, startdescPose, 0, 0, 20, 100, 100, -1,0, exaxisPos, 0, 0, offdese, 1, 50);
        robot.MoveC(midjointPos, middescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, endjointPos, enddescPose, 0, 0, 100, 100, exaxisPos, 0, offdese, 100, -1, 100, 0);
        robot.LinArcFIRPlanningEnd();
        Console.WriteLine("LinArcFIRPlanningEnd rtn is " + rtn);
    }

加速度平滑開啓
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 加速度平滑開啓
    * @param  [in] saveFlag 是否斷電保存
    * @return  錯誤碼
    */
    int AccSmoothStart(bool saveFlag);

加速度平滑關閉
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 加速度平滑關閉
    * @param  [in] saveFlag 是否斷電保存
    * @return  錯誤碼
    */
    int AccSmoothEnd(bool saveFlag);

代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button1_Click(object sender, EventArgs e)
    {

        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AccSmoothStart(false);
        Console.WriteLine("AccSmoothStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AccSmoothEnd(false);
        Console.WriteLine("AccSmoothEnd rtn is " + rtn);
    }

指定姿態速度開啓
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 指定姿態速度開啓
    * @param [in] ratio 姿態速度百分比[0-300]
    * @return  錯誤碼
    */
    int AngularSpeedStart(int ratio);

指定姿態速度關閉
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:
   
    /**
    * @brief 指定姿態速度關閉
    * @return  錯誤碼
    */
    int AngularSpeedEnd();

機器人指定姿態速度代碼示例
+++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private void button71_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);
        rtn = robot.AngularSpeedStart(50);
        Console.WriteLine("AngularSpeedStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.AngularSpeedEnd();
        Console.WriteLine("AngularSpeedEnd rtn is " + rtn);
    }

開始奇異位姿保護
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 開始奇異位姿保護
    * @param [in] protectMode 奇異保護模式，0：關節模式；1-笛卡爾模式
    * @param [in] minShoulderPos 肩奇異調整範圍(mm), 默認100
    * @param [in] minElbowPos 肘奇異調整範圍(mm), 默認50
    * @param [in] minWristPos 腕奇異調整範圍(°), 默認10
    * @return 錯誤碼
    */
    int SingularAvoidStart(int protectMode, double minShoulderPos, double minElbowPos, double minWristPos);

停止奇異位姿保護
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9

.. code-block:: c#
    :linenos:

    /**
    * @brief 停止奇異位姿保護
    * @return 錯誤碼
    */
    int SingularAvoidEnd();

代碼示例
+++++++++++++++++++++++++++++
.. versionadded:: C#SDK-v1.0.9
    
.. code-block:: c#
    :linenos:

    private void btnTestSingularAvoidEArc_Click(object sender, EventArgs e)
    {
        int rtn;
        JointPos startjointPos = new JointPos(-11.904f, -99.669f, 117.473f, -108.616f, -91.726f, 74.256f);
        JointPos endjointPos = new JointPos(-45.615f, -106.172f, 124.296f, -107.151f, -91.282f, 74.255f);

        DescPose startdescPose = new DescPose(-419.524f, -13.000f, 351.569f, -178.118f, 0.314f, 3.833f);
        DescPose enddescPose = new DescPose(-321.222f, 185.189f, 335.520f, -179.030f, -1.284f, -29.869f);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        rtn = robot.SingularAvoidStart(2, 10, 5, 5);
        Console.WriteLine("SingularAvoidStart rtn is " + rtn);
        robot.MoveJ( startjointPos,  startdescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        robot.MoveJ( endjointPos,  enddescPose, 0, 0, 100, 100, 100,  exaxisPos, -1, 0,  offdese);
        rtn = robot.SingularAvoidEnd();
        Console.WriteLine("SingularAvoidEnd rtn is " + rtn);
    }

安全停止觸發
++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 安全停止觸發信號
    * @return 錯誤碼
    */
    int GetSafetyCode();

清空運動指令隊列
++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C#SDK-V1.1.9  Web-3.8.7
    
.. code-block:: c#
    :linenos:

    /**
    * @brief 清空運動指令隊列
    * @return 錯誤碼
    */
    public int MotionQueueClear();

移動到相貫線起始點
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
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
.. code-block:: c#
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
.. code-block:: c#
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

原地空運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 原地空運動
    * @return 錯誤碼
    */
    public int MoveStationary()

原地空運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public void LaserSensorRecordandReplay()
    {
        int rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 1, 10, 100);
        Console.WriteLine($"LaserSensorRecordandReplay rtn is {rtn}");
        rtn = robot.MoveStationary();
        Console.WriteLine($"MoveStationary rtn is {rtn}");
        rtn = robot.LaserSensorRecord1(0, 10);
        Console.WriteLine($"LaserSensorRecord1 rtn is {rtn}"); 
    }

定點擺動開始
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 定點擺動開始
    * @param [in] weaveNum 擺動編號[0-7]
    * @param [in] mode 0-工具座標系；1-參考點
    * @param [in] refPoint 參考點笛卡爾座標[x,y,z,a,b,c]
    * @param [in] weaveTime 擺動時間[s]
    * @return 錯誤碼
    */
    public int OriginPointWeaveStart(int weaveNum, int mode, DescPose refPoint, double weaveTime);
    
定點擺動結束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 定點擺動結束
    * @return 錯誤碼
    */
    public int OriginPointWeaveEnd();
        
定點擺動的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void TestOriginPointWeave()
    {
        // 創建關節位置對象
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);

        // 參考點座標
        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);

        //// 第一次運動
        robot.MoveJ(j, 1, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // 啟動定點擺動（模式0）
        robot.OriginPointWeaveStart(0, 0, refPoint, 3);
        robot.MoveStationary();   // 執行固定運動（假設該方法存在）
        robot.OriginPointWeaveEnd();

        Thread.Sleep(2000);         // 等待2秒

        // 第二次運動
        robot.MoveJ(j, 1, 0, 100, 100, 100, epos, -1, 0, offset_pos);

        // 啟動定點擺動（模式1）
        robot.OriginPointWeaveStart(0, 1, refPoint, 3);
        robot.MoveStationary();
        robot.OriginPointWeaveEnd();

    }

定點擺動（包含雷射及擴展軸）的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    void TestOriginPointWeave2()
    {
        // 創建關節位置物件
        JointPos j = new JointPos(39.886, -98.580, -124.032, -47.393, 90.000, 40.842);
        ExaxisPos epos1 = new ExaxisPos(0, 0, 0, 0);
        DescPose offset_pos = new DescPose(0, 0, 0, 0, 0, 0);
        ExaxisPos epos2 = new ExaxisPos(5, 0.000, 0.000, 0.000);

        // 參考點座標
        DescPose refPoint = new DescPose(400.021, 300.022, 299.996, 179.997, -0.003, -90.956);

        int rtn = 0;
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020);
        robot.LaserTrackingSensorSamplePeriod(20);
        robot.LoadPosSensorDriver(101);

        // 載入 UDP 驅動
        robot.ExtDevLoadUDPDriver();

        // 設置外部軸命令完成時間
        rtn = robot.SetExAxisCmdDoneTime(5000.0);
        Console.WriteLine("SetExAxisCmdDoneTime rtn is " + rtn);

        // 使能外部軸 1 和 2
        rtn = robot.ExtAxisServoOn(1, 1);
        Console.WriteLine("ExtAxisServoOn axis id 1 rtn is " + rtn);
        rtn = robot.ExtAxisServoOn(2, 1);
        Console.WriteLine("ExtAxisServoOn axis id 2 rtn is " + rtn);
        Thread.Sleep(2000);

        // 設置外部軸回零
        robot.ExtAxisSetHoming(1, 0, 10, 2);
        robot.LaserTrackingLaserOnOff(1);


        //// 1---不帶擴展軸
        robot.LaserTrackingTrackOnOff(1, 4);
        robot.Sleep(200);
        // 啟動定點擺動
        robot.OriginPointWeaveStart(0, 0, refPoint, 10);
        robot.MoveStationary();   // 執行固定運動
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);

        Thread.Sleep(2000);         // 等待2秒

        //// 2---帶擴展軸
        robot.ExtAxisMove(epos1, 100, -1);
        robot.LaserTrackingTrackOnOff(1, 4);
        // 啟動定點擺動
        robot.OriginPointWeaveStart(0, 0, refPoint, 20);
        robot.ExtAxisMove(epos2, 100, -1);
        robot.OriginPointWeaveEnd();
        robot.LaserTrackingTrackOnOff(0, 4);
    }

關節空間速度伺服模式運動
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  關節空間速度伺服模式運動
    * @param  [in] joint_pos  6個目標關節速度,單位deg/s
    * @param  [in] axisPos  4個外部軸速度,單位deg/s
    * @param  [in] acc  加速度百分比，範圍[0~100],暫不開放，預設為0
    * @param  [in] vel  速度百分比，範圍[0~100]，暫不開放，預設為0
    * @param  [in] cmdT  指令下發週期，單位s，建議範圍[0.001~0.0016]
    * @param  [in] filterT 濾波時間，單位s，暫不開放，預設為0
    * @param  [in] gain  目標位置的比例放大器，暫不開放，預設為0
    * @param  [in] id servoJ指令ID,預設為0
    * @param[in] comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return  錯誤碼
    */
    public int ServoJV(double[] joint_vel, double[] exis_vel, float acc, float vel, float cmdT, float filterT, float gain, int id = 0, int comType = 0)

關節空間速度伺服模式運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoJVtest()
    {
        double[] joint_vel = new double[6] { 10, 0, 0, 0, 0, 0 };
        double[] exis_vel = new double[4] { 0, 0, 0, 0 };
        float acc = 0.0f; 
        float vel = 0.0f;
        float cmdT = 0.01f; 
        float filterT = 0.0f; 
        float gain = 0.0f;
        int cnt = 0;
        while (cnt < 200)
        {
            int error = robot.ServoJV(joint_vel, exis_vel, acc, vel, cmdT, filterT, gain);
            Console.WriteLine($"ServoJV rtn is {error}");
            cnt++;
        }
        return 0;
    }

關節MIT控制開始
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節MIT控制開始
    * @param [in]  comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return  錯誤碼
    */
    public int ServoMITStart(int comType = 0)

關節MIT控制結束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節MIT控制結束
    * @param [in]  comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return  錯誤碼
    */
    public int ServoMITEnd(int comType = 0)

關節MIT控制
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 關節MIT控制
    * @param [in] posGain j1~j6關節位置增益
    * @param [in] desPos j1~j6關節期望位置 單位:deg
    * @param [in] velGain j1~j6關節速度增益
    * @param [in] desVel j1~j6關節期望速度 單位:deg/s
    * @param [in] torque_ff j1~j6前饋力矩 單位:Nm
    * @param [in] interval 指令週期，單位s，範圍[0.001~0.008]
    * @param [in]  comType 指令下發類型；0-xmlrpc；1-UDP(對應機器人20007端口)
    * @return 錯誤碼
    */
    public int ServoMIT(double[] posGain, double[] desPos, double[] velGain, double[] desVel, double[] torque_ff, double interval, int comType = 0)

關節MIT控制運動代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int ServoMITtest()
    {
        // 訂閱回調
        robot.OnUdpFrameReceived += (comType, frameCount, frameCmdID, contentLen, content) =>
        {
            Console.WriteLine($"[UDP響應] comType={comType}, count={frameCount}, cmdID={frameCmdID}, content={content}");
        };
        while (true)
        {
            robot.ResetAllError();
            Thread.Sleep(500);

            double[] posGain = new double[6] { 0, 0, 0, 0, 0, 0 };
            double[] desPos = new double[6] { 0, 0, 0, 0, 0, 0 };
            double[] velGain = new double[6] { 0, 0, 0, 0, 0, 0 };
            double[] desVel = new double[6] { 0, 0, 0, 0, 0, 0 };
            double[] torques = new double[6] { 0, 0, 0, 0, 0, 0 };
            robot.GetJointTorques(1, torques);
            Console.WriteLine($"111111");
            //robot.ServoMITEnd(0);
            robot.ServoMITStart(0);
            Console.WriteLine($"ServoMITStart");
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.DragTeachSwitch(1);
            Console.WriteLine($"DragTeachSwitch");
            double intev = 0.008;
            double[] jPowerLimit = new double[6] { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
            double[] jVelLimit = new double[6] { 50, 50, 50, 50, 50, 50 };
            int error = 0;
            while (true)
            {

                torques[5] = 0.03;
                Console.WriteLine($"ServoMIT call ");
                error = robot.ServoMIT(posGain, desPos, velGain, desVel, torques, intev, 0);

                Console.WriteLine($"ServoMIT111111 rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                //Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                Console.WriteLine($"pkg.jt_cur_pos[5]:{pkg.jt_cur_pos[5]}");
                if (pkg.jt_cur_pos[5] > 30)
                {
                    break;
                }
            }

            while (true)
            {

                torques[5] = -0.03;
                error = robot.ServoMIT(posGain, desPos, velGain, desVel, torques, intev, 0);

                Console.WriteLine($"ServoJT222222 rtn is {error}");
                Thread.Sleep(1);

                robot.GetRobotRealTimeState(ref pkg);
                //Console.WriteLine($"maincode {pkg.main_code}, subcode {pkg.sub_code}");
                Console.WriteLine($"pkg.jt_cur_pos[5]:{pkg.jt_cur_pos[5]}");
                if (pkg.jt_cur_pos[5] < 0)
                {
                    break;
                }
            }

            robot.DragTeachSwitch(0);
            error = robot.ServoMITEnd(0);
        }
        return 0;
    }

工件座標系點位轉換開始
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  工件座標系點位轉換開始
    * @param  [in] workpieceID 工件號[0-14]
    * @return  錯誤碼，成功返回0
    */
    public int WorkPieceTrsfStart(int workpieceID)
    
工件座標系點位轉換結束
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief  工件座標系點位轉換結束
    * @return  錯誤碼，成功返回0
    */
    public int WorkPieceTrsfEnd()
        
工件座標系點位轉換代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    public int TestWorkPieceTrsf()
    {

        // ---- 點位定義----
        JointPos j1 = new JointPos(-11.188, -64.165, -107.299, -76.706, 89.590, 92.983);
        DescPose d1 = new DescPose(225.986, 190.694, 394.238, -6.230, -23.797, -98.972);
        JointPos j2 = new JointPos(-38.148, -97.408, -133.704, -30.999, 89.584, 92.986);
        DescPose d2 = new DescPose(52.741, 262.917, 30.824, -5.696, -9.864, -126.092);
        JointPos j3 = new JointPos(-25.561, -123.131, -85.736, -94.911, 89.582, 93.006);
        DescPose d3 = new DescPose(70.455, 88.410, 45.299, -4.101, 31.775, -113.199);
        JointPos j4 = new JointPos(-8.013, -125.881, -79.196, -84.440, 89.564, 93.005);
        DescPose d4 = new DescPose(209.453, -73.895, 56.416, -4.727, 17.523, -95.906);
        JointPos j5 = new JointPos(-2.722, -94.518, -119.965, -54.518, 89.563, 93.005);
        DescPose d5 = new DescPose(274.800, 81.106, 102.977, -5.467, -2.980, -90.711);
        JointPos j6 = new JointPos(-2.671, -56.234, -138.914, -25.099, 95.355, 92.967);
        DescPose d6 = new DescPose(300.392, 177.281, 300.926, -1.909, -51.894, -89.703);
        JointPos j7 = new JointPos(-1.229, -121.184, -63.201, -122.331, 93.045, 93.019);
        DescPose d7 = new DescPose(296.856, -31.294, 215.698, -0.589, 34.594, -88.954);

        ExaxisPos ex = new ExaxisPos(0, 0, 0, 0);
        DescPose zeroOff = new DescPose(0, 0, 0, 0, 0, 0);

        int tool = 1;
        int workpiece = 1;
        float blend = 5.0f;

        // ===== 座標系1 =====
        // Home
        robot.MoveJ(j1, d1, tool, workpiece, 100, 100, 100, ex, -1, 0, zeroOff);
        // PTP
        robot.MoveJ(j2, d2, tool, workpiece, 100, 100, 100, ex, blend, 0, zeroOff);
        // LIN
        robot.MoveL(j3, d3, tool, workpiece, 10, 100, 100, blend, 0, ex, 0, 1, zeroOff, 0, 90);
        // ARC
        robot.MoveC(j4, d4, tool, workpiece, 100, 100, ex, 0, zeroOff,
                    j5, d5, tool, workpiece, 100, 100, ex, 0, zeroOff,
                    10, blend, 100, 0);
        // CIR
        robot.Circle(j6, d6, tool, workpiece, 100, 100, ex,
                        j7, d7, tool, workpiece, 100, 100, ex,
                        10, 0, zeroOff, 100.0, blend, 0);

        // ===== WorkPieceTrsfStart(2) =====
        int rtn = robot.WorkPieceTrsfStart(2);
        Console.WriteLine("  WorkPieceTrsfStart(2) rtn={0}", rtn);

        // ===== 座標系2 (轉換後) =====
        robot.MoveJ(j1, d1, tool, workpiece, 100, 100, 100, ex, -1, 0, zeroOff);
        robot.MoveJ(j2, d2, tool, workpiece, 100, 100, 100, ex, blend, 0, zeroOff);
        robot.MoveL(j3, d3, tool, workpiece, 10, 100, 100, blend, 0, ex, 0, 1, zeroOff, 0, 90);
        robot.MoveC(j4, d4, tool, workpiece, 100, 100, ex, 0, zeroOff,
                    j5, d5, tool, workpiece, 100, 100, ex, 0, zeroOff,
                    10, blend, 100, 0);
        robot.Circle(j6, d6, tool, workpiece, 100, 100, ex,
                        j7, d7, tool, workpiece, 100, 100, ex,
                        10, 0, zeroOff, 100.0, blend, 0);

        // ===== WorkPieceTrsfEnd =====
        rtn = robot.WorkPieceTrsfEnd();
        Console.WriteLine("  WorkPieceTrsfEnd() rtn={0}", rtn);

        return rtn;
    }    