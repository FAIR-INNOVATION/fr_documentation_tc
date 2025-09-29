虛擬機-VMware
===============================================

概述
------------------
本手冊旨在介紹如何使用 FAIRINO SimMachine 虛擬機。

操作說明
------------------------------------

安裝 VMware Workstation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VMware Workstation 演示版本：17.6.3（已安裝則跳過此步）。

在瀏覽器直接搜尋VMware官網或直接點擊網址 \ `<https://www.vmware.com>`__\ ，下載安裝包後選擇預設路徑安裝即可。

.. image:: controller_virtual_machine/001.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-1 VMWare 界面

打開鏡像
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 下載虛擬機鏡像 FAIRINO_SimMachine.zip 並解壓
   
2. 打開 VMware，點擊 File->Open。如下圖 2-2 所示：

.. image:: controller_virtual_machine/002.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-2 打開鏡像

3. 找到解壓後的資料夾，選擇 vmx 後綴檔案。如下圖 2-3 所示：
   
.. image:: controller_virtual_machine/003.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-3 選擇檔案

4. 點擊「Power on this virtual machine」打開虛擬機。如下圖 2-4 所示：
   
.. image:: controller_virtual_machine/004.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-4 開啟虛擬機

5. 在解壓資料夾中找到「fr_get_vm_net」雙擊打開，如下圖 2-5 所示，輸出內容為虛擬機 IP。如下圖 2-6 所示。

.. note:: 如遇獲取失敗，請前往虛擬機中通過執行「ifconfig」命令獲取。
         
.. image:: controller_virtual_machine/005.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-5 fr_get_vm_net.bat
      
.. image:: controller_virtual_machine/006.png
   :width: 4in
   :align: center

.. centered:: 圖表 6.2-6 虛擬機 IP

Windows 訪問 WebApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 在得到虛擬機 IP 後，在 Windows 瀏覽器中直接訪問虛擬機 IP 即可進入 WebApp，如輸入：192.168.182.222，如圖 2-7：
         
.. image:: controller_virtual_machine/007.png
   :width: 6in
   :align: center

.. centered:: 圖表 6.2-7 通過虛擬機 IP 訪問 WebApp