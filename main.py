import requests
def get_trmsa_file():
    requestsfile = requests.get('https://www.trmsa.org.tw/front/metal?qryMetal=co')
    requestsfile.encoding='utf-8'
    return requestsfile.text
def index_json_file(html_file):
    start_pos = html_file.index('mainJsonString')+17
    end_pos = html_file.index('var mainXmlString')-3
    return html_file[start_pos:end_pos]
json_file = index_json_file(get_trmsa_file())
date_list = []

pos_start_index = int(0)
keep_while = True
while(keep_while == True):
    s_p = json_file.find('date":"',pos_start_index)+7
    if s_p <= 7:
        keep_while = False
        break
    else:
        e_p = json_file.find('","closingLow',pos_start_index)
        pos_start_index = e_p+3
        date_list.append(json_file[s_p:e_p])
max_year = str(0)
for element in date_list:
    if int(element[0:4]) > int(max_year):
        max_year = str(element[0:4])
max_y_mon = str(0)
for element in date_list:
    if str(max_year) in element:
        if int(element[5:7]) > int(max_y_mon):
            max_y_mon = str(element[5:7])
max_y_m_day = str(0)
for element in date_list:
    if (str(max_year)+'-'+str(max_y_mon)) in str(element):
        if int(element[8:]) > int(max_y_m_day):
            max_y_m_day = str(element[8:])
max_date = str(max_year+'-'+max_y_mon+'-'+max_y_m_day)

highpost_start_find = json_file.index(max_date)
print(json_file[json_file.index('spotHigh":',highpost_start_find)+10:json_file.index(',"futureClosingLow',highpost_start_find)])