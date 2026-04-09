CNDE功能操作
=====================

輸入配置與輸入數據
~~~~~~~~~~~~~~~~~~~~~~~~~

客戶端透過CNDE向機器人發送資料幀對機器人DO、AO輸出、輸入暫存器等進行控制，在發送輸入資料前，需要先配置需要控制的功能內容。表2-1為CNDE輸入設定內容格式，包含配方編號及一系列輸入設定功能名稱（表1-2）；對應的表3-2為輸入資料內容格式，包含配方編號及輸入資料位元組。

CNDE資料輸入支援最多8個配方，在發送輸入資料時，機器人將根據收到資料中的配方編號配對到對應的配方配置功能名稱組，並解析資料得到其中每個功能名稱的輸入資料值，進而根據輸入的資料進行機器人控制操作。

.. centered:: 表3-1 輸入配置內容格式

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **配方編號**
     - **功能名稱字符串**

   * - 長度(byte)
     - 1
     - --

   * - 内容
     - 0 ~ 7
     - 一系列輸入資料功能名稱

.. centered:: 表3-2 輸入數據內容格式

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **配方編號**
     - **資料位元組**

   * - 長度(byte)
     - 1
     - --

   * - 內容
     - 0 ~ 7
     - 輸入資料內容

輸入配置時，機器人控制器在收到配置名稱群組後會對每個名稱進行校驗，若所配置的功能名稱正確無誤，則機器人會回饋以「,」分割的所有配置功能的資料類型名稱；若配置的功能名稱有誤，機器人會回饋對應的錯誤內容。輸入配置資料幀(16進位)範例如下：

.. image:: cnde/001.png
   :width: 6in
   :align: center

其中配置輸入功能名稱組總長度為54個字節，加上輸入配方編號1個字節，共55個字節，轉成16進制為0x0037，在小端模式下，對應輸入資料幀中的數據長度即為「37 00」。

此時機器人將回饋一類型為字元提示訊息(本文3.3.1節字元提示訊息)的資料幀：

.. image:: cnde/002.png
   :width: 6in
   :align: center

訊息類型「00」表示這是一條執行成功的回饋訊息，客戶端可以提取「輸入資料配置類型」和表1-3對比，得到輸入配置的位元組長度，本範例中資料總長度為1*5 +4*30+8*30 = 365個位元組。

若輸入配置名稱有誤：

.. image:: cnde/003.png
   :width: 6in
   :align: center

其對應的回饋訊息為：

.. image:: cnde/004.png
   :width: 6in
   :align: center

輸入資料可以以一定的週期循環輸入，也可以只在有需要的時候輸入，循環輸入時機器人可以處理的最快週期為1ms，但較快的輸入週期會帶來一定的機器人系統資源開銷，建議您根據實際情況合理設定資料輸入週期。

另外向機器人發送資料幀時，機器人不會有回饋訊息，除非發送的資料幀長度或資料異常。輸入資料幀範例如下，其中輸入資料配方編號與輸入資料字節長度應該與輸入配置相符：

.. image:: cnde/005.png
   :width: 6in
   :align: center

輸出配置與輸出數據
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

客戶端透過CNDE獲取機器人狀態回饋可以根據需要自訂狀態回饋內容和回饋週期，使用機器人CNDE狀態回饋需要以下三個步驟：①輸出配置；②啟動輸出；③接收輸出資料。

輸出配置
+++++++++++++++++++++++

輸出配置幀內容包含輸出週期和輸出功能名稱組(所有可配置名稱見表1-1)，輸出週期可配置範圍為1 ~ 200ms，輸出資料位元組數最大支援4096byte。輸出功能名稱群組為一系列以「,」分隔的輸出功能名稱字串，客戶端發送輸出配置幀後，機器人會對配置的功能名稱進行校驗，若所配置的功能名稱均為當前機器人CNDE支持的功能名稱，則機器人回饋一系列「,」分隔的資料類型組合；否則若檢驗輸出配置名稱失敗，則回饋對應的錯誤訊息。

.. centered:: 表3-3 輸出配置內容

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **輸出週期(ms)**
     - **功能名稱字串**

   * - 長度(byte)
     - 2
     - --

   * - 内容
     - 1-200
     - 輸出功能名稱群組

如輸出配置幀如下：

.. image:: cnde/006.png
   :width: 6in
   :align: center

