def FILE_NOT_FOUND(filepath: str):
    return f'Arquivo não encontrado: {filepath}'

def INCORRECT_FILE_FORMAT(line: str):
    return f"""
    Formato de arquivo inválido.
    Esperado: <string1> <string2>
    Recebido:{line}
    """