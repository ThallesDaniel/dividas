SELECT_DIVIDAS = """SELECT id,
                           nome,
                           valor,
                           to_char(prazo, 'HH24:MI - DD/MM/YYYY') AS prazo_formatado
                        FROM dividas d
                        """
