import mysql.connector
mysql_config = {
'user' : 'tu_usuario', 'host' : 'local_host',
'database': 'nombre_base_datos',
'auth_plugin' : 'mysql_native_password'


}

connection = mysql.connector.conect (**mysql_config)
def get_connection () :
    return connection