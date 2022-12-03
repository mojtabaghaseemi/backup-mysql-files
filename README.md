# backup-mysql-files
<div align="center">Backup Mysql and Files with Docker in Python</div>


## 1. Edit File Config 
> Example:

``` python
backup_dirs = "/root/"
backup_location = "/backup"

mysql_backups = True
clear_backups = True

folder_docker_compose = "/root/Docker/"
name_mysql_in_docker_compose = "mariadb"

mysql_username = "root"
mysql_pass = "1234"

hosturl = "ftp.example.com"
hostuser = "root"
hostpass = "1234"

folder_upload_file_backup = "/backup/file/"
folder_upload_mysql_backup = "/backup/sql/"

date_format = "%Y_%m_%d-%H_%M"
backup_name_format = "%date%-%backupName%"
```

### 2. Run

``` bash
python3 backup.py
```
