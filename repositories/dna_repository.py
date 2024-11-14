import sqlite3


class DNARepository:
    def __init__(self):
        self.db_name = 'MUTANT.db'

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dna_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dna TEXT UNIQUE,
                    is_mutant BOOLEAN
                )
            ''')
            connection.commit()

    def save_result(self, dna: list[str], is_mutant: bool):
        dna_str = ''.join(dna)

        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO dna_results (dna, is_mutant)
                VALUES (?, ?)
            ''', (dna_str, is_mutant))
            connection.commit()

    def obtener_adn(self, dna: list[str]):
        dna_str = ''.join(dna)

        with self._get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT is_mutant FROM dna_results WHERE dna = ?
            ''', (dna_str,))
            result = cursor.fetchone()

        return result
