#رمز نگاری کردن متن
def encrypt(string_):
    new_string = ""
    for i in string_:
        x = ord(i) * 2
        new_string += chr(x)
    return new_string 
# رمز گشایی 
def decrypt(string_):
    new_string = ""
    for i in string_:
        x = ord(i) // 2
        new_string += chr(x)
    return new_string 


print(encrypt("mahdiar barzegar"))
print(decrypt("ÚÂÐÈÒÂä@ÄÂäôÊÎÂä"))