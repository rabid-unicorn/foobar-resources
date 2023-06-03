'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/wishnu002/Google_Foobar_re-ID/blob/main/foobar_lvl1_reID.py"


#  Mod:
#  - replaced 'primeList.clear()' with 'primeList[:] = []'


primeList = [2,3] #set a list with the first and second prime number

def isPrime_opt(x):
    '''
    A function to check wether a number(x) is a prime number or not.
    Default return is True unless proven False.
    '''
    
    isPrime = True
    
    for i in primeList:
        if x%i == 0:
            isPrime = False
            break
        
    return isPrime

#===============================================================

def generatePrimeNumbers_opt(minStrLength):
    '''
    A function to generate concatenated string of prime numbers
    with customizable minimum string length.
    '''
    
    strPrimeGen='23'
    testNumber=3
    
    currentLen = 2
    
    while currentLen < minStrLength:
        '''
        Because the only even prime number is 2,
        only test for odd ones
        '''
        testNumber +=2
        
        '''
        Skip the test number if it's a multiplication
        of 5 (except 5 itself), since it can't be a
        prime number.
        '''
        if (testNumber > 5) & (testNumber%5 == 0):
             testNumber +=2
        
        '''
        Do the checking and concatenate the number if it's a prime
        '''
        if isPrime_opt(testNumber) == True:
            primeList.append(testNumber) #memoization
            addStr = str(testNumber)
            strPrimeGen += addStr
            currentLen += len(addStr)
    
    #memo won't be used anymore, clear to free some memory
    primeList[:] = []
            
    return strPrimeGen

#===============================================================
    
'''
Generate prime number string with minimum length of 10005 chars.
Minimum number is more than 10000 to accomodate the 10000th
minion's ID number
'''
strPrime = generatePrimeNumbers_opt(10005)

def solution(i):
    '''
    Main function by case specification.
    This function will be called and should print the
    requested 5-digit ID number of (n)th-minion.
    '''
    return strPrime[i:(i+5)]
