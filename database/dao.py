from database.DB_connect import DBConnect
from model.interazione import Interazione


class DAO:

    @staticmethod
    def get_cromosomi():
        conn = DBConnect.get_connection()

        cromosomi = []     # Lista di cromosomi : int

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT cromosoma
                    FROM gene
                    WHERE cromosoma != 0"""

        cursor.execute(query)

        for row in cursor:
            cromosomi.append(row["cromosoma"])

        cursor.close()
        conn.close()
        return cromosomi

    @staticmethod
    def get_interazioni():
        conn = DBConnect.get_connection()

        interazioni = []     # Lista di oggetti Interazione: [(id_gene1, id_gene2, cromosoma_1, cromosoma_2, correlazione),...]

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct id_gene1, id_gene2, g1.cromosoma as cromosoma_1, g2.cromosoma as cromosoma_2, correlazione
                    from gene g1, gene g2, interazione i
                    where i.id_gene1 = g1.id and i.id_gene2 = g2.id and g1.cromosoma != g2.cromosoma"""

        cursor.execute(query)

        for row in cursor:
            interazione = Interazione(id_gene1 = row["id_gene1"],
                                      id_gene2 = row["id_gene2"],
                                      cromosoma_1 = row["cromosoma_1"],
                                      cromosoma_2 = row["cromosoma_2"],
                                      correlazione = row["correlazione"])
            interazioni.append(interazione)

        cursor.close()
        conn.close()
        return interazioni

