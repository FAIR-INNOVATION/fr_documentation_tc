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
    虛擬機器設定 -> 系統 -> 處理器，預設啟用 PAE/NX，如果電腦BIOS尚未啟用虛擬化，會導致啟動失敗，需在 BIOS 中開啟虛擬化，詳見 \ `附录1 <#bios>`__\。

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
   如目前沒有測試電腦，可在本機電腦上新增虛擬網路卡（環回網路介面卡），詳見\ `附錄2 <#id4>`__\。

虛擬機-Docker
===================================

Linux部署docker映像
---------------------------

操作環境
~~~~~~~~~~~~~~

虛擬機器運作環境系統：Ubuntu 18.04.6；

虛擬機器運作環境系統：RAM 4G，ROM 50G，6核CPU ；

操作權限：使用超級管理員root權限，設定方法見附錄3；

docker安裝檔：fr_docker.tar.gz；

FAIRINO SimMachine鏡像：FAIRINOSimMachine.tar；

安裝docker
~~~~~~~~~~~~~~

若使用者已安裝部署docker，則跳過此節，進行1.3映像部署。

1.下載fr_docker.tar.gz，放至Ubuntu檔案路徑/opt/。

2.解壓縮fr_docker.tar.gz.，以/opt/目錄下為例：

.. code-block:: console
   :linenos:

   cd /opt/ && tar -zxvf fr_docker.tar.gz

.. image:: controller_virtual_machine/036.png
   :width: 6in
   :align: center

3.執行安裝docker腳本：

.. code-block:: console
   :linenos:

   sh install.sh docker-27.0.3.tgz

待腳本執行完畢後，出現版本號，表示安裝成功。

.. image:: controller_virtual_machine/037.png
   :width: 6in
   :align: center

鏡像配置
~~~~~~~~~~~~~~

導入docker映像
++++++++++++++++++++

1. 下載虛擬機器鏡像FAIRINOSimMachine.tar並解壓縮。

2. 查看docker版本確認已安裝。

.. code-block:: console
   :linenos:

   docker -v

.. image:: controller_virtual_machine/038.png
   :width: 6in
   :align: center   

3. 導入鏡像   

.. code-block:: console
   :linenos:

   docker load -i ./FAIRINOSimMachine.tar

出現fairno_simmachine:latest則表示匯入完成。

.. image:: controller_virtual_machine/039.png
   :width: 6in
   :align: center  

4. 執行docker images查看是否匯入成功。

建立自訂橋接網絡
++++++++++++++++++++

1. 執行以下指令，建立名為fairino-net，網段為192.168.58.0/24的橋接網路。

.. code-block:: console
   :linenos:

   docker network create --driver bridge --subnet 192.168.58.0/24 --gateway 192.168.58.1 fairino-net

2. 查看網路

.. code-block:: console
   :linenos:

   docker network ls

存在fairino-net網路表示創建成功。

.. image:: controller_virtual_machine/040.png
   :width: 6in
   :align: center 

首次啟動docker容器
++++++++++++++++++++

1. 建立容器並啟動

使用fairino-net網絡，fairino_simmachine鏡像啟動容器。

.. code-block:: console
   :linenos:

   docker run -d -P --name fairino-container --privileged -u root --net fairino-net fairino_simmachine

.. image:: controller_virtual_machine/041.png
   :width: 6in
   :align: center 

.. code-block:: console
   :linenos:

   docker ps 

查看容器是否成功啟動，出現fairino-container則表示啟動成功。

.. image:: controller_virtual_machine/042.png
   :width: 6in
   :align: center 

web操作虛擬機器人
----------------------------

容器正常啟動
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

此小節針對非首次啟動容器，因重新啟動電腦或docker關閉等原因容器未在背景運作狀況。

1. 啟動docker：

.. code-block:: console
   :linenos:

   systemctl start docker

2. 查看docker狀態：

.. code-block:: console
   :linenos:

   systemctl status docker
   
綠色active(running)表示啟動成功。

.. image:: controller_virtual_machine/043.png
   :width: 6in
   :align: center 

3. 執行docker ps -a查看容器ID。

.. image:: controller_virtual_machine/044.png
   :width: 6in
   :align: center 

