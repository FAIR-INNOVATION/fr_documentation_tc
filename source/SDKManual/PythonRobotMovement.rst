機器人運動
============

.. toctree:: 
    :maxdepth: 5

jog點動
+++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StartJOG(ref,nb,dir,max_dis,vel=20.0,acc=100.0)``"
    "描述", "jog點動"
    "必選參數", "- ``ref``：0-關節點動,2-基座標系點動,4-工具座標系點動,8-工件座標系點動；
    - ``nb``：1-1關節(x軸),2-2關節(y軸),3-3關節(z軸),4-4關節(rx),5-5關節(ry),6-6關節(rz);
    - ``dir``：0-負方向，1-正方向;
    - ``max_dis``：單次點動最大角度/距離，單位 ° 或 mm;"
    "默認參數", "- ``vel``：速度百分比，[0~100] 默認20;
    - ``acc``：加速度百分比，[0~100] 默認100;"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

jog點動減速停止
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StopJOG(ref)``"
    "描述", "jog點動減速停止"
    "必選參數", "- ``ref``：1-關節點動停止,3-基座標系點動停止,5-工具座標系點動停止,9-工件座標系點動停止"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

jog點動立即停止
++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ImmStopJOG()``"
    "描述", "jog點動立即停止"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人點動控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    for i in range(6):
        robot.StartJOG(0, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(2, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.ImmStopJOG()
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(4, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(5)
        time.sleep(1)
    for i in range(6):
        robot.StartJOG(8, i + 1, 0, 20.0, 20.0, 30.0)
        time.sleep(1)
        robot.StopJOG(9)
        time.sleep(1)
    robot.CloseRPC()

關節空間運動
++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveJ(joint_pos, tool, user, desc_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0, ovl = 100.0, exaxis_pos = [0.0,0.0,0.0,0.0], blendT = -1.0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "關節空間運動"
    "必選參數", "- ``joint_pos``:目標關節位置，單位[°]；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``desc_pos``:目標笛卡爾位姿，單位 [mm][°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用正運動學求解返回值;
    - ``vel``:速度百分比，[0~100] 默認20.0;
    - ``acc``:加速度百分比，[0~100]，暫不開放；
    - ``ovl``:速度縮放因子，[0~100] 默認100.0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``blendT``:[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``offset_pos``:位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0];"
    "返回值", "錯誤碼  成功-0  失敗- errcode"

笛卡爾空間直線運動
+++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveL(desc_pos, tool, user, joint_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], vel=20.0, acc=0.0, ovl=100.0,blendR=-1.0, blendMode = 0,exaxis_pos=[0.0, 0.0, 0.0, 0.0], search=0, offset_flag=0,offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],oacc = 100.0,config=-1,velAccParamMode=0,overSpeedStrategy=0,speedPercent=10)``"
    "描述", "笛卡爾空間直線運動"
    "必選參數", "- ``desc_pos``:目標笛卡爾位姿，單位[mm][°]；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel``:速度百分比，[0~100] 默認20.0；
    - ``acc``:加速度百分比，[0~100]，暫不開放 默認0.0；
    - ``ovl``:速度縮放因子，[0~100] 默認100.0；
    - ``blendR``:[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半徑 (非阻塞)，單位 [mm] 默認-1.0;
    - ``blendMode``:過渡方式；0-內切過渡；1-角點過渡,默認-0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``search``:[0]-不焊絲尋位，[1]-焊絲尋位；
    - ``offset_flag``:[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``offset_pos``:位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0];
    - ``oacc``:加速度縮放因子[0-100]/物理加速度(mm/s2) 默認 100;
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1
    - ``velAccParamMode``:速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默認0
    - ``overSpeedStrategy``:超速處理策略，0-策略關閉；1-標準；2-超速時報錯停止；3-自適應降速，默認為0
    - ``speedPercent``:允許降速閾值百分比[0-100]，默認10%
    "
    "返回值", "錯誤碼 成功-0  失敗- errcode"

笛卡爾空間圓弧運動
++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveC(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=100.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], offset_flag_p=0,offset_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_t=20.0, acc_t=100.0, exaxis_pos_t=[0.0, 0.0, 0.0, 0.0], offset_flag_t=0,offset_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],ovl=100.0, blendR=-1.0,oacc=100.0,config=-1,velAccParamMode=0)``"
    "描述", "笛卡爾空間圓弧運動"
    "必選參數", "- ``desc_pos_p``:路徑點笛卡爾位姿，單位[mm][°]；
    - ``tool_p``:路徑點工具號，[0~14];
    - ``user_p``:路徑點工件號，[0~14];
    - ``desc_pos_t``:目標點笛卡爾位姿，單位 [mm][°];
    - ``tool_t``:工具號，[0~14]；
    - ``user_t``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos_p``:路徑點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``joint_pos_t``:目標點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel_p``:路徑點速度百分比，[0~100] 默認20.0;
    - ``acc_p``:路徑點加速度百分比，[0~100] 暫不開放,默認0.0;
    - ``exaxis_pos_p``:路徑點外部軸 1位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``offset_flag_p``:路徑點是否偏移[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``vel_t``:目標點速度百分比，[0~100] 默認20.0;
    - ``acc_t``:目標點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_t``:目標點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``offset_flag_t``:目標點是否偏移[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``offset_pos_t``:目標點位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0];
    - ``ovl:``:速度縮放因子，[0~100] 默認100.0;
    - ``blendR``:[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半徑 (非阻塞)，單位 [mm] 默認-1.0;
    - ``oacc``:加速度縮放因子[0-100]/物理加速度(mm/s2) 默認 100;
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1;
    - ``velAccParamMode``:速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

笛卡爾空間整圓運動
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Circle(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],joint_pos_t=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],vel_p=20.0, acc_p=0.0, exaxis_pos_p=[0.0, 0.0, 0.0, 0.0], vel_t=20.0, acc_t=0.0,exaxis_pos_t=[0.0, 0.0, 0.0, 0.0],ovl=100.0, offset_flag=0, offset_pos=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], oacc=100.0, blendR=-1,config=-1,velAccParamMode=0)``"
    "描述", "笛卡爾空間整圓運動"
    "必選參數", "- ``desc_pos_p``:路徑點笛卡爾位姿，單位[mm][°]；
    - ``tool_p``:工具號，[0~14]；
    - ``user_p``:工件號，[0~14]；
    - ``desc_pos_t``:目標點笛卡爾位姿，單位[mm][°]；
    - ``tool_t``:工具號，[0~14]；
    - ``user_t``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos_p``:路徑點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``joint_pos_t``:目標點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel_p``:速度百分比，[0~100] 默認20.0;
    - ``acc_p``:路徑點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_p``:路徑點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``vel_t``:目標點速度百分比，[0~100] 默認20.0;
    - ``acc_t``:目標點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_t``:標點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]
    - ``ovl``:速度縮放因子，[0~100] 默認100.0;
    - ``offset_flag``:是否偏移[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``offset_pos``:位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]
    - ``oacc``:加速度縮放因子[0-100]/物理加速度(mm/s2)，默認：100；
    - ``blendR``:-1：阻塞；0~1000：平滑半徑,默認：-1；
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1;
    - ``velAccParamMode``:速度加速度參數模式；0-百分比；1-物理速度(mm/s)加速度(mm/s2) 默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

