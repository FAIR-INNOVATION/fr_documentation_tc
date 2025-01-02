简介
===================

FRCap是一个基于Web的插件，可集成到协作机器人WebApp中。FRCap通过基于Node.js和Vue3的Element plus，frcap-ui和frcap-api等模块构建一个协作机器人WebApp配置页面或者应用来扩展机器人功能及应用场景。

从本质上讲，FRCap是一个运行在Node.js环境下的Web应用，与WebApp相互独立，WebApp提供管理和访问服务。FRCap可以通过提供的官方接口与机器人控制器交互，或者客户依据实际需求编写自定义接口指令和处理逻辑进行个性化开发。

.. image:: frcap_pictures/001.png
   :width: 6in
   :align: center

.. centered:: 图表 1.1 WebApp + FRCap展示图