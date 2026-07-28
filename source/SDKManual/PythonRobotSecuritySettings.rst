機器人安全設置
=================

.. toctree:: 
    :maxdepth: 5

設置碰撞等級
+++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetAnticollision (mode,level,config)``"
    "描述", "設置碰撞等級"
    "必選參數", "- ``mode``:0-等級，1-百分比；
    - ``level=[j1,j2,j3,j4,j5,j6]``:碰撞閾值；
    - ``config``:0-不更新配置文件，1-更新配置文件"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置碰撞後策略
++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionStrategy(strategy,safeTime,safeDistance,safeVel,safetyMargin)``"
    "描述", "設置碰撞後策略"
    "必選參數", "- ``strategy``：0-報錯暫停，1-繼續運行，2-報錯停止，3-重力矩模式，4-震盪相應模式，5-碰撞回彈模式"
    "默認參數", "- ``safeTime``：安全停止時間[1000-2000]ms，默認爲：1000
    - ``safeDistance``：安全停止距離[1-150]mm，默認爲：100
    - ``safeVel``：安全停止速度[50-250]mm/s，默認爲：250
    - ``safetyMargin[6]``：安全係數[1-10]，默認爲：[10,10,10,10,10,10]"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

自定義碰撞檢測閾值功能開始，設置關節端和TCP端的碰撞檢測閾值
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomCollisionDetectionStart(flag, jointDetectionThreshould, tcpDetectionThreshould, block)``"
    "描述", "自定義碰撞檢測閾值功能開始，設置關節端和TCP端的碰撞檢測閾值"
    "必選參數", "- ``flag``： 1-僅關節檢測開啓；2-僅TCP檢測開啓；3-關節和TCP檢測同時開啓
    - ``jointDetectionThreshould``： 關節碰撞檢測閾值 j1-j6
    - ``tcpDetectionThreshould``： TCP碰撞檢測閾值，xyzabc
    - ``block``： 0-非阻塞；1-阻塞"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

自定義碰撞檢測閾值功能關閉
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.0

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CustomCollisionDetectionEnd()``"
    "描述", "自定義碰撞檢測閾值功能關閉"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

機器人碰撞等級設置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    mode = 0
    config = 1
    level1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    level2 = [50.0, 20.0, 30.0, 40.0, 50.0, 60.0]
    rtn = robot.SetAnticollision(mode, level1, config)
    print(f"SetAnticollision mode 0 rtn is {rtn}")
    mode = 1
    rtn = robot.SetAnticollision(mode, level2, config)
    print(f"SetAnticollision mode 1 rtn is {rtn}")
    p1Joint = [-11.904, -99.669, 117.473, -108.616, -91.726, 74.256]
    p2Joint = [-45.615, -106.172, 124.296, -107.151, -91.282, 74.255]
    p1Desc = [-419.524, -13.000, 351.569, -178.118, 0.314, 3.833]
    p2Desc = [-321.222, 185.189, 335.520, -179.030, -1.284, -29.869]
    exaxisPos = [0.0, 0.0, 0.0, 0.0]
    offdese = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100, blendR=2)
    robot.ResetAllError()
    safety = [5, 5, 5, 5, 5, 5]
    rtn = robot.SetCollisionStrategy(3, 1000, 150, 250, safety)
    print(f"SetCollisionStrategy rtn is {rtn}")
    jointDetectionThreshould = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    tcpDetectionThreshould = [60, 60, 60, 60, 60, 60]
    rtn = robot.CustomCollisionDetectionStart(3, jointDetectionThreshould, tcpDetectionThreshould, 0)
    print(f"CustomCollisionDetectionStart rtn is {rtn}")
    robot.MoveL(desc_pos=p1Desc, tool=0, user=0, vel=100)
    robot.MoveL(desc_pos=p2Desc, tool=0, user=0, vel=100)
    rtn = robot.CustomCollisionDetectionEnd()
    print(f"CustomCollisionDetectionEnd rtn is {rtn}")
    robot.CloseRPC()

設置正限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitPositive(p_limit)``"
    "描述", "設置正限位"
    "必選參數", "- ``p_limit=[j1,j2,j3,j4,j5,j6]``：六個關節位置"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

設置負限位
+++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetLimitNegative(n_limit)``"
    "描述", "設置負限位"
    "必選參數", "- ``n_limit=[j1,j2,j3,j4,j5,j6]``：六個關節位置"
    "默認參數", "無"
    "返回值", "錯誤碼 成功-0  失敗- errcode"

獲取關節軟限位角度
+++++++++++++++++++
.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``GetJointSoftLimitDeg(flag=1)``"
    "描述", "獲取關節軟限位角度"
    "必選參數", "無"
    "默認參數", "``flag``：0-阻塞，1-非阻塞  默認1"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode
    - ``[j1min,j1max,j2min,j2max,j3min,j3max, j4min,j4max,j5min, j5max, j6min,j6max]``：軸1~軸6，關節負限位與正限位，單位[mm]"

