虚拟机-Virtual Box
===================

虚拟机环境配置
------------------

安装Virtual Box
~~~~~~~~~~~~~~~~~~~~

- Virtual Box版本：VirtualBox-7.0.14。
- 文件名称：VirtualBox-7.0.14-161095-Win.exe。
- 下载安装包后选择默认路径安装即可。

.. image:: controller_virtual_machine/001.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-1 VirtualBox 7.0.14

镜像配置
~~~~~~~~~~~

1) 下载并打开镜像。

- 下载虚拟机镜像FAIRINO SimMachine.rar并解压。
- 打开VirtualBox，选择“注册”，选择虚拟机“FAIRINO SimMachine.vbox”文件，即可导入虚拟环境。

.. image:: controller_virtual_machine/002.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-2 VirtualBox 中选择注册

.. image:: controller_virtual_machine/003.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-3 选择虚拟机文件

- 导入后，选择“FAIRINO SimMachine”，点击“启动”按钮，开启虚拟机。

.. image:: controller_virtual_machine/004.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-4 启动虚拟机

.. note:: 
    虚拟机设置 -> 系统 -> 处理器，默认启用 PAE/NX，如果电脑BIOS尚未启用虚拟化，会导致启动失败，需在 BIOS 中开启虚拟化，详见 \ `附录1 <#bios>`__\。

2) 共享文件夹。

虚拟机和宿主机之间的共享文件夹已经默认设置好，建议拷贝文件时都使用共享文件夹进行拷贝。同时虚拟机环境已经安装增强功能，共享粘贴板，方便复制粘贴。

- 宿主机共享文件夹在 D:\share（需要手动创建share文件夹）。
- 虚拟机共享文件夹在 /home/fr/shared。

.. image:: controller_virtual_machine/005.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-5 共享文件夹配置

3) 进入虚拟机系统。

- 虚拟机运行环境系统：Ubuntu 18.04.6。
- 虚拟机运行环境系统：RAM 4G，ROM 50G，6核CPU 。
- 用户名：root，密码：123。

.. image:: controller_virtual_machine/007.png
   :width: 6in
   :align: center

.. centered:: 图表 6.1-6 tty登录虚拟机系统

虚拟机系统默认关闭用户图形界面，使用tty登录。

- 如果用户需要开启用户图形界面：
  
.. list-table::
   :widths: 200
   :align: center

   * - systemctl set-default graphical.target

   * - reboot
  
- 如果用户需要再次关闭用户图形界面：
  
.. list-table::
   :widths: 200
   :align: center

   * - systemctl set-default multi-user.target

   * - reboot

用户登录web页面，操作虚拟机器人
-----------------------------------

- 首次登录，用戶准备一台测试电脑，通过网线连接到虚拟机，测试电脑网口IP设置为192.168.58.XXX 网段，子网掩码设置为255.255.255.0。
- 在测试电脑上，打开 Chrome 浏览器，输入默认IP：192.168.58.2，即可访问web界面，操作虚拟机器人。

.. image:: controller_virtual_machine/008.png
   :width: 6in
   :align: center

.. centered:: 图表 6.2-1 虚拟机web登录界面

.. image:: controller_virtual_machine/009.png
   :width: 6in
   :align: center

.. centered:: 图表 6.2-2 虚拟机web操作界面

用户修改IP地址
~~~~~~~~~~~~~~~~~~~~~~

.. image:: controller_virtual_machine/010.png
   :width: 6in
   :align: center

.. centered:: 图表 6.2-3 设置网络页面

1. 打开浏览器，输入默认IP：192.168.58.2，打开web页面；
2. 使用admin账号登录，密码：123；
3. 进入“系统设置” -> “通用设置” -> “网络设置”，修改 IP为目标IP地址，点击“设置网络”；
4. 重启虚拟机，虚拟机桥接网卡上 IP 已经自动变更为修改后的 IP地址；
5. 配置本地测试电脑以太网口、宿主机以太网口与虚拟机桥接网卡上 IP为同一网段；
6. 此时用户在测试电脑上，打开 Chrome 浏览器，输入修改后IP地址，即可访问web界面，操作虚拟机器人。

