擴展軸
=============

.. toctree:: 
    :maxdepth: 5

設定485擴展軸參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [in] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驅動器軟體版本，1-V1.0
    * @param [in] servoResolution 編碼器分辨率
    * @param [in] axisMechTransRatio 機械傳動比
    * @return 錯誤碼
    */
    errno_t AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

取得485擴展軸配置參數
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得485擴展軸配置參數
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoCompany 伺服驅動器廠商，1-戴納泰克
    * @param [out] servoModel 伺服驅動器型號，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驅動器軟體版本，1-V1.0
    * @param [out] servoResolution 編碼器分辨率
    * @param [out] axisMechTransRatio 機械傳動比
    * @return 錯誤碼
    */
    errno_t AuxServoGetParam(int servoId, int* servoCompany, int* servoModel, int* servoSoftVersion, int* servoResolution, double* axisMechTransRatio);
    
代碼範例
**************
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

        int retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;

        int servoCompany;
        int servoModel;
        int servoSoftVersion;
        int servoResolution;
        double axisMechTransRatio;
        retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
        std::cout << "servoCompany " << servoCompany<< "\n"
                  << "servoModel " << servoModel << "\n"
                  << "servoSoftVersion " << servoSoftVersion<< "\n"
                  << "servoResolution " << servoResolution<< "\n"
                  << "axisMechTransRatio "<<axisMechTransRatio<< "\n"
                  << std::endl;

        retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;

        retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
        std::cout << "servoCompany " << servoCompany<< "\n"
                  << "servoModel " << servoModel << "\n"
                  << "servoSoftVersion " << servoSoftVersion<< "\n"
                  << "servoResolution " << servoResolution<< "\n"
                  << "axisMechTransRatio "<<axisMechTransRatio<< "\n"
                  << std::endl;

        return 0;
    }
    
設定485擴展軸使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸使能/去使能
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] status 使能狀態，0-去使能， 1-使能
    * @return 錯誤碼
    */
    errno_t AuxServoEnable(int servoId, int status);

設定485擴展軸控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸控制模式
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 錯誤碼
    */
    errno_t AuxServoSetControlMode(int servoId, int mode);

設定485擴展軸目標位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸目標位置(位置模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] pos 目標位置，mm或°
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetPos(int servoId, double pos, double speed);

設定485擴展軸目標轉矩(力矩模式) - 暫未開放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸目標轉矩(力矩模式)
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] torque 目標力矩，Nm
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetTorque(int servoId, double torque);

設定485擴展軸回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸回零
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] mode 回零模式，0-目前位置回零；1-限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);
    
清除485擴展軸錯誤訊息
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 清除485擴展軸錯誤訊息
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼
    */
    errno_t AuxServoClearError(int servoId);

取得485擴展軸伺服狀態
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得485擴展軸伺服狀態
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [out] servoErrCode 伺服驅動器故障碼
    * @param [out] servoState 伺服驅動器狀態[十进制数转為二进制，bit0-bit5：伺服使能-伺服运行-正限位触发-负限位触发-定位完成-回零完成]
    * @param [out] servoPos 伺服當前位置 mm或°
    * @param [out] servoSpeed 伺服當前速度 mm/s或°/s
    * @param [out] servoTorque 伺服當前轉矩Nm
    * @return 錯誤碼
    */
    errno_t AuxServoGetStatus(int servoId, int* servoErrCode, int* servoState, double* servoPos, double* servoSpeed, double* servoTorque);

代碼範例
**************
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

        retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);
        std::cout << "AuxServoSetParam is: " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(3));

        retval = robot.AuxServoEnable(1, 0);
        std::cout << "AuxServoEnable disenable " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        int servoerrcode = 0;
        int servoErrCode;
        int servoState;
        double servoPos;
        double servoSpeed;
        double servoTorque;
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoState "<< servoState << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        retval = robot.AuxServoEnable(1, 1);
        std::cout << "AuxServoEnable enable " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoState "<< servoState << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        retval = robot.AuxServoHoming(1, 1, 5, 1);
        std::cout << "AuxServoHoming " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(3));

        retval = robot.AuxServoSetTargetPos(1, 200, 30);
        std::cout << "AuxServoSetTargetPos " << retval << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
        retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
        std::cout << "AuxServoGetStatus servoSpeed "<< servoSpeed << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));

        return 0;
    }

設定485擴展軸目標速度（速度模式）
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定485擴展軸目標速度（速度模式）
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @param [in] speed 目標速度，mm/s或°/s
    * @return 錯誤碼
    */
    errno_t AuxServoSetTargetSpeed(int servoId, double speed);
    
設定狀態回饋中485擴展軸資料軸號
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定狀態回饋中485擴展軸資料軸號
    * @param [in] servoId 伺服驅動器ID，範圍[1-15],對應從站ID
    * @return 錯誤碼
    */
    errno_t AuxServosetStatusID(int servoId);
        
取得機器人即時狀態結構體
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得機器人即時狀態結構體
    * @param [out] pkg 機器人即時狀態結構體
    * @return 錯誤碼
    */
    errno_t GetRobotRealTimeState(ROBOT_STATE_PKG *pkg);
        
UDP擴展軸通訊參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸通訊參數配置
    * @param [in] ip PLC IP地址
    * @param [in] port	連接埠號
    * @param [in] period	通訊週期(ms，預設為2，請勿修改此參數)
    * @param [in] lossPkgTime	丟包檢測時間(ms)
    * @param [in] lossPkgNum	丟包次數
    * @param [in] disconnectTime	通訊斷開確認時長
    * @param [in] reconnectEnable	通訊斷開自動重連啟用 0-不啟用 1-啟用
    * @param [in] reconnectPeriod	重連週期間隔(ms)
    * @param [in] reconnectNum	重連次數
    * @return 錯誤碼
    */
    errno_t ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum);
        
取得UDP擴充軸通訊參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得UDP擴充軸通訊參數
    * @param [out] ip PLC IP地址
    * @param [out] port	連接埠號
    * @param [out] period	通訊週期(ms，預設為2，請勿修改此參數)
    * @param [out] lossPkgTime	丟包檢測時間(ms)
    * @param [out] lossPkgNum	丟包次數
    * @param [out] disconnectTime	通訊斷開確認時長
    * @param [out] reconnectEnable	通訊斷開自動重連啟用 0-不啟用 1-啟用
    * @param [out] reconnectPeriod	重連週期間隔(ms)
    * @param [out] reconnectNum	重連次數
    * @return 錯誤碼
    */
    errno_t ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum);
        
加載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 加載UDP通信
    * @return 錯誤碼
    */
    errno_t ExtDevLoadUDPDriver();

卸載UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 卸載UDP通信
    * @return 錯誤碼
    */
    errno_t ExtDevUnloadUDPDriver();

代碼範例
**************

.. code-block:: c++
    :linenos:

    int testUDPParam(FRRobot* robot)
    {
        int rtn = 0;
        rtn = robot->ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5);
        cout << "ExtDevSetUDPComParam rtn is " << rtn << endl;
        string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
        rtn = robot->ExtDevGetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum);
        string patam = "\nip " + ip + "\nport " + to_string(port) + "\nperiod  " + to_string(period) + "\nlossPkgTime " + to_string(lossPkgTime) + "\nlossPkgNum  " + to_string(lossPkgNum) + "\ndisConntime  " + to_string(disconnectTime) + "\nreconnecable  " + to_string(reconnectEnable) + "\nreconnperiod  " + to_string(reconnectPeriod) + "\nreconnnun  " + to_string(reconnectNum);
        cout << "ExtDevGetUDPComParam rtn is " << rtn << patam<< endl;

        robot->ExtDevLoadUDPDriver();
        //Sleep(1000 * 5);
        robot->ExtDevUnloadUDPDriver();
        return 0;
    }

UDP擴充軸通訊異常斷開後恢復連接
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後恢復連接
    * @return 錯誤碼
    */
    errno_t ExtDevUDPClientComReset();

UDP擴充軸通訊異常斷開後關閉通訊
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸通訊異常斷開後關閉通訊
    * @return 錯誤碼
    */
    errno_t ExtDevUDPClientComClose();

UDP擴充軸參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴充軸參數配置
    * @param [in] axisID 軸號
    * @param [in] axisType 擴展軸類型 0-平移；1-旋轉
    * @param [in] axisDirection 擴展軸方向 0-正向；1-方向
    * @param [in] axisMax 擴展軸最大位置 mm
    * @param [in] axisMin 擴展軸最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 導程mm
    * @param [in] encResolution 編碼器分辨率
    * @param [in] axisOffect焊接起始點擴展軸偏移量
    * @param [in] axisCompany 驅動器廠商 1-禾川；2-匯川；3-松下
    * @param [in] axisModel 驅動器型號 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-匯川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 編碼器類型 0-增量；1-絕對值
    * @return 錯誤碼
    */
    errno_t ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

設定擴展軸安裝位置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴展軸安裝位置
    * @param [in] installType 0-機器人安裝在外部軸上，1-機器人安裝在外部軸外
    * @return 錯誤碼
    */
    errno_t SetRobotPosToAxis(int installType);

設定擴展軸系統DH參數配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴展軸系統DH參數配置
    * @param [in]  axisConfig 外部軸構型，0-單自由度直線滑軌，1-兩自由度L型變位機，2-三自由度，3-四自由度，4-單自由度變位機
    * @param [in]  axisDHd1 外部軸DH參數d1 mm
    * @param [in]  axisDHd2 外部軸DH參數d2 mm
    * @param [in]  axisDHd3 外部軸DH參數d3 mm
    * @param [in]  axisDHd4 外部軸DH參數d4 mm
    * @param [in]  axisDHa1 外部軸DH參數11 mm
    * @param [in]  axisDHa2 外部軸DH參數a2 mm
    * @param [in]  axisDHa3 外部軸DH參數a3 mm
    * @param [in]  axisDHa4 外部軸DH參數a4 mm
    * @return 錯誤碼
    */
    errno_t SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

代碼範例
**********

.. code-block:: c++
    :linenos:

    int testAxisParam(FRRobot* robot)
    {
        int rtn = 0;
        rtn = robot->SetRobotPosToAxis(1);
        cout << "SetRobotPosToAxis rtn is " << rtn <<endl;
        rtn = robot->SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
        cout << "SetAxisDHParaConfig rtn is " << rtn << endl;
        rtn = robot->ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0);
        cout << "ExtAxisParamConfig rtn is " << rtn << endl;
        return 0;
    }

設定擴展軸座標系參考點-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴展軸座標系參考點-四點法
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    errno_t ExtAxisSetRefPoint(int pointNum);

計算擴展軸座標系-四點法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 計算擴展軸座標系-四點法
    * @param [out]  coord 座標系值
    * @return 錯誤碼
    */
    errno_t ExtAxisComputeECoordSys(DescPose& coord);

應用擴展軸座標系
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 應用擴展軸座標系
    * @param [in]  applyAxisId 擴展軸編號 bit0-bit3對應擴展軸編號1-4，如應用擴展軸1和3，則是 0b 0000 0101；也就是5
    * @param [in]  axisCoordNum 擴展軸座標系編號
    * @param [in]  coord 座標系值
    * @param [in]  calibFlag 標定標誌 0-否，1-是
    * @return 錯誤碼
    */
    errno_t ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

代碼範例
************

.. code-block:: c++
    :linenos:

    int testExtAxisCoord(FRRobot* robot)
    {
        DescPose coord = {};
        int rtn = 0;
        rtn = robot->ExtAxisSetRefPoint(1);
        rtn = robot->ExtAxisSetRefPoint(2);
        rtn = robot->ExtAxisSetRefPoint(3);
        rtn = robot->ExtAxisSetRefPoint(4);

        rtn = robot->ExtAxisComputeECoordSys(coord);

        rtn = robot->ExtAxisActiveECoordSys(1, 1, coord, 1);
        cout << "ExtAxisActiveECoordSys rtn is " << rtn << endl;
        return 0;
    }

設定標定參考點在變位機末端座標系下位姿
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定標定參考點在變位機末端座標系下位姿
    * @param [in] pos 位元姿值
    * @return 錯誤碼
    */
    errno_t SetRefPointInExAxisEnd(DescPose pos);

變位機座標系參考點設置
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 變位機座標系參考點設置
    * @param [in]  pointNum 點編號[1-4]
    * @return 錯誤碼
    */
    errno_t PositionorSetRefPoint(int pointNum);

變位機座標系計算-四點法
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 變位機座標系計算-四點法
    * @param [out] coord 座標系值
    * @return 錯誤碼
    */
    errno_t PositionorComputeECoordSys(DescPose& coord);

代碼範例
************

.. code-block:: c++
    :linenos:

    int testExtAxisCoord(FRRobot* robot)
    {
        DescPose coord = {};
        int rtn = 0;
        DescPose dese = {};
        rtn = robot->SetRefPointInExAxisEnd(dese);

        rtn = robot->PositionorSetRefPoint(1);
        rtn = robot->PositionorSetRefPoint(2);
        rtn = robot->PositionorSetRefPoint(3);
        rtn = robot->PositionorSetRefPoint(4);
        cout << "PositionorSetRefPoint rtn is " << rtn << endl;

        rtn = robot->PositionorComputeECoordSys(coord);
        cout << "PositionorComputeECoordSys rtn is " << rtn << endl;
        cout << "coord x is " << coord.tran.x << endl;
        cout << "coord y is " << coord.tran.y << endl;
        cout << "coord z is " << coord.tran.z << endl;
        cout << "coord rx is " << coord.rpy.rx << endl;
        cout << "coord ry is " << coord.rpy.ry << endl;
        cout << "coord rz is " << coord.rpy.rz << endl;

        rtn = robot->ExtAxisActiveECoordSys(1, 1, coord, 1);
        cout << "ExtAxisActiveECoordSys rtn is " << rtn << endl;
        return 0;
    }

UDP擴展軸使能
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸使能
    * @param [in] axisID 軸號[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 錯誤碼
    */
    errno_t ExtAxisServoOn(int axisID, int status);

UDP擴展軸回零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸回零
    * @param [in] axisID 軸號[1-4]
    * @param [in] mode 回零方式 0-目前位置回零，1-負限位回零，2-正限位回零
    * @param [in] searchVel 尋零速度(mm/s)
    * @param [in] latchVel 尋零箍位速度(mm/s)
    * @return 錯誤碼
    */
    errno_t ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP擴展軸點動開始
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸點動開始
    * @param [in] axisID 軸號[1-4]
    * @param [in] direction 轉動方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc 加速度 (mm/s2)
    * @param [in] maxDistance 最大點動距離
    * @return 錯誤碼
    */
    errno_t ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP擴展軸點動停止
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸點動停止
    * @param [in] axisID 軸號[1-4]
    * @return 錯誤碼
    */
    errno_t ExtAxisStopJog(int axisID);

代碼範例
************

.. code-block:: c++
    :linenos:

    int testServoOnHomingJog(FRRobot* robot)
    {
        robot->ExtAxisServoOn(2, 1);
        Sleep(1000 * 3);
        robot->ExtAxisStartJog(1, 0, 10, 10, 30);
        Sleep(1000 * 1);
        robot->ExtAxisStopJog(1);
        robot->ExtAxisSetHoming(2, 0, 10, 2);
        Sleep(1000 * 3);
        robot->ExtAxisServoOn(2, 0);
        return 0;
    }

UDP擴展軸運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸運動
    * @param [in] pos 目標位置
    * @param [in] ovl 速度百分比
    * @return 錯誤碼
    */
    errno_t ExtAxisMove(ExaxisPos pos, double ovl);

代碼範例
************

.. code-block:: c++
    :linenos:

    int testExtAxisMove(FRRobot* robot)
    {
        ExaxisPos axisPos;
        axisPos.ePos[0] = 20;
        axisPos.ePos[1] = 0;
        axisPos.ePos[2] = 0;
        axisPos.ePos[3] = 0;
        robot->ExtAxisMove(axisPos, 50);
        return 0;
    }

UDP擴展軸與機器人關節運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人關節運動同步運動
    * @param [in] joint_pos 目標關節位置,單位deg
    * @param [in] desc_pos 目標笛卡兒位姿
    * @param [in] tool 工具座標號，範圍[0~14]
    * @param [in] user 工件座標號，範圍[0~14]
    * @param [in] vel 速度百分比，範圍[0~100]
    * @param [in] acc 加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl 速度縮放因子，範圍[0~100]
    * @param [in] epos 擴展軸位置，單位mm
    * @param [in] blendT [-1.0]-運動到位(阻塞)，[0~500.0]-平滑時間(非阻塞)，單位ms
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位元位偏移量
    * @return  錯誤碼
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

代碼範例
************

.. code-block:: c++
    :linenos:

    void testSyncMoveJ()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴展軸座標系標定及應用
        DescPose pos = {/* 輸入您的標定點座標 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步關節運動起始點
        DescPose startdescPose = {/*輸入您的座標*/ };
        JointPos startjointPos = {/*輸入您的座標*/ };
        ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點座標 */ };

        //8.記錄您的同步關節運動終點座標
        DescPose enddescPose = {/*輸入您的座標*/ };
        JointPos endjointPos = {/*輸入您的座標*/ };
        ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點座標 */ };

        //9.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
    }

