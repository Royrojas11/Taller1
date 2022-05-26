############# importar librerias o recursos#####
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'taller1'
mysql = MySQL(app)
# settings A partir de ese momento Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"

# ruta para consultar todos los Usuarios
@app.route('/getUsuarios', methods=['GET'])
def getUsuarios():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idusuario': result[0], 'nombre': result[1], 'iddocumento': result[2],
            'numdocu': result[3],'user': result[4], 'pass': result[5], 'estado': result[6],
            'idperfil': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

# ruta para consultar todos los Login
@app.route('/getLogin', methods=['POST'])
def getLogin():
    try:
        if request.method == 'POST':
            User = request.json['user']
            Pass = request.json['pass']
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM usuarios WHERE user =%s AND pass=%s',
            (User,Pass))
            rv = cur.fetchall()
            return  jsonify(rv[0])
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})
# ruta para consultar por parametro

@app.route('/getAllById/<id>',methods=['GET'])
def getAllById(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE idusuario = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idusuario': result[0], 'nombre': result[1], 'iddocumento': result[2],
            'numdocu': result[3],'user': result[4], 'pass': result[5], 'estado': result[6],
            'idperfil': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getEmpleados', methods=['GET'])
def getEmpleados():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM empleados')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idempleado': result[0], 'idusuario': result[1], 'nombre': result[2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getReservas', methods=['GET'])
def getReservas():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM reservas')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idreserva': result[0], 'idusuario': result[1], 'fecha': result[1], 'hora': result[2],
                      'estado': result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getDetalle', methods=['GET'])
def getDetalle():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM detalle')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'iddetalle': result[0], 'idreserva': result[1], 'respuesta': result[2], 
            'estado': result[3]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


@app.route('/getPerfil', methods=['GET'])
def getPerfil():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM perfil')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idperfil': result[0], 'nombre': result[1], 'estado': result [2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})
        
@app.route('/getDocumentos', methods=['GET'])
def getDocumentos():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM documentos')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'iddocumento': result[0], 'nombre': result[1], 'estado': result [2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getConsulta1', methods=['GET'])
def getConsulta1():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM documentos order by nombre ')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'iddocumento': result[0], 'nombre': result[1], 'estado': result [2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getConsulta2', methods=['GET'])
def getConsulta2():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM perfil order by estado')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idperfil': result[0], 'nombre': result[1], 'estado': result [2]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/getConsulta3', methods=['GET'])
def getConsulta3():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios order by nombre')
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idusuario': result[0], 'nombre': result[1], 'iddocumento': result[2],
            'numdocu': result[3],'user': result[4], 'pass': result[5], 'estado': result[6],
            'idperfil': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE idusuario = %s', (id))
        rv = cur.fetchall()
        cur.close()
        payload = []
        content = {}
        for result in rv:
            content = {'idusuario': result[0], 'nombre': result[1], 'iddocumento': result[2], 'numdocu': result[3], 'user': result[4], 'pass': result[5],
            'estado': result[6], 'idperfil': result[7]}
            payload.append(content)
            content = {}
        return jsonify(payload)
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})
    

#### ruta para crear un registro########
@app.route('/add_Perfil', methods=['POST'])
def add_Perfil():
    try:
        if request.method == 'POST':
            Nombre = request.json['nombre']
            estado = request.json['estado']            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO perfil (nombre,estado) VALUES (%s,%s)", (Nombre,estado))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/add_Documentos', methods=['POST'])
def add_Documentos():
    try:
        if request.method == 'POST':
            Nombre = request.json['nombre'] 
            Estado = request.json['estado']            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO documentos (nombre,estado) VALUES (%s,%s)", (Nombre,Estado))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/add_Usuarios', methods=['POST'])
def add_Usuarios():
    try:
        if request.method == 'POST':
            Nombre = request.json['nombre']
            TipoDocu = request.json['iddocumento']
            Numero = request.json['numdocu']
            User = request.json['user']
            Pass = request.json['pass']
            Estado = request.json['estado']
            Perfil = request.json['idperfil']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO usuarios (nombre,iddocumento,numdocu,user,pass,estado,idperfil) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (Nombre,TipoDocu,Numero,User,Pass,Estado,Perfil))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


