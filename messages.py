def FILE_NOT_FOUND(filepath: str):
    return f'Arquivo não encontrado: {filepath}'

def INCORRECT_FILE_FORMAT(line: str):
    return f"""
    Formato de arquivo inválido.
    Esperado: <string1> <string2>
    Recebido:{line}
    """

def RESULTS_MESSAGE(s1: str, s2: str, answer:str):
    return f"""------------------ RESULTADOS ------------------
INPUTS:
String1: {s1}
String2: {s2}

OUTPUTS:
Menor Supersequência: {answer}
Tamanho: {len(answer)}
------------------------------------------------
"""