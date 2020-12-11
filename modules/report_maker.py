
from modules.db_handler import DB_handler
from modules.dashbaord_handler import Dash_handler
from modules.report_handler import Report_handler
from modules.json_handler import Json_handler
from modules.report_designer import Report_designer


 
import configparser
import json
import os


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config', 'db_creds.ini'))
config_info = config['DB']
db_name = config_info['db_name']
db_user = config_info['scrutinizer_user']
db_pass = config_info['scrutinizer_host']
db_host = config_info['scrutinizer_host']


report_designer = Report_designer()
db_handler = DB_handler(db_name,db_user,db_pass,db_host)








def make_report(report_obj):
    db_handler.open_connection()
    #get available ID
    print('getting available reportID')
    get_id_query = report_designer.get_available_id()
    rpt_id = db_handler.execute_query(get_id_query)[0]
    print('report id is {}'.format(rpt_id))

    #create headers 
    print('creating headers')
    headers_query = report_designer.report_headers(rpt_id,report_obj)
    db_handler.execute_query(headers_query)

    # # #create columns
    print('creating columns')
    report_columns_query = report_designer.create_report_columns(rpt_id, report_obj)
    db_handler.execute_query(report_columns_query)

    # # #create group_bys
    print('creating group by')
    group_by_query = report_designer.report_types_groupby(rpt_id,report_obj )
    db_handler.execute_query(group_by_query)

    # #create opertions
    print('creating operations') 
    operations_query = report_designer.report_type_operations(rpt_id, report_obj)
    db_handler.execute_query(operations_query)

    #create select 

    print('creating selectors')
    select_query = report_designer.report_type_select(rpt_id, report_obj)
    db_handler.execute_query(select_query)

    # # # add lang key to make name pretty in menue

    print('making name pretty')
    language_query = report_designer.add_lang_kery(report_obj)
    db_handler.execute_query(language_query)

    # # # alter sequence to not break report designer. 

    print('altering sequence')
    alter_sequence_query = report_designer.alter_sequence(rpt_id)
    db_handler.execute_query(alter_sequence_query)

    print('refreshing views')
    refresh_views = report_designer.refresh_viwes()
    db_handler.execute_query(refresh_views)

    db_handler.close_connection()
