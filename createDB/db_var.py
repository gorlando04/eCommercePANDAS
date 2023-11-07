from pymongo import MongoClient #Conexão com MongoDB
import pprint #Mostrar informações dos dados do banco de dados
import pandas as pd #Leitura dos arquivos
from pymongo import timeout
import numpy as np


client = MongoClient('localhost', 27017)
#Nome do banco de dados
nome_bd = 'Sales-Forecasting_' 

db = client[nome_bd]