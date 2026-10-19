from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import bcrypt



@app.route("/")
def  inicio():
    return render_template("index.html")

@app.route("/crear", methods=[ "POST"])
def  crear_usuario():
    
    if not Usuario.validar_registro(request.form):
        
        flash("correo es obligatoria")
        return redirect("/")
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    registro_usuario = {
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email'],
        "password":request.form['password'],
        'password':pass_hasheado
      }
    
    Usuario.save()
    return render_template("dashboard.html", Usuario=Usuario)