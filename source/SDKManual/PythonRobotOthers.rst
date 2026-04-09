其他接口
=================

.. toctree:: 
    :maxdepth: 5

獲取SSH公鑰
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSSHKeygen()``"
    "描述", "獲取SSH公鑰"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``keygen``：公鑰"

下發SCP指令
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.3

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetSSHScpCmd(mode, sshname, sship, usr_file_url, robot_file_url)``"
    "描述", "下發SCP指令"
    "必選參數", "- ``mode``：0-上傳（上位機->控制器），1-下載（控制器->上位機）
    - ``sshname``：上位機用戶名
    - ``sship``：上位機ip地址
    - ``usr_file_url``：上位機文件路徑
    - ``robot_file_url``：機器人控制器文件路徑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

計算指定路徑下文件的MD5值
++++++++++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``ComputeFileMD5(file_path)``"
    "描述", "計算指定路徑下文件的MD5值"
    "必選參數", "- ``file_path``：文件路徑包含文件名，默認Traj文件夾路徑爲:/fruser/traj/,如/fruser/traj/trajHelix_aima_1.txt"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``md5``：文件MD5值"

機器人SSH、MD5指令代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    file_path = "/fruser/airlab.lua"
    md5 = ""
    emerg_state = 0
    si0_state = 0
    si1_state = 0
    sdk_com_state = 0
    ssh_keygen = ""
    retval,ssh_keygen = robot.GetSSHKeygen()
    print(f"GetSSHKeygen retval is: {retval}")
    print(f"ssh key is: {ssh_keygen}")
    ssh_name = "fr"
    ssh_ip = "192.168.58.45"
    ssh_route = "/home/fr"
    ssh_robot_url = "/root/robot/dhpara.config"
    retval = robot.SetSSHScpCmd(1, ssh_name, ssh_ip, ssh_route, ssh_robot_url)
    print(f"SetSSHScpCmd retval is: {retval}")
    print(f"robot url is: {ssh_robot_url}")
    error, md5 = robot.ComputeFileMD5(file_path)
    print(f"md5 is: {md5}")
    robot.CloseRPC()

設置機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateSamplePeriod(period)``"
    "描述", "設置機器人 20004 端口反饋週期"
    "必選參數", "- ``period``：機器人 20004 端口反饋週期(ms)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode "

獲取機器人 20004 端口反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotRealtimeStateSamplePeriod()``"
    "描述", "獲取機器人 20004 端口反饋週期"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``period``：機器人 20004 端口反饋週期(ms)"

機器人20004端口狀態反饋週期配置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.SetRobotRealtimeStateSamplePeriod(10)
    error,getPeriod = robot.GetRobotRealtimeStateSamplePeriod()
    print(f"period is {getPeriod}")
    time.sleep(1)
    robot.CloseRPC()

機器人軟件升級
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SoftwareUpgrade(filePath, block)``"
    "描述", "機器人軟件升級"
    "必選參數", "- ``filePath``：軟件升級包全路徑
    - ``block``：是否阻塞至升級完成 true:阻塞；false:非阻塞"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode "

獲取機器人軟件升級狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetSoftwareUpgradeState()``"
    "描述", "獲取機器人軟件升級狀態"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode 
    - ``state``：機器人軟件包升級狀態，0：空閒中或上傳升級包中，1~100：升級完成百分比，-1：升級軟件失敗，-2：校驗失敗，-3：版本校驗失敗，-4：解壓失敗，-5：用戶配置升級失敗，-6：外設配置升級失敗，-7：擴展軸配置升級失敗，-8：機器人配置升級失敗，-9：DH參數配置升級失敗"

機器人軟件升級代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    error = robot.SoftwareUpgrade("D://zUP/QNX382/software.tar.gz", False)
    print(f"SoftwareUpgrade error is {error}")
    while True:
        curState = robot.GetSoftwareUpgradeState()
        print(f"upgrade state is {curState}")
        time.sleep(3)
    robot.CloseRPC()

