
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
import numpy as np
from random import sample
from random import choice
from random import randint
from random import shuffle

from text_transformer.tt_text_transformer_interface import add_changeable
#from text_transformer.tt_text_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import change_one_occurrence

# # this import removes an import error. I don't know why (jbs
# # 2018/12/12). see pt_import_tests.py and try to correct the problem.
# import py_transformer.ast_processor

# from python_transformer.pt_python_transformer_interface import change_identifier_all_occurrences
# from python_transformer.pt_python_transformer_interface import change_all_occurrences_in_strings
from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences

#from sympy import latex, sympify





# in the question (program)
add_changeable('135')    # seed
add_changeable('la')     # the image list
add_changeable('lb')     # the grayScale list
add_changeable('lc')     # the list after filter
add_changeable('i')      # loop variable
                         # error ocurred. see ERROR below
add_changeable('10')     # the image list length


# answers list name
add_changeable(r'\verb+la+')
add_changeable(r'\verb+lb+')
add_changeable(r'\verb+lc+')

# treshold limiar
add_changeable(r'\verb+limTreshold+')

# R, G or B pixel decision
add_changeable(r'\verb+RGBpix+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
add_changeable(r'\verb+3+')
add_changeable(r'\verb+4+')
add_changeable(r'\verb+5+')

# right answers values
add_changeable(r'\verb+11+')
add_changeable(r'\verb+22+')
add_changeable(r'\verb+33+')
add_changeable(r'\verb+44+')
add_changeable(r'\verb+55+')

# wrong answers values
add_changeable(r'\verb+111+')
add_changeable(r'\verb+222+')
add_changeable(r'\verb+333+')
add_changeable(r'\verb+444+')
add_changeable(r'\verb+555+')





# variáveis partilhas entre as funções make_transformations e
# make_transformations_on_results
a  = None
b  = None
c  = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None
rgb_idx = None
limiar = None





def make_transformations():

    ''
    global a
    global b
    global c
    global _1
    global _2
    global _3
    global _4
    global _5
    global rgb_idx
    global limiar
    # question
    _135 = str(randint(1000000, 2000000))
    a = choice(string.ascii_lowercase) # ERROR: isto está mal!!!  a letra 'a'
    # não pode ser uma letra qualquer. porque se for igual a 'n' como
    # há no programa uma variável 'n' isto vai causar um erro
    # deexecuçaõ. Intermitente, o que ainda é pior
    # soluções possíveis:
    # 1. escolher uma letra qualquer execto o 'n'
    # 2. substituir também a variável 'n' escolhendo duas letras diferentes
    # vai ser usada a solução 2 porque assim as versões ainda ficam
    # mais diferentes. a variável 'n' passa também a ser diferente
    [a, b, c, i] = sample(string.ascii_lowercase, 4)
    _10 = randint(19000, 20000)

    
    change_all_occurrences('135',"<b><font color=red><i>" +  _135+ "</font></i></b>")
    change_token_all_occurrences('la',"<b><font color=red><i>" +  a+ "</font></i></b>")
    change_token_all_occurrences('lb',"<b><font color=red><i>" +  b+ "</font></i></b>")
    change_token_all_occurrences('lc',"<b><font color=red><i>" +  c+ "</font></i></b>")
    change_token_all_occurrences('i',"<b><font color=red><i>" +  i+ "</font></i></b>")
    change_all_occurrences('10',"<b><font color=red><i>" +  str(_10)+ "</font></i></b>")


    # answers
    change_all_occurrences(r'\verb+la+',"<b><font color=red><i>" +  r'\verb+' + a + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+lb+',"<b><font color=red><i>" +  r'\verb+' + b + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+lc+',"<b><font color=red><i>" +  r'\verb+' + c + '+'+ "</font></i></b>")
    # indexes with no repetitions
    [_2, _4, _5] = sample(range(_10), 3)
    _1 = randint(0, 255)
    _3 = choice((0, 255))
    black_or_white = 'brancos' if _3 == 255 else 'pretos'
    change_all_occurrences(r'\verb+1+',"<b><font color=red><i>" +  r'\verb+' + str(_1) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+2+',"<b><font color=red><i>" +  r'\verb+' + str(_2) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3+',"<b><font color=red><i>" +  r'\verb+' + black_or_white + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+4+',"<b><font color=red><i>" +  r'\verb+' + str(_4) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+5+',"<b><font color=red><i>" +  r'\verb+' + str(_5) + '+'+ "</font></i></b>")
    rgb_idx = rgb_decision()
    RGBpix = rgb_str(rgb_idx)
    change_all_occurrences(r'\verb+RGBpix+',"<b><font color=red><i>" +  RGBpix+ "</font></i></b>")
    limiar = randint(80, 140)
    change_all_occurrences(r'\verb+limTreshold+',"<b><font color=red><i>" +  str(limiar)+ "</font></i></b>")

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global b
    global c
    global _1
    global _2
    global _3
    global _4
    global _5
    global rgb_idx
    global limiar

    the_list = program.get_global(a)
    the_2nd_list = []
    the_3rd_list = []

    for pixel in the_list:
        the_2nd_list.append(round(rgb2gray(pixel),2))

    for pixel in the_2nd_list:
        the_3rd_list.append(treshold(pixel,limiar))

    answer_1_true = numOfIndexPixelsBiggerThanX(rgb_idx, the_list, _1)
    answer_2_true = the_2nd_list[_2]
    answer_3_true = numPixels(the_3rd_list, _3)
    answer_4_true = (np.array(the_list)).size / (np.array(the_3rd_list)).size
    answer_5_true = the_list[_5]

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><font color=red><i>" +  str(answer_1_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+22+',"<b><font color=red><i>" +  str(answer_2_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+33+',"<b><font color=red><i>" +  str(answer_3_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+44+',"<b><font color=red><i>" +  str(answer_4_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+55+',"<b><font color=red><i>" +  str(answer_5_true)+ "</font></i></b>")

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1
    answer_2_false = answer_2_true + increment2
    answer_3_false = answer_3_true + increment3
    answer_4_false = answer_4_true + increment4
    answer_5_false = the_list[_5 + increment5]

    change_all_occurrences(r'\verb+111+',"<b><font color=red><i>" +  str(answer_1_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+222+',"<b><font color=red><i>" +  str(answer_2_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+333+',"<b><font color=red><i>" +  str(answer_3_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+444+',"<b><font color=red><i>" +  str(answer_4_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+555+',"<b><font color=red><i>" +  str(answer_5_false)+ "</font></i></b>")

#functions that we need

    
def rgb_decision():
    return choice((0, 1, 2))

def rgb_str(var):
    if var == 0:
        return "RED"
    if var == 1:
        return "GREEN"
    return "BLUE"

def rgb2gray(pixel):
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    return 0.2989 * R + 0.5870 * G + 0.1140 * B

def treshold(pixel, value):
    return 0 if pixel < value else 255

def numPixels(pixels, limiar):
    num = 0
    for pixel in pixels:
        if pixel == limiar : num += 1
    return num

def numOfIndexPixelsBiggerThanX(index, pixels, x):
    num = 0
    for pixel in pixels:
        if pixel[index] > x:
            num+= 1
    return num

