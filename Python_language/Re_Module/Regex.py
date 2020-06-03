import re

def findall_fun(pattern, txt):
    x = re.findall(pattern, txt)
    print(x)
    if (x):
        print("Yes, there is at least one match!")
    else:
        print("No match")

def split_fun(pattern, txt):
    x = re.split(pattern, txt)
    print(x)

def sub_fun(pattern, txt):
    x = re.sub(pattern, "@@@", txt)
    print(x)
    
def escape_fun(txt):
    print(re.escape("This is Awseome even 1 AM")) 
    print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))
            
msg = '''
Metacharacters
[]
A set of characters    
"[a-m]"
Find all lower case characters alphabetically between "a" and "m":
'''
print('\n'*3,msg)
txt = "The rain in Spain"
pattern = "[a-m]"
findall_fun(pattern, txt)

msg = '''
Metacharacters
.
Any character (except newline character)    
"he..o"
Search for a sequence that starts with "he",
followed by two (any) characters, and an "o":
'''
print('\n'*3,msg)

txt = "hello world"
pattern = "he..o"
findall_fun(pattern, txt)

msg = '''
Metacharacters
^
Starts with
"^hello"
Check if the string starts with 'hello':
'''
print('\n'*3,msg)

txt = "hello world"
pattern = "^hello"
findall_fun(pattern, txt)
    
msg = '''
Metacharacters
$
Ends with    
"world$"
Check if the string starts with 'world'
'''
print('\n'*3,msg)

txt = "hello world"
pattern = "world$"
findall_fun(pattern, txt)

msg = '''
Metacharacters
*
Zero or more occurrences
"aix*"
Check if the string contains "ai" 
followed by 0 or more "x" characters:
'''
print('\n'*3,msg)
txt = "The rain in Spain falls mainly in the plain!"
pattern = "aix*"
findall_fun(pattern, txt)

msg = '''
Metacharacters
+
One or more occurrences
"aix+"
Check if the string contains "ai"
followed by 1 or more "x" characters:
'''
print('\n'*3,msg)
txt = "The rain in Spain falls mainly in the ain!"
pattern = "ain+"
findall_fun(pattern, txt)

msg = '''
Metacharacters
{}
Exactly the specified number of occurrences
"al{2}"
Check if the string contains "a"
followed by exactly two "l" characters:
'''
print('\n'*3,msg)
txt = "The rain in Spain falls mainly in the plain!"
pattern = "al{2}"
findall_fun(pattern, txt)

msg = '''
Metacharacters
|
Either or
"falls|stays"
Check if the string contains either "falls" or "stays":
'''
print('\n'*3,msg)
txt = "The rain in Spain falls mainly in the plain!"
pattern = "falls|stays"
findall_fun(pattern, txt)

msg = '''
Special Sequences
Signals a special sequence (can also be used to escape special characters)
"\d"
Find all digit characters:
'''
print('\n'*3,msg)
txt = "That will be 59 dollars"
pattern = "\d"
findall_fun(pattern, txt)

msg = '''
Special Sequences
\A
Returns a match if the specified 
characters are at the beginning of the string
"\AThe"
Check if the string starts with "The":
'''
print('\n'*3,msg)
txt = "The rain in The Spain"
pattern = "\AThe"
findall_fun(pattern, txt)

msg = '''
Special Sequences
\Z
Returns a match if the specified 
characters are at the end of the string
"Spain\Z"
Check if the string starts with "The":
'''
print('\n'*3,msg)
txt = "The rain in The Spain"
pattern = "Spain\Z"
findall_fun(pattern, txt)

msg = '''
Special Sequences
Returns a match where the specified characters are 
at the beginning or at the end of a word
(the "r" in the beginning is making sure that 
the string is being treated as a "raw string")
r"\bain"
Check if "ain" is present at the beginning of a WORD:
r"ain\b"
Check if "ain" is present at the end of a WORD:
'''
print('\n'*3,msg)
txt = "Rain in Spain, Rain in Canada"
pattern = r"\bRain"
findall_fun(pattern, txt)

print('\n'*3,msg)
pattern = r"ain\b"
findall_fun(pattern, txt)

msg = '''
\B
Returns a match where the specified characters are present,
but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure
that the string is being treated as a "raw string")
r"\Bain"
Check if "ain" is present, but NOT at the beginning of a word:
r"ain\B"
Check if "ain" is present, but NOT at the end of a word:
'''
print('\n'*3,msg)
txt = "ains The rain in Spain"
pattern = r"\Bain"
findall_fun(pattern, txt)

txt = "The sainz ainr in Spain"
pattern = r"ain\B"
findall_fun(pattern, txt)

msg = '''
\d
Returns a match where the string contains digits (numbers from 0-9)
"\d"
'''
print('\n'*3,msg)
txt = "The 3 spelling is three, 4 spelling is four"
pattern = "\d"
findall_fun(pattern, txt)
    
msg = '''
\D
Returns a match where the string DOES NOT contain digits
"\D"
'''
print('\n'*3,msg)
txt = "4 spelling is four"
pattern = "\D"
findall_fun(pattern, txt)

msg = '''
\s
Returns a match where the string contains a white space character
"\s"
'''
print('\n'*3,msg)
txt = "4 spelling is four"
pattern = "\s"
findall_fun(pattern, txt)

msg = '''
\S
Returns a match where the string does not contain a white space character
"\S"
'''
print('\n'*3,msg)
txt = "4 spelling is four"
pattern = "\S"
findall_fun(pattern, txt)

