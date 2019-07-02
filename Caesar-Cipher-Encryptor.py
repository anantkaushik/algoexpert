"""
Problem Link: https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor

Given a non-empty string of lowercase letters and a non-negative integer value representing a key, 
write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, 
where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".
"""
def caesarCipherEncryptor(string, key):
    # Write your code here.
	key = key % 26
	res = []
	for c in string:
		newC = (ord(c)-ord('a')+key)
		newC = newC if newC < 26 else newC%26
		res.append(chr(newC+ord('a')))
	return "".join(res)