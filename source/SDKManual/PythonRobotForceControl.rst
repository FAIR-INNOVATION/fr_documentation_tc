機器人力控
============

.. toctree:: 
    :maxdepth: 5

力傳感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetConfig(company,device,softversion=0,bus=0)``"
    "描述", "力傳感器配置"
    "必選參數", "- ``company``：傳感器廠商，17-坤維科技，19-航天十一院，20-ATI傳感器，21-中科米點，22-偉航敏芯，23-NBIT，24-鑫精誠(XJC)，26-NSR；
    - ``device``：設備號，坤維(0-KWR75B)，航天十一院(0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點(0-MST2010)，偉航敏芯(0-WHC6L-YB-10A)，NBIT(0-XLH93003ACS)，鑫精誠XJC(0-XJC-6F-D82)，NSR(0-NSR-FTSensorA)；"
    "默認參數", "- ``softversion``：軟件版本號，暫不使用，默認爲0；
    - ``bus``：設備掛載末端總線位置，暫不使用，默認爲 0；"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取力傳感器配置
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetConfig()``"
    "描述", "獲取力傳感器配置"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[number,company,device,softversion,bus]``：number 傳感器編號;company  力傳感器廠商，17-坤維科技，19-航天十一院，20-ATI 傳感器，21-中科米點，22-偉航敏芯;device  設備號，坤維 (0-KWR75B)，航天十一院 (0-MCS6A-200-4)，ATI(0-AXIA80-M8)，中科米點 (0-MST2010)，偉航敏芯 (0-WHC6L-YB10A);softvesion  軟件版本號，暫不使用，默認爲0" 

力傳感器激活
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Activate(state)``"
    "描述", "力傳感器激活"
    "必選參數", "- ``state``：0-復位，1-激活"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

力傳感器校零
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetZero(state)``"
    "描述", "力傳感器校零"
    "必選參數", "- ``state``：0-去除零點，1-零點矯正"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置力傳感器參考座標系
+++++++++++++++++++++++++
.. versionchanged:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SetRCS(ref,coord=[0,0,0,0,0,0])``"
    "描述", "設置力傳感器參考座標系"
    "必選參數", "- ``ref``：0-工具座標系，1-基座標系"
    "默認參數", "- ``coord``：[x,y,z,rx,ry,rz]自定義座標系值,默認[0,0,0,0,0,0]"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

        
設置力傳感器下負載重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayload(weight)``"
    "描述", "設置力傳感器下負載重量"
    "必選參數", " - ``weight``：負載重量 kg"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
  
設置力傳感器下負載質心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorPayloadCog(x,y,z)``"
    "描述", "設置力傳感器下負載質心"
    "必選參數", "
    - ``x``：負載質心x mm
    - ``y``：負載質心y mm
    - ``z``：負載質心z mm
    "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
            
獲取力傳感器下負載重量
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayload()``"
    "描述", "獲取力傳感器下負載重量"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weight``：負載重量 kg"
            
獲取力傳感器下負載質心
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceSensorPayloadCog()``"
    "描述", "獲取力傳感器下負載質心"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
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
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weight``：傳感器質量 kg
    - ``pos=[x,y,z]``：傳感器質心 mm"

獲取參考座標系下力/扭矩數據
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueRCS()``"
    "描述", "獲取參考座標系下力/扭矩數據"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``data=[fx,fy,fz,tx,ty,tz]``：參考座標系下力/扭矩數據"

獲取力傳感器原始力/扭矩數據
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_GetForceTorqueOrigin()``"
    "描述", "獲取力傳感器原始力/扭矩數據"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode  
    - ``data=[fx,fy,fz,tx,ty,tz]``：力傳感器原始力/扭矩數據 "

力傳感器配置及自動校零代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    import frrpc
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = frrpc.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error,ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    ftCoord = [0, 0, 0, 0, 0, 0]
    robot.FT_SetRCS(0, ftCoord)
    robot.SetForceSensorPayload(0.824)
    robot.SetForceSensorPayloadCog(0.778, 2.554, 48.765)
    error,weight = robot.GetForceSensorPayload()
    error,x, y, z = robot.GetForceSensorPayloadCog()
    print(f"the FT load is  {weight}, {x} {y} {z}")
    robot.SetForceSensorPayload(0)
    robot.SetForceSensorPayloadCog(0, 0, 0)
    error,computeWeight, tran = robot.ForceSensorAutoComputeLoad()
    print(f"the result is weight {computeWeight} pos is {tran[0]} {tran[1]} {tran[2]}")
    robot.CloseRPC()

負載重量辨識記錄
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenRecord(tool_id)``"
    "描述", "負載重量辨識記錄"
    "必選參數", "- ``tool_id``：傳感器座標系編號，範圍[0~14]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode  "

負載重量辨識計算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdIdenCompute()``"
    "描述", "負載重量辨識計算"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode   
    - ``weight``：負載重量，單位 kg  "

負載質心辨識記錄
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenRecord(tool_id,index)``"
    "描述", "負載質心辨識記錄"
    "必選參數", "- ``tool_id``：傳感器座標系編號，範圍[0~14];
    - ``index``：點編號[1~3]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

負載質心辨識計算
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_PdCogIdenCompute()``"
    "描述", "負載質心辨識計算"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode  
    - ``cog=[cogx,cogy,cogz]``：負載質心，單位 mm  "

力傳感器負載辨識代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    import frrpc
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = frrpc.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    error,ft = robot.FT_GetForceTorqueOrigin()
    print(f"ft origin:{ft[0]},{ft[1]},{ft[2]},{ft[3]},{ft[4]},{ft[5]}")
    robot.FT_SetZero(1)
    time.sleep(1)
    tcoord = [0, 0, 35.0, 0, 0, 0]
    robot.SetToolCoord(10, tcoord, 1, 0, 0, 0)
    robot.FT_PdIdenRecord(10)
    time.sleep(1)
    error,weight = robot.FT_PdIdenCompute()
    print(f"payload weight:{weight}")
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 1)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 2)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    time.sleep(1)
    robot.FT_PdCogIdenRecord(10, 3)
    time.sleep(1)
    error,cog = robot.FT_PdCogIdenCompute()
    print(f"FT_PdCogIdenCompute return {error}")
    print(f"cog:{cog[0]},{cog[1]},{cog[2]}")
    robot.CloseRPC()