.. image:: controller_virtual_machine/011.png
   :width: 6in
   :align: center

.. centered:: 图表 6.2-4 网络拓扑图

.. note:: 
   如当前没有测试电脑，可在本地电脑上添加虚拟网卡（环回网络适配器），详见\ `附录2 <#id4>`__\。

虚拟机-Docker
=================================

Linux部署docker镜像
---------------------------

操作环境
~~~~~~~~~~~~~~

虚拟机运行环境系统：Ubuntu 18.04.6；

虚拟机运行环境系统：RAM 4G，ROM 50G，6核CPU ；

操作权限：使用超级管理员root权限，设置方法见附录3；

docker安装文件：fr_docker.tar.gz；

FAIRINO SimMachine镜像：FAIRINOSimMachine.tar；

安装docker
~~~~~~~~~~~~~~

若用户已安装部署docker，则跳过此节，进行1.3镜像部署。

1.下载fr_docker.tar.gz，放至Ubuntu文件路径/opt/。

2.解压fr_docker.tar.gz.，以/opt/目录下为例：

.. code-block:: console
   :linenos:

   cd /opt/ && tar -zxvf fr_docker.tar.gz

.. image:: controller_virtual_machine/036.png
   :width: 6in
   :align: center

3.执行安装docker脚本：

.. code-block:: console
   :linenos:

   sh install.sh docker-27.0.3.tgz

待脚本执行完毕后，出现版本号，则表示安装成功。

.. image:: controller_virtual_machine/037.png
   :width: 6in
   :align: center

镜像配置
~~~~~~~~~~~~~~

导入docker镜像
++++++++++++++++++++

1. 下载虚拟机镜像FAIRINOSimMachine.tar并解压。

2. 查看docker版本确认已安装。

.. code-block:: console
   :linenos:

   docker -v

.. image:: controller_virtual_machine/038.png
   :width: 6in
   :align: center   

3. 导入镜像   

.. code-block:: console
   :linenos:

   docker load -i ./FAIRINOSimMachine.tar

出现fairno_simmachine:latest则表示导入完成。

.. image:: controller_virtual_machine/039.png
   :width: 6in
   :align: center  

4. 执行docker images查看是否导入成功。

创建自定义桥接网络
++++++++++++++++++++

1. 执行以下命令，创建名为fairino-net，网段为192.168.58.0/24的桥接网络。

.. code-block:: console
   :linenos:

   docker network create --driver bridge --subnet 192.168.58.0/24 --gateway 192.168.58.1 fairino-net

2. 查看网络

.. code-block:: console
   :linenos:

   docker network ls

存在fairino-net网络表示创建成功。

.. image:: controller_virtual_machine/040.png
   :width: 6in
   :align: center 

首次启动docker容器
++++++++++++++++++++

1. 创建容器并启动

使用fairino-net网络，fairino_simmachine镜像启动容器。

.. code-block:: console
   :linenos:

   docker run -d -P --name fairino-container --net fairino-net fairino_simmachine

.. image:: controller_virtual_machine/041.png
   :width: 6in
   :align: center 

.. code-block:: console
   :linenos:

   docker ps 

查看容器是否成功启动，出现fairino-container则表示启动成功。

.. image:: controller_virtual_machine/042.png
   :width: 6in
   :align: center 

web操作虚拟机器人
----------------------------

容器正常启动
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

此小节针对非首次启动容器，由于重启电脑或docker关闭等原因容器未在后台运行情况。

1. 启动docker： 

.. code-block:: console
   :linenos:

   systemctl start docker

2. 查看docker状态：

.. code-block:: console
   :linenos:

   systemctl status docker
   
绿色active(running)表示启动成功。

.. image:: controller_virtual_machine/043.png
   :width: 6in
   :align: center 

