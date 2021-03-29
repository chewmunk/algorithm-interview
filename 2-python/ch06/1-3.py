import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱





    def is_palindrome2(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        result = s == s[::-1]
        print(result)


Solution().is_palindrome2('abb')