笛卡爾空間點到點運動
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveCart(desc_pos, tool, user, vel = 20.0, acc = 0.0, ovl = 100.0, blendT = -1.0, config = -1)``"
    "描述", "笛卡爾空間點到點運動"
    "必選參數", "- ``desc_pos``:目標笛卡爾位置；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``vel``:速度，範圍 [0~100]，默認爲 20.0;
    - ``acc``:加速度，範圍 [0~100]，暫不開放,默認爲 0.0;
    - ``ovl``:速度縮放因子，[0~100]，默認爲 100.0;
    - ``blendT``:[-1.0]-運動到位 (阻塞)，[0~500]-平滑時間 (非阻塞)，單位 [ms] 默認爲 -1.0;
    - ``config``:關節配置，[-1]-參考當前關節位置求解，[0~7]-依據關節配置求解 默認爲 -1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人基本運動指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    j4 = [-31.154, -95.317, 94.276, -88.079, -89.740, 74.256]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    desc_pos4 = [-443.165, 147.881, 480.951, 179.511, -0.775, -15.409]
    offset_pos = [0.0] * 6
    epos = [0.0] * 4
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    oacc = 100.0
    blendT = 0.0
    blendR = 0.0
    flag = 0
    search = 0
    blendMode = 0
    velAccMode = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos,oacc=oacc, velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel,acc_t=acc, exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, oacc=oacc, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl,offset_flag=flag, offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    rtn = robot.MoveCart(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, acc=acc,ovl=ovl, blendT=blendT, config=-1)
    print(f"MoveCart errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, blendR=blendR, blendMode=blendMode, exaxis_pos=epos, search=search, offset_flag=flag, offset_pos=offset_pos, config=-1,velAccParamMode=velAccMode)
    print(f"movel errcode:{rtn}")
    rtn = robot.MoveC(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, offset_flag_p=flag, offset_pos_p=offset_pos, desc_pos_t=desc_pos4, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc,exaxis_pos_t=epos, offset_flag_t=flag, offset_pos_t=offset_pos, ovl=ovl, blendR=blendR, config=-1, velAccParamMode=velAccMode)
    print(f"movec errcode:{rtn}")
    rtn = robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos)
    print(f"movej errcode:{rtn}")
    rtn = robot.Circle(desc_pos_p=desc_pos3, tool_p=tool, user_p=user, vel_p=vel, acc_p=acc, exaxis_pos_p=epos, desc_pos_t=desc_pos1, tool_t=tool, user_t=user, vel_t=vel, acc_t=acc, exaxis_pos_t=epos, ovl=ovl, offset_flag=flag,offset_pos=offset_pos, oacc=oacc, blendR=-1, velAccParamMode=velAccMode)
    print(f"circle errcode:{rtn}")
    robot.CloseRPC()
    return 0

笛卡爾空間螺旋線運動
++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSpiral(desc_pos, tool, user, param, joint_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0, exaxis_pos = [0.0,0.0,0.0,0.0], ovl = 100.0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0], config = -1)``"
    "描述", "笛卡爾空間螺旋線運動"
    "必選參數", "- ``desc_pos``:目標笛卡爾位姿，單位[mm][°];
    - ``tool``:工具號，[0~14];
    - ``user``:工件號，[0~14];
    - ``param=[circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]``：circle_num: 螺旋圈數;circle_angle: 螺旋傾角;rad_init: 螺旋初始半徑;rad_add: 半徑增量;rotaxis_add: 轉軸方向增量;rot_direction: 旋轉方向，0-順時針，1-逆時針, velAccMode速度加速度參數模式：0-角速度恆定，1-線速度恆定;"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel``:速度百分比，[0~100] 默認20.0;
    - ``acc``:加速度百分比，[0~100] 默認100.0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``ovl``:速度縮放因子，[0~100] 默認100.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基座標系下偏移，[2]-工具座標系下偏移 默認 0;
    - ``offset_pos``:位姿偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]
    - ``config``:逆解關節空間配置，[-1]-參考當前關節位置解算，[0~7]-依據特定關節空間配置求解，默認-1"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

代碼示例
++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j = [67.957, -81.482, 87.595, -95.691, -94.899, -9.727]
    desc_pos = [-123.142, -551.735, 430.549, 178.753, -4.757, 167.754]
    offset_pos1 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    offset_pos2 = [50.0, 0.0, 0.0, -30.0, 0.0, 0.0]
    epos = [0.0] * 4
    sp = [2, 30.0, 50.0, 10.0, 10.0, 0, 1]  # [circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction, velAccMode]
    tool = 0
    user = 0
    vel = 30.0
    acc = 60.0
    ovl = 100.0
    blendT = -1.0
    flag = 2
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j, tool=tool, user=user, vel=vel, acc=acc, ovl=ovl, exaxis_pos=epos, blendT=blendT, offset_flag=flag, offset_pos=offset_pos1)
    print(f"movej errcode:{rtn}")
    rtn = robot.NewSpiral(desc_pos=desc_pos, tool=tool, user=user, vel=vel, acc=acc, exaxis_pos=epos, ovl=ovl, offset_flag=flag, offset_pos=offset_pos2, param=sp)
    print(f"newspiral errcode:{rtn}")
    robot.CloseRPC()
    return 0

伺服運動開始
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveStart(cmdType=0)``"
    "描述", "伺服運動開始，配合ServoJ、ServoCart指令使用"
    "必選參數", "- ``cmdType``: 命令傳輸類型，0=XML-RPC，1=UDP透傳"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

