資料結構說明
================

.. toctree:: 
    :maxdepth: 5

關節位置資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 關節位置資料類型 
    */  
    public class JointPos
    {
      double J1;
      double J2;
      double J3;
      double J4;
      double J5;
      double J6;

      public JointPos(double j1, double j2, double j3, double j4, double j5, double j6)
      {
        J1 = j1;
        J2 = j2;
        J3 = j3;
        J4 = j4;
        J5 = j5;
        J6 = j6;
      }

      public JointPos()
      {

      }
    }

笛卡爾空間位置資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡爾空間位置資料類型
    */
    public class DescTran
    {
      public double x = 0.0;    /* x軸座標，單位mm  */
      public double y = 0.0;    /* y軸座標，單位mm  */
      public double z = 0.0;    /* z軸座標，單位mm  */
      public DescTran(double posX, double posY, double posZ)
      {
        x = posX;
        y = posY;
        z = posZ;
      }

      public DescTran()
      {

      }

    }

歐拉角姿態資料型態
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 歐拉角姿態資料型態
    */
    public class Rpy
    {
      public double rx = 0.0;   /* 繞固定軸X旋轉角度，單位：deg  */
      public double ry = 0.0;   /* 繞固定軸Y旋轉角度，單位：deg  */
      public double rz = 0.0;   /* 繞固定軸Z旋轉角度，單位：deg  */
      public Rpy(double rotateX, double rotateY, double rotateZ)
      {
        rx = rotateX;
        ry = rotateY;
        rz = rotateZ;
      }
    }

笛卡爾空間位姿資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief 笛卡兒空間位姿類型
    */
    public class DescPose
    {
      public DescTran tran = new DescTran(0.0, 0.0, 0.0);      /* 笛卡兒空間位置  */
      public Rpy rpy = new Rpy(0.0, 0.0, 0.0);			       /* 笛卡兒空間姿態  */

      public DescPose()
      {

      }

      public DescPose(DescTran descTran, Rpy rotateRpy)
      {
        tran = descTran;
        rpy = rotateRpy;
      }

      public DescPose(double tranX, double tranY, double tranZ, double rX, double ry, double rz)
      {
        tran.x = tranX;
        tran.y = tranY;
        tran.z = tranZ;
        rpy.rx = rX;
        rpy.ry = ry;
        rpy.rz = rz;
      }

      public String toString()
      {
        return String.valueOf(tran.x) + "," +  String.valueOf(tran.y) + "," +String.valueOf(tran.z) + "," +String.valueOf(rpy.rx) + "," +String.valueOf(rpy.ry) + "," +String.valueOf(rpy.rz);
      }
    }

擴展軸位置資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 擴展軸位置資料類型
    */
    public class ExaxisPos
    {
      public double axis1 = 0.0;
      public double axis2 = 0.0;
      public double axis3 = 0.0;
      public double axis4 = 0.0;

      public ExaxisPos()
      {

      }
      public ExaxisPos(double[] exaxisPos)
      {
        axis1 = exaxisPos[0];
        axis2 = exaxisPos[1];
        axis3 = exaxisPos[2];
        axis4 = exaxisPos[3];
      }

      public ExaxisPos(double pos1, double pos2, double pos3, double pos4)
      {
        axis1 = pos1;
        axis2 = pos2;
        axis3 = pos3;
        axis4 = pos4;
      }
    }

力矩感測器資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力感測器的受力分量和力矩分量
    */
    public class ForceTorque
    {
      public double fx;  /* 沿x軸受力分量，單位N  */
      public double fy;  /* 沿y軸受力分量，單位N  */
      public double fz;  /* 沿z軸受力分量，單位N  */
      public double tx;  /* 绕x軸力矩分量，單位Nm */
      public double ty;  /* 绕y軸力矩分量，單位Nm */
      public double tz;  /* 绕z軸力矩分量，單位Nm */
      public ForceTorque(double fX, double fY, double fZ, double tX, double tY, double tZ)
      {
        fx = fX;
        fy = fY;
        fz = fZ;
        tx = tX;
        ty = tY;
        tz = tZ;
      }
    }

螺旋參數資料類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  螺旋參數資料類型
    */
    public class SpiralParam
    {
      public int circle_num;              /* 螺旋圈數  */
      public double circle_angle;         /* 螺旋傾角  */
      public double rad_init;             /* 螺旋初始半徑，單位mm  */
      public double rad_add;              /* 半徑增量  */
      public double rotaxis_add;          /* 轉軸方向增量  */
      public int rot_direction;           /* 旋轉方向，0-順時針，1-逆時針  */
      public SpiralParam(int circleNum, double circleAngle, double radInit, double radAdd, double rotaxisAdd, int rotDirection)
      {
        circle_num = circleNum;
        circle_angle = circleAngle;
        rad_init = radInit;
        rad_add = radAdd;
        rotaxis_add = rotaxisAdd;
        rot_direction = rotDirection;
      }
    }