4. 執行 docker start [容器ID]。

.. image:: controller_virtual_machine/045.png
   :width: 6in
   :align: center 

5. 執行成功，再次docker ps 查看容器正在運作。

.. image:: controller_virtual_machine/046.png
   :width: 6in
   :align: center 

操作虛擬機器人
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 確認docker容器正在運作。

.. code-block:: console
   :linenos:

   docker ps 

出現fairino-container則表示正在運作。

.. image:: controller_virtual_machine/047.png
   :width: 6in
   :align: center 

2. 開啟瀏覽器，輸入預設IP：192.168.58.2，即可存取web介面，操作虛擬機器人。

.. image:: controller_virtual_machine/048.png
   :width: 6in
   :align: center 

3. 使用admin帳號登錄，密碼：123。

.. image:: controller_virtual_machine/049.png
   :width: 6in
   :align: center 

用戶修改IP位址
~~~~~~~~~~~~~~~~~~~~~~

.. image:: controller_virtual_machine/050.png
   :width: 6in
   :align: center 

1. 開啟瀏覽器，輸入預設 IP： 192.168.58.2，開啟 web 頁面；
2. 使用 admin 帳號登錄，密碼： 123；
3. 進入“系統設定” → “通用設定” → “網路設定”， 修改 IP 為目標 IP 位址、遮罩、閘道。點選「設定網路」；

以修改IP為192.168.56.2/24為例。

.. image:: controller_virtual_machine/051.png
   :width: 6in
   :align: center 

4. 打開終端，關閉容器；

查看容器ID：

.. code-block:: console
   :linenos:
      
   docker ps -a

.. image:: controller_virtual_machine/052.png
   :width: 6in
   :align: center 

關閉容器：

.. code-block:: console
   :linenos:
   
   docker stop [容器ID]

.. image:: controller_virtual_machine/053.png
   :width: 6in
   :align: center 

5. 重新配置容器網路；

刪除原先網路：

.. code-block:: console
   :linenos:
   
   docker network rm fairino-net

建立新網路：

.. code-block:: console
   :linenos:
   
   docker network create --driver bridge --subnet [目標IP/子网掩码] --gateway [网關IP] fairino-net

以192.168.56.0/24為例：docker network create --driver bridge --subnet 192.168.56.0/24 --gateway 192.168.56.1 fairino-net

.. image:: controller_virtual_machine/054.png
   :width: 6in
   :align: center 

6. 將容器重新連接到新建立的網路；

.. code-block:: console
   :linenos:

   docker network connect fairino-net [容器ID]

.. image:: controller_virtual_machine/055.png
   :width: 6in
   :align: center 

7. 重新啟動容器；

.. code-block:: console
   :linenos:
   
   docker start [容器ID]

8. 此時開啟瀏覽器， 輸入修改後 IP 位址，即可存取 web 介面，操作虛擬機器人。

.. image:: controller_virtual_machine/056.png
   :width: 6in
   :align: center 

附錄
=====================

附錄1：BIOS 中啟用虛擬化
-------------------------

不同型號的電腦啟用虛擬化的流程可能不同，現在以聯想ThinkPad系列windows10舉例：

- 開啟電腦設置，選擇更新和安全性。

.. image:: controller_virtual_machine/013.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/014.png
   :width: 4in
   :align: center

- 選擇“恢復”。

.. image:: controller_virtual_machine/015.png
   :width: 4in
   :align: center

- 選擇“立即重新啟動”。

.. image:: controller_virtual_machine/016.png
   :width: 4in
   :align: center

- 選擇“疑難解答”。
  
.. image:: controller_virtual_machine/017.png
   :width: 4in
   :align: center

- 選擇“高級選項”。

.. image:: controller_virtual_machine/018.png
   :width: 4in
   :align: center

- 選擇UEFI韌體設定。

.. image:: controller_virtual_machine/019.png
   :width: 4in
   :align: center

- 選擇「重啟」。

.. image:: controller_virtual_machine/020.png
   :width: 4in
   :align: center

- 選擇「Security」下的「Virtualization」。

.. image:: controller_virtual_machine/021.png
   :width: 4in
   :align: center

