class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #changing the defalut value of this hashmap to list

        for eachString in strs:
            count = [0] * 26 

            for everyChar in eachString:
                # we need to map 'a' to index '0' and 'z' to index '25'
                count[ord(everyChar) - ord("a")] += 1
                # so list can't be a key
            result[tuple(count)].append(eachString) #tuple is non mutable; so can't be modifited after created
        
        return list(result.values())

        # O(m*n*26)
        # m = total number of input strings 
        # n = avg length of each string 
        # 26 = max chars lowercase ( length of the counnt array)
        # So final = O(m*n)