import re

#Q1
'''If zero or more characters at the beginning of string match the regular expression pattern, 
return a corresponding match object. Return None if the string does not match the pattern; 
note that this is different from a zero-length match.
'''
test_string1 = "!@#asd232"
if re.match("^(?=.*[a-zA-Z])(?=.*[0-9])", test_string1): # match signle characters between ! and ~, asii index 33-126
    print("Q1 RE matches", test_string1)
else:
    print("Q1 RE does not matches", test_string1)

#Q2
test_string2 = "abc123"
test_string_reje = "ab@12"
pattern = "^[A-Za-z0-9/]*$"
if re.match(pattern, test_string2): # match signle characters between ! and ~
    print("Q2 RE matches", test_string2)
else:
    print("Q2 RE does not matches", test_string2)
if re.match(pattern, test_string_reje): # match signle characters between ! and ~
    print("Q2 RE does not matches",test_string_reje)
else:
    print("Q2 RE does not matches", test_string_reje)  

#Q3
'''Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.
If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; 
if it is a string, any backslash escapes in it are processed.
'''
test_string3 = "abc123xyzw98"
result = re.sub("[A-Za-z]","",test_string3)
print("Q3 result is",result)
'''We can also use findall. + causes the resulting RE to match 1 or more repetitions of the preceding RE.
'''
result = re.findall("[0-9]+",test_string3)
print("Q3 result is",result)

#Q4
'''re.findall(pattern, string, flags=0)Return all non-overlapping matches of pattern in string, 
as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. 
Empty matches are included in the result.'''
test_string4 = "<TagName1/><TagName2/>A quick brown fox jumps over lazy dog<TagName3/>"
result = re.findall(r"\<(.*?)\>",test_string4)
print(result)

