#N=4, M=5, Итого: 20 повторений
def strcounter(stroka):
    for sym in set(stroka):
        counter=0
        for sub_sym in stroka:
            if sym==sub_sym:
                counter+=1
        print(sym, counter)

def strcounter_new(stroka):
    syms_counter={}
    for sym in stroka:
        syms_counter[symb]=syms_counter.get(sym, 0)+1
    print(syms_counterms_cou)
stroka='aabbcd'
print(set(stroka))
strcounter(stroka)




