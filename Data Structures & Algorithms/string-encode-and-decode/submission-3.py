class Solution:

    def encode(self, strs: List[str]) -> str:
        #and join() requires strings
        
# putting the size of each string in the list inside the list called size
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return ''.join(res)
# for each length of the word, first convert the int size into str because atlast we need to use join() and that shit need everything to be str
# here we just use the format res = "5#hello5#world"
# to create that, first we run a for loop for every string inside strs, then we get the length of each word and convert it into string and add it to the res. then we add the # in between, and finally the word. hence => res = ["5","#","hello"]
# this continues until all the words are attached, then finally using join to convert the list of strings into 1 big ass string res = "5#hello"
# then use ''.join(res) to finally join everything. res =  "5#hello5#world"
# also note that ''.join(res)  converts list into str




    def decode(self, s: str) -> List[str]:
        i, res = 0,[]
        while i < len(s):
            j = i
            while s[j]!="#":
                j +=1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res

# decoding is simple af, initially i points to the first character of the string which is the first character of the length of the first word, the while loop runs till the end of all the characters in the encode string s.
# creating a second pointer j and a while loop that stops when s[j] = #
# this second while loop essentially gives the pointers i and j of the length of the word. if 543#acbenjfkgn..... is the string, then i points to 5 and j points to #
# now, slice the string from s[i:j] this gives s ="543" and convert this string to integer; then move i to the first character of the word. now i points to h in hello and i+length, points to whichever character comes after the end of the word.
# using this, slice it up! eg, s = "5#hello"
#now u have, length = 5, i = 2, and i + length = 7
# then s[i:i+length] gives u "hello"
# append that to res.
# now, as i + length points to the next character after the end of the word, update i as i = i+ length, now that i is updated, the first while loop condition is checked again and the cycle repeats.
# keep going until u reach i == len(s). at this point, the condition for the first while loop becomes false and u get all the strings inside res.