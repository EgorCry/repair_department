# Это программа-эмулятор для демонстрирования работы датчиков на складе суточного хранения.
import random
import time
import sys
import os
from Classes.Ingredient import Ingredient
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import csv


if __name__ == '__main__':
    flour = Ingredient('flour', 95000, 360, 60, 70, 10, 15)
    sugar = Ingredient('sugar', 61500, 720, 65, 70, 10, 20)
    eggs = Ingredient('eggs', 30000, 180, 65, 75, 10, 20)
    ingredients = [flour, sugar, eggs]
    temperature = 12
    humidity = 67
    temp_sens = [temperature]
    hum_sens = [humidity]
    weight_sens = {'flour': [flour.weight], 'sugar': [sugar.weight], 'eggs': [eggs.weight]}
    hour = 0
    dust = 0

    with open('data_common.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['x_hour', 'temperature', 'humidity', 'dust'])
        csv_writer.writeheader()

    with open('data_weight.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['x_hour', 'weight_ratio_flour', 'weight_ratio_sugar',
                                                          'weight_ratio_eggs'])
        csv_writer.writeheader()

    while True:
        temperature += random.uniform(-.5, .5)
        humidity += random.uniform(-.5, .5)
        dust += random.uniform(-1, 3)
        for i in ingredients:
            chance = random.choice([1, 2])
            if chance == 1:
                i.change_weight(random.uniform(150, 250))
            weight_sens[i.name].append(i.weight)
            if hour % 24 == 0:
                i.change_expiration_date()
        hour += 1
        print(temperature, humidity)
        for i in ingredients:
            print(i.name + ':')
            if i.check_weight() < 0.0:
                print(f'Error! No more {i.name} left!!!')
                i.weight = 0.0
            elif i.check_weight() < .1:
                print(f'Only {i.check_weight()*100}% of {i.name} left!!!')
            else:
                print(f'{i.check_weight()*100}% of product left.')
            if i.check_humidity(humidity):
                print('Humidity is okay.')
            else:
                if humidity >= i.max_humidity:
                    print(f'Humidity is too high for {i.name}!!!')
                else:
                    print(f'Humidity is too low for {i.name}!!!')
            if i.check_temperature(temperature):
                print('Temperature is okay.')
            else:
                if temperature >= i.max_temperature:
                    print(f'Temperature is too high for {i.name}!!!')
                else:
                    print(f'Temperature is too low for {i.name}!!!')
            if i.check_expiration_date():
                i.hours -= 1
                print(f'Only {i.hours} left until expiration date!!!')
            else:
                print(f'{i.expiration_date} left until expiration date.')

        if dust >= 50.0:
            print('Too much dust in the storage!!!')
        if dust >= 80.0:
            print('Critical level of the dust!!!')
        if dust >= 100.0:
            print('Error! Too high dust level! System shutdown!')
            sys.exit()

        with open('data_common.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['x_hour', 'temperature', 'humidity', 'dust'])

            info = {
                'x_hour': hour,
                'temperature': round(temperature, 2),
                'humidity': round(humidity, 2),
                'dust': dust
            }

            csv_writer.writerow(info)

        with open('data_weight.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['x_hour', 'weight_ratio_flour', 'weight_ratio_sugar',
                                                          'weight_ratio_eggs'])

            info = {
                'x_hour': hour,
                'weight_ratio_flour': flour.check_weight()*100,
                'weight_ratio_sugar': sugar.check_weight()*100,
                'weight_ratio_eggs': eggs.check_weight()*100
            }

            csv_writer.writerow(info)

        time.sleep(1)
