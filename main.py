# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from pathlib import Path

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


if __name__ == '__main__':
    txt_to_solariot()

    # client = SungrowModbusTcpClient(sungrowIp)
    # running = True

    # print(getHoldingValue("Voltage Phase A"))
    # print(getHoldingValue("Voltage Phase B"))
    # print(getHoldingValue("Voltage Phase C"))

    # client.close()
