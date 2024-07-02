INSERT_DIVIDAS = """
INSERT INTO public.dividas (nome, valor, prazo)
VALUES (%s, %s, %s);
"""