# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 02:51:33 2016

@author: miszk
"""
import random, time
tab = []
for i in range(0,5000):
    tab.append(random.randint(1,100))

print("Tablica nieposortowana: ",tab)
tab1=tab 
tab2=tab 
tab3=tab 
tab4=tab 

def babelkowe(tab):
    start = time.time()
    for t in range(len(tab)-1,1,-1):
        for i in range(0,t):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]= tab[i+1], tab[i]
    end = time.time()
    czas_babelkowe=end-start
    return czas_babelkowe

def wstawianie(tab):
    start2 = time.time()
    for i in range(0,len(tab)):
        c=tab[0]
        for t in range(0,len(tab)-1-i):
            if c>tab[t+1]:
                c = tab[t+1]
        tab.remove(c)
        tab.append(c)
    end2 = time.time()
    czas_wstawianie=end2-start2
    return czas_wstawianie

def wybieranie(tab):
    start3 = time.time()
    for i in range(0,len(tab)):
        mini = tab[i]
        for t in range(i,len(tab)-1):
            if mini > tab[t+1]:
                mini = tab[t+1]
        tab.remove(mini)
        tab.insert(i, mini)
    end3 = time.time()
    czas_wybieranie=end3-start3
    return czas_wybieranie
    
def kopcowanie(tab):
    start5 = time.time()
    def kopiec(tab, end, i):
        lewe_dziecko = 2 * i + 1
        prawe_dziecko = 2 * (i + 1)
        max = i
        if (lewe_dziecko < end) and (tab[i] < tab[lewe_dziecko]):
            max = lewe_dziecko
        if (prawe_dziecko < end) and (tab[max] < tab[prawe_dziecko]):
            max = prawe_dziecko
        if max != i:
            tab[i], tab[max] = tab[max], tab[i]
            kopiec(tab, end, max)
    end = len(tab)
    start = end // 2 - 1 
    for i in range(start, -1, -1):   
        kopiec(tab, end, i)
    for i in range(end-1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        kopiec(tab, i, 0)
    end5 = time.time()
    czas_kopcowania=end5-start5
    return czas_kopcowania
        


def quick(tab,lewy,prawy):
    start11 = time.clock()
    pivot = lewy
    l=lewy
    p=prawy
    while (p>l):
        if (pivot == l):
            if (tab[p] < tab[pivot]):
                tab[p],tab[pivot]= tab[pivot], tab[p]
                pivot = p
                l+=1
            else:
                p-=1
        if (pivot == p):
            if (tab[l] > tab[pivot]):
                tab[l], tab[pivot] = tab[pivot], tab[l]
                pivot = l
                p-=1
            else:
                l+=1
    if (p+1<prawy):
        quick(tab,p+1,prawy)
    if (l>lewy):
        quick(tab,lewy,l-1)
    end11 = time.clock()
    czas_szybkiego=end11-start11
    return czas_szybkiego




czas_szybkiego = quick(tab,0,len(tab)-1)



s = time.clock()
babelkowe(tab2)
k = time.clock()
print('Czas sortowania babelkowego wynosi: %.11f' %(k-s))

s = time.clock()
wstawianie(tab2)
k = time.clock()
print('Czas sortowania przez wstawianie wynosi: %.11f'  %(k-s) )

s = time.clock()
wybieranie(tab3)
k = time.clock()
print('Czas sortowania przez wybieranie wynosi: %.11f'  %(k-s) )

s = time.clock()
kopcowanie(tab4)
k = time.clock()
print('Czas sortowania przez kopcowanie wynosi: %.11f'  %(k-s) )

print('Czas szybkiego sortowania wynosi: %.11f' %czas_szybkiego)