3. 执行docker ps -a查看容器ID。

.. image:: controller_virtual_machine/044.png
   :width: 6in
   :align: center 

4. 执行 docker start [容器ID]。

.. image:: controller_virtual_machine/045.png
   :width: 6in
   :align: center 

5. 执行成功，再次docker ps 查看容器正在运行。

.. image:: controller_virtual_machine/046.png
   :width: 6in
   :align: center 

操作虚拟机器人
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 确认docker容器正在运行。

.. code-block:: console
   :linenos:

   docker ps 

出现fairino-container则表示正在运行。

.. image:: controller_virtual_machine/047.png
   :width: 6in
   :align: center 

2. 打开浏览器，输入默认IP：192.168.58.2，即可访问web界面，操作虚拟机器人。

.. image:: controller_virtual_machine/048.png
   :width: 6in
   :align: center 

3. 使用admin账号登录，密码：123。

.. image:: controller_virtual_machine/049.png
   :width: 6in
   :align: center 

用户修改IP地址
~~~~~~~~~~~~~~~~~~~~~~

.. image:: controller_virtual_machine/050.png
   :width: 6in
   :align: center 

1. 打开浏览器，输入默认 IP： 192.168.58.2，打开 web 页面；
2. 使用 admin 账号登录，密码： 123；
3. 进入“系统设置” → “通用设置” → “网络设置”， 修改 IP 为目标 IP 地址、掩码、网关。点击“设置网络”；
   
以修改IP为192.168.56.2/24为例。

.. image:: controller_virtual_machine/051.png
   :width: 6in
   :align: center 

4. 打开终端，关闭容器；
 	
查看容器ID：

.. code-block:: console
   :linenos:
      
   docker ps -a

.. image:: controller_virtual_machine/052.png
   :width: 6in
   :align: center 

关闭容器：

.. code-block:: console
   :linenos:
   
   docker stop [容器ID]

.. image:: controller_virtual_machine/053.png
   :width: 6in
   :align: center 

5. 重新配置容器网络；
   
删除原先网络：

.. code-block:: console
   :linenos:
   
   docker network rm fairino-net

创建新网络：

.. code-block:: console
   :linenos:
   
   docker network create --driver bridge --subnet [目标IP/子网掩码] --gateway [网关IP] fairino-net

以192.168.56.0/24为例：docker network create --driver bridge --subnet 192.168.56.0/24 --gateway 192.168.56.1 fairino-net

.. image:: controller_virtual_machine/054.png
   :width: 6in
   :align: center 

6. 将容器重新连接到新创建的网络；

.. code-block:: console
   :linenos:

   docker network connect fairino-net [容器ID]

.. image:: controller_virtual_machine/055.png
   :width: 6in
   :align: center 

7. 重新启动容器；

.. code-block:: console
   :linenos:
   
   docker start [容器ID]

8. 此时打开浏览器， 输入修改后 IP 地址，即可访问 web 界面，操作虚拟机器人。

.. image:: controller_virtual_machine/056.png
   :width: 6in
   :align: center 

附录
===================

附录1：BIOS 中启用虚拟化
-------------------------

不同型号的电脑启用虚拟化的流程可能不同，现以联想ThinkPad系列windows10举例：

- 打开电脑设置，选择更新和安全。

.. image:: controller_virtual_machine/013.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/014.png
   :width: 4in
   :align: center

- 选择“恢复”。

.. image:: controller_virtual_machine/015.png
   :width: 4in
   :align: center

- 选择“立即重启”。

.. image:: controller_virtual_machine/016.png
   :width: 4in
   :align: center

- 选择“疑难解答”。
  
.. image:: controller_virtual_machine/017.png
   :width: 4in
   :align: center

- 选择“高级选项”。

.. image:: controller_virtual_machine/018.png
   :width: 4in
   :align: center

- 选择UEFI固件设置。

.. image:: controller_virtual_machine/019.png
   :width: 4in
   :align: center

- 选择“重启”。

