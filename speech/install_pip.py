import os
import sys

def install_pip():
    try:
        from urllib import request
    except ImportError:
        import urllib as request

    # Download get-pip.py
    url = 'https://bootstrap.pypa.io/get-pip.py'
    script = 'get-pip.py'
    request.urlretrieve(url, script)

    # Run get-pip.py
    os.system(f'{sys.executable} {script}')
    print('success')

if __name__ == "__main__":
    install_pip()