msg = '''
\w
Returns a match where the string contains any word characters
(characters from a to Z, digits from 0-9, and the underscore _ character)
'''
print('\n'*3,msg)
txt = "435 is four three five m_abc"
pattern = "\w"
findall_fun(pattern, txt)

msg = '''
\W
Returns a match where the string DOES NOT contain any word characters
(characters NOT between a and Z. Like "!", "?" white-space etc.):
'''

txt = "The rain in Spain"
print('\n'*3,msg)
txt = "435 is four three five m_abc;;@#"
pattern = "\W"
findall_fun(pattern, txt)

msg = '''
Returns a match where one of the specified characters (a, r, or n) are present
[arn]
Check if the string has any a, r, or n characters:
'''
print('\n'*3,msg)
txt = "The rain in Spain"
pattern = "[arn]"
findall_fun(pattern, txt)

msg = '''
Returns a match for any lower case character, alphabetically between a and n
[a-n]
'''
print('\n'*3,msg)
txt = "The rain in Spain"
pattern = "[a-n]"
findall_fun(pattern, txt)

msg = '''
[^arn]
Returns a match for any character EXCEPT a, r, and n
'''
print('\n'*3,msg)
txt = "The rain in Spain"
pattern = "[^arn]"
findall_fun(pattern, txt)

msg = '''
[0123]
Returns a match where any of the specified digits (0, 1, 2, or 3) are present
'''
print('\n'*3,msg)
txt = "The 1 rain in 2 Spain"
pattern = "[123]"
findall_fun(pattern, txt)

msg = '''
[0-9]
Returns a match for any digit between 0 and 9
'''
print('\n'*3,msg)
txt = "The 1 rain in 2 Spain"
pattern = "[0-9]"
findall_fun(pattern, txt)

msg = '''
[0-5][0-9]
Returns a match for any two-digit numbers from 00 and 59
'''
print('\n'*3,msg)
txt = "The 1 rain in 12, 06 Spain"
pattern = "[0-5][0-9]"
findall_fun(pattern, txt)

msg = '''
[a-zA-Z]
Returns a match for any character alphabetically between a and z, lower case OR upper case
'''
print('\n'*3,msg)
txt = "The 1 rain in 12, 06 Spain"
pattern = "[a-zA-Z]"
findall_fun(pattern, txt)

msg = '''
[+]
In sets, +, *, ., |, (), $,{} has no special meaning, so [+]
means: return a match for any + character in the string    
'''
print('\n'*3,msg)
txt = "The 1 rain + in 12, 06 Spain ++"
pattern = "[+]"
findall_fun(pattern, txt)
split_fun(pattern, txt)

'''

"[a-m]"
"he..o"
"^hello"
"world$"
"aix*"
"aix+"
"al{2}"
"falls|stays"
"\d"
"\AThe"
"Spain\Z"
r"\bain"
r"ain\b"
r"\Bain"
r"ain\B"
"\D"
"\s"
"\S"
"\w"
"\W"
"[arn]"
"[a-n]"
"[^arn]"
"[0123]"
"[0-9]"
"[0-5][0-9]"
"[a-zA-Z]"
"[+]"

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match     Match a regular expression pattern to the beginning of a string.
    fullmatch Match a regular expression pattern to all of a string.
    search    Search a string for the presence of a pattern.
    sub       Substitute occurrences of a pattern found in a string.
    subn      Same as sub, but also return the number of substitutions made.
    split     Split a string by the occurrences of a pattern.
    findall   Find all occurrences of a pattern in a string.
    finditer  Return an iterator yielding a Match object for each match.
    compile   Compile a pattern into a Pattern object.
    purge     Clear the regular expression cache.
    escape    Backslash all non-alphanumerics in a string.

Some of the functions in this module takes flags as optional parameters:
    A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                   match the corresponding ASCII character categories
                   (rather than the whole Unicode categories, which is the
                   default).
                   For bytes patterns, this flag is the only available
                   behaviour and needn't be specified.
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline)
                   as well as the string.
                   "$" matches the end of lines (before a newline) as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     For compatibility only. Ignored for string patterns (it
                   is the default), and forbidden for bytes patterns.

This module also defines an exception 'error'.


'''

# Lets use a regular expression to match a date string 
# in the form of Month name followed by day number 
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24") 

if match != None: 

    # We reach here when the expression "([a-zA-Z]+) (\d+)" 
    # matches the date string. 

    # This will print [14, 21), since it matches at index 14 
    # and ends at 21. 
    print ("Match at index %s, %s" % (match.start(), match.end())) 

    # We us group() method to get all the matches and 
    # captured groups. The groups contain the matched values. 
    # In particular: 
    # match.group(0) always returns the fully matched string 
    # match.group(1) match.group(2), ... return the capture 
    # groups in order from left to right in the input string 
    # match.group() is equivalent to match.group(0) 

    # So this will print "June 24" 
    print ("Full match: %s" % (match.group(0)))

    # So this will print "June" 
    print ("Month: %s" % (match.group(1))) 

    # So this will print "24" 
    print ("Day: %s" % (match.group(2)))

else: 
    print ("The regex pattern does not match.")
    


email = "My email id is vp.panchal111@gmail.com , vp.panchal1141@gmail.com"
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", 
                           email, re.IGNORECASE))
print (new_emails) 
