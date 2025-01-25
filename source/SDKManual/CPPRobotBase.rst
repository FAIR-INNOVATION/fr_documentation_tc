機器人基礎
=============

.. toctree:: 
    :maxdepth: 5

實例化機器人
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  機器人介面類別建構函數
    */
    FRRobot();

與控制器建立通信
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  與機器人控制器建立通信
    * @param  [in] ip  控制器IP位址，出場預設為192.168.58.2
    * @return 錯誤碼
    */
    errno_t  RPC(const char *ip);

與控制器關閉通訊
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
     * @brief 與機器人控制器關閉通訊
     * @return 錯誤碼
     */
    errno_t  CloseRPC();

查詢SDK版本號
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢SDK版本號
    * @param  [out] version   SDK版本號
    * @return  錯誤碼
    */  
    errno_t  GetSDKVersion(char *version);

獲取控制器IP
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  獲取控制器IP
    * @param  [out] ip  控制器IP
    * @return  錯誤碼
    */
    errno_t  GetControllerIP(char *ip);

控制機器人進入或退出拖曳示教模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制機器人進入或退出拖曳示教模式
    * @param  [in] state 0-退出拖曳示教模式，1-進入拖曳示教模式
    * @return  錯誤碼
    */
    errno_t  DragTeachSwitch(uint8_t state);

查詢機器人是否處於拖曳模式
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  查詢機器人是否處於拖曳示教模式
    * @param  [out] state 0-非拖曳示教模式，1-拖曳示教模式
    * @return  錯誤碼
    */
    errno_t  IsInDragTeach(uint8_t *state);

控制機器人上使能或下使能
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief  控制機器人上使能或下使能，機器人上電後預設自動上啟用
    * @param  [in] state  0-下使能，1-上使能
    * @return  錯誤碼
    */
    errno_t  RobotEnable(uint8_t state);

控制機器人手自動模式切換
++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    /**
    * @brief 控制機器人手自動模式切換
    * @param [in] mode 0-自動模式，1-手動模式
    * @return 錯誤碼
    */
    errno_t  Mode(int mode);

代碼範例
+++++++++++++
.. code-block:: c++
    :linenos:
    
    #include <cstdlib>
    #include <iostream>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #include "FRRobot.h"
    #include "RobotTypes.h"

    using namespace std;

    int main(void)
    {
        FRRobot robot;                 //實例化機器人對象
        robot.RPC("192.168.58.2");     //與機器人控制器建立通信连接

        char ip[64]="";
        char version[64] = "";
        uint8_t state;

        robot.GetSDKVersion(version);
        printf("SDK version:%s\n", version);
        robot.GetControllerIP(ip);
        printf("controller ip:%s\n", ip);

        robot.Mode(1);
        sleep(1);
        robot.DragTeachSwitch(1);
        robot.IsInDragTeach(&state);
        printf("drag state :%u\n", state);
        sleep(3);
        robot.DragTeachSwitch(0);
        sleep(1);
        robot.IsInDragTeach(&state);
        printf("drag state :%u\n", state);
        sleep(3);

        robot.RobotEnable(0);
        sleep(3);
        robot.RobotEnable(1);

        robot.Mode(0);
        sleep(1);
        robot.Mode(1);
        
        return 0;
    }
