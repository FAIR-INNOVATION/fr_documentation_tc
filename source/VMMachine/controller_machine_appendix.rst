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

7. docker 容器:

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

8. docker 容器:

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