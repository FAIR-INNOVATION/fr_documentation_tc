WebApp 訪問登入
===================

.. toctree:: 
   :maxdepth: 6

訪問登入WebApp界面
--------------------

1. 開啟控制箱並將網線連接PC；
2. PC打開chrome瀏覽器訪問目標網址192.168.58.2；
3. 輸入用戶名和密碼點擊登入即可登入WebApp。

初始用戶名為admin，密碼為123。

.. figure:: teaching_pendant_software/001.png
   :width: 6in
   :align: center

.. centered:: 圖表 2.1‑1 登入界面

簡單認識WebApp界面
--------------------

登入成功後系統進入“初始界面”，主要包含：

1. 法奧LOGO；
2. 選單欄縮放按鈕；
3. 選單欄；
4. 機器人控制區
5. 機器人狀態區；
6. 三維模擬機器人——三維場景操作；
7. 三維模擬機器人——機器人本體操作；
8. 機器人配套功能；
9. 機器人及配套功能狀態。

如下圖系統初始界面示意圖所示：

.. image:: teaching_pendant_software/002.png
   :align: center
   :width: 6in

.. centered:: 圖表 2.2‑1 系統初始界面示意圖

控制區
~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/064.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**開啟教導程式按鈕**
   
   作用：開啟程式編程、圖形化編程和節點圖編程的教導程式

.. note:: 
   .. image:: teaching_pendant_software/003.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**使能按鈕**
   
   作用：使能機器人

.. note:: 
   .. image:: teaching_pendant_software/004.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**開始按鈕**
   
   作用：上傳並開始執行教導程式

.. note:: 
   .. image:: teaching_pendant_software/005.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**停止按鈕**
   
   作用：停止目前教導程式執行

.. note:: 
   .. image:: teaching_pendant_software/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**暫停/恢復按鈕**
   
   作用：暫停和恢復目前教導程式

.. important::
   暫停指令在程式的末尾，無法進行判斷

狀態欄
~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人狀態**
   
   作用：Stopped-停止，Running-執行，Pause-暫停，Drag-拖動

.. note:: 
   .. image:: teaching_pendant_software/009.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**執行速度百分比**
   
   作用：機器人目前模式執行時速度

.. note:: 
   .. image:: teaching_pendant_software/012.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**自動模式**
   
   作用：機器人自動執行模式，開啟手動切自動模式全域速度調整並指定速度時，全域速度會自動調整為指定速度

.. note:: 
   .. image:: teaching_pendant_software/013.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**手動模式**
   
   作用：機器人手動模式，進行機器人教導操作

.. note:: 
   .. image:: teaching_pendant_software/010.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人執行正常狀態**
   
   作用：目前機器人正常執行

.. note:: 
   .. image:: teaching_pendant_software/011.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人執行錯誤狀態**
   
   作用：目前機器人執行有錯誤

.. note:: 
   .. image:: teaching_pendant_software/065.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人狀態折疊/展開按鈕**
   
   作用：折疊/展開工具座標系、工件座標系、擴展軸座標系、負載、機器人拖動狀態、本地/遠端模式、機器人連接狀態、BOOT模式和帳戶資訊內容

.. note:: 
   .. image:: teaching_pendant_software/008.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**工具座標系編號**
   
   作用：展示目前應用的工具座標系編號

.. note:: 
   .. image:: teaching_pendant_software/027.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**工件座標系編號**
   
   作用：展示目前應用的工件座標系編號

.. note:: 
   .. image:: teaching_pendant_software/028.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**擴展軸座標系編號**
   
   作用：展示目前應用的擴展軸座標系編號

.. note:: 
   .. image:: teaching_pendant_software/066.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**負載**
   
   作用：展示目前應用的負載重量和質心座標X、Y、Z

.. note:: 
   .. image:: teaching_pendant_software/014.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人拖動狀態**
   
   作用：目前機器人可拖動

.. note:: 
   .. image:: teaching_pendant_software/015.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人拖動狀態**
   
   作用：目前機器人不可拖動

.. note:: 
   .. image:: teaching_pendant_software/068.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人本地模式**
   
   作用：目前機器人透過控制箱控制

.. note:: 
   .. image:: teaching_pendant_software/067.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**機器人遠端模式**
   
   作用：目前機器人只能透過PLC控制

.. note:: 
   .. image:: teaching_pendant_software/017.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**連接狀態**
   
   作用：機器人已連接

.. note:: 
   .. image:: teaching_pendant_software/016.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**未連接狀態**
   
   作用：機器人未連接

.. note:: 
   .. image:: teaching_pendant_software/018.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   名稱：**帳戶資訊**
   
   作用：顯示用戶名和權限及登出用戶
