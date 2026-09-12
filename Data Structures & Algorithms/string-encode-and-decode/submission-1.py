class Solution:

    def encode(self, strs: List[str]) -> str:
        #and join() requires strings
        if not strs:
            return ""
        size , res = [],[]
        for s in strs:
            size.append(len(s))
# putting the size of each string in the list inside the list called size
        for sz in size:
            res.append(str(sz))
            res.append(",")
        res.append("#")
        res.extend(strs)
        return ''.join(res)
# for each length of the word, first convert the int size into str because atlast we need to use join() and that shit need everything to be str
#after adding the len of each word inside the res, add a comma, it helps in decoding. and then finally after adding all word lengths, add the # to mark it as the end of it
# then, use extend()
# basically, before extend(),res looked like this res = ["5" , "," , "5" , "," ]
# and after extend(), res = ["5", "," , "5", "," , "hello", "world"]
# then use ''.join(res) to finally join everything. res = "5,5,#helloworld"
# also note that ''.join(res)  converts list into str




    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size,res,i= [], [],0
# i is the pointer to the first letter in the string
        while s[i]!='#':
            j=i
            while s[j] != ",":
                j+=1
            size.append(int(s[i:j]))
            i = j+1
        i +=1
# i is the starting pointer of each character in the string, and in this while loop we are trying to decode the length of each word, length of each word ends before # and the letters begin after #
# j helps to look for comma - which is the end pointer of each length. if length is 553, then i points to 5 and j would point to the comma after 3 in the string s, so the second while loop, gets the starting and ending of each length, and then slices those length, converts them back to integer, and puts them in the size array.
# then i is moved to the character after j, that is, i is moved to i+j, as j points to the comma, now again i points to the initial character of the length. then loop continues, giving i and j for seconf length and so on, until the first while loop condition becomes false. at the end of that loop, i will be pointing to # which is why the loop ended, so we move it to the next character, the first character of the first word. 
# now i points to the first character of the first word and size array has the sizes of all the words.
# now we use slicing to chop up the string s, from i to i+sz, essentially getting all the characters from them eg. s[0:5], s= 0,1,2,3,4 -> hellon -> remember, in slicing the ending index is not counted in the sliced part of the list. 
# then move the i pointer to the next word beginning. i =i+sz, now slice from the same format, s[i:i+sz] which is => s[5:10], s=5,6,7,8,9 -> world
# slicing word by word and appending it in the res as a list of strings. et voila! done!!!
        for sz in size:
            res.append(s[i:i+sz])
            i = i + sz
        return res
