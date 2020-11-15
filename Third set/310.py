def romanToInt(s):
	roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
	result = 0

	for i in range(len(s)):
		if i>0 and roman[s[i]] > roman[s[i-1]]:
			result += roman[s[i]] - 2 * roman[s[i-1]]
		else:
			result += roman[s[i]]
	return result

print(romanToInt('CXXIV'))