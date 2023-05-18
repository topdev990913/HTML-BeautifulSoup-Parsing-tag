from bs4 import BeautifulSoup
import re
import string
import pandas as pd
f = open('db1.txt', 'r', encoding="utf-8")
response = f.read()
soup = BeautifulSoup(response, 'html.parser')   
tables = soup.findAll('table', attrs = {'class':'tabla_ancha'}) 
# print(len(tables))
Marca = []
Model_tipo = []
Inicio = []
Fin = []
C_C = []
N_decilind = []
G_D = []
P_KW = []
cvf = []
cv = []
Valor_euros = []
Python_list = []

for i in range(len(tables)):
    thead = tables[i].find("thead")
    trs_marca = thead.findChildren(recursive=False)  
    tbody = tables[i].find("tbody") 
    trs = tbody.findChildren(recursive=False)
    for k in range(len(trs)):
     if k==0:
      marca_individual = trs_marca[k].text.replace("Marca: ", "").replace("\n", "")
     Marca.append(marca_individual)
     tds = trs[k].findChildren(recursive=False)
     print(len(tds)) 
     new_data = {}   
     if len(tds)!=10:
        break 
     for j in range(len(tds)):
        td_text = tds[j].text.replace("\xa0", "")
        print(td_text)
        if j==0:
           Model_tipo.append(td_text)
           new_data["Model_tipo"] = td_text
        if j==1:
           Inicio.append(td_text)
           new_data["Inicio"] = td_text
        if j==2:
           Fin.append(td_text)
           new_data["Fin"] = td_text
        if j==3:
           C_C.append(td_text)
           new_data["C_C"] = td_text
        if j==4:
           N_decilind.append(td_text)
           new_data["N_decilind"] = td_text
        if j==5:
           G_D.append(td_text)
           new_data["G_D"] = td_text
        if j==6:
           P_KW.append(td_text)
           new_data["P_KW"] = td_text
        if j==7:
           cvf.append(td_text)
           new_data["cvf"] = td_text
        if j==8:
           cv.append(td_text)
           new_data["cv"] = td_text
        if j==9:
           Valor_euros.append(td_text)
           new_data["Valor_euros"] = td_text
        Python_list.append(new_data)

Marca = Marca[:-4]
print(len(Marca), len(Inicio))
dic = {'Marca': Marca, 'Model_tipo': Model_tipo, 'Inicio': Inicio, 'Fin': Fin, 'C_C': C_C,
                 'N_decilind': N_decilind, 'G_D': G_D, 'P_KW': P_KW, 'cvf': cvf, 'cv': cv, 'Valor_euros': Valor_euros}
df = pd.DataFrame(dic)

df.to_csv('Result.csv')  
print(Python_list)   
# print(Marca)
# print(len(Marca), len(Inicio))