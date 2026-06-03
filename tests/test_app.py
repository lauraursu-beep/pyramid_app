from app import create_db_connection

def test_cursor_exists():
    con = create_db_connection()
    cursor = con.cursor() 
    assert cursor 



