CNDE資料幀協議格式
===========================

協作機器人CNDE通訊協議如下，客戶端向機器人發送資料及機器人向客戶端回饋資料均需遵循此協定；協定透過幀類型區分不同功能的資料幀，幀類型定義見表2-2；不同類型幀對應不用的資料內容，具體資料內容定義見表3-1 ~ 表3-7。

.. centered:: 表2-1 機器人CNDE資料幀格式

.. list-table::
   :widths: 20 20 20 20 20 20 20
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **幀頭**
     - **幀計數**
     - **幀類型**
     - **資料長度**
     - **內容**
     - **幀尾**
   
   * - **長度(byte)**
     - 2
     - 1
     - 1
     - 2
     - --
     - 2
   
   * - **内容**
     - 0x5A5A
     - 0 ~ 255
     - 0 ~ 8
     - “數據內容”的位元組個數
     - 資料幀內容
     - 0xA5A5

.. centered:: 表2-2 機器人CNDE資料幀類型

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **類型**
     - **數值**
     - **資料幀方向**

   * - 輸入配置幀（控製配置）
     - 0x00
     - Client->Robot

   * - 輸出配置幀（狀態配置）
     - 0x01
     - Client->Robot

   * - CNDE輸出啟動
     - 0x02
     - Client->Robot

   * - CNDE輸出停止
     - 0x03
     - Client->Robot

   * - 輸出資料幀（狀態資料）
     - 0x04
     - Robot->Client

   * - 輸入資料幀（控制資料）
     - 0x05
     - Client->Robot

   * - 字元提示訊息
     - 0x06
     - Client->Robot, Robot->Client

   * - 設定機器人CNDE協議版本號
     - 0x07
     - Client->Robot

   * - 取得機器人軟韌體版本
     - 0x08
     - Client->Robot, Robot->Client