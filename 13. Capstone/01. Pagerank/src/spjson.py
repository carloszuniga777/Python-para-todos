#[Script 4]
from database.conexion import get_connection
import os

with get_connection() as conn:

    with conn.cursor() as cur:

        print("Creating JSON output on spider.js...")
        howmany = int(input("How many nodes? "))

        cur.execute('''SELECT COUNT(from_id) AS inbound, 
                               old_rank, 
                               new_rank, 
                               id, 
                               url 
                        FROM Pages 
                        JOIN Links 
                            ON Pages.id = Links.to_id
                        WHERE html IS NOT NULL AND ERROR IS NULL
                        GROUP BY id ORDER BY id,inbound''')
        

    
        #--------- Contruir la ruta del archivo--------------- 

        # Obtiene la ruta del directorio actual del script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construye la ruta al archivo independientemente de dónde se abra el proyecto
        file_path = os.path.join(current_dir, 'spider.js')                      
        file_path = os.path.abspath(file_path)

        #------------------------------------------------------

        # Abre el archivo spider.js 
        with open(file_path,'w') as fhand:
            nodes = list()
            maxrank = None
            minrank = None
            for row in cur :
                nodes.append(row)
                rank = row[2]
                if maxrank is None or maxrank < rank: maxrank = rank
                if minrank is None or minrank > rank : minrank = rank
                if len(nodes) > howmany : break

            if maxrank == minrank or maxrank is None or minrank is None:
                print("Error - please run sprank.py to compute page rank")
                quit()

            fhand.write('spiderJson = {"nodes":[\n')
            count = 0
            map = dict()
            ranks = dict()
            for row in nodes :
                if count > 0 : fhand.write(',\n')
                # print row
                rank = row[2]
                rank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
                fhand.write('{'+'"weight":'+str(row[0])+',"rank":'+str(rank)+',')
                fhand.write(' "id":'+str(row[3])+', "url":"'+row[4]+'"}')
                map[row[3]] = count
                ranks[row[3]] = rank
                count = count + 1
            fhand.write('],\n')

            cur.execute('''SELECT DISTINCT from_id, to_id FROM Links''')
            fhand.write('"links":[\n')

            count = 0
            for row in cur :
                # print row
                if row[0] not in map or row[1] not in map : continue
                if count > 0 : fhand.write(',\n')
                rank = ranks[row[0]]
                srank = 19 * ( (rank - minrank) / (maxrank - minrank) ) 
                fhand.write('{"source":'+str(map[row[0]])+',"target":'+str(map[row[1]])+',"value":3}')
                count = count + 1
            fhand.write(']};')

        print("Open force.html in a browser to view the visualization")
