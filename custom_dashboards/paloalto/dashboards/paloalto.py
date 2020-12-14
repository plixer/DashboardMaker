
### Three Dashboards that are created for Palo Alto Devices. 

dashboard_PALO = 'Palo Alto - General'
exporter = 'in_GROUP_ALL'
user_id = 1

#### Palo Alto Reports ####

report_1 = {
    'name' : 'Palo Alto - NAT',
    'lang' : 'postTranslationsNAT',
    'filters' : {"sdfPorts_0":"in_53-17"},
    'position' : { 'width':12, 'height':14, 'y':0, 'x':0 },
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter': exporter,
    'view':'graph',
    'user_id':user_id,
    'dashboard': dashboard_PALO

}

report_2 = {
    'name': 'Palo Alto - Apps ',
    'lang': 'paApplications',
    'filters' : {"sdfPorts_0":"in_53-17"},
    'position': {'width':4,'height':9,'x':0,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_PALO

}


report_3 = {
    'name': 'Palo Alto - Users',
    'lang': 'paUsers',
    'filters' : {},
    'position': {'width':4,'height':9,'x':4,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_PALO

}


report_4 = {
    'name': 'Palo Alto - Events',
    'lang': 'paFirewallEvents',
    'filters' : {},
    'position': {'width':4,'height':9,'x':8,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_PALO

}


paloalto_dash = [report_1, report_2, report_3, report_4]