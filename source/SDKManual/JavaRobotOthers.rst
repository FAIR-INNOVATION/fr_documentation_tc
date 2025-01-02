其他接口
================

.. toctree:: 
    :maxdepth: 5

下载点位表数据库
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 下载点位表数据库 
    * @param [in] pointTableName 要下载的点位表名称    pointTable1.db
    * @param [in] saveFilePath 下载点位表的存储路径   C://test/
    * @return 错误码 
    */
    int PointTableDownLoad(String pointTableName, String saveFilePath);

上传点位表数据库
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 上传点位表数据库 
    * @param [in] pointTableFilePath 上传点位表的全路径名   C://test/pointTable1.db
    * @return 错误码 
    */
    int PointTableUpLoad(String pointTableFilePath);

切换点位表并应用
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 切换点位表并应用 
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db"
    * @param [in] errorStr 切换点位表错误信息
    * @return 错误码 
    */
    int PointTableSwitch(String pointTableName, String errorStr);

点位表更新lua文件
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 点位表更新lua文件
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db",当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "testPointTable.lua"
    * @param [out] errorStr 切换点位表错误信息
    * @return 错误码 
    */
    int PointTableUpdateLua(String pointTableName, String luaFileName, String errorStr);

代码示例
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }

        robot.PointTableUpLoad("D://zUP/point_table_test1.db");//点位表上传
        robot.PointTableDownLoad("point_table_test1.db", "D://zUP/");//点位表下载
        String errStr = "";
        robot.PointTableSwitch("point_table_test1.db", errStr);//切换点位表
        //点位表更新LUA程序
        robot.PointTableUpdateLua("point_table_test2.db", "1010Test.lua", errStr);
    }

初始化日志参数
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 初始化日志参数
    * @param [in] logType：输出模式，DIRECT-直接输出；BUFFER-缓冲输出；ASYNC-异步输出
    * @param [in] logLevel：日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @param [in] filePath: 文件保存路径，如“D://Log/”
    * @param [in] saveFileNum：保存文件个数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @param [in] saveDays: 保存文件天数，同时超出保存文件个数和保存文件天数的文件将被删除
    * @return 错误码
    */
    int LoggerInit(FrLogType logType, FrLogLevel logLevel, String filePath, int saveFileNum, int saveDays);

设置日志过滤等级
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param [in] logLevel: 日志过滤等级，ERROR-错误；WARNING-警告;INFO-信息；DEBUG-调试
    * @return 错误码
    */
    int SetLoggerLevel(FrLogLevel logLevel);


代码示例
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        robot.SetLoggerLevel(FrLogLevel.DEBUG);
    }

设置机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码 
    */
    int SetExDevProtocol(int protocol);

获取机器人外设协议
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取机器人外设协议
    * @return List[0]:错误码; List[1] : int protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster 
    */
    List<Integer> GetExDevProtocol();

代码示例
+++++++++++++++++++++++++++++++++++
.. code-block:: console
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }

        robot.SetExDevProtocol(4096);
        List<Number> rtnArr =  robot.GetTargetPayload(1);
        rtnArr=GetExDevProtocol();
    }

末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器配置
    * @param [in] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [in] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @param [in] config idSoftware 软件版本，0-J1.0/HuiDe1.0(暂未开放)
    * @param [in] config idBus 挂载位置，1-末端1号口；2-末端2号口...8-末端8号口(暂未开放)
    * @return 错误码
    */
    int AxleSensorConfig(DeviceConfig config);

获取末端传感器配置
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 获取末端传感器配置
    * @param [out] config idCompany 厂商，18-JUNKONG；25-HUIDE
    * @param [out] config idDevice 类型，0-JUNKONG/RYR6T.V1.0
    * @return 错误码
    */
    int AxleSensorConfigGet(DeviceConfig config);

末端传感器激活
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器激活
    * @param [in] actFlag 0-复位；1-激活
    * @return 错误码
    */
    int AxleSensorActivate(int actFlag);

末端传感器寄存器写入
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 末端传感器寄存器写入
    * @param [in] devAddr  设备地址编号 0-255
    * @param [in] regHAddr 寄存器地址高8位
    * @param [in] regLAddr 寄存器地址低8位
    * @param [in] regNum  寄存器个数 0-255
    * @param [in] data1 写入寄存器数值1
    * @param [in] data2 写入寄存器数值2
    * @param [in] isNoBlock 0-阻塞；1-非阻塞
    * @return 错误码
    */
    int AxleSensorRegWrite(int devAddr, int regHAddr, int regLAddr, int regNum, int data1, int data2, int isNoBlock);

代码示例
+++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    public static void main(String[] args)
    {
        Robot robot = new Robot();
        robot.SetReconnectParam(true,20,500);//设置重连次数、间隔
        robot.LoggerInit(FrLogType.DIRECT, FrLogLevel.INFO, "D://log", 10, 10);
        int rtn = robot.RPC("192.168.58.2");
        if(rtn == 0)
        {
            System.out.println("rpc连接 success");
        }
        else
        {
            System.out.println("rpc连接 fail");
            return ;
        }
        DeviceConfig axleSensorConfig = new DeviceConfig(18, 0, 0, 1);
        robot.AxleSensorConfig(axleSensorConfig);

        DeviceConfig getConfig = new DeviceConfig();
        robot.AxleSensorConfigGet(getConfig);
        System.out.println("company is " + getConfig.company + ",  type is " + getConfig.device);

        robot.AxleSensorActivate(1);

        robot.AxleSensorRegWrite(1, 4, 6, 1, 0, 0, 0);
    }