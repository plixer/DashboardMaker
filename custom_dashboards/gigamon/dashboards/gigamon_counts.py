### Three Dashboards that are created for Gigamon Devices. 

dashboard_counts = 'Gigamon - Counts'
exporter = 'in_GROUP_ALL'
user_id = 1

#### DNS Monitor Reports ####

count_1 = {
    'name' : 'Gigamon SSL Version',
    'lang' : 'gigamonSSLVersionCount',
    'filters' : {},
    'position' : { 'width':4, 'height':15, 'y':0, 'x':0 },
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter': exporter,
    'view':'tableGraph',
    'user_id':user_id,
    'dashboard': dashboard_counts

}

count_2 = {
    'name': 'Gigamon SMB Version',
    'lang': 'custom_smbversion',
    'filters' : {},
    'position': {'width':4,'height':15,'x':4,'y':0},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'tableGraph',
    'user_id':user_id,
    'dashboard': dashboard_counts

}


count_3 = {
    'name': 'Gigamon HTTP Response',
    'lang': 'custom_responsecount',
    'filters' : {},
    'position': {'width':4,'height':15,'x':8,'y':0},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'tableGraph',
    'user_id':user_id,
    'dashboard': dashboard_counts

}




count_monitor = [count_1, count_2, count_3]