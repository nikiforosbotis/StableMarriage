#A program that implements the Gale-Shapley algorithm for Stable Marriages.
#Author: Nikiforos Botis
#Date: May 2015

import json
import sys

#Opens and reads the json file which includes the preferences of men and women
f = open(sys.argv[2], 'r')
j = json.load(f)
f.close()

#This function returns the result of the algorithm. Parameter 'a' refers to the preferences of the gender
#that we want to find the optimized solution for, while the parameter 'b' refers to the preferences of the other gender.
def StableMatching(a, b):
    "this function returns a stable matching"
    dict_a = a.keys()
    #This list contains the names of all the men (if we are want to optimize for them) or the women (respectively).
    names1 = list(dict_a)
    dict_b = b.keys()
    #This list contains the names of all the women (if we want to optimize for the men) or the men (respectively).
    names2 = list(dict_b)
    i = 0
    engaged = []
    #This dictionary contains the names of the gender for which we attempt to find the optimized solution.
    times = {}
    t = 0
    position_existing = 0
    position_potential = 0
    counter = 0
    #Can have the values 'free' or 'not free'.
    a_p = {}
    while(counter < len(names1)):
        a_p.update({names1[counter]: 'free'})
        counter = counter + 1

    counter = 0
    #Can have the values 'free' or 'not free'.
    b_p = {}
    while(counter < len(names2)):
        b_p.update({names2[counter]: 'free'})
        counter = counter + 1

    counter = 0
    #Initialization of times dictionary.
    while(counter < len(names1)):
        times.update({names1[counter]: 0})
        counter = counter + 1

    #The value -1 has the meaning that when all men or women are paired, the loop stops;
    while((i != -1) and (a_p[names1[i]] == 'free') and (times[names1[i]] < len(names2))):
        #The man/woman who is next in the ranking of the proposals.
        w = a[names1[i]][times[names1[i]]]
        if(b_p[w] == 'free'):
            a_p[names1[i]] = 'not free'
            b_p[w] = 'not free'
            t = (names1[i], w)
            engaged.append(t)
            times[names1[i]] = times[names1[i]] + 1
        else:
            q = 0
            while(q < (len(engaged))):
                  if(w in engaged[q]):
                      t1 = engaged[q]
                      l = 0
                      while(l < len(names1)):
                          if(names1[i] == b[w][l]):
                              position_potential = l
                              l = len(names1)
                          l = l + 1
                      l = 0
                      while(l < len(names1)):
                          if(t1[0] == b[w][l]):
                              position_existing = l
                              l = len(names1)
                          l = l + 1
                      if(position_potential < position_existing):
                          t = (names1[i], w)
                          engaged.append(t)
                          del(engaged[q])
                          a_p[names1[i]] = 'not free'
                          a_p[t1[0]] = 'free'
                          q = len(engaged)
                  q = q + 1

            times[names1[i]] = times[names1[i]] + 1
        i = i + 1
        #If the variable i has passed from all the men/women then it starts from the beginning
        #in order to check the ones who remain single.
        if(i == len(names1)):
            i = 0
        if(a_p[names1[i]] == 'not free'):
            k = 0
            z = False
            while((k < len(names1)) and (z == False)):
                if(a_p[names1[k]] == 'free'):
                    i = k
                    z = True
                k = k + 1
            if((k == len(names1)) and (z == False)):
                i = -1
    #The list is transformed into a dictionary in order to be presented as a .JSON file.
    engaged_dict = dict(engaged)
    return engaged_dict

#The following refer to the arguments with which the program will be called from the command line.
if(sys.argv[1] == '-m'):
    matched = StableMatching(j['men_rankings'], j['women_rankings'])
elif(sys.argv[1] == '-w'):
    matched = StableMatching(j['women_rankings'], j['men_rankings'])

print(json.dumps(matched, indent=4, sort_keys=True))

if(len(sys.argv) > 3):
    if(sys.argv[3] == '-o'):
        with open(sys.argv[4], 'w') as fp:
            json.dump(matched, fp, indent=4, sort_keys=True)
