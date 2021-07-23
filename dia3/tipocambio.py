#EJEMPLO DE WEBSCRAPPING CON PYTHON
from bs4 import BeautifulSoup
import requests 
import os

url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")

status_code = url.status_code
if status_code == 200:
    # html = BeautifulSoup(url.text,"html.parser")
    html = BeautifulSoup(url.content,"html.parser")
    """<tr class="rgRow" id="ctl00_cphContent_rgTipoCambio_ctl00__0">
				<td class="APLI_fila3" style="width:40%;">Dólar de N.A.</td><td class="APLI_fila2" style="width:30%;">3.948</td><td class="APLI_fila2" style="width:30%;">3.954</td>
			</tr>"""
    
    tabla = html.find('table',{'class':'rgMasterTable'})
    #print(tabla)
    
    
    fr = open('cambio.txt','w')
    fr.write("\n")
    fr.close()
    
    
    for c in range(5):
        moneda = tabla.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(c)});
        
        #find_all trae todo los valores en una lista
        lstTipoCambioDolar = moneda.find_all('td')
        # print(lstTipoCambioDolar)
        strNombreMoneda = lstTipoCambioDolar[0].text
        strValorCompra = lstTipoCambioDolar[1].text
        strValorVenta = lstTipoCambioDolar[2].text
        
        listTipoCambio = strNombreMoneda+","+strValorCompra+","+strValorVenta+'\n'
        # print(strNombreMoneda+" | "+strValorCompra+" | "+strValorVenta)
        
        f = open('cambio.txt','a')
        f.write(listTipoCambio);
        f.close();
     
    fileName = r"cambio.txt"   
    fr = open(fileName,'r')
    fTipoCambio = fr.read()
    # print(fTipoCambio)
    # TipoCambio = cargarTipoCambio(fTipoCambio)
    lstTipoCambioData = []
    lstTipoCambio = fTipoCambio.splitlines()
    del lstTipoCambio[0]
    for objTipoCambio in lstTipoCambio:
        lstTipoCambio = objTipoCambio.split(',')
        moneda = lstTipoCambio[0]
        preciocompra = lstTipoCambio[1]
        precioventa = lstTipoCambio[2]
        dictTipoCambio = {
            'moneda':moneda,
            'preciocompra':preciocompra,
            'precioventa':precioventa
        }
        lstTipoCambioData.append(dictTipoCambio)
    fr.close()
        
        
    print("TIPO DE CAMBIO\n")
    
    for a in lstTipoCambioData:
        print("=====================")
        for clave,valor in a.items():
            print(clave + " : " + valor)
        
else:
    print("error nro" + str(status_code))