伺服運動結束
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveEnd(cmdType=0)``"
    "描述", "伺服運動結束，配合ServoJ、ServoCart指令使用"
    "必選參數", "- ``cmdType``: 命令傳輸類型，0=XML-RPC，1=UDP透傳"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節空間伺服模式運動
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJ(joint_pos, axisPos, acc = 0.0, vel = 0.0, cmdT = 0.008, filterT = 0.0, gain = 0.0, id=0, cmdType=0)``"
    "描述", "關節空間伺服模式運動"
    "必選參數", "- ``joint_pos``:目標關節位置，單位[°]；
    - ``axisPos``:外部軸位置,單位mm；"
    "默認參數", "- ``acc``:加速度，範圍 [0~100]，暫不開放，預設為 0.0;
    - ``vel``:速度，範圍 [0~100]，暫不開放，預設為 0.0;
    - ``cmdT``:指令下發週期，單位s，建議範圍[0.001~0.0016], 預設為0.008;
    - ``filterT``:濾波時間，單位 [s]，暫不開放， 預設為0.0;
    - ``gain``:目標位置的比例放大器，暫不開放， 預設為0.0;
    - ``id``:servoJ指令ID,預設為0;
    - ``cmdType``:命令傳輸類型，0=XML-RPC，1=UDP透傳;"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