其中配置輸出功能名稱組總長度為48個字節，加上輸出週期2個字節，共50個字節，轉成16進制為0x0032，在小端模式下，對應輸入資料幀中的數據長度即為“32 00”。

此時機器人將回饋一類型為字元提示訊息(本文3.3.1節字元提示訊息)的資料幀：

.. image:: cnde/007.png
   :width: 6in
   :align: center

訊息類型「00」表示這是一條執行成功的回饋訊息，客戶端可以擷取「輸出資料配置類型」和表1-3對比，得到輸出配置的位元組長度，本範例中資料總長度為1+8*10+4 = 85個字節。

若輸入配置名稱有誤，如「queue」誤寫為「quene」：

.. image:: cnde/008.png
   :width: 6in
   :align: center

其對應的回饋訊息為：

.. image:: cnde/009.png
   :width: 6in
   :align: center

輸出啟動和停止
+++++++++++++++++++++++++

機器人CNDE輸出配置完成後，發送啟動CNDE輸出啟動指令，機器人即依照配置的輸出週期和輸出內容進行狀態回饋輸出，同樣發送CNDE停止輸出指令，機器人將停止狀態回授輸出。 CNDE啟動、停止指令沒有指令內容，對應資料長度為0。

.. centered:: 表3-4 CNDE輸出啟動、停止內容

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **資料位元組**

   * - 長度(byte)
     - 0

   * - 内容
     - 無

啟動機器人CNDE輸出資料幀範例如下：

.. image:: cnde/010.png
   :width: 3in
   :align: center

客戶端接收輸出數據
+++++++++++++++++++++++

機器人CNDE資料輸出啟動後，客戶端需要一個循環接收機器人回饋的資料訊息，且客戶端的循環接收頻率要高於配置的輸出資料頻率，否則可能會發生資料丟包。機器人輸出資料內容如表3-5；機器人輸出資料字節長度為輸出配置的所有功能資料位元組長度總和，位元組數組為1位元組對齊的按配置功能順序的所有狀態資料組合。

.. centered:: 表3-5 CNDE輸出資料內容

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **資料位元組**

   * - 長度(byte)
     - --

   * - 内容
     - 輸出資料字節

機器人輸出資料幀範例如下：

.. image:: cnde/011.png
   :width: 4in
   :align: center

CNDE輔助功能
~~~~~~~~~~~~~~~~~

字串提示訊息
++++++++++++++++++

客戶端和機器人之間可以透過CNDE相互發送字串提示訊息，訊息內容包括訊息類型和訊息字串(表3-6)，其中訊息類型定義如表3-7。當CNDE客戶端向機器人發送輸入配置、輸出配置、輸出啟動、輸出停止等指令時，機器人均回覆一則字元提示訊息。

若上述指令執行成功，則機器人回饋訊息類型為“成功”，對應訊息類型數值碼為0x00；反之若上述指令執行失敗，則機器人回饋訊息類型為“錯誤”，對應訊息類型數值為0x03，客戶端可根據回饋的訊息類型開判斷指令執行結果，若訊息類型為“錯誤”，則可以提取錯誤訊息以分析錯誤原因。

.. centered:: 表3-6 字串提示訊息內容

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **名稱**
     - **訊息類型**
     - **訊息字串**

   * - 長度(byte)
     - 1
     - --

   * - 内容
     - 0 ~ 4
     - 訊息字串

.. centered:: 表3-7 機器人CNDE字元提示訊息類型

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **類型**
     - **數值**

   * - 成功
     - 0x00

   * - 資訊
     - 0x01

   * - 警告
     - 0x02

   * - 錯誤
     - 0x03

   * - 故障
     - 0x04

切換機器人CNDE協議版本號
++++++++++++++++++++++++++++++++++++++

目前機器人CNDE僅有一個版本，版本編號為“FR-CNDE-V0001”，因此此功能為預留功能，暫未開放使用。

取得機器人軟韌體版本信息
+++++++++++++++++++++++++++++++++++++++++++++

客戶端透過CNDE向機器人發送獲取軟韌體版本資訊指令，指令內容為空，機器人收到請求後會回饋一條字元提示訊息，訊息內容包括機器人型號、機器人軟體版本、機器人韌體版本、機器人硬體版本等相關資訊.

末端透傳功能週期數據獲取（CNDE）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CNDE配置描述
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

