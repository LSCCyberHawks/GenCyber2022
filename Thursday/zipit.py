import zipfile
myzip = zipfile.ZipFile("test.zip")

password = "University0" + str(7)
try:
    myzip.extractall(pwd=bytes(password, encoding="utf-8"))
    print("File extracted! The password was " + password)
except Exception as e:
    print(e)
