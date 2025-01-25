其他接口
=================

.. toctree:: 
    :maxdepth: 5

取得機器人DH參數補償值
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得機器人DH參數補償值
    * @param [out] dhCompensation 機器人DH參數补偿值(mm) [cmpstD1,cmpstA2,cmpstA3,cmpstD4,cmpstD5,cmpstD6]
    * @return 錯誤碼
    */
    errno_t GetDHCompensation(double dhCompensation[6]);

下載點位表資料庫
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 下載點位表資料庫
    * @param [in] pointTableName 要下載的點位表名稱    pointTable1.db
    * @param [in] saveFilePath 下載點位表的儲存路徑   C://test/
    * @return 錯誤碼
    */
    errno_t PointTableDownLoad(const std::string &pointTableName, const std::string &saveFilePath);

上傳點位表資料庫
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳點位表資料庫
    * @param [in] pointTableFilePath 上傳點位表的全路徑名   C://test/pointTable1.db
    * @return 錯誤碼
    */
    errno_t PointTableUpLoad(const std::string &pointTableFilePath);

點位表更新lua文件
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.1.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 點位表更新lua文件
    * @param [in] pointTableName 要切換的點位表名稱   "pointTable1.db",當點位表為空，即""时，表示将lua程序更新為未應用點位表的初始程序
    * @param [in] luaFileName 要更新的lua檔案名稱   "testPointTable.lua"
    * @param [out] errorStr 切換點位表錯誤訊息
    * @return 錯誤碼
    */
    errno_t PointTableUpdateLua(const std::string &pointTableName, const std::string &luaFileName);

初始化日誌參數
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 初始化日誌參數;
    * @param output_model：輸出模式，0-直接輸出；1-緩衝輸出；2-非同步輸出;
    * @param file_path: 檔案保存路徑+名稱，,長度上限256，名稱必須是xxx.log的形式，比如/home/fr/linux/fairino.log;
    * @param file_num：捲動儲存的檔案數量，1~20個.單一檔案上限50M;
    * @return errno_t 錯誤碼;
    */
	errno_t LoggerInit(int output_model = 0, std::string file_path = "", int file_num = 5);

設定日誌過濾等級
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定日誌過濾等級;
    * @param lvl: 过滤等级值，值越小輸出日志越少，默認值是1. 1-error, 2-warnning, 3-inform, 4-debug;
    */
    void SetLoggerLevel(int lvl = 1);

代碼範例
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.2.0

.. code-block:: c++
    :linenos:

    #include "libfairino/robot.h"

    //如果使用Windows，包含下面的頭文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的頭文件
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
        
取得機器人週邊協議
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得機器人週邊協議
    * @param [out] protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼
    */
    errno_t GetExDevProtocol(int *protocol);

設置機器人週邊協議
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設置機器人週邊協議
    * @param [in] protocol 機器人週邊協議號 4096-擴充軸控制卡；4097-ModbusSlave；4098-ModbusMaster
    * @return 錯誤碼
    */
    errno_t SetExDevProtocol(int protocol);

代碼範例
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:
    
    #include "libfairino/robot.h"
    //如果使用Windows，包含下面的頭文件
    #include <string.h>
    #include <windows.h>
    //如果使用linux，包含下面的頭文件
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

取得末端通訊參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得末端通訊參數
    * @param param 末端通訊參數
    * @return  錯誤碼
    */
    errno_t GetAxleCommunicationParam(AxleComParam* param);

設定末端通訊參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定末端通訊參數
    * @param param  末端通訊參數
    * @return  錯誤碼
    */
    errno_t SetAxleCommunicationParam(AxleComParam param);

設定末端檔案傳輸類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定末端檔案傳輸類型
    * @param type 1-MCU升級檔；2-LUA文件
    * @return  錯誤碼
    */
    errno_t SetAxleFileType(int type);

設定啟用末端LUA執行
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定啟用末端LUA執行
    * @param enable 0-不啟用；1-啟用
    * @return  錯誤碼
    */
    errno_t SetAxleLuaEnable(int enable);

