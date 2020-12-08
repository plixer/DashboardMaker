gigamon_dns_queries = [
                
                
                [
                {"headers":{
                        "rpt_lang":"custom_gigamonquery",
                        "pretty_name":"Gigamon Query Count",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"dnsqueryname",
                    "col_order":1,
                    "col_lang":"Query",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    

                {"trend_by":{
                    "col_name_sum":"sum_plixeraggregatedrecordcount",
                    "col_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Count",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]


gigamon_dns_requestors = [

[
                {"headers":{
                        "rpt_lang":"custom_gigamonresponders",
                        "pretty_name":"Gigamon DNS Responders",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"gigamondnsresponseipv4address",
                    "col_order":1,
                    "col_lang":"dnsrequestor",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    

                {"trend_by":{
                    "col_name_sum":"sum_plixeraggregatedrecordcount",
                    "col_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Count",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]



gigamon_protocols_external = [

[
                {"headers":{
                        "rpt_lang":"custom_protowatch",
                        "pretty_name":"External Communications",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"srcipgroup",
                    "col_order":1,
                    "col_lang":"Src Group",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 1}},
                    {"group_by":{
                    "col_name":"sourceipaddress",
                    "col_order":2,
                    "col_lang":"Src IP",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    {"group_by":{
                    "col_name":"applicationid",
                    "col_order":3,
                    "col_lang":"App",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    {"group_by":{
                    "col_name":"destinationipaddress",
                    "col_order":4,
                    "col_lang":"Dst IP",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    {"group_by":{
                    "col_name":"dstipas",
                    "col_order":5,
                    "col_lang":"Dst AS",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 1}},                    
                    {"group_by":{
                    "col_name":"dstcountry",
                    "col_order":6,
                    "col_lang":"Dst Country",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 1}},

                    {"select":{
                    "col_name":"octetdeltacount",
                    "manufactured": 'null'}},
                
                    

                {"trend_by":{
                    "col_name_sum":"sum_octetdeltacount",
                    "col_nam_reg":"octetdeltacount",
                    "col_order":7,
                    "col_lang":"Bits",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'bB',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]


gigamon_countries = [
                
                
                [
                {"headers":{
                        "rpt_lang":"custom_dstcountrycount",
                        "pretty_name":"Dst Country Count",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"dstcountry",
                    "col_order":1,
                    "col_lang":"Destination Country",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 1}},
                    {"select":{
                    "col_name":"destinationipaddress",
                    "manufactured": 'null'}},
                    

                {"trend_by":{
                    "col_name_sum":"sum_plixeraggregatedrecordcount",
                    "col_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Connections",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]




gigamon_version_count = [
                
                
                [
                {"headers":{
                        "rpt_lang":"custom_smbversion",
                        "pretty_name":"Gigamon SMB Version",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"gm_smb_fileserver_version",
                    "col_order":1,
                    "col_lang":"SMB Version",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    

                {"trend_by":{
                    "col_name_sum":"sum_plixeraggregatedrecordcount",
                    "col_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Count",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]


gigamon_response_count = [
                
                
                [
                {"headers":{
                        "rpt_lang":"custom_responsecount",
                        "pretty_name":"Gigamon HTTP Code Count",
                        "menu_group": 23,
                        "graph_type":"stacked",
                        "bi_width":950,
                        "totals_table":0
                    }},
                    
                    {"group_by":{
                    "col_name":"httpstatuscode",
                    "col_order":1,
                    "col_lang":"Response Code",
                    "col_style":"width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "manufactured": 'null'}},
                    

                {"trend_by":{
                    "col_name_sum":"sum_plixeraggregatedrecordcount",
                    "col_nam_reg":"plixeraggregatedrecordcount",
                    "col_order":2,
                    "col_lang":"Count",
                    "col_style":"alignRight,dataWidth,width_dynamic",
                    "col_header_title_attr":"null",
                    "col_width":"dynamic",
                    "col_operation":"sum",
                    "default_col":1,
                    "availableratetotals":"rate,total",
                    "defaultratetotal":"total",
                    "availablegraphstyles":"stacked,nonStacked",
                    "defaultgraphstyle":"stacked",
                    "showother":0,
                    "percentok":0,
                    "units":'',
                    "total_operation":"sum",
                    "lowbad":0,
                    "manufactured": 'null'}}                            
                
                    

                ]


]



gigamon_reports_list = [gigamon_dns_queries, gigamon_dns_requestors, gigamon_protocols_external, gigamon_countries, gigamon_version_count,gigamon_response_count]