@app.route('/add_Reservas', methods=['POST'])
def add_Reservas():
    try:
        if request.method == 'POST':
            idusuario = request.json['idusuario']
            fecha_reserva = request.json['fecha']
            hora_reserva = request.json['hora']
            estado = request.json['stado']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO reservas (idusuario,fecha,hora,estado) VALUES (%s,%s,%s,%s)", 
            (idusuario,fecha_reserva,hora_reserva,estado))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})  


@app.route('/add_Detalle', methods=['POST'])
def add_Detalle():
    try:
        if request.method == 'POST':
            idreserva = request.json['idreserva']
            respuesta = request.json['respuesta']
            estado = request.json['estado']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO detalle (idreserva,respuesta,estado) VALUES (%s,%s,%s)", 
            (idreserva,respuesta,estado))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})
        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/add_Empleados', methods=['POST'])
def add_Empleados():
    try:
        if request.method == 'POST':                 
            Usuario = request.json['idusuario']  
            nombre = request.json['nombre']           
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO empleados (idusuario,nombre) VALUES (%s,%s)", (Usuario,nombre))
            mysql.connection.commit()
            return jsonify({"informacion":"Registro exitoso"})        
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})     

######### ruta para actualizar################

@app.route('/update_Perfil/<id>', methods=['PUT'])
def update_Perfil(id):
    try:
        Nombre = request.json['nombre']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE perfil
        SET nombre = %s,
        estado= %s,
        WHERE idperfil = %s
        """, (Nombre, estado, id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/update_Documentos/<id>', methods=['PUT'])
def update_Documentos(id):
    try:
        Nombre = request.json['nombre']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute(""" UPDATE documentos SET nombre = %s, estado= %s, WHERE iddocumnto = %s""", (Nombre, estado, id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/update_Usuarios/<id>', methods=['PUT'])
def update_Usuarios(id):
    try:
        idperfil = request.json['idperfil']
        Nombre = request.json['nombre']
        TipoDocu = request.json['iddocumento']
        Numdocu = request.json['numdocu']
        user = request.json['user']
        password = request.json['pass']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE usuarios
        SET nombre = %s, iddocumento = %s,numdocu = %s, user = %s, pass = %s, estado = %s, idperfil = %s WHERE 
        idusuario = %s""", (Nombre, TipoDocu, Numdocu, user, password, estado,idperfil, id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/update_Reservas/<id>', methods=['PUT'])
def update_Reservas(id):
    try:
        idusuario = request.json['idusuario']
        fecha_reserva = request.json['fecha']
        hora_reserva = request.json['hora']
        estado = request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE reservas
        SET idusuario = %s,
            fecha = %s,
            hora = %s,
            estado = %s,
        WHERE idreserva = %s
        """, (idusuario, fecha_reserva, hora_reserva, estado, id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/update_Empleados/<id>', methods=['PUT'])
def update_Empleados(id):
    try:
        idusuario = request.json['idusuario']
        Nombre = request.json['nombre']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE empleados
        SET idusuario = %s,
            nombre = %s,
        WHERE idempleado = %s
        """, (idusuario, Nombre, id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


@app.route('/update_Detalle/<id>', methods=['PUT'])
def update_Detalle(id):
    try:
        Reserva = request.json['idreserva']
        Respuesta = request.json['respuesta']
        Estado =request.json['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE detalle
        SET idreserva = %s,
            respuesta = %s,
            estado = %s,
        WHERE iddetalle = %s
        """, (Reserva, Respuesta,Estado,id))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro actualizado"})
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


##################### Ruta Eliminar ############################
@app.route('/delete_Perfil/<id>', methods = ['DELETE'])
def delete_Perfil(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM perfil WHERE idperfil = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/delete_Documentos/<id>', methods = ['DELETE'])
def delete_Documentos(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM documentos WHERE iddocuento = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/delete_Usuarios/<id>', methods = ['DELETE'])
def delete_Usuarios(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM usuarios WHERE usuarios.idusuario = %s", (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})
        

@app.route('/delete_Empleados/<id>', methods = ['DELETE'])
def delete_empleados(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM empleados WHERE empleados.idempleado = %s", (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/delete_Reservas/<id>', methods = ['DELETE'])
def delete_Reservas(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM reservas WHERE idreserva = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})

@app.route('/delete_Detalle/<id>', methods = ['DELETE'])
def delete_Detalle(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM detalle WHERE iddetalle = %s', (id,))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro eliminado"}) 
    except Exception as e:
        print(e)
        return jsonify({"informacion":e})


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
