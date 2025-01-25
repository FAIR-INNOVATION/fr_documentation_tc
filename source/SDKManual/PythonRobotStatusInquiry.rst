機器人狀態查詢
===============

.. toctree:: 
    :maxdepth: 5

取得機器人安裝角度
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotInstallAngle()``"
    "描述", "取得機器人安裝角度"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[yangle,zangle]``：yangle-傾斜角,zangle-旋轉角"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotInstallAngle()
    print("取得機器人安裝角度", ret)

取得系統變數值
+++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSysVarValue(id)``"
    "描述", "取得系統變數值"
    "必選參數", "- ``id``：系統變數編號，範圍[1~20]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``var_value``：系統變數值"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    for i in range(1,21):
        error = robot.GetSysVarValue(i)
        print("系統變數編號:",i,"值", error)

取得目前關節位置(角度)
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosDegree(flag=1)``"
    "描述", "獲取關節目前位置(角度)"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞，默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：當前關節位置(角度)"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointPosDegree()
    print("獲取當前關節位置 (角度)", ret)

取得目前關節位置(弧度)
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointPosRadian(flag=1)``"
    "描述", "獲取關節目前位置(弧度)"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：當前關節位置(弧度)"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointPosRadian()
    print("獲取當前關節位置 (弧度)", ret)

取得關節回饋速度-deg/s
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualJointSpeedsDegree (flag=1)``"
    "描述", "取得關節回饋速度-deg/s"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``speed=[j1,j2,j3,j4,j5,j6]``：關節反馈速度-deg/s"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualJointSpeedsDegree()
    print("取得關節回饋速度-deg/s", ret)

獲取TCP指令合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPCompositeSpeed(flag=1)``"
    "描述", "獲取TCP指令合速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetTCPCompositeSpeed()
    print("獲取TCP指令合速度", ret)

獲取TCP反馈合速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPCompositeSpeed(flag=1)``"
    "描述", "獲取TCP反馈合速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[tcp_speed,ori_speed]``：tcp_speed-线性合速度 ori_speed-姿态合速度"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPCompositeSpeed()
    print("獲取TCP反馈合速度", ret)

取得TCP指令速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetTCPSpeed(flag=1)``"
    "描述", "取得TCP指令速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP指令速度，mm/s"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetTCPSpeed()
    print("取得TCP指令速度", ret)

獲取TCP回饋速度
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPSpeed(flag=1)``"
    "描述", "獲取TCP回饋速度"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``speed=[x,y,z,rx,ry,rz]``：TCP反馈速度"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPSpeed()
    print("獲取TCP回饋速度", ret)

取得當前工具位姿
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPPose(flag=1)``"
    "描述", "取得當前工具位姿"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tcp_pose=[x,y,z,rx,ry,rz]``：當前工具位姿"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPPose()
    print("取得當前工具位姿", ret)

取得目前工具坐標系編號
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualTCPNum(flag=1)``"
    "描述", "取得目前工具坐標系編號"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞 默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tool_id``:工具座標系編號"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualTCPNum()
    print("取得目前工具坐標系編號", ret)

取得目前工件坐標系編號
+++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualWObjNum(flag=1)``"
    "描述", "取得目前工件坐標系編號"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``wobj_id``:工件座標系編號"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualWObjNum()
    print("取得目前工件坐標系編號", ret)

取得目前末端法蘭位姿
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetActualToolFlangePose(flag=1)``"
    "描述", "取得目前末端法蘭位姿"
    "必選參數", "無"
    "默認參數", "- ``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``flange_pose=[x,y,z,rx,ry,rz]``：當前末端法蘭位姿"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetActualToolFlangePose()
    print("取得目前末端法蘭位姿", ret)

逆運動學求解
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKin(type,desc_pos,config=-1)``"
    "描述", "逆運動学，笛卡兒位姿求解關節位置 "
    "必選參數", "- ``type``:0-绝对位姿(基坐標系)，1-相对位姿（基坐標系），2-相对位姿（工具座標系）
    - ``desc_pose``:[x,y,z,rx,ry,rz],工具位姿，單位[mm][°]"
    "默認參數", "- ``config``:關節配置，[-1]-參考當前關節位置求解，[0~7]-依据關節配置求解 默認-1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆運動学解，笛卡兒位姿求解關節位置"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKin(0,P1,config=-1)
    print("逆運動学，笛卡兒位姿求解關節位置", ret)

