快速開始
=========================

.. toctree:: 
   :maxdepth: 6

我沒有FRCap
-------------

如果您目前還沒有FRCap，那麼可以在本小節快速建立FRCap。

首先，我們需要連接機器人並存取WebApp，在本機中開啟瀏覽器並輸入機器人預設IP位址（http://192.168.58.2）並登入進入WebApp。

.. image:: frcap_pictures/002.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-1  WebApp的「FRCap管理」頁面

在WebApp中依序點選「系統設定」->「FRCap管理」->「管理工具」後會在瀏覽器開啟一個新的標籤頁並存取「FRCap管理工具」。

.. image:: frcap_pictures/003.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-2  FRCap管理工具

在FRCap管理工具中選擇“建立精靈”，依序輸入或選擇以下外掛程式內容：

- 外掛名稱：Hello_FRCap。
- 外掛程式作者：admin。
- 外掛程式描述：Hello FRCap。
- 外掛程式類型：配置。

其中外掛圖示無需上傳，參數輸入或選擇完畢後，點選「建立」即可完成建立FRCap。

.. image:: frcap_pictures/004.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-3  FRCap建立精靈

建立成功後，跳到建立成功頁面並顯示目前已建立成功的FRCap名稱，點選「下載」即可將已建立好的FRCap下載到本機。

.. image:: frcap_pictures/005.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-4  下載Hello FRCap插件包

我已有FRCap
-------------
如果您已有FRCap專案資料夾，且符合FRCap專案結構，請直接閱讀\ `建構FRCap <frcap_quick_start.html#id3>`__\。

如果您已有檔案字尾名稱為「.frcap」的完整外掛程式包，請直接閱讀\ `Hello FRCap <frcap_quick_start.html#hello-frcap>`__\。

建構FRCap
-------------
開啟2.1章節下載的FRCap項目，或是您已有的FRCap項目。

根據目前使用的系統不同，先開啟build腳本，修改buildName參數,為你想要的名稱，然後儲存關閉，在終端機執行對應的腳本。

- Window中啟動終端，執行下列指令：

.. code-block:: c++
   :linenos:

   ./build.bat

- Linux中啟動終端，運行以下指令：
  
.. code-block:: c++
   :linenos:

   ./build.sh

建置完成後，在FRCap專案目錄下產生檔案名稱為FRCap名稱的，檔案後綴為「.frcap」的套件檔案。

.. image:: frcap_pictures/006.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-5  建置完成的FRCap包文件

Hello FRCap
-------------
FRCap專案建置完成後，在本機電腦中開啟瀏覽器並輸入機器人預設IP位址（http://192.168.58.2）並登入進入WebApp，依序點擊“系統設定”->“FRCap管理”->“匯入” 。選擇建置完成的「.frcap」字尾的FRCap包文件，開啟即可上傳。上傳成功後在下方的插件資訊清單中展示導入的FRCap資訊。

透過清單中的操作列控制FRCap啟用與否和刪除，在啟動停止狀態列查看FRCap的啟用狀態。

Hello FRCap啟用後可以在「輔助應用」->「FRCap」->「Hello FRCap」使用。此頁面承載配置類FRCap，可以全幅，也可以半幅，預設依照半幅展示。

至此，您已經完成了整個外掛程式快速建立和使用流程。

.. image:: frcap_pictures/007.png
   :width: 6in
   :align: center

.. centered:: 圖表 2-6  Hello FRCap内容

想要了解詳細的創建嚮導指導可以繼續查看\ `建立嚮導 <frcap_create.html#id1>`__\。

想要了解開發FRCap所需的工具環境和指導，請查看\ `開發指導 <frcap_development_guidance.html#id1>`__\。

想要了解FRCap在WebApp中具體的使用指導，請查看\ `WebApp中使用FRCap <frcap_use.html#webappfrcap>`__\。
