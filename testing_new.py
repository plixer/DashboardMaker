
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

json_handler = Json_handler()


report_designer = Report_designer()

designed_report_name = 'newestGigamona'
dashbaord_name = 'gigamon dash2'

saved_report_name = 'gigamon_test_brian1'

exporter = 'in_GROUP_ALL'
saved_report_name = 'brian_report'
report_lang = 'conversationsApp'
timerange = 'Last24Hours'

db_handler = DB_handler(db_name,db_user,db_pass,db_host)
#open connection to DB
db_handler.open_connection()





def get_designed_report_id():
    report_id_query = report_handler.get_report_id(designed_report_name)
    report_id = db_handler.execute_query(report_id_query)
    return report_id


def get_availabled_saved_id():
    saved_id_query = report_handler.available_saved_id()
    saved_id = db_handler.execute_query(saved_id_query)[0]

    return saved_id

def created_saved_report(exporter, report_name, report_lang, filters):
    
    saved_id = get_availabled_saved_id()

    report_obj = json_handler.report_json(report_name, saved_id, exporter, report_lang, filters)
    created_report_query = report_handler.create_report_query(saved_id,report_name,report_obj,1)
    
    db_handler.execute_query(created_report_query)



def get_saved_report_id(saved_report_name):
    saved_id_query = report_handler.get_saved_report_id(saved_report_name)
    try:
        saved_id = db_handler.execute_query(saved_id_query)[0]
    except:
        print('unable to find saved report')
        return
    return saved_id


def create_dashboard(dashbaord_name):
    #find next available dashID
    dashboard_id_query = dash_handler.available_dash_id()
    dashboard_id = db_handler.execute_query(dashboard_id_query)[0]

    #create dashboard
    create_dashboard_query = dash_handler.create_dashboard(dashbaord_name,dashboard_id)
    db_handler.execute_query(create_dashboard_query)

    #make dash visible 

    make_visible_query = dash_handler.make_visible(dashboard_id, 1)
    db_handler.execute_query(make_visible_query)



def make_dash_gadget(saved_report_name, user_id):
    
    saved_id_query = report_handler.get_saved_report_id(saved_report_name)
    saved_id = db_handler.execute_query(saved_id_query)[0]
    gadget_json = json_handler.gadget_json('graph',saved_id)
    gadget_query = dash_handler.make_dash_gadget(saved_report_name,gadget_json, user_id )
    db_handler.execute_query(gadget_query)



def create_dashboard_gadget(view,saved_id):

    dashboard_gadget_json = json_handler.gadget_json(view, saved_id)
    create_gadget_query = dash_handler.make_dash_gadget()






def delete_designed_report(report_id,report_name):
    report_designer_query = report_handler.delete_designed_report(report_id,report_name)
    for query in report_designer_query:
        db_handler.execute_query(query)


def delete_saved_report(saved_id):
    delete_saved_report_query = report_handler.delete_saved_report(saved_id)
    db_handler.execute_query(delete_saved_report_query)




def delete_dashboard(dashbaord_name):
    dashboard_id_query = dash_handler.find_dashboard_id(dashbaord_name)
    dashboard_id = db_handler.execute_query(dashboard_id_query)[0]

    delete_dashboard_query = dash_handler.delete_dashboard(dashboard_id)

    for query in delete_dashboard_query:
        db_handler.execute_query(query)



make_dash_gadget(saved_report_name, 1)



db_handler.close_connection()