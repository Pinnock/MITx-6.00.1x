# -*- coding: utf-8 -*-
s = 'nofejqtcnmakddgunpfxwwoq'
c1 = ''
c2 = ''
s2 = ''
s3 = ''
s_pos = 0
s2_pos = 0
max_s = ''
max_length = 0
is_ordered = True
for s_pos in range(len(s)):
    s2 = s[s_pos:]

    for s2_pos in range(1,len(s2)+1):
        s3 = s2[0:s2_pos]
        c2 = s3[0]
        is_ordered = True
        #print(s3)
        
        for c1 in s3:
            if c2 > c1:
                # s3 does not contain letters in alphabetical order
                is_ordered = False
                #print (s3 + ' is not ordered')
                break
            c2 = c1
        
        if is_ordered and len(s3) > max_length:
            max_s = s3
            max_length = len(s3)
            #print  (s3 + ' is ordered')
            
print('Longest substring in alphabetical order is: ' + max_s)