"""
Definitions of command and error codes as stated in the "Mecom" protocol standard.
https://www.meerstetter.ch/category/35-latest-communication-protocols
"""

# {"id": , "name": "", "format": ""},

TEC_PARAMETERS = [
    
    #Common Product Parameters
    #Device Identification
    {"id": 100, "name": "Device Type", "format": "INT32"},
    {"id": 101, "name": "Device Hardware Version", "format": "INT32"},
    {"id": 102, "name": "Device Serial Number", "format": "INT32"},
    {"id": 103, "name": "Device Firmware Version", "format": "INT32"},
    {"id": 104, "name": "Device Status", "format": "INT32"},
    {"id": 105, "name": "Device Error Number", "format": "INT32"},
    {"id": 106, "name": "Device Error Instance", "format": "INT32"},
    {"id": 107, "name": "Device Error Parameter", "format": "INT32"},
    {"id": 108, "name": "Device Save Data to Flash", "format": "INT32"},
    {"id": 109, "name": "Device Flash Status", "format": "INT32"},
    
    #Monitor 
    #CHx Temperature Measurement
    {"id": 1000, "name": "Object Temperature", "format": "FLOAT32"},
    {"id": 1001, "name": "Sink Temperature", "format": "FLOAT32"},
    
    #CHx Temperature Control
    {"id": 1010, "name": "Target Object Temperature", "format": "FLOAT32"},
    {"id": 1011, "name": "Ramp Object Temperature", "format": "FLOAT32"},
    {"id": 1012, "name": "Thermal Power Model Current", "format": "FLOAT32"},

    #CHx Output Stage Monitoring    
    {"id": 1020, "name": "Actual Output Current", "format": "FLOAT32"},
    {"id": 1021, "name": "Actual Output Voltage", "format": "FLOAT32"},
    
    #CHx Fan Controller
    {"id": 1100, "name": "Relative Cooling Power", "format": "FLOAT32"},
    {"id": 1101, "name": "Nominal Fan Speed", "format": "FLOAT32"},
    {"id": 1102, "name": "Actual Fan Speed", "format": "FLOAT32"},
    {"id": 1103, "name": "Fan PWM Level", "format": "FLOAT32"},
    
    #CHx Temperature Controller PID Status
    {"id": 1030, "name": "PID Lower Limitation", "format": "FLOAT32"},
    {"id": 1031, "name": "PID Upper Limitation", "format": "FLOAT32"},
    {"id": 1032, "name": "PID Control Variable", "format": "FLOAT32"},
    
    #CHx Temperature Measurement
    {"id": 1040, "name": "Object Sensor ADC Value", "format": "FLOAT32"},
    {"id": 1046, "name": "Object Differential Voltage", "format": "FLOAT32"},
    {"id": 1042, "name": "Object Sensor Resistance", "format": "FLOAT32"},
    {"id": 1045, "name": "Object Sensor Temperature", "format": "FLOAT32"},
    {"id": 1041, "name": "Sink Sensor Raw ADC Value ", "format": "FLOAT32"},
    {"id": 1043, "name": "Sink Sensor Resistance", "format": "FLOAT32"},
    {"id": 1044, "name": "Sink Sensor Temperature", "format": "FLOAT32"},
    
    #Firmware and Hardware Verion
    {"id": 1050, "name": "Firmware Version", "format": "INT32"},
    {"id": 1051, "name": "Firmware Build Number", "format": "INT32"},
    {"id": 1054, "name": "Min Version for Firmware Downgrade", "format": "INT32"},
    {"id": 1052, "name": "Hardware Version", "format": "INT32"},
    {"id": 1053, "name": "Serial Number", "format": "INT32"},
    
    #Power Supplies and Temperature
    {"id": 1060, "name": "Driver Input Voltage", "format": "FLOAT32"},
    {"id": 1061, "name": "Medium Internal Supply", "format": "FLOAT32"},
    {"id": 1062, "name": "3.3V Internal Supply", "format": "FLOAT32"},
    {"id": 1063, "name": "Device Temperature", "format": "FLOAT32"},
    
    #Device Temperature Mode (Standart or Extended)
    {"id": 1110, "name": "Maximum Device Temperature", "format": "FLOAT32"},
    {"id": 1111, "name": "Maximum Output Current", "format": "FLOAT32"},
    
    #Parallel Output Stage Monitoring (Common Load)
    {"id": 1090, "name": "Actual Output Current", "format": "FLOAT32"},
    
    #Error Status
    {"id": 1070, "name": "Error Number", "format": "INT32"},
    {"id": 1071, "name": "Error Instance", "format": "INT32"},
    {"id": 1072, "name": "Error Parameter", "format": "INT32"},
    
    #Driver Status
    {"id": 1080, "name": "Driver Status", "format": "INT32"},
    {"id": 1081, "name": "Parameter System: Flash Status", "format": "INT32"},
    
    #Object Temperature Stability Detection
    {"id": 1200, "name": "Temperature is Stable", "format": "INT32"},

    #Operation
    #CHx Output Stage Control Input Selection
    {"id": 2000, "name": "Input Selection", "format": "INT32"},
    
    #CHx Output Stage Enable
    {"id": 2010, "name": "Status", "format": "INT32"},
    
    #CHx Output Stage 'Static Current/Voltage' Control Values
    {"id": 2020, "name": "Set Current", "format": "FLOAT32"},
    {"id": 2021, "name": "Set Voltage", "format": "FLOAT32"},
    
    #CHx Output Stage Limits
    {"id": 2030, "name": "Current Limitation", "format": "FLOAT32"},
    {"id": 2031, "name": "Voltage Limitation", "format": "FLOAT32"},
    {"id": 2032, "name": "Current Error Threshold", "format": "FLOAT32"},
    {"id": 2033, "name": "Voltage Error Threshold", "format": "FLOAT32"},
    
    #General Operating Mode
    {"id": 2040, "name": "General Operating Mode", "format": "INT32"},
    
    #Device Address
    {"id": 2051, "name": "Device Address", "format": "INT32"},
    
    #UART Interface Settings
    {"id": 2050, "name": "Base Boud Rate", "format": "INT32"},
    {"id": 2052, "name": "Response Delay", "format": "INT32"},
    
    #Communication Watchdog 
    {"id": 2060, "name": "Timeout", "format": "FLOAT32"},
    
    #CHx Nominal Temperature
    {"id": 3000, "name": "Target Object Temp (Set)", "format": "FLOAT32"},
    {"id": 3003, "name": "Coarse Temp Ramp", "format": "FLOAT32"},
    {"id": 3002, "name": "Proximity Width", "format": "FLOAT32"},
    
    #CHx Temperature Controller PID Values
    {"id": 3010, "name": "Kp", "format": "FLOAT32"},
    {"id": 3011, "name": "Ti", "format": "FLOAT32"},
    {"id": 3012, "name": "Td", "format": "FLOAT32"},
    {"id": 3013, "name": "D Part Damping PT1", "format": "FLOAT32"},
    
    #CHx Modelization for Thermal Power Regulation
    {"id": 3020, "name": "Mode", "format": "INT32"},
    
    #CHx Peltier Characteristics
    {"id": 3030, "name": "Maximal Current Imax", "format": "FLOAT32"},
    {"id": 3033, "name": "Data Temperature dTmax", "format": "FLOAT32"},
    {"id": 3034, "name": "Positive Current is", "format": "INT32"},

    #Chx Resistor Characteristics
    {"id": 3040, "name": "Resistance", "format": "FLOAT32"},
    {"id": 3041, "name": "Maximal Current", "format": "FLOAT32"},
    
    #CHx Peltier, Heat Only - Cool Only Boundaries
    {"id": 3051, "name": "Upper Boundary", "format": "FLOAT32"},
    {"id": 3050, "name": "Lower Boundary", "format": "FLOAT32"},
    
    #Object Temperature 
    #Chx Object Measurement Settings
    {"id": 4001, "name": "Temperature Offset", "format": "FLOAT32"},
    {"id": 4002, "name": "Temperature Gain", "format": "FLOAT32"},

    #CHx Actual Object Temperature Error Limits
    {"id": 4011, "name": "Upper Error Threshold", "format": "FLOAT32"},
    {"id": 4010, "name": "Lower Error Threshold", "format": "FLOAT32"},
    {"id": 4012, "name": "Max Temp Change", "format": "FLOAT32"},
    
    #CHx Object Temperature Stability Indicator Settings 
    {"id": 4040, "name": "Temperature Deviation", "format": "FLOAT32"},
    {"id": 4041, "name": "Min Time in Window", "format": "FLOAT32"},
    {"id": 4042, "name": "Max Stabilization Time", "format": "FLOAT32"},
    
    #CHx Object Temperature Measurement Limits (Read Only)
    {"id": 4035, "name": "Highest Voltage", "format": "FLOAT32"},
    {"id": 4036, "name": "Lowest Voltage", "format": "FLOAT32"},
    {"id": 4030, "name": "Lowest Resistance", "format": "FLOAT32"},
    {"id": 4031, "name": "Highest Resistance", "format": "FLOAT32"},
    {"id": 4032, "name": "Temperature at Lowest Resistance", "format": "FLOAT32"},
    {"id": 4033, "name": "Temperature at Highest Resistance", "format": "FLOAT32"},
    {"id": 4034, "name": "Object Sensor Type", "format": "INT32"},
    
    #Sink Temperature
    #CHx Sink Measurement Settings
    {"id": 5001, "name": "Temperature Offset", "format": "FLOAT32"},
    {"id": 5002, "name": "Temperature Gain", "format": "FLOAT32"},
    
    #CHx Actual Sink Temperature Error Limits
    {"id": 5011, "name": "Upper Error Threshold", "format": "FLOAT32"},
    {"id": 5010, "name": "Lower Error Threshold", "format": "FLOAT32"},
    {"id": 5012, "name": "Max Temp Change", "format": "FLOAT32"},
    
    #CHx Sink Temperature General
    {"id": 5030, "name": "Sink Temperature Selection", "format": "INT32"},
    {"id": 5031, "name": "Fixed Temperature", "format": "FLOAT32"},
    {"id": 5032, "name": "Upper ADC Limit Error", "format": "INT32"},
    
    #CHx Sink Temperature Measurement Limits (Read Only)
    {"id": 5040, "name": "Lowest Resistance", "format": "FLOAT32"},
    {"id": 5041, "name": "Highest Resistance", "format": "FLOAT32"},
    {"id": 5042, "name": "Temperature at Lowest Resistance", "format": "FLOAT32"},
    {"id": 5043, "name": "Temperature at Highest Resistance", "format": "FLOAT32"},
    
    
    #Auto Tuning
    {"id": 51000, "name": "Auto Tuning Start", "format": "INT32"},
    {"id": 51001, "name": "Auto Tuning Cancel", "format": "INT32"},
    {"id": 51002, "name": "Thermal Model Speed", "format": "INT32"},
    {"id": 51010, "name": "Tuning Parameter 2A (Temp peak-peak)", "format": "FLOAT32"},
    {"id": 51011, "name": "Tuning Parameter 2D (Var peak-peak)", "format": "FLOAT32"},
    {"id": 51012, "name": "Tuning Parameter Ku (ult. Gain)", "format": "FLOAT32"},
    {"id": 51013, "name": "Tuning Parameter Tu (ult. period)", "format": "FLOAT32"},
    {"id": 51014, "name": "PID Parameter Kp", "format": "FLAOT32"},
    {"id": 51015, "name": "PID Parameter Ti", "format": "FLOAT32"},
    {"id": 51016, "name": "PID Parameter Td", "format": "FLOAT32"},
    {"id": 51022, "name": "Slow PI Parameter Kp", "format": "FLOAT32"},
    {"id": 51023, "name": "Slow PI Parameter Ti", "format": "FLOAT32"},
    {"id": 51024, "name": "PID D Part Damping PT1 Recommendation", "format": "FLOAT32"},
    {"id": 51017, "name": "Coarse Temp Ramp", "format": "FLOAT32"},
    {"id": 51018, "name": "Proximity Width", "format": "FLOAT32"},
    {"id": 51020, "name": "Tuning Status", "format": "INT32"},
    {"id": 51021, "name": "Tuning Progress", "format": "FLOAT32"},
    
    
    #Advanced
    #Advanced/Temperature Measurement
    #Chx Object Measurement Settings
    {"id": 6000, "name": "PGA Gain", "format": "INT32"},
    {"id": 6007, "name": "PGA Bypass", "format": "INT32"},
    {"id": 6001, "name": "Current Source", "format": "INT32"},
    {"id": 6008, "name": "Current Source 2 Out", "format": "INT32"},
    {"id": 6009, "name": "Measurement Type", "format": "INT32"},
    {"id": 6002, "name": "ADC Rs", "format": "FLOAT32"},
    {"id": 6006, "name": "ADC Rp", "format": "FLOAT32"},
    {"id": 6003, "name": "ADC Calibration Offset", "format": "FLOAT32"},
    {"id": 6004, "name": "ADC Calibration Gain", "format": "FLOAT32"},
    
    #CHx Sink Measurement Settings
    {"id": 6010, "name": "ADV Rv", "format": "FLOAT32"},
    {"id": 6013, "name": "ADV vps", "format": "FLAOT32"},
    {"id": 6011, "name": "ADV Calibration Offset", "format": "FLOAT32"},
    {"id": 6012, "name": "ADV Calibration Gain", "format": "FLOAT32"},
    
    #Advanced/Temperature Conversion 
    #CHx Object Conversion Mode
    {"id": 6005, "name": "Sensor Type Selection", "format": "INT32"},
    
    #CHx Object NTC Sensor Characteristics
    {"id": 4024, "name": "Upper Point: Temperature", "format": "FLOAT32"},
    {"id": 4025, "name": "Upper Point: Resistance", "format": "FLOAT32"},
    {"id": 4022, "name": "Middle Point: Temperature", "format": "FLOAT32"},
    {"id": 4023, "name": "Middle Point: Resistance", "format": "FLOAT32"},
    {"id": 4020, "name": "Lower Point: Temperature", "format": "FLOAT32"},
    {"id": 4021, "name": "Lower Point: Resistance", "format": "FLOAT32"},
    
    #CHx Object Voltage to Temperature Conversion
    {"id": 6400, "name": "Reference Temperature", "format": "FLOAT32"},
    {"id": 6401, "name": "Reference Voltage", "format": "FLOAT32"},
    {"id": 6402, "name": "Temperature Slope", "format": "FLOAT32"},
    
    #CHx Sink NTC Sensor Characteristics
    {"id": 5024, "name": "Upper Point: Temperature", "format": "FLOAT32"},
    {"id": 5025, "name": "Upper Point: Resistance", "format": "FLOAT32"},
    {"id": 5022, "name": "Middle Point: Temperature", "format": "FLOAT32"},
    {"id": 5023, "name": "Middle Point: Resistance", "format": "FLOAT32"},
    {"id": 5020, "name": "Lower Point: Temperature", "format": "FLOAT32"},
    {"id": 5021, "name": "Lower Point: Resistance", "format": "FLOAT32"},    
    
    #Advanced/ADS Self Check 
    #CHx Object Measurement ADS Self Check Settings. The Parameter 6051 is volatile
    {"id": 6050, "name": "Self-Check Period", "format": "INT32"},
    {"id": 6051, "name": "Self-Chek Trigger", "format": "INT32"},
    {"id": 6052, "name": "IRs Error Enable", "format": "INT32"},

    #CHx Object Measurement ADS Self Check Result. The folowing Parameters are volatile
    {"id": 6053, "name": "AVDD", "format": "FLOAT32"},
    {"id": 6054, "name": "IRs", "format": "FLOAT32"},
    {"id": 6055, "name": "VRef", "format": "FLOAT32"},
    
    #Advanced/Lookup Table 
    {"id": 52000, "name": "Lookup Table Start", "format": "INT32"},
    {"id": 52001, "name": "Lookup Table Stop", "format": "INT32"},
    {"id": 52002, "name": "Lookup Table Status", "format": "INT32"},
    {"id": 52003, "name": "Lookup Table Status Current Table Line", "format": "INT32"},
    {"id": 52010, "name": "Lookup Table ID Selection", "format": "INT32"},
    {"id": 52012, "name": "Number of Repetitions", "format": "INT32"},
    
    #Advanced/Display
    #Display Configuration
    {"id": 6020, "name": "Display Type", "format": "INT32"},
    {"id": 6023, "name": "Display Line 1-4 Alternative Mode", "format": "INT32"},
    {"id": 6024, "name": "Display Line 1-4 default Text", "format": "LATIN1"},
    {"id": 6025, "name": "Display Line 1-4 Alternative Text", "format": "LATIN1"},
    {"id": 6026, "name": "Display Line 1-4 Startup Text", "format": "LATIN1"},
    
    #Advanced/GPIO
    #GPIO Configuration(GPIO1 ... GPIO8)
    {"id": 6100, "name": "GPIO Function", "format": "INT32"},
    {"id": 6101, "name": "GPIO Level Assignment", "format": "INT32"},
    {"id": 6102, "name": "GPIO Hardware Configuration", "format": "INT32"},
    {"id": 6103, "name": "GPIO Channel", "format": "INT32"},
    
    #CHx Change Target Temperature Buttons
    {"id": 6111, "name": "Upper Temperature Limit", "format": "FLOAT32"},
    {"id": 6110, "name": "Lower Temperature Limit", "format": "FLOAT32"},
    {"id": 6112, "name": "Step Size", "format": "FLAOT32"},
    
    #CHx Pump Control 
    {"id": 6120, "name": "Actual Temperature Source", "format": "INT32"},
    {"id": 6121, "name": "ON Threshold", "format": "FLOAT32"},
    {"id": 6122, "name": "OFF Threshold", "format": "FLOAT32"},
    
    #CHx Alternative Target Temperature over GPIO Pin
    {"id": 6130, "name": "Temperature 1", "format": "FLOAT32"},
    {"id": 6131, "name": "Temperature 2", "format": "FLOAT32"},
    {"id": 6132, "name": "Temperature 3", "format": "FLOAT32"},
    
    #Advanced/Fan
    #CHx Fan Control Enable 
    {"id": 6200, "name": "Fan Control Enable", "format": "INT32"},
    
    #CHx Fan Temperature Controller 
    {"id": 6210, "name": "Actual Temperature Source", "format": "INT32"},
    {"id": 6211, "name": "Target Temperature", "format": "FLOAT32"},
    {"id": 6212, "name": "Kp", "format": "FLOAT32"},
    {"id": 6213, "name": "Ti", "format": "FLOAT32"},
    {"id": 6214, "name": "Td", "format": "FLOAT32"},
    
    #CHx Fan Speed Controller
    {"id": 6220, "name": "Fan Speed 0", "format": "FLOAT32"},
    {"id": 6221, "name": "Fan Speed 100", "format": "FLOAT32"},
    {"id": 6227, "name": "Fan Min Speed Start", "format": "FLOAT32"},
    {"id": 6228, "name": "Fan Min Speed Stop", "format": "FLOAT32"},
    {"id": 6222, "name": "Kp", "format": "FLOAT32"},
    {"id": 6223, "name": "Ti", "format": "FLOAT32"},
    {"id": 6224, "name": "Td", "format": "FLOAT32"},
    {"id": 6225, "name": "Bypassing Speed Conroller", "format": "INT32"},
    {"id": 6226, "name": "Fan Surveillance", "format": "INT32"},
    
    #Fan General Settings
    {"id": 6230, "name": "Fan PWM Frequency", "format": "INT32"},
    
    
    #Advanced/Misc
    #CHx Actual Object Temperature
    {"id": 6300, "name": "Source Selection", "format": "INT32"},
    {"id": 6301, "name": "Control Speed", "format": "INT32"},
    {"id": 6302, "name": "Observe Mode", "format": "INT32"},
    
    #Error State Auto Restart Delay
    {"id": 6310, "name": "Delay till Restart", "format": "FLOAT32"},
    
    #Device Temperature Mode (Output Stage)
    {"id": 6330, "name": "Mode", "format": "INT32"},
    
    #Output Stage Controller Limit (Error 108)
    {"id": 6320, "name": "Error Delay", "format": "INT32"},
    
    #Other Parameters (Not directly displayed in the Service Software)
    #Power Supply Prameters(Bus-Controlled) Mode Parameters
    {"id": 50000, "name": "Live Enable", "format": "INT32"},
    {"id": 50001, "name": "Live Set Current", "format": "FLOAT32"},
    {"id": 50002, "name": "Live Set Voltage", "format": "FLOAT32"},
    
    #Temperature Regulator Additional Parameters
    {"id": 50010, "name": "Sine Ramp Start Point", "format": "INT32"},
    {"id": 50011, "name": "Object Target Temperature Source Selection", "format": "INT32"},
    {"id": 50012, "name": "Object Target Temperature", "format": "FLOAT32"},
    
    #GPIO(1-8) Signal Control
    {"id": 52100, "name": "Enable Function", "format": "INT32"},
    {"id": 52101, "name": "Set Output to Push-Pull", "format": "INT32"},
    {"id": 52102, "name": "Set Output States", "format": "INT32"},
    {"id": 52103, "name": "Read Input States", "format": "INT32"},

    #Set Actual Object Temperature from external
    {"id": 52200, "name": "External Object Temperature", "format": "FLOAT32"},
]



