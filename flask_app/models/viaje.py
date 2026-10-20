from flask_app.config.mysqlconnection import connectToMySQL

class Viaje:
    def __init__(self, data):
        self.id = data.get('id')
        self.destino = data.get('destino')
        self.fecha_inicio = data.get('fecha_inicio')
        self.fecha_fin = data.get('fecha_fin')
        self.itinerario = data.get('itinerario')     
        self.usuario_id = data.get('usuario_id')
    @classmethod
    def save(cls, datos):
            query = "INSERT INTO viajes (destino, fecha_inicio, fecha_fin, itinerario, usuario_id) VALUES (%(destino)s, %(fecha_inicio)s, %(fecha_fin)s,%(itinerario)s, %(usuario_id)s"
    
            return connectToMySQL('viajero_frecuente').query_db(query, datos)
    @classmethod
    def get_all_by_usuario(cls, datos):
                query = """
                SELECT * FROM VIAJES WHERE usuarios_id = %(usuario_id)s
                ORDEN BY fecha_inicio ASC
                
                """
                resultado = connectToMySQL('viajero_frecuente').query_db(query,datos)
                
                viajes = []
                
                if resultado:
                    for viajes in resultado:
                        viajes.append(cls(viajes))
                return viajes
    @classmethod
    def get_by_id(cls,datos):
        query = "SELECT * FROM viajes WHERE id = %(id)s;"
        resultado = connectToMySQL('viajero_frecuente').query_db(query,datos)       
        if not resultado:
            return None
        return cls(resultado[0])
    @classmethod
    def update(cls, datos):
        query  = """
        UPDATE viajes
        SET destino = %(destino)s,
        fecha_inicio = %(fecha_inicio)s,
        fecha_fin = %(fecha_fin)s,
        itinerario = %(itinerario)s
        WHERE id = %(id)s AND usuario_id = %(usuario_id)s;
    
        """
        return connectToMySQL('viajero_frecuente').query_db(cls,datos)
        
    @classmethod
    def delete(cls, data):
            query = "DELETE FROM viajes WHERE id = %(id)s AND usuario_id = %(usuario_id)s;"
            return connectToMySQL('viajero_frecuente').query_db(query, data)
                
                
                