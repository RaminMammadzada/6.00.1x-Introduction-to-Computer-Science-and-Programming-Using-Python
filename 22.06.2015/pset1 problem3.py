s=str(raw_input(''))
longest = ''
for i in xrange(len(s)):
     for j in xrange(i+1, len(s)):
         ss = s[i:j+1]
         if ''.join(sorted(ss)) == ss:
             longest = max(longest, ss, key=len)
         else:
             break
if len(longest)<2:
    longest='z'
print('Longest substring in alphabetical order is:')
print(longest)
