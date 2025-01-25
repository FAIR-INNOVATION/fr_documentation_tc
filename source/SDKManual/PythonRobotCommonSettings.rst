機器人常用設定
=================

.. toctree:: 
    :maxdepth: 5

設定全域速度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSpeed(vel)``"
    "描述", "設定全域速度"
    "必選參數", "- ``vel``:速度百分比，範圍[0~100]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetSpeed(20)
    print("設定全域速度錯誤碼:",error)

設定係統變數值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysVarValue(id,value)``"
    "描述", "設定系統變數"
    "必選參數", "- ``id``：變數編號，範圍[1~20];
    - ``value``：變數值"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1,21):
        error = robot.SetSysVarValue(i,10)
    robot.WaitMs(1000)
    for i in range(1,21):
        sys_var = robot.GetSysVarValue(i)
        print("系統變數編號:",i,"值",sys_var)

設定工具參考點-六點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolPoint(point_num)``"
    "描述", "設定工具參考點-六點法"
    "必選參數", "- ``point_num``：點編號,範圍[1~6]"
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
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    for i in range(1,7):
        robot.DragTeachSwitch(1)#切入拖曳示教模式
        time.sleep(5)
        error = robot.SetToolPoint(i) #实际應控制機器人依照要求移動到適當位置後再發送指令
        print("六點法設定工具坐標系，記錄點",i,"錯誤碼",error)
        robot.DragTeachSwitch(0)
        time.sleep(1)
    error = robot.ComputeTool()
    print("六點法設定工具坐標系錯誤碼",error)

計算工具座標系-六點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTool()``"
    "描述", "計算工具座標系-六點法（設定完六個工具參考點后再进行计算）"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

設定工具參考點-四點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTcp4RefPoint(point_num)``"
    "描述", "設定工具參考點-四點法"
    "必選參數", "``point_num``：點編號,範圍[1~4]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    for i in range(1,5):
        robot.DragTeachSwitch(1)#切入拖曳示教模式
        time.sleep(5)
        error = robot.SetTcp4RefPoint(i) #應控制機器人依照要求移動到適當位置後再發送指令
        print("四點法設定工具坐標系，記錄點",i,"錯誤碼",error)
        robot.DragTeachSwitch(0)
        time.sleep(1)
    error,t_coord= robot.ComputeTcp4()
    print("四點法設定工具坐標系錯誤碼",error,"工具TCP",t_coord)

計算工具座標系-四點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTcp4()``"
    "描述", "計算工具座標系-四點法（設定完四個工具參考點后再进行计算）"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

設定工具坐標系
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolCoord(id,t_coord,type,install,toolID,loadNum)``"
    "描述", "設定工具坐標系"
    "必選參數", "- ``id``:座標系編號，範圍[1~15]；
    - ``t_coord``:工具中心點相對末端法蘭中心位姿，單位[mm][°]；
    - ``type``:0-工具坐標系，1-感測器座標系；
    - ``install``:安裝位置，0-機器人末端，1-機器人外部
    - ``toolID``:工具ID
    - ``loadNum``:負載編號"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetToolCoord(10,t_coord,0,0,0,0)
    print("設定工具坐標系錯誤碼",error)

設定工具坐標系列表
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolList(id,t_coord ,type, install, loadNum)``"
    "描述", "設定工具坐標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[1~15]；
    - ``t_coord``:[x,y,z,rx,ry,rz] 工具中心點相對末端法蘭中心位姿，單位[mm][°]；
    - ``type``:0-工具坐標系，1-感測器座標系；
    - ``install``:安裝位置，0-機器人末端，1-機器人外部
    - ``loadNum``:負載編號"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    t_coord = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetToolList(10,t_coord,0,0,0)
    print("設定工具坐標系列表錯誤碼",error)

設定外部工具參考點-三點法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExTCPPoint(point_num)``"
    "描述", "設定外部工具參考點-三點法"
    "必選參數", "- ``point_num``：點編號,範圍[1~3]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    for i in range(1,4):
        error = robot.SetExTCPPoint(i) #應控制機器人依照要求移動到適當位置後再發送指令
        print("三點法設定外部工具坐標系，記錄點",i,"錯誤碼",error)
        time.sleep(1)
    error,etcp = robot.ComputeExTCF()
    print("三點法設定外部工具坐標系錯誤碼",error,"外部工具TCP",etcp)
    error = robot.SetExToolCoord(10,etcp,etool)
    print("設定外部工具坐標系錯誤碼",error)
    error = robot.SetExToolList(10,etcp,etool)
    print("設定外部工具坐標系列表錯誤碼",error)

計算外部工具坐標系-三點法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeExTCF (point_num)``"
    "描述", "計算外部工具坐標系-三點法（設定完三個參考點后再进行计算）"
    "必選參數", "``point_num``：點編號,範圍[1~3]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``etcp=[x,y,z,rx,ry,rz]``：外部工具座標系"

設定外部工具坐標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolCoord(id,etcp,etool)``"
    "描述", "設定外部工具坐標系"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``etcp``:外部工具座標系，單位[mm][°]；
    - ``etool``:末端工具座標系，單位[mm][°]；"
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
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    error = robot.SetExToolCoord(10,etcp,etool)
    print("設定外部工具坐標系錯誤碼",error)

