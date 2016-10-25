import datetime
import colorama
import sys
import requests
from hot_code_reload import constants

DEFAULT_URL = 'http://localhost:1234/ping'
DEFAULT_TIMEOUT_SECS = 0.1

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    try:
        message_value = constants.EXPECTED_MESSAGE_VALUE
        while True:
            message = ''
            try:
                timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                r = requests.get(url, timeout=DEFAULT_TIMEOUT_SECS)
                if r.status_code != requests.codes.ok:
                    raise ValueError('Server returned error '
                                     'code: {}'.format(r.status_code))
                data = r.json()
                msg = data.get('message', '')
                if msg == message_value:
                    message = colorama.Fore.GREEN + 'UP: response was {}'.format(data)
                else:
                    message_value = msg
                    message = colorama.Fore.YELLOW + 'UP AND CHANGED: response was {}'.format(data)
            except requests.exceptions.Timeout:
                message = colorama.Fore.RED + 'DOWN'
            finally:
                message += ' [{}]'.format(timestamp)
                print(message)
    except ValueError:
        colorama.Style.RESET_ALL
        raise
    except KeyboardInterrupt:
        colorama.Style.RESET_ALL
