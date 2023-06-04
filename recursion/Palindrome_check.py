def palindrome(text):
    n = len(text)
    
    for i in range((n+1)//2):
        if text[i] == text[n-1-i]:
            return True
        
    return False

if __name__ == "__main__":

    print(palindrome("i"))