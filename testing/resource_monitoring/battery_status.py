import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

i2c = board.I2C()  # uses board.SCL and board.SDA

ina219 = INA219(i2c, 0x41)

print('INA219 Battery Status')

# display some of the advanced field (just to test)
print('Config Register:')
print('  bus_voltage_range:    0x%1X' % ina219.bus_voltage_range)
print('  gain:                 0x%1X' % ina219.gain)
print('  bus_adc_resolution:   0x%1X' % ina219.bus_adc_resolution)
print('  shunt_adc_resolution: 0x%1X' % ina219.shunt_adc_resolution)
print('  mode:                 0x%1X' % ina219.mode)
print('')

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

# measure and display loop
while True:
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    percentage = (bus_voltage - 9) / 3.6 * 100
    if(percentage > 100):percentage = 100
    if(percentage < 0):percentage = 0
    
    if(current < 0):current = 0
    if(current > 30):
        Charge = True
    else:
        Charge = False

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print('Voltage (VIN+) : {:.2f} V'.format(bus_voltage + shunt_voltage))
    print('Voltage (VIN-) : {:.2f} V'.format(bus_voltage))
    print('Shunt Voltage  : {:.2f} V'.format(shunt_voltage))
    print('Shunt Current  : {:.2f} A'.format(current / 1000))
    print('Power Calc.    : {:.2f} W'.format(bus_voltage * (current / 1000)))
    print('Power Register : {:.2f} W'.format(power))
    print('Percentage     : {:.2f} W'.format(percentage))

    if(Charge == False):
        print('Charging Status: None')
    else:
        print('Charging Status: Charging')
    
    print('')

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        print('Internal Math Overflow Detected!')
        print('')

    time.sleep(2)