.. image:: controller_virtual_machine/020.png
   :width: 4in
   :align: center

- 选择“Security”下的“Virtualization”。

.. image:: controller_virtual_machine/021.png
   :width: 4in
   :align: center

- 选择“Enabled”，按下“Enter”确认。

.. image:: controller_virtual_machine/022.png
   :width: 4in
   :align: center

- 按下“F10”，选择“Yes”，按下“Enter”保存修改。

.. image:: controller_virtual_machine/023.png
   :width: 4in
   :align: center

附录2：添加虚拟网卡（环回网络适配器）
--------------------------------------

1. 打开设备管理器，按下“Windows键-X”，选择“设备管理器”。
   
.. image:: controller_virtual_machine/024.png
   :width: 4in
   :align: center

2. 添加网络适配器。

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
   
3. 查看虚拟网卡，按下“Windows键-X”，选择“网络连接”。

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
   
4. 配置环回适配器网络。

- IP地址: 192.168.58.XXX（与192.168.58.2 同一网段即可）。
- 子网掩码：255.255.255.0。

.. image:: controller_virtual_machine/012.png
   :width: 6in
   :align: center

5. 打开Virtualbox网络配置，网卡名称选择“环回适配器网络”，启动虚拟机即可。

.. image:: controller_virtual_machine/013.png
   :width: 6in
   :align: center

附录3：root权限
--------------------------------------

Ubuntu安装好后，Ubuntu系统默认root用户是不能登录的，密码也是空的。如果想要使用root用户登录，必须先为root用户设置密码。

1. 打开终端，输入 sudo passwd root ，然后回车输入几次密码，显示密码设置成功。

.. image:: controller_virtual_machine/057.png
   :width: 6in
   :align: center

2. 在终端继续输入 su - root 命令切换用户，回车输入密码。

.. warning:: 输入命令时一定要输入“-”，选项“-”表示连带环境变量一起切换，“-”坚决不能少。

.. image:: controller_virtual_machine/058.png
   :width: 6in
   :align: center

附录4：docker基础命令
--------------------------------------

1. docker 帮助命令 :

.. code-block:: console
   :linenos:

   docker --help

2. 启动docker :

.. code-block:: console
   :linenos:

   systemctl start docker

3. 关闭docker :

.. code-block:: console
   :linenos:

   systemctl stop docker

4. 重启docker :

.. code-block:: console
   :linenos:

   systemctl restart docker

5. docker设置随服务启动而自启动 :

.. code-block:: console
   :linenos:

   systemctl enable docker

6. 查看docker 运行状态 :

.. code-block:: console
   :linenos:

   systemctl status docker
   --如果是在运行中输入命令后会看到绿色的active

7. docker镜像相关 :

.. code-block:: console
   :linenos:

   docker images：列出已经下载的镜像，查看镜像
   docker rmi 镜像id或name：删除本地镜像
   docker rmi -f 镜像id或name: 删除镜像
   docker build：构建镜像
   docker search 镜像id或name：在Docker Hub仓库中搜索关键字镜像
   docker pull 镜像id或name：从仓库中下载镜像
   docker images：列出已经下载的镜像，查看镜像
   docker rmi 镜像id或name：删除本地镜像
   docker rmi -f 镜像id或name: 删除镜像
   docker build：构建镜像

8. docker镜像相关 :

.. code-block:: console
   :linenos:

   docker ps：列出运行中的容器
   docker ps -a ： 查看所有容器，包括未运行
   docker stop 容器id或name：停止容器
   docker kill 容器id：强制停止容器
   docker start 容器id或name：启动已停止的容器
   docker inspect 容器id：查看容器的所有信息
   docker container logs 容器id：查看容器日志
   docker top 容器id：查看容器里的进程
   docker exec -it 容器id /bin/bash：进入容器
   exit：退出容器
   docker rm 容器id或name：删除已停止的容器
   docker rm -f 容器id：删除正在运行的容器
   docker exec -it 容器ID sh :进入容器