下載點位表數據庫
+++++++++++++++++++++++++++++++

.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableDownLoad(point_table_name, save_file_path)``"
    "描述", "下載點位表數據庫"
    "必選參數", "- ``point_table_name``：要下載的點位表名稱    pointTable1.db;
    - ``save_file_path``:下載點位表的存儲路徑   C://test/;"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

上傳點位表數據庫
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpLoad(point_table_file_path)``"
    "描述", "上傳點位表數據庫"
    "必選參數", "- ``point_table_file_path``：上傳點位表的全路徑名   C://test/pointTable1.db"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

點位表更新lua文件
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``PointTableUpdateLua(point_table_name, lua_file_name)``"
    "描述", "點位表更新lua文件"
    "必選參數", "- ``point_table_name``：要切換的點位表名稱pointTable1.db,當點位表爲空，即""時，表示將lua程序更新爲未應用點位表的初始程序
    - ``lua_file_name``: 要更新的lua文件名稱 testPointTable.lua"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人點位表操作代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    save_path = "D://zDOWN/"
    point_table_name = "point_table_FR5.db"
    rtn = robot.PointTableDownLoad(point_table_name, save_path)
    print(f"download : {point_table_name} fail: {rtn}")
    upload_path = "D://zDOWN/point_table_FR5.db"
    rtn = robot.PointTableUpLoad(upload_path)
    print(f"retval is: {rtn}")
    point_tablename = "point_table_FR5.db"
    lua_name = "test0610.lua"
    rtn,error = robot.PointTableUpdateLua(point_tablename, lua_name)
    print(f"retval is: {rtn}")
    robot.CloseRPC()

控制器日誌下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RbLogDownload(savePath)``"
    "描述", "控制器日誌下載"
    "必選參數", "- ``savePath``：保存文件路徑D://zDown/"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

所有數據源下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AllDataSourceDownload(savePath)``"
    "描述", "所有數據源下載"
    "必選參數", "- ``savePath``：保存文件路徑D://zDown/"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

數據備份包下載
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.1

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DataPackageDownload(savePath)``"
    "描述", "數據備份包下載"
    "必選參數", "- ``savePath``：保存文件路徑D://zDown/"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

下載控制器數據代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.RbLogDownload("D://zDOWN/")
    print(f"RbLogDownload rtn is {rtn}")
    rtn = robot.AllDataSourceDownload("D://zDOWN/")
    print(f"AllDataSourceDownload rtn is {rtn}")
    rtn = robot.DataPackageDownload("D://zDOWN/")
    print(f"DataPackageDownload rtn is {rtn}")
    robot.CloseRPC()

