機器人力控
============

.. toctree:: 
    :maxdepth: 5

取得力傳感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetConfig()``"
    "描述", "取得力傳感器配置"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[number,company,device,softversion,bus]``：number 传感器編號;company  力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI 传感器，21-中科米點，22-伟航敏芯;device  设备号，坤维 (0-KWR75B)，航天十一院 (0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點 (0-MST2010)，伟航敏芯 (0-WHC6L-YB10A);softvesion  軟體版本號，暫不使用，預設為0" 

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 17    #感測器廠商，17-坤維科技
    device = 0      #感測器設備號
    error = robot.FT_SetConfig(company, device)   #配置力感測器
    print("配置力感測器錯誤碼",error)
    config = robot.FT_GetConfig() #取得力傳感器配置信息
    print('取得力傳感器配置信息',config)
    time.sleep(1)
    error = robot.FT_Activate(0)  #感測器復位
    print("感測器復位錯誤碼",error)
    time.sleep(1)
    error = robot.FT_Activate(1)  #感測器啟動
    print("感測器啟動錯誤碼",error)
    time.sleep(1)
    error = robot.SetLoadWeight(0.0)    #末端負載設定為零
    print("末端負載設定為零錯誤碼",error)
    time.sleep(1)
    error = robot.SetLoadCoord(0.0,0.0,0.0)  #末端負載質心設定為零
    print("末端质心設定為零錯誤碼",error)
    time.sleep(1)
    error = robot.FT_SetZero(0)   #感測器去除零點
    print("感測器去除零點錯誤碼",error)
    time.sleep(1)
    error = robot.FT_GetForceTorqueOrigin()   #查詢感測器原始數據
    print("查詢感測器原始數據",error)
    error = robot.FT_SetZero(1)   #感測器零點矯正,注意此時末端不能安裝工具，只有力道感測器
    print("传感器零點矫正",error)
    time.sleep(1)
    error = robot.FT_GetForceTorqueRCS()  #查詢感測器座標系下數據
    print("查詢感測器座標系下數據",error)

力感測器配置
+++++++++++++++++++++++++
.. versionchanged:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetConfig(company,device,softversion=0,bus=0)``"
    "描述", "力感測器配置"
    "必選參數", "- ``company``：感測器廠商，17-坤維科技，19-航太十一院，20-ATI感測器，21-中科米點，22-偉航敏芯，23-NBIT，24-鑫精誠(XJC)，26-NSR；
    - ``device``：設備號，坤維(0-KWR75B)，航太十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A)，偉航敏芯(0-WHC6L-YB-10 6F-D82)，NSR(0-NSR-FTSensorA)；"
    "默認參數", "- ``softversion``：軟體版本號，暫不使用，預設為0；
    - ``bus``：設備掛載末端匯流排位置，暫不使用，預設為 0；"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

力傳感器激活
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Activate(state)``"
    "描述", "力傳感器激活"
    "必選參數", "- ``state``：0-復位，1-激活"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

力傳感器校零
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetZero(state)``"
    "描述", "力傳感器校零"
    "必選參數", "- ``state``：0-去除零點，1-零點矯正"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