設定外部工具坐標系列表
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolList(id,etcp ,etool)``"
    "描述", "設定外部工具坐標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``etcp``:外部工具座標系，單位[mm][°]；
    - ``etool``:末端工具座標系，單位[mm][°]；"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    etcp = [1.0,2.0,3.0,4.0,5.0,6.0]
    etool = [21.0,22.0,23.0,24.0,25.0,26.0]
    error = robot.SetExToolList(10,etcp,etool)
    print("設定外部工具坐標系列表錯誤碼",error)

設定工件參考點-三點法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoordPoint(point_num)``"
    "描述", "設定工件參考點-三點法"
    "必選參數", "``point_num``:點編號,範圍[1~3]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    robot.SetToolList(0,[0,0,0,0,0,0],0,0)#設定參考點前应當将工具和工件號座標系切换至0
    robot.SetWObjList(0,[0,0,0,0,0,0])
    for i in range(1,4):
        error = robot.SetWObjCoordPoint(i) #实际應控制機器人依照要求移動到適當位置後再發送指令
        print("三點法設定工件座標系，記錄點",i,"錯誤碼",error)
        time.sleep(1)
    error, w_coord = robot.ComputeWObjCoord(0,0)
    print("三點法計算工件座標系錯誤碼",error,"工件座標系", w_coord)

計算工件座標系-三點法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoord(method, refFrame)``"
    "描述", "計算工件座標系-三點法（三個參考點設定完成后再进行计算）;"
    "必選參數", "- ``method``：计算方式0：原點-x軸-z軸，1：原點-x軸-xy平面
    - ``refFrame``：參考座標系"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``wobj_pose=[x,y,z,rx,ry,rz]``：工件座標系"


設定工件座標系
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoord(id, coord, refFrame)``"
    "描述", "設定工件座標系"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``coord``:工件坐標系相對於末端法蘭中心位姿，單位 [mm][°]
    - ``refFrame``:參考座標系"
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
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    error = robot.SetWObjCoord(id=11,coord=w_coord,refFrame=0)
    print("設定工件座標系錯誤碼",error)

設定工件座標系列表
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjList(id, coord, refFrame)``"
    "描述", "設定工件座標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``coord``:工件坐標系相對於末端法蘭中心位姿，單位 [mm][°]
    - ``refFrame``:參考座標系"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    w_coord = [11.0,12.0,13.0,14.0,15.0,16.0]
    error = robot.SetWObjList(id=11,coord=w_coord,refFrame=0)
    print("設定工件座標系列表錯誤碼",error)

設定末端負載重量
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadWeight(weight)``"
    "描述", "設定末端負載重量,錯誤負載重量設定可能会导致拖動模式下機器人失控"
    "必選參數", "- ``weight``:單位[kg]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetLoadWeight(0)#！！！負載重量設定应于实际相符(錯誤負載重量設定可能会导致拖動模式下機器人失控)

設定機器人安裝方式-固定安裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallPos(method)``"
    "描述", "設定機器人安裝方式-固定安裝,錯誤安裝方式設定會導致拖曳模式下機器人失控"
    "必選參數", "- ``method``:0-平裝，1-側裝，2-挂裝"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetRobotInstallPos(0) #！！！安裝方式設定应与实际一致 0-正裝，1-側裝，2-倒裝 (錯誤安裝方式設定会导致拖動模式下機器人失控）
    print("設定機器人安裝方式錯誤碼",error)

設定機器人安裝角度-自由安裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallAngle(yangle,zangle)``"
    "描述", "設定機器人安裝角度-自由安裝,錯誤安裝角度設定会导致拖動模式下機器人失控"
    "必選參數", "- ``yangle``：傾斜角
    - ``zangle``：旋轉角"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetRobotInstallAngle(0.0,0.0) #！！！安裝角度設定应与实际一致 (錯誤安裝角度設定会导致拖動模式下機器人失控）
    print("設定機器人安裝角度錯誤碼",error)

設定末端負載質心座標
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadCoord(x,y,z)``"
    "描述", "設定末端負載質心座標,錯誤負載質心設定可能会导致拖動模式下機器人失控"
    "必選參數", "- ``x``: 质心座標，單位[mm]
    - ``y``: 质心座標，單位[mm]
    - ``z``: 质心座標，單位[mm]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetLoadCoord(3.0,4.0,5.0) #！！！負載質心設定应于实际相符(錯誤負載質心設定可能会导致拖動模式下機器人失控)
    print("設定負載質心錯誤碼",error)

等待指定時間
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``WaitMs(t_ms)``"
    "描述", "等待指定時間"
    "必選參數", "- ``t_ms``:單位[ms]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.WaitMs(1000)
    print("等待指定時間錯誤碼",error)

設定機器人加速度
+++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOaccScale(acc)``"
    "描述", "設定機器人加速度"
    "必選參數", "- ``acc``:機器人加速度百分比"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.SetOaccScale (20)

設定機器指定姿態速度開啟
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AngularSpeedStart(ratio)``"
    "描述", "指定姿態速度開啟"
    "必選參數", "- ``ratio``:姿態速度百分比[0-300]"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

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
    "傳回值", "錯誤碼 成功-0 失敗- errcode "