from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def  inicio():
    return render_template("index.html")

@app.route("/crear", methods=[ "POST"])
def  crear_usuario():
    
    if not Usuario.validar_registro(request.form):
        
        flash("correo es obligatoria")
        return redirect("/")
    pass_hasheado = bcrypt.generate_password_hash(
        request.form['password'])
    
    usuario = {
        "nombre":request.form['nombre'],
        "apellido":request.form['apellido'],
        "email":request.form['email'],
        'password':pass_hasheado
      }
    resultado = Usuario.save(usuario)
    
    if not resultado: 
        flash("no e pudo registrar")
        return redirect("/")
    session["usuario_id"] = resultado
    return redirect("/dashboard")

@app.route("/iniciar_sesion", methods=["POST"])
def iniciar_sesion():
    datos = {
        "email":request.form["email_inicio_sesion"]
    }
    usuario = Usuario.get_by_email(datos)
    print("encontre al usuario", datos)
    
    if not usuario:
        flash("correo &/o contraseña incorrecta")
        return redirect("/")
    
    if bcrypt.check_password_hash(
        usuario.password,
        request.form["password_inicio_sesion"]
    ):
        session["usuario_id"] = usuario.id
        return redirect("/dashboard")
    else:
        flash("Correo i o contraseña incorrectos")
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/")
    usuario = Usuario.get_by_id({
        "id": session["usuario_id"]
    })
    return render_template("dashboard.html", usuario=usuario) 
    


@app.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect("/")