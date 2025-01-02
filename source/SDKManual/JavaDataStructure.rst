数据结构说明
================

.. toctree:: 
    :maxdepth: 5

关节位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /** 
    * @brief 关节位置数据类型 
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

笛卡尔空间位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 笛卡尔空间位置数据类型
    */
    public class DescTran
    {
      public double x = 0.0;    /* x轴坐标，单位mm  */
      public double y = 0.0;    /* y轴坐标，单位mm  */
      public double z = 0.0;    /* z轴坐标，单位mm  */
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

欧拉角姿态数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 欧拉角姿态数据类型
    */
    public class Rpy
    {
      public double rx = 0.0;   /* 绕固定轴X旋转角度，单位：deg  */
      public double ry = 0.0;   /* 绕固定轴Y旋转角度，单位：deg  */
      public double rz = 0.0;   /* 绕固定轴Z旋转角度，单位：deg  */
      public Rpy(double rotateX, double rotateY, double rotateZ)
      {
        rx = rotateX;
        ry = rotateY;
        rz = rotateZ;
      }
    }

笛卡尔空间位姿数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    *@brief 笛卡尔空间位姿类型
    */
    public class DescPose
    {
      public DescTran tran = new DescTran(0.0, 0.0, 0.0);      /* 笛卡尔空间位置  */
      public Rpy rpy = new Rpy(0.0, 0.0, 0.0);			       /* 笛卡尔空间姿态  */

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

扩展轴位置数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 扩展轴位置数据类型
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

力矩传感器数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief 力传感器的受力分量和力矩分量
    */
    public class ForceTorque
    {
      public double fx;  /* 沿x轴受力分量，单位N  */
      public double fy;  /* 沿y轴受力分量，单位N  */
      public double fz;  /* 沿z轴受力分量，单位N  */
      public double tx;  /* 绕x轴力矩分量，单位Nm */
      public double ty;  /* 绕y轴力矩分量，单位Nm */
      public double tz;  /* 绕z轴力矩分量，单位Nm */
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

螺旋参数数据类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  螺旋参数数据类型
    */
    public class SpiralParam
    {
      public int circle_num;              /* 螺旋圈数  */
      public double circle_angle;         /* 螺旋倾角  */
      public double rad_init;             /* 螺旋初始半径，单位mm  */
      public double rad_add;              /* 半径增量  */
      public double rotaxis_add;          /* 转轴方向增量  */
      public int rot_direction;           /* 旋转方向，0-顺时针，1-逆时针  */
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

扩展轴状态类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  扩展轴状态类型
    */
    public class EXT_AXIS_STATUS
    {
     public double pos = 0;        //扩展轴位置
     public double vel = 0;        //扩展轴速度
     public int errorCode = 0;     //扩展轴故障码
     public int ready = 0;        //伺服准备好
     public int inPos = 0;        //伺服到位
     public int alarm = 0;        //伺服报警
     public int flerr = 0;        //跟随误差
     public int nlimit = 0;       //到负限位
     public int pLimit = 0;       //到正限位
     public int mdbsOffLine = 0;  //驱动器485总线掉线
     public int mdbsTimeout = 0;  //控制卡与控制箱485通信超时
     public int homingStatus = 0; //扩展轴回零状态
    }

传感器类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  传感器类型
    */
    public class DeviceConfig
    {
      int company = 0;          // 厂商
      int device = 0;           // 类型/设备号
      int softwareVersion = 0;  // 软件版本
      int bus = 0;              // 挂载位置

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

485扩展轴配置
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  485扩展轴配置
    */
    public class Axis485Param
    {
      int servoCompany;           // 伺服驱动器厂商，1-戴纳泰克
      int servoModel;             // 伺服驱动器型号，1-FD100-750C
      int servoSoftVersion;       // 伺服驱动器软件版本，1-V1.0
      int servoResolution;        // 编码器分辨率
      double axisMechTransRatio;  // 机械传动比

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

伺服控制器状态
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  伺服控制器状态
    */
    public class ROBOT_AUX_STATE
    {
      public int servoId = 0;           //伺服驱动器ID号
      public int servoErrCode = 0;       //伺服驱动器故障码
      public int servoState = 0;         //伺服驱动器状态
      public double servoPos = 0;        //伺服当前位置
      public float servoVel = 0;         //伺服当前速度
      public float servoTorque = 0;      //伺服当前转矩    25
    }

机器人状态反馈结构体类型
+++++++++++++++++++++++++++
.. code-block:: Java
    :linenos:

    /**
    * @brief  机器人状态反馈结构体类型
    */
    public class ROBOT_STATE_PKG
    {
      public short frame_head = 0;            //帧头 0x5A5A
      public byte frame_cnt = 0;              //帧计数
      public short data_len = 0;              //数据长度  5
      public int program_state = 0;          //程序运行状态，1-停止；2-运行；3-暂停
      public int robot_state = 0;            //机器人运动状态，1-停止；2-运行；3-暂停；4-拖动  7
      public int main_code = 0;               //主故障码
      public int sub_code = 0;                //子故障码
      public int robot_mode = 0;             //机器人模式，0-自动模式；1-手动模式 16
      public double[] jt_cur_pos  =new double[6];                  //关节当前位置
      public double[] tl_cur_pos = new double[6];                  //工具当前位姿
      public double[] flange_cur_pos = new double[6];              //末端法兰当前位姿
      public double[] actual_qd = new double[6];                   //机器人当前关节速度
      public double[] actual_qdd = new double[6];                  //机器人当前关节加速度
      public double[] target_TCP_CmpSpeed = new double[2];         //机器人TCP合成指令速度
      public double[] target_TCP_Speed = new double[6];            //机器人TCP指令速度
      public double[] actual_TCP_CmpSpeed = new double[2];         //机器人TCP合成实际速度
      public double[] actual_TCP_Speed = new double[6];            //机器人TCP实际速度
      public double[] jt_cur_tor = new double[6];                             //当前扭矩
      public int tool = 0;                        //工具号
      public int user = 0;                        //工件号
      public int cl_dgt_output_h = 0;            //数字输出15-8
      public int cl_dgt_output_l = 0;            //数字输出7-0
      public int tl_dgt_output_l = 0;            //工具数字输出7-0(仅bit0-bit1有效)
      public int cl_dgt_input_h = 0;             //数字输入15-8
      public int cl_dgt_input_l = 0;             //数字输入7-0
      public int tl_dgt_input_l = 0;             //工具数字输入7-0(仅bit0-bit1有效)
      public short[] cl_analog_input = new short[2];          //控制箱模拟量输入
      public short tl_anglog_input = 0;                       //工具模拟量输入
      public double[] ft_sensor_raw_data = new double[6];     //力/扭矩传感器原始数据
      public double[] ft_sensor_data = new double[6];         //参考坐标系下力/扭矩传感器数据
      public int ft_sensor_active = 0;           //力/扭矩传感器激活状态， 0-复位，1-激活
      public int EmergencyStop = 0;              //急停标志
      public int motion_done = 0;                 //到位信号
      public int gripper_motiondone = 0;         //夹爪运动完成信号
      public int mc_queue_len = 0;                //运动队列长度
      public int collisionState = 0;             //碰撞检测，1-碰撞；0-无碰撞
      public int trajectory_pnum = 0;             //轨迹点编号
      public int safety_stop0_state = 0;  /* 安全停止信号SI0 */
      public int safety_stop1_state = 0;  /* 安全停止信号SI1 */
      public int gripper_fault_id = 0;    /* 错误夹爪号 */               // + 19 = 567
      public short gripper_fault = 0;      /* 夹爪故障 */
      public short gripper_active = 0;     /* 夹爪激活状态 */
      public int gripper_position = 0;    /* 夹爪位置 */
      public int gripper_speed = 0;       /* 夹爪速度 */
      public int gripper_current = 0;     /* 夹爪电流 */
      public int gripper_tmp = 0;          /* 夹爪温度 */
      public int gripper_voltage = 0;      /* 夹爪电压 */
      public ROBOT_AUX_STATE auxState = new ROBOT_AUX_STATE(); /* 485扩展轴状态 */
      public EXT_AXIS_STATUS extAxisStatus0 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus1 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus2 = new EXT_AXIS_STATUS();
      public EXT_AXIS_STATUS extAxisStatus3 = new EXT_AXIS_STATUS();
      public short[] extDIState = new short[8];        //扩展DI输入
      public short[] extDOState = new short[8];        //扩展DO输出
      public short[] extAIState = new short[4];        //扩展AI输入
      public short[] extAOState = new short[4];        //扩展AO输出
      public int rbtEnableState = 0;       //机器人使能状态--robot enable s
      public double[] jointDriverTorque  =new double[6];       //关节驱动器当前扭矩
      public double[] jointDriverTemperature = new double[6];  //关节驱动器当前温度
      public ROBOT_TIME robotTime = new ROBOT_TIME();
      public int softwareUpgradeState = 0;   //机器人软件升级状态 0-空闲中或上传升级包中；1~100：升级完成百分比；-1:升级软件失败；-2：校验失败；-3：版本校验失败；-4：解压失败；-5：用户配置升级失败；-6：外设配置升级失败；-7：扩展轴配置升级失败；-8：机器人配置升级失败；-9：DH参数配置升级失败
      public int endLuaErrCode;              //末端LUA运行状态
      public short check_sum = 0;          /* 和校验 */

      public ROBOT_STATE_PKG()
      {

      }
    }