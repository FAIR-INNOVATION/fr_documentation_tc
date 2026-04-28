CNDE
=============

.. toctree:: 
    :maxdepth: 5

配置機器人CNDE狀態反饋
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStateConfig(states: List[RobotState], period: int = 500) -> int:``"
    "描述", "設置CNDE默認配置（在RPC連接前調用）"
    "必選參數", "
    - ``states``：RobotState枚舉列表
    - ``period``：數據週期(ms)，範圍8-1000，默認8ms
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode"

CNDE狀態配置添加機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``AddRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "描述", "在配置基礎上添加CNDE狀態列表（支持動態維護和IP隔離）"
    "必選參數", "
    - ``states``：RobotState枚舉列表，要添加的狀態
    - ``ip``：可選，指定機器人IP（用於多機器人隔離配置，不提供則修改全域配置）
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode"

CNDE狀態配置刪除機器人狀態
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``DeleteRobotRealtimeState(states: List[RobotState], ip: str = None) -> int:``"
    "描述", "在配置基礎上刪除CNDE狀態列表（支持動態維護和IP隔離）"
    "必選參數", "
    - ``states``：RobotState枚舉列表，要刪除的狀態
    - ``ip``：可選，指定機器人IP（用於多機器人隔離配置，不提供則修改全域配置）
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode"

設置CNDE狀態反饋週期
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``SetRobotRealtimeStatePeriod(period: int, ip: str = None) -> int:``"
    "描述", "設置CNDE狀態反饋週期（支持全域或IP隔離配置）"
    "必選參數", "
    - ``period``：數據週期(ms)，範圍8-1000
    - ``ip``：可選，指定機器人IP（不提供則修改全域配置）
    "
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode"

獲取當前CNDE狀態反饋所有狀態集合
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table:: 
    :stub-columns: 1
    :widths: 10 30

    "原型", "``CNDEGetConfig(self) -> tuple:``"
    "描述", "獲取當前所有狀態集合"
    "必選參數", "無"
    "默認參數", "無"
    "返回值", "- 錯誤碼 成功-0  失敗-errcode 包含狀態列表的配置結果結構體"

