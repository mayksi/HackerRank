# Enter your code here. Read input from STDIN. Print output to STDOUT
OPEN_SQ_PARA = '['
CLOSE_SQ_PARA = ']'
OPEN_CU_PARA = '{'
CLOSE_CU_PARA = '}'
OPEN_RD_PARA = '('
CLOSE_RD_PARA = ')'

PARA_PAIRS_DICT = {CLOSE_SQ_PARA: OPEN_SQ_PARA,
                   CLOSE_CU_PARA: OPEN_CU_PARA,
                   CLOSE_RD_PARA: OPEN_RD_PARA}

def validateParanthesis(paraString):
    '''
    Method to check if parathesis string is balanced
    '''
    stk = []

    validParantheses = True
    for ch in paraString:
        if not PARA_PAIRS_DICT.has_key(ch): # check if the paranthesis is open one
            stk.append(ch)
        else: # paranthesis is closed one
            if len(stk) > 0 and stk[-1] == PARA_PAIRS_DICT[ch]:
                stk.pop()
            else:
                validParantheses = False
                break
    return validParantheses and len(stk) == 0



fl = open('balanced_parantheses_input.txt')
testCases = int(fl.readline().strip())

for _ in range(testCases):
    if validateParanthesis(fl.readline().strip()):
        print 'YES'
    else:
        print 'NO'
