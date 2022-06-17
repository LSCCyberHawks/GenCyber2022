import zipfile
myzip = zipfile.ZipFile("test.zip")
for x in range(10000,100000):
	password = "University0" + str(x)
	try:
		myzip.extractall(pwd=bytes(password, encoding="utf-8"))
		print("FILE EXTRACTED! The password was " + password)
	except Exception as e:
		print("wrong" + password)