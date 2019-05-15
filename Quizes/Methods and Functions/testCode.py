hyphenSeperatedString = "Bob-does-not-like-frank"
hyphenList = hyphenSeperatedString.split("-")
hyphenList.sort()
hyphenSeperatedStringAlpha = '-'.join(hyphenList)
print(hyphenSeperatedStringAlpha)