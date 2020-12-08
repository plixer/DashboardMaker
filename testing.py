
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


column_names = [
                {
                
                {"group_by":{
                    "column_name":"dstcountry",
                    "col_order":1,
                    "col_lang":"Destination Country",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"",
                    "col_width":"dynmaic"}},

                {"trend_by":{
                    "column_name_sum":"sum_plixeraggregatedrecordcount",
                    "column_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Connections",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"",
                    "col_width":"dynmaic"}}

                }                   
                
                    

                ]

report_lang = "country_count"
report_pretty = "Destination Country Count"

db_handler = DB_handler(db_name,db_user,db_pass,db_host)
#open connection to DB




def main(report_columns):

    # report_id_query = report_designer.get_available_id()
    # report_id = db_handler.execute_query(report_id_query)[0]

    report_designer.create_report_columns_new(report_columns)


# find next report ID


db_handler.open_connection()

main(column_names)


db_handler.close_connection()


# querys = []

# # create report header info 

# report_header_query = report_designer.report_headers(report_id,report_lang, 23, 'stacked')

# querys.append(report_header_query)

# ## create columns query

# report_columns_query = report_designer.create_report_columns(report_id, column_names)


# querys.append(report_columns_query)
# ## set group by information
# report_groupby_query = report_designer.report_types_groupby(report_id, column_names)


# querys.append(report_groupby_query)
# ## set aggregations
# report_aggregation_query = report_designer.report_type_aggregations(report_id, column_names)

# querys.append(report_aggregation_query)

# ## set whats mandatory for report
# report_type_select = report_designer.report_type_select(report_id, column_names)
# querys.append(report_type_select)

# # make report name prettier
# report_add_lang = report_designer.add_lang_kery(report_lang, report_pretty)


# querys.append(report_add_lang)

# # alter sequence
# report_restart_sequence = report_designer.alter_sequence(report_id)


# querys.append(report_restart_sequence)


# for query in querys:
#     db_handler.execute_query(query)


















