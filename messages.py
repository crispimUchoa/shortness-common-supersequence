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

def EXCED_ARGUMENTS_ERROR(args: int):
    return f"""
Erro: Número de argumentos excedeu o esperado. Esperava no máximo 1, recebeu {args}.
Para mais informações, execute scs.py --help
"""

def HELP_TEXT():
    return"""
Uso:
    python scs.py
    ou
    python scs.py <arquivo>
    ou
    python scs.py -a

Descrição:
    Calcula a Shortest Common Supersequence, ou menor supersequência comum,
    entre duas strings lidas de um arquivo. Se nenhum arquivo for passado como
    parâmetro, calcula a solução para ./tests/test_0.txt

Formato do arquivo:
    O arquivo deve conter duas strings separadas por espaço na primeira linha:
    <string1> <string2>

Exemplo:
    string1 string2

Saída esperada:
    Menor supersequência comum entre as duas strings.
    
Exemplos de saída:
    string12
    string21
    

Comandos:
    -h, --help      Mostra essa mensagem
    -a, --all       Calcula a solução para todos os arquivos de ./tests
"""