LDD_PARAMETERS = [
    
    #Common Product Parameters
    #Device Identification
    {"id": 100, "name": "Device Type", "format": "INT32"},
    {"id": 101, "name": "Device Hardware Version", "format": "INT32"},
    {"id": 102, "name": "Device Serial Number", "format": "INT32"},
    {"id": 103, "name": "Device Firmware Version", "format": "INT32"},
    {"id": 104, "name": "Device Status", "format": "INT32"},
    {"id": 105, "name": "Device Error Number", "format": "INT32"},
    {"id": 106, "name": "Device Error Instance", "format": "INT32"},
    {"id": 107, "name": "Device Error Parameter", "format": "INT32"},
    {"id": 108, "name": "Device Save Data to Flash", "format": "INT32"},
    {"id": 109, "name": "Device Flash Status", "format": "INT32"},
    
    #Monitor (Read only)
    #Firmware and Hardware Versions
    {"id": 1000, "name": "Device Type", "format": "INT32"},
    {"id": 1001, "name": "Serial Number", "format": "INT32"},
    {"id": 1002, "name": "Harware Version", "format": "INT32"},
    {"id": 1003, "name": "Firmware Version [STM32]", "format": "INT32"},
    {"id": 1004, "name": "Firmware Build Number", "format": "INT32"},
    {"id": 1005, "name": "FPGA Version", "format": "INT32"},
    
    #Laser Diode Values
    {"id": 1016, "name": "Laser Diode Current", "format": "FLOAT32"},
    {"id": 1017, "name": "Laser Diode Voltage", "format": "FLOAT32"},
    {"id": 1015, "name": "Laser Diode Temperature", "format": "FLOAT32"},
    
    #Laser Light Values
    {"id": 1060, "name": "Photo Diode Current", "format": "FLOAT32"},
    {"id": 1061, "name": "Laer Power", "format": "FLOAT32"},
    
    #Laser Diode Values (Details)
    {"id": 1011, "name": "Laser Diode Current CW", "format": "FLOAT32"},
    {"id": 1010, "name": "Laser Diode Current Actual", "format": "FLOAT32"},
    {"id": 1013, "name": "Laser Diode Voltage Actual", "format": "FLOAT32"},
    {"id": 1012, "name": "Laser Diode Current Pulse", "format": "FLOAT32"},
    {"id": 1014, "name": "Laser Diode Voltage Pulse", "format": "FLOAT32"},
    
    #Power Supplies
    {"id": 1020, "name": "Driver Input Voltage", "format": "FLOAT32"},
    {"id": 1021, "name": "Medium Internal Supply", "format": "FLOAT32"},
    {"id": 1022, "name": "3.3V Internal Supply", "format": "FLOAT32"},
    {"id": 1023, "name": "1.2V Internal Supply", "format": "FLOAT32"},
    
    #Error Status
    {"id": 1030, "name": "Error Number", "format": "INT32"},
    {"id": 1031, "name": "Error Instance", "format": "INT32"},
    {"id": 1032, "name": "Error Parameter", "format": "INT32"},
    
    #Driver Values
    {"id": 1040, "name": "Buck Converter 1 Current", "format": "FLOAT32"},
    {"id": 1041, "name": "Buck Converter 2 Currnet", "format": "FLOAT32"},
    {"id": 1042, "name": "Buck Converter 3 Current", "format": "FLOAT32"},
    {"id": 1043, "name": "Base Plate Temperature", "format": "FLOAT32"},
    
    #Driver Status
    {"id": 1050, "name": "Driver Status", "format": "INT32"},
    {"id": 1051, "name": "Parameter System: Flash Status", "format": "INT32"},
    
    #Operation Control
    #Current Settings
    {"id": 2000, "name": "Input Source", "format": "INT32"},
    {"id": 2001, "name": "Current CW", "format": "FLOAT32"},
    {"id": 2002, "name": "Current High", "format": "FLOAT32"},
    {"id": 2003, "name": "Current Low", "format": "FLOAT32"},
    {"id": 2004, "name": "High Time", "format": "FLOAT32"},
    {"id": 2005, "name": "Low Time", "format": "FLOAT32"},
    {"id": 2006, "name": "Rise Time", "format": "FLOAT32"},
    {"id": 2007, "name": "Fall Time", "format": "FLOAT32"},
    {"id": 2008, "name": "Generator Trigger", "format": "INT32"},
    
    #Pulse Settings
    {"id": 2010, "name": "Input Source", "format": "INT32"},
    {"id": 2011, "name": "High Time", "format": "FLOAT32"},
    {"id": 2012, "name": "Low Time", "format": "FLOAT32"},
    
    #Enable Settings
    {"id": 2020, "name": "Input Source", "format": "INT32"},
    
    #Settings
    #PID Current Control Parameter
    {"id": 3000, "name": "Kp", "format": "FLOAT32"},
    {"id": 3001, "name": "Ti", "format": "FLOAT32"},
    {"id": 3002, "name": "Td", "format": "FLOAT32"},
    
    #Analog Control
    {"id": 3010, "name": "Current Factor", "format": "FLOAT32"},
    
    #Maximum Values
    {"id": 3020, "name": "Current Limit Max [A]", "format": "FLOAT32"},
    {"id": 3021, "name": "Current Limit Min [A]", "format": "FLOAT32"},
    {"id": 3022, "name": "Max Current Error [A]", "format": "FLOAT32"},
    {"id": 3023, "name": "Slope Limit [A/us]", "format": "FLOAT32"},
    
    #PBC Configuration (RES1 ... RES8)
    {"id": 3080, "name": "Hardware PIN", "format": "INT32"},
    
    #Communication
    {"id": 3030, "name": "Communication Watchdog", "format": "FLOAT32"},

    #Device Address
    {"id": 3040, "name": "Device Address", "format": "INT32"},
    
    #RS485 Channel 1 Settings
    {"id": 3050 , "name": "Baud Rate", "format": "INT32"},
    {"id": 3051 , "name": "Response Delay ", "format": "INT32"},

    #Laser Diode Temperature Settings
    {"id": 3060, "name": "Lower Error Threshold", "format": "FLOAT32"},
    {"id": 3061, "name": "Upper Error Threshold", "format": "FLOAT32"},

    #NTC Sensor Characteristic
    {"id": 3070, "name": "Lower Point Temperature", "format": "FLOAT32"},
    {"id": 3071, "name": "Lower Point Resistance", "format": "FLOAT32"},
    {"id": 3072, "name": "Middle Point Temperature", "format": "FLOAT32"},
    {"id": 3073, "name": "Middle Point Resistance", "format": "FLOAT32"},
    {"id": 3074, "name": "Upper Point Temperature", "format": "FLOAT32"},
    {"id": 3075, "name": "Upper Point Resistance", "format": "FLOAT32"},

    #Expert
    #Laser Diode Temperature Measurement Settings
    {"id": 4000, "name": "ADC Calibration Offset", "format": "FLOAT32"},
    {"id": 4001, "name": "ADC Calibration Gain", "format": "FLOAT32"},
    {"id": 4002, "name": "ADC Rv", "format": "FLOAT32"},
    {"id": 4003, "name": "Temperature Offset", "format": "FLOAT32"},
    {"id": 4004, "name": "Temperature Gain", "format": "FLOAT32"},

    #Laser Power Measurement Settings
    {"id": 4010, "name": "Measurement Rs", "format": "FLOAT32"},
    
    #Current Measurement Settings
    {"id": 4020, "name": "Current Offset", "format": "FLOAT32"},
    {"id": 4021, "name": "Current Gain", "format": "FLOAT32"},
    
    #LDD Parallel Master/Slave Configuration
    {"id": 4100, "name": "Parallel Function/Type", "format": "INT32"},
    {"id": 4101, "name": "RS485 Sync. Channel", "format": "INT32"},
    {"id": 4102, "name": "Master: Number of Slaves", "format": "INT32"},
    {"id": 4103, "name": "Slave: Slave ID", "format": "INT32"},
    
    
]
    
ERRORS = [
    {"code": 1, "symbol": "EER_CMD_NOT_AVAILABLE", "description": "Command not available"},
    {"code": 2, "symbol": "EER_DEVICE_BUSY", "description": "Device is busy"},
    {"code": 3, "symbol": "ERR_GENERAL_COM", "description": "General communication error"},
    {"code": 4, "symbol": "EER_FORMAT", "description": "Format error"},
    {"code": 5, "symbol": "EER_PAR_NOT_AVAILABLE", "description": "Parameter is not available"},
    {"code": 6, "symbol": "EER_PAR_NOT_WRITABLE", "description": "Parameter is read only"},
    {"code": 7, "symbol": "EER_PAR_OUT_OF_RANGE", "description": "Value is out of range"},
    {"code": 8, "symbol": "EER_PAR_INST_NOT_AVAILABLE", "description": "Parameter is read only"},
    {"code": 20, "symbol": "MEPORT_ERROR_SET_TIMEOUT", "description": "timeout reached, value cannot be set"},
    {"code": 21, "symbol": "MEPORT_ERROR_QUERY_TIMEOUT", "description": "timeout reached query cannot be served"},
]
