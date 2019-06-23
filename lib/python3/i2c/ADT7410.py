# -*- coding:utf-8 -*-
import smbus
from time import sleep

def read_adt7410(address_adt7410,register_adt7410):
    word_data = bus.read_word_data(address_adt7410, register_adt7410)
    data = (word_data & 0xff00) >> 8 | (word_data & 0x00ff) << 8
    data = data >> 3 # 13bit data
    if data & 0x1000 == 0:
        temperature = data / 16
    else : 
        temperature = (data - 8192) /16
    return temperature

if __name__ == '__main__':
    bus = smbus.SMBus(1)
    address_adt7410 = 0x48
    register_adt7410 = 0x00

    temperature = read_adt7410(address_adt7410, register_adt7410)
    print(temperature)