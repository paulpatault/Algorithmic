
class Solution:
    def transpose_file(self, filename):
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip().split() for x in content] 
        
        nc = []

        for j in range (len(content[0])):
            tab = []
            for i in range (len(content)):
                tab.append(content[i][j])
            nc.append(tab)
        return nc

print(Solution().transpose_file("leetcode/transpose file/file.txt"))