擴展軸狀態類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  擴展軸狀態類型
    */
    public class EXT_AXIS_STATUS
    {
     public double pos = 0;        //擴展軸位置
     public double vel = 0;        //擴展軸速度
     public int errorCode = 0;     //擴展軸故障码
     public int ready = 0;        //伺服准备好
     public int inPos = 0;        //伺服到位
     public int alarm = 0;        //伺服报警
     public int flerr = 0;        //跟随误差
     public int nlimit = 0;       //到负限位
     public int pLimit = 0;       //到正限位
     public int mdbsOffLine = 0;  //驅動器485总线掉线
     public int mdbsTimeout = 0;  //控制卡与控制箱485通信超时
     public int homingStatus = 0; //擴展軸回零狀態
    }

感測器類型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  感測器類型
    */
    public class DeviceConfig
    {
      int company = 0;          // 廠商
      int device = 0;           // 類型/設備號
      int softwareVersion = 0;  // 軟體版本
      int bus = 0;              // 掛載位置

      public DeviceConfig()
      {

      }

      public DeviceConfig(int company, int device, int softwareVersion, int bus)
      {
        this.company = company;
        this.device = device;
        this.softwareVersion = softwareVersion;
        this.bus = bus;
      }
    }

485擴展軸配置
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  485擴展軸配置
    */
    public class Axis485Param
    {
      int servoCompany;           // 伺服驅動器廠商，1-戴納泰克
      int servoModel;             // 伺服驅動器型號，1-FD100-750C
      int servoSoftVersion;       // 伺服驅動器軟體版本，1-V1.0
      int servoResolution;        // 編碼器分辨率
      double axisMechTransRatio;  // 機械傳動比

      public Axis485Param(int company, int model, int softVersion, int resolution, double mechTransRatio)
      {
        servoCompany = company;
        servoModel = model;
        servoSoftVersion = softVersion;
        servoResolution = resolution;
        axisMechTransRatio = mechTransRatio;
      }

      public Axis485Param()
      {

      }
    }

伺服控制器狀態
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  伺服控制器狀態
    */
    public class ROBOT_AUX_STATE
    {
      public int servoId = 0;           //伺服驅動器ID号
      public int servoErrCode = 0;       //伺服驅動器故障碼
      public int servoState = 0;         //伺服驅動器狀態
      public double servoPos = 0;        //伺服當前位置
      public float servoVel = 0;         //伺服當前速度
      public float servoTorque = 0;      //伺服當前轉矩    25
    }

焊接中斷狀態
+++++++++++++++++++++++++++
.. versionadded:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
 :linenos:

 /**
 * @brief 焊接中斷狀態
 */
 public class WELDING_BREAKOFF_STATE
 {
 public int breakOffState = 0; //焊接中斷狀態
 public int weldArcState = 0; //焊接電弧中斷狀態
 }

UDP擴展軸通訊參數
++++++++++++++++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  焊接中斷狀態
    */
    public class WELDING_BREAKOFF_STATE
    {
      public String ip = "192.168.58.88";//IP位址
      public int port = 2021;            //埠號
      public int period = 2;             //通訊週期(ms，預設為2，請勿修改此參數)
      public int lossPkgTime = 50;       //封包遺失檢測時間(ms)
      public int lossPkgNum = 2;         //封包遺失次數
      public int disconnectTime = 100;   //通訊斷開確認時長
      public int reconnectEnable = 0;    //通訊斷開自動重連使能 0-不使能 1-使能
      public int reconnectPeriod = 100;  //重連週期間隔(ms)
      public int reconnectNum = 3;       //重連次數
      public int selfConnect =0;         //斷電重啟是否自動建立連接；0-不建立連接；1-建立連接
    }

機器人狀態回饋結構體類型
+++++++++++++++++++++++++++
.. versionchanged:: Java SDK-v1.0.1-3.7.8

