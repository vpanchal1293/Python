123-456-4543
424.546.2324
677*434*4644

\d\d\d[-.]\d\d\d[-.]\d\d\d\d
\d{3}[-.]\d{3}[-.]\d{4}

800.754.5645
900.323.3433

[89]00[-.]\d\d\d[-.]\d\d\d\d

[1-7] -> range of 1 to 7
[a-z] -> a to z 
[A-Za-z] -> a to z, A to Z

[^a-z] -> everyting but not a to z

cat
bat
mat
pat

[^b]at -> bat, mat,pat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

https?://(www\.)?(\w+)(\.\w+)

Look->
Check someting is present or not, Before or after pattern
head -> +ve =, -ve !
behind -> +ve <=, -ve <!

+ve Lookhead -> (?=pattern)

p_lookhead = r'This is vipul123'
a = re.search(r'vipul(?=\d\d\d)',p_lookhead)
print(a.group())
p_lookhead = r'This is vipul'
a = re.search(r'vipul(?=\d\d\d)',p_lookhead)
print(a)

-ve Lookhead -> (?!pattern)
n_lookhead = r'This is vipul'
a = re.search(r'vipul(?!\d\d\d)',n_lookhead)
print(a.group())
n_lookhead = r'This is vipul123'
a = re.search(r'vipul(?!\d\d\d)',n_lookhead)
print(a)

+ve Lookbehind -> (?<=pattern)
p_lookbehind = r'This is 123vipul'
a = re.search(r'(?<=\d\d\d)vipul',p_lookbehind)
print(a.group())
p_lookbehind = r'This is vipul'
a = re.search(r'(?<=\d\d\d)vipul',p_lookbehind)
print(a)

-ve Lookbehind -> (?<!pattern)
n_lookbehind = r'This 123is vipul'
a = re.search(r'(?<!\d\d\d)vipul',n_lookbehind)
print(a.group())
n_lookbehind = r'This is 123vipul'
a = re.search(r'(?<!\d\d\d)vipul',n_lookbehind)
print(a)