設定力道感測器參考座標系
+++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetRCS(ref,coord=[0,0,0,0,0,0])``"
    "描述", "設定力道感測器參考座標系"
    "必選參數", "- ``ref``：0-工具座標系，1-基坐標系"
    "默認參數", "- ``coord``：[x,y,z,rx,ry,rz]自定义座標系值,默認[0,0,0,0,0,0]"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #負載辨識，此時末端安裝要辨識的工具，工具安裝在力道感測器下方,末端垂直向下
    error = robot.FT_SetRCS(0)    #設定參考坐標系為工具坐標系，0-工具坐標系，1-基坐標系
    print('設定參考座標系錯誤碼',error)
    time.sleep(1)
    tool_id = 10  #传感器座標系編號
    tool_coord = [0.0,0.0,35.0,0.0,0.0,0.0]   # 传感器相对末端法蘭位姿
    tool_type = 1  # 0-工具，1-传感器
    tool_install = 0 # 0-安裝末端，1-機器人外部
    error = robot.SetToolCoord(tool_id,tool_coord,tool_type,tool_install)     #設定传感器座標系，传感器相对末端法蘭位姿
    print('設定传感器座標系錯誤碼',error)
    time.sleep(1)
    error = robot.FT_PdIdenRecord(tool_id)   #記錄辨識數據
    print('記錄負載重量錯誤碼',error)
    time.sleep(1)
    error = robot.FT_PdIdenRecord()  #计算負載重量，單位kg
    print('计算負載重量錯誤碼',error)
    #負載質心辨识，機器人需要示教三個不同的姿態，然后記錄辨識數據，最后计算負載質心
    robot.Mode(1)
    ret = robot.DragTeachSwitch(1)  #機器人切入拖曳示教模式，必須在手動模式下才能切入拖曳示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,1)
    print('負載質心1錯誤碼',error)#記錄辨識數據
    ret = robot.DragTeachSwitch(1)  #機器人切入拖曳示教模式，必須在手動模式下才能切入拖曳示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,2)
    print('負載質心2錯誤碼',error)
    ret = robot.DragTeachSwitch(1)  #機器人切入拖曳示教模式，必須在手動模式下才能切入拖曳示教模式
    time.sleep(5)
    ret = robot.DragTeachSwitch(0)
    time.sleep(1)
    error = robot.FT_PdCogIdenRecord(tool_id,3)
    print('負載質心3錯誤碼',error)
    time.sleep(1)
    error = robot.FT_PdCogIdenCompute()
    print('負載質心计算錯誤碼',error)

負載重量辨識計算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenCompute()``"
    "描述", "負載重量辨識計算"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode   
    - ``weight``：負載重量，單位 kg  "

負載重量辨識記錄
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenRecord(tool_id)``"
    "描述", "負載重量辨識記錄"
    "必選參數", "- ``tool_id``：传感器座標系編號，範圍[0~14]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode  "

負載質心辨識計算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenCompute()``"
    "描述", "負載質心辨識計算"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode  
    - ``cog=[cogx,cogy,cogz]``：負載質心，單位 mm  "

負載質心辨識記錄
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenRecord(tool_id,index)``"
    "描述", "負載質心辨識記錄"
    "必選參數", "- ``tool_id``：传感器座標系編號，範圍[0~14];
    - ``index``：點編號[1~3]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

取得參考坐標系下力/扭力數據
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueRCS()``"
    "描述", "取得參考坐標系下力/扭力數據"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``data=[fx,fy,fz,tx,ty,tz]``：參考座標系下力/扭矩數據"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rcs = robot.FT_GetForceTorqueRCS()  #查詢感測器座標系下數據
    print(rcs)

取得力感測器原始力/扭力數據
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueOrigin()``"
    "描述", "取得力感測器原始力/扭力數據"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode  
    - ``data=[fx,fy,fz,tx,ty,tz]``：力感測器原始力/扭力數據 "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    origin = robot.FT_GetForceTorqueOrigin()   #查詢感測器原始數據
    print(origin)

