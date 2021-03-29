class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return 

    def is_palindrome(self, s: str) -> bool:
        """
        팰린드롭 'aaaaa' 'aba' '12321' '11111' 등의 가운데를 기준으로 양옆을 접었을 때, 같은 값인 경우 팰린드롭이라 한다.
        """
        str_list = []
        for char in s:
            if char.isalnum():
                str_list.append(char.lower())
        
        while len(str_list) > 1:
            if str_list.pop(0) != str_list.pop():
                return print(False)
        
        return print(True)

# Solution().is_palindrome('aaaa')


def test_str():
    s = '1234567'
    for v in s:
        print(v)

test_str()