import openpyxl
import get_host
import json
import extool
import os
import put_host
import json
import ruleNote
import get_rules
from pprint import pprint

#確認檔案存在是否,沒有就創建一個檔案
def ckfile():
    filepath = 'test1.xlsx'
    
    if os.path.isfile(filepath):
        workbook = openpyxl.load_workbook('test1.xlsx')
        
    else:
        workbook = extool.create()
       
    return workbook

#更新處理
def putloop(workbook, sheet, fields):
    setdata = {}
    for row in range(2,sheet.max_row + 1):
        for field in fields:
            setdata[field] = extool.gett(sheet, row, fields.index(field) + 1)
            
        get_id = setdata['id']
        put_host.putdata(setdata, get_id)
        setdata = {}
    print("OK!!!!")
        

#取得處理  
def getloop(workbook,sheet ,data, field):
    index = 2
    base = data.json()['items']
    while index < len(base) :
        for get_data in field:
            try:
                extool.write(workbook, sheet, index,field.index(get_data)+ 1, base[index][get_data] )
            except KeyError:
                print("havn\'t", get_data, "in" ,base[index]['id'], "list.")
                continue
        index += 1
    print("OK!!!!")
    

#取得host
def get_datas(obj):
    field = get_host.set_field()
    sheet = workbook.get_sheet_by_name(obj)
    for x in field:
        extool.write(workbook, sheet, 1, field.index(x)+1,x)  
    host = get_host.a(obj)
    getloop(workbook,sheet,host,field)
    


    
'''def gethost():
    field = get_host.set_field()
    sheet = workbook.get_sheet_by_name("host")
    for x in field:
        extool.write(workbook, sheet, 1, field.index(x)+1,x)  
    host = get_host.a()
    getloop(workbook,sheet,host,field)'''
    
#更新host
def put_datas():
    sheet = workbook.get_sheet_by_name("hosts")
    field = put_host.set_field()
    putloop(workbook, sheet, field)

#取得ruleNote
def getruleNote():
    ruleNote.a()
    
#取得rule
def getrules(get_id):
    get_rules.a(get_id)
    
    
    


    
    
    
workbook = ckfile()   
get_datas('networks')



    
getruleNote()


