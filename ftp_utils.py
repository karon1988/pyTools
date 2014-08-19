import ftplib
import os
import sys

#TODO:make this code more general
def gettext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))

def getbinary(ftp, filename, outfile=None):
    # fetch a binary file
    if outfile is None:
        outfile = sys.stdout
    ftp.retrbinary("RETR " + filename, outfile.write)

ftp = ftplib.FTP("127.0.0.1")
ftp.login(user="test", passwd="test")
ftp.cwd("myfold/")
dirs = ftp.nlst()
for d in dirs:
    ftp.cwd("/myfold/"+d)
    print("cwd:"+ftp.pwd())
    files = ftp.nlst()
    print("\n".join(files))
    for f in files:
        try:
            getbinary(ftp, f, open("./data/"+d+"/"+f, "wb"))
	except IOError:
            os.system("mkdir -p ./data/"+d)
            getbinary(ftp, f, open("./data/"+d+"/"+f, "wb"))