末端透傳功能開啟後，可在CNDE中配置「axle_gen_com_data」選項及週期，從而獲取末端讀取的外設的週期數據，反饋的數據幀定義如下。

.. centered:: 表3-8  末端透傳功能週期數據CNDE反饋協議定義

.. list-table::
   :widths: 30 30 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Byte 1**
     - **Byte 2**
     - **Byte 3-130**

   * - ErrorCode
     - Len
     - Data

   * - 0-通訊正常
     - 週期數據的長度
     - 數據幀Buffer

   * - 1-末端與機器人通訊異常
     - 錯誤碼不為0時長度清零
     - 錯誤碼不為0時Buffer清零

   * - 2-末端485通訊異常	
     - 
     - 

以倍益康艾灸頭外設週期數據配置為例，代碼顯示配置為獲取末端週期透傳數據，獲取週期50ms。

末端透傳CNDE配置代碼示意:

.. code-block:: 
    :linenos:

    tring outputCfg = "axle_gen_com_data";    //獲取末端透傳週期數據
    byte[] sendBuffer = new byte[] { };
    byte[] cfgBuffer = Encoding.UTF8.GetBytes(outputCfg);
    CNDEPkg pkg  = new CNDEPkg();
    pkg.type = 1;  //輸出配置
    pkg.len = (ushort)(2 + outputCfg.Length);
    pkg.data.Clear();
    UInt16 period = 50;   //50ms update
    byte[] periodBt = new byte[2] {0, 0};
    Int16ToByte(period, ref periodBt);
    pkg.data.AddRange(periodBt);  //通訊週期
    pkg.data.AddRange(cfgBuffer); 
    pkg.ToBytes(ref sendBuffer);

基於CNDE的倍益康艾灸頭週期數據解包代碼示例:
  
.. code-block:: 
    :linenos:

    if (pkg.type == 4)
    {
        int size = Marshal.SizeOf(putDate);
        IntPtr structPtr = Marshal.AllocHGlobal(size);
        Marshal.Copy(pkg.data.ToArray(), 0, structPtr, size);
        putDate = (OUTPKG)Marshal.PtrToStructure(structPtr, typeof(OUTPKG));

        int errorcode = putDate.axle_gen_com_data[0];
        int datalen = putDate.axle_gen_com_data[1];
        // 過濾異常包
        if ((errorcode != 0) || (datalen == 0) ||
        (putDate.axle_gen_com_data[2] != 0xAB) || 
        (putDate.axle_gen_com_data[3] != 0xBA))
        {
            Console.WriteLine($"rcv data is error");
            continue;
        }
        // 按照倍益康艾灸頭協議進行組包
        int curTem = putDate.axle_gen_com_data[6];
        int targetTem = putDate.axle_gen_com_data[7];
        int genData1 = putDate.axle_gen_com_data[8] << 8 | putDate.axle_gen_com_data[9];
        int genData2 = putDate.axle_gen_com_data[10] << 8 | putDate.axle_gen_com_data[11];
        int genData3 = putDate.axle_gen_com_data[12] << 8 | putDate.axle_gen_com_data[13];
        int genData4 = putDate.axle_gen_com_data[14] << 8 | putDate.axle_gen_com_data[15];
        int genData5 = putDate.axle_gen_com_data[16] << 8 | putDate.axle_gen_com_data[17];
        int genData6 = putDate.axle_gen_com_data[18] << 8 | putDate.axle_gen_com_data[19];

        Console.WriteLine($"the data is errorcode {errorcode};  datalen  {datalen}  curTem  {curTem}; targetTem  {targetTem}  genData1  {genData1}  genData2  {genData2}  genData3  {genData3}  genData4  {genData4}  genData5  {genData5}  genData6  {genData6}  ");
        udpClient.Client.ReceiveTimeout = 100;
        Marshal.FreeHGlobal(structPtr);
    }

基於末端透傳功能倍益康艾灸頭非週期數據通訊代碼示例:
  
.. code-block:: 
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

        int[] rcvdata = new int[16];
        int ret = 0;
        int cnt = 1;

        JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
        DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

        JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
        DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        //開啟末端透傳功能
        robot.SetAxleGenComEnable(1);
        robot.SetAxleLuaEnable(1);

        while(cnt<=10)
        { 
            //讀取版本號
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            //讀取艾灸頭在位狀態
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            //開啟艾灸頭激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            //關閉艾灸頭激光
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }