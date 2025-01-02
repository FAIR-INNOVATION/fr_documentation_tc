扩展轴
=============

.. toctree:: 
    :maxdepth: 5

设置485扩展轴参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [in] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [in] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [in] servoResolution 编码器分辨率
    * @param [in] axisMechTransRatio 机械传动比
    * @return 错误码
    */
    errno_t AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

获取485扩展轴配置参数
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取485扩展轴配置参数
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [out] servoCompany 伺服驱动器厂商，1-戴纳泰克
    * @param [out] servoModel 伺服驱动器型号，1-FD100-750C
    * @param [out] servoSoftVersion 伺服驱动器软件版本，1-V1.0
    * @param [out] servoResolution 编码器分辨率
    * @param [out] axisMechTransRatio 机械传动比
    * @return 错误码
    */
    errno_t AuxServoGetParam(int servoId, int* servoCompany, int* servoModel, int* servoSoftVersion, int* servoResolution, double* axisMechTransRatio);
    
代码示例
**************
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
    
设置485扩展轴使能/去使能
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴使能/去使能
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] status 使能状态，0-去使能， 1-使能
    * @return 错误码
    */
    errno_t AuxServoEnable(int servoId, int status);

设置485扩展轴控制模式
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴控制模式
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] mode 控制模式，0-位置模式，1-速度模式
    * @return 错误码
    */
    errno_t AuxServoSetControlMode(int servoId, int mode);

设置485扩展轴目标位置(位置模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标位置(位置模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] pos 目标位置，mm或°
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoSetTargetPos(int servoId, double pos, double speed);

设置485扩展轴目标转矩(力矩模式) - 暂未开放
++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标转矩(力矩模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] torque 目标力矩，Nm
    * @return 错误码
    */
    errno_t AuxServoSetTargetTorque(int servoId, double torque);

设置485扩展轴回零
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴回零
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] mode 回零模式，0-当前位置回零；1-限位回零
    * @param [in] searchVel 回零速度，mm/s或°/s
    * @param [in] latchVel 箍位速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);
    
清除485扩展轴错误信息
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 清除485扩展轴错误信息
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @return 错误码
    */
    errno_t AuxServoClearError(int servoId);

获取485扩展轴伺服状态
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取485扩展轴伺服状态
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [out] servoErrCode 伺服驱动器故障码
    * @param [out] servoState 伺服驱动器状态[十进制数转为二进制，bit0-bit5：伺服使能-伺服运行-正限位触发-负限位触发-定位完成-回零完成]
    * @param [out] servoPos 伺服当前位置 mm或°
    * @param [out] servoSpeed 伺服当前速度 mm/s或°/s
    * @param [out] servoTorque 伺服当前转矩Nm
    * @return 错误码
    */
    errno_t AuxServoGetStatus(int servoId, int* servoErrCode, int* servoState, double* servoPos, double* servoSpeed, double* servoTorque);

代码示例
**************
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

设置485扩展轴目标速度(速度模式)
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置485扩展轴目标速度(速度模式)
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @param [in] speed 目标速度，mm/s或°/s
    * @return 错误码
    */
    errno_t AuxServoSetTargetSpeed(int servoId, double speed);
    
设置状态反馈中485扩展轴数据轴号
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置状态反馈中485扩展轴数据轴号
    * @param [in] servoId 伺服驱动器ID，范围[1-15],对应从站ID
    * @return 错误码
    */
    errno_t AuxServosetStatusID(int servoId);
        
获取机器人实时状态结构体
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取机器人实时状态结构体
    * @param [out] pkg 机器人实时状态结构体
    * @return 错误码
    */
    errno_t GetRobotRealTimeState(ROBOT_STATE_PKG *pkg);
        
UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴通讯参数配置
    * @param [in] ip PLC IP地址
    * @param [in] port	端口号
    * @param [in] period	通讯周期(ms，默认为2，请勿修改此参数)
    * @param [in] lossPkgTime	丢包检测时间(ms)
    * @param [in] lossPkgNum	丢包次数
    * @param [in] disconnectTime	通讯断开确认时长
    * @param [in] reconnectEnable	通讯断开自动重连使能 0-不使能 1-使能
    * @param [in] reconnectPeriod	重连周期间隔(ms)
    * @param [in] reconnectNum	重连次数
    * @return 错误码
    */
    errno_t ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum);
        
获取UDP扩展轴通讯参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取UDP扩展轴通讯参数
    * @param [out] ip PLC IP地址
    * @param [out] port	端口号
    * @param [out] period	通讯周期(ms，默认为2，请勿修改此参数)
    * @param [out] lossPkgTime	丢包检测时间(ms)
    * @param [out] lossPkgNum	丢包次数
    * @param [out] disconnectTime	通讯断开确认时长
    * @param [out] reconnectEnable	通讯断开自动重连使能 0-不使能 1-使能
    * @param [out] reconnectPeriod	重连周期间隔(ms)
    * @param [out] reconnectNum	重连次数
    * @return 错误码
    */
    errno_t ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum);
        
加载UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 加载UDP通信
    * @return 错误码
    */
    errno_t ExtDevLoadUDPDriver();

卸载UDP通信
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 卸载UDP通信
    * @return 错误码
    */
    errno_t ExtDevUnloadUDPDriver();

代码示例
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

UDP扩展轴通信异常断开后恢复连接
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后恢复连接
    * @return 错误码
    */
    errno_t ExtDevUDPClientComReset();

UDP扩展轴通信异常断开后关闭通讯
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴通信异常断开后关闭通讯
    * @return 错误码
    */
    errno_t ExtDevUDPClientComClose();

UDP扩展轴参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴参数配置
    * @param [in] axisID 轴号
    * @param [in] axisType 扩展轴类型 0-平移；1-旋转
    * @param [in] axisDirection 扩展轴方向 0-正向；1-方向 
    * @param [in] axisMax 扩展轴最大位置 mm
    * @param [in] axisMin 扩展轴最小位置 mm
    * @param [in] axisVel 速度mm/s
    * @param [in] axisAcc 加速度mm/s2
    * @param [in] axisLead 导程mm
    * @param [in] encResolution 编码器分辨率
    * @param [in] axisOffect焊缝起始点扩展轴偏移量
    * @param [in] axisCompany 驱动器厂家 1-禾川；2-汇川；3-松下
    * @param [in] axisModel 驱动器型号 1-禾川-SV-XD3EA040L-E，2-禾川-SV-X2EA150A-A，1-汇川-SV620PT5R4I，1-松下-MADLN15SG，2-松下-MSDLN25SG，3-松下-MCDLN35SG
    * @param [in] axisEncType 编码器类型  0-增量；1-绝对值
    * @return 错误码
    */
    errno_t ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

设置扩展轴安装位置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展轴安装位置
    * @param [in] installType 0-机器人安装在外部轴上，1-机器人安装在外部轴外
    * @return 错误码
    */
    errno_t SetRobotPosToAxis(int installType);

设置扩展轴系统DH参数配置
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展轴系统DH参数配置
    * @param [in]  axisConfig 外部轴构型，0-单自由度直线滑轨，1-两自由度L型变位机，2-三自由度，3-四自由度，4-单自由度变位机
    * @param [in]  axisDHd1 外部轴DH参数d1 mm
    * @param [in]  axisDHd2 外部轴DH参数d2 mm
    * @param [in]  axisDHd3 外部轴DH参数d3 mm
    * @param [in]  axisDHd4 外部轴DH参数d4 mm
    * @param [in]  axisDHa1 外部轴DH参数11 mm
    * @param [in]  axisDHa2 外部轴DH参数a2 mm
    * @param [in]  axisDHa3 外部轴DH参数a3 mm
    * @param [in]  axisDHa4 外部轴DH参数a4 mm
    * @return 错误码
    */
    errno_t SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

代码示例
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

设置扩展轴坐标系参考点-四点法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展轴坐标系参考点-四点法
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    errno_t ExtAxisSetRefPoint(int pointNum);

计算扩展轴坐标系-四点法
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 计算扩展轴坐标系-四点法
    * @param [out]  coord 坐标系值
    * @return 错误码
    */
    errno_t ExtAxisComputeECoordSys(DescPose& coord);