碰撞守護
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Guard(flag,sensor_num,select,force_torque,max_threshold,min_threshold)``"
    "描述", "碰撞守護"
    "必選參數", "- ``flag``：0-關閉碰撞守護，1-開啟碰撞守護；
    - ``sensor_num``：力傳感器編號；
    - ``select``：六個自由度是否偵測碰撞[fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``force_torque``：碰撞檢測力/力矩，單位N或Nm；
    - ``max_threshold``：最大閾值；
    - ``min_threshold``：最小閾值；
    - 力/力矩检测範圍:(force_torque-min_threshold,force_torque+max_threshold)"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #碰撞守護
    actFlag = 1   #開啟标志，0-關閉碰撞守護，1-開啟碰撞守護
    sensor_num = 1  #力傳感器編號
    is_select = [1,1,1,1,1,1]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,0.0,0.0,0.0,0.0]  #碰撞检测力和力矩，检测範圍（force_torque-min_threshold,force_torque+max_threshold）
    max_threshold = [10.0,10.0,10.0,10.0,10.0,10.0]  #最大閾值
    min_threshold = [5.0,5.0,5.0,5.0,5.0,5.0]   #最小閾值
    P1=[-160.619,-586.138,384.988,-170.166,-44.782,169.295]
    P2=[-87.615,-606.209,556.119,-102.495,10.118,178.985]
    P3=[41.479,-557.243,484.407,-125.174,46.995,-132.165]
    error = robot.FT_Guard(actFlag, sensor_num, is_select, force_torque, max_threshold, min_threshold)    #開啟碰撞守護
    print("開啟碰撞守護錯誤碼",error)
    error = robot.MoveL(P1,1,0)         #笛卡兒空間直線運動
    print("笛卡兒空間直線運動錯誤碼",error)
    error = robot.MoveL(P2,1,0)
    print("笛卡兒空間直線運動錯誤碼",error)
    error = robot.MoveL(P3,1,0)
    print("笛卡兒空間直線運動錯誤碼",error)
    actFlag = 0  
    error = robot.FT_Guard(actFlag, sensor_num, is_select, force_torque, max_threshold, min_threshold)    #關閉碰撞守護
    print("關閉碰撞守護錯誤碼",error)

