import psycopg2
from config import DB_CONFIG
def get_connection():
    """Create and return a database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.OperationalError as e:
        print(f"[ERROR] Could not connect to the database: {e}")
        raise
def get_cursor(conn):
    """Return a cursor from the given connection."""
    return conn.cursor()
 