应用扩展轴坐标系
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 应用扩展轴坐标系
    * @param [in]  applyAxisId 扩展轴编号 bit0-bit3对应扩展轴编号1-4，如应用扩展轴1和3，则是 0b 0000 0101；也就是5
    * @param [in]  axisCoordNum 扩展轴坐标系编号
    * @param [in]  coord 坐标系值
    * @param [in]  calibFlag 标定标志 0-否，1-是
    * @return 错误码
    */
    errno_t ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

代码示例
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

设置标定参考点在变位机末端坐标系下位姿
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置标定参考点在变位机末端坐标系下位姿
    * @param [in] pos 位姿值
    * @return 错误码
    */
    errno_t SetRefPointInExAxisEnd(DescPose pos);

变位机坐标系参考点设置
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 变位机坐标系参考点设置
    * @param [in]  pointNum 点编号[1-4]
    * @return 错误码
    */
    errno_t PositionorSetRefPoint(int pointNum);

变位机坐标系计算-四点法
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 变位机坐标系计算-四点法
    * @param [out] coord 坐标系值
    * @return 错误码
    */
    errno_t PositionorComputeECoordSys(DescPose& coord);

代码示例
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

UDP扩展轴使能
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴使能
    * @param [in] axisID 轴号[1-4]
    * @param [in] status 0-去使能；1-使能
    * @return 错误码
    */
    errno_t ExtAxisServoOn(int axisID, int status);

UDP扩展轴回零
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴回零
    * @param [in] axisID 轴号[1-4]
    * @param [in] mode 回零方式 0-当前位置回零，1-负限位回零，2-正限位回零
    * @param [in] searchVel 寻零速度(mm/s)
    * @param [in] latchVel 寻零箍位速度(mm/s)
    * @return 错误码
    */
    errno_t ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

UDP扩展轴点动开始
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴点动开始
    * @param [in] axisID 轴号[1-4]
    * @param [in] direction 转动方向 0-反向；1-正向
    * @param [in] vel 速度(mm/s)
    * @param [in] acc 加速度 (mm/s2)
    * @param [in] maxDistance 最大点动距离
    * @return 错误码
    */
    errno_t ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
UDP扩展轴点动停止
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴点动停止
    * @param [in] axisID 轴号[1-4]
    * @return 错误码
    */
    errno_t ExtAxisStopJog(int axisID);

代码示例
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

UDP扩展轴运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴运动
    * @param [in] pos 目标位置
    * @param [in] ovl 速度百分比
    * @return 错误码
    */
    errno_t ExtAxisMove(ExaxisPos pos, double ovl);

代码示例
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

UDP扩展轴与机器人关节运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴与机器人关节运动同步运动
    * @param [in] joint_pos 目标关节位置,单位deg
    * @param [in] desc_pos 目标笛卡尔位姿
    * @param [in] tool 工具坐标号，范围[0~14]
    * @param [in] user 工件坐标号，范围[0~14]
    * @param [in] vel 速度百分比，范围[0~100]
    * @param [in] acc 加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl 速度缩放因子，范围[0~100]
    * @param [in] epos 扩展轴位置，单位mm
    * @param [in] blendT [-1.0]-运动到位(阻塞)，[0~500.0]-平滑时间(非阻塞)，单位ms
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return  错误码
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

代码示例
************

.. code-block:: c++
    :linenos:

    void testSyncMoveJ()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用
        DescPose pos = {/* 输入您的标定点坐标 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步关节运动起始点
        DescPose startdescPose = {/*输入您的坐标*/ };
        JointPos startjointPos = {/*输入您的坐标*/ };
        ExaxisPos startexaxisPos = {/* 输入您的扩展轴起始点坐标 */ };

        //8.记录您的同步关节运动终点坐标
        DescPose enddescPose = {/*输入您的坐标*/ };
        JointPos endjointPos = {/*输入您的坐标*/ };
        ExaxisPos endexaxisPos = {/* 输入您的扩展轴终点坐标 */ };

        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
    }

