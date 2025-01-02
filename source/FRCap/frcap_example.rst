FRCap案例
=========================

.. toctree:: 
   :maxdepth: 6

FAIRINO Palletizer（码垛机）
-----------------------------

请访问以下地址获取源代码和码垛FRCap包：\ `FAIR-INNOVATION/frcap_palletizer <https://gitee.com/fair-innovation/frcap_palletizer>`__\。

或者直接在本地克隆：

.. code-block:: c++
   :linenos:

   git clone https://gitee.com/fair-innovation/frcap_palletizer.git

将项目中的build文件夹下的“码垛机Palletizer.frcap”在WebApp中上传注册启用后即可使用。

.. image:: frcap_pictures/011.png
   :width: 6in
   :align: center

.. centered:: 图表 7.1 码垛FRCap使用

码垛工件配置
+++++++++++++++

指令名称：palletizing_config_box。 

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  int length 工件长度
   * @param  int width 工件速度
   * @param  int height 工件高度
   * @param  int payload 工件负载
   * @param  string grip_point工件抓取点
   * /

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "palletizing_config_box",
      data: {
         length: 800,
         width: 615,
         height: 312,
         payload: 2.34,
         grip_point: "grippoint"
      }
   } 

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */

码垛托盘配置
+++++++++++++++

指令名称：palletizing_config_pallet。

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  int front 托盘前边
   * @param  int side 托盘侧边
   * @param  int height 托盘高度
   * @param  int left_pallet 左托盘启用
   * @param  int right_pallet 右托盘启用
   */

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "palletizing_config_pallet",
      data: {
            front: 1200,
            side: 1000,
            height: 110,
            left_pallet: 0,
            right_pallet: 1
         }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */ 

码垛高级配置
+++++++++++++++

指令名称：palletizing_advanced_cfg。

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  string height 码垛抓取点抬升高度
   * @param  string x1 码垛渐进点1：x 方向偏移,单位mm
   * @param  string y1 码垛渐进点1：y 方向偏移,单位mm
   * @param  string z1 码垛渐进点1：z 方向偏移,单位mm
   * @param  string x2 码垛渐进点2：x 方向偏移,单位mm
   * @param  string y2 码垛渐进点2：y 方向偏移,单位mm
   * @param  string z2 码垛渐进点2：z 方向偏移,单位mm
   * @param  string time 吸料等待时间,单位 ms
   */ 

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "palletizing_advanced_cfg",
      data: {
      height: "1000",
            x1: "100",
            y1: "100",
            z1: "100",
            x2: "10",
            y2: "10",
            z2: "10",
            time: "1"
         }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */

码垛设备尺寸配置
+++++++++++++++++

指令名称：palletizing_config_device。

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  int x 左托盘右上角点相对于机器人基座标系坐标轴的x方向绝对值
   * @param  int y 左托盘右上角点相对于机器人基座标系坐标轴的y方向绝对值
   * @param  int z 左托盘右上角点相对于机器人基座标系坐标轴的z方向绝对值
   * @param  int angle 机器人安装时的旋转角度
   */ 

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "palletizing_config_device",
      data: {
         x: 2400,
         y: 1800,
         z: 120,
         angle: 0   
      }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */

码垛模式配置
+++++++++++++++

指令名称：palletizing_config_pattern。

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  int layers 码垛层数
   * @param  int box_gap 工件像素点间隔，单位：mm
   * @param  string sequence 码垛工作模式
   * @param  int pattern_b_enable 模式b是否开启，1：开启，0：不开启
   * @param  string left_pattern_a 左工位模式a笛卡尔坐标
   * @param  string left_pattern_b 左工位模式b笛卡尔坐标
   * @param  string right_pattern_a 右工位模式a笛卡尔坐标
   * @param  string right_pattern_b 右工位模式b笛卡尔坐标
   * @param  string origin_pattern_a 初始模式a笛卡尔坐标
   * @param  string origin_pattern_b 初始模式b笛卡尔坐标
   */

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "palletizing_config_pattern",
      data: {
         layers: 8,
         box_gap: 0,
         sequence: "a,b,a,b,a,b,a,b",
         pattern_b_enable: 1,
         left_pattern_a: "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
         "left_pattern_b": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
         "right_pattern_a": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
         "right_pattern_b": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
         "origin_pattern_a": "[]",
         "origin_pattern_b": "[]"
      }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */

