機器人週邊
============

.. toctree:: 
    :maxdepth: 5

取得夾爪配置
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperConfig()``"
    "描述", "取得夾爪配置"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``[number,company,device,softversion]``： number，夾爪編號;company，夹爪廠商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行 ;device，設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20);softvesion，軟體版本號，暫不使用，預設為0。"

啟動夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ActGripper(index,action)``"
    "描述", "啟動夾爪"
    "必選參數", "- ``index``:夾爪編號；
    - ``action``:0-復位，1-激活"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

控制夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``MoveGripper(index,pos,vel,force,maxtime,block,type,rotNum,rotVel,rotTorque)``"
    "描述", "控制夾爪"
    "必選參數", "- ``index``:夾爪編號；
    - ``pos``:位置百分比，範圍[0~100]；
    - ``vel``:速度百分比，範圍[0~100];
    - ``force``:力矩百分比，範圍[0~100]；
    - ``maxtime``:最大等待時間，範圍[0~30000]，單位[ms]；
    - ``block``:0-阻塞，1-非阻塞；
    - ``type``:夾爪類型，0-平行夾爪；1-旋轉夾爪；
    - ``rotNum``:rotNum 旋轉圈數；
    - ``rotVel``:旋轉速度百分比[0-100]；
    - ``rotTorque``:旋轉力矩百分比[0-100]。"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得夾爪運動狀態
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetGripperMotionDone()``"
    "描述", "取得夾爪運動狀態"
    "必選參數", "無"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``[fault,status]``：夹爪運動狀態，fault:0-無錯誤，1-有錯誤；status:0-運動未完成，1-運動完成"

配置夾爪
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetGripperConfig(company,device,softversion=0,bus=0)``"
    "描述", "配置夾爪"
    "必選參數", "- ``company``：夹爪廠商，1-Robotiq，2-慧灵，3-天机，4-大寰，5-知行；
    - ``device``：設備號，Robotiq(0-2F-85系列)，慧靈(0-NK系列,1-Z-EFG-100)，天機(0-TEG-110)，大寰(0-PGI-140)，知行(0-CTPM2F20)"
    "默認參數", "- ``softversion``：軟體版本號，暫不使用，預設為0；
    - ``bus``：設備掛載末端匯流排位置，暫不使用，預設為0；"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

代碼範例
------------
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    desc_pos1=[-333.683,-228.968,404.329,-179.138,-0.781,91.261]
    desc_pos2=[-333.683,-100.8,404.329,-179.138,-0.781,91.261]
    zlength1 =10
    zlength2 =15
    zangle1 =10
    zangle2 =15
    #測試外設指令
    ret = robot.SetGripperConfig(4,0)  #配置夾爪
    print("配置夾爪錯誤碼", ret)
    time.sleep(1)
    config = robot.GetGripperConfig()     #取得夾爪配置
    print("取得夾爪配置",config)
    error = robot.ActGripper(1,0)  #啟動夾爪
    print("啟動夾爪錯誤碼",error)
    time.sleep(1)
    error = robot.ActGripper(1,1)#啟動夾爪
    print("啟動夾爪錯誤碼",error)
    time.sleep(2)
    error = robot.MoveGripper(1,100,48,46,30000,0,0,0,0,0) #控制夾爪
    print("控制夾爪錯誤碼",error)
    time.sleep(3)
    error = robot.MoveGripper(1,0,50,0,30000,0,0,0,0,0) #控制夾爪
    print("控制夾爪錯誤碼",error)
    error = robot.GetGripperMotionDone() #取得夾爪運動狀態
    print("取得夾爪運動狀態錯誤碼",error)
    error = robot.ComputePrePick(desc_pos1, zlength1, zangle1) #計算預抓取點-視覺
    print("计算预抓取點",error)
    error = robot.ComputePrePick(desc_pos2, zlength2, zangle2) #計算撤退點-視覺
    print("计算撤退點",error)

計算預抓取點-視覺
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePrePick(desc_pos, zlength, zangle)``"
    "描述", "計算預抓取點-視覺"
    "必選參數", "- ``desc_pos``：夹抓取點笛卡爾位姿;
    - ``zlength``：z軸偏移量;
    - ``zangle``：繞z軸旋轉偏移量"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``pre_pos``：预抓取點笛卡爾位姿"

計算撤退點-視覺
++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputePostPick(desc_pos, zlength, zangle)``"
    "描述", "計算撤退點-視覺"
    "必選參數", "- ``desc_pos``：抓取點笛卡爾位姿;
    - ``zlength``：z軸偏移量;
    - ``zangle``：繞z軸旋轉偏移量"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``post_pos``：撤退點笛卡兒位姿"

設定啟用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAxleLuaGripperFunc(id, func)``"
    "描述", "設定啟用夾爪動作控制功能"
    "必選參數", "- ``id``：夾爪設備編號
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置設定；3-速度設定；4-力矩設定；6-讀夹爪狀態；7-讀初始化狀態；8-讀故障码；9-讀位置；10-讀速度；11-讀力矩,12-15预留"
    "默認參數", "無"
    "傳回值", "錯誤碼 成功-0 失敗- errcode "

取得啟用夾爪動作控制功能
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetAxleLuaGripperFunc(id)``"
    "描述", "取得啟用夾爪動作控制功能"
    "必選參數", "- ``id``：夾爪設備編號"
    "默認參數", "無"
    "傳回值", "- 錯誤碼 成功-0 失敗- errcode 
    - ``func``：0-夹爪使能；1-夹爪初始化；2-位置設定；3-速度設定；4-力矩設定；6-讀夹爪狀態；7-讀初始化狀態；8-讀故障码；9-讀位置；10-讀速度；11-讀力矩,12-15预留"