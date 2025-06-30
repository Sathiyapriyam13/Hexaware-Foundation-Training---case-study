from mysql.connector import connect, Error
from util.DBPropertyUtil import PropertyUtil

def establish_link():
    try:
        props = PropertyUtil.get_property_dict()

        conn = connect(
            host=props.get('host'),
            user=props.get('user'),
            password=props.get('password'),
            database=props.get('database')
        )

        if conn.is_connected():
            print("Connected to MySQL successfully")
            return conn
        else:
            print("Connection failed!")
            return None

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
