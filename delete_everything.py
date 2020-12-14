from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
from modules.report_designer import Report_designer
from modules.report_maker import make_report


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
db_handler = DB_handler(db_name,db_user,db_pass,db_host)


#takes in the primary dashbaord object
def delete_saved_reports(report_object):
    db_handler.open_connection()
    for report in report_object:
        report_name = report['name']
        delete_report_query = report_handler.delete_saved_report(report_name)
        db_handler.execute_query(delete_report_query)

    db_handler.close_connection()
    return

#takes in the designed report object
def delete_designed_reports(report_object):

    db_handler.open_connection()
    for report in report_object:
        for column in report:
            try:
                report_lang = column['headers']['rpt_lang']
                print('report lang to be deleted is {}'.format(report_lang))
                lang_to_find = report_handler.get_report_id(report_lang)
                report_id = db_handler.execute_query(lang_to_find)[0]
                print('found id {} for {}'.format(report_id,report_lang))
                delete_designed_reports_query = report_handler.delete_designed_report(report_id, report_lang)
                for query in delete_designed_reports_query:
                    print('running {}'.format(query))
                    db_handler.execute_query(query)
                    print('success')
            except:
                pass
    


    db_handler.close_connection()
    return

#takes in the primary dashbaord object
def delete_dashboard_gadgets(report_object):
    db_handler.open_connection()
    for report in report_object:
        report_name = report['name']
        print('deleting gadget of report {}'.format(report_name))
        delete_query = report_handler.delete_report_as_gadget(report_name)
        db_handler.execute_query(delete_query)
        print('success')
    db_handler.close_connection()

def delete_dashboards(report_object):
    db_handler.open_connection()
    dashboard_name = report_object[0]['dashboard']
    
    dashboard_id = dash_handler.find_dashboard_id(dashboard_name)

    try:
        dashboard_id = db_handler.execute_query(dashboard_id)[0]
        print({'Id is {} for {}'.format(dashboard_id,dashboard_name)})
        delete_dashboards_queries = dash_handler.delete_dashboard(dashboard_id)
        print('deleting dashboard {}'.format(dashboard_name))
        for dashboard_query in delete_dashboards_queries:
            db_handler.execute_query(dashboard_query)
        print('success')
    except:
        print('Dashboard {} does not exist Skipping'.format(dashboard_name))
        pass

    db_handler.close_connection()
    return