基於UDP通訊的ServoJ、ServoMoveStart、ServoMoveEnd SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def TestServoJUDP(self):
        # 設置回調
        def callback(src_type, count, cmd_id, data_len, content):
            print("回調函數: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        # # 初始化關節位置和外部軸位置
        j= [105, -108, 74, -66, -88.893, -1.621]
        offset_pos = [0, 0, 0, 0, 0, 0]
        epos = [0, 0, 0, 0]
        # # 移動到初始位置
        result=robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100,exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        print("MoveJ返回結果: {}".format(result))
        vel = 0.0
        acc = 0.0
        cmdT = 0.016
        filterT = 0.0
        gain = 0.0
        flag = 0
        dt = 0.1
        cmdID = 0

        # 獲取當前關節位置
        ret, j = robot.GetActualJointPosDegree(flag)
        if ret != 0:
            print(f"GetActualJointPosDegree errcode:{ret}")
        while 1:
            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("ServoMoveStart返回結果: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT,filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] += dt
                j[1] += dt
                j[2] += dt
                j[3] += dt
                j[4] += dt
                j[5] += dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("ServoMoveEnd返回結果: {}".format(result))

            count = 300
            result = robot.ServoMoveStart(cmdType=1)
            print("ServoMoveStart返回結果: {}".format(result))
            while count > 0:
                result = robot.ServoJ(joint_pos=j, axisPos=epos, acc=acc, vel=vel, cmdT=cmdT,filterT=filterT, gain=gain, id=cmdID, cmdType=1)
                j[0] -= dt
                j[1] -= dt
                j[2] -= dt
                j[3] -= dt
                j[4] -= dt
                j[5] -= dt
                count -= 1
                time.sleep(0.01)
            result = robot.ServoMoveEnd(cmdType=1)
            print("ServoMoveEnd返回結果: {}".format(result))
        robot.CloseRPC()
        return 0
    TestServoJUDP(robot)

關節空間伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j = [0.0] * 6
    epos = [0.0] * 4
    vel = 0.0
    acc = 0.0
    cmdT = 0.008
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 500
    dt = 0.1
    cmdID = 0
    ret, j = robot.GetActualJointPosDegree(flag)
    if ret == 0:
        cmdID += 1
        robot.ServoMoveStart()
        while count:
            robot.ServoJ(joint_pos=j,axisPos= epos,acc= acc,vel= vel, cmdT=cmdT, filterT=filterT, gain=gain, id=cmdID)
            j[4] += dt
            count -= 1
            time.sleep(cmdT)
            rtn,pkg = robot.GetRobotRealTimeState()
            print(f"Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")

            if count < 50:
                robot.MotionQueueClear()
                print(f"After queue clear, Servoj Count {pkg.servoJCmdNum}; last pos is {pkg.lastServoTarget[0]},{pkg.lastServoTarget[1]},{pkg.lastServoTarget[2]},{pkg.lastServoTarget[3]},{pkg.lastServoTarget[4]},{pkg.lastServoTarget[5]}")
                break
        robot.ServoMoveEnd()
    else:
        print(f"GetActualJointPosDegree errcode:{ret}")
    robot.CloseRPC()

關節扭矩控制開始
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJTStart(cmdType=0)``"
    "描述", "關節扭矩控制開始"
    "必選參數", "- ``cmdType``: 命令傳輸類型，0=XML-RPC，1=UDP透傳"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節扭矩控制
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJT(torque, interval, checkFlag=0, jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], cmdType=0)``"
    "描述", "關節扭矩控制"
    "必選參數", "- ``torque``:j1~j6關節扭矩，單位Nm
                - ``interval``:指令週期，單位s，範圍[0.001~0.008]
                - ``checkFlag``:檢測策略 0-不限制；1-限制功率；2-限制速度；3-功率和速度同時限制,默認0
                - ``jPowerLimit``:關節最大功率限制(W)，默認[0.0,0.0,0.0,0.0,0.0,0.0]
                - ``jVelLimit``:關節最大速度(°/s)，默認[0.0,0.0,0.0,0.0,0.0,0.0]
                - ``cmdType``:命令傳輸類型，0=XML-RPC，1=UDP透傳"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節扭矩控制結束
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJTEnd(cmdType=0)``"
    "描述", "關節扭矩控制結束"
    "必選參數", "- ``cmdType``: 命令傳輸類型，0=XML-RPC，1=UDP透傳"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

基於UDP通訊的ServoJT、ServoJTStart、ServoJTEnd SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def TestServoJTUDP(self):
        # 設置回調
        def callback(src_type, count, cmd_id, data_len, content):
            print("回調函數: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0

        robot.SetUDPCmdRpyCallback(callback)
        while True:
            # 初始化關節位置和外部軸位置
            j = [0, -90, 90, 0, 0, 0]
            epos = [0, 0, 0, 0]
            offset_pos = [0, 0, 0, 0, 0, 0]

            # 移動到初始位置
            robot.MoveJ(joint_pos=j, tool=0, user=0, vel=100, acc=100, ovl=100,
                        exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
            time.sleep(3)
            # 開啟拖動示教
            result=robot.DragTeachSwitch(1)
            print("DragTeachSwitch返回結果: {}".format(result))
            torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # 獲取關節力矩
            ret, torques = robot.GetJointTorques(flag=1)
            if ret != 0:
                print(f"GetJointTorques errcode:{ret}")

            count = 100
            result = robot.ServoJTStart(cmdType=1)
            print("ServoJTStart返回結果: {}".format(result))
            # 正向力矩控制
            while True:
                torques[0] = 0.03
                result = robot.ServoJT(
                    torque=torques,
                    interval=0.001,
                    checkFlag=0,
                    jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                    cmdType=1
                )
                print("返回結果: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] > 30:
                    break

            # 反向力矩控制
            while True:
                torques[0] = -0.03
                result = robot.ServoJT(
                        torque=torques,
                        interval=0.001,
                        checkFlag=0,
                        jPowerLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        jVelLimit=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        cmdType=1
                    )
                print("返回結果: {}".format(result))
                time.sleep(1)

                ret, pkg = robot.GetRobotRealTimeState()
                if pkg.jt_cur_pos[0] < 0:
                    break

            # 結束力矩控制並關閉拖動示教
            result = robot.ServoJTEnd(cmdType=1)
            print("ServoJTEnd返回結果: {}".format(result))
            result = robot.DragTeachSwitch(0)
            print("DragTeachSwitch返回結果: {}".format(result))

        robot.CloseRPC()
        return 0
    TestServoJTUDP(robot)

關節扭矩控制代碼示例
++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    # torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    error,torques = robot.GetJointTorques(1)
    robot.ServoJTStart()
    count = 100
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

具有超速保護的關節扭矩控制程式碼範例
++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    robot.ResetAllError()
    time.sleep(0.5)
    torques = [0.0] * 6
    rtn, torques = robot.GetJointTorques(1)
    robot.ServoJTStart()
    robot.DragTeachSwitch(1)
    checkFlag = 3
    jPowerLimit = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    jVelLimit = [181,80,80,80,80,80]
    count = 800000
    error = 0
    while count > 0:
        torques[2] = torques[2] + 0.01
        error = robot.ServoJT(torques, 0.008, checkFlag, jPowerLimit, jVelLimit)
        print(f"ServoJT rtn is {error}")
        count = count - 1
        time.sleep(0.001)
        rtn,pkg = robot.GetRobotRealTimeState()
        print(f"maincode {pkg.main_code},subcode {pkg.sub_code}")
    robot.DragTeachSwitch(0)
    error = robot.ServoJTEnd()

笛卡爾空間伺服模式運動
++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoCart(mode, desc_pos, exaxis, pos_gain=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0], acc=0.0, vel=0.0, cmdT=0.008,filterT=0.0, gain=0.0)``"
    "描述", "笛卡爾空間伺服模式運動"
    "必選參數", "- ``mode``:[0]-絕對運動(基座標系)，[1]-增量運動(基座標系)，[2]-增量運動(工具座標系)；
    - ``exaxis``:擴展軸位置；
    - ``desc_pos``:目標笛卡爾位置/目標笛卡爾位置增量；"
    "預設參數", "- ``pos_gain``:位姿增量比例係數，僅在增量運動下生效，範圍 [0~1], 預設為 [1.0, 1.0, 1.0, 1.0, 1.0, 1.0];
    - ``acc``:加速度，範圍 [0~100]，暫不開放，預設為 0.0;
    - ``vel``:速度，範圍 [0~100]，暫不開放，預設為 0.0;
    - ``cmdT``:指令下發週期，單位s，建議範圍[0.001~0.0016], 預設為0.008;
    - ``filterT``:濾波時間，單位 [s]，暫不開放， 預設為0.0;
    - ``gain``:目標位置的比例放大器，暫不開放， 預設為0.0;"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

笛卡爾空間伺服模式運動程式碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    desc_pos_dt = [83.00800, 50.525000, 29.246, 179.629, -7.138, -166.975]
    exaxis = [100.0, 0.0, 0.0, 0.0]
    pos_gain = [0.0] * 6
    mode = 0
    vel = 0.0
    acc = 0.0
    cmdT = 0.001
    filterT = 0.0
    gain = 0.0
    flag = 0
    count = 5000
    robot.SetSpeed(20)
    while count:
        rtn = robot.ServoCart(mode, desc_pos_dt, exaxis, pos_gain, acc, vel, cmdT, filterT, gain)
        print(f"ServoCart rtn is {rtn}")
        count -= 1
        desc_pos_dt[0] += 0.01
        exaxis[0] += 0.01
    robot.CloseRPC()
    return 0

樣條運動開始
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineStart()``"
    "描述", "樣條運動開始"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

樣條運動PTP
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplinePTP(joint_pos, tool, user, desc_pos = [0.0,0.0,0.0,0.0,0.0,0.0],  vel = 20.0,  acc = 100.0, ovl = 100.0)``"
    "描述", "樣條運動PTP"
    "必選參數", "- ``joint_pos``:目標關節位置，單位[°]；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``desc_pos``:目標笛卡爾位姿，單位 [mm][°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用正運動學求解返回值;
    - ``vel``:速度，範圍 [0~100]，默認爲 20.0;
    - ``acc``:加速度，範圍 [0~100]，默認爲 100.0;
    - ``ovl``:速度縮放因子，[0~100]，默認爲 100.0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

樣條運動結束
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineEnd()``"
    "描述", "樣條運動結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
樣條運動代碼示例
++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    joint_points = [
        [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256],  # j1
        [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255],  # j2
        [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260],  # j3
        [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]  # j4
    ]
    cart_points = [
        [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833],  # desc_pos1
        [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869],  # desc_pos2
        [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207],  # desc_pos3
        [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]  # desc_pos4
    ]
    offset_pos = [0] * 6 
    epos = [0] * 4 
    tool = user = 0
    vel = acc = ovl = 100.0 
    blendT = -1.0  
    flag = 0 
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=joint_points[0],tool=tool, user=user,vel=vel)
    print(f"MoveJ 錯誤碼: {err1}")
    robot.SplineStart()
    robot.SplinePTP(joint_pos=joint_points[0],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[1],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[2],tool=tool, user=user)
    robot.SplinePTP(joint_pos=joint_points[3],tool=tool, user=user)
    robot.SplineEnd()
    robot.CloseRPC()

新樣條運動開始
+++++++++++++++++++
.. versionchanged:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplineStart(type,averageTime=2000)``"
    "描述", "新樣條運動開始"
    "必選參數", "- ``type``:0-圓弧過渡，1-給定點位路徑點"
    "默認參數", "- ``averageTime``:全局平均銜接時間（ms）默認爲 2000"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

新樣條指令點
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplinePoint(desc_pos,tool,user,lastFlag,joint_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel = 0.0, acc = 0.0, ovl = 100.0 ,blendR = 0.0 )``"
    "描述", "新樣條指令點"
    "必選參數", "- ``desc_pos``:目標笛卡爾位姿，單位 [mm][°];
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；
    - ``lastFlag``:是否爲最後一個點，0-否，1-是;"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值爲[0.0,0.0,0.0,0.0,0.0,0.0]，默認值調用逆運動學求解返回值;
    - ``vel``:速度，範圍 [0~100]，暫不開放，默認爲 0.0;；
    - ``acc``:加速度，範圍 [0~100]，暫不開放，默認爲 0.0;
    - ``ovl``:速度縮放因子，[0~100] 默認爲 100.0;
    - ``blendR``: [0~1000]-平滑半徑，單位 [mm] 默認0.0;"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

新樣條運動結束
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``NewSplineEnd()``"
    "描述", "新樣條運動結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

新樣條運動代碼示例
++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    j3 = [-61.954, -84.409, 108.153, -116.316, -91.283, 74.260]
    j4 = [-89.575, -80.276, 102.713, -116.302, -91.284, 74.267]
    j5 = [-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_pos3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    desc_pos4 = [-104.066, 544.321, 327.023, -177.715, 3.371, -73.818]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    err1 = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    print(f"movej errcode:{err1}")
    robot.NewSplineStart(1, 2000)
    robot.NewSplinePoint(desc_pos=desc_pos1, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos2, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos3, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos4, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplinePoint(desc_pos=desc_pos5, tool=tool, user=user, vel=vel, lastFlag=-1, blendR=0)
    robot.NewSplineEnd()
    robot.CloseRPC()

機器人終止運動
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``StopMotion()``"
    "描述", "終止運動，使用終止運動需運動指令爲非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人暫停運動
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PauseMotion()``"
    "描述", "暫停運動，使用暫停運動需運動指令爲非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人恢復運動
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``ResumeMotion()``"
    "描述", "恢復運動，使用恢復運動需運動指令爲非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

運動暫停、恢復、停止代碼示例
++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 =[-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j5 =[-95.228, -54.621, 73.691, -112.245, -91.280, 74.268]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos5 = [-33.421, 732.572, 275.103, -177.907, 2.709, -79.482]
    offset_pos = [0, 0, 0, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    rtn = robot.MoveJ(joint_pos=j1, tool=tool, user=user, vel=vel)
    rtn = robot.MoveJ(joint_pos=j5, tool=tool, user=user, vel=vel, blendT=1)
    time.sleep(1)
    robot.PauseMotion()
    time.sleep(1)
    robot.ResumeMotion()
    time.sleep(1)
    robot.StopMotion()
    time.sleep(1)
    robot.CloseRPC()

點位整體偏移開始
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetEnable(flag,offset_pos)``"
    "描述", "點位整體偏移開始"
    "必選參數", "- ``flag``:0-基座標或工件座標系下偏移， 2-工具座標系下偏移；
    - ``offset_pos``:偏移量，單位[mm][°]。"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

點位整體偏移結束
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetDisable()``"
    "描述", "點位整體偏移結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

點位偏移代碼示例
+++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 100.0
    acc = 100.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    time.sleep(1)
    robot.PointsOffsetEnable(flag=0, offset_pos=offset_pos1)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.PointsOffsetDisable()
    robot.CloseRPC()

控制箱運動AO開始
+++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveAOStart(AONum,maxTCPSpeed=1000,maxAOPercent=100,zeroZoneCmp=20)``"
    "描述", "控制箱運動AO開始"
    "必選參數", "- ``AONum``:控制箱AO編號"
    "默認參數", "
    - ``maxTCPSpeed``:最大TCP速度值[1-5000mm/s]，默認1000；
    - ``maxAOPercent``:最大TCP速度值對應的AO百分比，默認100%；
    - ``zeroZoneCmp``:死區補償值AO百分比，整形，默認爲20%，範圍[0-100]。"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

控制箱運動AO結束
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveAOStop()``"
    "描述", "控制箱運動AO結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

末端運動AO開始
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveToolAOStart(AONum,maxTCPSpeed=1000,maxAOPercent=100,zeroZoneCmp =20)``"
    "描述", "末端運動AO開始"
    "必選參數", "- ``AONum``:末端AO編號"
    "默認參數", "
    - ``maxTCPSpeed``:最大TCP速度值[1-5000mm/s]，默認1000；
    - ``maxAOPercent``:最大TCP速度值對應的AO百分比，默認100%；
    - ``zeroZoneCmp``:死區補償值AO百分比，整形，默認爲20%，範圍[0-100]。"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

末端運動AO結束
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``MoveToolAOStop()``"
    "描述", "末端運動AO結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
      
AO飛拍代碼示例
+++++++++++++++++++++++

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_pos1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_pos2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    offset_pos = [0, 0, 0, 0, 0, 0]
    offset_pos1 = [0, 0, 50, 0, 0, 0]
    epos = [0, 0, 0, 0]
    tool = 0
    user = 0
    vel = 20.0
    acc = 20.0
    ovl = 100.0
    blendT = -1.0
    flag = 0
    robot.SetSpeed(20)
    robot.MoveAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveAOStop()
    time.sleep(1)
    robot.MoveToolAOStart(0, 100, 100, 20)
    robot.MoveJ(joint_pos=j1,tool=tool, user=user, vel=vel)
    robot.MoveJ(joint_pos=j2, tool=tool, user=user, vel=vel)
    robot.MoveToolAOStop()
    robot.CloseRPC()

開始Ptp運動FIR濾波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningStart(maxAcc, maxJek)``"
    "描述", "開始Ptp運動FIR濾波"
    "必選參數", "- ``maxAcc``:最大加速度極值(deg/s2)
    - ``maxJek``:統一關節急動度極值(deg/s3)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關閉Ptp運動FIR濾波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningEnd()``"
    "描述", "關閉Ptp運動FIR濾波"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

開始LIN、ARC運動FIR濾波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningStart(maxAccLin,maxAccDeg,maxJerkLin,maxJerkDeg)``"
    "描述", "開始LIN、ARC運動FIR濾波"
    "必選參數", "- ``maxAccLin``:線加速度極值(mm/s2)
    - ``maxAccDeg``:角加速度極值(deg/s2)
    - ``maxJerkLin``:線加加速度極值(mm/s3)
    - ``maxJerkDeg``:角加加速度極值(deg/s3)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關閉LIN、ARC運動FIR濾波
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningEnd()``"
    "描述", "關閉LIN、ARC運動FIR濾波"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"   

FIR濾波代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    midjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    endjointPos = [-29.777, -84.536, 109.275, -114.075, -86.655, 74.257]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    middescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    enddescPose = [-487.434, 154.362, 308.576, 176.600, 0.268, -14.061]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.PtpFIRPlanningStart(1000.0, 1000.0)
    print(f"PtpFIRPlanningStart rtn is {rtn}")
    error = robot.MoveJ(joint_pos=startjointPos,tool= 0,user= 0,desc_pos=startdescPose,vel= 100,acc=100,ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    error = robot.MoveJ(joint_pos=endjointPos,tool= 0,user= 0,desc_pos=enddescPose,vel= 100,acc=100,ovl=100, blendT=-1.0, offset_flag=0)
    print(f"MoveJ rtn is {rtn}")
    robot.PtpFIRPlanningEnd()
    print(f"PtpFIRPlanningEnd rtn is {rtn}")
    rtn = robot.LinArcFIRPlanningStart(1000, 1000, 1000, 1000)
    print(f"LinArcFIRPlanningStart rtn is {rtn}")
    error = robot.MoveL(desc_pos=startdescPose,tool= 0,user= 0, joint_pos=startjointPos,vel= 100,overSpeedStrategy=1,speedPercent=1)
    print(f"MoveL rtn is {rtn}")
    error = robot.MoveC(desc_pos_p=middescPose,tool_p= 0,user_p= 0, joint_pos_p=midjointPos,vel_p= 100,desc_pos_t=enddescPose,tool_t= 0,user_t= 0,joint_pos_t=endjointPos,vel_t= 100)
    print(f"MoveC rtn is {rtn}")
    robot.LinArcFIRPlanningEnd()
    print(f"LinArcFIRPlanningEnd rtn is {rtn}")
    robot.CloseRPC()

加速度平滑開啓
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothStart(saveFlag_flag)``"
    "描述", "加速度平滑開啓"
    "必選參數", "- ``saveFlag_flag``：是否斷電保存"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

加速度平滑關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothEnd(saveFlag_flag)``"
    "描述", "加速度平滑關閉"
    "必選參數", "- ``saveFlag_flag``：是否斷電保存"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

加速度平滑代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AccSmoothStart(0)
    print(f"AccSmoothStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos,tool= 0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos,tool= 0,user= 0,vel= 100)
    rtn = robot.AccSmoothEnd(0)
    print(f"AccSmoothEnd rtn is {rtn}")

設置機器指定姿態速度開啓
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedStart(ratio)``"
    "描述", "指定姿態速度開啓"
    "必選參數", "- ``ratio``:姿態速度百分比[0-300]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

指定姿態速度關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedEnd()``"
    "描述", "指定姿態速度關閉"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

機器人指定姿態速度代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.AngularSpeedStart(50)
    print(f"AngularSpeedStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos, tool=0,user= 0,vel= 100)
    rtn = robot.AngularSpeedEnd()
    print(f"AngularSpeedEnd rtn is {rtn}")
    robot.CloseRPC()

奇異位姿保護開啓
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SingularAvoidStart(protectMode, minShoulderPos=100, minElbowPos=50, minWristPos=10)``"
    "描述", "開啓奇異位姿保護"
    "必選參數", "
    - ``protectMode``：奇異位姿保護保護模式：0-關節模式；1-笛卡爾模式
    "
    "默認參數", "- ``minShoulderPos``：肩奇異調整範圍(mm), 默認100.0
    - ``minElbowPos``：肘奇異調整範圍(mm), 默認50.0
    - ``minWristPos``：腕奇異調整範圍(°), 默認10.0"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

奇異位姿保護關閉
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SingularAvoidEnd()``"
    "描述", "關閉奇異位姿保護"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

機器人奇異位姿保護代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startjointPos = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    endjointPos = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    startdescPose = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    enddescPose = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    rtn = robot.SingularAvoidStart(2, 10, 5, 5)
    print(f"SingularAvoidStart rtn is {rtn}")
    robot.MoveJ(joint_pos=startjointPos, tool=0,user= 0,vel= 100)
    robot.MoveJ(joint_pos=endjointPos, tool=0,user= 0,vel= 100)
    rtn = robot.SingularAvoidEnd()
    print(f"SingularAvoidEnd rtn is {rtn}")
    robot.CloseRPC()

清空運動指令隊列
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MotionQueueClear()``"
    "描述", "清空運動指令隊列"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

清空運動指令佇列
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveToIntersectLineStart(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveType,mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],extAxisFlag=0,exaxisPos=[0.0,0.0,0.0,0.0],moveDirection=0,offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "清空運動指令佇列"
    "必選參數", "
    - ``mainPoint``：主管6個示教點的笛卡爾位姿
    - ``piecePoint``：支管6個示教點的笛卡爾位姿
    - ``tool``：工具座標系編號
    - ``wobj``：工件座標系編號
    - ``vel``：速度百分比
    - ``acc``：加速度百分比
    - ``ovl``：速度縮放因子
    - ``oacc``：加速度縮放因子
    - ``moveType``：運動類型; 0-PTP；1-LIN
    - ``mainExaxisPos``：主管6個示教點擴展軸位置,預設[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``：支管6個示教點擴展軸位置,預設[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``：是否啟用擴展軸；0-不啟用；1-啟用
    - ``exaxisPos``：起點擴展軸位置[0.0,0.0,0.0,0.0]
    - ``moveDirection``：運動方向；0-順時針；1-逆時針
    - ``offset``：偏移量
    "
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0 失敗- errcode"

相貫線運動
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveIntersectLine(mainPoint, piecePoint, tool, wobj, vel, acc, ovl, oacc, moveDirection,mainExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],pieceExaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],extAxisFlag=0,exaxisPos=[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]],offset=[0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "相貫線運動"
    "必選參數", "
    - ``mainPoint``：主管6個示教點的笛卡爾位姿
    - ``piecePoint``：支管6個示教點的笛卡爾位姿
    - ``tool``：工具座標系編號
    - ``wobj``：工件座標系編號
    - ``vel``：速度百分比
    - ``acc``：加速度百分比
    - ``ovl``：速度縮放因子
    - ``oacc``：加速度縮放因子
    - ``moveDirection``：運動方向；0-順時針；1-逆時針
    - ``mainExaxisPos``：主管6個示教點擴展軸位置,預設[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``pieceExaxisPos``：支管6個示教點擴展軸位置,預設[[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    - ``extAxisFlag``：是否啟用擴展軸；0-不啟用；1-啟用
    - ``exaxisPos``：起點擴展軸位置[0.0,0.0,0.0,0.0]
    - ``offset``：偏移量
    "
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0 失敗- errcode"

機器人相貫線運動程式碼範例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    mainPoint = [[0.0] * 6 for _ in range(6)]
    piecePoint = [[0.0] * 6 for _ in range(6)]
    mainExaxisPos = [[0.0] * 4 for _ in range(6)]
    pieceExaxisPos = [[0.0] * 4 for _ in range(6)]
    extAxisFlag = 1
    exaxisPos = [[0.0] * 4 for _ in range(4)]
    offset = [0.0, 2.0, 30.0, -2.0, 0.0, 0.0]
    mainPoint[0] = [490.004, -383.194, 402.735, -9.332, -1.528, 69.594]
    mainPoint[1] = [444.950, -407.117, 389.011, -5.546, -2.196, 65.279]
    mainPoint[2] = [445.168, -463.605, 355.759, -1.544, -10.886, 57.104]
    mainPoint[3] = [507.529, -485.385, 343.013, -0.786, -4.834, 61.799]
    mainPoint[4] = [554.390, -442.647, 367.701, -4.761, -10.181, 64.925]
    mainPoint[5] = [532.552, -394.003, 396.467, -13.732, -13.592, 67.411]
    mainExaxisPos[0] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[1] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[2] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[3] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[4] = [-29.996, 0.000, 0.000, 0.000]
    mainExaxisPos[5] = [-29.996, 0.000, 0.000, 0.000]
    piecePoint[0] = [505.571, -192.408, 316.759, 38.098, 37.051, 139.447]
    piecePoint[1] = [533.837, -201.558, 332.340, 34.644, 42.339, 137.748]
    piecePoint[2] = [530.386, -225.085, 373.808, 35.431, 45.111, 137.560]
    piecePoint[3] = [485.646, -229.195, 383.778, 33.870, 45.173, 137.064]
    piecePoint[4] = [460.551, -212.161, 354.256, 28.856, 45.602, 135.930]
    piecePoint[5] = [474.217, -197.124, 324.611, 42.469, 41.133, 148.167]
    pieceExaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[1] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[2] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[3] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[4] = [-29.996, -0.000, 0.000, 0.000]
    pieceExaxisPos[5] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[0] = [-29.996, -0.000, 0.000, 0.000]
    exaxisPos[1] = [-44.994, 90.000, 0.000, 0.000]
    exaxisPos[2] = [-59.992, 0.002, 0.000, 0.000]
    exaxisPos[3] = [-44.994, -89.997, 0.000, 0.000]
    tool = 2
    wobj = 0
    vel = 100.0
    acc = 100.0
    ovl = 12.0
    oacc = 12.0
    moveType = 1
    moveDirection = 1
    rtn = robot.MoveToIntersectLineStart(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag,exaxisPos=exaxisPos[0], tool=tool, wobj=wobj, vel=vel, acc=acc, ovl=ovl, oacc=oacc, moveType=moveType, moveDirection=moveDirection, offset=offset)
    print(f"MoveToIntersectLineStart rtn is {rtn}")
    rtn = robot.MoveIntersectLine(mainPoint=mainPoint, mainExaxisPos=mainExaxisPos, piecePoint=piecePoint, pieceExaxisPos=pieceExaxisPos, extAxisFlag=extAxisFlag, exaxisPos=exaxisPos, tool=tool,wobj=wobj, vel=vel, acc=acc, ovl=5.0, oacc=5.0, moveDirection=moveDirection, offset=offset)
    print(f"MoveIntersectLine rtn is {rtn}")
    robot.CloseRPC()

原地空運動
+++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveStationary()``"
    "描述", "原地空運動"
    "必選參數", "無"
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"
 
原地空運動程式碼範例
+++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.LaserSensorRecordandReplay(0, 10, 1, 0, 0.1, 1, 0, 10, 100)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    rtn = robot.MoveStationary()
    print(f"MoveStationary rtn is {rtn}")
    rtn = robot.LaserSensorRecord1(0, 10)
    print(f"LaserSensorRecordandReplay rtn is {rtn}")
    robot.CloseRPC()
    return 0

定點擺動開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OriginPointWeaveStart(weaveNum, mode, refPoint, weaveTime)``"
    "描述", "定點擺動開始"
    "必選參數", "
    - ``weaveNum``:擺動編號[0-7]
    - ``mode``:0-工具座標系；1-參考點
    - ``refPoint``:參考點笛卡爾座標[x,y,z,a,b,c]
    - ``weaveTime``:擺動時間[s]
    - "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

定點擺動結束
+++++++++++++++++++++++++++++++++
    
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``OriginPointWeaveEnd()``"
    "描述", "定點擺動結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

定點擺動的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def TestOriginPointWeave(self):
        time.sleep(2)
        # 初始化關節位置、外部軸和偏移
        j = [39.886, -98.580, -124.032, -47.393, 90.000, 40.842]
        epos = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]

        # 參考點位置 [x, y, z, rx, ry, rz]
        refPoint = [400.021, 300.022, 299.996, 179.997, -0.003, -90.956]

        # 移動到起始位置
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 第一次擺動：絕對座標系（tool=0），模式0
        robot.OriginPointWeaveStart(0, 0, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        time.sleep(2)

        # 再次移動到起始位置
        robot.MoveJ(joint_pos=j, tool=1, user=0, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        # 第二次擺動：絕對座標系（tool=0），模式1
        robot.OriginPointWeaveStart(0, 1, refPoint, 3)
        robot.MoveStationary()
        robot.OriginPointWeaveEnd()

        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)

    TestOriginPointWeave(robot)

定點擺動（包含雷射及擴展軸）的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def TestOriginPointWeave(self):
        time.sleep(2)
        # 初始化關節位置、外部軸和偏移
        j = [39.886, -98.580, -124.032, -47.393, 90.000, 40.842]
        epos1 = [0, 0, 0, 0]
        offset_pos = [0, 0, 0, 0, 0, 0]
        epos2 = [5, 0.000, 0.000, 0.000]
        # 參考點位置 [x, y, z, rx, ry, rz]
        refPoint = [400.021, 300.022, 299.996, 179.997, -0.003, -90.956]

        rtn = 0
        robot.LaserTrackingSensorConfig("192.168.58.20", 5020)
        robot.LaserTrackingSensorSamplePeriod(20)
        robot.LoadPosSensorDriver(101)

        # 載入 UDP 驅動
        robot.ExtDevLoadUDPDriver()

        # 設置外部軸命令完成時間
        rtn = robot.SetExAxisCmdDoneTime(5000.0)
        print(f"SetExAxisCmdDoneTime rtn is {rtn}")

        # 使能外部軸 1 和 2
        rtn = robot.ExtAxisServoOn(1, 1)
        print(f"ExtAxisServoOn axis id 1 rtn is {rtn}")
        rtn = robot.ExtAxisServoOn(2, 1)
        print(f"ExtAxisServoOn axis id 2 rtn is {rtn}")
        time.sleep(2)

        # 設置外部軸回零
        robot.ExtAxisSetHoming(1, 0, 10, 2)
        robot.LaserTrackingLaserOnOff(1)

        # 1---不帶擴展軸
        robot.LaserTrackingTrackOnOff(1, 4)
        time.sleep(0.2)
        # 啟動定點擺動
        robot.OriginPointWeaveStart(0, 0, refPoint, 10)
        robot.MoveStationary()  # 執行固定運動（假設該方法存在）
        robot.OriginPointWeaveEnd()
        robot.LaserTrackingTrackOnOff(0, 4)

        time.sleep(2)  # 等待2秒

        # 2----帶擴展軸
        robot.ExtAxisMove(epos1, 100, -1)
        robot.LaserTrackingTrackOnOff(1, 4)
        # 啟動定點擺動
        robot.OriginPointWeaveStart(0, 0, refPoint, 20)
        robot.ExtAxisMove(epos2, 100, -1)
        robot.OriginPointWeaveEnd()
        robot.LaserTrackingTrackOnOff(0, 4)

        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)

    TestOriginPointWeave(robot)

關節空間速度伺服模式運動
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJV(self, joint_vel, exis_vel, acc=0.0, vel=0.0, cmdT=0.008, filterT=0.0, gain=0.0, id=0, comType=0)``"
    "描述", "關節空間速度伺服模式運動"
    "必選參數", "
    - ``joint_vel``:6個目標關節速度，單位deg/s
    - ``exis_vel``:4個外部軸速度，單位deg/s
    - ``acc``: 加速度百分比，範圍[0~100]，暫不開放，預設為0
    - ``vel``:速度百分比，範圍[0~100]，暫不開放，預設為0
    - ``cmdT``:指令下發週期，單位s，建議範圍[0.001~0.0016]
    - ``filterT``:濾波時間，單位s，暫不開放，預設為0
    - ``gain``:目標位置的比例放大器，暫不開放，預設為0
    - ``id``:servoJ指令ID，預設為0
    - ``comType``:指令下發類型；0-xmlrpc；1-UDP(對應機器人20007埠)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節空間速度伺服模式運動代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time

    def main():
        # 與機器人控制器建立連接
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  # 等待連接和數據接收

        # 初始化關節速度數組和擴展軸速度數組
        joint_vel = [10.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        exis_vel = [0.0, 0.0, 0.0, 0.0]
        acc = 0.0
        vel = 0.0
        cmdT = 0.008
        filterT = 0.0
        gain = 0.0
        cnt = 0

        # 循環調用ServoJV，共200次
        while cnt < 200:
            rtn = robot.ServoJV(joint_vel=joint_vel, exis_vel=exis_vel, acc=acc, vel=vel,
                                cmdT=cmdT, filterT=filterT, gain=gain)
            print(f"ServoJV rtn is {rtn}")
            cnt += 1

        # 關閉連接
        robot.CloseRPC()


    # 調用測試函數
    main()

關節MIT控制開始
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMITStart(self, comType=0)``"
    "描述", "關節MIT控制開始"
    "必選參數", "
    - ``comType``:指令下發類型；0-xmlrpc；1-UDP(對應機器人20007埠)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節MIT控制結束
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMITEnd(self, comType=0)``"
    "描述", "關節MIT控制結束"
    "必選參數", "
    - ``comType``:指令下發類型；0-xmlrpc；1-UDP(對應機器人20007埠)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節MIT控制
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMIT(self, posGain, desPos, velGain, desVel, torque_ff, interval, comType=0)``"
    "描述", "關節MIT控制"
    "必選參數", "
    - ``posGain``:j1~j6關節位置增益
    - ``desPos``:j1~j6關節期望位置 單位:deg
    - ``velGain``:j1~j6關節速度增益
    - ``desVel``:j1~j6關節期望速度 單位:deg/s
    - ``torque_ff``:j1~j6前饋力矩 單位:Nm
    - ``interval``:指令週期，單位s，範圍[0.001~0.008]
    - ``comType``:指令下發類型；0-xmlrpc；1-UDP(對應機器人20007埠)
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人關節MIT控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: python
    :linenos: 

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    # 定義回調函數
    def udp_frame_callback(src_type, count, cmd_id, data_len, content):
        """UDP命令響應回調函數"""
        print(f"回調函數: cmd_id={cmd_id} count={count} data_len={data_len} content={content}")
        return 0

    def ServoMITtest(self):
        # 設置UDP命令響應回調
        robot.SetUDPCmdRpyCallback(udp_frame_callback)

        while True:
            # 復位所有錯誤
            robot.ResetAllError()
            time.sleep(0.5)

            # 初始化參數數組
            posGain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            desPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            velGain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            desVel = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            torques = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            # 獲取關節力矩
            rtn, torques = robot.GetJointTorques(flag=1)
            print(f"GetJointTorques rtn: {rtn}")
            print("111111")

            # 啟動Servo MIT模式
            rtn = robot.ServoMITStart(0)
            print(f"ServoMITStart rtn: {rtn}")

            # 開啟拖動示教
            rtn = robot.DragTeachSwitch(1)
            print(f"DragTeachSwitch rtn: {rtn}")

            intev = 0.008

            # 正向運動：第6軸正向力矩，直到角度超過30度
            while True:
                torques[5] = 0.03
                rtn = robot.ServoMIT(posGain, desPos, velGain,
                                    desVel, torques, intev, comType=0)
                print(f"ServoMIT call rtn is {rtn}")
                time.sleep(0.001)  # 1ms

                rtn, pkg = robot.GetRobotRealTimeState()
                print(f"pkg.jt_cur_pos[5]: {pkg.jt_cur_pos[5]}")

                if pkg.jt_cur_pos[5] > 30:
                    break

            # 反向運動：第6軸負向力矩，直到角度小於0度
            while True:
                torques[5] = -0.03
                rtn = robot.ServoMIT(posGain, desPos, velGain,
                                    desVel, torques, intev, comType=0)
                print(f"ServoMIT call rtn is {rtn}")
                time.sleep(0.001)  # 1ms

                rtn, pkg = robot.GetRobotRealTimeState()
                print(f"pkg.jt_cur_pos[5]: {pkg.jt_cur_pos[5]}")

                if pkg.jt_cur_pos[5] < 0:
                    break

            # 關閉拖動示教
            rtn = robot.DragTeachSwitch(0)
            print(f"DragTeachSwitch off rtn: {rtn}")

            # 結束Servo MIT模式
            rtn = robot.ServoMITEnd(0)
            print(f"ServoMITEnd rtn: {rtn}")

    # 調用測試函數
    ServoMITtest(robot)