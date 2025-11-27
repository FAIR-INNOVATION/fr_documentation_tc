機器人常用設置
=================

.. toctree:: 
    :maxdepth: 5

設置工具參考點-六點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolPoint(point_num)``"
    "描述", "設置工具參考點-六點法"
    "必選參數", "- ``point_num``：點編號,範圍[1~6]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算工具座標系-六點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTool()``"
    "描述", "計算工具座標系-六點法（設置完六個工具參考點後再進行計算）"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

設置工具參考點-四點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetTcp4RefPoint(point_num)``"
    "描述", "設置工具參考點-四點法"
    "必選參數", "``point_num``：點編號,範圍[1~4]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

計算工具座標系-四點法
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeTcp4()``"
    "描述", "計算工具座標系-四點法（設置完四個工具參考點後再進行計算）"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：工具座標系"

根據點位信息計算工具座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeToolCoordWithPoints(method, pos)``"
    "描述", "根據點位信息計算工具座標系"
    "必選參數", "- ``method``：計算方法；0-四點法；1-六點法
    - ``pos``：關節位置組，四點法時數組長度爲4個，六點法時數組長度爲6個"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``tcp_offset=[x,y,z,rx,ry,rz]``：根據點位信息計算得到的工具座標系，單位 [mm][°]"

設置工具座標系
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolCoord(id,t_coord,type,install,toolID,loadNum)``"
    "描述", "設置工具座標系"
    "必選參數", "- ``id``:座標系編號，範圍[1~15]；
    - ``t_coord``:工具中心點相對末端法蘭中心位姿，單位[mm][°]；
    - ``type``:0-工具座標系，1-傳感器座標系；
    - ``install``:安裝位置，0-機器人末端，1-機器人外部
    - ``toolID``:工具ID
    - ``loadNum``:負載編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置工具座標系列表
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetToolList(id,t_coord ,type, install, loadNum)``"
    "描述", "設置工具座標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[1~15]；
    - ``t_coord``:[x,y,z,rx,ry,rz] 工具中心點相對末端法蘭中心位姿，單位[mm][°]；
    - ``type``:0-工具座標系，1-傳感器座標系；
    - ``install``:安裝位置，0-機器人末端，1-機器人外部
    - ``loadNum``:負載編號"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取當前工具座標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTCPOffset(flag=1)``"
    "描述", "獲取當前工具座標系"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: 當前工具座標系相對位姿，單位[mm][°]"

