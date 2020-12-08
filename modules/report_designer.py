import itertools

class Report_designer():
    def __init__(self):
        self.headers = 'headers'
        self.rpt_lang = 'rpt_lang'
        self.pretty_name = 'pretty_name'
        self.menu_group = 'menu_group'
        self.graph_type = 'graph_type'
        self.bi_width = 'bi_width'
        self.totals_table = 'totals_table'
        self.group_by = 'group_by'
        self.trend_by = 'trend_by'
        self.col_name = 'col_name'
        self.col_order = 'col_order'
        self.col_lang = 'col_lang'
        self.col_style = 'col_style'
        self.col_attr = 'col_header_title_attr'
        self.col_width = 'col_width'
        self.col_name_trend = 'col_name_sum'
        self.col_nam_reg='col_nam_reg'
        self.col_operation = 'col_operation'
        self.default_col = 'default_col'
        self.availableratetotals = "availableratetotals"
        self.defaultratetotal = 'defaultratetotal'
        self.availablegraphstyles = 'availablegraphstyles'
        self.defaultgraphstyle = 'defaultgraphstyle'
        self.showother = 'showother'
        self.percentok = 'percentok'
        self.units = 'units'
        self.total_operation = 'total_operation'
        self.lowbad = 'lowbad'
        self.manufactured = 'manufactured'
        self.select = 'select'

        return

    def _unpack(self, columns):
        # helper function used to format list into a query for SQL
        return ",".join(map(str, columns))  

    def get_available_id(self):
        return(f"SELECT MAX(rt_id)+ 1 FROM plixer.report_types;")

    def check_if_exists(self, report_obj):
        for report in report_obj:
            print(report)
        return
    
    def report_headers(self, report_id, report_obj ):

        for report in report_obj:
            for element in report:
                if self.headers in element:
                    header_element = element[self.headers]
                    print(header_element)
                    try:
                        rpt_lang = header_element[self.rpt_lang]
                        menu_group = header_element[self.menu_group]
                        graph_type = header_element[self.graph_type]
                        bi_width = header_element[self.bi_width]
                        totals_table = header_element[self.totals_table]
                        print(f'creating insert statment for {rpt_lang}')
                        headers = (f"INSERT INTO plixer.report_types (rt_id, rpt_lang, menugroup, graphtype, biwidth, totalstable, rt_source) VALUES ('{report_id}','{rpt_lang}','{menu_group}','{graph_type}',{bi_width},{totals_table},1);")
                        return headers
                    except Exception as err:
                        print('error creating report headers, make sure you have all the needed keys rpt_lang, menu_group, graph_type, bi_width, totals_table ')
                        print(err)
                        return

                else:
                    print('report object does not have headers')
                    return
        # return(f"INSERT INTO plixer.report_types (rt_id, rpt_lang, menugroup, graphtype, biwidth, totalstable, rt_source) VALUES ('{report_id}','{lang_key}','{menu_group}','{graph_type}',950,0,0);")





    def create_report_columns(self, report_id, report_object):

        #takes in a list that includes all the report columns, outputs a list that will be used to create the insert statement.


        all_report_column = []

        #attributed needed for report columns. 



        for report in report_object:
            for column in report:

                required_headers = [self.col_name,self.col_order,self.col_lang,self.col_style,self.col_attr,self.col_width]
                if self.group_by in column:
                    try:
                        column_groupby = column[self.group_by]
                        col_name = column_groupby[self.col_name]
                        col_order = column_groupby[self.col_order]
                        col_lang = column_groupby[self.col_lang]
                        col_style = column_groupby[self.col_style]
                        col_attr = column_groupby[self.col_attr]
                        col_width = column_groupby[self.col_width]
                    except KeyError as error:
                        print(f'unable to create all required headers, verify that your object has all of the required headers {required_headers}')
                        print(column_groupby.keys())
                        print(error)
                        return
                    
                    print(f'creating columns for {col_name}, {col_lang}')
                    column_group  = f"('{report_id}','{col_name}','{col_order}','{col_lang}','{col_style}','{col_attr}','{col_width}')"
                    all_report_column.append(column_group)

                elif self.trend_by in column:
                    column_trend = column[self.trend_by]
                    col_name = column_trend[self.col_name_trend]
                    col_order_trend = column_trend[self.col_order]
                    col_lang = column_trend[self.col_lang]
                    col_style = column_trend[self.col_style]
                    col_attr = column_trend[self.col_attr]
                    col_width = column_trend[self.col_width]
                    column_trend = f"('{report_id}','{col_name}','{col_order_trend}','{col_lang}','{col_style}','{col_attr}','{col_width}')"
                    all_report_column.append(column_trend)





        values = self._unpack(all_report_column)
      
    
        return (f"INSERT INTO plixer.report_types_columns (rt_id,col_name,col_order,col_lang,col_style,col_header_title_attr,col_width) VALUES {values}")




    def report_types_groupby(self, report_id, report_columns):
        


        all_report_column = []


        for report in report_columns:

            for column in report:

                if self.group_by in column:
                    
                    column_name = column[self.group_by][self.col_name]
                    print(f'creating groupbys for {column_name}')
                    column  = f"('{report_id}','{column_name}')"
                    all_report_column.append(column)

        values = self._unpack(all_report_column)


        return(f"INSERT INTO plixer.report_types_groupby (rt_id, col_name)VALUES{values}")

    def report_type_operations(self, report_id, report_columns):

    
        all_report_column = []

        for report in report_columns:

            for column in report:
                if self.trend_by in column:
                    col_trend= column[self.trend_by]
                    col_name = col_trend[self.col_nam_reg]
                    operation = col_trend[self.col_operation]
                    default_col = col_trend[self.default_col]
                    availableratetotals = col_trend[self.availableratetotals]
                    defaultratetotal = col_trend[self.defaultratetotal]
                    availablegraphstyles = col_trend[self.availablegraphstyles]
                    defaultgraphstyle = col_trend[self.defaultgraphstyle]
                    showother = col_trend[self.showother]
                    percentok = col_trend[self.percentok]
                    units = col_trend[self.units]
                    total_operation = col_trend[self.total_operation]
                    lowbad = col_trend[self.lowbad]
                    print(f'creating operations for {col_name}')
                    column = (f"('{report_id}','{col_name}','{operation}','{default_col}','{availableratetotals}','{defaultratetotal}','{availablegraphstyles}','{defaultgraphstyle}',{showother},{percentok},'{units}','{total_operation}',{lowbad})")
                    all_report_column.append(column)

        values = self._unpack(all_report_column)



        return(f"INSERT INTO plixer.report_types_operations(rt_id, col_name, operation, default_col, availableratetotals,defaultratetotal, availablegraphstyles, defaultgraphstyle, showother,percentok, units, total_operation, lowbad) VALUES {values}")

    def report_type_select(self, report_id, report_columns):


        all_report_column = []

        for report in report_columns:
            for column in report:
                if self.group_by in column:
                    
                    column_name = column[self.group_by][self.col_name]
                    manufactured = column[self.group_by][self.manufactured]
                    column  = f"('{report_id}', '{column_name}', {manufactured})"
                    print(f'creating groupby select for {column_name}')
                    all_report_column.append(column)

                elif self.select in column:
                    select_name = column[self.select][self.col_name]
                    manufactured_name = column[self.select][self.manufactured]
                    column  = f"('{report_id}', '{select_name}', {manufactured_name})"
                    print(f'creating tendby select for {select_name}')
                    all_report_column.append(column)

        values = self._unpack(all_report_column)

        return(f"INSERT INTO plixer.report_types_select(rt_id, col_name, manufactured)VALUES {values}")

    def add_lang_kery(self, report_columns ):
        for report in report_columns:
            for column in report:
                if self.headers in column:
                    
                    column_header = column[self.headers]
                    report_lang = column_header[self.rpt_lang]
                    report_name = column_header[self.pretty_name]
                    print(f'adding langkery for {report_lang} to make pretty name {report_name}')

        return(f"INSERT INTO languages.custom (id,string) VALUES ('{report_lang}','{report_name}');")

    def alter_sequence(self, report_id):
        return(f"ALTER SEQUENCE plixer.report_types_rt_id_seq RESTART WITH {report_id};")

    def refresh_viwes(self):
        return('REFRESH MATERIALIZED VIEW plixer.report_types_reports_in_group; REFRESH MATERIALIZED VIEW plixer.report_types_template2id; REFRESH MATERIALIZED VIEW plixer.report_types_all_report_groups;')




