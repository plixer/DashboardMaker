import json

class Report_handler:
    def __init__(self):
        return

    def available_saved_id(self):
        return ("SELECT COALESCE(MAX(saved_id),0) + 1 FROM reporting.saved_reports;")



    def create_report_query(self, saved_id, saved_name, report_obj, created_by):
        if saved_id == None:
            saved_id = 1
        return ("INSERT INTO reporting.saved_reports(saved_id, saved_name, report_obj, hasthreshold, is_hidden, created_by)  VALUES ('{}','{}','{}', 0, 0, {})".format(saved_id,saved_name,report_obj,created_by))


    def get_saved_report_id(self, report_name):
        return("SELECT saved_id FROM reporting.saved_reports WHERE saved_name = '{}'".format(report_name))

    def get_report_id(self, report_lang):
        return("select * from plixer.report_types where rpt_lang = '{}' ".format(report_lang))

    def get_gadget_id(self, report_name):
        return("SELECT gadget_id FROM plixer.dash_gadgets WHERE gadget_name = '{}'".format(report_name))


    def delete_report_as_gadget(self, report_name):
        return("DELETE FROM plixer.dash_gadgets WHERE gadget_name = '{}'".format(report_name))

    def delete_saved_report(self, saved_name):
        return("DELETE FROM reporting.saved_reports WHERE saved_name = '{}'".format(saved_name))

    def delete_designed_report(self, report_id, report_name):
        return([
                "DELETE FROM plixer.report_types WHERE rt_id = '{}'".format(report_id), 
                
                "DELETE FROM plixer.report_types_columns WHERE rt_id = '{}'".format(report_id),

                "DELETE FROM plixer.report_types_groupby WHERE rt_id = '{}'".format(report_id),

                "DELETE FROM plixer.report_types_operations WHERE rt_id = '{}'".format(report_id),

                "DELETE FROM plixer.report_types_select WHERE rt_id = '{}'".format(report_id),

                "DELETE FROM languages.custom WHERE id = '{}'".format(report_name),


                ])

    def get_report_object(self, report_name):
        return "SELECT * FROM languages.custom WHERE string = '{}'".format(report_name)
