from flask import Flask,request

app = Flask(__name__)
@app.route('/')
def index():
    return '''
            <h1>Ejemplos de Rutas con Flask</h1><br />
            <a href="/calculadora"> Ejemplo de Calculadora </a>
            '''

@app.route('/calculadora',methods=['GET','POST'])    
def calculadora():
    form = "<form action='calculadora'  method='POST'>"
    form += '<input type="text" name="n1" size="5" /> '
    form += '''
            <select name="tipo">
                <option>+</option>
                <option>-</option>
                <option>*</option>
                <option>/</option>
            </select>
            '''
    form += '<input type="text" name="n2" size="5" /> '
    form += '<input type="submit" value="calcular" />'
    form += '</form>'
    
    if request.method == 'POST':
        n1=request.form['n1']
        n2=request.form['n2']
        op=request.form['tipo']
        
        if(op=='+'):
            resultado = int(n1) + int(n2)
        elif(op=='-'):
            resultado = int(n1) - int(n2)
        elif(op=='*'):
            resultado = int(n1) * int(n2)   
        elif(op=='/'):
            resultado = int(n1) / int(n2)    
            
        form += '<b>{}</b>'.format(resultado)
        
    return form
    

if __name__ =='__main__':
    app.run(debug=True,port=5000)