UDP扩展轴与机器人直线运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴与机器人直线运动同步运动
    * @param [in] joint_pos  目标关节位置,单位deg
    * @param [in] desc_pos   目标笛卡尔位姿
    * @param [in] tool  工具坐标号，范围[0~14]
    * @param [in] user  工件坐标号，范围[0~14]
    * @param [in] vel  速度百分比，范围[0~100]
    * @param [in] acc  加速度百分比，范围[0~100],暂不开放
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @param [in] epos  扩展轴位置，单位mm
    * @param [in] offset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos  位姿偏移量
    * @return 错误码
    */
    errno_t ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

代码示例
************

.. code-block:: c++
    :linenos:

    void testSyncMoveL()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用
        DescPose pos = {/* 输入您的标定点坐标 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步直线运动起始点
        DescPose startdescPose = {/*输入您的坐标*/ };
        JointPos startjointPos = {/*输入您的坐标*/ };
        ExaxisPos startexaxisPos = {/* 输入您的扩展轴起始点坐标 */ };

        //8.记录您的同步直线运动终点坐标
        DescPose enddescPose = {/*输入您的坐标*/ };
        JointPos endjointPos = {/*输入您的坐标*/ };
        ExaxisPos endexaxisPos = {/* 输入您的扩展轴终点坐标 */ };

        //9.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
    }
    
UDP扩展轴与机器人圆弧运动同步运动
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief UDP扩展轴与机器人圆弧运动同步运动
    * @param [in] joint_pos_p  路径点关节位置,单位deg
    * @param [in] desc_pos_p   路径点笛卡尔位姿
    * @param [in] ptool  工具坐标号，范围[0~14]
    * @param [in] puser  工件坐标号，范围[0~14]
    * @param [in] pvel  速度百分比，范围[0~100]
    * @param [in] pacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_p  中间点扩展轴位置，单位mm
    * @param [in] poffset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos_p  位姿偏移量
    * @param [in] joint_pos_t  目标点关节位置,单位deg
    * @param [in] desc_pos_t   目标点笛卡尔位姿
    * @param [in] ttool  工具坐标号，范围[0~14]
    * @param [in] tuser  工件坐标号，范围[0~14]
    * @param [in] tvel  速度百分比，范围[0~100]
    * @param [in] tacc  加速度百分比，范围[0~100],暂不开放
    * @param [in] epos_t  扩展轴位置，单位mm
    * @param [in] toffset_flag  0-不偏移，1-基坐标系/工件坐标系偏移，2-工具坐标系偏移
    * @param [in] offset_pos_t  位姿偏移量	 
    * @param [in] ovl  速度缩放因子，范围[0~100]
    * @param [in] blendR [-1.0]-运动到位(阻塞)，[0~1000.0]-平滑半径(非阻塞)，单位mm
    * @return 错误码
    */
    errno_t ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);
    
代码示例
************