機器人工具座標系操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posJ = [p1Joint, p2Joint, p3Joint, p4Joint, p5Joint, p6Joint]
    rtn,coordRtn = robot.ComputeToolCoordWithPoints(1, posJ)
    print(f"ComputeToolCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(4)
    robot.MoveJ(joint_pos=p5Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(5)
    robot.MoveJ(joint_pos=p6Joint,tool=0, user=0, vel=100)
    robot.SetToolPoint(6)
    rtn,coordRtn = robot.ComputeTool()
    print(f"6 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolList(1, coordRtn, 0, 0, 0)
    robot.MoveJ(joint_pos=p1Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0, user=0, vel=100)
    robot.SetTcp4RefPoint(4)
    rtn,coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool        {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(2, coordRtn, 0, 0, 1, 0)
    rtn,getCoord = robot.GetTCPOffset(0)
    print(f"GetTCPOffset    {rtn}  coord is {getCoord[0]} {getCoord[1]} {getCoord[2]} {getCoord[3]} {getCoord[4]} {getCoord[5]}")
    robot.CloseRPC()

設置外部工具參考點-六點法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExTCPPoint(point_num)``"
    "描述", "設置外部工具參考點-三點法"
    "必選參數", "- ``point_num``：點編號,範圍[1~3]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

計算外部工具座標系-六點法
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeExTCF(point_num)``"
    "描述", "計算外部工具座標系-三點法（設置完三個參考點後再進行計算）"
    "必選參數", "``point_num``：點編號,範圍[1~3]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``etcp=[x,y,z,rx,ry,rz]``：外部工具座標系"

設置外部工具座標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolCoord(id,etcp,etool)``"
    "描述", "設置外部工具座標系"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``etcp``:外部工具座標系，單位[mm][°]；
    - ``etool``:末端工具座標系，單位[mm][°]；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置外部工具座標系列表
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetExToolList(id,etcp ,etool)``"
    "描述", "設置外部工具座標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``etcp``:外部工具座標系，單位[mm][°]；
    - ``etool``:末端工具座標系，單位[mm][°]；"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

機器人外部工具座標系操作代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    robot.MoveJ(joint_pos=p1Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=1, user=0, vel=50)
    robot.SetExTCPPoint(3)
    rtn,coordRtn = robot.ComputeExTCF()
    print(f"ComputeExTCF {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetExToolCoord(1, coordRtn, offdese)
    robot.SetExToolList(1, coordRtn, offdese)
    robot.CloseRPC()

設置工件參考點-三點法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoordPoint(point_num)``"
    "描述", "設置工件參考點-三點法"
    "必選參數", "``point_num``:點編號,範圍[1~3]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

計算工件座標系-三點法
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoord(method, refFrame)``"
    "描述", "計算工件座標系-三點法（三個參考點設置完成後再進行計算）;"
    "必選參數", "- ``method``：計算方式0：原點-x軸-z軸，1：原點-x軸-xy平面
    - ``refFrame``：參考座標系"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``wobj_pose=[x,y,z,rx,ry,rz]``：工件座標系"

設置工件座標系
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjCoord(id, coord, refFrame)``"
    "描述", "設置工件座標系"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``coord``:工件座標系相對於末端法蘭中心位姿，單位 [mm][°]
    - ``refFrame``:參考座標系"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置工件座標系列表
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWObjList(id, coord, refFrame)``"
    "描述", "設置工件座標系列表"
    "必選參數", "- ``id``:座標系編號，範圍[0~14]；
    - ``coord``:工件座標系相對於末端法蘭中心位姿，單位 [mm][°]
    - ``refFrame``:參考座標系"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

根據點位信息計算工件座標系
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeWObjCoordWithPoints(method, pos, refFrame)``"
    "描述", "根據點位信息計算工件座標系"
    "必選參數", "- ``method``：計算方法；0：原點-x軸-z軸  1：原點-x軸-xy平面
    - ``pos``：三個TCP位置組
    - ``refFrame``：參考座標系"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``wobj_offset=[x,y,z,rx,ry,rz]``：根據點位信息計算得到的工件座標系，單位 [mm][°]"

獲取當前工件座標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWObjOffset(flag=1)``"
    "描述", "獲取當前工件座標系"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞，默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: 當前工件座標系相對位姿，單位[mm][°]"

機器人工件座標系操作代碼示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [-89.606, 779.517, 193.516, 178.000, 0.476, -92.484]
    p2Desc = [-24.656, 850.384, 191.361, 177.079, -2.058, -95.355]
    p3Desc = [-99.813, 766.661, 241.878, -176.817, 1.917, -91.604]
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    p2Joint = [-111.024, -41.538, 69.222, -114.913, -87.743, 74.329]
    p3Joint = [-107.266, -56.116, 85.971, -122.560, -92.548, 74.331]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 0, 0, 0, 0]
    posTCP = [p1Desc, p2Desc, p3Desc]
    rtn,coordRtn = robot.ComputeWObjCoordWithPoints(1, posTCP, 0)
    print(f"ComputeWObjCoordWithPoints    {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.MoveJ(joint_pos=p1Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=1, user=0, vel=100)
    robot.SetWObjCoordPoint(3)
    rtn,coordRtn = robot.ComputeWObjCoord(1, 0)
    print(f"ComputeWObjCoord   {rtn}  coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} {coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetWObjCoord(1, coordRtn, 0)
    robot.SetWObjList(1, coordRtn, 0)
    rtn,getWobjDesc = robot.GetWObjOffset(0)
    print(f"GetWObjOffset    {rtn}  coord is {getWobjDesc[0]} {getWobjDesc[1]} {getWobjDesc[2]} {getWobjDesc[3]} {getWobjDesc[4]} {getWobjDesc[5]}")
    robot.CloseRPC()

設置全局速度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSpeed(vel)``"
    "描述", "設置全局速度"
    "必選參數", "- ``vel``:速度百分比，範圍[0~100]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置機器人加速度
+++++++++++++++++
.. versionadded:: python SDK-v2.0.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetOaccScale(acc)``"
    "描述", "設置機器人加速度"
    "必選參數", "- ``acc``:機器人加速度百分比"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取默認速度
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDefaultTransVel()``"
    "描述", "獲取默認速度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``vel``: 默認速度，單位 [mm/s]"

設置末端負載重量
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadWeight(loadNum, weight)``"
    "描述", "設置末端負載重量,錯誤負載重量設置可能會導致拖動模式下機器人失控"
    "必選參數", "- ``loadNum``:負載編號
    - ``weight``:單位[kg]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置末端負載質心座標
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLoadCoord(x,y,z,loadNum = 0)``"
    "描述", "設置末端負載質心座標,錯誤負載質心設置可能會導致拖動模式下機器人失控"
    "必選參數", "- ``x``: 質心座標，單位[mm]
    - ``y``: 質心座標，單位[mm]
    - ``z``: 質心座標，單位[mm]"
    "默認參數", "- ``loadNum``: 負載編號，默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取當前負載的重量
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayload(flag=1)``"
    "描述", "獲取當前負載的質量"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``weight``：當前負載重量，單位 [kg]"

獲取當前負載的質心
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayloadCog(flag=1)``"
    "描述", "獲取當前負載的質心"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``cog=[x,y,z]``: 當前質心座標，單位 [mm]"

設置機器人安裝方式-固定安裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallPos(method)``"
    "描述", "設置機器人安裝方式-固定安裝,錯誤安裝方式設置會導致拖動模式下機器人失控"
    "必選參數", "- ``method``:0-平裝，1-側裝，2-掛裝"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

設置機器人安裝角度-自由安裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotInstallAngle(yangle,zangle)``"
    "描述", "設置機器人安裝角度-自由安裝,錯誤安裝角度設置會導致拖動模式下機器人失控"
    "必選參數", "- ``yangle``：傾斜角
    - ``zangle``：旋轉角"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取機器人安裝角度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotInstallAngle()``"
    "描述", "獲取機器人安裝角度"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[yangle,zangle]``：yangle-傾斜角,zangle-旋轉角"

設置系統變量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSysVarValue(id,value)``"
    "描述", "設置系統變量"
    "必選參數", "- ``id``：變量編號，範圍[1~20];
    - ``value``：變量值"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取系統變量值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSysVarValue(id)``"
    "描述", "獲取系統變量值"
    "必選參數", "- ``id``：系統變量編號，範圍[1~20]"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``var_value``：系統變量值"

機器人常用設置代碼示例
++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1, 100):
        robot.SetSpeed(i)
        robot.SetOaccScale(i)
        time.sleep(0.03)
    error,defaultVel = robot.GetDefaultTransVel()
    print(f"GetDefaultTransVel is {defaultVel}")
    for i in range(1, 21):
        robot.SetSysVarValue(i, i + 0.5)
        time.sleep(0.1)
    for i in range(1, 21):
        value = robot.GetSysVarValue(i)
        print(f"sys value {i} is: {value}")
        time.sleep(0.1)
    robot.SetLoadWeight(0, 2.5)
    robot.SetLoadCoord(3.0,4.0,5.0)
    time.sleep(1)
    error,getLoad = robot.GetTargetPayload(0)
    error,getLoadTran = robot.GetTargetPayloadCog(0)
    print(f"get load is {getLoad}; get load cog is {getLoadTran[0]} {getLoadTran[1]} {getLoadTran[2]}")
    robot.SetRobotInstallPos(0)
    robot.SetRobotInstallAngle(15.0, 25.0)
    error,[anglex, angley] = robot.GetRobotInstallAngle()
    print(f"GetRobotInstallAngle x: {anglex}; y: {angley}")
    robot.CloseRPC()

關節摩擦力補償開關
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FrictionCompensationOnOff(state)``"
    "描述", "關節摩擦力補償開關"
    "必選參數", "- ``state``：0-關，1-開"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_level(coeff)``"
    "描述", "設置關節摩擦力補償係數-固定安裝-正裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節補償係數"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_wall(coeff)``"
    "描述", "設置關節摩擦力補償係數-固定安裝-側裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節補償係數"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_ceiling(coeff)``"
    "描述", "設置關節摩擦力補償係數-固定安裝-倒裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節補償係數"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置關節摩擦力補償係數-自由安裝
+++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_freedom(coeff)``"
    "描述", "設置關節摩擦力補償係數-自由安裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節補償係數"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人設置關節摩擦力補償代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    lcoeff = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    wcoeff = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
    ccoeff = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
    fcoeff = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    rtn = robot.FrictionCompensationOnOff(1)
    print(f"FrictionCompensationOnOff rtn is {rtn}")
    rtn = robot.SetFrictionValue_level(lcoeff)
    print(f"SetFrictionValue_level rtn is {rtn}")
    rtn = robot.SetFrictionValue_wall(wcoeff)
    print(f"SetFrictionValue_wall rtn is {rtn}")
    rtn = robot.SetFrictionValue_ceiling(ccoeff)
    print(f"SetFrictionValue_ceiling rtn is {rtn}")
    rtn = robot.SetFrictionValue_freedom(fcoeff)
    print(f"SetFrictionValue_freedom rtn is {rtn}")
    robot.CloseRPC()

查詢機器人錯誤碼
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotErrorCode()``"
    "描述", "查詢機器人錯誤碼"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[maincode subcode]``：機器人錯誤碼，maincode-主錯誤碼，subcode-子錯誤碼"

錯誤狀態清除
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ResetAllError()``"
    "描述", "錯誤狀態清除，只能清除可復位的錯誤"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人故障狀態獲取及清除錯誤代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Joint = [-108.145, -50.137, 85.818, -125.599, -87.946, 74.329]
    robot.MoveJ(joint_pos=p1Joint, tool=5, user=2, vel=50)
    time.sleep(1)
    error,[maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    time.sleep(1)
    robot.ResetAllError()
    time.sleep(1)
    error,[maincode, subcode] = robot.GetRobotErrorCode()
    print(f"robot maincode is {maincode}; subcode is {subcode}")
    robot.CloseRPC()

設置寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetWideBoxTempFanMonitorParam(enable, period)``"
    "描述", "設置寬電壓控制箱溫度及風扇轉速監控參數"
    "必選參數", "- ``enable``：0-不使能監測；1-使能監測
    - ``period``：監測週期(s),範圍1-100"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取寬電壓控制箱溫度及風扇轉速監控參數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWideBoxTempFanMonitorParam()``"
    "描述", "獲取寬電壓控制箱溫度及風扇轉速監控參數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``enable``：0-不使能監測；1-使能監測
    - ``period``：監測週期(s),範圍1-100"

寬電壓控制箱溫度和風扇電流狀態獲取代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.SetWideBoxTempFanMonitorParam(1, 2)
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    rtn = robot.SetWideBoxTempFanMonitorParam(0, 2)
    print(f"SetWideBoxTempFanMonitorParam rtn is:{rtn}")
    error, enable, period = robot.GetWideBoxTempFanMonitorParam()
    print(f"GetWideBoxTempFanMonitorParam enable is:{enable},period is:{period}")
    for i in range(100):
        error, pkg = robot.GetRobotRealTimeState()
        print(f"robot ctrl box temp is:{pkg.wideVoltageCtrlBoxTemp},fan current is:{pkg.wideVoltageCtrlBoxFanCurrent}")
        time.sleep(0.1)
    robot.CloseRPC()

設置焦點標定點
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFocusCalibPoint(pointNum, point)``"
    "描述", "設置焦點標定點"
    "必選參數", "- ``pointNum``：焦點標定點編號 1-8
    - ``point``：標定點座標"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算焦點標定結果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFocusCalib(pointNum)``"
    "描述", "計算焦點標定結果"
    "必選參數", "- ``pointNum``：標定點個數"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``resultPos``：標定結果XYZ
    - ``accuracy``：標定精度誤差"

開啓焦點跟隨
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FocusStart(kp=50.0, kpredic=19.0, aMax=1440, vMax=180, type=0)``"
    "描述", "開啓焦點跟隨"
    "必選參數", "無"
    "默認參數", "- ``kp``：比例參數，默認50.0
    - ``kpredic``：前饋參數，默認19.0
    - ``aMax``：最大角加速度限制，默認1440°/s^2
    - ``vMax``：最大角速度限制，默認180°/s
    - ``type``：鎖定X軸指向(0-參考輸入矢量；1-水平；2-垂直)，默認0"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

停止焦點跟隨
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FocusEnd()``"
    "描述", "停止焦點跟隨"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置焦點座標
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFocusPosition(pos)``"
    "描述", "設置焦點座標"
    "必選參數", "- ``pos``：焦點座標XYZ"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人焦點跟隨代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p1Desc = [186.331, 487.913, 209.850, 149.030, 0.688, -114.347]
    p1Joint = [-127.876, -75.341, 115.417, -122.741, -59.820, 74.300]
    p2Desc = [69.721, 535.073, 202.882, -144.406, -14.775, -89.012]
    p2Joint = [-101.780, -69.828, 110.917, -125.740, -127.841, 74.300]
    p3Desc = [146.861, 578.426, 205.598, 175.997, -36.178, -93.437]
    p3Joint = [-112.851, -60.191, 86.566, -80.676, -97.463, 74.300]
    p4Desc = [136.284, 509.876, 225.613, 178.987, 1.372, -100.696]
    p4Joint = [-116.397, -76.281, 113.845, -128.611, -88.654, 74.299]
    p5Desc = [138.395, 505.972, 298.016, 179.134, 2.147, -101.110]
    p5Joint = [-116.814, -82.333, 109.162, -118.662, -88.585, 74.302]
    p6Desc = [105.553, 454.325, 232.017, -179.426, 0.444, -99.952]
    p6Joint = [-115.649, -84.367, 122.447, -128.663, -90.432, 74.303]
    exaxisPos = [0, 0, 0, 0]
    offdese = [0, 0, 100, 0, 0, 0]
    robot.MoveJ(joint_pos=p1Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(1)
    robot.MoveJ(joint_pos=p2Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(2)
    robot.MoveJ(joint_pos=p3Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(3)
    robot.MoveJ(joint_pos=p4Joint,tool=0,user=0,vel=100,acc=100,ovl=100,exaxis_pos=exaxisPos,blendT=-1,offset_flag=0,offset_pos=offdese)
    robot.SetTcp4RefPoint(4)
    rtn,coordRtn = robot.ComputeTcp4()
    print(f"4 Point ComputeTool {rtn} coord is {coordRtn[0]} {coordRtn[1]} {coordRtn[2]} "
          f"{coordRtn[3]} {coordRtn[4]} {coordRtn[5]}")
    robot.SetToolCoord(1, coordRtn, 0, 0, 1, 0)
    error, p1Desc = robot.GetForwardKin(p1Joint)
    error, p2Desc = robot.GetForwardKin(p2Joint)
    error, p3Desc = robot.GetForwardKin(p3Joint)
    robot.SetFocusCalibPoint(1, p1Desc)
    robot.SetFocusCalibPoint(2, p2Desc)
    robot.SetFocusCalibPoint(3, p3Desc)
    rtn, resultPos, accuracy = robot.ComputeFocusCalib(pointNum=3)
    print(f"ComputeFocusCalib coord is {rtn} {resultPos[0]} {resultPos[1]} {resultPos[2]} accuracy is {accuracy}")
    rtn = robot.SetFocusPosition(resultPos)
    error, p5Desc = robot.GetForwardKin(p5Joint)
    error, p6Desc = robot.GetForwardKin(p6Joint)
    robot.MoveL(desc_pos=p5Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.FocusStart(50, 19, 710, 90, 0)
    robot.MoveL(desc_pos=p5Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.MoveL(desc_pos=p6Desc,tool=1,user=0,vel=10,acc=100,ovl=100,blendR=-1,blendMode=0,exaxis_pos=exaxisPos,search=0,offset_flag=1,offset_pos=offdese)
    robot.FocusEnd()
    robot.CloseRPC()

關節扭矩傳感器靈敏度標定功能開啓
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityEnable(status)``"
    "描述", "關節扭矩傳感器靈敏度標定功能開啓"
    "必選參數", "- ``status``：0-關閉；1-開啓"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

關節扭矩傳感器靈敏度數據採集
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityCollect()``"
    "描述", "關節扭矩傳感器靈敏度數據採集"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取關節扭矩傳感器靈敏度標定結果
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityCalibration()``"
    "描述", "獲取關節扭矩傳感器靈敏度標定結果"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``calibResult``：j1~j6關節靈敏度[0-1]
    - ``linearityn``：j1~j6關節線性度[0-1]"

取得關節扭矩感測器遲滯誤差
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointHysteresisError()``"
    "描述", "取得關節扭矩感測器遲滯誤差"
    "必選參數", "無"
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``hysteresisError``：j1~j6 關節遲滯誤差"

取得關節扭矩感測器重複精度
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointRepeatability()``"
    "描述", "取得關節扭矩感測器重複精度"
    "必選參數", "無"
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``repeatability``：j1~j6 關節重複精度"

設定關節力感測器參數
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAdmittanceParams(M, B, K, threshold, sensitivity, setZeroFlag)``"
    "描述", "設定關節力感測器參數"
    "必選參數", "
    - ``M``：J1-J6 質量係數 [0.001 ~ 10]
    - ``B``：J1-J6 阻尼係數 [0.001 ~ 10]
    - ``K``：J1-J6 剛度係數 [0.001 ~ 10]
    - ``threshold``：力控制閾值，Nm
    - ``sensitivity``：靈敏度, Nm/V, [0 ~ 10]
    - ``setZeroFlag``：功能開啟標誌位；0-關閉；1-開啟；2-位置1記錄零點；3-位置2記錄零點"
    "預設參數", "無"
    "返回值", "- 錯誤碼 成功-0 失敗- errcode"

關節扭矩傳感器靈敏度自動標定代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.JointSensitivityEnable(0)
    rtn = robot.JointSensitivityEnable(1)
    print(f"JointSensitivityEnable rtn is {rtn}")
    curJPos = [0.0] * 6
    rtn, curJPos = robot.GetActualJointPosDegree(0)
    epos = [0.0] * 4
    offset_pos = [0.0] * 6
    jointPos1 = [curJPos[0], 0.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos1 = [0.0] * 6
    rtn, descPos1 = robot.GetForwardKin(jointPos1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 1 rtn is {rtn}")
    time.sleep(0.1)
    jointPos2 = [curJPos[0], -30.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos2 = [0.0] * 6
    rtn, descPos2 = robot.GetForwardKin(jointPos2)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 2 rtn is {rtn}")
    time.sleep(0.1)
    jointPos3 = [curJPos[0], -60.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos3 = [0.0] * 6
    rtn, descPos3 = robot.GetForwardKin(jointPos3)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 3 rtn is {rtn}")
    time.sleep(0.1)
    jointPos4 = [curJPos[0], -90.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos4 = [0.0] * 6
    rtn, descPos4 = robot.GetForwardKin(jointPos4)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 4 rtn is {rtn}")
    time.sleep(0.1)
    jointPos5 = [curJPos[0], -120.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos5 = [0.0] * 6
    rtn, descPos5 = robot.GetForwardKin(jointPos5)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 5 rtn is {rtn}")
    time.sleep(0.1)
    jointPos6 = [curJPos[0], -150.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos6 = [0.0] * 6
    rtn, descPos6 = robot.GetForwardKin(jointPos6)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 6 rtn is {rtn}")
    time.sleep(0.1)
    jointPos7 = [curJPos[0], -180.0, 0.0, -90.0, 0.02, curJPos[5]]
    descPos7 = [0.0] * 6
    rtn, descPos7 = robot.GetForwardKin(jointPos7)
    robot.MoveJ(joint_pos=jointPos7, desc_pos=descPos7, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 7 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos6, desc_pos=descPos6, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 8 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos5, desc_pos=descPos5, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 9 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos4, desc_pos=descPos4, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 10 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos3, desc_pos=descPos3, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 11 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos2, desc_pos=descPos2, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.1)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 12 rtn is {rtn}")
    time.sleep(0.1)
    robot.MoveJ(joint_pos=jointPos1, desc_pos=descPos1, tool=0, user=0, vel=100, acc=100, ovl=100, exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
    time.sleep(0.2)
    rtn = robot.JointSensitivityCollect()
    print(f"JointSensitivityCollect 13 rtn is {rtn}")
    time.sleep(0.1)
    calibResult = [0.0] * 6
    linearity = [0.0] * 6
    rtn,calibResult, linearity = robot.JointSensitivityCalibration()
    print(f"JointSensitivityCalibration rtn is {rtn}")
    rtn = robot.JointSensitivityEnable(0)
    print(f"JointSensitivityEnable rtn is {rtn}")
    print(f"jointSensor Calib result is {calibResult[0]},{calibResult[1]},{calibResult[2]},{calibResult[3]},{calibResult[4]},{calibResult[5]}")
    print( f"jointSensor linearity is {linearity[0]},{linearity[1]},{linearity[2]},{linearity[3]},{linearity[4]},{linearity[5]}")
    hysteresisError = [0.0] * 6
    rtn,hysteresisError = robot.JointHysteresisError()
    print(f"JointHysteresisError result is {hysteresisError[0]},{hysteresisError[1]},{hysteresisError[2]},{hysteresisError[3]},{hysteresisError[4]},{hysteresisError[5]}")
    repeatability = [0.0] * 6
    rtn,repeatability = robot.JointRepeatability()
    print(f"JointRepeatability result is {repeatability[0]},{repeatability[1]},{repeatability[2]},{repeatability[3]},{repeatability[4]},{repeatability[5]}")
    M = [1.0] * 6
    B = [1.0] * 6
    K = [0.0] * 6
    threshold = [1.0] * 6
    setZeroFlag = 1
    rtn = robot.SetAdmittanceParams(M, B, K, threshold, calibResult, setZeroFlag)
    print(f"SetAdmittanceParams rtn is {rtn}")
    robot.CloseRPC()

獲取機器人8個從站端口錯誤幀數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlavePortErrCounter()``"
    "描述", "獲取機器人8個從站端口錯誤幀數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``inRecvErr``：輸入接收錯誤幀數
    - ``inCRCErr``：輸入CRC錯誤幀數
    - ``inTransmitErr``：輸入轉發錯誤幀數
    - ``inLinkErr``：輸入鏈接錯誤幀數
    - ``outRecvErr``：輸出接收錯誤幀數
    - ``outCRCErr``：輸出CRC錯誤幀數
    - ``outTransmitErr``：輸出轉發錯誤幀數
    - ``outLinkErr``：輸出鏈接錯誤幀數"

從站端口錯誤幀清零
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointSensitivityEnable(slaveID)``"
    "描述", "從站端口錯誤幀清零"
    "必選參數", "- ``slaveID``：從站編號0~7"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取從站端口錯誤幀代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    inRecvErr = [0] * 8
    inCRCErr = [0] * 8
    inTransmitErr = [0] * 8
    inLinkErr = [0] * 8
    outRecvErr = [0] * 8
    outCRCErr = [0] * 8
    outTransmitErr = [0] * 8
    outLinkErr = [0] * 8
    rtn,inRecvErr, inCRCErr, inTransmitErr, inLinkErr, outRecvErr, outCRCErr, outTransmitErr, outLinkErr = robot.GetSlavePortErrCounter()
    for i in range(8):
        if inRecvErr[i] != 0:
            print(f"inRecvErr {i} is {inRecvErr[i]}")
        if inCRCErr[i] != 0:
            print(f"inCRCErr {i} is {inCRCErr[i]}")
        if inTransmitErr[i] != 0:
            print(f"inTransmitErr {i} is {inTransmitErr[i]}")
        if inLinkErr[i] != 0:
            print(f"inLinkErr {i} is {inLinkErr[i]}")
        if outRecvErr[i] != 0:
            print(f"outRecvErr {i} is {outRecvErr[i]}")
        if outCRCErr[i] != 0:
            print(f"outCRCErr {i} is {outCRCErr[i]}")
        if outTransmitErr[i] != 0:
            print(f"outTransmitErr {i} is {outTransmitErr[i]}")
        if outLinkErr[i] != 0:
            print(f"outLinkErr {i} is {outLinkErr[i]}")
    print("others has no err!")
    for i in range(8):
        robot.SlavePortErrCounterClear(i)
    robot.CloseRPC()

設置各軸速度前饋係數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetVelFeedForwardRatio(radio)``"
    "描述", "設置各軸速度前饋係數"
    "必選參數", "- ``radio``：各軸速度前饋係數"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取各軸速度前饋係數
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetVelFeedForwardRatio()``"
    "描述", "獲取各軸速度前饋係數"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``radio``：各軸速度前饋係數"

機器人速度前饋係數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    setRadio = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    robot.SetVelFeedForwardRatio(setRadio)
    getRadio = [0.0] * 6
    rtn,getRadio = robot.GetVelFeedForwardRatio()
    print(f"{getRadio[0]},{getRadio[1]},{getRadio[2]},{getRadio[3]},{getRadio[4]},{getRadio[5]}")
    robot.CloseRPC()