虛擬機器-Virtual Box
=====================

虛擬機器環境配置
------------------

安裝Virtual Box
~~~~~~~~~~~~~~~~~~~~

- Virtual Box版本：VirtualBox-7.0.14。
- 檔案名稱：VirtualBox-7.0.14-161095-Win.exe。
- 下載安裝套件後選擇預設路徑安裝即可。

.. image:: controller_virtual_machine/001.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-1 VirtualBox 7.0.14

镜像配置
~~~~~~~~~~~

1) 下載並開啟鏡像。

- 下載虛擬機器鏡像FAIRINO SimMachine.rar並解壓縮。
- 開啟VirtualBox，選擇“註冊”，選擇虛擬機器“FAIRINO SimMachine.vbox”文件，即可匯入虛擬環境。

.. image:: controller_virtual_machine/002.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-2 VirtualBox 中選擇注册

.. image:: controller_virtual_machine/003.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-3 選擇虚拟机文件

- 匯入後，選擇“FAIRINO SimMachine”，點選“啟動”按鈕，開啟虛擬機器。

.. image:: controller_virtual_machine/004.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-4 启動虚拟机

.. note:: 
    虛擬機器設定 -> 系統 -> 處理器，預設啟用 PAE/NX，如果電腦BIOS尚未啟用虛擬化，會導致啟動失敗，需在 BIOS 中開啟虛擬化，詳見附錄1。

2) 共享資料夾。

虛擬機器和宿主機器之間的共用資料夾已經預設設定好，建議拷貝檔案時都使用共用資料夾進行拷貝。同時虛擬機器環境已經安裝增強功能，共用貼上板，方便複製貼上。

- 宿主機共用資料夾在 D:\share（需要手動建立share資料夾）。
- 虛擬機器共用資料夾在 /home/fr/shared。

.. image:: controller_virtual_machine/005.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-5 共享資料夾配置

3) 進入虛擬機器系統。

- 虛擬機器運作環境系統：Ubuntu 18.04.6。
- 虛擬機器運作環境系統：RAM 4G，ROM 50G，6核CPU 。
- 使用者名稱：root，密碼：123。

.. image:: controller_virtual_machine/007.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.1-6 tty登入虛擬機器系統

虛擬機器系統預設關閉使用者圖形介面，使用tty登入。

- 如果使用者需要開啟使用者圖形介面：
  
.. list-table::
   :widths: 200
   :align: center

   * - systemctl set-default graphical.target

   * - reboot
  
- 如果使用者需要再次關閉使用者圖形介面：
  
.. list-table::
   :widths: 200
   :align: center

   * - systemctl set-default multi-user.target

   * - reboot

使用者登入web頁面，操作虛擬機器人
-----------------------------------

- 首次登錄，用戶準備一台測試電腦，透過網路線連接到虛擬機，測試電腦網路埠IP設定為192.168.58.XXX 網段，子網路遮罩設定為255.255.255.0。
- 在測試電腦上，開啟 Chrome 瀏覽器，輸入預設IP：192.168.58.2，即可存取web介面，操作虛擬機器人。

.. image:: controller_virtual_machine/008.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-1 虛擬機器web登入介面

.. image:: controller_virtual_machine/009.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-2 虛擬機器web操作介面

用戶修改IP位址
~~~~~~~~~~~~~~~~~~~~~~

.. image:: controller_virtual_machine/010.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-3 設定網路頁面

1. 開啟瀏覽器，輸入預設IP：192.168.58.2，開啟web頁面；
2. 使用admin帳號登錄，密碼：123；
3. 進入“系統設定” -> “一般設定” -> “網路設定”，修改 IP為目標IP位址，點選“設定網路”；
4. 重新啟動虛擬機，虛擬機橋接網路卡上 IP 已經自動變更為修改後的 IP位址；
5. 設定本機測試電腦乙太網路埠、宿主機乙太網路埠與虛擬機橋接網卡上 IP為同一網段；
6. 此時使用者在測試電腦上，開啟 Chrome 瀏覽器，輸入修改後IP位址，即可存取web介面，操作虛擬機器人。

.. image:: controller_virtual_machine/011.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-4 網路拓撲圖

.. note:: 
   如目前沒有測試電腦，可在本機電腦上新增虛擬網路卡（環回網路介面卡），詳見附錄2。

