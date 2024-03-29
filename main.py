# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from pathlib import Path

import yaml

from SungrowModbusTcpClient import SungrowModbusTcpClient
from mapping import lengthMapping, sungrowIp, unitMapping, factorMapping, addressMapping
import csv


def getInputRegisterValue(address, length, factor):
    value = 0
    value = value * factor

    return value


def combineWords(msw, lsw):
    return 0  # TODO


def getHoldingValue(address, length):
    value = 0
    if length == 1:
        value = 0  # TODO
    elif length == 2:
        value0 = getHoldingValue(address + 0, 1)
        value1 = getHoldingValue(address + 1, 1)
        value = combineWords(value0, value1)
    else:
        pass
        # meep meep
    return value


def printHoldingValue(valueName):
    length = lengthMapping[valueName]
    address = addressMapping[valueName]
    unit = unitMapping[valueName]
    factor = factorMapping[valueName]
    value = factor * getHoldingValue(address, length)
    print(valueName + ": " + value + " " + unit)


def txt_to_solariot():
    with open(Path('documentation') / 'eingangsregister_stand2021_02_02.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        header = []
        output = {}
        for i, row in enumerate(reader):
            if i == 0:
                header = row
                print(header)
            if i > 0:
                factor = row[header.index('factor')]
                if len(factor) == 0:
                    factor = 1
                print(factor)
                factor = float(factor)
                factor = 1 / factor
                if factor == 1:
                    factor = ''
                else:
                    factor = f'_{factor}'
                name = str(row[header.index('name')]).replace('  ', ' ').replace('  ', ' ').replace(' ', '_').lower()
                address = int(row[header.index('address')]) + 1
                output[str(address)] = f'{name}{factor}'
                # print(row[header.index('deviceId')])
        print(output)


class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def modbus4mqtt_to_home_assistant(filename: str):
    with open(filename, 'r') as file:
        try:
            content = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(e)
            return
    target_dict = {'sensor': [], 'binary_sensor': []}
    for register in content['registers']:
        sensor = {
            'platform': 'mqtt',
            'state_topic': f'modbus4mqtt/{register["pub_topic"]}',
        }
        if 'json_key' in register:
            sensor['name'] = f'{register["json_key"]}'
            sensor['value_template'] = f'{{{{ value_json.{register["json_key"]} }}}}'
            sensor['unique_id'] = f'sungrow.{register["json_key"]}'  # TODO replace . with _
        else:
            sensor['name'] = f'{register["pub_topic"]}'
            sensor['unique_id'] = f'sungrow.{register["pub_topic"]}'  # TODO replace . with _
        if 'unit' in register:
            sensor['unit_of_measurement'] = register['unit']
            if 'class' in register:
                sensor['device_class'] = register['class']
            elif 'A' == register['unit']:
                sensor['device_class'] = 'current'
            elif 'V' == register['unit']:
                sensor['device_class'] = 'voltage'
            elif 'Wh' == register['unit'] or 'kWh' == register['unit']:
                sensor['device_class'] = 'energy'
            elif 'W' == register['unit'] or 'kW' == register['unit']:
                sensor['device_class'] = 'power'
            elif '\\xC2\\xB0C' == register['unit']:
                sensor['device_class'] = 'temperature'
        if 'sensor_type' in register:
            if register['sensor_type'] == 'binary':
                sensor['payload_off'] = 0
                sensor['payload_on'] = 1
                target_dict['binary_sensor'].append(sensor)
                continue
            elif register['sensor_type'] == 'measurement':
                sensor['state_class'] = 'measurement'
                sensor['last_reset_topic'] = sensor['state_topic']
                sensor['last_reset_value_template'] = '1970-01-01T00:00:00+00:00'
        target_dict['sensor'].append(sensor)
    with open('modbus4mqtt_sensor.yaml', 'w', encoding='utf8') as outfile:
        dump = yaml.dump(target_dict['sensor'], default_flow_style=False)
        dump = dump.replace('\\xC2\\xB0C', '°C')
        outfile.write(dump)
    with open('modbus4mqtt_binary_sensor.yaml', 'w', encoding='utf8') as outfile:
        dump = yaml.dump(target_dict['binary_sensor'], default_flow_style=False)
        dump = dump.replace('\\xC2\\xB0C', '°C')
        outfile.write(dump)
    dump = yaml.dump(target_dict, Dumper=MyDumper, default_flow_style=False)
    dump = dump.replace('\\xC2\\xB0C', '°C')
    print(dump)


if __name__ == '__main__':
    modbus4mqtt_to_home_assistant('modbus4mqtt/sungrow_sh10rt.yaml')
    # txt_to_solariot()

    # client = SungrowModbusTcpClient(host='192.168.178.66', port=502, timeout=10)
    # result = client.read_input_registers(address=4950, count=100, unit=0x01)
    # print(result.registers)
    # client.read_input_registers(address=13000, count=125)
    # client.read_holding_registers(address=5000, count=10)
    # client.read_holding_registers(address=13000, count=110)
    # running = True

    # print(getHoldingValue("Voltage Phase A"))
    # print(getHoldingValue("Voltage Phase B"))
    # print(getHoldingValue("Voltage Phase C"))

    # client.close()