逆運動學求解-指定參考位置
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinRef(type,desc_pos,joint_pos_ref)``"
    "描述", "逆運動学，工具位姿求解關節位置，參考指定關節位置求解"
    "必選參數", "- ``type``:0-绝对位姿(基坐標系)，1-相对位姿（基坐標系），2-相对位姿（工具座標系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，單位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，關節參考位置，單位[°]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``joint_pos=[j1,j2,j3,j4,j5,j6]``：逆運動学解，工具位姿求解關節位置"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKinRef(0,P1,J1)
    print("逆運動学，工具位姿求解關節位置，參考指定關節位置求解", ret)

逆運動學求解-是否有解
++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetInverseKinHasSolution(type,desc_pos,joint_pos_ref)``"
    "描述", "逆運動学，工具位姿求解關節位置 是否有解"
    "必選參數", "- ``type``:0-绝对位姿(基坐標系)，1-相对位姿（基坐標系），2-相对位姿（工具座標系）
    - ``desc_pos``：[x,y,z,rx,ry,rz]工具位姿，單位[mm][°]
    - ``joint_pos_ref``：[j1,j2,j3,j4,j5,j6]，關節參考位置，單位[°]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``result``:“True”-有解，“False”-無解"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
    ret = robot.GetInverseKinHasSolution(0,P1,J1)
    print("逆運動学，工具位姿求解關節位置是否有解", ret)

正運動學求解
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetForwardKin(joint_pos)``"
    "描述", "正運動学，關節位置求解工具位姿"
    "必選參數", "- ``joint_pos``:[j1,j2,j3,j4,j5,j6]:關節位置，單位[°]"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``desc_pos=[x,y,z,rx,ry,rz]``：正運動学解，關節位置求解工具位姿"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    J1=[95.442,-101.149,-98.699,-68.347,90.580,-47.174]
    ret = robot.GetForwardKin(J1)
    print("正運動学，關節位置求解工具位姿", ret)

取得當前關節轉矩
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointTorques(flag=1)``"
    "描述", "取得當前關節轉矩"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``torques=[j1,j2,j3,j4,j5,j6]``：關節扭矩"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot 
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetJointTorques()
    print("取得當前關節轉矩", ret)

取得目前負載的重量
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayload(flag=1)``"
    "描述", "獲取當前负载的质量"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``weight``：當前負載重量，單位 [kg]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetPayload(0)
    print("獲取當前负载的质量", ret)

取得目前負載的質心
+++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTargetPayloadCog(flag=1)``"
    "描述", "取得目前負載的質心"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``cog=[x,y,z]``: 當前质心座標，單位 [mm]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTargetPayloadCog(0)
    print("取得目前負載的質心", ret)

獲取當前工具坐標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetTCPOffset(flag=1)``"
    "描述", "獲取當前工具坐標系"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``tcp_offset=[x,y,z,rx,ry,rz]``: 當前工具座標系相对位姿，單位[mm][°]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetTCPOffset()
    print("獲取當前工具坐標系", ret)

取得當前工件坐標系
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetWObjOffset(flag=1)``"
    "描述", "取得當前工件坐標系"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞，默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``wobj_offset=[x,y,z,rx,ry,rz]``: 當前工件座標系相对位姿，單位[mm][°]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetWObjOffset()
    print("取得當前工件坐標系", ret)

取得關節軟限位角度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointSoftLimitDeg(flag=1)``"
    "描述", "取得關節軟限位角度"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[j1min,j1max,j2min,j2max,j3min,j3max, j4min,j4max,j5min, j5max, j6min,j6max]``：軸1~軸6，關節负限位与正限位，單位[mm]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetJointSoftLimitDeg()
    print("取得關節軟限位角度", ret)

