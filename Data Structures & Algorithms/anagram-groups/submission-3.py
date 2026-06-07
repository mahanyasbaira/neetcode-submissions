from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           groups = defaultdict(list)

           for word in strs:
                count = {}

                for ch in word:
                    count[ch] = count.get(ch, 0) + 1
                
                key = tuple(sorted(count.items()))
                groups[key].append(word)

                return list(groups.values())

            
            #hashMapA, hashMapB = {}, {}
            #for word in range(len(strs)):
             #   hashMapA[self.word] = 1 + hashMapA.get([self.word], 0)
              #  hashMapB[[self.word]] = 1 + hashMapB.get([self.word], 0)

                #for count in hashMapA:
                #    if hashMapA[count] != hashMapB[count]:
                 #       return hashMapA

                #return hashMapB

