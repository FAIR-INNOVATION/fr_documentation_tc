機器人安全設定
=================

.. toctree:: 
    :maxdepth: 5


設定碰撞等級
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAnticollision (mode,level,config)``"
    "描述", "設定碰撞等級"
    "必選參數", "- ``mode``:0-等級，1-百分比；
    - ``level=[j1,j2,j3,j4,j5,j6]``:碰撞阈值；
    - ``config``:0-不更新設定文件，1-更新設定文件"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    level = [1.0,2.0,3.0,4.0,5.0,6.0]
    error = robot.SetAnticollision(0,level,1)
    print("設定碰撞等級錯誤碼:",error)
    level = [50.0,20.0,30.0,40.0,50.0,60.0]
    error = robot.SetAnticollision(1,level,1)
    print("設定碰撞等級錯誤碼:",error)

設定碰撞後策略
++++++++++++++++++
.. versionchanged:: Python SDK-v2.0.8-3.7.8

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionStrategy(strategy,safeTime,safeDistance,safeVel,safetyMargin)``"
    "描述", "設定碰撞後策略"
    "必選參數", "- ``strategy``：0-報錯暫停，1-繼續運行，2-錯誤停止，3-重力矩模式，4-震盪對應模式，5-碰撞回彈模式"
    "默認參數", "- ``safeTime``：安全停止時間[1000-2000]ms，默認為：1000
    - ``safeDistance``：安全停止距離[1-150]mm，默認為：100
    - ``safeVel``：安全停止速度[50-250]mm/s，預設為：250
    - ``safetyMargin[6]``：安全係數[1-10]，默認為：[10,10,10,10,10,10]"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SetCollisionStrategy(strategy=1)
    print("設定碰撞後策略錯誤碼:",error)

設定正限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitPositive(p_limit)``"
    "描述", "設定正限位"
    "必選參數", "- ``p_limit=[j1,j2,j3,j4,j5,j6]``：六個關節位置"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    p_limit = [170.0,80.0,150.0,80.0,170.0,160.0]
    error = robot.SetLimitPositive(p_limit)
    print("設定正限位錯誤碼:",error)

設定負限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitNegative(n_limit)``"
    "描述", "設定負限位"
    "必選參數", "- ``n_limit=[j1,j2,j3,j4,j5,j6]``：六個關節位置"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    n_limit = [-170.0,-260.0,-150.0,-260.0,-170.0,-160.0]
    error = robot.SetLimitNegative(n_limit)
    print("設定負限位錯誤碼:",error)

錯誤狀態清除
++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ResetAllError()``"
    "描述", "錯誤狀態清除，只能清除可复位的錯誤"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.ResetAllError()
    print("錯誤狀態清除錯誤碼:",error)

關節摩擦力補償開關
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``FrictionCompensationOnOff(state)``"
    "描述", "關節摩擦力補償開關"
    "必選參數", "- ``state``：0-關，1-開"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.FrictionCompensationOnOff(1)
    print("關節摩擦力補償開關錯誤碼:",error)

設定關節摩擦力補償係數-正裝
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_level(coeff)``"
    "描述", "設定關節摩擦力补偿系数-固定安裝-正裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節补偿系数"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    lcoeff = [0.9,0.9,0.9,0.9,0.9,0.9]
    error = robot.SetFrictionValue_level(lcoeff)
    print("設定關節摩擦力補償係數-正裝錯誤碼:",error)

設定關節摩擦力補償係數-側裝
++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_wall(coeff)``"
    "描述", "設定關節摩擦力补偿系数-固定安裝-側裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節补偿系数"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    wcoeff = [0.4,0.4,0.4,0.4,0.4,0.4]
    error = robot.SetFrictionValue_wall(wcoeff)
    print("設定關節摩擦力補償係數-側裝錯誤碼:",error)

設定關節摩擦力補償係數-倒裝
++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_ceiling(coeff)``"
    "描述", "設定關節摩擦力补偿系数-固定安裝-倒裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節补偿系数"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    ccoeff = [0.6,0.6,0.6,0.6,0.6,0.6]
    error =robot.SetFrictionValue_ceiling(ccoeff)
    print("設定關節摩擦力補償係數-倒裝錯誤碼:",error)

設定關節摩擦力補償係數-自由安裝
+++++++++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetFrictionValue_freedom(coeff)``"
    "描述", "設定關節摩擦力補償係數-自由安裝"
    "必選參數", "- ``coeff=[j1,j2,j3,j4,j5,j6]``：六個關節补偿系数"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    fcoeff = [0.5,0.5,0.5,0.5,0.5,0.5]
    error =robot.SetFrictionValue_freedom(fcoeff)
    print("設定關節摩擦力补偿系数-自由裝錯誤碼:",error)

