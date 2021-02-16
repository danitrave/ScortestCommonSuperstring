##This is the implementation for the brute force approach used to solve the shortest
##common supersting (SCS) problem of a given set of subsequences that has been generate
##from an initial superstring.
##The algorithm must be run using the terminal and the user has not to provide any parameter.
##The program must be run on python version 2.7.
##As common problem for brute force approach algorithms, since the program performs the overlap for
##all possible combinations of substrings, it takes a lot of time to compute it.
##The program, by default, allows the user to insert a list of strings as input and then, it will produce the
##shortest common superstring (lines 96-101 included). Actually the program allows the user to generate a random sequence
##of a length that he will provide as input and from this string the program will generate substrings
##of a length that the user has to specify as input when asked. To do that, the user has just to uncomment
##the section of the file from lines 83 to lines 91 included and comment the section at lines 96-101 included

import itertools  #import itertools to build all possible combination of substrings from a string
import random  #import random to divide a string randomly

def merger(suffix,prefix):  #this function has to merge substrings having
    k = -2                     #a suffix-prefix overlap of a minimum length of l 
    h = 2
    output = ''
    while h<len(prefix):           #check if the suffix of a substring overlaps
        if suffix[k:] == prefix[:h]:                 #with a prefix of a substring   #cambia
            output = suffix + prefix[h:]         #if so, merge them
            return output
        else:              #if the suffix-prefix do not overlap, merge 
            k = k-1
            h = h+1

    if suffix[-1] == prefix[0]:
        output = suffix + prefix[1:]
        return output
    else:
        output = suffix + prefix
        return output
            
def permutations(L):   #built all possible combinations od substring
    LL = []
    global stringset
    for perm in itertools.permutations(stringset):  #use itertools to built combination of substring
        VL = []
        for x in perm:
            VL += [x,]
        LL += [VL,]       #collect combination of substrings
    return LL

def bruteforce(L):
    permu = permutations(L)    #take all possible combination of substring you got
    i = 0
    j = 1
    BFA = []
    check = len(L)             #check for considering the shortes common superstring
    scsList = ''
    for e in permu:              #select each combination of substrings, each by each
        while len(e) != 1:                 #untill you have not considered all substring
            result = merger(e[i],e[j])    #merge or concatenate them, depending on their suffix-prefix overlap
            e.remove(e[i])                #delete substrings already merged 
            e.insert(0,result)             #collect merged substrings
            e.remove(e[j])
            if len(e) < check:      #final check for the shortest common superstring
                scsList = e
                check = len(e)
            
        BFA += [e,]

    scs = ''.join(scsList)
    return scs     
        
def getGenome(length=15):       #generate random sequence with a default legth of 15
    genome = "".join(random.choice('AGCT') for i in range(length))
    return genome

def getSubstrings(seq,length=6):     #generate substrings of ny random sequences 
    L = []                            #with size "length"
    for i in range(len(seq)-length+1):
        L.append(seq[i:i+length])
    return L

"""UNCOMMENT THIS SECTION (LINES 83-91 INCLUDED) AND COMMENT THE SECTION FROM LINE 96 TO 101
   IF YOU WANT TO GENERATE A RANDOM SEQUENCE OF A LENGTH THAT THE PROGRAM WILL ASK TO PROVIDE YOU AS AN INPUT
   AND FROM THIS FRAGMENT YOU GENERATE A SET OF SUBSTRINGS OF A LENGTH THAT THE PROGRAM
   WILL ASK YOU TO INSERT BY INPUT"""             

##sequence = getGenome(int(input('insert the length of the sequence: ')))  #produce a random sequence of a given length
##stringset = getSubstrings(sequence, length = int(input('insert the length of substring:')))  #divide the strings in substrings of equal length
##print(sequence)
##result = bruteforce(stringset)
##print(result)
##if result == sequence:
##    print(True)
##else:
##    print(False)

"""COMMENT THIS SECTION (LINES 96-101 INCLUDED) AND UNCOMMENT THE SECTION FROM LINE 83 TO 91 INCLUDED
   IF YOU WANT TO GENERATE A RANDOM SEQUENCE AND A SET OF SUBSTRINGS FROM IT ALL HAVING THE SAME LENGTH"""

stringset = input('Insert a list of strings:')
print('The input substrings to get the shortest common superstring are:')
print(stringset)
result = bruteforce(stringset)
print('The shortest common superstring obtained is:')
print(result)




