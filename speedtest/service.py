import subprocess
import sys
import json
import logging

logger = logging.Logger('speedtest.service')


def network_speedtest() -> dict:
    util_path = 'D:/ookla-speedtest-1.2.0-win64/speedtest.exe' if sys.platform == 'win32' else '/usr/bin/speedtest'
    try:
        p = subprocess.run(util_path + ' -f json', shell=True, capture_output=True)
        result = p.stdout
        return json.loads(result)
    except Exception as error:
        logger.error(msg=f'{error}')


def network_speedtest_detail() -> list:
    util_path = 'D:/ookla-speedtest-1.2.0-win64/speedtest.exe' if sys.platform == 'win32' else '/usr/bin/speedtest'
    try:
        p = subprocess.run(util_path + ' -f json -p yes', shell=True, capture_output=True)
        result = p.stdout.decode('utf-8').split('\r\n')
        return result
    except Exception as error:
        logger.error(msg=f'{error}')
