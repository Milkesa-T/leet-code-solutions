class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        lowered = cleaned_text.lower()
        left=0
        right=len(lowered)-1
        while left<right:
            if lowered[left]!=lowered[right]:
                return False
            right-=1
            left+=1
        return True
