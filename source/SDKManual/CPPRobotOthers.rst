其他接口
=================

.. toctree:: 
    :maxdepth: 5

获取机器人DH参数补偿值
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人DH参数补偿值
    * @param [out] dhCompensation 机器人DH参数补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 错误码
    */
    errno_t GetDHCompensation(double dhCompensation[6]);

下载点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下载点位表数据库
    * @param [in] pointTableName 要下载的点位表名称    pointTable1.db
    * @param [in] saveFilePath 下载点位表的存储路径   C://test/
    * @return 错误码
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

上传点位表数据库
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传点位表数据库
    * @param [in] pointTableFilePath 上传点位表的全路径名   C://test/pointTable1.db
    * @return 错误码
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

点位表更新lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 点位表更新lua文件
    * @param [in] pointTableName 要切换的点位表名称   "pointTable1.db",当点位表为空，即""时，表示将lua程序更新为未应用点位表的初始程序
    * @param [in] luaFileName 要更新的lua文件名称   "testPointTable.lua"
    * @param [out] errorStr 切换点位表错误信息
    * @return 错误码
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

初始化日志参数
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 初始化日志参数;
    * @param output_model：输出模式，0-直接输出；1-缓冲输出；2-异步输出;
    * @param file_path: 文件保存路径+名称，,长度上限256，名称必须是xxx.log的形式，比如/home/fr/linux/fairino.log;
    * @param file_num：滚动存储的文件数量，1~20个.单个文件上限50M;
    * @return errno_t 错误码;
    */
	errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

设置日志过滤等级
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置日志过滤等级;
    * @param lvl: 过滤等级值，值越小输出日志越少，默认值是1. 1-error, 2-warnning, 3-inform, 4-debug;
    */
    void SetLoggerLevel(int lvl = 1);

代码示例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;

    int main(void)
    {
        FRRobot robot;
        robot.LoggerInit(2, "C:/Users/fr/Desktop/c++sdk//sdk_with_log/abcd.log", 2);
        // robot.LoggerInit();
        robot.SetLoggerLevel(3);
        // robot.SetLoggerLevel();
        robot.RPC("192.168.58.2");

        double dh[6] = {0};
        int retval = 0;
        retval = robot.GetDHCompensation(dh);
        cout << "retval is: " << retval << endl;
        cout << "dh is: " << dh[0] << " " << dh[1] << " " << dh[2] << " " << dh[3] << " " << dh[4] << " " << dh[5] << endl;

        string save_path = "D://sharkLog/";
        string point_table_name = "point_table_a.db";
        retval = robot.PointTableDownLoad(point_table_name, save_path);
        cout<<"download : "<<point_table_name<<" fail: "<<retval<< endl;

        string upload_path = "D://sharkLog/0.db";
        retval = robot.PointTableUpLoad(upload_path);
        cout << "retval is: "<<retval<<endl;

        string point_tablename = "point_table_test.db";
        string lua_name = "testPoint.lua";
        retval = robot.PointTableUpdateLua(point_tablename, lua_name);
        cout << "retval is: " << retval << endl;
    }
        
获取机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人外设协议
    * @param [out] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t GetExDevProtocol(int *protocol);

设置机器人外设协议
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置机器人外设协议
    * @param [in] protocol 机器人外设协议号 4096-扩展轴控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 错误码
    */
    errno_t SetExDevProtocol(int protocol);

代码示例
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    #include "libfairino/robot.h"
    //如果使用Windows，包含下面的头文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的头文件
    /*
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    */
    #include <chrono>
    #include <thread>
    #include <string>

    using namespace std;

    int main(void)
    {
        FRRobot robot; 
        robot.LoggerInit();
        robot.SetLoggerLevel();
        robot.RPC("192.168.58.2");
        int retval = 0;

        ROBOT_STATE_PKG robot_pkg;
        int i = 0;
        while (i < 5)
        {
            std::this_thread::sleep_for(std::chrono::seconds(1));
            memset(&robot_pkg, 0, sizeof(ROBOT_STATE_PKG));
            retval = robot.GetRobotRealTimeState(&robot_pkg);
            std::cout << "program_state " << (int)robot_pkg.program_state<< "\n"
                << "data_len " << (int)robot_pkg.data_len << "\n"
                << "robot_state " << (int)robot_pkg.robot_state << "\n"
                << "robot_mode " << (int)robot_pkg.robot_mode << std::endl;
            i++;
        }

        int protocol = 4096;
        retval = robot.SetExDevProtocol(protocol);
        std::cout << "SetExDevProtocol retval " << retval << std::endl;
        retval = robot.GetExDevProtocol(&protocol);
        std::cout << "GetExDevProtocol retval " << retval <<" protocol is: " << protocol << std::endl;

        return 0;
    }

