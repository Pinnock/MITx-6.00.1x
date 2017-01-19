# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:53:35 2017

@author: Rayon
"""

s = 'lvjvghwieyqypsjlnvv'
inputSize = len(s)
startIndex = 0
endIndex = 0
resultStartIndex = 0
resultEndIndex = 0

while startIndex < inputSize:
    endIndex = startIndex
    
    # check order of letters in substring starting at startIndex
    while endIndex < inputSize - 1:
        if s[endIndex] <= s[endIndex + 1]:
            endIndex += 1
            continue
        
        break
    
    # check for longest alphabetically ordered substring
    if (endIndex - startIndex)  > (resultEndIndex - resultStartIndex):
        resultStartIndex = startIndex
        resultEndIndex = endIndex
    
    # set starting index for next set of substrings to check        
    startIndex = endIndex + 1
    
print('Longest substring in alphabetical order is: ' + s[resultStartIndex:resultEndIndex+1])