.. code-block:: c++
    :linenos:

    void btnSyncMoveC()
    {
    Robot robot = new Robot();
    robot.RPC("192.168.58.2");

    //1.标定并应用机器人工具坐标系，您可以使用四点法或六点法进行工具坐标系的标定和应用，涉及工具坐标系标定的接口如下：
        //    int SetToolPoint(int point_num);  //设置工具参考点-六点法
        //    int ComputeTool(ref DescPose tcp_pose);  //计算工具坐标系
        //    int SetTcp4RefPoint(int point_num);    //设置工具参考点-四点法
        //    int ComputeTcp4(ref DescPose tcp_pose);   //计算工具坐标系-四点法
        //    int SetToolCoord(int id, DescPose coord, int type, int install);  //设置应用工具坐标系
        //    int SetToolList(int id, DescPose coord, int type, int install);   //设置应用工具坐标系列表

        //2.设置UDP通信参数，并加载UDP通信
        robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
        robot.ExtDevLoadUDPDriver();

        //3.设置扩展轴参数，包括扩展轴类型、扩展轴驱动器参数、扩展轴DH参数
        robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //单轴变位机及DH参数
        robot.SetRobotPosToAxis(1);  //扩展轴安装位置
        robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //伺服驱动器参数，本示例为单轴变位机，因此只需要设置一个驱动器参数，若您选择包含多个轴的扩展轴类型，需要每一个轴设置驱动器参数

        //4.设置所选的轴使能、回零
        robot.ExtAxisServoOn(1, 0);
        robot.ExtAxisSetHoming(1, 0, 20, 3);

        //5.进行扩展轴坐标系标定及应用
        DescPose pos = {/* 输入您的标定点坐标 */ };
        robot.SetRefPointInExAxisEnd(pos);
        robot.PositionorSetRefPoint(1); /*您需要通过四个不同位置的点来标定扩展轴，因此需要调用此接口4次才能完成标定 */
        DescPose coord = {};
        robot.PositionorComputeECoordSys(coord); //计算扩展轴标定结果
        robot.ExtAxisActiveECoordSys(1, 1, coord, 1);  //将标定结果应用到扩展轴坐标系

        //6.在扩展轴上标定工件坐标系，您需要用到以下接口
        //int SetWObjCoordPoint(int point_num);
        //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
        //int SetWObjCoord(int id, DescPose coord);
        //int SetWObjList(int id, DescPose coord);

        //7.记录您的同步圆弧运动起始点
        DescPose startdescPose = {/*输入您的坐标*/ };
        JointPos startjointPos = {/*输入您的坐标*/ };
        ExaxisPos startexaxisPos = {/* 输入您的扩展轴起始点坐标 */ };

        //8.记录您的同步圆弧运动终点坐标
        DescPose enddescPose = {/*输入您的坐标*/ };
        JointPos endjointPos = {/*输入您的坐标*/ };
        ExaxisPos endexaxisPos = {/* 输入您的扩展轴终点坐标 */ };

        //9.记录您的同步圆弧运动中间点坐标
        DescPose middescPose = {/*输入您的坐标*/ };
        JointPos midjointPos = {/*输入您的坐标*/ };
        ExaxisPos midexaxisPos = {/* 输入机器人圆弧中间点时的扩展轴坐标 */ };

        //10.编写同步运动程序
        //运动到起始点，假设应用的工具坐标系、工件坐标系都是1
        robot.ExtAxisMove(startexaxisPos, 20);
        DescPose offdese = { 0, 0, 0, 0, 0, 0 };
        robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);

        //开始同步运动
        robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
    }
    
设置扩展DO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展DO
    * @param [in] DONum DO编号
    * @param [in] bOpen 开关 true-开；false-关
    * @param [in] smooth 是否平滑
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    errno_t SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
设置扩展AO
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展AO
    * @param [in] AONum AO编号 
    * @param [in] value 模拟量值[0-4095]
    * @param [in] block 是否阻塞
    * @return 错误码
    */
    errno_t SetAuxAO(int AONum, double value, bool block);
    
代码示例
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
            
设置扩展DI输入滤波时间
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展DI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    errno_t SetAuxDIFilterTime(int filterTime);

设置扩展AI输入滤波时间
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 设置扩展AI输入滤波时间
    * @param [in] filterTime 滤波时间(ms)
    * @return 错误码
    */
    errno_t SetAuxAIFilterTime(int filterTime);

等待扩展DI输入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待扩展DI输入
    * @param [in] DINum DI编号
    * @param [in] bOpen 开关 0-关；1-开
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    errno_t WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
等待扩展AI输入
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 等待扩展AI输入
    * @param [in] AINum AI编号
    * @param [in] sign 0-大于；1-小于
    * @param [in] value AI值
    * @param [in] time 最大等待时间(ms)
    * @param [in] errorAlarm 是否继续运动
    * @return 错误码
    */
    errno_t WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
获取扩展DI值
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取扩展DI值
    * @param [in] DINum DI编号
    * @param [in] isNoBlock 是否阻塞
    * @param [out] isOpen 0-关；1-开
    * @return 错误码
    */
    errno_t GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
获取扩展AI值
+++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief 获取扩展AI值
    * @param [in] AINum AI编号
    * @param [in] isNoBlock 是否阻塞
    * @param [in] value 输入值
    * @return 错误码
    */
    errno_t GetAuxAI(int AINum, bool isNoBlock, int& value);

代码示例
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