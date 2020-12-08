from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
from modules.report_designer import Report_designer
from modules.report_maker import make_report

#prebuilt dashboards

from custom_dashboards.gigamon.dashboards.gigamon_counts import count_monitor
from custom_dashboards.gigamon.dashboards.gigamon_sus import sus_monitor
from custom_dashboards.gigamon.dashboards.gigamon_dns import dns_monitor


# from custom_dashboards.gigamon.dashboards.dashboard_names import gigamon_dashboards

#prebuilt designed reports
from custom_dashboards.gigamon.designed_reports.gigamon_reports import gigamon_reports_list

import configparser
import json
import os
import sys,getopt

from delete_everything import delete_saved_reports,delete_dashboards,delete_designed_reports, delete_dashboard_gadgets


# Include standard modules
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-G", "--make", help="specificy dashboard to make")
parser.add_argument("-D", "--delete", help="Delete a Dashboard, supply dashboard name after")
args = parser.parse_args()


# iniate database configuration information.
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config', 'db_creds.ini'))
config_info = config['DB']
db_name = config_info['db_name']
db_user = config_info['scrutinizer_user']
db_pass = config_info['scrutinizer_password']
db_host = config_info['scrutinizer_host']



## iniate all modules to handle various portions of the Script.
dash_handler = Dash_handler()
report_handler = Report_handler()
json_handler = Json_handler()
report_designer = Report_designer()
db_handler = DB_handler(db_name,db_user,db_pass,db_host)


# create the dashboard. 
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



# In order to move reports to a dashboard, we will first need to save the reports. These 2 methods will achieve saving reports thats are native to Scrutinizer. In some instances we will first need to design reports, and then save them (for reports that are not int he product yet). 


## finds the next available saved report ID
def get_availabled_saved_id():
    print('gettting saved report id')
    saved_id_query = report_handler.available_saved_id()
    saved_id = db_handler.execute_query(saved_id_query)[0]
    print(f'saved_id is {saved_id}')
    return saved_id


# create saved report object, this is the JSON passed into the Query to make a saved report. 

def create_report_object(report_object):
    rep_nam = report_object['name']
    print(f'creating report object for {rep_nam}')
    saved_id = get_availabled_saved_id()

    report_name = report_object['name']
    exporter = report_object['exporter']
    report_lang = report_object['lang']
    data_type = report_object['data_type']
    stacked = report_object['stacked']
    report_filters = report_object['filters']
    time_range = report_object['time_range']
    report_direction = report_object['direction']

    report_obj = json_handler.report_json(report_name,saved_id,exporter,report_lang,data_type, stacked,report_filters, time_range, report_direction)

    return report_obj


## created a saved report.

def created_saved_report(report_obj):
    print('creating saved report')
    saved_id = get_availabled_saved_id()

    report_name = json.loads(report_obj)["saved"]["name"]
    print(f'{report_name} object created')
    created_report_query = report_handler.create_report_query(saved_id,report_name,report_obj,1)
    
    db_handler.execute_query(created_report_query)




def make_dash_gadget(report_object):
    

    report_name = report_object['name']
    view = report_object['view']
    user = report_object['user_id']
    print(f'making dashboard gadget for {report_name}')
    saved_id_query = report_handler.get_saved_report_id(report_name)
    saved_id = db_handler.execute_query(saved_id_query)[0]
    gadget_json = json_handler.gadget_json(view,saved_id)
    gadget_query = dash_handler.make_dash_gadget(report_name,saved_id,gadget_json, user )

    db_handler.execute_query(gadget_query)


def create_dashbord_json(report_list):
    print('making dashboard JSON')

    gadget_json_list = []

    for report in report_list:
        rep_name = report['name']
        print(f'making gadget for {rep_name}')
        gadget_id = report_handler.get_gadget_id(report['name'])
        gadget_id = db_handler.execute_query(gadget_id)[0]
        gadget_json = json_handler.add_gadget_json(gadget_id, report['position'])
        gadget_json_list.append(gadget_json)

    gadget_json_list = '[%s]' % ', '.join(map(str, gadget_json_list))



    return gadget_json_list


def place_gadgets(dashboard_name, gadget_json):
    print(f'placing gadgets on dash {dashboard_name}')
    dash_id = dash_handler.find_dashboard_id(dashboard_name)
    dash_id = db_handler.execute_query(dash_id)[0]

    add_gadgets_query = dash_handler.add_gadget_to_dash(gadget_json,dash_id )

    db_handler.execute_query(add_gadgets_query)
    


def delete_all(designed_reports = None, *kwargs):

    
    for dashboard in kwargs:
        delete_saved_reports(dashboard)
        delete_dashboard_gadgets(dashboard)
        delete_dashboards(dashboard)
    
    if designed_reports is not None:
        for designed_report in designed_reports:
            delete_designed_reports(designed_report)

def main(designed_reports = None, *kwargs):

    for dashboard in kwargs:
        dash_name = dashboard[0]['dashboard']
        print(f'create dashboard {dash_name}')
        create_dashboard(dashboard[0]['dashboard'])

    if designed_reports is not None:
        for designed_report in designed_reports:
            make_report(designed_report)
    
    for dashboard in kwargs: 
        for report in dashboard:
            #make report object
            saved_obj = create_report_object(report)
            #create report
            created_saved_report(saved_obj)
            #convert report into gadget 
            make_dash_gadget(report)
        dashboard_name = dashboard[0]['dashboard']
        json_for_dash = create_dashbord_json(dashboard)
        place_gadgets(dashboard_name, json_for_dash)



#open connection to DB
db_handler.open_connection()


if __name__ == "__main__":

    if args.make == 'gigamon':
        print(f"making dashboard for {args.make}")
        main(gigamon_reports_list, dns_monitor, sus_monitor, count_monitor)
    elif args.delete == 'gigamon':
        delete_all(gigamon_reports_list, dns_monitor, sus_monitor, count_monitor)







#close connection
db_handler.close_connection()