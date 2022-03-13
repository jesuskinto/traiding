import re
import csv
import pandas as pd
from datetime import datetime, date
from os.path import join
import string
#from testusaadress import split_address
from os import listdir
from os.path import isfile, join

def clean_text(text, replace_commas_for_spaces=True):
    text = str(text)
    if not isinstance(text, float) and not isinstance(text, int):
        text = ''.join([c for c in text if c in string.printable])
        if replace_commas_for_spaces:
            text = text.replace(';', ' ').replace(',', '').replace('"','').replace("['", '').replace("']", '').replace('\xa0','')\
                .replace("\n", '').replace("\t", '').replace("\r", '').strip()
        else:
            text = text.replace(';', ' ').replace(',', '').replace('"','').replace("['", '').replace("']", '').replace('\xa0','').replace("\n", '').strip()
    if text == 'nan':
        text = ''
    return text

def clean_date(lista_fecha):
    print("lista_fecha",len(lista_fecha))
    list_date = []
    for date in lista_fecha:
        #print("date",date)
        if date == 'nan' or date =='NaT' or clean_text(date) =='' or date == 'EXPIRED' or clean_text(date) == 'VOIDED' or clean_text(date) == 'VOID' or clean_text(date) == 'Voided' or clean_text(date) == 'WITHDRAWN':
            list_date.append('')
        else:
            format_correct = re.findall(r'[0-9]+\-[0-9]+\-[0-9]+',date)
            if format_correct:
                list_date.append(clean_text(format_correct))
            else:
                digitos = re.findall(r'[0-9]+',date)
                if digitos:
                    if len(digitos[0]) == 1:
                        mes = '0' + digitos[0]
                        #print("digitos",mes)
                    else:
                        mes = digitos[0]
                    
                    if len(digitos[1]) == 1:
                        dia = '0' + digitos[1]
                        #print("digitos",dia)
                    else:
                        dia = digitos[1]
                    
                    if len(digitos[2]) == 2:
                        ano = '20' + digitos[2]
                        #print("digitos",ano)
                    else:
                        ano = digitos[2]

                    date_format = mes + '/' + dia + '/' + ano
                    #print("date_format",date_format)

                    if date_format:
                        #print("date_format",date_format)
                        date = datetime.strptime(date_format,"%m/%d/%Y")
                        per_date = date.strftime("%Y-%m-%d")
                        list_date.append(per_date)
                    else:
                        list_date.append(date_format)
                else:
                    #print("error fecha",date)
                    list_date.append('')
        
    return list_date




def execute_excel():
    excel_list = [arch for arch in listdir('raw_data/') if isfile(join('raw_data/', arch))]
    for excel_name in excel_list:
        # Recorremos los excel
        print("\nEstas dentro del excel: \n", excel_name)
        if excel_name != '.DS_Store':
            getData(excel_name)

def getData(excel_name):
    xls = pd.ExcelFile('raw_data/'+excel_name)
    name_sheet = xls.sheet_names
    print("name_sheet",name_sheet)
    for name in name_sheet:
        print('name_sheet :', excel_name)
        print('Obteniendo datos de :', name)
        if name == 'Operaciones':
            df = pd.read_excel('raw_data/'+excel_name, sheet_name = name,skiprows= 0)
            print(df)
            print(df.columns)

            for x in range (len(df['Trade #'])):
                traiding = str(df['Trade #'][x])
                type= str(df['Type'][x])
                symbol= str(df['Symbol'][x])
                signal= str(df['Signal'][x])
                date= str(df['Date/Time'][x])
                price= str(df['Price'][x])
                profit= str(df['Profit %'][x])
                drawdown= str(df['Drawdown %'][x])
                    
                if traiding != 'nan':
                    lista1.append(clean_text(traiding))
                    lista2.append(clean_text(type))
                    lista3.append(clean_text(symbol))
                    lista4.append(clean_text(signal))
                    lista5.append(clean_text(date))
                    lista6.append(clean_text(price))
                    lista7.append(clean_text(profit))
                    lista8.append(clean_text(drawdown))
        
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
lista7 = []
lista8 = []

execute_excel()

print("lista1",len(lista1))
print("lista2",len(lista2))

df = pd.DataFrame({'trade': lista1,
    'type': lista2,
    'symbol': lista3,
    'signal': lista4,
    'date': lista5,
    'price': lista6,
    'profit': lista7,
    'drawdown': lista8,
    })

js = df.to_json('process_data/salida.json',orient = 'records')
print(js)

#Close actividad1.txt