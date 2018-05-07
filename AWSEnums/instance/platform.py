from enum import Enum


class Platform(Enum):
    LINUX = 'Linux/UNIX'
    SUSE_LINUX = 'SUSE Linux'
    WINDOWS = 'Windows'
    WINDOWS_SQL = 'Windows with SQL Server Standard'
    UNKNOWN = 'Unknown'
