
# Получить справочник переменных окружения
import os
from dotenv import load_dotenv
load_dotenv()
json_file_path = os.getenv('json_file_path')
# Получить доступ к файлу
from json_file_worker import fromJson, toJson

''' Описывает CRUD операции над Person'ами '''


currentState = fromJson(json_file_path)

def GetAll():
    return currentState

def GetByKey(key: str):
    return currentState.get(key, default = None)
