from ftplib import FTP

ftp = FTP('game.bradleymcgill.co.uk')
ftp.login(user='u64454791-game',passwrd='G4m3_S3v3r')

ftp.cwd('/Users/')

def grabFile():

    filename = 'Bobby.json'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()

grapFile()
