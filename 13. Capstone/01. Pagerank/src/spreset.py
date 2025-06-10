from database.conexion import get_connection

with get_connection() as conn:

    with conn.cursor() as cur:
        cur.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
        conn.commit()
        print("All pages set to a rank of 1.0")
