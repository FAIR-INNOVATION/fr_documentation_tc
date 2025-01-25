API說明
=========================

.. toctree:: 
   :maxdepth: 6

act 指令
-------------

以下所有act指令使用POST，URL為/action/act。

保存示教點
+++++++++++++

指令名稱：save_point。

指令參數：

.. code-block:: c++
    :linenos:

    /** 
    * @param  string name記錄的示教點名稱
    * @param  string speed 速度
    * @param  string elbow_speed 肘速度
    * @param  string acc加速度
    * @param  string elbow_acc 肘加速度
    * @param  string toolnum 工具號
    * @param  string workpiecenum 工件號
    */ 

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "save_point",
        data:{
            name: "point1",
            speed: "100",
            elbow_speed: "100",
            acc: "100",
            elbow_acc: "100",
            toolnum: "1",
            workpiecenum: "1"
        }
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @return status:404 "fail"
    */ 

sta 指令
-------------

以下所有sta指令使用POST，URL為/action/sta。

取得機器人狀態數據
++++++++++++++++++++

指示名稱：basic。

指令參數：無。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "basic",
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 
    * @param  object joints 關節位置
    * @param  object tcp 笛卡兒位姿
    * @param  array exAxisPos 外部軸位置
    * @return status:404 "fail"
    */
    {
        joints: {
            j1: "90",
            j2: "90",
            j3: "90",
            j4: "90",
            j5: "90",
            j6: "90",
        },
        tcp: {
            x: "100",
            x: "100",
            z: "100",
            rx: "90",
            ry: "90",
            rz: "90",
        },
        exAxisPos: [0,0,0,0]
    }

get 指令
-------------

以下所有get指令使用POST，URL為/action/get。

取得示教點
+++++++++++++

指令名稱：get_points()。

指令參數：無。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "get_points"
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  ${point_name}: object 示教點相關資訊
    * @return status:404 "fail"
    */ 

指令回饋案例：

.. code-block:: c++
    :linenos:

    {
        "localpoint1": {
            "name":"localpoint1",
            "elbow_speed":"1",
            "elbow_acc":"1",
            "x": "1",
            "y": "1",
            "z": "1",
            "rx": "1",
            "ry": "1",
            "rz": "1",
            "j1": "1",
            "j2": "1",
            "j3": "1",
            "j4": "1",
            "j5": "1",
            "j6": "1",
            "toolnum": "1",
            "workpiecenum": "1",
            "speed": "1",
            "acc": "1",
            "E1": "1",
            "E2: "1",
            "E3": "1",
            "E4": "1"
        }
    }

取得系統配置
+++++++++++++

指令名稱：get_syscfg()。

指令參數：無。

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: "get_syscfg"
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  string log_count 記錄最大日誌天數
    * @param  string language 目前使用語言包
    * @param  string lifespan 超時時間
    * * @return status:404 "fail"
    */ 

指令回饋案例：

.. code-block:: c++
    :linenos:

    {
        log_count:"10",
        language:"zh",
        lifespan:"1800"
    }

set 指令
-------------

以下所有set指令使用POST，URL為/action/set。

下發系統變數指令
++++++++++++++++++

指令名稱：511。

指令參數：

.. code-block:: c++
    :linenos:

    /** 
    * @param int index系統變數序號:1-20 
    * @param int value系統變數值 
    */ 

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: 511,
        data:{
            content:"SetSysVarValue(2,1)"
        }
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:2001：代表成功，0：代表失敗
    * @return status:404 "fail"
    */

指令回饋案例：

.. code-block:: c++
    :linenos:

    1

取得系統變數指令
+++++++++++++++++++

指令名稱：512。

指令參數：

.. code-block:: c++
    :linenos:

    /** 
    * @param int index系統變數序號:1-20 
    * /

指令案例：

.. code-block:: c++
    :linenos:

    {
        cmd: 512,
        data:{
            content:"GetSysVarValue(2)"
        }
    }

指令回饋：

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200
    * @param int value系統變數值 
    * @return status:404 "fail"
    * /

指令回饋案例：

.. code-block:: c++
    :linenos:

    1

better-sqlite3指令
-----------------------

查詢資料庫中第一行記錄
++++++++++++++++++++++

指令參數：

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 資料庫名稱(包含絕對路徑)
    * @param string sql sql語句
    * @return string result 查詢到的第一行記錄
    */

指令内容：

.. code-block:: c++
    :linenos:

    queryget(string db_name, string sql);

查詢資料庫中所有記錄
+++++++++++++++++++++

指令參數：

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 資料庫名稱(包含絕對路徑)
    * @param string sql sql語句
    * @return string result 查詢到的所有記錄
    */

指令内容：

.. code-block:: c++
    :linenos:

    queryall(string db_name, string sql);

執行資料庫語句
+++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name 資料庫名稱(包含絕對路徑)
    * @param string sql sql語句
    * @param object obj sql 語句執行所需的參數
    * @return \
    */

指令參數：

.. code-block:: c++
    :linenos:

    exec(string db_name, string sql, object obj);

指令内容：

socket指令
-----------------------

socket send
++++++++++++++++++++++

指令參數：

.. code-block:: c++
    :linenos:

    /**
    * @param string send_content socket 通訊指令發送內容
    * @return \
    */

指令内容：

.. code-block:: c++
    :linenos:

    socket_cmd.send(string send_content);//8065
    socket_file.send(string send_content);//8067

socket recv
+++++++++++++++++++++

指令參數：

.. code-block:: c++
    :linenos:

    /**
    * @return string recv_content socket 通訊指令回覆內容
    */

指令内容：

.. code-block:: c++
    :linenos:

    socket_cmd.recv();//8065
    socket_file.recv();//8067