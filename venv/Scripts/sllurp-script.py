#!D:\Python_projects\RFID_test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sllurp==0.5.1','console_scripts','sllurp'
__requires__ = 'sllurp==0.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sllurp==0.5.1', 'console_scripts', 'sllurp')()
    )
