def isPalindrome(string):
    # Write your code here.
	if len(string) == 1:
		return True
	l = 0
	r = len(string) - 1
	maxiteration = (len(string) // 2) + 1
	ctr = 0
	for i in range(maxiteration):
		if string[l] == string[r]:
			ctr += 1
			l += 1
			r -= 1
		else:
			return False
	if ctr == maxiteration:
		return True
	return False