CNDE狀態反饋使用代碼示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: python
    :linenos: 

    from fairino import Robot
    from fairino.Robot import RobotState, SetRobotRealtimeStateConfig, DEFAULT_CNDE_STATES, AddRobotRealtimeState, DeleteRobotRealtimeState, SetRobotRealtimeStatePeriod
    import time

    # ==================== 全局配置參數 ====================
    ROBOT_IP = '192.168.58.2'       # 機器人IP地址
    # ========== Test1: CNDE配置與數據獲取測試 =============
    # 測試步驟:
    # 1. 設置CNDE配置 (JointCurPos, ToolCurPos, 20ms週期)
    # 2. 建立RPC連接
    # 3. 列印機器人關節和TCP位姿數據
    # 4. 獲取時間戳並驗證週期
    # 5. 修改配置 (RobotMode, RbtEnableState, 10ms週期)
    # 6. 驗證新配置生效

    def test1_cnde_config_and_data():
        """Test1: CNDE配置與數據獲取測試 - 驗證配置設置和數據即時性"""
        print_separator("Test1: CNDE配置與數據獲取測試")

        # ===== 步驟1: 設置CNDE配置 (JointCurPos, ToolCurPos, 20ms) =====
        print("\n【步驟1】設置CNDE配置...")
        print("  配置欄位: JointCurPos, ToolCurPos")
        print("  反饋週期: 20ms")

        custom_states = [
            RobotState.JointCurPos,   # 關節當前位置
            RobotState.ToolCurPos,    # 工具(TCP)當前位置
        ]

        rtn = SetRobotRealtimeStateConfig(custom_states, 20)
        if rtn != 0:
            print(f"✗ 配置設置失敗，錯誤碼: {rtn}")
            return None
        print("✓ CNDE配置設置成功")

        # ===== 步驟2: 建立RPC連接 =====
        print(f"\n【步驟2】建立RPC連接 ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # 等待連接和數據接收

        # 驗證配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 連接成功，當前配置: {len(states)} 個欄位, 週期 {period}ms")
        else:
            print("✗ 無法獲取CNDE配置")
            return robot

        # ===== 步驟3: 列印機器人關節和TCP位姿 =====
        print("\n【步驟3】列印機器人關節和TCP位姿...")
        print("  (提示: 可拖動機器人觀察數據變化)")
        print("  按 Ctrl+C 停止數據列印")
        print("  (使用 Wireshark 抓包驗證實際數據週期)\n")

        sample_count = 0
        try:
            while sample_count < 100:  # 採集100個樣本
                pkg = robot.robot_state_pkg

                # 每10幀列印一次
                if sample_count % 10 == 0:
                    print(f"--- 樣本 #{sample_count} ---")
                    print(f"  關節位置 (deg): [{', '.join([f'{x:.3f}' for x in pkg.jt_cur_pos])}]")
                    print(f"  TCP位姿 (mm/deg): [{', '.join([f'{x:.3f}' for x in pkg.tl_cur_pos])}]")
                    print(f"  當前幀計數: {pkg.frame_cnt}")
                    print()

                sample_count += 1
                time.sleep(0.02)  # 20ms

        except KeyboardInterrupt:
            print("\n  用戶中斷數據列印")

        # 關閉連接
        robot.CloseRPC()
        time.sleep(1)

        # ===== 步驟4: 修改配置並驗證 =====
        print("\n【步驟4】修改CNDE配置...")
        print("  新配置欄位: RobotMode, RbtEnableState")
        print("  新反饋週期: 10ms")

        new_states = [
            RobotState.RobotMode,
            RobotState.RbtEnableState,
        ]

        # 設置新配置
        rtn = SetRobotRealtimeStateConfig(new_states, 10)
        if rtn != 0:
            print(f"✗ 新配置設置失敗，錯誤碼: {rtn}")
            return robot
        print("✓ 新配置設置成功")

        # 重新連接
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # 驗證新配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 當前配置: {[s.name for s in states]}")
            print(f"✓ 當前週期: {period}ms")

            if period == 10:
                print("✓ 配置修改驗證通過 (週期已變為10ms)")
            else:
                print(f"⚠ 週期未生效 (期望10ms, 實際{period}ms)")

            # 列印新數據
            pkg = robot.robot_state_pkg
            print(f"\n【新配置數據】")
            print(f"  robot_mode: {pkg.robot_mode}")
            print(f"  rbtEnableState: {pkg.rbtEnableState}")
        else:
            print("✗ 無法獲取新配置")

        print("\n✓ Test1 完成")
        return robot


    if __name__ == "__main__":
        test1_cnde_config_and_data()


    # ======== Test2: Add/Delete 狀態欄位測試 ====================
    # 功能: 測試 AddRobotRealtimeState() 和 DeleteRobotRealtimeState()
    # 測試步驟:
    #   1. 使用 AddRobotRealtimeState() 添加 SpeedScaleManual 和 SpeedScaleAuto
    #   2. 連接機器人，列印手動/自動模式全局速度
    #   3. 在 WebApp 修改全局速度，觀察 SDK 數據變化
    #   4. 使用 DeleteRobotRealtimeState() 刪除添加的欄位
    #   5. 重新連接，驗證速度值是否為 0（欄位不再更新）


    def test2_add_delete_state():
        """Test2: Add/Delete 狀態欄位測試 - 驗證動態添加和刪除 CNDE 狀態"""
        print_separator("Test2: Add/Delete 狀態欄位測試")

        # ===== 步驟1: 添加 SpeedScaleManual 和 SpeedScaleAuto 欄位 =====
        print("\n【步驟1】使用 AddRobotRealtimeState() 添加速度比例欄位...")
        print("  添加欄位: SpeedScaleManual, SpeedScaleAuto")

        rtn = AddRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ 添加欄位失敗，錯誤碼: {rtn}")
            return None
        print("✓ 欄位添加成功")

        # ===== 步驟2: 建立 RPC 連接並列印速度 =====
        print(f"\n【步驟2】建立 RPC 連接 ({ROBOT_IP})...")
        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)  # 等待連接和數據接收

        # 驗證配置
        config = robot.CNDEGetConfig()
        if config:
            states, period = config
            print(f"✓ 連接成功，當前配置: {len(states)} 個欄位")
            # 檢查是否包含添加的欄位
            has_manual = RobotState.SpeedScaleManual in states
            has_auto = RobotState.SpeedScaleAuto in states
            if has_manual and has_auto:
                print("✓ 配置驗證通過: SpeedScaleManual 和 SpeedScaleAuto 已添加")
            else:
                print(f"⚠ 配置驗證警告: Manual={has_manual}, Auto={has_auto}")
        else:
            print("✗ 無法獲取 CNDE 配置")

        # 列印速度數據
        print("\n【當前速度數據】(請在 WebApp 中修改全局速度觀察變化)")
        print("  提示: 拖動機器人使能並切換手/自動模式，觀察速度值")
        print("  按 Ctrl+C 停止數據列印\n")

        sample_count = 0
        try:
            while sample_count < 100:  # 採集 100 個樣本 (約 10 秒，按 100ms 間隔)
                pkg = robot.robot_state_pkg
                print(f"  [{sample_count:3d}] SpeedScaleManual: {pkg.speedScaleManual:.2f}, "
                    f"SpeedScaleAuto: {pkg.speedScaleAuto:.2f}, "
                    f"Mode: {pkg.robot_mode}")
                sample_count += 1
                time.sleep(0.1)  # 100ms 間隔
        except KeyboardInterrupt:
            print("\n  用戶中斷數據列印")

        print(f"\n✓ 數據採集完成，共 {sample_count} 個樣本")

        # ===== 步驟3: 斷開連接 =====
        print("\n【步驟3】斷開當前連接...")
        robot.CloseRPC()
        time.sleep(1.0)  # 等待CNDE完全關閉

        # ===== 步驟4: 刪除添加的欄位 =====
        print("\n【步驟4】使用 DeleteRobotRealtimeState() 刪除速度比例欄位...")
        rtn = DeleteRobotRealtimeState([
            RobotState.SpeedScaleManual,
            RobotState.SpeedScaleAuto,
        ])

        if rtn != 0:
            print(f"✗ 刪除欄位失敗，錯誤碼: {rtn}")
            return robot
        print("✓ 欄位刪除成功")

        # ===== 步驟5: 重新連接並驗證欄位值為 0 =====
        print(f"\n【步驟5】重新連接並驗證刪除後的欄位值...")

        robot = Robot.RPC(ROBOT_IP)
        time.sleep(0.5)

        # 讀取速度值
        pkg = robot.robot_state_pkg
        manual_speed = pkg.speedScaleManual
        auto_speed = pkg.speedScaleAuto

        print(f"\n  刪除後 SpeedScaleManual: {manual_speed:.2f}")
        print(f"  刪除後 SpeedScaleAuto: {auto_speed:.2f}")

        # 驗證是否為 0
        if manual_speed == 0 and auto_speed == 0:
            print("\n✓ Test2 驗證通過: 刪除欄位後速度值為 0")
        else:
            print(f"\n⚠ Test2 警告: 刪除欄位後速度值非零")

        print("\n✓ Test2 完成")
        return robot

    if __name__ == "__main__":
        test2_add_delete_state()