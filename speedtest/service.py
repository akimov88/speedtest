import subprocess
import sys
import json


def network_speedtest() -> dict:
    if sys.platform == 'win32':
        util_path = 'D:/ookla-speedtest-1.2.0-win64/speedtest.exe'
    else:
        util_path = '/usr/bin/speedtest'
    try:
        p = subprocess.run(util_path + ' -f json', shell=True, capture_output=True)
        result = p.stdout
        return json.loads(result)
    except Exception as error:
        print(f'{error}')
