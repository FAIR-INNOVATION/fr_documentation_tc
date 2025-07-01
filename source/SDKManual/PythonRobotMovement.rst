機器人運動
============

.. toctree:: 
    :maxdepth: 5

機器人點動
+++++++++++++

jog點動
---------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StartJOG(ref,nb,dir,max_dis,vel=20.0,acc=100.0)``"
    "描述", "jog點動"
    "必選參數", "- ``ref``：0-關節點動,2-基坐標系點動,4-工具座標系點動,8-工件座標系點動；
    - ``nb``：1-1關節(x軸),2-2關節(y軸),3-3關節(z軸),4-4關節(rx),5-5關節(ry),6-6關節(rz);
    - ``dir``：0-負方向，1-正方向;
    - ``max_dis``：單次點動最大角度/距离，單位 ° 或 mm;"
    "默認參數", "- ``vel``：速度百分比，[0~100] 默認20;
    - ``acc``：加速度百分比，[0~100] 默認100;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

jog點動减速停止
-----------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``StopJOG(ref)``"
    "描述", "jog點動减速停止"
    "必選參數", "- ``ref``：1-關節點動停止,3-基坐標系點動停止,5-工具座標系點動停止,9-工件座標系點動停止"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

jog點動立即停止
-----------------

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ImmStopJOG()``"
    "描述", "jog點動立即停止"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    # 機器人單軸點動
    robot.StartJOG(0,1,0,20.0,20.0,30.0)    # 單關節運動,StartJOG為非阻塞指令，運動狀態下接收其他運動指令（包含StartJOG）会被丢弃
    time.sleep(1)
    #機器人單軸點動減速停止
    ret = robot.StopJOG(1)
    print(ret)
    #機器人單軸點動立即停止
    robot.ImmStopJOG()
    robot.StartJOG(0,2,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(0,3,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(0,4,1,20.0,vel=40)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(0,5,1,20.0,acc=50)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(0,6,1,20.0,20.0,30.0)
    time.sleep(1)
    robot.ImmStopJOG()
    # 基坐標
    robot.StartJOG(2,1,0,20.0)  #基座標系下點動
    time.sleep(1) 
    # #機器人單軸點動立即停止
    robot.ImmStopJOG()
    robot.StartJOG(2,1,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(2,2,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(2,3,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(2,4,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(2,5,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(2,6,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    # 工具座標
    robot.StartJOG(4,1,0,20.0,20.0,100.0)  #工具座標系下點動
    time.sleep(1)
    # #機器人單軸點動立即停止
    robot.ImmStopJOG()
    robot.StartJOG(4,1,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(4,2,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(4,3,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(4,4,1,20.0,20.0,100.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(4,5,1,20.0,vel=10.0,acc=20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(4,6,1,20.0,acc=40.0)
    time.sleep(1)
    robot.ImmStopJOG()
    # 工件座標
    robot.StartJOG(8,1,0,20.0,20.0,100.0)  #工件座標系下點動
    time.sleep(1)
    # #機器人單軸點動立即停止
    robot.ImmStopJOG()
    robot.StartJOG(8,1,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(8,2,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(8,3,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(8,4,1,20.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(8,5,1,20.0,vel=30.0)
    time.sleep(1)
    robot.ImmStopJOG()
    robot.StartJOG(8,6,1,20.0,20.0,acc=90.0)
    time.sleep(1)
    robot.ImmStopJOG()

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
    "默認參數", "- ``desc_pos``:目標笛卡兒位姿，單位 [mm][°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用正運動學求解傳回值;
    - ``vel``:速度百分比，[0~100] 默認20.0;
    - ``acc``:加速度百分比，[0~100]，暫不開放；
    - ``ovl``:速度縮放因子，[0~100] 預設100.0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``blendT``:[-1.0]-運動到位 (阻塞)，[0~500.0]-平滑時間 (非阻塞)，單位 [ms] 默認-1.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``offset_pos``:位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0];"
    "傳回值", "錯誤碼  成功-0  失败- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    joint_pos4 = [-83.24, -96.476, 93.688, -114.079, -62, -100]
    joint_pos5 = [-43.24, -70.476, 93.688, -114.079, -62, -80]
    joint_pos6 = [-83.24, -96.416, 43.188, -74.079, -80, -10]
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    ret = robot.MoveJ(joint_pos4, tool, user, vel=30)   #關節空間運動
    print("關節空間運動點4:錯誤碼", ret)
    ret = robot.MoveJ(joint_pos5, tool, user)
    print("關節空間運動點5:錯誤碼", ret)
    robot.MoveJ(joint_pos6, tool, user, offset_flag=1, offset_pos=[10,10,10,0,0,0])
    print("關節空間運動點6:錯誤碼", ret)

笛卡兒空間直線運動
+++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveL(desc_pos, tool, user, joint_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0 , ovl = 100.0, blendR = -1.0, exaxis_pos = [0.0,0.0,0.0,0.0], search = 0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0],overSpeedStrategy=0,speedPercent=10)``"
    "描述", "笛卡兒空間直線運動"
    "必選參數", "- ``desc_pos``:目標笛卡兒位姿，單位[mm][°]；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``vel``:速度百分比，[0~100] 默認20.0；
    - ``acc``:加速度百分比，[0~100]，暫不開放 默認0.0；
    - ``ovl``:速度縮放因子，[0~100] 預設100.0；
    - ``blendR``:blendR:[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，單位 [mm] 默認-1.0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``search``:[0]-不焊丝寻位，[1]-焊丝寻位；
    - ``offset_flag``:offset_flag:[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``offset_pos``:位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]
    - ``overSpeedStrategy``:超速处理策略，0-策略關閉；1-标准；2-超速时报错停止；3-自适应降速，默認為0
    - ``speedPercent``:允許降速閾值百分比[0-100]，預設為10%
    "
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos1 = [36.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos2 = [136.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos3 = [236.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    ret = robot.MoveL(desc_pos1, tool, user)   #笛卡兒空間直線運動
    print("笛卡兒空間直線運動點1:錯誤碼", ret) 
    robot.MoveL(desc_pos2, tool, user, vel=20, acc=100)
    print("笛卡兒空間直線運動點2:錯誤碼", ret) 
    robot.MoveL(desc_pos3, tool, user, offset_flag=1, offset_pos=[10,10,10,0,0,0])
    print("笛卡兒空間直線運動點3:錯誤碼", ret)

笛卡兒空間圓弧運動
++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveC(desc_pos_p, tool_p, user_p, desc_pos_t, tool_t, user_t, joint_pos_p =[0.0,0.0,0.0, 0.0,0.0,0.0],joint_pos_t=[0.0,0.0,0.0,0.0,0.0,0.0], vel_p = 20.0,acc_p=100.0, exaxis_pos_p =[0.0,0.0,0.0,0.0], offset_flag_p = 0, offset_pos_p = [0.0,0.0,0.0,0.0,0.0,0.0], vel_t= 20.0, acc_t=100.0,exaxis_pos_t=[0.0,0.0,0.0,0.0], offset_flag_t = 0, offset_pos_t = [0.0,0.0,0.0, 0.0,0.0,0.0], ovl = 100.0, blendR = -1.0)``"
    "描述", "笛卡兒空間圓弧運動"
    "必選參數", "- ``desc_pos_p``:路徑點笛卡爾位姿，單位[mm][°]；
    - ``tool_p``:路徑點工具號，[0~14];
    - ``user_p``:路徑點工件號，[0~14];
    - ``desc_pos_t``:目標點笛卡爾位姿，單位 [mm][°];
    - ``tool_t``:工具號，[0~14]；
    - ``user_t``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos_p``:路徑點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``joint_pos_t``:目標點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``vel_p``:路徑點速度百分比，[0~100] 默認20.0;
    - ``acc_p``:路徑點加速度百分比，[0~100] 暫不開放,默認0.0;
    - ``exaxis_pos_p``:路徑點外部軸 1位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``offset_flag_p``:路徑點是否偏移[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``vel_t``:目標點速度百分比，[0~100] 默認20.0;
    - ``acc_t``:目標點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_t``:目標點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``offset_flag_t``:目標點是否偏移[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``offset_pos_t``:目標點位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0];
    - ``ovl:``:速度縮放因子，[0~100] 預設100.0;
    - ``blendR``:[-1.0]-運動到位 (阻塞)，[0~1000]-平滑半径 (非阻塞)，單位 [mm] 默認-1.0;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos1 = [236.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_posc1 = [266.794,-455.119, 65.379, -176.938, 2.535, -179.829] #MoveC过渡點
    desc_posc2 = [286.794,-475.119, 65.379, -176.938, 2.535, -179.829]  #MoveC目標點
    tool = 0#工具座標系編號
    user = 0 #工件座標系編號
    ret = robot.MoveL(desc_pos1, tool, user, vel=30, acc=100)
    print("笛卡兒空間直線運動:錯誤碼", ret) 
    ret = robot.MoveC(desc_posc1, tool, user, desc_posc2,tool, user)  #笛卡兒空間圓弧運動
    print("笛卡兒空間圓弧運動:錯誤碼", ret)

笛卡兒空間整圓運動
+++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``Circle(desc_pos_p,tool_p,user_p,desc_pos_t,tool_t,user_t,joint_pos_p=[0.0,0.0,0.0,0.0,0.0,0.0], joint_pos_t = [0.0,0.0,0.0,0.0,0.0,0.0], vel_p = 20.0, acc_p=0.0, exaxis_pos_p= [0.0,0.0, 0.0,0.0], vel_t=20.0, acc_t = 0.0, exaxis_pos_t =[0.0,0.0,0.0,0.0], ovl=100.0, offset_flag=0, offset_pos= [0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "笛卡兒空間整圓運動"
    "必選參數", "- ``desc_pos_p``:路徑點笛卡爾位姿，單位[mm][°]；
    - ``tool_p``:工具號，[0~14]；
    - ``user_p``:工件號，[0~14]；
    - ``desc_pos_t``:目標點笛卡爾位姿，單位[mm][°]；
    - ``tool_t``:工具號，[0~14]；
    - ``user_t``:工件號，[0~14]；"
    "默認參數", "- ``joint_pos_p``:路徑點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``joint_pos_t``:目標點關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``vel_p``:速度百分比，[0~100] 默認20.0;
    - ``acc_p``:路徑點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_p``:路徑點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``vel_t``:目標點速度百分比，[0~100] 默認20.0;
    - ``acc_t``:目標點加速度百分比，[0~100] 暫不開放 默認0.0;
    - ``exaxis_pos_t``:标點外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0]
    - ``ovl``:速度縮放因子，[0~100] 預設100.0;
    - ``offset_flag``:是否偏移[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``offset_pos``:位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    middescPoseCir1 = [-435.414, -342.926, 309.205, -171.382, -4.513, 171.520]
    midjointPosCir1 = [26.804, -79.866, 106.642, -125.433, -85.562, -54.721]
    enddescPoseCir1 = [-524.862, -217.402, 308.459, -171.425, -4.810, 156.088]
    endjointPosCir1 = [11.399, -78.055, 104.603, -125.421, -85.770, -54.721]
    middescPoseCir2 = [-482.691, -587.899, 318.594, -171.001, -4.999, -172.996]
    midjointPosCir2 = [42.314, -53.600, 67.296, -112.969, -85.533, -54.721]
    enddescPoseCir2 = [-403.942, -489.061, 317.038, -163.189, -10.425, -175.627]
    endjointPosCir2 = [39.959, -70.616, 96.679, -134.243, -82.276, -54.721]
    middescPoseMoveC = [-435.414, -342.926, 309.205, -171.382, -4.513, 171.520]
    midjointPosMoveC = [26.804, -79.866, 106.642, -125.433, -85.562, -54.721]
    enddescPoseMoveC = [-524.862, -217.402, 308.459, -171.425, -4.810, 156.088]
    endjointPosmoveC = [11.399, -78.055, 104.603, -125.421, -85.770, -54.721]
    middescPoseCir3 = [-435.414, -342.926, 309.205, -171.382, -4.513, 171.520]
    midjointPosCir3 = [26.804, -79.866, 106.642, -125.433, -85.562, -54.721]
    enddescPoseCir3 = [-569.505, -405.378, 357.596, -172.862, -10.939, 171.108]
    endjointPosCir3 = [27.138, -63.750, 78.586, -117.861, -90.588, -54.721]
    middescPoseCir4 = [-482.691, -587.899, 318.594, -171.001, -4.999, -172.996]
    midjointPosCir4 = [42.314, -53.600, 67.296, -112.969, -85.533, -54.721]
    enddescPoseCir4 = [-569.505, -405.378, 357.596, -172.862, -10.939, 171.108]
    endjointPosCir4 = [27.138, -63.750, 78.586, -117.861, -90.588, -54.721]
    startdescPose = [-569.505, -405.378, 357.596, -172.862, -10.939, 171.108]
    startjointPos = [27.138, -63.750, 78.586, -117.861, -90.588, -54.721]
    linedescPose = [-403.942, -489.061, 317.038, -163.189, -10.425, -175.627]
    linejointPos = [39.959, -70.616, 96.679, -134.243, -82.276, -54.721]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    robot.MoveJ(joint_pos=startjointPos, tool=3, user=0, vel=100)
    robot.Circle(desc_pos_p=middescPoseCir1, tool_p=3, user_p=0, vel_p=100, desc_pos_t=enddescPoseCir1, tool_t=3,user_t=0, vel_t=100, offset_flag=-1,oacc=100, blendR=20)
    robot.Circle(desc_pos_p=middescPoseCir2, tool_p=3, user_p=0, vel_p=100, desc_pos_t=enddescPoseCir2, tool_t=3,user_t=0, vel_t=100, offset_flag=-1,oacc=100, blendR=20)
    robot.MoveC(desc_pos_p=middescPoseMoveC, tool_p=3, user_p=0, vel_p=100,desc_pos_t=enddescPoseMoveC,tool_t=3,user_t=0,vel_t=100, blendR=20)
    robot.Circle(desc_pos_p=middescPoseCir3, tool_p=3, user_p=0, vel_p=100, desc_pos_t=enddescPoseCir3, tool_t=3,user_t=0, vel_t=100, offset_flag=-1,oacc=100, blendR=20)
    robot.MoveL(desc_pos=linedescPose, tool=3, user=0, vel=100,blendMode=0)
    robot.Circle(desc_pos_p=middescPoseCir4, tool_p=3, user_p=0, vel_p=100, desc_pos_t=enddescPoseCir4, tool_t=3,user_t=0, vel_t=100, offset_flag=-1,oacc=100, blendR=20)

笛卡兒空間螺旋線運動
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSpiral(desc_pos, tool, user, param, joint_pos = [0.0,0.0,0.0,0.0,0.0,0.0], vel = 20.0, acc = 0.0, exaxis_pos = [0.0,0.0,0.0,0.0], ovl = 100.0, offset_flag = 0, offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0])``"
    "描述", "笛卡兒空間螺旋線運動"
    "必選參數", "- ``desc_pos``:目標笛卡兒位姿，單位[mm][°];
    - ``tool``:工具號，[0~14];
    - ``user``:工件號，[0~14];
    - ``param=[circle_num, circle_angle, rad_init, rad_add, rotaxis_add, rot_direction]``：circle_num: 螺旋圈數;circle_angle: 螺旋傾角;rad_init: 螺旋初始半径;rad_add: 半徑增量;rotaxis_add: 轉軸方向增量;rot_direction: 旋轉方向，0-順時針，1-逆時針;"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``vel``:速度百分比，[0~100] 默認20.0;
    - ``acc``:加速度百分比，[0~100] 默認100.0;
    - ``exaxis_pos``:外部軸 1 位置 ~ 外部軸 4 位置 默認[0.0,0.0,0.0,0.0];
    - ``ovl``:速度縮放因子，[0~100] 預設100.0;
    - ``offset_flag``:[0]-不偏移，[1]-工件/基底座標系下偏移，[2]-工具坐標系下偏移 預設 0;
    - ``offset_pos``:位元位偏移量，單位 [mm][°] 默認[0.0,0.0,0.0,0.0,0.0,0.0]"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos_spiral= [236.794,-475.119, -65.379, -176.938, 2.535, -179.829]#Spiral目標點
    #螺旋线參數[circle_num,circle_angle,rad_init,rad_add,rotaxis_add,rot_direction]
    # circle_num:螺旋圈數，circle_angle:螺旋傾角，rad_init:螺旋初始半径，rad_add:半徑增量，
    # rotaxis_add:轉軸方向增量，rot_direction:旋轉方向，0-順時針，1-逆時針
    param = [5.0,10,30,10,5,0]
    tool = 0#工具座標系編號
    user = 0 #工件座標系編號
    ret = robot.NewSpiral(desc_pos_spiral, tool, user, param,vel=40 )  #笛卡兒空間螺旋線運動
    print("笛卡兒空間螺旋線運動:錯誤碼", ret)

伺服運動開始
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveStart()``"
    "描述", "伺服運動開始，配合ServoJ、ServoCart指令使用"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

伺服運動結束
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoMoveEnd()``"
    "描述", "伺服運動結束，配合ServoJ、ServoCart指令使用"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

關節空間伺服模式運動
+++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoJ(joint_pos, axisPos, acc = 0.0, vel = 0.0, cmdT = 0.008, filterT = 0.0, gain = 0.0)``"
    "描述", "關節空間伺服模式運動"
    "必選參數", "- ``joint_pos``:目標關節位置，單位[°]；
    - ``axisPos``:外部軸位置,單位mm；"
    "默認參數", "- ``acc``:加速度，範圍 [0~100]，暫不開放，默認為 0.0;
    - ``vel``:速度，範圍 [0~100]，暫不開放，默認為 0.0;
    - ``cmdT``:指令下發週期，單位s，建議範圍[0.001~0.0016], 默認為0.008;
    - ``filterT``:濾波時間，單位 [s]，暫不開放， 默認為0.0;
    - ``gain``:目標位置的比例放大器，暫不開放， 默認為0.0;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

笛卡兒空間伺服模式運動
++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ServoCart(mode, desc_pos, pos_gain = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0] , acc = 0.0, vel = 0.0, cmdT = 0.008, filterT = 0.0, gain = 0.0)``"
    "描述", "笛卡兒空間伺服模式運動"
    "必選參數", "- ``mode``:[0]-绝对運動(基坐標系)，[1]-增量運動(基坐標系)，[2]-增量運動(工具座標系)；
    - ``desc_pos``:目標笛卡兒位置/目標笛卡兒位置增量；"
    "默認參數", "- ``pos_gain``:位姿增量比例系数，仅在增量運動下生效，範圍 [0~1], 默認為 [1.0, 1.0, 1.0, 1.0, 1.0, 1.0];
    - ``acc``:加速度，範圍 [0~100]，暫不開放，默認為 0.0;
    - ``vel``:速度，範圍 [0~100]，暫不開放，默認為 0.0;
    - ``cmdT``:指令下發週期，單位s，建議範圍[0.001~0.0016], 默認為0.008;
    - ``filterT``:濾波時間，單位 [s]，暫不開放， 默認為0.0;
    - ``gain``:目標位置的比例放大器，暫不開放， 默認為0.0;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error,joint_pos = robot.GetActualJointPosDegree()
    print("機器人當前關節位置",joint_pos)
    joint_pos = [joint_pos[0],joint_pos[1],joint_pos[2],joint_pos[3],joint_pos[4],joint_pos[5]]
    error_joint = 0
    count =100
    error = robot.ServoMoveStart()  #伺服運動開始
    print("伺服運動開始錯誤碼",error)
    while(count):
        error = robot.ServoJ(joint_pos=joint_pos,axisPos=[0,0,0,0,0,0])   #關節空間伺服模式運動
        if error!=0:
            error_joint =error
        joint_pos[0] = joint_pos[0] + 0.1  #每次1軸運動0.1度，運動100次
        count = count - 1
        time.sleep(0.008)
    print("關節空間伺服模式運動錯誤碼",error_joint)
    error = robot.ServoMoveEnd()  #伺服運動結束
    print("伺服運動結束錯誤碼",error) 
    mode = 2  #[0]-绝对運動(基坐標系)，[1]-增量運動(基坐標系)，[2]-增量運動(工具座標系)
    n_pos = [0.0,0.0,0.5,0.0,0.0,0.0]   #笛卡兒空间位姿增量
    error,desc_pos = robot.GetActualTCPPose()
    print("機器人目前笛卡爾位置",desc_pos)
    count = 100
    error_cart =0
    error = robot.ServoMoveStart()  #伺服運動開始
    print("伺服運動開始錯誤碼",error)
    while(count):
        error = robot.ServoCart(mode, n_pos, vel=40)   #笛卡兒空間伺服模式運動
        if error!=0:
            error_cart =error
        count = count - 1
        time.sleep(0.008)
    print("笛卡兒空間伺服模式運動錯誤碼", error_cart)
    error = robot.ServoMoveEnd()  #伺服運動開始
    print("伺服運動結束錯誤碼",error)

笛卡兒空間點到點運動
++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveCart(desc_pos, tool, user, vel = 20.0, acc = 0.0, ovl = 100.0, blendT = -1.0, config = -1)``"
    "描述", "笛卡兒空間點到點運動"
    "必選參數", "- ``desc_pos``:目標笛卡兒位置；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``vel``:速度，範圍 [0~100]，默認為 20.0;
    - ``acc``:加速度，範圍 [0~100]，暫不開放,默認為 0.0;
    - ``ovl``:速度縮放因子，[0~100]，默認為 100.0;
    - ``blendT``:[-1.0]-運動到位 (阻塞)，[0~500]-平滑時間 (非阻塞)，單位 [ms] 默認為 -1.0;
    - ``config``:關節配置，[-1]-參考當前關節位置求解，[0~7]-依据關節配置求解 默認為 -1"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos7 = [236.794,-475.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos8 = [236.794,-575.119, 165.379, -176.938, 2.535, -179.829]
    desc_pos9 = [236.794,-475.119, 265.379, -176.938, 2.535, -179.829]
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    robot.MoveCart(desc_pos7, tool, user)
    print("笛卡兒空間點到點運動點7:錯誤碼", ret) 
    robot.MoveCart(desc_pos8, tool, user, vel=30)
    print("笛卡兒空間點到點運動點8:錯誤碼", ret) 
    robot.MoveCart(desc_pos9, tool, user,)
    print("笛卡兒空間點到點運動點9:錯誤碼", ret)

機器人样条運動
++++++++++++++++

樣條運動開始
-----------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineStart()``"
    "描述", "樣條運動開始"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

樣條運動PTP
---------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplinePTP(joint_pos, tool, user, desc_pos = [0.0,0.0,0.0,0.0,0.0,0.0],  vel = 20.0,  acc = 100.0, ovl = 100.0)``"
    "描述", "樣條運動PTP"
    "必選參數", "- ``joint_pos``:目標關節位置，單位[°]；
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；"
    "默認參數", "- ``desc_pos``:目標笛卡兒位姿，單位 [mm][°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用正運動學求解傳回值;
    - ``vel``:速度，範圍 [0~100]，默認為 20.0;
    - ``acc``:加速度，範圍 [0~100]，默認為 100.0;
    - ``ovl``:速度縮放因子，[0~100]，默認為 100.0"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

樣條運動結束
----------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SplineEnd()``"
    "描述", "樣條運動結束"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    joint_pos1 = [116.489,-85.278,111.501,-112.486,-85.561,24.693]
    joint_pos2 = [86.489,-65.278,101.501,-112.486,-85.561,24.693]
    joint_pos3 = [116.489,-45.278,91.501,-82.486,-85.561,24.693]
    ret = robot.SplineStart() #樣條運動開始
    print("樣條運動開始:錯誤碼", ret)
    ret = robot.SplinePTP(joint_pos1, tool, user)   #樣條運動PTP
    print("樣條運動PTP運動點1:錯誤碼", ret) 
    ret = robot.SplinePTP(joint_pos2, tool, user)   #樣條運動PTP
    print("樣條運動PTP運動點2:錯誤碼", ret) 
    ret = robot.SplinePTP(joint_pos3, tool, user)   #樣條運動PTP
    print("樣條運動PTP運動點3:錯誤碼", ret)
    ret = robot.SplineEnd() #樣條運動結束
    print("樣條運動結束:錯誤碼", ret)

機器人新样条運動
+++++++++++++++++++
新樣條運動開始
------------------
.. versionchanged:: python SDK-v2.0.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplineStart(type,averageTime=2000)``"
    "描述", "新樣條運動開始"
    "必選參數", "- ``type``:0-圆弧过渡，1-给定點位路徑點"
    "默認參數", "- ``averageTime``:全局平均銜接時間（ms）默認為 2000"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

新樣條運動結束
-------------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``NewSplineEnd()``"
    "描述", "新樣條運動結束"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

新樣條指令點
----------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``NewSplinePoint(desc_pos,tool,user,lastFlag,joint_pos=[0.0,0.0,0.0,0.0,0.0,0.0], vel = 0.0, acc = 0.0, ovl = 100.0 ,blendR = 0.0 )``"
    "描述", "新樣條指令點"
    "必選參數", "- ``desc_pos``:目標笛卡兒位姿，單位 [mm][°];
    - ``tool``:工具號，[0~14]；
    - ``user``:工件號，[0~14]；
    - ``lastFlag``:是否為最後一個點，0-否，1-是;"
    "默認參數", "- ``joint_pos``:目標關節位置，單位 [°] 默認初值為[0.0,0.0,0.0,0.0,0.0,0.0]，默認值调用逆運動學求解傳回值;
    - ``vel``:速度，範圍 [0~100]，暫不開放，默認為 0.0;；
    - ``acc``:加速度，範圍 [0~100]，暫不開放，默認為 0.0;
    - ``ovl``:速度縮放因子，[0~100] 預設為 100.0;
    - ``blendR``: [0~1000]-平滑半径，單位 [mm] 默認0.0;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"


代碼範例
^^^^^^^^^^^

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    lastFlag= 0 # 是否為最後一個點，0-否，1-是
    desc_pos4 = [236.794,-375.119, 65.379, -176.938, 2.535, -179.829]
    desc_pos5 = [236.794,-275.119, 165.379, -176.938, 2.535, -179.829]
    desc_pos6 = [286.794,-375.119, 265.379, -176.938, 2.535, -179.829]
    ret = robot.NewSplineStart(1) #新樣條運動開始
    print("新樣條運動開始:錯誤碼", ret)
    ret = robot.NewSplinePoint(desc_pos4, tool, user, lastFlag)#新樣條指令點
    print("新樣條指令點4:錯誤碼", ret) 
    ret = robot.NewSplinePoint(desc_pos5, tool, user, lastFlag, vel=30)#新樣條指令點
    print("新樣條指令點5:錯誤碼", ret) 
    lastFlag = 1
    ret = robot.NewSplinePoint(desc_pos6, tool, user, lastFlag, vel=30)#新樣條指令點
    print("新樣條指令點6:錯誤碼", ret) 
    ret = robot.NewSplineEnd() #新樣條運動結束
    print("新樣條運動結束:錯誤碼", ret)

機器人終止運動
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``StopMotion()``"
    "描述", "終止運動，使用終止運動需運動指令為非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
-------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos1 = [-187.519, 319.248, 397, -157.278, -31.188, 107.199]
    desc_pos2 = [-187.519, 310.248, 297, -157.278, -31.188, 107.199]
    joint_pos1 = [-83.24, -96.476, 93.688, -114.079, -62, -100]
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    ret = robot.MoveL(desc_pos1, tool, user, joint_pos=joint_pos1)   #笛卡兒空間直線運動
    print("笛卡兒空間直線運動點1:錯誤碼", ret)
    ret = robot.StopMotion()  #終止運動
    print("終止運動:錯誤碼", ret) 
    robot.MoveL(desc_pos2, tool, user, vel=40, acc=100)
    print("笛卡兒空間直線運動點2:錯誤碼", ret)

機器人暫停運動
++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PauseMotion()``"
    "描述", "暫停運動，使用暫停運動需運動指令為非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

機器人恢復運動
++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``ResumeMotion()``"
    "描述", "恢復運動，使用恢復運動需運動指令為非阻塞狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

機器人點位整体偏移
+++++++++++++++++++
點位整體偏移開始
-------------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetEnable(flag,offset_pos)``"
    "描述", "點位整體偏移開始"
    "必選參數", "- ``flag``:0-基坐標或工件座標系下偏移， 2-工具座標系下偏移；
    - ``offset_pos``:偏移量，單位[mm][°]。"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

點位整體偏移結束
--------------------
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PointsOffsetDisable()``"
    "描述", "點位整體偏移結束"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
^^^^^^^^^^^^

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos3 = [-127.519, 256.248, 312, -147.278, -51.588, 107.199]
    desc_pos4 = [-140.519, 219.248, 300, -137.278, -11.188, 127.199]
    desc_pos5 = [-187.519, 319.248, 397, -157.278, -31.188, 107.199]
    desc_pos6 = [-207.519, 229.248, 347, -157.278, -31.188, 107.199]
    tool = 0 #工具座標系編號
    user = 0 #工件座標系編號
    flag = 1  #0-基座標系下/工件坐標系下偏移，2-工具坐標系下偏移
    offset_pos = [10,20,30,0,0,0]  #位元位偏移量
    ret = robot.PointsOffsetEnable(flag,offset_pos)
    print("點位整體偏移開始:錯誤碼", ret)
    robot.MoveL(desc_pos3, tool, user, offset_flag=1, offset_pos=[10,10,10,0,0,0])
    print("笛卡兒空間直線運動點3:錯誤碼", ret) 
    robot.MoveL(desc_pos4, tool, user, vel=30, acc=100)
    print("笛卡兒空間直線運動點4:錯誤碼", ret) 
    robot.MoveL(desc_pos5, tool, user)
    print("笛卡兒空間直線運動點5:錯誤碼", ret) 
    ret = robot.PointsOffsetDisable()
    print("點位整體偏移結束:錯誤碼", ret)

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
    - ``maxAOPercent``:最大TCP速度值對應的AO百分比，預設100%；
    - ``zeroZoneCmp``:死區補償值AO百分比，整形，預設為20%，範圍[0-100]。"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
    
代碼範例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #控制箱運動AO開始
    error = robot.MoveAOStart(0,100,98,1)
    print("MoveAOStart",error)
    error,joint_pos = robot.GetActualJointPosDegree()
    print("GetActualJointPosDegree",error,joint_pos)
    joint_pos[0] = joint_pos[0]+10
    #機器人關節運動
    error = robot.MoveJ(joint_pos,1,1)
    print("MoveJ",error)
    time.sleep(3)
    #控制箱運動AO停止
    error = robot.MoveAOStop()
    print("MoveAOStop",error)

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
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

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
    - ``maxAOPercent``:最大TCP速度值對應的AO百分比，預設100%；
    - ``zeroZoneCmp``:死區補償值AO百分比，整形，預設為20%，範圍[0-100]。"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
代碼範例
---------------

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #末端運動AO開始
    error = robot.MoveToolAOStart(0,100,98,1)
    print("MoveToolAOStart",error)
    error,desc_pos = robot.GetActualTCPPose()
    print("GetActualTCPPose",error,desc_pos)
    desc_pos[2] = desc_pos[2]-50
    #笛卡兒空間直線運動
    error = robot.MoveL(desc_pos,1,1)
    print("MoveL",error)
    time.sleep(3)
    #末端運動AO停止
    error = robot.MoveToolAOStop()
    print("MoveToolAOStop",error)
    
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
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

開始Ptp運動FIR測量
+++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningStart(maxAcc)``"
    "描述", "開始Ptp運動FIR測量"
    "必選參數", "- ``maxAcc``:最大加速度極值(deg/s2)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

關閉Ptp運動FIR測量
+++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``PtpFIRPlanningEnd()``"
    "描述", "關閉Ptp運動FIR測量"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
---------------
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，並連接到一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startdescPose = [-569.710, -132.595, 395.147, 178.418, -1.893, 171.051]
    startjointPos = [-2.334, -79.300, 108.196, -120.594, -91.790, -83.386]
    enddescPose = [-366.397, -572.427, 418.339, -178.972, 1.829, -142.970]
    endjointPos = [43.651, -70.284, 91.057, -109.075, -88.768, -83.382]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]

    # Ptp运动FIR滤波开启
    robot.PtpFIRPlanningStart(maxAcc=1000)
    robot.MoveJ(startjointPos, 0, 0,vel=50)
    robot.MoveJ(endjointPos, 0, 0,vel=50)
    robot.PtpFIRPlanningEnd()

开始LIN、ARC运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningStart(maxAccLin,maxAccDeg,maxJerkLin,maxJerkDeg)``"
    "描述", "开始LIN、ARC运动FIR滤波"
    "必選參數", "- ``maxAccLin``:线加速度极值(mm/s2)
    - ``maxAccDeg``:角加速度极值(deg/s2)
    - ``maxJerkLin``:线加加速度极值(mm/s3)
    - ``maxJerkDeg``:角加加速度极值(deg/s3)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

关闭LIN、ARC运动FIR滤波
+++++++++++++++++++++++
.. versionadded:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``LinArcFIRPlanningEnd()``"
    "描述", "关闭LIN、ARC运动FIR滤波"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"   

代碼範例
---------------
.. versionadded:: Python SDK-v2.0.8-3.7.8
    
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，並連接到一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    startdescPose = [-569.710, -132.595, 395.147, 178.418, -1.893, 171.051]
    startjointPos = [-2.334, -79.300, 108.196, -120.594, -91.790, -83.386]
    enddescPose = [-366.397, -572.427, 418.339, -178.972, 1.829, -142.970]
    endjointPos = [43.651, -70.284, 91.057, -109.075, -88.768, -83.382]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]

    # LIN、ARC運動FIR探測開啟
    robot.LinArcFIRPlanningStart(5000, 5000, 5000, 5000)
    robot.MoveL(startdescPose, 0, 0,vel=100)
    robot.MoveL(enddescPose, 0, 0,vel=100)
    robot.LinArcFIRPlanningEnd()

停止運動
+++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30
    
    "原型", "``StopMove()``"
    "描述", "停止運動"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"  


加速度平滑開啟
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothStart(saveFlag_flag)``"
    "描述", "加速度平滑開啟"
    "必選參數", "- ``saveFlag_flag``: 是否斷電保存"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

加速度平滑關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AccSmoothEnd(saveFlag_flag)``"
    "描述", "加速度平滑關閉"
    "必選參數", "- ``saveFlag_flag``: 是否斷電保存"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0 失敗- errcode"

代碼示例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    JP1 = [88.927,-85.834,80.289,-85.561,-91.388,108.718]
    DP1 = [88.739,-527.617,514.939,-179.039,1.494,70.209]

    JP2 = [27.036,-83.909,80.284,-85.579,-90.027,108.604]
    DP2 = [-433.125,-334.428,497.139,-179.723,-0.745,8.437]
    error = robot.AccSmoothStart(saveFlag=0)
    print("AccSmoothStart 返回值:",error)
    error = robot.MoveJ(JP1, tool=0, user=0, vel=100)
    error = robot.MoveJ(JP2, tool=0, user=0, vel=100)
    error = robot.MoveJ(JP1, tool=0, user=0, vel=100)
    error = robot.MoveJ(JP2, tool=0, user=0, vel=100)
    error = robot.AccSmoothEnd(saveFlag=0)
    print("AccSmoothEnd 返回值:", error)