碰撞守護
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Guard(flag,sensor_num,select,force_torque,max_threshold,min_threshold)``"
    "描述", "碰撞守護"
    "必選參數", "- ``flag``：0-關閉碰撞守護，1-開啓碰撞守護；
    - ``sensor_num``：力傳感器編號；
    - ``select``：六個自由度是否檢測碰撞[fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``force_torque``：碰撞檢測力/力矩，單位N或Nm；
    - ``max_threshold``：最大閾值；
    - ``min_threshold``：最小閾值；
    - 力/力矩檢測範圍:(force_torque-min_threshold,force_torque+max_threshold)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

碰撞守護代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    sensor_id = 1
    select = [1, 1, 1, 1, 1, 1]
    max_threshold = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    min_threshold = [5.0, 5.0, 5.0, 5.0, 5.0, 5.0]
    ft = None 
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    desc_p3 = [-327.622, 402.230, 320.402, -178.067, 2.127, -46.207]
    error = robot.FT_Guard(1, sensor_id, select,[0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.MoveCart(desc_p1, 0, 0, 100.0)
    robot.MoveCart(desc_p2, 0, 0, 100.0)
    robot.MoveCart(desc_p3, 0, 0, 100.0)
    robot.FT_Guard(0, sensor_id, select,[0.0,0.0,0.0,0.0,0.0,0.0], max_threshold, min_threshold)
    robot.CloseRPC()

恆力控制
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M=None, B=None, threshold=[0.2,0.2], adjustCoeff=[1.0,1.0], polishRadio=0, filter_Sign=0, posAdapt_sign=0, isNoBlock=0)``"
    "描述", "恆力控制"
    "必選參數", "- ``flag``：恆力控制開啓標誌，0-關，1-開；
    - ``sensor_id``：力傳感器編號；
    - ``select``：六個自由度是否檢測 [fx,fy,fz,mx,my,mz]，0-不生效，1-生效；
    - ``ft``：檢測力/力矩，單位N或Nm；
    - ``ft_pid``：[f_p,f_i,f_d,m_p,m_i,m_d],力PID參數，力矩PID參數；
    - ``adj_sign``：自適應啓停狀態，0-關閉，1-開啓；
    - ``ILC_sign``: ILC控制啓停狀態，0-停止，1-訓練，2-實操；
    - ``max_dis``：最大調整距離；
    - ``max_ang``：最大調整角度；"
    "默認參數", "- ``M``：質量參數；
    - ``B``：阻尼參數；
    - ``threshold``：rx、ry啟動閾值[0-10], 預設0.2；
    - ``adjustCoeff``：rx、ry力矩調節係數[0-1], 預設1；
    - ``polishRadio``：打磨盤半徑，單位mm；
    - ``filter_Sign``：濾波開啓標誌 0-關；1-開，默認 0-關閉；
    - ``posAdapt_sign``：姿態順應開啓標誌 0-關；1-開，默認 0-關閉；
    - ``isNoBlock``：阻塞標誌，0-阻塞；1-非阻塞 默認0-阻塞；"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

具有阻尼的恆力控制代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    sensor_id = 10
    select = [0, 0, 1, 0, 0, 0]
    ft_pid = [0.0008, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 1000.0
    max_ang = 20.0
    ft = [0.0] * 6 
    epos = [0.0] * 4
    j1 = [80.765, -98.795, 106.548, -97.734, -89.999, 94.842]
    j2 = [43.067, -84.429, 92.620, -98.175, -90.011, 57.144]
    desc_p1 = [5.009, -547.463, 262.053, -179.999, -0.019, 75.923]
    desc_p2 = [-347.966, -547.463, 262.048, -180.000, -0.019, 75.923]
    offset_pos = [0.0] * 6
    M = [2.0, 2.0]
    B = [15.0, 15.0]
    threshold = [1.0, 1.0]
    adjustCoeff = [1.0, 0.8]
    polishRadio = 0.0
    filter_Sign = 0
    posAdapt_sign = 1
    isNoBlock = 0
    ft[2] = -10.0 
    while True:
        rtn = robot.FT_Control(1, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold,adjustCoeff, 0, 0, 1, 0)
        print(f"FT_Control start rtn is {rtn}")
        rtn = robot.MoveL(desc_pos=desc_p1, tool=1, user=0, vel=100, acc=100, ovl=100, blendR=-1, blendMode = 0, exaxis_pos=epos, search=0, offset_flag=0, offset_pos=offset_pos)
        rtn = robot.MoveL(desc_pos=desc_p2, tool=1, user=0, vel=100, acc=100, ovl=100, blendR=-1, blendMode = 0, exaxis_pos=epos, search=0, offset_flag=0, offset_pos=offset_pos)
        rtn = robot.FT_Control(0, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, M, B, threshold,adjustCoeff, 0, 0, 1, 0)
        print(f"FT_Control end rtn is {rtn}")
    robot.CloseRPC()
    return 0

螺旋線探索
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_SpiralSearch(rcs, ft, dr=0.7, max_t_ms=60000, max_vel=5)``"
    "描述", "螺旋線探索"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基座標系
    - ``ft``：力或力矩閾值 (0~100)，單位 N 或 Nm;"
    "默認參數", "- ``dr``：每圈半徑進給量，單位 mm 默認0.7;
    - ``max_t_ms``：最大探索時間，單位 ms 默認 60000;
    - ``max_vel``：線速度最大值，單位 mm/s 默認 5"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

旋轉插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_RotInsertion(rcs, ft, orn, angVelRot=3, angleMax=45, angAccmax=0, rotorn=1, strategy=0)``"
    "描述", "旋轉插入"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基座標系；
    - ``ft``：力或力矩閾值 (0~100)，單位 N 或 Nm;
    - ``orn``：力/扭矩方向，1-沿z軸方向，2-繞z軸方向;"
    "預設參數", "- ``angVelRot``：旋轉角速度，單位°/s,預設 3;
    - ``angleMax``：最大旋轉角度，單位 ° 預設 45;
    - ``angAccmax``：最大旋轉加速度，單位 °/s^2，暫不使用 預設0;
    - ``rotorn``：旋轉方向，1-順時針，2-逆時針 預設1;
    - ``strategy``：未偵測到力/力矩的處理策略，0-報錯；1-警告，繼續運動"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

螺旋探索、直線插入等指令程式碼範例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    j1=[-11.904,-99.669,117.473,-108.616,-91.726,74.256]
    j2=[-45.615,-106.172,124.296,-107.151,-91.282,74.255]
    j3=[-29.777,-84.536,109.275,-114.075,-86.655,74.257]
    j4=[-31.154,-95.317,94.276,-88.079,-89.740,74.256]
    desc_pos1=[-419.524,-13.000,351.569,-178.118,0.314,3.833]
    desc_pos2=[-321.222,185.189,335.520,-179.030,-1.284,-29.869]
    desc_pos3=[-487.434,154.362,308.576,176.600,0.268,-14.061]
    desc_pos4=[-443.165,147.881,480.951,179.511,-0.775,-15.409]
    offset_pos=[0.0]*6
    epos=[0.0]*4
    tool=0
    user=0
    vel=100.0
    acc=100.0
    ovl=100.0
    oacc=100.0
    blendT=0.0
    blendR=0.0
    flag=0
    search=0
    blendMode=0
    velAccMode=0
    robot.SetSpeed(20)
    rtn=robot.MoveJ(joint_pos=j1,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,exaxis_pos=epos,blendT=blendT,offset_flag=flag,offset_pos=offset_pos)
    print(f"movejerrcode:{rtn}")
    rtn=robot.MoveL(desc_pos=desc_pos2,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,blendR=blendR,blendMode=blendMode,exaxis_pos=epos,search=search,offset_flag=flag,offset_pos=offset_pos,oacc=oacc,velAccParamMode=velAccMode)
    print(f"movelerrcode:{rtn}")
    rtn=robot.MoveC(desc_pos_p=desc_pos3,tool_p=tool,user_p=user,vel_p=vel,acc_p=acc,exaxis_pos_p=epos,offset_flag_p=flag,offset_pos_p=offset_pos,desc_pos_t=desc_pos4,tool_t=tool,user_t=user,vel_t=vel,acc_t=acc,exaxis_pos_t=epos,offset_flag_t=flag,offset_pos_t=offset_pos,ovl=ovl,blendR=blendR,oacc=oacc,velAccParamMode=velAccMode)
    print(f"movecerrcode:{rtn}")
    rtn=robot.MoveJ(joint_pos=j2,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,exaxis_pos=epos,blendT=blendT,offset_flag=flag,offset_pos=offset_pos)
    print(f"movejerrcode:{rtn}")
    rtn=robot.Circle(desc_pos_p=desc_pos3,tool_p=tool,user_p=user,vel_p=vel,acc_p=acc,exaxis_pos_p=epos,desc_pos_t=desc_pos1,tool_t=tool,user_t=user,vel_t=vel,acc_t=acc,exaxis_pos_t=epos,ovl=ovl,offset_flag=flag,offset_pos=offset_pos,oacc=oacc,blendR=-1,velAccParamMode=velAccMode)
    print(f"circleerrcode:{rtn}")
    rtn=robot.MoveCart(desc_pos=desc_pos4,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,blendT=blendT,config=-1)
    print(f"MoveCarterrcode:{rtn}")
    rtn=robot.MoveJ(joint_pos=j1,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,exaxis_pos=epos,blendT=blendT,offset_flag=flag,offset_pos=offset_pos)
    print(f"movejerrcode:{rtn}")
    rtn=robot.MoveL(desc_pos=desc_pos2,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,blendR=blendR,blendMode=blendMode,exaxis_pos=epos,search=search,offset_flag=flag,offset_pos=offset_pos,config=-1,velAccParamMode=velAccMode)
    print(f"movelerrcode:{rtn}")
    rtn=robot.MoveC(desc_pos_p=desc_pos3,tool_p=tool,user_p=user,vel_p=vel,acc_p=acc,exaxis_pos_p=epos,offset_flag_p=flag,offset_pos_p=offset_pos,desc_pos_t=desc_pos4,tool_t=tool,user_t=user,vel_t=vel,acc_t=acc,exaxis_pos_t=epos,offset_flag_t=flag,offset_pos_t=offset_pos,ovl=ovl,blendR=blendR,config=-1,velAccParamMode=velAccMode)
    print(f"movecerrcode:{rtn}")
    rtn=robot.MoveJ(joint_pos=j2,tool=tool,user=user,vel=vel,acc=acc,ovl=ovl,exaxis_pos=epos,blendT=blendT,offset_flag=flag,offset_pos=offset_pos)
    print(f"movejerrcode:{rtn}")
    rtn=robot.Circle(desc_pos_p=desc_pos3,tool_p=tool,user_p=user,vel_p=vel,acc_p=acc,exaxis_pos_p=epos,desc_pos_t=desc_pos1,tool_t=tool,user_t=user,vel_t=vel,acc_t=acc,exaxis_pos_t=epos,ovl=ovl,offset_flag=flag,offset_pos=offset_pos,oacc=oacc,blendR=-1,velAccParamMode=velAccMode)
    print(f"circleerrcode:{rtn}")
    robot.CloseRPC()
    return 0

直線插入
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_LinInsertion(rcs, ft, disMax, linorn, lin_v=1.0, lin_a=1.0)``"
    "描述", "直線插入"
    "必選參數", "- ``rcs``：參考座標系，0-工具座標系，1-基座標系；
    - ``ft``：力或力矩閾值 (0~100)，單位 N 或 Nm;
    - ``disMax``：最大插入距離，單位 mm;
    - ``linorn``：插入方向:0-負方向，1-正方向"
    "默認參數", "- ``lin_v``：直線速度，單位 mm/s 默認1;
    - ``lin_a``：直線加速度，單位 mm/s^2，暫不使用 默認1"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

螺旋探索、直線插入等指令代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:
    
    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    status = 1
    sensor_num = 1
    gain = [0.0001, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 5.0
    ft = [0.0,0.0,-10.0,0.0,0.0,0.0]
    rcs = 0
    dr = 0.7
    fFinish = 1.0
    t = 60000.0
    vmax = 3.0
    force_goal = 20.0
    lin_v = 0.0
    lin_a = 0.0
    disMax = 100.0
    linorn = 1
    angVelRot = 2.0
    forceInsertion = 1.0
    angleMax = 45
    orn = 1
    angAccmax = 0.0
    rotorn = 1
    select1 = [0, 0, 1, 1, 1, 0]
    robot.FT_Control(status, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_SpiralSearch(rcs, dr, fFinish, t, vmax)
    print(f"FT_SpiralSearch rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select1, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select2 = [1, 1, 1, 0, 0, 0]
    gain[0] = 0.00005
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select2, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select3 = [0, 0, 1, 1, 1, 0]
    ft[2] = -10.0
    gain[0] = 0.0001
    robot.FT_Control(1, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_RotInsertion(rcs, angVelRot, forceInsertion, angleMax, orn, angAccmax, rotorn)
    print(f"FT_RotInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select3, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    select4 = [1, 1, 1, 0, 0, 0]
    ft[2] = -30.0
    robot.FT_Control(1, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    rtn = robot.FT_LinInsertion(rcs, force_goal, lin_v, lin_a, disMax, linorn)
    print(f"FT_LinInsertion rtn is {rtn}")
    robot.FT_Control(0, sensor_num, select4, ft, gain, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

表面定位
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_FindSurface (rcs, dir, axis, disMax, ft, lin_v=3.0, lin_a=0.0)``"
    "描述", "表面定位"
    "必選參數", "- ``rcs``： 參考座標系，0-工具座標系，1-基座標系；
    - ``dir``：移動方向，1-正方向，2-負方向；
    - ``axis``：移動軸，1-x，2-y，3-z；
    - ``disMax``：大探索距離，單位 mm;
    - ``ft``：動作終止力閾值，單位N；"
    "默認參數", "- ``lin_v``：探索直線速度，單位mm/s 默認3;
    - ``lin_a``：探索直線加速度，單位mm/s^2 默認0;"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算中間平面位置開始
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterStart()``"
    "描述", "計算中間平面位置開始"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算中間平面位置結束
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_CalCenterEnd()``"
    "描述", "計算中間平面位置結束"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode
    - ``pos=[x,y,z,rx,ry,rz]``：中間平面位置"

表面定位代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    rcs = 0
    dir = 1
    axis = 1
    lin_v = 3.0
    lin_a = 0.0
    maxdis = 50.0
    ft_goal = 2.0
    desc_pos = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    xcenter = [0, 0, 0, 0, 0, 0]
    ycenter = [0, 0, 0, 0, 0, 0]
    ft = [-2.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.FT_CalCenterStart()
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error,xcenter = robot.FT_CalCenterEnd()
    print(f"xcenter:{xcenter[0]},{xcenter[1]},{xcenter[2]},{xcenter[3]},{xcenter[4]},{xcenter[5]}")
    robot.MoveCart(xcenter, 9, 0, 60.0)
    robot.FT_CalCenterStart()
    dir = 1
    axis = 2
    lin_v = 6.0
    maxdis = 150.0
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    robot.MoveCart(desc_pos, 9, 0, 100.0)
    robot.WaitMs(1000)
    dir = 2
    robot.FT_FindSurface(rcs, dir, axis, lin_v, lin_a, maxdis, ft_goal)
    error,ycenter = robot.FT_CalCenterEnd()
    print(f"ycenter:{ycenter[0]},{ycenter[1]},{ycenter[2]},{ycenter[3]},{ycenter[4]},{ycenter[5]}")
    robot.MoveCart(ycenter, 9, 0, 60.0)
    robot.CloseRPC()

柔順控制開啓
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStart(p, force)``"
    "描述", "柔順控制開啓"
    "必選參數", "- ``p``: 位置調節係數或柔順係數
    - ``force``：柔順開啓力閾值，單位N"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode  "

柔順控制關閉
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FT_ComplianceStop()``"
    "描述", "柔順控制關閉"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

柔順控制代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    company = 24
    device = 0
    softversion = 0
    bus = 1
    index = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    error,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    flag = 1
    sensor_id = 1
    select = [1, 1, 1, 0, 0, 0]
    ft_pid = [0.0005, 0.0, 0.0, 0.0, 0.0, 0.0]
    adj_sign = 0
    ILC_sign = 0
    max_dis = 100.0
    max_ang = 0.0
    ft = [-10.0, -10.0, -10.0, 0.0, 0.0, 0.0]
    offset_pos = [0.0,0.0,0.0,0.0,0.0,0.0]  # 替代 DescPose(0, 0, 0, 0, 0, 0)
    epos = [0.0,0.0,0.0,0.0]  # 替代 ExaxisPos(0, 0, 0, 0)
    j1 = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]  # JointPos
    j2 = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    desc_p1 = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]  # DescPose
    desc_p2 = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    p = 0.00005
    force = 30.0
    rtn = robot.FT_ComplianceStart(p, force)
    print(f"FT_ComplianceStart rtn is {rtn}")
    count = 3
    while count > 0:
        robot.MoveL(desc_pos=desc_p1,tool= 0,user= 0,vel= 100.0)
        robot.MoveL(desc_pos=desc_p2,tool= 0,user= 0,vel= 100.0)
        count -= 1
    robot.FT_ComplianceStop()
    print(f"FT_ComplianceStop rtn is {rtn}")
    flag = 0
    robot.FT_Control(flag, sensor_id, select, ft, ft_pid, adj_sign, ILC_sign, max_dis, max_ang, 0, 0, 0)
    robot.CloseRPC()

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
    "返回值", "錯誤碼 成功-0  失敗- errcode  "

負載辨識變量初始化
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyDynVarInit()``"
    "描述", "負載辨識變量初始化"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode  "

負載辨識主程序
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyMain(joint_torque, joint_pos, t)``"
    "描述", "負載辨識主程序"
    "必選參數", "- ``joint_torque``： 關節扭矩 j1-j6；
    - ``joint_pos``：關節位置 j1-j6
    - ``t``：採樣週期"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取負載辨識結果
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``LoadIdentifyGetResult(gain)``"
    "描述", "獲取負載辨識結果"
    "必選參數", "- ``gain``：重力項係數double[6]，離心項係數double[6]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weight``：負載重量
    - ``cog=[x,y,z]``：負載質心座標"

機器人負載辨識代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    retval = robot.LoadIdentifyDynFilterInit()
    print(f"LoadIdentifyDynFilterInit retval is: {retval}")
    retval = robot.LoadIdentifyDynVarInit()
    print(f"LoadIdentifyDynVarInit retval is: {retval}")
    error, posJ = robot.GetActualJointPosDegree(0)
    posJ[1] += 10  # Modify joint 2
    error, joint_toq = robot.GetJointTorques(0)
    joint_toq[1] += 2  # Modify torque on joint 2
    tmpTorque = joint_toq.copy()
    retval = robot.LoadIdentifyMain(tmpTorque, posJ, 1)
    print(f"LoadIdentifyMain retval is: {retval}")
    gain = [0, 0.05, 0, 0, 0, 0, 0, 0.02, 0, 0, 0, 0]
    weight = [0.0]
    load_pos = [0.0, 0.0, 0.0]
    retval, weight, load_pos = robot.LoadIdentifyGetResult(gain)
    print(f"LoadIdentifyGetResult retval is: {retval} ; weight is {weight}  cog is {load_pos[0]} {load_pos[1]} {load_pos[2]}")
    robot.CloseRPC()

力傳感器輔助拖動
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

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
        
獲取力傳感器拖動開關狀態
++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForceAndTorqueDragState()``"
    "描述", "獲取力傳感器拖動開關狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``dragState``：力傳感器輔助拖動控制狀態，0-關閉；1-開啓
    - ``sixDimensionalDragState``：六維力輔助拖動控制狀態，0-關閉；1-開啓"
    
報錯清除後力傳感器自動開啓
++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetForceSensorDragAutoFlag(status)``"
    "描述", "報錯清除後力傳感器自動開啓"
    "必選參數", "- ``status``：控制狀態，0-關閉；1-開啓"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
力傳感器輔助拖動代碼示例
++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.SetForceSensorDragAutoFlag(1)
    M = [15.0, 15.0, 15.0, 0.5, 0.5, 0.1]
    B = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    K = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    F = [10.0, 10.0, 10.0, 1.0, 1.0, 1.0]
    robot.EndForceDragControl(1, 0, 0, 0, M, B, K, F, 50, 100)
    time.sleep(5)
    drag_state = 0
    six_dimensional_drag_state = 0
    error,drag_state, six_dimensional_drag_state = robot.GetForceAndTorqueDragState()
    print(f"the drag state is {drag_state} {six_dimensional_drag_state}")
    robot.EndForceDragControl(0, 0, 0, 0, M, B, K, F, 50, 100)
    robot.CloseRPC()
    
設置六維力和關節阻抗混合拖動開關及參數
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

六維力和關節阻抗混合拖動代碼示例
++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    lamde_dain = [3.0, 2.0, 2.0, 2.0, 2.0, 3.0]
    k_gain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    b_gain = [150.0, 150.0, 150.0, 5.0, 5.0, 1.0]
    rtn = robot.ForceAndJointImpedanceStartStop(1, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    time.sleep(5)
    robot.DragTeachSwitch(0)
    rtn = robot.ForceAndJointImpedanceStartStop(0, 0, lamde_dain, k_gain, b_gain, 1000, 180)
    print(f"ForceAndJointImpedanceStartStop rtn is {rtn}")
    robot.CloseRPC()

阻抗啓停控制
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ImpedanceControlStartStop(status, workSpace, forceThreshold, m, b, k, maxV, maxVA, maxW, maxWA)``"
    "描述", "阻抗啓停控制"
    "必選參數", "- ``status``：0-關閉；1-開啓
    - ``workSpace``：0-關節空間；1-迪卡爾空間
    - ``forceThreshold``：觸發力閾值(N)
    - ``m``：質量參數
    - ``b``：阻尼參數
    - ``k``：剛度參數
    - ``maxV``：最大線速度(mm/s)
    - ``maxVA``：最大線加速度(mm/s2)
    - ``maxW``：最大角速度(°/s)
    - ``maxWA``：最大角加速度(°/s2)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

阻抗啓停控制代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    j1 = [102.622, -135.990, 120.769, -73.950, -90.848, 35.507]
    j2 = [93.674, -80.062, 82.947, -92.199, -90.967, 26.559]
    desc_pos1 = [136.552, -149.799, 449.532, 179.817, -1.172, 157.123]
    desc_pos2 = [136.540, -561.048, 449.542, 179.819, -1.172, 157.122]
    offset_pos = [0.0] * 6
    epos = [0.0] * 4
    tool = 0
    user = 0
    vel = 100.0
    acc = 200.0
    ovl = 100.0
    blendT = -1.0
    blendR = -1.0
    flag = 0
    search = 0
    robot.SetSpeed(20)
    company = 17
    device = 0
    softversion = 0
    bus = 1
    robot.FT_SetConfig(company, device, softversion, bus)
    time.sleep(1)
    rnt,[company, device, softversion, bus] = robot.FT_GetConfig()
    print(f"FT config:{company},{device},{softversion},{bus}")
    time.sleep(1)
    robot.FT_Activate(0)
    time.sleep(1)
    robot.FT_Activate(1)
    time.sleep(1)
    time.sleep(1)
    robot.FT_SetZero(0)
    time.sleep(1)
    robot.FT_SetZero(1)
    time.sleep(1)
    forceThreshold = [30.0, 30.0, 30.0, 5.0, 5.0, 5.0]
    m = [0.1, 0.1, 0.1, 0.02, 0.02, 0.02]
    b = [1.0, 1.0, 1.0, 0.08, 0.08, 0.08]
    k = [0.0] * 6
    rtn = robot.ImpedanceControlStartStop(1, 1, forceThreshold, m, b, k, 1000, 500, 100, 100)
    print(f"ImpedanceControlStartStop errcode:{rtn}")
    rtn = robot.MoveL(desc_pos=desc_pos1,tool= tool,user= user,vel= vel,speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2,tool= tool,user= user,vel= vel,speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos1,tool= tool,user= user,vel= vel,speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2,tool= tool,user= user,vel= vel,speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos1,tool= tool,user= user,vel= vel,speedPercent=1)
    rtn = robot.MoveL(desc_pos=desc_pos2,tool= tool,user= user,vel= vel,speedPercent=1)
    print(f"movel errcode:{rtn}")
    robot.ImpedanceControlStartStop(0, 1, forceThreshold, m, b, k, 1000, 500, 100, 100)
    robot.CloseRPC()

開啟力矩補償功能及補償係數
++++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SerCoderCompenParams(status, torqueCoeff)``"
    "描述", "開啟力矩補償功能及補償係數"
    "必選參數", "- ``status``：開關，0-關閉；1-開啟
    - ``torqueCoeff``：J1-J6力矩補償係數[0-1]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"