码垛程序生成
+++++++++++++++

指令名称：generate_palletizing_program。

指令参数：

.. code-block:: c++
   :linenos:

   /**
   * @param  string palletizing_name 码垛名称
   * @param  string depalletizing_name 拆垛名称
   * @param  string flag 码垛或者拆垛程序是否生成，0-不生成，1生成
   */ 

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "generate_palletizing_program",
      data: {
         palletizing_name: "palletizing_1",
         depalletizing_name:"depalletizing_1",
         flag:"[0,1]"
      }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 "success"
   * @return status:404 "fail"
   */

获取码垛配方
+++++++++++++++

指令名称：get_palletizing_formula。

指令参数：

.. code-block:: c++
   :linenos:

   /** 
   * @param  string name 码垛配方名称
   */ 

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "get_palletizing_formula",
      data: {
         name: "palletizing_1"
      }
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 
   * @param  object box_config 工件配置
   * @param  object pallet_config 托盘配置
   * @param  object device_config 安装设备位置
   * @param  object pattern_config 模式配置
   * @param  object program_config 程序生成配置
   * @param  object lefttransitionpoint 左过渡点笛卡尔坐标
   * @param  object righttransitionpoint 右过渡点笛卡尔坐标
   * @param  object advanced_config 高级配置
   * @return status:404 "fail"
   */

指令反馈案例：

.. code-block:: c++
   :linenos:

   {
      "box_config": {
        "flag": 1,
        "length": 200,
        "width": 400,
        "height": 300,
        "payload": 2.34,
        "grip_point": "grippoint"
      },
      "pallet_config": {
        "flag": 1,
        "front": 1000,
        "side": 1200,
        "height": 110,
         "left_pallet": 0,
         "right_pallet": 1
      },
      "device_config": {
      "flag": 1,
      "x": 2400,
      "y": 1800,
      "z": 120,
      "angle": 0
      },
      "pattern_config": {
      "flag": 1,
      "layers": 8,
      "box_gap": 0,
      "sequence": "a,b,a,b,a,b,a,b",
      "pattern_b_enable": 1,
      "left_pattern_a": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
      "left_pattern_b": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
      "right_pattern_a": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
      "right_pattern_b": "{\"1\": [[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3],[1,2,3,0.1,0.2,0.3]]}",
      "origin_pattern_a": "[]",
      "origin_pattern_b": "[]"
      },
      "program_config": {
      "palletizing_name": "palletizing_1",
      "depalletizing_name":"depalletizing_1",
      "flag":"[0,1]"   
      },
      "lefttransitionpoint":{
      "j1":"120",
      "j2":"120",
      "j3":"120",
      "j4":"120",
      "j5":"120",
      "j6":"120"
      },
      "righttransitionpoint":{
      "j1":"120",
      "j2":"120",
      "j3":"120",
      "j4":"120",
      "j5":"120",
      "j6":"120"
      },
      "advanced_config":{
      "height": "1000",
      "x1": "100",
      "y1": "100",
      "z1": "100",
      "x2": "10",
      "y2": "10",
      "z2": "10",
      "time": "1"
      }
   }

获取码垛已有配方名称列表
++++++++++++++++++++++++++++

指令名称：get_palletizing_formula_list。

指令参数：无。

指令案例：

.. code-block:: c++
   :linenos:

   {
      cmd: "get_palletizing_formula_list"
   }

指令反馈：

.. code-block:: c++
   :linenos:

   /** 
   * @return status:200 
   * @param  Array ${name} 码垛名称列表
   * @return status:404 "fail"
   */

指令反馈案例：

.. code-block:: c++
   :linenos:

   ["palletizing1"]


