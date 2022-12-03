# ------------------ folder backup ------------------

backup_dirs = "/root/"

# ---------- folder save backup temporary ----------

backup_location = "/backup"

# --------------------- backup --------------------

mysql_backups = True
clear_backups = True

# --------------------- docker -------------------

folder_docker_compose = "/root/"
name_mysql_in_docker_compose = "mysql" # or [ mariadb or mysql-server ]

# ------------------ info mysql ------------------

mysql_pass = "TEST"
mysql_username = "root"

# ------ info (server or host) for backup --------

hosturl = "test.example.com"
hostuser = "TEST"
hostpass = "TEST"

# ------------- folder upload backup -------------

folder_upload_file_backup = "/backup/file/"
folder_upload_mysql_backup = "/backup/sql/"

# ------------- name format backup -------=------

date_format = "%Y_%m_%d-%H_%M"
backup_name_format = "%date%-%backupName%"


