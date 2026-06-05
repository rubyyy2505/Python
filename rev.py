# to rev the string
string = "hello world"
rev = string[::-1]
print(rev)

# to rev the string w without usingout using slicing
string = "hello world"
rev = ""
for char in string:
    rev = char + rev
    print(rev)

# to rev the string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
string = "hello world"
rev = reverse_string(string)
print(rev)