import ply.lex as lex
from ply import yacc

# Análise Léxica
reserved = {
   'inprograma': 'inprograma',
   'fmprograma': 'fmprograma',
   'ni': 'ni',
   'nd': 'nd',
   'input': 'input',
   'saida': 'saida',
   'se' : 'se',
   'senao' : 'senao',
   'enquanto' : 'enquanto',
   'para' : 'para',
}


tokens = [
    'INTEIRO',
    'DOUBLE',
    'STRING',
    'INT',
    'VARIAVEL',
    'OP_MAT_ADICAO',
    'OP_MAT_SUB',
    'OP_MAT_MULT',
    'OP_MAT_POT',
    'OP_MAT_DIV',
    'OP_EXEC_VIRGULA',
    'OP_ATRIB_IGUAL',
    'OP_ATRIB_MAIS_IGUAL',
    'OP_REL_DUPLO_IGUAL',
    'OP_REL_MENOR',
    'OP_REL_MAIOR',
    'OP_FINAL_LINHA_PONTO_VIRGULA', 
    'OP_PRIO_ABRE_PARENTESES',
    'OP_PRIO_FECHA_PARENTESES',
    'OP_PRIO_ABRE_CHAVES',
    'OP_PRIO_FECHA_CHAVES',
] + list(reserved.values())  # Concatenando com as palavras reservadas para verificação

# Regras de expressão regular (RegEx) para tokens simples
t_ENQUANTO = r'ENQUANTO'
t_se = r'se'
t_ELSE = r'ELSE'
t_PARA = r'PARA'
t_ESCREVA = r'ESCREVA'
t_LEIA = r'LEIA'
t_EM = r'EM'
t_RANGE = r'RANGE'
t_ADICAO = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_POT = r'\*\*'
t_DIV = r'/'
t_OP_FINAL_LINHA_PONTO_VIRGULA = r'\;'
t_VIRGULA = r'\,'
t_IGUAL = r'\='
t_MAIS_IGUAL = r'\+\='
t_DUPLO_IGUAL = r'\=\=' 
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_ABRE_CHAVES = r'\{'
t_FECHA_CHAVES = r'\}'

t_ignore = ' \t'  # Ignora espaço e tabulação

# Regras de expressão regular (RegEx) para tokens mais "complexos"


def t_STRING(t):
    r'("[^"]*")'
    return t

def t_DOUBLE(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    return t

def t_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIAVEL(t):
    r'[a-z][a-z_0-9]*'
    return t

def t_INT(t):
    r'INT'
    return t

# Define uma regra para que seja possível rastrear o números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra de tratamento de erros
erroslexicos = []
def t_error(t):
    erroslexicos.append(t)
    t.lexer.skip(1)

# Análise Sintática

def p_declaracoes_single(p):
    '''
    declaracoes : declaracao
    '''

def p_declaracoes_mult(p):
    '''
    declaracoes :  declaracao bloco
    '''
def p_bloco(p):
    '''
    bloco : OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES declaracao blocos OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita escrita impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES escrita escrita expr impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao param_cond OP_FINAL_LINHA_PONTO_VIRGULA OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES param_cond OP_FINAL_LINHA_PONTO_VIRGULA impressao OP_PRIO_FECHA_CHAVES
          | OP_PRIO_ABRE_CHAVES impressao expr OP_PRIO_FECHA_CHAVES
          
    '''

def p_declaracao_ENQUANTO(p):
    '''
    declaracao : ENQUANTO param_cond bloco
               | declaracao ENQUANTO param_cond bloco
    '''

def p_declaracao_para(p):
    '''
    declaracao : PARA VARIAVEL EM RANGE OP_PRIO_ABRE_PARENTESES INTEIRO OP_EXEC_VIRGULA INTEIRO OP_PRIO_FECHA_PARENTESES bloco
    '''

def p_declaracao_atribuicaoValorVariavel(p):
    '''
    declaracao : VARIAVEL OP_ATRIB_IGUAL expr OP_FINAL_LINHA_PONTO_VIRGULA
    
    '''

def p_declaracao_condicionais(p):
    '''
    declaracao : declaracao SE param_cond bloco
    '''

def p_declaracao_funcao_invocada(p):
    '''
    declaracao : funcao OP_FINAL_LINHA_PONTO_VIRGULA
               | 
               | 
    '''

def p_declaracao_definir_funcao(p):
    '''
    declaracao : funcao OP_PRIO_ABRE_CHAVES declaracoes OP_PRIO_FECHA_CHAVES
    '''

def p_parametro_condicional(p):
    '''
    param_cond :  
                | 
    '''

def p_impressao(p):
    '''impressao : 
                 | 
    '''

def p_escrita(p):
    '''escrita : 
    '''


def p_expressao_variavel(p):
    '''

    '''


def p_expressao_operacao(p):
    '''

    '''

def p_parametro_vazio(p):
    '''

    '''


def p_parametro(p):
    '''

    '''

def p_regra_funcao(p):
    '''

    '''

def p_senao_se(p):
    '''

    '''

errossintaticos = []
parser = yacc.yacc()

erros = 0
saidas = []

lexer = lex.lex()


