import os
import hashlib
 
def filecount():
    filecount = int(os.popen('dir /B |find /V /C ""').read())
    return (filecount)
 
 
def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())
 
 
def delfile():
    all_md5 = {}
    filedir = os.walk(os.getcwd())
    for i in filedir:
        for tlie in i[2]:
            if md5sum(tlie) in all_md5.values():
                os.remove(tlie)
            else:
                all_md5[tlie] = md5sum(tlie)
 
 
if __name__ == '__main__':
    oldf = filecount()
    print('BEFOUR', oldf, 'files \n\n\n Just you see...')
    delfile()
    print('\n\nAFTER', filecount(), 'files')
    print('\n\nDELETE', oldf - filecount(), 'files\n\n')