取得系統時間
++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSystemClock()``"
    "描述", "取得系統時間"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``t_ms``: 系統時間，單位 [ms]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSystemClock()
    print("取得系統時間", ret)

取得機器人當前關節配置
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotCurJointsConfig()``"
    "描述", "取得機器人當前關節配置"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``config``: 機器人當前關節配置，範圍 [0~7]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotCurJointsConfig()
    print("取得機器人當前關節配置", ret)

獲取默認速度
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDefaultTransVel()``"
    "描述", "獲取默認速度"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``vel``: 默認速度，單位 [mm/s]"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetDefaultTransVel()
    print("獲取默認速度", ret)

查詢機器人運動是否完成
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotMotionDone()``"
    "描述", "查詢機器人運動是否完成"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``state``: 機器人運動狀態，0-未完成，1-完成"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotMotionDone()
    print("查詢機器人運動是否完成", ret)

查詢機器人錯誤碼
++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotErrorCode()``"
    "描述", "查詢機器人錯誤碼"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[maincode subcode]``：機器人錯誤碼，maincode-主錯誤碼，subcode-子錯誤碼"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotErrorCode()
    print("查詢機器人錯誤碼", ret)

查詢機器人示教管理點位數據
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotTeachingPoint(name)``"
    "描述", "查詢機器人示教管理點位數據"
    "必選參數", "``name``：點位名"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``[x,y,z,rx,ry,rz,j1,j2,j3,j4,j5,j6,tool,wobj,speed,acc,e1,e2,e3,e4]``：點位數據"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetRobotTeachingPoint("11")
    print("查詢機器人示教管理點位數據錯誤碼", ret)

取得SSH公鑰
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSSHKeygen()``"
    "描述", "取得SSH公鑰"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``keygen``：公鑰"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSSHKeygen() #獲取SSH
    print("獲取SSH", ret)

計算指定路徑下檔案的MD5值
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFileMD5(file_path)``"
    "描述", "計算指定路徑下檔案的MD5值"
    "必選參數", "- ``file_path``：文件路徑包含文件名，默認Traj文件夹路徑為:/fruser/traj/,如/fruser/traj/trajHelix_aima_1.txt"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``md5``：文件MD5值"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.ComputeFileMD5("/fruser/201.lua")   #計算指定路徑下檔案的MD5值
    print("計算指定路徑下檔案的MD5值", ret)

獲取機器人版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareVersion()``"
    "描述", "獲取機器人版本信息"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``robotModel``：機器人模型
    - ``webVersion``：web版本
    - ``controllerVersion``：控制器版本"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')

    ret = robot.GetSoftwareVersion()
    print("GetSoftwareVersion()：", ret)

取得機器人硬體版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveHardVersion()``"
    "描述", "取得機器人硬體版本信息"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSlaveHardVersion()
    print("GetSlaveHardVersion()：", ret)

取得機器人韌體版本信息
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSlaveFirmVersion()``"
    "描述", "取得機器人韌體版本信息"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``ctrlBoxBoardVersion``：控制箱版本
    - ``driver1Version``
    - ``driver2Version``
    - ``driver3Version``
    - ``driver4Version``
    - ``driver5Version``
    - ``driver6Version``
    - ``endBoardVersion``"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ret = robot.GetSlaveFirmVersion()
    print("GetSlaveFirmVersion()：", ret)

獲取DH补偿參數
++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetDHCompensation()``"
    "描述", "獲取DH补偿參數"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode
    - ``dhCompensation=[cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]``：機器人DH參數补偿值(mm)"

代碼範例
------------
.. code-block:: python
    :linenos:

    import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.GetDHCompensation()
    print(error)

獲取關節驅動器當前扭矩
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTorque()``"
    "描述", "獲取關節驅動器當前扭矩"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``data=[j1,j2,j3,j4,j5,j6]``：關節驅動器當前扭矩"

獲取關節驅動器當前溫度
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointDriverTemperature()``"
    "描述", "獲取關節驅動器當前溫度"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``data=[t1,t2,t3,t4,t5,t6]``：關節驅動器當前溫度"