获取末端通讯参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取末端通讯参数
    * @param param 末端通讯参数
    * @return  错误码
    */
    errno_t GetAxleCommunicationParam(AxleComParam* param);

设置末端通讯参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端通讯参数
    * @param param  末端通讯参数
    * @return  错误码
    */
    errno_t SetAxleCommunicationParam(AxleComParam param);

设置末端文件传输类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端文件传输类型
    * @param type 1-MCU升级文件；2-LUA文件
    * @return  错误码
    */
    errno_t SetAxleFileType(int type);

设置启用末端LUA执行
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置启用末端LUA执行
    * @param enable 0-不启用；1-启用
    * @return  错误码
    */
    errno_t SetAxleLuaEnable(int enable);

末端LUA文件异常错误恢复
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 末端LUA文件异常错误恢复
    * @param status 0-不恢复；1-恢复
    * @return  错误码
    */
    errno_t SetRecoverAxleLuaErr(int status);

末端LUA文件异常错误恢复
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取末端LUA执行使能状态
    * @param status status[0]: 0-未使能；1-已使能
    * @return  错误码
    */
    errno_t GetAxleLuaEnableStatus(int status[]);

设置末端LUA末端设备启用类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置末端LUA末端设备启用类型
    * @param forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    errno_t SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable);

设置末端LUA末端设备启用类型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:
        
    /**
    * @brief 获取末端LUA末端设备启用类型
    * @param enable enable[0]:forceSensorEnable 力传感器启用状态，0-不启用；1-启用
    * @param enable enable[1]:gripperEnable 夹爪启用状态，0-不启用；1-启用
    * @param enable enable[2]:IOEnable IO设备启用状态，0-不启用；1-启用
    * @return  错误码
    */
    errno_t GetAxleLuaEnableDeviceType(int* forceSensorEnable, int* gripperEnable, int* IOEnable);

获取当前配置的末端设备
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取当前配置的末端设备
    * @param forceSensorEnable 力传感器启用设备编号 0-未启用；1-启用
    * @param gripperEnable 夹爪启用设备编号，0-不启用；1-启用
    * @param IODeviceEnable IO设备启用设备编号，0-不启用；1-启用
    * @return  错误码
    */
    errno_t GetAxleLuaEnableDevice(int forceSensorEnable[], int gripperEnable[], int IODeviceEnable[]);

设置启用夹爪动作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置启用夹爪动作控制功能
    * @param id 夹爪设备编号
    * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    errno_t SetAxleLuaGripperFunc(int id, int func[]);

获取启用夹爪动作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取启用夹爪动作控制功能
    * @param id 夹爪设备编号
    * @param func func[0]-夹爪使能；func[1]-夹爪初始化；2-位置设置；3-速度设置；4-力矩设置；6-读夹爪状态；7-读初始化状态；8-读故障码；9-读位置；10-读速度；11-读力矩
    * @return  错误码
    */
    errno_t GetAxleLuaGripperFunc(int id, int func[]);

机器人Ethercat从站文件写入
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人Ethercat从站文件写入
    * @param type 从站文件类型，1-升级从站文件；2-升级从站配置文件
    * @param slaveID 从站号
    * @param fileName 上传文件名
    * @return  错误码
    */
    errno_t SlaveFileWrite(int type, int slaveID, std::string fileName);

上传末端Lua开放协议文件
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上传末端Lua开放协议文件
    * @param filePath 本地lua文件路径名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 错误码
    */
    errno_t AxleLuaUpload(std::string filePath);

机器人Ethercat从站进入boot模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 机器人Ethercat从站进入boot模式
    * @return  错误码
    */
    errno_t SetSysServoBootMode();

