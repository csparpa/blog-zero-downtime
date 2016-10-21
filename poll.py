import colorama
import sys
import requests

DEFAULT_URL = 'http://localhost:8000/ping'
DEFAULT_TIMEOUT_SECS = 0.01

if __name__ == '__main__':
    url = sys.argv[1] if sys.argv[1] is not None else DEFAULT_URL
    try:
        while True:
            try:
                r = requests.get(url, timeout=DEFAULT_TIMEOUT_SECS)
                if r.status_code != requests.codes.ok:
                    raise ValueError('Server returned error '
                                     'code: {}'.format(r.status_code))
                message = 'UP: response was {}'.format(r.json())
            except requests.exceptions.Timeout:
                message = 'DOWN'
            finally:
                print(message)
    except ValueError:
        colorama.Style.RESET_ALL
        raise
    except KeyboardInterrupt:
        colorama.Style.RESET_ALL
