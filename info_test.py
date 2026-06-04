# https://drive.google.com/file/d/1-NFJrNPh9MPMGv_Kl4JdCRtPXcc9765s/view?usp=sharing
# https://drive.google.com/file/d/1UyXOvAtCwp8jzgcFlyyg3S5l9z1jFQFu/view?usp=sharing

import pandas as pd                                       # Робота з таблицями (DataFrame): зчитування, обробка, аналіз
import numpy as np                                        # Математика й масиви: середнє, суми, випадкові числа, статистика
import matplotlib.pyplot as plt                           # Побудова графіків і діаграм (базова візуалізація)
import seaborn as sns                                     # Красива статистична візуалізація (поверх matplotlib)
from datetime import datetime                             # Робота з датами й часом (парсинг, форматування, різниця дат), імпорт класу datetime з модуля datetime
import re                                                 # Регулярні вирази - пошук і очищення тексту за шаблоном, модуль регулярних виразів (regular expressions)
import warnings                                           # Приховування або керування попередженнями в коді (щоб не засмічували вивід)
warnings.filterwarnings('ignore', category=FutureWarning) # Глушить тільки попередження про зміни у майбутніх версіях
import requests                                           # для роботи з завантаженням API
