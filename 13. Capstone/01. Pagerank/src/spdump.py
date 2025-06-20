#[Script 3]

from database.conexion import get_connection


with get_connection() as conn:

    with conn.cursor() as cur:
        
        cur.execute('''SELECT COUNT(from_id) AS inbound, 
                               old_rank, 
                               new_rank,
                               id, 
                               url 
                       FROM Pages 
                       JOIN Links 
                            ON Pages.id = Links.to_id
                      WHERE html IS NOT NULL
                            GROUP BY id ORDER BY inbound DESC''')

        count = 0
        for row in cur :
            if count < 50 : print(row)
            count = count + 1
        print(count, 'rows.')
