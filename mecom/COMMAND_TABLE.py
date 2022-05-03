#COMMANDS_FOR SKRIPTS
COMMAND_TABLE_TEC = {
    "Device Type": [100, ""],
    "Device Hardware Version": [101, ""],
    "Device Serial Number": [102, ""], 
    "Device Firmware Version": [103, ""], 
    "Device Status": [104, ""], 
    "Device Error Number": [105, ""], 
    "Device Error Instance": [106, ""], 
    "Device Error Parameter": [107, ""], 
    "Device Save Data to Flash": [108, ""], 
    "Device Flash Status": [109, ""], 
    
    "Object Temperature": [1000, "degC"], 
    "Sink Temperature": [1001, "degC"], 
    
    "Target Object Temperature": [1010, "degC"], 
    "Ramp Object Temperature": [1011, "degC"], 
    "Thermal Power Model Current": [1012, "A"], 
    
    "Actual Output Current": [1090, "A"], 
    "Actual Output Voltage": [1021, "V"],
    
    "Relative Cooling Power": [1100, "%"], 
    "Nominal Fan Speed": [1101, "rpm"], 
    "Actual Fan Speed": [1102, "rpm"], 
    "Fan PWM Level": [1103, "%"],
    
    "PID Lower Limitation": [1030, "%"], 
    "PID Upper Limitation": [1031, "%"], 
    "PID Control Variable": [1032, "%"],
    
    "Object Sensor ADC Value": [1040, ""], 
    "Object Differential Voltage": [1046, "V"], 
    "Object Sensor Resistance": [1042, "Ohm"], 
    "Object Sensor Temperature": [1045, "degC"], 
    "Sink Sensor Raw ADC Value ": [1041, ""], 
    "Sink Sensor Resistance": [1043, "Ohm"], 
    "Sink Sensor Temperature": [1044, "degC"],
    
    "Firmware Version": [1050, ""], 
    "Firmware Build Number": [1051, ""], 
    "Min Version for Firmware Downgrade": [1054, ""], 
    "Hardware Version": [1052, ""], 
    "Serial Number": [1053, ""],
    
    "Driver Input Voltage": [1060, "V"], 
    "Medium Internal Supply": [1061, "V"], 
    "3.3V Internal Supply": [1062, "V"], 
    "Device Temperature": [1063, "degC"],
    
    "Maximum Device Temperature": [1110, "degC"], 
    "Maximum Output Current": [1111, "A"],
    
    "Error Number": [1070, ""], 
    "Error Instance": [1071, ""], 
    "Error Parameter": [1072, ""], 
    
    "Driver Status": [1080, ""], 
    "Parameter System: Flash Status": [1081, ""], 
    
    "Temperature is Stable": [1200, ""], 
    
    "Input Selection": [2000, ""], 
    
    "Status": [2010, ""], 
    
    "Set Current": [2020, "A"], 
    "Set Voltage": [2021, "V"], 
    "Current Limitation": [2030, "A"], 
    "Voltage Limitation": [2031, "V"], 
    "Current Error Threshold": [2032, "A"], 
    "Voltage Error Threshold": [2033, "V"],
    
    "General Operating Mode": [2040, ""],
    
    "Device Address": [2051, ""], 
    
    "Base Boud Rate": [2050, ""], 
    "Response Delay": [2052, "us"], 
    
    "Timeout": [2060, "s"], 
    
    "Target Object Temp (Set)": [3000, "RNG_TEMP"], 
    "NomTemp Coarse Temp Ramp": [3003, "degC/s"], 
    "NomTempProximity Width": [3002, "degC"], 
    
    "TempControl Kp": [3010, "degC"], 
    "TempControl Ti": [3011, "s"], 
    "TempControl Td": [3012, "s"], 
    "D Part Damping PT1": [3013, ""],
    
    "ModeThermPowerReg Mode": [3020, ""], 
    
    "Maximal Current Imax": [3030, "A"], 
    "Data Temperature dTmax": [3033, "degC"], 
    "Positive Current is": [3034, ""],
    
    "Resistance": [3040, "Ohm"], 
    "Maximal Current": [3041, "A"], 
    
    "Upper Boundary": [3051, "RNG_TEMP"], 
    "Lower Boundary": [3050, "RNG_TEMP"], 
    
    "ObjMeasSettings Temperature Offset": [4001, "degC"], 
    "ObjMeasSettings Temperature Gain": [4002, "degC"],
    
    "ActObjObjErrLimit Upper Error Threshold": [4011, "RNG_TEMP"], 
    "ActObjObjErrLimit Lower Error Threshold": [4010, "RNG_TEMP"], 
    "ActObjObjErrLimit Max Temp Change": [4012, "degC/s"],
    
    "Temperature Deviation": [4040, "degC"], 
    "Min Time in Window": [4041, "s"], 
    "Max Stabilization Time": [4042, "s"],
    
    "Highest Voltage": [4035, "V"], 
    "Lowest Voltage": [4036, "V"], 
    "ObjTempMeasLim Lowest Resistance" : [4030, "Ohm"], 
    "ObjTempMeasLim Highest Resistance": [4031, "Ohm"], 
    "ObjTempLim Temperature at Lowest Resistance": [4032, "degC"], 
    "ObjTempLim Temperature at Highest Resistance": [4033, "degC"], 
    "Object Sensor Type": [4034, ""], 
     
    "Temperature Offset": [5001, "Ohm"], 
    "Temperature Gain": [5002, "Ohm"], 
    
    "Upper Error Threshold": [5011, "RNG_TEMP"], 
    "Lower Error Threshold": [5010, "RNG_TEMP"], 
    "Max Temp Change": [5012, "degC/s"], 
    
    "SinkTempMeasLim Lowest Resistance": [5040, "Ohm"], 
    "SinkTempMeasLim Highest Resistance": [5041, "Ohm"], 
    "SinkTempMeasLim Temperature at Lowest Resistance": [5042, "degC"], 
    "SinkTempMeasLim Temperature at Highest Resistance": [5043, "degC"],
    
    "Sink Temperature Selection": [5030, ""], 
    "Fixed Temperature": [5031, "RNG_TEMP"], 
    "Upper ADC Limit Error": [5032, ""], 
    
    "Auto Tuning Start": [51000, ""], 
    "Auto Tuning Cancel": [51001, ""], 
    "Thermal Model Speed": [51002, ""], 
    "Tuning Parameter 2A (Temp peak-peak)": [51010, "degC"], 
    "Tuning Parameter 2D (Var peak-peak)": [51011, "%"], 
    "Tuning Parameter Ku (ult. Gain)": [51012, "%/degC"], 
    "Tuning Parameter Tu (ult. period)": [51013, "s"], 
    "PID Parameter Kp": [51014, "%/degC"], 
    "PID Parameter Ti": [51015, "s"], 
    "PID Parameter Td": [51016, "s"], 
    "Coarse Temp Ramp": [51017, "degC/s"], 
    "Proximity Width": [51018, "degC"], 
    "Kp": [6222, ""], 
    "Ti": [6223, ""], 
    "Td": [6224, ""], 
    "Slow PI Parameter Kp": [51022, "%/degC"], 
    "Slow PI Parameter Ti": [51023, "s"], 
    "PID D Part Damping PT1 Recommendation": [51024, ""], 
    "Tuning Status": [51020, ""], 
    "Tuning Progress": [51021, "%"], 
    "PGA Gain": [6000, ""], 
    "PGA Bypass": [6007, ""], 
    "Current Source": [6001, ""], 
    "Current Source 2 Out": [6008, ""], 
    "Measurement Type": [6009, ""], 
    "ADC Rs": [6002, "Ohm"], 
    "ADC Rp": [6006, "Ohm"], 
    "ADC Calibration Offset": [6003, "degC"], 
    "ADC Calibration Gain": [6004, "degC"],
    
    "ADV Rv": [6010, "Ohm"], 
    "ADV vps": [6013, "V"], 
    "ADV Calibration Offset": [6011, "degC"], 
    "ADV Calibration Gain": [6012, "degC"], 
    "Sensor Type Selection": [6005, ""], 
    
    "NTCSensorChar Upper Point: Temperature": [4024, "RNG_TEMP"], 
    "NTCSensorChar Upper Point: Resistance": [4025, "Ohm"], 
    "NTCSensorChar Middle Point: Temperature": [4022, "RNG_TEMP"], 
    "NTCSensorChar Middle Point: Resistance": [4023, "Ohm"], 
    "NTCSensorChar Lower Point: Temperature": [4020, "RNG_TEMP"], 
    "NTCSensorChar Lower Point: Resistance": [4021, "Ohm"], 
    
    "SinkNTCSensorChar Upper Point: Temperature": [5024, "RNG_TEMP"], 
    "SinkNTCSensorChar Upper Point: Resistance": [5025, "Ohm"], 
    "SinkNTCSensorChar Middle Point: Temperature": [5022, "RNG_TEMP"], 
    "SinkNTCSensorChar Middle Point: Resistance": [5023, "Ohm"], 
    "SinkNTCSensorChar Lower Point: Temperature": [5020, "RNG_TEMP"], 
    "SinkNTCSensorChar Lower Point: Resistance": [5021, "Ohm"], 
    
    "Reference Temperature": [6400, "RNG_TEMP"], 
    "Reference Voltage": [6401, "V"], 
    "Temperature Slope": [6402, "V/degC"], 
    
    "Self-Check Period": [6050, "s"], 
    "Self-Chek Trigger": [6051, ""], 
    "IRs Error Enable": [6052, ""], 
    
    "AVDD": [6053, "V"], 
    "IRs": [6054, "I"], 
    "VRef": [6055, "V"],
    
    "Lookup Table Start": [52000, ""], 
    "Lookup Table Stop": [52001, ""], 
    "Lookup Table Status": [52002, ""], 
    "Lookup Table Status Current Table Line": [52003, ""], 
    "Lookup Table ID Selection": [52010, ""], 
    "Number of Repetitions": [52012, ""],
    
    "Display Type": [6020, ""], 
    "Display Line 1-4 Alternative Mode": [6023, ""], 
    "Display Line 1-4 default Text": [6024, ""], 
    "Display Line 1-4 Alternative Text": [6025, ""], 
    "Display Line 1-4 Startup Text": [6026, ""], 
    
    "GPIO Function": [6100, ""], 
    "GPIO Level Assignment": [6101, ""], 
    "GPIO Hardware Configuration": [6102, ""], 
    "GPIO Channel": [6103, ""], 
    
    "Upper Temperature Limit": [6111, "RNG_TEMP"], 
    "Lower Temperature Limit": [6110, "RNG_TEMP"], 
    "Step Size": [6112, "RNG_TEMP"], 
    
    "PumpContorl Actual Temperature Source": [6120, ""], 
    "ON Threshold": [6121, "RNG_TEMP"], 
    "OFF Threshold": [6122, "RNG_TEMP"]
    , 
    "Temperature 1": [6130, "RNG_TEMP"], 
    "Temperature 2": [6131, "RNG_TEMP"], 
    "Temperature 3": [6132, "RNG_TEMP"],
    
    "Fan Control Enable": [6200, ""],
    
    "Actual Temperature Source": [6210, ""], 
    "Target Temperature": [6211, "RNG_TEMP"],
    "FanTempController Kp": [6212, "%/degC"],
    "FanTempController Ti": [6213, "s"], 
    "FanTempContorller Td": [6214, "s"], 


    "Fan Speed 0": [6220, ""], 
    "Fan Speed 100": [6221, ""], 
    "Fan Min Speed Start": [6227, ""], 
    "Fan Min Speed Stop": [6228, ""],
    "FanSpeedController Kp": [6222, "%/degC"], 
    "FanSpeedController Ti": [6223, "s"], 
    "FanSpeedController Td": [6224, "s"], 
    "Bypassing Speed Conroller": [6225, ""], 
    "Fan Surveillance": [6226, ""], 

    "Fan PWM Frequency": [6230, ""], 

    "Source Selection": [6300, ""], 
    "Control Speed": [6301, ""], 
    "Observe Mode": [6302, ""], 
    
    "Delay till Restart": [6310, ""], 
    
    "Error Delay": [6320, ""], 
    
    "Mode": [6330, ""],
    
    "Live Enable": [50000, ""], 
    "Live Set Current": [50001, "A"], 
    "Live Set Voltage": [50002, "V"], 
    "Sine Ramp Start Point": [50010, ""], 
    "Object Target Temperature Source Selection": [50011, ""], 
    "Object Target Temperature": [50012, "RNG_TEMP"], 
    
    "Enable Function": [52100, ""], 
    "Set Output to Push-Pull": [52101, ""], 
    "Set Output States": [52102, ""], 
    "Read Input States": [52103, ""], 
    
    "External Object Temperature": [52200, "RNG_TEMP"]
}