示例程序1
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    void TestAxleLuaGripper(FRRobot* robot)
    {
        robot->AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua"); 

        //Restart robot     

        ROBOT_STATE_PKG pkg;
        memset(&pkg, 0, sizeof(pkg));
        AxleComParam param(7, 8, 1, 0, 5, 3, 1);
        //AxleComParam param = new AxleComParam(8,7,2,1,6,4,2);
        robot->SetAxleCommunicationParam(param);

        AxleComParam getParam;
        robot->GetAxleCommunicationParam(&getParam);
        printf("GetAxleCommunicationParam param is %d %d %d %d %d %d %d\n", getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify, getParam.timeout, getParam.timeoutTimes, getParam.period);

        robot->SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot->GetAxleLuaEnableStatus(&luaEnableStatus);
        robot->SetAxleLuaEnableDeviceType(0, 1, 0);
        
        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        robot->GetAxleLuaEnableDeviceType(&forceEnable, &gripperEnable, &ioEnable);
        printf("GetAxleLuaEnableDeviceType param is %d %d %d\n", forceEnable, gripperEnable, ioEnable);

        //int func[16] = {0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0};
        int func[16] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        robot->SetAxleLuaGripperFunc(1, func);
        int getFunc[16] = {0};
        robot->GetAxleLuaGripperFunc(1, getFunc);
        int getforceEnable[16] = {0};
        int getgripperEnable[16] = {0};
        int getioEnable[16] = {0};
        robot->GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        printf("\ngetforceEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getforceEnable[i]);
        }
        printf("\ngetgripperEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getgripperEnable[i]);
        }
        printf("\ngetioEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getioEnable[i]);
        }
        printf("\n");
        robot->ActGripper(1, 0);
        robot->Sleep(2000);
        robot->ActGripper(1, 1);
        robot->Sleep(2000);
        robot->MoveGripper(1, 90, 10, 100, 50000, 0);
        int pos = 0;
        while (true)
        {
            robot->GetRobotRealTimeState(&pkg);
            printf("gripper pos is %u\n", pkg.gripper_position);
            robot->Sleep(100);
        }
    }

示例程序2
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    void TestAxleLuaForceSensor(FRRobot* robot)
    {
        robot->AxleLuaUpload("D://zUP/AXLE_LUA_End_DaHuan.lua");

        //Restart robot  

        ROBOT_STATE_PKG pkg;
        memset(&pkg, 0, sizeof(pkg));
        AxleComParam param(7, 8, 1, 0, 5, 3, 1);
        robot->SetAxleCommunicationParam(param);

        AxleComParam getParam;
        robot->GetAxleCommunicationParam(&getParam);
        printf("GetAxleCommunicationParam param is %d %d %d %d %d %d %d\n", getParam.baudRate, getParam.dataBit, getParam.stopBit, getParam.verify, getParam.timeout, getParam.timeoutTimes, getParam.period);

        robot->SetAxleLuaEnable(1);
        int luaEnableStatus = 0;
        robot->GetAxleLuaEnableStatus(&luaEnableStatus);
        robot->SetAxleLuaEnableDeviceType(1, 0, 0);

        int forceEnable = 0;
        int gripperEnable = 0;
        int ioEnable = 0;
        robot->GetAxleLuaEnableDeviceType(&forceEnable, &gripperEnable, &ioEnable);
        printf("GetAxleLuaEnableDeviceType param is %d %d %d\n", forceEnable, gripperEnable, ioEnable);

        
        int getforceEnable[16] = { 0 };
        int getgripperEnable[16] = { 0 };
        int getioEnable[16] = { 0 };
        robot->GetAxleLuaEnableDevice(getforceEnable, getgripperEnable, getioEnable);
        printf("\ngetforceEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getforceEnable[i]);
        }
        printf("\ngetgripperEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getgripperEnable[i]);
        }
        printf("\ngetioEnable status : ");
        for (int i = 0; i < 16; i++)
        {
            printf("%d,", getioEnable[i]);
        }
        printf("\n");
        
        vector <double> M = { 15.0, 15.0, 15.0, 0.5, 0.5, 0.1 };
        vector <double> B = { 150.0, 150.0, 150.0, 5.0, 5.0, 1.0 };
        vector <double> K = { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };
        vector <double> F = { 10.0, 10.0, 10.0, 1.0, 1.0, 1.0 };
        robot->EndForceDragControl(1, 0, 0, M, B, K, F, 50, 100);

        robot->Sleep(10 * 1000);

        robot->EndForceDragControl(0, 0, 0, M, B, K, F, 50, 100);
    }
