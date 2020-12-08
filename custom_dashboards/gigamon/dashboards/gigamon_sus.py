dashboard_Sus = 'Gigamon - Suspicious Traffic'



sus_protocals = { 'sdfPorts_0': 'in_22-6', 'sdfPorts_1': 'in_3389-6', 'sdfPorts_2': 'in_23-6'}

exporter = 'in_GROUP_ALL'
user_id = 1


sus_1 = {
    'name' : 'Gigamon - Protocol Watch',
    'lang' : 'flowCountByWKP',
    'filters' : sus_protocals,
    'position' : { 'width':12, 'height':13, 'y':0, 'x':0 },
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter': exporter,
    'view':'tableGraph',
    'user_id':user_id,
    'dashboard': dashboard_Sus

}


sus_2 = {
    'name': 'Gigamon - Protocol External',
    'lang': 'custom_protowatch',
    'filters' : sus_protocals,
    'position': {'width':6,'height':6,'x':0,'y':14},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_Sus

}


sus_3 = {
    'name': 'Gigamon - Country Count',
    'lang': 'custom_dstcountrycount',
    'filters' : {},
    'position': {'width':6,'height':6,'x':6,'y':13},
    'direction':'inbound',
    'time_range':'Last24Hours',
    'data_type': 'total',
    'stacked':'stacked',
    'exporter':exporter,
    'view':'table',
    'user_id':user_id,
    'dashboard': dashboard_Sus

}

sus_monitor = [sus_1, sus_2, sus_3]