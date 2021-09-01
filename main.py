# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from SungrowModbusTcpClient import SungrowModbusTcpClient
from mapping import lengthMapping, sungrowIp, unitMapping, factorMapping, addressMapping


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


if __name__ == '__main__':
    client = SungrowModbusTcpClient(sungrowIp)
    running = True

    # print(getHoldingValue("Voltage Phase A"))
    # print(getHoldingValue("Voltage Phase B"))
    # print(getHoldingValue("Voltage Phase C"))

    client.close()
