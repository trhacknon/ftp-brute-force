from colorama import Fore

### APP HEADERS ###
__author__ = "trhacknon"
__license__ = "GNU GPLv3"
__email__ = "trhacknon@gmail.com"
__status__ = "Development"
### END HEADERS ###


### APP CONSTANTS ###
LOGIN_ATTEMPT = '{} ' + Fore.CYAN + 'Tried ' + Fore.WHITE + '{}:{}'
CONNECTION_ERROR = Fore.RED + 'Error: ' + Fore.WHITE + 'bad response code.'
SUCCESS = Fore.GREEN + '[+]'
FAILURE = Fore.RED + '[-]'
CRLF = '\r\n'
CHUNK_SIZE = 1024
ATTEMPTS_LIMIT = 3
### END CONSTANTS ###


### FTP CONSTANTS ###
FTP_LOGIN_SUCCESS = '230'
FTP_CONNECTION_SUCCESS = '220'
FTP_USERNAME_CMD = 'USER {}' + CRLF
FTP_PASSWORD_CMD = 'PASS {}' + CRLF
### END CONSTANTS ###