- 選擇“Enabled”，按下“Enter”確認。

.. image:: controller_virtual_machine/022.png
   :width: 4in
   :align: center

- 按下“F10”，選擇“Yes”，按下“Enter”儲存修改。

.. image:: controller_virtual_machine/023.png
   :width: 4in
   :align: center

附錄2：新增虛擬網路卡（環回網路介面卡）
-----------------------------------------

1. 開啟裝置管理員，按下“Windows鍵-X”，選擇“裝置管理員”。
   
.. image:: controller_virtual_machine/024.png
   :width: 4in
   :align: center

2. 新增網路適配器。

.. image:: controller_virtual_machine/025.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/026.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/027.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/028.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/029.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/030.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/031.png
   :width: 4in
   :align: center
   
3. 檢視虛擬網路卡，按下“Windows鍵-X”，選擇“網路連線”。

.. image:: controller_virtual_machine/032.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/033.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/034.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/035.png
   :width: 4in
   :align: center
   
4. 設定環回適配器網路。

- IP位址: 192.168.58.XXX（與192.168.58.2 同一網段即可）。
- 子網路遮罩：255.255.255.0。

.. image:: controller_virtual_machine/012.png
   :width: 6in
   :align: center

5. 開啟Virtualbox網路配置，網路卡名稱選擇“環回適配器網路”，啟動虛擬機器即可。

.. image:: controller_virtual_machine/013.png
   :width: 6in
   :align: center

附錄3：root權限
--------------------------------------

Ubuntu安裝好後，Ubuntu系統預設root使用者是不能登入的，密碼也是空的。如果想要使用root使用者登入，必須先為root使用者設定密碼。

1. 開啟終端，輸入 sudo passwd root ，然後回車輸入幾次密碼，顯示密碼設定成功。

.. image:: controller_virtual_machine/057.png
   :width: 6in
   :align: center

2. 在終端機繼續輸入 su - root 指令切換用戶，回車輸入密碼。

.. warning:: 輸入指令時一定要輸入“-”，選項“-”表示連帶環境變數一起切換，“-”堅決不能少。

.. image:: controller_virtual_machine/058.png
   :width: 6in
   :align: center

附錄4：docker基礎命令
--------------------------------------

1. docker 幫助命令 :

.. code-block:: console
   :linenos:

   docker --help

2. 啟動docker :

.. code-block:: console
   :linenos:

   systemctl start docker

3. 關閉docker :

.. code-block:: console
   :linenos:

   systemctl stop docker

4. 重啟docker :

.. code-block:: console
   :linenos:

   systemctl restart docker

5. docker設定隨服務啟動而自啟動 :

.. code-block:: console
   :linenos:

   systemctl enable docker

6. 查看docker 運行狀態 :

.. code-block:: console
   :linenos:

   systemctl status docker
   --如果是在執行中輸入指令後會看到綠色的active

7. docker映像相關 :

.. code-block:: console
   :linenos:

   docker images：列出已經下載的映像，檢視鏡像
   docker rmi 映像id或name：刪除本機映像
   docker rmi -f 映像id或name: 刪除映像
   docker build：建置映像
   docker search 映像id或name：在Docker Hub倉庫中搜尋關鍵字映像
   docker pull 映像id或name：從倉庫下載映像
   docker images：列出已經下載的映像，檢視鏡像
   docker rmi 映像id或name：刪除本機映像
   docker rmi -f 映像id或name: 刪除映像
   docker build：建置映像

8. docker鏡像相關 :

.. code-block:: console
   :linenos:

   docker ps：列出運行中的容器
   docker ps -a ： 查看所有容器，包括未運行
   docker stop 容器id或name：停止容器
   docker kill 容器id：強制停止容器
   docker start 容器id或name：啟動已停止的容器
   docker inspect 容器id：查看容器的所有信息
   docker container logs 容器id：查看容器日誌
   docker top 容器id：查看容器裡的進程
   docker exec -it 容器id /bin/bash：進入容器
   exit：退出容器
   docker rm 容器id或name：刪除已停止的容器
   docker rm -f 容器id：刪除正在執行的容器
   docker exec -it 容器ID sh :進入容器