from misClases import ClassCurso

import os
#PROGRAMA PARA GESTÓN DE cursos
#CRUD : CREATE , READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
cursos = []
salir = '-1'

def menuopciones():
    os.system('cls')
    
    print("========= SISTEMA DE REGISTRO DE CURSOS ===========")
    print("===================================================\n\n")
    
    print("*" * 20)
    print("MENÚ DE OPCIONES")
    print("*" * 20)
    print("\n")
    print("[1] REGISTRAR")
    print("[2] MOSTRAR")
    print("[3] ACTUALIZAR")
    print("[4] ELIMINAR")
    print("[0] SALIR")
    print("*" * 20)

def mostrarAlumno():
    os.system('cls')
    print("========= SISTEMA DE REGISTRO DE CURSOS ===========")
    print("===================================================\n\n")
    
    print("=====================")
    print("LISTADO DE CURSOS")
    print("=====================")
    
    for a in cursos:
        print(a.codigo + " | " + a.nombre + " | "+ a.nota)
        print("=====================")
        
def grabarcursos():
    strcursos = ""
    for a in cursos:
        strcursos += "\n" + a.codigo + ","+ a.nombre +","+ a.nota
    return strcursos  

def updateCurso(codigo):
    encontrado=False
    ok = 1
    posicion=-1;
    
    for i in range(len(cursos)):
        nvObj = cursos[i]
        if(nvObj.codigo == codigo):
            encontrado=True
            posicion = i;
            break;
            
    if encontrado == True:
        codigo = input("CODIGO : ")
        nombre = input("NOMBRE : ")
        nota = input("NOTA : ")
        del cursos[posicion]
        nCurso  = ClassCurso(codigo,nombre,nota)
        cursos.append(nCurso)
        
    else:
        ok = 0;
        
    return ok;
    
def deleteCurso(codigo):
    encontrado=False
    ok = 1
    posicion=-1;
    
    for i in range(len(cursos)):
        nvObj = cursos[i]
        if(nvObj.codigo == codigo):
            encontrado=True
            posicion = i;
            break;
            
    if encontrado == True:
        del cursos[posicion]
        
    else:
        ok = 0;
        
    return ok;

#libreria alumno
def cargarcursos(strcursos):
    listCursosData = []
    listCursos = strcursos.splitlines()
    del listCursos[0]
    for objCurso in listCursos:
        lstobjCurso = objCurso.split(',')
        codigo = lstobjCurso[0]
        nombre = lstobjCurso[1]
        nota = lstobjCurso[2]
        
        #instancia e la clase clsAlumno
        nuevoCurso = ClassCurso(codigo,nombre,nota)
        listCursosData.append(nuevoCurso)
        
    return listCursosData

fileName = r"cursos.txt"

if(os.path.isfile(fileName)):
    fr = open(fileName,'r')
    fcursos = fr.read()
    # print(fcursos)
    cursos = cargarcursos(fcursos)
    fr.close()
else:
    fr = open('cursos.txt','w')
    fr.write("\n")
    cursos = []
    fr.close()

while(salir != '0'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    
    if(opcion == "1"):
        os.system('cls')
        print("========= SISTEMA DE REGISTRO DE CURSOS ===========")
        print("===================================================\n\n")
        
        print("REGISTRO")
        print("========\n")
        codigo = input("CODIGO : ")
        nombre = input("NOMBRE : ")
        nota = input("NOTA : ")
        nCurso  = ClassCurso(codigo,nombre,nota)
        cursos.append(nCurso)
        
        print('\nRegistro Exitoso')
        
    elif(opcion == "2"):
        mostrarAlumno()
            
    elif(opcion == "3"):
        os.system('cls')
        print("========= SISTEMA DE REGISTRO DE CURSOS ===========")
        print("===================================================\n\n")
        
        print("ACTUALIZAR")
        print("==========\n")
        
        codcur = input('Ingrese el código: ')
        result = updateCurso(codcur)
        if(result == 1):
            print('\nRegistro Actualizado')
        else:
            print('\nNo se encontró el registro')
            
    elif (opcion == "4"):
        os.system('cls')
        print("========= SISTEMA DE REGISTRO DE CURSOS ===========")
        print("===================================================\n\n")
        
        print("ELIMINAR")
        print("===============\n")
        
        codcur = input('Ingrese el código: ')
        result = deleteCurso(codcur)
        if(result == 1):
            print('\nRegistro eliminado')
        else:
            print('\nNo se encontró el registro')
    
    elif(opcion == "0"):
        salir = opcion
    
    else:
        print("MARCO UNA OPCIÓN INCORRECTA\n")
        continue
    
    if salir != "0":
        print("\n1: Volver al menú   0: salir del sistema ")    
        salir = input()
        
    if(salir == "0"):
        print("ADIOS!!!")
        strcursosGrabar = grabarcursos()
        fw = open(fileName,'w')
        fw.write(strcursosGrabar)
        fw.close()