CNDE
=============

.. toctree:: 
    :maxdepth: 5

配置機器人狀態反饋
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 配置機器人狀態反饋
    * @param state 機器人狀態列舉列表
    * @param period 狀態反饋週期，範圍8-1000
    * @return 錯誤碼，正常-0，參數異常-4，狀態欄位不存在-18，總位元組數超過4K-20
    */
    public int SetRobotRealtimeStateConfig(List<RobotState> state, int period)
    
CNDE狀態配置添加一個機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 添加一個機器人狀態到配置列表
    * @param state 機器人狀態列舉
    * @return 錯誤碼，正常-0，狀態已存在-17，狀態欄位不存在-18，超過4K-20
    */
    public int AddRobotRealtimeState(RobotState state)
    
CNDE狀態配置刪除一個機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 從配置列表刪除一個機器人狀態
    * @param state 機器人狀態列舉
    * @return 錯誤碼，正常-0，狀態不存在-18，至少保留一個狀態-19
    */
    public int DeleteRobotRealtimeState(RobotState state)
        
設置CNDE狀態反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 設置CNDE狀態反饋週期
    * @param period 狀態反饋週期，範圍8-1000
    * @return 錯誤碼，正常-0，參數異常-4
    */
    public int SetRobotRealtimeStatePeriod(int period)
            
獲取當前CNDE狀態反饋所有狀態集合和週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
     * @brief 獲取當前所有狀態集合和週期
     * @return 包含狀態列表和週期的配置結果結構體
    */
    public StateConfigResult GetRobotRealtimeStateConfig()
                
CNDE狀態反饋使用代碼示例
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief CNDE即時狀態配置介面使用示例
    */
    public static void TestRealtimeStateConfig(Robot robot)
    {
        
        // 1. 創建初始狀態列表
        List<RobotState> stateList1 = new ArrayList<>();
        stateList1.add(RobotState.ProgramState);
        stateList1.add(RobotState.RobotState);
        stateList1.add(RobotState.JointCurPos);
        stateList1.add(RobotState.ToolCurPos);
        
        // 2. 第一次調用 SetRobotRealtimeStateConfig 配置狀態和週期
        int period1 = 100;  // 100ms週期
        int rtn = robot.SetRobotRealtimeStateConfig(stateList1, period1);
        System.out.printf("1. SetRobotRealtimeStateConfig (初始列表, 週期=%d) rtn: %d%n", period1, rtn);
        
        if (rtn == 0) {
            // 3. 添加額外狀態
            rtn = robot.AddRobotRealtimeState(RobotState.RobotTime);
            System.out.printf("2. AddRobotRealtimeState (RobotTime) rtn: %d%n", rtn);
            
            // 4. 再次調用 SetRobotRealtimeStateConfig 重新配置（不同狀態列表）
            List<RobotState> stateList2 = new ArrayList<>();
            stateList2.add(RobotState.ProgramState);
            stateList2.add(RobotState.RobotState);
            stateList2.add(RobotState.MainCode);
            stateList2.add(RobotState.SubCode);
            stateList2.add(RobotState.JointCurPos);
            stateList2.add(RobotState.ToolCurPos);
            stateList2.add(RobotState.ActualJointTorque);
            
            int period2 = 50;  // 50ms週期
            rtn = robot.SetRobotRealtimeStateConfig(stateList2, period2);
            System.out.printf("3. SetRobotRealtimeStateConfig (更新列表, 週期=%d) rtn: %d%n", period2, rtn);
            
            // 5. 修改週期
            int newPeriod = 80;  // 80ms週期
            rtn = robot.SetRobotRealtimeStatePeriod(newPeriod);
            System.out.printf("4. SetRobotRealtimeStatePeriod (週期=%d) rtn: %d%n", newPeriod, rtn);
            
            // 6. 獲取當前配置並列印
            Robot.StateConfigResult configResult = robot.GetRobotRealtimeStateConfig();
            System.out.println("5. GetRobotRealtimeStateConfig 結果:");
            System.out.printf("   - 週期: %d ms%n", configResult.period);
            System.out.println("   - 已配置的狀態:");
            for (int i = 0; i < configResult.stateList.size(); i++) {
                System.out.printf("     [%d] %s%n", i, configResult.stateList.get(i));
            }
            
            rtn = robot.RPC("192.168.58.2");
            if (rtn == 0) {
                System.out.println("rpc連接成功");
            } else {
                System.out.println("rpc連接失敗");
                return;
            }
            // 等待CNDE連接建立
            System.out.println("等待CNDE連接建立...");
            while (robot.CNDEGetStateData() == null) {
                robot.Sleep(100);
            }
            System.out.println("CNDE連接已建立，開始接收數據...");

            // 7. 循環讀取即時狀態驗證配置是否生效
            System.out.println("6. 讀取即時狀態...");
            while(true) {
                robot.Sleep(1000);
                // 透過 CNDE 獲取狀態數據
                ROBOT_STATE_PKG pkg = robot.CNDEGetStateData();
                if (pkg == null) {
                    System.out.println("狀態數據為空，CNDE連線中斷，等待重連");
                    continue;  // 連線中斷時繼續循環，等待重連
                }
                System.out.println("\n--- 機器人時間 ---");
                if (pkg.robotTime != null) {
                    System.out.println("robotTime: " + pkg.robotTime.year + "-" + pkg.robotTime.month + "-" + pkg.robotTime.day +
                            " " + pkg.robotTime.hour + ":" + pkg.robotTime.minute + ":" + pkg.robotTime.second +
                            "." + pkg.robotTime.millisecond);
                }

                System.out.println("   --- 狀態資訊 ---");
                System.out.printf("   program_state: %d%n", pkg.program_state);
                System.out.printf("   robot_state: %d%n", pkg.robot_state);
                System.out.printf("   main_code: %d%n", pkg.main_code);
                System.out.printf("   sub_code: %d%n", pkg.sub_code);
                System.out.println("   --- 關節位置 (actual_joint_pos) ---");
                System.out.printf("   jt_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[0], pkg.jt_cur_pos[1], pkg.jt_cur_pos[2]);
                System.out.printf("   jt_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_pos[3], pkg.jt_cur_pos[4], pkg.jt_cur_pos[5]);
                System.out.println("   --- TCP位置 (actual_TCP_pos) ---");
                System.out.printf("   tl_cur_pos[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[0], pkg.tl_cur_pos[1], pkg.tl_cur_pos[2]);
                System.out.printf("   tl_cur_pos[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.tl_cur_pos[3], pkg.tl_cur_pos[4], pkg.tl_cur_pos[5]);
                System.out.println("   --- 關節力矩 (actual_joint_torque) ---");
                System.out.printf("   jt_cur_tor[0-2]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[0], pkg.jt_cur_tor[1], pkg.jt_cur_tor[2]);
                System.out.printf("   jt_cur_tor[3-5]: %.2f, %.2f, %.2f%n",
                    pkg.jt_cur_tor[3], pkg.jt_cur_tor[4], pkg.jt_cur_tor[5]);
                robot.Sleep(500);
            }
        } else {
            System.out.printf("SetRobotRealtimeStateConfig 失敗，錯誤碼: %d%n", rtn);
        }
    }