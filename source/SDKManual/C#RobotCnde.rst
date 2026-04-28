CNDE
=================

.. toctree:: 
    :maxdepth: 5

配置機器人CNDE的數據列表和更新週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 配置機器人即時狀態反饋的數據列表和更新週期（覆蓋之前的配置）
    * @param [in] states 要訂閱的狀態枚舉列表，順序決定數據包中的排列順序。
    * @param [in] period 數據更新週期，單位毫秒，取值範圍 [8, 1000]
    * @return 成功返回 0；失敗返回負錯誤碼（如 ERR_STATE_INVALID、ERR_PARAM_VALUE 等）
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> states, int period)

在現有狀態反饋列表中新增一個狀態項
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 在現有狀態反饋列表中新增一個狀態項
    * @param [in] state 要新增的狀態枚舉值。
    * @return 成功返回 0；失敗返回負錯誤碼（如 ERR_STATE_ALREADY_EXISTS、ERR_STATE_INVALID 等）
    */
    public int AddRobotRealtimeState(RobotState state)
    
從現有狀態反饋列表中刪除一個狀態項
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 從現有狀態反饋列表中刪除一個狀態項（至少保留一個狀態）
    * @param [in] state 要刪除的狀態枚舉值
    * @return 成功返回 0；失敗返回負錯誤碼（如 ERR_STATE_INVALID、ERR_NEED_AT_LEAST_ONE_STATE）
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
僅修改狀態反饋的更新週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

     /**
    * @brief 僅修改狀態反饋的更新週期，不改變狀態列表
    * @param [in] period 新的更新週期，單位毫秒，取值範圍 [8, 1000]
    * @return 成功返回 0；失敗返回負錯誤碼（如 ERR_PARAM_VALUE）
    */
    public int SetRobotRealtimeStatePeriod(int period)
        
獲取當前配置的狀態反饋列表和更新週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    /**
    * @brief 獲取當前配置的狀態反饋列表和更新週期
    * @param [out] states 輸出當前訂閱的狀態枚舉列表
    * @param [out] period 輸出當前數據更新週期，單位毫秒
    * @return 成功返回 0；失敗返回負錯誤碼。
    */
    public int GetRobotRealtimeStateConfig(out List<RobotState> states, out int period)

CNDE配置相關的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestRobotRealtimeStates()
    {
        // 1. 定義需要訂閱的狀態欄位
        List<RobotState> requiredStates = new List<RobotState>
        {
            RobotState.JointCurPos,
            RobotState.ToolCurPos, 
            RobotState.JointDriverTemperature,
            RobotState.RobotTime,
        };

        // 2. 配置狀態反饋（週期 8ms）
        int periodMs = 8;
        int ret = robot.SetRobotRealtimeStateConfig(requiredStates, periodMs);
        if (ret != 0)
        {
            Console.WriteLine($"配置狀態失敗，錯誤碼: {ret}");
            return;
        }
        Console.WriteLine($"狀態配置成功，共 {requiredStates.Count} 個欄位，週期 {periodMs} ms");

        // 驗證配置是否生效
        List<RobotState> actualStates;
        int actualPeriod;
        robot.GetRobotRealtimeStateConfig(out actualStates, out actualPeriod);
        Console.WriteLine($"實際生效的狀態數: {actualStates.Count}, 週期: {actualPeriod} ms");
        Thread.Sleep(3000);
        // 3. 建立 RPC 連線（內部自動完成 CNDE 握手）
        robot.SetReconnectParam(true, 10, 1000);
        ret = robot.RPC("192.168.58.2");  // 請根據實際機器人 IP 修改
        if (ret != 0)
        {
            Console.WriteLine($"RPC 連線失敗，錯誤碼: {ret}");
            return;
        }
        // 4. 循環讀取並列印狀態數據
        DateTime startTime = DateTime.Now;
        const int durationSeconds = 500;

        while ((DateTime.Now - startTime).TotalSeconds < durationSeconds)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            ret = robot.GetRobotRealTimeState(ref pkg);
            Console.WriteLine($"GetRobotRealTimeState: {ret}");

            //關節位置（度）
            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
                Console.WriteLine($"關節位置(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");

            //TCP 位姿（mm /°）
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
                Console.WriteLine($"TCP位姿(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
    
            // 關節溫度
            if (pkg.jointDriverTemperature != null && pkg.jointDriverTemperature.Length >= 6)
                Console.WriteLine($"關節溫度(°C): J1={pkg.jointDriverTemperature[0]:F2}, J2={pkg.jointDriverTemperature[1]:F2}, J3={pkg.jointDriverTemperature[2]:F2}, J4={pkg.jointDriverTemperature[3]:F2}, J5={pkg.jointDriverTemperature[4]:F2}, J6={pkg.jointDriverTemperature[5]:F2}");

            // 機器人時間
            Console.WriteLine($"機器人時間: {pkg.robotTime.year}-{pkg.robotTime.mouth:D2}-{pkg.robotTime.day:D2} {pkg.robotTime.hour:D2}:{pkg.robotTime.minute:D2}:{pkg.robotTime.second:D2}.{pkg.robotTime.millisecond:D3}");

            await Task.Delay(100);
        }

        // 5. 斷開連線
        robot.CloseRPC();
    }

