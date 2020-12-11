import json

class Json_handler:
    def __init__(self):
        return    

    def report_json(self, report_name, saved_id, exporter, report_lang, data_type ,stacked, filters = None, direction = 'inbound', time_range = 'Last24Hours', ):



        
        def Merge(dict1, dict2):
            res = {**dict1, **dict2}
            return res
  

        exporter = {"sdfDips_0":"{}".format(exporter)}

        if filters != None:
            filters = filters
        else:
            filters = {}
 

        filters= Merge(exporter,filters)

      

        report_json = json.dumps({"saved":{"name":"{}".format(report_name),"id":"{}".format(saved_id)},"reportTypeLang":"{}".format(report_lang),"filters":filters,"byInt":{"selected":0},"dataMode":{"selected":"raw_flows"},"tableView":{"inbound":{"query_limit":{"max_num_rows":"10","offset":0}},"sorting":"DESC","maxNumRows":"10","outbound":{"query_limit":{"max_num_rows":"10","offset":0}},"hidden_cols":["rpt_man_peak","rpt_man_95th"]},"ipDns":{"selected":"dns"},"dataGranularity":{"selected":"auto"},"reportDirections":{"selected":"{}".format(direction)},"graphView":{"showOthers":1,"types":{"default":"pie","selected":"line","available":["pie","total_bar","donut","matrix","step","bar","sankey","hidden","line"]},"graphGranularity":{"seconds":1800,"default":"medium","selected":"medium","sizes":{"high":180,"low":60,"medium":"120"},"available":["low"]},"hidden":False,"graphStyle":{"default":"stacked","selected":"{}".format(stacked),"available":["stacked","nonStacked"]}},"orderBy":"sum_octetdeltacount","dataFormat":{"selected":"normal"},"times":{"clientTimezone":"America/New_York","dateRange":"{}".format(time_range)},"bbp":{"selected":"percent"},"rateTotal":{"selected":"{}".format(data_type),"available":["rate","total"]}})

        return report_json

    def gadget_json(self,view,saved_id):

        gadjet_json = json.dumps({"options":{"tableGraph":{"currentval":"{}".format(view),"opts":[{"lbl":"Table","val":"table"},{"lbl":"Graph","val":"graph"},{"lbl":"Graph and Table","val":"tableGraph"}],"inputtype":"select"},"refresh_interval":{"currentval":10,"validation":"isNumberInteger","inputtype":"text"}},"foreign_key":"{}".format(saved_id)})

        return gadjet_json

    def add_gadget_json(self, gadget_id, position):

        width = position['width']
        height = position['height']
        y_axis = position['y']
        x_axis = position['x']


        add_gadget = json.dumps({"gadget_type":"report","width":width,"y":y_axis,"x":x_axis,"id":"{}".format(gadget_id),"height":height})
        
        return add_gadget

    def add_json_to_list(self, report_json):
        gadget_list = []
        
        gadget_list.append(report_json)

        #strips out extre '' that PSQL doesn't like. 
        gadget_list = '[%s]' % ', '.join(map(str, gadget_list))

        return gadget_list
