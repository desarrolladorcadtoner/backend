# Server/config.py
import os

DATABASE_AuroFiscal = {
    "DRIVER": "{SQL Server}",
    "SERVER": os.getenv("DB_SERVER1", "192.168.1.222\\GXSQLSTAFF"),
    "DATABASE": os.getenv("DB_DATABASE1", "AuroFiscal"),
    "UID": os.getenv("DB_USER1", "paginacad"),
    "PWD": os.getenv("DB_PASSWORD1", "cadtoner")
}

DATABASE_DistProd = {
    "DRIVER": "{SQL Server}",
    "SERVER": os.getenv("DB_SERVER2", "DIR-JRANGEL\\SERVERJR"),
    "DATABASE": os.getenv("DB_DATABASE2", "DistBD"),
    "UID": os.getenv("DB_USER2", "sa"),
    "PWD": os.getenv("DB_PASSWORD2", "Jrangel01.")
}
