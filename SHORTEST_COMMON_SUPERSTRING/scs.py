##This is the implementation for the greedy algorith used to solve the shortest
##common supersting (SCS) problem of a given set of subsequences that has been generate
##from an initial superstring.
##The algorithm must be run using the terminal without inserting any parameters and must be run on python version 2.7.
##As common problem for greedy algorithm solving SCS problem, since the sequence with
##suffix-prefix overlap is chosen randomly among some having the same score (suffix-prefix length)
##sometimes, the algorithm may not return the shortes superstring, but a variant which is longer or shorter.
##The program, by default, allows the user to insert a list of strings as input and then, it will produce the
##shortest common superstring (lines 113-118 included). Actually the user is able to generate a random sequence
##of a length that he will provide as input and from this string the program will generate substrings
##of a length that the user has to specify as input when asked. To do that, the user has just to uncomment
##the the section of the file from lines 100 to lines 108 included and comment the section at lines 113-118 included

import random    #import random to select a random sequence while evaluating their merging score

def merge(x,y,n):    #this sequence merge two sequences which have a
    output = ''        #specific suffix-prefix overlap of size n 
    if x[-n:] == y[:n]:
        output = x + y[n:]    #if overlap is found, merge them
    else:          #if no overlap is found, concatenate them
         output = x + y    #concatenated sequences
    return output

def mergingScore(suffix,prefix):  #this function finds the largest suffix-prefix overlap
    matchSP = tuple()
    score = 0
    k = -3            #minimum length for suffix to be checked 
    h = 3              #minimum length for prefix to be checked 
    while True:
        if suffix[k:] == prefix[:h]:    #once you finde the maximum suffix-prefix overlap
            score = len(prefix[:h])
            matchSP = (suffix,)+(prefix,)   #collect them and their maximum length of the overlap
            return matchSP,score
        else:
            k = k-1    #keep on checking for suffix-prefix overlaps
            h = h+1    #of length higher then n
            if h >= len(prefix):    #if two sequences do not have suffix-prefix overlap
                score = 0
                matchSP = (suffix,)+(prefix,)   #collect them with score 0
                return matchSP,score                

def overlaps(L):        #L is a list of strings which are substring coming from the superstring
    overlapScore = {}      #collect overlapping suffix-prefix sequences and their score
    i = 0
    j = 1
    while i != len(L):       #find all possible combinations of suffix-prefix overlaps
        checkSuffix = L[i]
        while j != len(L):      #among all substrings in the list L
            checkPrefix = L[j]
            checkOne = mergingScore(checkSuffix,checkPrefix)     #check seq1[suffix] and seq2[prefix]
            if checkOne[1] >= 3:
                overlapScore[checkOne[0]] = checkOne[1]
            checkSuffix,checkPrefix = checkPrefix,checkSuffix
            checkTwo = mergingScore(checkSuffix,checkPrefix)   #check seq2[suffix] and seq2[prefix]
            if checkTwo[1] >= 3:
                overlapScore[checkTwo[0]] = checkTwo[1]
            checkSuffix,checkPrefix = checkPrefix,checkSuffix  #go back to the initial sequence you were considering
            j+=1        #proceed with the next sequence
            
        i+=1     #procede untill you have not checked 
        j = i+1    #all combination of substrings of L

    return overlapScore

def greedy(L):    
    while len(L) != 1:      #proceed until you do not get a SCS
        results = overlaps(L)
        if len(results) == 0:      #when you do not have overlapping sequences, return the sequence you got
            return L[0]+L[1]   #this case depends of the sequences chosen randomly
        score = max(results.values())
        LL = []       #initialize list where you will insert sequences with maximum score
        for key in results:
            if results[key] == score:     #select maximum score
                LL += [key,]
                
        start = random.choice(LL)        #select one starting sequence randomly
        if start[0] in L and start[1] in L:    #if you find these substrings in you lisy
            check = merge(start[0],start[1],score)   #merge them
            L.remove(start[0])
            L.remove(start[1])   #delete sequences you have just merged
            L.insert(0,check)        #insert merged sequence

    return L[0]         #return shortest common superstring

def getGenome(length=15):       #generate random sequence with a default legth of 15
    genome = "".join(random.choice('AGCT') for i in range(length))
    return genome

def getSubstrings(seq,length=6):     #generate substrings from a random sequence 
    L = []                            #with size "length"
    for i in range(len(seq)-length+1):
        L.append(seq[i:i+length])
    return L

"""UNCOMMENT THIS SECTION (LINES 100-108 INCLUDED) AND COMMENT SECTION FROM LINE 113 TO LINE 118 INCLUDED
   IF YOU WANT TO GENERATE A RANDOM SEQUENCE OF A LENGTH THAT THE PROGRAM WILL ASK TO PROVIDE YOU AS AN INPUT
   AND FROM THIS FRAGMENT YOU GENERATE A SET OF SUBSTRINGS OF A LENGTH THAT THE PROGRAM
   WILL ASK YOU TO INSERT BY INPUT"""

##sequence = getGenome(int(input('insert the length of the sequence: ')))   #produce a random sequence of a given length
##stringset = getSubstrings(sequence, length = int(input('insert the length of substring:')))   #divide the strings in substrings of equal length
##print('The string generated randomly is:',sequence)
##result = greedy(stringset)
##print('The shortest common substring generated is:',result)
##if result == sequence:
##    print(True)
##else:
##    print(False)

"""COMMENT THIS SECTION (LINES 113-118 INCLUDED) AND UNCOMMENT THE SECTION FROM LINE 100 TO 108 INCLUDED
   IF YOU WANT TO GENERATE A RANDOM SEQUENCE AND A SET OF SUBSTRINGS FROM IT ALL HAVING THE SAME LENGTH"""

stringSet = input('Insert a list of strings:')
print('The input substrings to get the shortest common superstring are:')
print(stringSet)
result = greedy(stringSet)
print('The shortest common superstring obtained is:')
print(result)

