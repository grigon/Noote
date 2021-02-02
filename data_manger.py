from psycopg2.extras import RealDictCursor

import connection

@connection.connection_handler
def get_notes(cursor: RealDictCursor) -> int:
    cursor.execute("""
             SELECT *
             FROM notes
             ORDER BY record_time DESC
             """)
    return cursor.fetchall()

@connection.connection_handler
def get_note_by_id(cursor: RealDictCursor, note_id: str) -> int:
    cursor.execute("""
             SELECT *
             FROM notes
             WHERE id = (%s)
             """, [note_id])
    return cursor.fetchall()

@connection.connection_handler
def delete_note(cursor: RealDictCursor, note_id: int) -> int:
    cursor.execute("""
             DELETE FROM notes
             WHERE id = (%s)
             """, [note_id])

@connection.connection_handler
def add_note(cursor: RealDictCursor, title: str, content: str) -> int:
    cursor.execute("""
             INSERT INTO notes (title, content)
             VALUES ((%s),(%s))
             """,[title, content])

@connection.connection_handler
def update_note(cursor: RealDictCursor, note_id: int, title: str, content: str) -> int:
    cursor.execute("""
             UPDATE notes
             SET title=(%s), content=(%s)
             WHERE id = (%s)
             """,[title, content, note_id])
