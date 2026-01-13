from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def get_cromosomi():
        conn = DBConnect.get_connection()

        cromosomi = []     # Lista di cromosomi : int

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct cromosoma
                    from gene
                    where cromosoma > 0"""

        cursor.execute(query)

        for row in cursor:
            cromosomi.append(row['cromosoma'])

        cursor.close()
        conn.close()
        return cromosomi

    @staticmethod
    def get_correlazioni():
        conn = DBConnect.get_connection()

        correlazioni = []     # Lista di liste, dove la lista interna sarà [cromosoma1, cromosoma2, peso]

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct g1.cromosoma as cromosoma1, g2.cromosoma as cromosoma2, correlazione
                    from gene g1, gene g2, interazione i
                    where g1.id = i.id_gene1 and g2.id = i.id_gene2 and 
                          g1.cromosoma != g2.cromosoma and g1.cromosoma > 0 and g2.cromosoma > 0"""

        cursor.execute(query)

        for row in cursor:
            cromosoma1 = row['cromosoma1']
            cromosoma2 = row['cromosoma2']
            peso = float(row['correlazione'])
            lista = [cromosoma1, cromosoma2, peso]
            correlazioni.append(lista)



        cursor.close()
        conn.close()
        return correlazioni






















