class Dash_handler:
    def __init__(self):
        return
    # query used to find the next dashbaord ID. 
    def available_dash_id(self):
        return ("SELECT MAX(dashboard_id)+ 1 FROM plixer.dash_tabs;")

    def create_dashboard(self, dashboard_name, dashboard_id):
  
        return ("INSERT INTO plixer.dash_tabs(dashboard_id, dashboard_name, dashboard_json, locked, plixer, created_by)  VALUES ('{}','{}','[]',0,0,1)".format(dashboard_id,dashboard_name))

    def make_visible(self, dashboard_id, user_id):

        return ("INSERT INTO plixer.users_dashboards(dashboard_id, user_id, is_default)  VALUES ('{}','{}','0')".format(dashboard_id,user_id))

    def make_dash_gadget(self, gadget_name,gadget_id, gadget_json, user_id):
        gadget_id = 'report_' + str(gadget_id)
        return("INSERT INTO plixer.dash_gadgets(gadget_id, gadget_name, gadget_type,gadget_json, category_id,created_by) VALUES ('{}', '{}', 'report', '{}', '2','1')".format(gadget_id,gadget_name,gadget_json))

    def add_gadget_to_dash(self, dash_list, dash_id):

        return ("UPDATE plixer.dash_tabs SET dashboard_json = '{}' WHERE dashboard_id = {}".format(dash_list,dash_id))

    def find_dashboard_id(self, dash_name):

        return ("SELECT dashboard_id FROM plixer.dash_tabs WHERE dashboard_name = '{}'".format(dash_name))

    def delete_dashboard(self, dash_id):

        return ([
                "DELETE FROM plixer.dash_tabs WHERE dashboard_id = '{}'".format(dash_id),
                "DELETE FROM plixer.users_dashboards WHERE dashboard_id = '{}'".format(dash_id)
        ])
