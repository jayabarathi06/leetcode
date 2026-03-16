class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string=""
        length=max(indices)+1
        for i in range(length):
            string+=s[indices.index(i)]
        return string