.. code-block:: Java
    :linenos:

    /**
    * @brief  機器人狀態回饋結構體類型
    */
    public class ROBOT_STATE_PKG
    {
      public short frame_head = 0;            //幀頭 0x5A5A
      public byte frame_cnt = 0;              //幀計數
      public short data_len = 0;              //數據長度  5
      public int program_state = 0;          //程序運作狀態，1-停止；2-運轉；3-暫停
      public int robot_state = 0;            //機器人運動狀態，1-停止；2-運轉；3-暫停；4-拖曳 7
      public int main_code = 0;               //主故障碼
      public int sub_code = 0;                //子故障碼
      public int robot_mode = 0;             //機器人模式，0-自動模式；1-手動模式 16
      public double[] jt_cur_pos  =new double[6];                  //關節目前位置
      public double[] tl_cur_pos = new double[6];                  //工具當前位姿
      public double[] flange_cur_pos = new double[6];              //末端法蘭目前位姿
      public double[] actual_qd = new double[6];                   //機器人目前關節速度
      public double[] actual_qdd = new double[6];                  //機器人當前關節加速度
      public double[] target_TCP_CmpSpeed = new double[2];         //機器人TCP合成指令速度
      public double[] target_TCP_Speed = new double[6];            //機器人TCP指令速度
      public double[] actual_TCP_CmpSpeed = new double[2];         //機器人TCP合成實際速度
      public double[] actual_TCP_Speed = new double[6];            //機器人TCP實際速度
      public double[] jt_cur_tor = new double[6];                             //當前扭矩
      public int tool = 0;                        //工具號
      public int user = 0;                        //工件號
      public int cl_dgt_output_h = 0;            //數位輸出15-8
      public int cl_dgt_output_l = 0;            //數位輸出7-0
      public int tl_dgt_output_l = 0;            //工具數位輸出7-0(僅bit0-bit1有效)
      public int cl_dgt_input_h = 0;             //數字輸入15-8
      public int cl_dgt_input_l = 0;             //數字輸入7-0
      public int tl_dgt_input_l = 0;             //工具數字輸入7-0(僅bit0-bit1有效)
      public short[] cl_analog_input = new short[2];          //控制箱類比輸入
      public short tl_anglog_input = 0;                       //工具類比輸入
      public double[] ft_sensor_raw_data = new double[6];     //力/扭矩传感器原始數據
      public double[] ft_sensor_data = new double[6];         //參考座標系下力/扭矩传感器數據
      public int ft_sensor_active = 0;           //力/扭力感測器啟動狀態， 0-復位，1-激活
      public int EmergencyStop = 0;              //急停標誌
      public int motion_done = 0;                 //到位訊號
      public int gripper_motiondone = 0;         //夹爪運動完成信号
      public int mc_queue_len = 0;                //運動队列長度
      public int collisionState = 0;             //碰撞检测，1-碰撞；0-無碰撞
      public int trajectory_pnum = 0;             //軌跡點編號
      public int safety_stop0_state = 0;  /* 安全停止訊號SI0 */
      public int safety_stop1_state = 0;  /* 安全停止訊號SI1 */
      public int gripper_fault_id = 0;    /* 錯誤夾爪號 */               // + 19 = 567
      public short gripper_fault = 0;      /* 夾爪故障 */
      public short gripper_active = 0;     /* 夾爪激活狀態 */
      public int gripper_position = 0;    /* 夾爪位置 */
      public int gripper_speed = 0;       /* 夾爪速度 */
      public int gripper_current = 0;     /* 夾爪電流 */
      public int gripper_tmp = 0;          /* 夾爪溫度 */
      public int gripper_voltage = 0;      /* 夾爪電壓 */
      public ROBOT_AUX_STATE auxState = new ROBOT_AUX_STATE(); /* 485擴展軸狀態 */
      public EXT_AXIS_STATUS extAxisStatus0 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus1 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus2 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus3 = new EXT_AXIS_STATUS();
      public short[] extDIState = new short[8];        //擴充DI輸入
      public short[] extDOState = new short[8];        //擴展DO輸出
      public short[] extAIState = new short[4];        //擴展AI輸入
      public short[] extAOState = new short[4];        //擴展AO輸出
      public int rbtEnableState = 0;       //機器人使能狀態--robot enable s
      public double[] jointDriverTorque  =new double[6];       //關節驅動器當前扭矩
      public double[] jointDriverTemperature = new double[6];  //關節驅動器當前溫度
      public ROBOT_TIME robotTime = new ROBOT_TIME();
      public int softwareUpgradeState = 0;   //機器人軟體升級狀態0-空閒或上傳升級包；1~100：升級完成百分比；-1:升級軟體失敗；-2：校驗失敗；-3：版本校驗失敗；-4：解壓縮失敗； -5：使用者配置升級失敗；-6：週邊配置升級失敗；-7：擴展軸配置升級失敗；-8：機器人配置升級失敗；-9：DH參數配置升級失敗
      public int endLuaErrCode;              //末端LUA運行狀態

      public int[] cl_analog_output=new int[2]; //控制箱模擬量輸出
      public int tl_analog_output; //工具類比量輸出
      public float gripperRotNum; //旋轉夾爪目前旋轉圈數
      ublic int gripperRotSpeed; //旋轉夾爪目前旋轉速度百分比
      public int gripperRotTorque; //旋轉夾爪目前旋轉力矩百分比

      public WELDING_BREAKOFF_STATE weldingBreakOffstate=new WELDING_BREAKOFF_STATE();//焊接中斷狀態

      public double[]  jt_tgt_tor=new double[6];    //關節指令力矩
      int smartToolState;         //SmartTool手柄按鈕狀態

      public float wideVoltageCtrlBoxTemp;        //寬電壓控制箱溫度
      public int wideVoltageCtrlBoxFanVel;   //寬電壓控制箱風扇轉速(mA)
      public short check_sum = 0;          /* 和校驗 */

      public ROBOT_STATE_PKG()
      {

      }
    }