下載點位表資料庫
+++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableDownLoad(point_table_name,save_file_path)``"
    "描述", "下載點位表資料庫"
    "必選參數", "- ``point_table_name``：要下載的點位表名稱    pointTable1.db;
    - ``save_file_path``:下載點位表的儲存路徑   C://test/;"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableDownLoad("point_table_a.db","D://Desktop/testPoint/download/")
    print("PointTableDownLoad錯誤碼:",error)
 
上傳點位表資料庫
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpLoad(point_table_file_path)``"
    "描述", "上傳點位表資料庫"
    "必選參數", "- ``point_table_file_path``：上傳點位表的全路徑名   C://test/pointTable1.db"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos:   

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpLoad("D://Desktop/testPoint/point_table_a.db")
    print("PointTableUpLoad錯誤碼:",error)

點位表切換
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableSwitch(point_table_name)``"
    "描述", "點位表切換"
    "必選參數", "- ``point_table_name``：要切換的點位表名稱pointTable1.db,當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot

    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableSwitch("point_table_a.db")
    print("PointTableSwitch:",error)

點位表更新lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "描述", "點位表更新lua文件"
    "必選參數", "- ``point_table_name``：要切換的點位表名稱   pointTable1.db,當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序
    - ``lua_file_name``: 要更新的lua檔案名稱 testPointTable.lua"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.PointTableUpdateLua("point_table_a.db","testpoint.lua")
    print("PointTableUpdateLua:",error)

設定機器人碰撞偵測方法
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionDetectionMethod(method)``"
    "描述", "設定機器人碰撞偵測方法"
    "必選參數", "
    - ``method``：碰撞偵測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啟  
    "
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"

設定靜態下碰撞偵測開始關閉
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStaticCollisionOnOff(status)``"
    "描述", "設定靜態下碰撞偵測開始關閉"
    "必選參數", "
    - ``status``： 0-關閉；1-開啟
    "
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"

設定碰撞偵測開始關閉
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPowerLimit(status, power)``"
    "描述", "設定靜態下碰撞偵測開始關閉"
    "必選參數", "
    - ``status``： 0-關閉；1-開啟
    "
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"
    
代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    error = robot.SetPowerLimit(0,2)
    print("SetPowerLimit return:",error)

    error = robot.DragTeachSwitch(1)
    print("DragTeachSwitch return:",error)

    error,joint_torque = robot.GetJointTorques()
    print("GetJointTorques return",joint_torque)
    joint_torque = [joint_torque[0],joint_torque[1],joint_torque[2],joint_torque[3],joint_torque[4],joint_torque[5]]
    error_joint = 0
    count =100
    error = robot.ServoJTStart()    #servoJT開始
    print("ServoJTStart return",error)
    while(count):
        if error!=0:
            error_joint =error
        joint_torque[0] = joint_torque[0] + 10  #每次1軸增加0.1NM，運動100次
        error = robot.ServoJT(joint_torque, 0.001)  # 關節空間伺服模式運動
        count = count - 1
        time.sleep(0.001)
    print("ServoJTStart return",error_joint)
    error = robot.ServoJTEnd()  #伺服運動結束
    time.sleep(1)
    print("ServoJTEnd return",error)

奇異位姿保護開啟
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SingularAvoidStart(protectMode, minShoulderPos=100, minElbowPos=50, minWristPos=10)``"
    "描述", "開啟奇異位姿保護"
    "必選參數", "
    - ``protectMode``：奇異位姿保護保護模式：0-關節模式；1-笛卡兒模式
    "
    "默認參數", "- ``minShoulderPos``：肩奇異調整範圍(mm), 默認100.0
    - ``minElbowPos``：肘奇異調整範圍(mm), 默認50.0
    - ``minWristPos``：腕奇異調整範圍(°), 預設10.0"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"

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
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode"

代碼範例
------------
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象

    robot = Robot.RPC('192.168.58.2')

    startdescPose = [-352.437, -88.350, 226.471, 177.222, 4.924, 86.631]
    startjointPos = [-3.463, -84.308, 105.579, -108.475, -85.087, -0.334]

    middescPose = [-518.339, -23.706, 207.899, -178.420, 0.171, 71.697]
    midjointPos = [-8.587, -51.805, 64.914, -104.695, -90.099, 9.718]

    enddescPose = [-273.934, 323.003, 227.224, 176.398, 2.783, 66.064]
    endjointPos = [-63.460, -71.228, 88.068, -102.291, -90.149, -39.605]

    robot.MoveL(desc_pos=startdescPose, tool=0, user=0,vel=50)
    error = robot.SingularAvoidStart(1,100,50,10)
    print("SingularAvoidStart return ", error)
    robot.MoveC(desc_pos_p=middescPose,tool_p=0,user_p=0,desc_pos_t=enddescPose,tool_t=0,user_t=0,vel_p=50,vel_t=50)
    error = robot.SingularAvoidEnd()
    print("SingularAvoidEnd return ", error)