機器人限位設置代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    plimit = [170.0, 80.0, 150.0, 80.0, 170.0, 160.0]
    robot.SetLimitPositive(plimit)
    nlimit = [-170.0, -260.0, -150.0, -260.0, -170.0, -160.0]
    robot.SetLimitNegative(nlimit)
    error,neg_deg = robot.GetJointSoftLimitDeg(0)
    print(f"pos limit deg: {neg_deg[1]}, {neg_deg[3]}, {neg_deg[5]}, {neg_deg[7]}, {neg_deg[9]}, {neg_deg[11]}")
    print(f"neg limit deg: {neg_deg[0]}, {neg_deg[2]}, {neg_deg[4]}, {neg_deg[6]}, {neg_deg[8]}, {neg_deg[10]}")
    robot.CloseRPC()

設置機器人碰撞檢測方法
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.1.2

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetCollisionDetectionMethod(method, thresholdMode)``"
    "描述", "設置機器人碰撞檢測方法"
    "必選參數", "
    - ``method``：碰撞檢測方法：0-電流模式；1-雙編碼器；2-電流和雙編碼器同時開啓
    - ``thresholdMode``：碰撞等級閾值方式；0-碰撞等級固定閾值方式；1-自定義碰撞檢測閾值  
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

設置靜態下碰撞檢測開始關閉
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetStaticCollisionOnOff(status)``"
    "描述", "設置靜態下碰撞檢測開始關閉"
    "必選參數", "
    - ``status``： 0-關閉；1-開啓
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

設置機器人碰撞檢測方法代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    rtn = robot.SetCollisionDetectionMethod(0,0)
    rtn = robot.SetStaticCollisionOnOff(1)
    print(f"SetStaticCollisionOnOff On rtn is {rtn}")
    time.sleep(5)
    rtn = robot.SetStaticCollisionOnOff(0)
    print(f"SetStaticCollisionOnOff Off rtn is {rtn}")
    robot.CloseRPC()

關節扭矩功率檢測
+++++++++++++++++++++++++++++++++
.. versionadded:: python SDK-v2.0.5

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetPowerLimit(status, power)``"
    "描述", "關節扭矩功率檢測"
    "必選參數", "
    - ``status``：0-關閉；1-開啓
    - ``power``：設定最大功率(W)
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"
    
關節扭矩功率檢測代碼示例
+++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time
    # 與機器人控制器建立連接，連接成功返回一個機器人對象
    robot = Robot.RPC('192.168.58.2')
    robot.DragTeachSwitch(1)
    robot.SetPowerLimit(1, 200)
    error,torques = robot.GetJointTorques(1)
    count = 100
    robot.ServoJTStart()
    while count > 0:
        error = robot.ServoJT(torques, 0.001)
        count -= 1
        time.sleep(0.001)  # 1ms delay
    error = robot.ServoJTEnd()
    robot.DragTeachSwitch(0)
    robot.CloseRPC()

設置安全速度參數
+++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetVelReducePara(enable, maxTCPVel, strategy, maxJointVel=[45.0, 45.0, 45.0, 45.0, 45.0, 45.0])``"
    "描述", "設置安全速度參數"
    "必選參數", "
    - ``enable``：0-關；1-手動模式啟用；2-所有模式啟用(不支援自動限速)
    - ``maxTCPVel``：限制最大TCP速度;[0-1000]mm/s
    - ``strategy``：超速後策略；0-停止報警；1-自動限速；2-停止報警並去使能
    - ``maxJointVel``：6個關節最大速度(°/s) 預設為[45.0, 45.0, 45.0, 45.0, 45.0, 45.0]
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗- errcode"

設置安全速度參數的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    import time


    def main():
        robot = Robot.RPC('192.168.58.2')
        time.sleep(0.5)  

        j1 = [10.220, -11.121, -118.086, -46.739, 82.036, 131.503]
        j2 = [89.782, -11.122, -118.086, -46.740, 82.036, 131.504]

        epos = [0.0, 0.0, 0.0, 0.0]
        offset_pos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        robot.SetSpeed(20)

        maxJointVel = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]

        rtn = robot.SetVelReducePara(0, 200, 0, maxJointVel)
        robot.MoveJ(joint_pos=j2, tool=1, user=2, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        rtn = robot.SetVelReducePara(2, 200, 0, maxJointVel)
        print(f"SetVelReduceParaA param error rtn is {rtn}")

        robot.MoveJ(joint_pos=j1, tool=1, user=2, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=1, user=2, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        maxJointVel = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0]
        rtn = robot.SetVelReducePara(2, 200, 0, maxJointVel)
        print(f"SetVelReduceParaB reduce vel rtn is {rtn}")

        robot.MoveJ(joint_pos=j1, tool=1, user=2, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)
        robot.MoveJ(joint_pos=j2, tool=1, user=2, vel=100, acc=100, ovl=100,
                    exaxis_pos=epos, blendT=-1, offset_flag=0, offset_pos=offset_pos)

        robot.CloseRPC()

    if __name__ == "__main__":
        main()