COMMAND_TABLE_LDD = {
    "Device Identification Type": [100, ""], 
    "Device  Identification Hardware Version": [101, ""], 
    "Device  IdentificationSerial Number": [102, ""], 
    "Device  IdentificationFirmware Version": [103, ""], 
    "Device  IdentificationStatus": [104, ""], 
    "Device  IdentificationError Number": [105, ""], 
    "Device  IdentificationError Instance": [106, ""], 
    "Device  IdentificationError Parameter": [107, ""], 
    "Device  IdentificationSave Data to Flash": [108, ""], 
    "Device  IdentificationFlash Status": [109, ""], 
    
    "Device Type": [1000, ""], 
    "Serial Number": [1001, ""], 
    "Harware Version": [1002, ""], 
    "Firmware Version [STM32]": [1003, ""], 
    "Firmware Build Number": [1004, ""], 
    "FPGA Version": [1005, ""], 
    
    "Laser Diode Current": [1016, "A"], 
    "Laser Diode Voltage": [1017, "V"], 
    "Laser Diode Temperature": [1015, "degC"],
    
    "Photo Diode Current": [1060, "A"], 
    "Laer Power": [1061, "W"],
    
    "Laser Diode Current CW": [1011, "A"], 
    "Laser Diode Current Actual": [1010, "A"], 
    "Laser Diode Voltage Actual": [1013, "V"], 
    "Laser Diode Current Pulse": [1012, "A"], 
    "Laser Diode Voltage Pulse": [1014, "V"],
    
    "Driver Input Voltage": [1020, "V"], 
    "Medium Internal Supply": [1021, "V"], 
    "3.3V Internal Supply": [1022, "V"], 
    "1.2V Internal Supply": [1023, "V"],
    
    "Error Number": [1030, ""], 
    "Error Instance": [1031, ""], 
    "Error Parameter": [1032, ""], 
    
    "Buck Converter 1 Current": [1040, "A"], 
    "Buck Converter 2 Currnet": [1041, "A"], 
    "Buck Converter 3 Current": [1042, "A"], 
    "Base Plate Temperature": [1043, "degC"],
    
    "Driver Status": [1050, ""], 
    "Parameter System: Flash Status": [1051, ""], 
    
    "Input Source": [2020, ""], 
    "Current CW": [2001, "A"], 
    "Current High": [2002, "A"], 
    "Current Low": [2003, "A"], 
    "High Time": [2011, "s"], 
    "Low Time": [2012, "s"], 
    "Rise Time": [2006, "s"], 
    "Fall Time": [2007, "s"], 
    "Generator Trigger": [2008, ""],
    
    "PulseSettings Input Source": [2010, ""],
    "PulseSettings High Time": [2011, "s"],
    "PulseSettings Low Time": [2012, "s"],
    
    "EnableSettings Input Source": [2020, ""],
    
    "LP Input Source" : [5000, ""],
    "LP CW": [5001, "W"], 
    "LP High": [5002, "W"], 
    "LP Low": [5003, "W"], 
    "LP High Time": [5004, "s"], 
    "LP Low Time": [5005, "s"], 
    "LP Rise Time": [5006, "s"], 
    "LP Fall Time": [5007, "s"], 
    
    "PID LP Kp" : [5010, "A/W"],
    "PID LP Ti" : [5011, "s"],
    "PID LP Td" : [5012, "s"],
    "Slope Limit": [5013, "W/us"],
    
    "Current Limiter Start Value": [5020, "A"], 
    "Current Limiter Ramp": [5021, "us"],
    
    "LP System Scale": [5030, "A/W"], 
    
    
    "Kp": [3000, "%/A"], 
    "Ti": [3001, "s"], 
    "Td": [3002, "s"], 
    
    "Current Factor": [3010, "A/V"], 
    
    "Current Limit Max [A]": [3020, "A"], 
    "Current Limit Min [A]": [3021, "A"], 
    "Max Current Error [A]": [3022, "A"], 
    "Slope Limit [A/us]": [3023, "A/us"],
    
    "Hardware PIN": [3080, ""], 
    
    "Communication Watchdog": [3030, "s"], 
    
    "Device Address": [3040, ""], 
    
    "Baud Rate": [3050, "Bits/s"], 
    "Response Delay ": [3051, "us"],
    
    "Lower Error Threshold": [3060, "degC"], 
    "Upper Error Threshold": [3061, "degC"],
    
    "Lower Point Temperature": [3070, "degC"], 
    "Lower Point Resistance": [3071, "Ohm"], 
    "Middle Point Temperature": [3072, "degC"], 
    "Middle Point Resistance": [3073, "Ohm"], 
    "Upper Point Temperature": [3074, "degC"], 
    "Upper Point Resistance": [3075, "Ohm"],
    
    "ADC Calibration Offset": [4000, ""], 
    "ADC Calibration Gain": [4001, ""], 
    "ADC Rv": [4002, "Ohm"], 
    "Temperature Offset": [4003, "degC"], 
    "Temperature Gain": [4004, "degC/degC"],
    
    "Measurement Rs": [4010, "Ohm"], 
    "Current Offset": [4020, "A"], 
    "Current Gain": [4021, "A/A"], 
    
    "LP Offset": [4030, "W"],
    "LP Gain": [4031, "W/W"],
    
    "Parallel Function/Type": [4100, ""], 
    "RS485 Sync. Channel": [4101, ""], 
    "Master: Number of Slaves": [4102, ""], 
    "Slave: Slave ID": [4103, ""]
}
