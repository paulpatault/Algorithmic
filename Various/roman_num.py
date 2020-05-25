class Solution:
    nums = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def romanToInt(self, num: str) -> int:
        res = 0
        lenght = len(num)
        block = False
        for i in range(lenght):
            if block:
                block = False
                continue
            if i < lenght - 1:
                n = num[i] + num[i + 1]
                if n in self.nums.keys():
                    res += self.nums[n]
                    block = True
                else:
                    res += self.nums[num[i]]
            else:
                res += self.nums[num[i]]
        return res


print(Solution().romanToInt("IX"))  # 9
print(Solution().romanToInt("VII"))  # 7
print(Solution().romanToInt("XLIV"))  # 44
print(Solution().romanToInt("MCMX"))  # 1910
print(Solution().romanToInt("MCMIV"))  # 2904