UDP擴展軸與機器人直線運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人直線運動同步運動
    * @param [in] joint_pos  目標關節位置,單位deg
    * @param [in] desc_pos   目標笛卡兒位姿
    * @param [in] tool  工具座標號，範圍[0~14]
    * @param [in] user  工件座標號，範圍[0~14]
    * @param [in] vel  速度百分比，範圍[0~100]
    * @param [in] acc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @param [in] epos  擴展軸位置，單位mm
    * @param [in] offset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos  位元位偏移量
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

代碼範例
************

.. code-block:: c++
    :linenos:

    void testSyncMoveL()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴展軸座標系標定及應用
        DescPose pos = {/* 輸入您的標定點座標 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步直線運動起始點
        DescPose startdescPose = {/*輸入您的座標*/ };
        JointPos startjointPos = {/*輸入您的座標*/ };
        ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點座標 */ };

        //8.記錄您的同步直線運動終點座標
        DescPose enddescPose = {/*輸入您的座標*/ };
        JointPos endjointPos = {/*輸入您的座標*/ };
        ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點座標 */ };

        //9.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
    }
    
UDP擴展軸與機器人圓弧運動同步運動
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP擴展軸與機器人圓弧運動同步運動
    * @param [in] joint_pos_p  路徑點關節位置,單位deg
    * @param [in] desc_pos_p   路徑點笛卡爾位姿
    * @param [in] ptool  工具座標號，範圍[0~14]
    * @param [in] puser  工件座標號，範圍[0~14]
    * @param [in] pvel  速度百分比，範圍[0~100]
    * @param [in] pacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_p  中间點擴展軸位置，單位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_p  位元位偏移量
    * @param [in] joint_pos_t  目標點關節位置,單位deg
    * @param [in] desc_pos_t   目標點笛卡爾位姿
    * @param [in] ttool  工具座標號，範圍[0~14]
    * @param [in] tuser  工件座標號，範圍[0~14]
    * @param [in] tvel  速度百分比，範圍[0~100]
    * @param [in] tacc  加速度百分比，範圍[0~100],暫不開放
    * @param [in] epos_t  擴展軸位置，單位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐標系/工件坐標系偏移，2-工具坐標系偏移
    * @param [in] offset_pos_t  位元位偏移量	 
    * @param [in] ovl  速度縮放因子，範圍[0~100]
    * @param [in] blendR [-1.0]-運動到位(阻塞)，[0~1000.0]-平滑半徑(非阻塞)，單位mm
    * @return 錯誤碼
    */
    errno_t ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);
    
代碼範例
************

.. code-block:: c++
    :linenos:

    void btnSyncMoveC()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.標定並應用機器人工具坐標系，您可以使用四點法或六點法進行工具坐標系的標定和應用，涉及工具坐標系標定的接口如下：
        //    int SetToolPoint(int point_num);  //設定工具參考點-六點法
        //    int ComputeTool(ref DescPose tcp_pose);  //計算工具座標系
        //    int SetTcp4RefPoint(int point_num);    //設定工具參考點-四點法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //計算工具座標系-四點法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //設定應用工具坐標系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //設定應用工具坐標系列表

        //2.設定UDP通訊參數，並載入UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.設定擴展軸參數，包括擴展軸類型、擴展軸驅動器參數、擴展軸DH參數
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //單軸变位机及DH參數
        robot.SetRobotPosToAxis(1);  //擴充軸安裝位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驅動器參數，本示例為單軸变位机，因此只需要設定一個驅動器參數，若您選擇包含多個軸的擴展軸類型，需要每一個軸設定驅動器參數

        //4.設定所選的軸使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.進行擴展軸座標系標定及應用
        DescPose pos = {/* 輸入您的標定點座標 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要透過四個不同位置的點來標定擴充軸，因此需要呼叫此介面4次才能完成標定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //計算擴展軸標定結果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //將標定結果應用到擴展軸座標系

        //6.在擴充軸上標定工件坐標系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.記錄您的同步圓弧運動起始點
        DescPose startdescPose = {/*輸入您的座標*/ };
        JointPos startjointPos = {/*輸入您的座標*/ };
        ExaxisPos startexaxisPos = {/* 輸入您的擴展軸起始點座標 */ };

        //8.記錄您的同步圓弧運動終點座標
        DescPose enddescPose = {/*輸入您的座標*/ };
        JointPos endjointPos = {/*輸入您的座標*/ };
        ExaxisPos endexaxisPos = {/* 輸入您的擴展軸終點座標 */ };

        //9.記錄您的同步圓弧運動中間點座標
        DescPose middescPose = {/*輸入您的座標*/ };
        JointPos midjointPos = {/*輸入您的座標*/ };
        ExaxisPos midexaxisPos = {/* 輸入機器人圓弧中間點時的擴展軸座標 */ };

        //10.編寫同步運動程式
        //運動到起始點，假設應用的工具坐標系、工件坐標係都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //開始同步運動
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
    }
    