CNDE增刪配置狀態及設置通信週期的SDK代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c#
    :linenos:

    private async void TestAddDeleteCNDE()
    {
        List<RobotState> finalStates;
        int finalPeriod;
        // 初始配置：不請求任何狀態（默認配置）
        List<RobotState> emptyStates = new List<RobotState>();
        int ret = robot.SetRobotRealtimeStateConfig(emptyStates, 20);

        robot.SetRobotRealtimeStatePeriod(10);
        // 刪除兩個狀態
        ret = robot.DeleteRobotRealtimeState(RobotState.JointCurPos);
        Console.WriteLine($"刪除 JointCurPos 結果: {ret}");
        ret = robot.DeleteRobotRealtimeState(RobotState.ToolCurPos);
        Console.WriteLine($"刪除 ToolCurPos 結果: {ret}");
        // 新增一個狀態
        ret = robot.AddRobotRealtimeState(RobotState.CollisionLevel);
        Console.WriteLine($"新增 CollisionLevel 結果: {ret}");

        // 獲取當前配置列表並重新發送
        List<RobotState> currentStates;
        int currentPeriod;
        robot.GetRobotRealtimeStateConfig(out currentStates, out currentPeriod);
        Console.WriteLine($"當前配置狀態數: {currentStates.Count}");
        ret = robot.SetRobotRealtimeStateConfig(currentStates, currentPeriod);
        Console.WriteLine($"套用新配置結果: {ret}"); Console.WriteLine($"初始配置結果: {ret}");
        robot.GetRobotRealtimeStateConfig(out finalStates, out finalPeriod);
        Console.WriteLine($"配置狀態數量: {finalStates.Count}");
        foreach (var s in finalStates) Console.WriteLine($"  {s}");
        Console.WriteLine($"週期: {finalPeriod} ms");

        Thread.Sleep(1000);
        //  建立 RPC 連線（內部自動連線 CNDE）
        robot.SetReconnectParam(true, 100, 1000);
        ret = robot.RPC("192.168.58.2");
        if (ret != 0)
        {
            Console.WriteLine($"RPC 連線失敗: {ret}");
            return;
        }

        // 循環列印刪除和新增的狀態，刪除的狀態列印為0，新增的狀態可正常獲取即時值
        DateTime lastTime = DateTime.Now;
        int frameCount = 0;
        DateTime startTime = DateTime.Now;
        while ((DateTime.Now - startTime).TotalSeconds < 10)
        {
            ROBOT_STATE_PKG pkg = new ROBOT_STATE_PKG();
            robot.GetRobotRealTimeState(ref pkg);
            DateTime now = DateTime.Now;
            double interval = (now - lastTime).TotalMilliseconds;
            lastTime = now;
            frameCount++;

            if (pkg.jt_cur_pos != null && pkg.jt_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  關節位置(°): J1={pkg.jt_cur_pos[0]:F2}, J2={pkg.jt_cur_pos[1]:F2}, J3={pkg.jt_cur_pos[2]:F2}, J4={pkg.jt_cur_pos[3]:F2}, J5={pkg.jt_cur_pos[4]:F2}, J6={pkg.jt_cur_pos[5]:F2}");
            }
            if (pkg.tl_cur_pos != null && pkg.tl_cur_pos.Length >= 6)
            {
                Console.WriteLine($"  TCP位姿(mm/°): X={pkg.tl_cur_pos[0]:F2}, Y={pkg.tl_cur_pos[1]:F2}, Z={pkg.tl_cur_pos[2]:F2}, RX={pkg.tl_cur_pos[3]:F2}, RY={pkg.tl_cur_pos[4]:F2}, RZ={pkg.tl_cur_pos[5]:F2}");
            }
            // 碰撞等級
            if (pkg.collisionLevel != null && pkg.collisionLevel.Length >= 6)
                Console.WriteLine($"碰撞等級: J1={pkg.collisionLevel[0]}, J2={pkg.collisionLevel[1]}, J3={pkg.collisionLevel[2]}, J4={pkg.collisionLevel[3]}, J5={pkg.collisionLevel[4]}, J6={pkg.collisionLevel[5]}");

            await Task.Delay(50);
        }
        //斷開連線
        robot.CloseRPC();
        Console.WriteLine("測試完成。");
    }