末端LUA文件異常錯誤恢復
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 末端LUA文件異常錯誤恢復
    * @param status 0-不恢復；1-恢復
    * @return  錯誤碼
    */
    errno_t SetRecoverAxleLuaErr(int status);

末端LUA文件異常錯誤恢復
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 獲取末端LUA執行啟用狀態
    * @param status status[0]: 0-未使能；1-已使能
    * @return  錯誤碼
    */
    errno_t GetAxleLuaEnableStatus(int status[]);

設定末端LUA末端設備啟用類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定末端LUA末端設備啟用類型
    * @param forceSensorEnable 力传感器啟用狀態，0-不啟用；1-啟用
    * @param gripperEnable 夾爪啟用狀態，0-不啟用；1-啟用
    * @param IOEnable IO设备啟用狀態，0-不啟用；1-啟用
    * @return  錯誤碼
    */
    errno_t SetAxleLuaEnableDeviceType(int forceSensorEnable, int gripperEnable, int IOEnable);

設定末端LUA末端設備啟用類型
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:
        
    /**
    * @brief 取得末端LUA末端設備啟用類型
    * @param enable enable[0]:forceSensorEnable 力传感器啟用狀態，0-不啟用；1-啟用
    * @param enable enable[1]:gripperEnable 夾爪啟用狀態，0-不啟用；1-啟用
    * @param enable enable[2]:IOEnable IO设备啟用狀態，0-不啟用；1-啟用
    * @return  錯誤碼
    */
    errno_t GetAxleLuaEnableDeviceType(int* forceSensorEnable, int* gripperEnable, int* IOEnable);

取得目前配置的末端設備
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得目前配置的末端設備
    * @param forceSensorEnable 力傳感器啟用設備編號 0-未啟用；1-啟用
    * @param gripperEnable 夾爪啟用設備編號，0-不啟用；1-啟用
    * @param IODeviceEnable IO设备啟用设备編號，0-不啟用；1-啟用
    * @return  錯誤碼
    */
    errno_t GetAxleLuaEnableDevice(int forceSensorEnable[], int gripperEnable[], int IODeviceEnable[]);

設定啟用夾爪動作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定啟用夾爪動作控制功能
    * @param id 夾爪設備編號
    * @param func func[0]-夾爪啟用；func[1]-夾爪初始化；2-位置設定；3-速度設定；4-力矩設定；6-讀夾爪狀態；7-讀取初始化狀態；8-讀故障碼；9-讀取位置；10-讀取速度；11-讀取力矩
    * @return  錯誤碼
    */
    errno_t SetAxleLuaGripperFunc(int id, int func[]);

取得啟用夾爪動作控制功能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得啟用夾爪動作控制功能
    * @param id 夾爪設備編號
    * @param func func[0]-夾爪啟用；func[1]-夾爪初始化；2-位置設定；3-速度設定；4-力矩設定；6-讀夾爪狀態；7-讀取初始化狀態；8-讀故障碼；9-讀取位置；10-讀取速度；11-讀取力矩
    * @return  錯誤碼
    */
    errno_t GetAxleLuaGripperFunc(int id, int func[]);

機器人Ethercat從站文件寫入
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 機器人Ethercat從站文件寫入
    * @param type 從站檔案類型，1-升級從站檔案；2-升級從站設定檔
    * @param slaveID 從站號
    * @param fileName 上傳檔案名稱
    * @return  錯誤碼
    */
    errno_t SlaveFileWrite(int type, int slaveID, std::string fileName);

上傳末端Lua開放協議文件
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 上傳末端Lua開放協議文件
    * @param filePath 本地lua檔案路徑名 ".../AXLE_LUA_End_DaHuan.lua"
    * @return 錯誤碼
    */
    errno_t AxleLuaUpload(std::string filePath);

機器人Ethercat從站進入boot模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 機器人Ethercat從站進入boot模式
    * @return  錯誤碼
    */
    errno_t SetSysServoBootMode();

範例程式1
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

範例程式2
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