恆力控制
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Control(flag,sensor_num,select,force_torque,gain,adj_sign,ILC_sign,max_dis,max_ang)``"
    "描述", "恆力控制"
    "必選參數", "- ``flag``：恆力控制開啟标志，0-關，1-開；
    - ``sensor_num``：力傳感器編號；
    - ``select``：六個自由度是否检测 [fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``force_torque``：检测力/力矩，單位N或Nm；
    - ``gain``：[f_p,f_i,f_d,m_p,m_i,m_d],力pid參數，力矩pid參數；
    - ``adj_sign``：自適應啟動停止狀態，0-關閉，1-開啟；
    - ``ILC_sign``: ILC控制啟動停止狀態，0-停止，1-訓練，2-實操；
    - ``max_dis``：最大調整距離；
    - ``max_ang``：最大調整角度；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #恆力控制
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [0,0,1,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0005,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 100.0  #最大調整距離
    max_ang = 0.0  #最大調整角度
    J1=[70.395, -46.976, 90.712, -133.442, -87.076, -27.138]
    P2=[-123.978, -674.129, 44.308, -178.921, 2.734, -172.449]
    P3=[123.978, -674.129, 42.308, -178.921, 2.734, -172.449]
    error = robot.MoveJ(J1,1,0)    
    print("關節空間運動指令錯誤碼",error)
    error = robot.MoveL(P2,1,0)
    print("笛卡兒空間直線運動指令錯誤碼",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開啟錯誤碼",error)
    error = robot.MoveL(P3,1,0)   #笛卡兒空間直線運動
    print("笛卡兒空間直線運動指令錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制结束錯誤碼",error)

螺旋線探索
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SpiralSearch(rcs, ft, dr=0.7, max_t_ms=60000, max_vel=5)``"
    "描述", "螺旋線探索"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基坐標系
    - ``ft``：力或力矩阈值 (0~100)，單位 N 或 Nm;"
    "默認參數", "- ``dr``：每圈半徑進給量，單位 mm 默認0.7;
    - ``max_t_ms``：最大探索時間，單位 ms 默認 60000;
    - ``max_vel``：線速度最大值，單位 mm/s 默認 5"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力參數
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [0,0,1,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 100.0  #最大調整距離
    max_ang = 5.0  #最大調整角度
    #螺旋線探索參數
    rcs = 0  #參考座標系，0-工具座標系，1-基坐標系
    fFinish = 10 #力或力矩閾值（0~100），單位N或Nm
    error = robot.MoveL(P,1,0) #笛卡兒空間直線運動至初始點
    print("笛卡兒空間直線運動至初始點",error)
    is_select = [0,0,1,1,1,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign, max_dis,max_ang)
    print("恆力控制開啟錯誤碼",error)
    error = robot.FT_SpiralSearch(rcs,fFinish,max_vel=3)
    print("螺旋線探索錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign, max_dis,max_ang)
    print("恆力控制關閉錯誤碼",error)

旋轉插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_RotInsertion(rcs, ft, orn, angVelRot=3, angleMax=45, angAccmax=0, rotorn=1)``"
    "描述", "旋轉插入"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基坐標系；
    - ``ft``：力或力矩閾值 (0~100)，單位 N 或 Nm;
    - ``orn``：力/扭力方向，1-沿z軸方向，2-繞z軸方向;"
    "默認參數", "- ``angVelRot``：旋轉角速度，單位°/s,默認 3;
    - ``angleMax``：最大旋轉角度，單位 ° 默認 45;
    - ``angAccmax``：最大旋轉加速度，單位 °/s^2，暫不使用 預設0;
    - ``rotorn``：旋轉方向，1-順時針，2-逆時針 默認1"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力參數
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [0,0,1,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0] 
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數   
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 100.0  #最大調整距離
    max_ang = 5.0  #最大調整角度
    #旋轉插入參數
    rcs = 0  #參考座標系，0-工具座標系，1-基坐標系
    forceInsertion = 2.0 #力或力矩閾值（0~100），單位N或Nm
    orn = 1 #力的方向，1-fz,2-mz
    #默認參數 angVelRot：旋轉角速度，單位 °/s  默認 3
    #默認參數 angleMax：最大旋轉角度，單位 ° 默認 5
    #默認參數 angAccmax：最大旋轉加速度，單位 °/s^2，暫不使用 預設0
    #默認參數 rotorn：旋轉方向，1-順時針，2-逆時針 默認1
    error = robot.MoveL(P,1,0) #笛卡兒空間直線運動至初始點
    print("笛卡兒空間直線運動至初始點",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開啟錯誤碼",error)
    error = robot.FT_RotInsertion(rcs,1,orn)
    print("旋轉插入錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制關閉錯誤碼",error)

直線插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_LinInsertion(rcs, ft, disMax, linorn, lin_v=1.0, lin_a=1.0)``"
    "描述", "直線插入"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基坐標系；
    - ``ft``：力或力矩阈值 (0~100)，單位 N 或 Nm;
    - ``disMax``：最大插入距離，單位 mm;
    - ``linorn``：插入方向:0-負方向，1-正方向"
    "默認參數", "- ``lin_v``：直線速度，單位 mm/s 默認1;
    - ``lin_a``：直線加速度，單位 mm/s^2，暫不使用 默認1"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:
    
    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    P = [36.794,-675.119, 65.379, -176.938, 2.535, -179.829]
    #恒力參數
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [0,0,1,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [0.0,0.0,-10.0,0.0,0.0,0.0]  
    gain = [0.0001,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 100.0  #最大調整距離
    max_ang = 5.0  #最大調整角度
    #直線插入參數
    rcs = 0  #參考座標系，0-工具座標系，1-基坐標系
    force_goal = 10.0  #力或力矩閾值（0~100），單位N或Nm
    disMax = 100.0 #最大插入距離，單位mm
    linorn = 1 #插入方向，1-正方向，2-負方向
    #默認參數 lin_v：直線速度，單位 mm/s 默認1
    #默認參數 lin_a：直線加速度，單位 mm/s^2，暫不使用 默認0
    error = robot.MoveL(P,1,0) #笛卡兒空間直線運動至初始點
    print("笛卡兒空間直線運動至初始點",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開啟錯誤碼",error)
    error = robot.FT_LinInsertion(rcs,force_goal,disMax,linorn)
    print("直線插入錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制關閉錯誤碼",error)

計算中間平面位置開始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterStart()``"
    "描述", "計算中間平面位置開始"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

計算中間平面位置結束
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterEnd()``"
    "描述", "計算中間平面位置結束"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode
    - ``pos=[x,y,z,rx,ry,rz]``：中间平面位置"

表面定位
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_FindSurface (rcs, dir, axis, disMax, ft, lin_v=3.0, lin_a=0.0)``"
    "描述", "表面定位"
    "必選參數", "- ``rcs``： 參考座標系，0-工具座標系，1-基坐標系；
    - ``dir``：移動方向，1-正方向，2-負方向；
    - ``axis``：移動軸，1-x，2-y，3-z；
    - ``disMax``：最大探索距離，單位 mm;
    - ``ft``：動作終止力閾值，單位N；"
    "默認參數", "- ``lin_v``：探索直線速度，單位mm/s 默認3;
    - ``lin_a``：探索直線加速度，單位mm/s^2 默認0;"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    #恆力控制
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [1,0,0,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [-2.0,0.0,0.0,0.0,0.0,0.0]  
    gain = [0.0002,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 15.0  #最大調整距離
    max_ang = 0.0  #最大調整角度
    #表面定位參數
    rcs = 0 #參考座標系，0-工具座標系，1-基坐標系
    direction = 1 #移動方向，1-正方向，2-負方向
    axis = 1 #移動軸，1-X,2-Y,3-Z
    lin_v = 3.0  #探索直線速度，單位mm/s
    lin_a = 0.0  #探索直線加速度，單位mm/s^2
    disMax = 50.0 #最大探索距離，單位mm
    force_goal = 2.0 #動作終止力閾值，單位N
    P1=[-77.24,-679.599,58.328,179.373,-0.028,-167.849]
    Robot.MoveCart(P1,1,0)       #關節空间點到點運動
    #x方向寻找中心
    #第1個表面
    error = robot.FT_CalCenterStart()
    print("计算中间平面開始錯誤碼",error)
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開始錯誤碼",error)
    error = robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找X+表面錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制结束錯誤碼",error)
    time.sleep(2)
    error = robot.MoveCart(P1,1,0)       #關節空间點到點運動
    print("關節空间點到點運動錯誤碼",error)
    time.sleep(5)
    #第2個表面
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開始錯誤碼",error)
    direction = 2 #移動方向，1-正方向，2-負方向
    error = robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找X—表面錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制结束錯誤碼",error)
    #计算x方向中心位置
    error,xcenter = robot.FT_CalCenterEnd()
    print("计算X方向中间平面结束錯誤碼",xcenter) 
    error = robot.MoveCart(xcenter,1,0)
    print("關節空间點到點運動錯誤碼",error)
    time.sleep(1)
    #y方向寻找中心
    #第1個表面
    error =robot.FT_CalCenterStart()
    print("计算中间平面開始錯誤碼",error)
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開始錯誤碼",error)
    direction = 1 #移動方向，1-正方向，2-負方向
    axis = 2 #移動軸，1-X,2-Y,3-Z
    disMax = 150.0 #最大探索距離，單位mm
    lin_v = 6.0  #探索直線速度，單位mm/s
    error =robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找表面Y+錯誤碼",error)
    status = 0
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制结束錯誤碼",error)
    error =robot.MoveCart(P1,1,0)       #關節空间點到點運動
    print("關節空间點到點運動錯誤碼",error)
    Robot.WaitMs(1000)
    #第2個表面
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開始錯誤碼",error)
    direction = 2 #移動方向，1-正方向，2-負方向
    error =robot.FT_FindSurface(rcs,direction,axis,disMax,force_goal)
    print("寻找表面Y-錯誤碼",error)
    status = 0
    error =robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制结束錯誤碼",error)
    #计算y方向中心位置
    error,ycenter=robot.FT_CalCenterEnd()
    print("计算中间平面Y方向结束錯誤碼",ycenter)
    error =robot.MoveCart(ycenter,1,0)
    print("關節空间點到點運動錯誤碼",error)

柔順控制關閉
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStop()``"
    "描述", "柔順控制關閉"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

柔順控制開啟
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStart(p, force)``"
    "描述", "柔順控制開啟"
    "必選參數", "- ``p``: 位置調節係數或柔順係數
    - ``force``：柔順開啟力閾值，單位N"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode  "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    J1=[75.005,-46.434,90.687,-133.708,-90.315,-27.139]
    P2=[-77.24,-679.599,38.328,179.373,-0.028,-167.849]
    P3=[77.24,-679.599,38.328,179.373,-0.028,-167.849]
    #恆力控制參數
    status = 1  #恆力控制開啟标志，0-關，1-開
    sensor_num = 1 #力傳感器編號
    is_select = [1,1,1,0,0,0]  #六個自由度選擇[fx,fy,fz,mx,my,mz]，0-不生效，1-生效
    force_torque = [-10.0,-10.0,-10.0,0.0,0.0,0.0] 
    gain = [0.0005,0.0,0.0,0.0,0.0,0.0]  #力pid參數，力矩pid參數
    adj_sign = 0  #自適應啟動停止狀態，0-關閉，1-開啟
    ILC_sign = 0  #ILC控制啟動停止狀態，0-停止，1-訓練，2-實操
    max_dis = 1000.0  #最大調整距離
    max_ang = 0.0  #最大調整角度
    error = robot.MoveJ(J1,1,0)
    print("關節空間運動到點1錯誤碼",error)
    #柔顺控制
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制開始錯誤碼",error)
    p = 0.00005  #位置調節係數或柔順係數
    force = 30.0 #柔順開啟力閾值，單位N
    error = robot.FT_ComplianceStart(p,force)
    print("柔顺控制開始錯誤碼",error)
    error = robot.MoveL(P2,1,0,vel =10)   #笛卡兒空間直線運動
    print("笛卡兒空間直線運動到點2錯誤碼", error)
    error = robot.MoveL(P3,1,0,vel =10)
    print("笛卡兒空間直線運動到點3錯誤碼", error)
    time.sleep(1)
    error = robot.FT_ComplianceStop()
    print("柔顺控制结束錯誤碼",error)
    status = 0
    error = robot.FT_Control(status,sensor_num,is_select,force_torque,gain,adj_sign, ILC_sign,max_dis,max_ang)
    print("恆力控制關閉錯誤碼",error)

負載辨識濾波初始化
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyDynFilterInit()``"
    "描述", "負載辨識濾波初始化"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode  "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    #負載辨識濾波初始化
    error = robot.LoadIdentifyDynFilterInit()
    print("LoadIdentifyDynFilterInit:",error)
    #負載辨識變數初始化
    error = robot.LoadIdentifyDynVarInit()
    print("LoadIdentifyDynVarInit:",error)

    joint_torque= [0,0,0,0,0,0]
    joint_pos= [0,0,0,0,0,0]
    gain=[0,0.05,0,0,0,0,0,0.02,0,0,0,0]
    t =10
    error,joint_pos=robot.GetActualJointPosDegree(1)
    joint_pos[1] = joint_pos[1]+10
    error,joint_torque=robot.GetJointTorques(1)
    joint_torque[1] = joint_torque[1]+2
    #負荷辨識主程序
    error = robot.LoadIdentifyMain(joint_torque, joint_pos, t)
    print("LoadIdentifyMain:",error)
    #獲取負荷辨識結果
    error = robot.LoadIdentifyGetResult(gain)
    print("LoadIdentifyGetResult:",error)

負載辨識變數初始化
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyDynVarInit()``"
    "描述", "負載辨識變數初始化"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode  "

負荷辨識主程序
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyMain(joint_torque, joint_pos, t)``"
    "描述", "負荷辨識主程序"
    "必選參數", "- ``joint_torque``： 關節扭矩 j1-j6；
    - ``joint_pos``：關節位置 j1-j6
    - ``t``：採樣週期"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

獲取負荷辨識結果
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyGetResult(gain)``"
    "描述", "獲取負荷辨識結果"
    "必選參數", "- ``gain``：重力項係數double[6]，離心項係數double[6]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weight``：負載重量
    - ``cog=[x,y,z]``：負載質心座標"

力道感測器輔助拖曳
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``EndForceDragControl(status, asaptiveFlag, interfereDragFlag, ingularityConstraintsFlag, M, B, K, F, Fmax, Vmax, forceCollisionFlag=0)``"
    "描述", "力傳感器輔助拖動"
    "必選參數", "- ``status``：控制狀態，0-關閉；1-開啓
    - ``asaptiveFlag``：自適應開啓標誌，0-關閉；1-開啓
    - ``interfereDragFlag``：干涉區拖動標誌，0-關閉；1-開啓
    - ``ingularityConstraintsFlag``：奇異點策略，0-規避；1-穿越
    - ``forceCollisionFlag``：輔助拖動時機器人碰撞檢測標誌；0-關閉；1-開啓
    - ``M=[m1,m2,m3,m4,m5,m6]``：慣性系數
    - ``B=[b1,b2,b3,b4,b5,b6]``：阻尼係數
    - ``K=[k1,k2,k3,k4,k5,k6]``：剛度係數
    - ``F=[f1,f2,f3,f4,f5,f6]``：拖動六維力閾值
    - ``Fmax``：最大拖動力限制
    - ``Vmax``：最大關節速度限制"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')
    M = [15.0, 15.0, 15.0, 0.5, 0.5, 0.1]
    B = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    K = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    F = [10.0, 10.0, 10.0, 1.0, 1.0, 1.0]

    rtn = robot.EndForceDragControl(status=1,asaptiveFlag= 0,interfereDragFlag= 0,ingularityConstraintsFlag= 0,forceCollisionFlag= 1,M= M,B= B,K= K,F= F,Fmax= 50,Vmax=100)
    print(f"force drag control start rtn is:{rtn}")
    time.sleep(5)

    rtn = robot.EndForceDragControl(status=0, asaptiveFlag=0, interfereDragFlag=0, ingularityConstraintsFlag=0,forceCollisionFlag=1, M=M, B=B, K=K, F=F, Fmax=50, Vmax=100)
    print(f"force drag control end rtn is:{rtn}")

    rtn = robot.ResetAllError()
    print(f"ResetAllError rtn is:{rtn}")

    rtn = robot.EndForceDragControl(status=1, asaptiveFlag=0, interfereDragFlag=0, ingularityConstraintsFlag=0,forceCollisionFlag=1, M=M, B=B, K=K, F=F, Fmax=50, Vmax=100)
    print(f"force drag control start again rtn is:{rtn}")
    time.sleep(5)

    rtn = robot.EndForceDragControl(status=0, asaptiveFlag=0, interfereDragFlag=0, ingularityConstraintsFlag=0,forceCollisionFlag=1, M=M, B=B, K=K, F=F, Fmax=50, Vmax=100)
    print(f"force drag control end again rtn is:{rtn}")

報錯清除後力感知器自動開啟
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorDragAutoFlag(status)``"
    "描述", "報錯清除後力感知器自動開啟"
    "必選參數", "- ``status``：控制狀態，0-關閉；1-開啟"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
    
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    error = robot. SetForceSensorDragAutoFlag (1)
    print("SetForceSensorDragAutoFlag return:",error)
    
設定六維力和關節阻抗混合拖曳開關及參數
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceAndJointImpedanceStartStop(status, impedanceFlag, lamdeDain, KGain, BGain, dragMaxTcpVel, dragMaxTcpOriVel)``"
    "描述", "設置六維力和關節阻抗混合拖動開關及參數"
    "必選參數", "- ``status``：控制狀態，0-關閉；1-開啓
    - ``impedanceFlag``：阻抗開啓標誌，0-關閉；1-開啓
    - ``lamdeDain``：[D1,D2,D3,D4,D5, D6] 拖動增益
    - ``KGain``：[K1,K2,K3,K4,K5,K6]剛度增益
    - ``BGain``：[B1,B2,B3,B4,B5,B]阻尼增益
    - ``dragMaxTcpVel``：拖動末端最大線速度限制
    - ``dragMaxTcpOriVel``：拖動末端最大角速度限制"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    status = 1 #控制狀態，0-關閉；1-開啟
    impedanceFlag = 1 #阻抗開啟標誌，0-關閉；1-開啟
    lamdeDain = [ 3.0, 2.0, 2.0, 2.0, 2.0, 3.0] # 拖曳增益
    KGain = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00] # 剛度增益
    BGain = [150, 150, 150, 5.0, 5.0, 1.0] # 阻尼增益
    dragMaxTcpVel = 1000 #拖曳末端最大線速度限制
    dragMaxTcpOriVel = 180 #拖曳末端最大角速度限制

    error = robot.DragTeachSwitch(1)
    print("DragTeachSwitch 1  return:",error)

    error = robot.ForceAndJointImpedanceStartStop(status, impedanceFlag, lamdeDain, KGain, BGain,dragMaxTcpVel,dragMaxTcpOriVel)
    print("ForceAndJointImpedanceStartStop return:",error)

    error = robot.GetForceAndTorqueDragState()
    print("GetForceAndTorqueDragState return:",error)

    time.sleep(10)

    status = 0 #控制狀態，0-關閉；1-開啟
    impedanceFlag = 0 #阻抗開啟標誌，0-關閉；1-開啟
    error = robot.ForceAndJointImpedanceStartStop(status, impedanceFlag, lamdeDain, KGain, BGain,dragMaxTcpVel,dragMaxTcpOriVel)
    print("ForceAndJointImpedanceStartStop return:",error)

    error = robot.GetForceAndTorqueDragState()
    print("GetForceAndTorqueDragState return:",error)

    error = robot.DragTeachSwitch(0)
    print("DragTeachSwitch 0  return:",error)
        
取得力道感測器拖曳開關狀態
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceAndTorqueDragState()``"
    "描述", "取得力道感測器拖曳開關狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``dragState``：力道感測器輔助拖曳控制狀態，0-關閉；1-開啟
    - ``sixDimensionalDragState``：六維力輔助拖曳控制狀態，0-關閉；1-開啟"
        
設定力道感測器下負載重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayload(weight)``"
    "描述", "設定力道感測器下負載重量"
    "必選參數", " - ``weight``：負載重量 kg"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
        
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    error = robot.SetForceSensorPayload(0.8)
    print("SetForceSensorPayload return:",error)

    error = robot.SetForceSensorPayloadCog(0.5,0.6,12.5)
    print("SetForceSensorPayLoadCog return:",error)

    error = robot.GetForceSensorPayload()
    print("GetForceSensorPayLoad return:",error)

    error = robot.GetForceSensorPayloadCog()
    print("GetForceSensorPayLoadCog return:",error)
            
設定力道感測器下負載質心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayloadCog(x,y,z)``"
    "描述", "設定力道感測器下負載質心"
    "必選參數", "
    - ``x``：負載質心x mm
    - ``y``：負載質心y mm
    - ``z``：負載質心z mm
    "
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"
            
取得力道感測器下負載重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayload()``"
    "描述", "取得力道感測器下負載重量"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weight``：負載重量 kg"
            
取得力感測器下負載質心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayloadCog()``"
    "描述", "取得力感測器下負載質心"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``x``：負載質心x mm 
    - ``y``：負載質心y mm 
    - ``z``：負載質心z mm"
            
力傳感器自動校零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceSensorAutoComputeLoad()``"
    "描述", "力傳感器自動校零"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weight``：感測器質量 kg
    - ``pos=[x,y,z]``：感測器質心 mm"
        
代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    error = robot.SetForceSensorPayload(0)
    print("SetForceSensorPayload return:",error)

    error = robot.SetForceSensorPayloadCog(0,0,0)
    print("SetForceSensorPayLoadCog return:",error)

    error = robot.ForceSensorAutoComputeLoad()
    print("ForceSensorAutoComputeLoad return:",error)

感測器自動校零資料記錄
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceSensorSetSaveDataFlag(recordCount)``"
    "描述", "感測器自動校零資料記錄"
    "必選參數", "- ``recordCount``：記錄數據個数 1-3"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗-errcode"

感測器自動校零計算
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ForceSensorComputeLoad()``"
    "描述", "感測器自動校零資料記錄"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗-errcode
    - ``weight``：感測器質量 kg 
    - ``pos=[x,y,z]``：感測器質心 mm"