概述
++++++++++
frcobot_ros簡要架構如下圖所示，協作機器人端提供了XMLRPC伺服器和TCP伺服器。

- XMLRPC伺服器主要提供機器人指令API完成機器人運動和狀態值取得功能
- 狀態回饋的TCP伺服器提供了機器人狀態的即時回饋，回饋週期8ms。

用戶PC端中已安裝了ROS和Moveit!，編譯完成frcobot_ros。在frcobot_ros中每個功能包都包含了機器人API的lib庫，以及在frcobot_hw建立與機器人狀態回饋伺服器通訊的TCP客戶端，取得機器人狀態回饋資料。

.. figure:: img/frcobot_ros.png
    :width: 6in
    :align: center

安裝
++++++++++
本章介紹如何建置frcobot_ros以及所需的安裝環境。

環境要求
-----------

frcobot_ros推薦環境如下：

.. note::
 - Ubuntu 18.04 LTS Bionic Beaver和ROS Melodic Morenia
 - Ubuntu 20.04 LTS Focal Fossa和ROS Noetic Ninjemys

以下說明適用於 Ubuntu 20.04 LTS 系統和 ROS Noetic Ninjemys。如果使用的是Melodic，則將下發命令列中的 ``noetic`` 替換成 ``melodic``.

ROS安裝要求
--------------
安裝Ubuntu系統後，`安裝並設定ROS Noetic環境 <https://wiki.ros.org/noetic/Installation/Ubuntu>`__。

配置ROS Noetic後，安裝如下所需環境：

.. code-block:: shell
    :linenos:

    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    sudo apt-get install -y \
        ros-noetic-rosparam-shortcuts \
        ros-noetic-ros-control \
        ros-noetic-ros-controllers \
        ros-noetic-moveit \
        libxmlrpcpp-dev

編譯ROS包
-------------
在正確安裝和設定好ROS Noetic後，在您選擇的目錄中建立一個Catkin工作區。

.. code-block:: shell
    :linenos:

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws
    catkin_init_workspace src

然後從Gitee克隆frcobot_ros庫。

.. code-block:: shell
    :linenos:

    cd ~/catkin_ws/src
    git clone https://gitee.com/fair-innovation/frcobot_ros.git

建置frcobot_ros包

.. code-block::  shell
    :linenos:

    cd ~/catkin_ws
    catkin_make
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
    source ~/.bashrc

如果發生報錯請檢查ROS安裝需求中的套件是否都已安裝成功，編譯完成後，將lib庫拷貝到ROS的lib環境下(路徑為：/opt/ros/noetic/lib)，以便程式可以正常執行。

.. code-block:: shell
    :linenos:

    # 此處catkin_ws預設路徑為“~”，如有不同，將“~”改為實際路徑即可
    sudo cp ~/catkin_ws/src/frcobot_ros/frcobot_hw/lib/* /opt/ros/noetic/lib

快速開始
++++++++++

frcobot_hw
-----------------
frcobot_hw主要提供了和協作機器人通訊的基本功能。

.. note::
 - 包含協作機器人狀態回饋msg
 - 提供控制協作機器人的指令demo
 - 提供協作機器人狀態回饋節點和Topic
 - 可透過launch檔案快速啟動狀態節點和指令demo

frcobot_hw.launch內容如下：

.. code-block:: xml
    :linenos:

    <launch>

        <!-- params -->
        <param name="robot_ip" type="string" value="192.168.58.2"/>
        <param name="robot_port" type="int" value="8083"/>

        <!-- frcobot status node -->
        <node pkg="frcobot_hw" type="frcobot_status_node" name="frcobot_status_node" output="screen" />

        <!-- frcobot control demo -->
        <node pkg="frcobot_hw" type="frcobot_cmd_demo" name="frcobot_cmd_demo" output="screen" />
        
    </launch>

.. important:: 

 - ``robot_ip`` 和 ``robot_port`` 需要注意與被控制的協作機器人IP和連接埠一致
 - 出廠機器人預設IP為192.168.58.2，用戶狀態回饋埠為8083

透過以下指令可快速啟動機器人狀態回饋節點和指令demo功能。

.. code-block:: shell
    :linenos:

    roslaunch frcobot_hw frcobot_hw.launch

新開一個terminal，透過以下指令可列印並查看即時的狀態回饋資料。

.. code-block:: shell
    :linenos:

    rostopic ehco /frcobot_status

.. frcobot_camera
.. -----------------
.. frcobot_camera提供与图漾RVS和相机的手眼标定功能和無序抓取（Bin-Picking）功能。



.. frcobot_gripper
.. -------------------


.. frcobot_description
.. ----------------------


.. frcobot moveit!
.. -----------------------

    