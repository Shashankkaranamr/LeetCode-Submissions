class Solution:
    def isPalindrome(self, s: str) -> bool:
        num_set=set(["0","1","2","3","4","5","6","7","8","9"])
        alphabet_set=set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
        front=0
        back=len(s)-1

        while front<back:
            if (s[front] in num_set or s[front].lower() in alphabet_set) and (s[back] in num_set or s[back].lower() in alphabet_set):
                if s[front].lower()!=s[back].lower():
                    return False
                else:
                    front+=1
                    back-=1
            elif (s[front] in num_set or s[front].lower() in alphabet_set) and not (s[back] in num_set or s[back].lower() in alphabet_set):
                back-=1
            elif not (s[front] in num_set or s[front].lower() in alphabet_set) and (s[back] in num_set or s[back].lower() in alphabet_set):
                front+=1
            else:
                front+=1
                back-=1
        return True

        