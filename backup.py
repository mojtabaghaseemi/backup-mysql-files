import os
import time
import ftplib
from config import *

# config
backup_location = "/backup"
backup_dirs = "/root/"
mysql_backups = True
clear_backups = True
folder_docker_compose = "/root/"
name_mysql_in_docker_compose = "mysql" # or [ mariadb or mysql-server ]

mysql_pass = "TEST"
mysql_username = "root"

hosturl = "test.example.com"
hostuser = "TEST"
hostpass = "TEST"

date_format = "%Y_%m_%d-%H_%M"
backup_name_format = "%date%-%backupName%"

os.environ['TZ'] = 'Asia/Tehran'
time.tzset()
date = time.strftime(date_format)

# func
def getFileName(name):
    fileName = backup_name_format
    fileName = fileName.replace('%date%', date)
    fileName = fileName.replace('%backupName%', name)
    return fileName

def clearBackups():
    print("INFO", "Cleaning backup dir...")
    os.system(f"rm -r {backup_location}/ && mkdir {backup_location}")
    print("Successfully deleted old backup files")

# main
def mysql_backup():
    print("Starting Backup for MySQL Database...")
    mysqlBackupFileName = getFileName('mysqlBackup') + '.sql'
    mysqlBackupFileName2 = getFileName('mysqlBackup') + '.tar.gz'
    createBackup = os.system(f"cd {folder_docker_compose} && docker-compose exec {name_mysql_in_docker_compose} mysqldump -u{mysql_username} -p'{mysql_pass}' --all-databases > {backup_location}/{mysqlBackupFileName} && cd {backup_location} && tar -cpzf {mysqlBackupFileName2} {mysqlBackupFileName}")
    print(f"{mysqlBackupFileName2} {mysqlBackupFileName}")
    os.system(f"cd {backup_location} && tar -cpzf {mysqlBackupFileName2} {mysqlBackupFileName} && rm -r {mysqlBackupFileName}")
    print("MySQL database backup successfully created.")
    time.sleep(2)
    return mysqlBackupFileName2

def backup():
    if backup_dirs == None:
        print("No directories to backup")
    else:
        if (clear_backups == True):
            clearBackups()
        counter = 0
        for dir in backup_dirs:
            backupFileName = getFileName('backup_' + str(counter + 1)) + '.tar.gz'
            counter += 1
            mysql_backup_src = ""
            if (mysql_backups == True):
                mysql_backup_src = mysql_backup()
            print("Starting backup for " + dir +"...")
            status = os.system("cd " + backup_location + " && tar -czvf " + backupFileName + " " + dir)
            print("Backup for "+dir+" successfully")
            session = ftplib.FTP(hosturl, hostuser, hostpass)
            filelist = []
            try:
                files = session.nlst("backup/file")
                for f in files:
                   if (str(f).find("/.") == -1):
                      filelist += [str(f)]
                if (len(filelist) == 2):
                   filelist.reverse()
                   session.delete(str(filelist[0]))
            except:
                pass
            file = open((backup_location) + '/' + (backupFileName), 'rb')
            session.storbinary('STOR /backup/file/' + str(backupFileName), file)
            file.close()
            if (mysql_backup_src != ""):
                try:
                    files = session.nlst("backup/sql")
                    for f in files:
                        if (str(f).find("/.") == -1):
                            filelist += [str(f)]
                    if (len(filelist) == 2):
                        filelist.reverse()
                        session.delete(str(filelist[0]))
                except:
                    pass
                file2 = open((backup_location) + '/' + str(mysql_backup_src),'rb')
                session.storbinary('STOR /backup/sql/' + str(mysql_backup_src), file2)
                file2.close()
            session.quit()
            print('Upload successfully!')
            if (clear_backups == True):
                clearBackups()

if __name__ == "__main__":
    backup()