設定擴充DO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴充DO
    * @param [in] DONum DO編號
    * @param [in] bOpen 開關 true-開；false-關
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    errno_t SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
設定擴充AO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴充AO
    * @param [in] AONum AO編號 
    * @param [in] value 類比量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 錯誤碼
    */
    errno_t SetAuxAO(int AONum, double value, bool block);
    
代碼範例
************

.. code-block:: c++
    :linenos:

    int testAODO(FRRobot* robot)
    {
        for (int i = 0; i < 128; i++)
        {
            robot->SetAuxDO(i, true, false, true);
            Sleep(100);
        }
        for (int i = 0; i < 128; i++)
        {
            robot->SetAuxDO(i, false, false, true);
            Sleep(100);
        }

        for (int i = 0; i < 409; i++)
        {
            robot->SetAuxAO(0, i * 10, true);
            robot->SetAuxAO(1, 4095 - i * 10, true);
            robot->SetAuxAO(2, i * 10, true);
            robot->SetAuxAO(3, 4095 - i * 10, true);
            Sleep(10);
        }
        return 0;
    }
            
設定擴充DI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴充DI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    errno_t SetAuxDIFilterTime(int filterTime);

設定擴展AI輸入濾波時間
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 設定擴展AI輸入濾波時間
    * @param [in] filterTime 濾波時間(ms)
    * @return 錯誤碼
    */
    errno_t SetAuxAIFilterTime(int filterTime);

等待擴充DI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴充DI輸入
    * @param [in] DINum DI編號
    * @param [in] bOpen 開關 0-關；1-開
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    errno_t WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
等待擴展AI輸入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待擴展AI輸入
    * @param [in] AINum AI編號
    * @param [in] sign 0-大於；1-小於
    * @param [in] value AI值
    * @param [in] time 最大等待時間(ms)
    * @param [in] errorAlarm 是否繼續運動
    * @return 錯誤碼
    */
    errno_t WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
取得擴展DI值
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得擴展DI值
    * @param [in] DINum DI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [out] isOpen 0-關；1-開
    * @return 錯誤碼
    */
    errno_t GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
取得擴展AI值
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 取得擴展AI值
    * @param [in] AINum AI編號
    * @param [in] isNoBlock 是否阻塞
    * @param [in] value 輸入值
    * @return 錯誤碼
    */
    errno_t GetAuxAI(int AINum, bool isNoBlock, int& value);

代碼範例
***********
.. code-block:: c++
    :linenos:

    int testGetDI(FRRobot* robot)
    {
    robot->SetAuxDIFilterTime(10);
    robot->SetAuxAIFilterTime(10);

        for (int i = 0; i < 20; i++)
        {
            bool curValue = false;
            int rtn = robot->GetAuxDI(i, false, curValue);
            cout << "DI"<<i<< "   " << curValue<< endl;
        }
    int curValue = -1;
    int rtn = 0;
    for (int i = 0; i < 4; i++)
    {
        rtn = robot->GetAuxAI(i, true, urValue);
    }

    robot->WaitAuxDI(1, true, 1000, false);
    robot->WaitAuxAI(1, 1, 132, 1000, false);

        return 0;
    }