設置編碼器升級
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetEncoderUpgrade(path)``"
    "描述", "設置編碼器升級"
    "必選參數", "- ``path``：本地升級包全路徑(D://zUP/XXXXX.bin)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置關節固件升級
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetJointFirmwareUpgrade(type, path)``"
    "描述", "設置關節固件升級"
    "必選參數", "- ``type``：升級文件類型；1-升級固件；2-升級從站配置文件
    - ``path``：本地升級包全路徑(D://zUP/XXXXX.bin)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置控制箱固件升級
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCtrlFirmwareUpgrade(type, path)``"
    "描述", "設置控制箱固件升級"
    "必選參數", "- ``type``：升級文件類型；1-升級固件；2-升級從站配置文件
    - ``path``：本地升級包全路徑(D://zUP/XXXXX.bin)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
    
設置末端固件升級
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetEndFirmwareUpgrade(type, path)``"
    "描述", "設置末端固件升級"
    "必選參數", "- ``type``：升級文件類型；1-升級固件；2-升級從站配置文件
    - ``path``：本地升級包全路徑(D://zUP/XXXXX.bin)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
       
關節全參數配置文件升級
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.4

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``JointAllParamUpgrade(path)``"
    "描述", "關節全參數配置文件升級"
    "必選參數", "- ``path``：本地升級包全路徑(D://zUP/XXXXX.bin)"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

機器人從站固件升級代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from fairino import Robot
    import time
    import threading
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.RobotEnable(0)
    time.sleep(0.2)
    rtn = robot.JointAllParamUpgrade("D://zUP/MT/joint0603/jointallparameters.db")
    print(f"robot JointAllParamUpgrade rtn is {rtn}")
    rtn = robot.SetCtrlFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Cbd_Asix_V2.0.bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(2, "D://zUP/MT/FAIR_Cobot_Axle_Asix_V2.4.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    robot.SetSysServoBootMode()
    time.sleep(0.2)
    rtn = robot.SetCtrlFirmwareUpgrade(1, "D://zUP/MT/FR_CTRL_PRIMCU_FV201412_MAIN_U4_T01_20250630(MT).bin")
    print(f"robot SetCtrlFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetEndFirmwareUpgrade(1, "D://zUP/MT/FR_END_FV2010010_MAIN_U1_T01_20250603.bin")
    print(f"robot SetEndFirmwareUpgrade rtn is {rtn}")
    rtn = robot.SetJointFirmwareUpgrade(1, "D://zUP/MT/FR_SERVO_FV504215_MAIN_U7_T07_20250603.bin")
    print(f"robot SetJointFirmwareUpgrade rtn is {rtn}")
    robot.CloseRPC()

機器人操作系統升級(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``KernelUpgrade(filePath)``"
    "描述", "機器人操作系統升級(LA控制箱)"
    "必選參數", "- ``filePath``：操作系統升級包全路徑"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
       
獲取機器人操作系統升級結果(LA控制箱)
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.6

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetKernelUpgradeResult()``"
    "描述", "獲取機器人操作系統升級結果(LA控制箱)"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
       
機器人MCU日誌生成
+++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.7

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``RobotMCULogCollect()``"
    "描述", "機器人MCU日誌生成"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置端口通訊斷開時停止機器人運行
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotStopOnComDisc(portID, enable, confirmTime)``"
    "描述", "設置端口通訊斷開時停止機器人運行"
    "必選參數", "
    - ``portID``：端口編號 0-8080；1-8083；2-20002；3-20004
    - ``enable``：0-關閉；1-開啟
    - ``confirmTime``：通訊中斷確認時長(ms)[0-5000]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"
           
獲取端口通訊斷開時停止機器人運行參數
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetRobotStopOnComDisc(portID)``"
    "描述", "獲取端口通訊斷開時停止機器人運行參數"
    "必選參數", "
    - ``portID``：端口編號 0-8080；1-8083；2-20002；3-20004
    - ``enable``：0-關閉；1-開啟
    - ``confirmTime``：通訊中斷確認時長(ms)[0-5000]"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

端口通訊斷開時停止機器人運行參數代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot
    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def test_robot_stop_on_com_disc(self):
        # 初始化參數
        enable = False
        confirm_time = 0

        # 設置通信斷開時機器人停止功能
        rtn = robot.SetRobotStopOnComDisc(0, True, 330)
        print(f"SetRobotStopOnComDisc index0: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(1, True, 550)
        print(f"SetRobotStopOnComDisc index1: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(2, True, 110)
        print(f"SetRobotStopOnComDisc index2: {rtn}")

        rtn = robot.SetRobotStopOnComDisc(3, True, 220)
        print(f"SetRobotStopOnComDisc index3: {rtn}")

        # 獲取通信斷開時機器人停止設置
        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(0)
        print(f"GetRobotStopOnComDisc 8080 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(1)
        print(f"GetRobotStopOnComDisc 80803 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(2)
        print(f"GetRobotStopOnComDisc 20002 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        rtn, enable, confirm_time = robot.GetRobotStopOnComDisc(3)
        print(f"GetRobotStopOnComDisc 20004 rtn {rtn}; enable is {enable}; confirm time is {confirm_time}")

        # 關閉RPC連接
        robot.CloseRPC()
        return 0

    test_robot_stop_on_com_disc(robot)

UDP發送指令幀
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SendUDPFrame(frame)``"
    "描述", "UDP發送指令幀"
    "必選參數", "
    - ``frame``：發送UDP數據，透傳，不封裝"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

基於UDP通訊的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')

    def TestSendUDPFrame(self):
        # 設置回調
        def callback(src_type, count, cmd_id, data_len, content):
            print("收到回覆: cmd_id={} count={} data_len={} content={}".format(cmd_id, count, data_len, content))
            return 0
        robot.SetUDPCmdRpyCallback(callback)

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame Mode(0) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII21III303III7IIIMode(1)III/b/f")
        print(f"SendUDPFrame Mode(1) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII49III201III184IIIMoveJ(-15.625, -82.680, 101.654, -110.950, -88.290, 0.017, -383.012, -2.325, 242.655, -178.024, 1.710, 74.416, 0, 0, 100, 100, 100, 0.000, 0.000, 0.000, 0.000, -1, 0, 0, 0, 0, 0, 0, 0)III/b/f")
        print(f"SendUDPFrame MoveJ(-15.625) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame(
            "/f/bIII48III203III199IIIMoveL(-75.622, -82.680, 101.654, -110.950, -88.290, 0.017, -193.537, 330.525, 242.657, -178.024, 1.710, 14.420, 0, 0, 100, 100, 100, -1, 0, 0.000, 0.000, 0.000, 0.000, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0)III/b/f")
        print(f"SendUDPFrame MoveL(-75.622) rtn is {rtn}")
        time.sleep(1)

        rtn = robot.SendUDPFrame("/f/bIII4III905III20IIIGetSoftwareVersion()III/b/f")
        print(f"SendUDPFrame GetSoftwareVersion() rtn is {rtn}")

        time.sleep(1)

        # 發送UDP幀數據校驗測試
        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("III20III303III7IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III7IIIMode(0)")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bIII20III303III6IIIMode(0)III/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/b|||20|||303|||7|||Mode(0)|||/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        rtn = robot.SendUDPFrame("/f/bII20II303II7IIMode(0)II/b/f")
        print(f"SendUDPFrame rtn is {rtn}")

        robot.CloseRPC()
        time.sleep(1)

    TestSendUDPFrame(robot)
    
設置用戶自定義機器人末端燈色
+++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetUserLEDColor(r, g, b)``"
    "描述", "設置用戶自定義機器人末端燈色"
    "必選參數", "
    - ``r``：末端紅燈控制；0-滅；1-亮
    - ``g``：末端綠燈控制；0-滅；1-亮
    - ``b``：末端藍燈控制；0-滅；1-亮
    - "
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置用戶自定義機器人末端燈色的SDK代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos:

    from time import sleep
    import time
    from fairino import Robot

    # 與機器人控制器建立連接
    robot = Robot.RPC('192.168.58.2')


    def testled(self):
        # 設置用戶LED燈顏色
        # 參數順序: R, G, B (紅, 綠, 藍)

        # 白色 (紅綠藍全亮)
        robot.SetUserLEDColor(True, True, True)
        time.sleep(1)

        # 關閉所有燈
        robot.SetUserLEDColor(False, False, False)
        time.sleep(1)

        # 紅色 (僅紅燈亮)
        robot.SetUserLEDColor(True, False, False)
        time.sleep(1)

        # 綠色 (僅綠燈亮)
        robot.SetUserLEDColor(False, True, False)
        time.sleep(1)

        # 藍色 (僅藍燈亮)
        robot.SetUserLEDColor(False, False, True)

        # 關閉連接
        robot.CloseRPC()

    testled(robot)