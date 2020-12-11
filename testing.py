
from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
from modules.report_designer import Report_designer


import configparser
import json
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'db_creds.ini'))
config_info = config['DB']
db_name = config_info['db_name']
db_user = config_info['scrutinizer_user']
db_pass = config_info['scrutinizer_host']
db_host = config_info['scrutinizer_host']


dash_handler = Dash_handler()

report_handler = Report_handler()
db_handler = DB_handler(db_name,db_user,db_pass,db_host)


report_obj_query = report_handler.get_report_object('country count')

db_handler.open_connection()

things = db_handler.execute_query(report_obj_query)

print(things)

db_handler.close_connection()

