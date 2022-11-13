### TODO ###
# Add PAndas and opt. loading dictionaries to memory
### END TODO ###


### IMPORT MODULES ###
from bruteforce import brute_force
import argparse
### END MODULES ###



# ================================= MAIN FUNCTION =========================== #
def main(args):
	# get args' values #
	logins, passwords = [], []
	login = args['l']
	login_dict_path = args['L']
	password = args['p']
	password_dict_path = args['P']
	num_threads = args['t']
	host = args['host']
	port = args['port']
	reverse = args['reverse']
	delay = args['delay']


	# Set brute force login(s)
	if login_dict_path:
		login_dict = open(login_dict_path, 'r')
		logins = [login.replace('\n', '') for login in login_dict]
	elif login:
		logins.append(login)

	# Set brute force password(s)
	if password_dict_path:
		password_dict = open(password_dict_path, 'r')
		passwords = [passwd.replace('\n', '') for passwd in password_dict]
	elif password:
		passwords.append(password)

	# Start brute force attack
	brute_force(host, port, logins, passwords, num_threads, delay, reverse)



# ================================ DEFINE ARGS =============================== #
def define_args():
	parser = argparse.ArgumentParser(prog = 'cracker')

	login_group = parser.add_mutually_exclusive_group(required = True)
	define_login_group(login_group)
	password_group = parser.add_mutually_exclusive_group(required = True)
	define_password_group(password_group)

	parser.add_argument('-t'
                        , metavar = 'THREADS'
                        , type = int
                        , default = 1
                        , help = 'Set number of threads (default: 1)')

	parser.add_argument('host'
                        , help = 'Set target host')

	parser.add_argument('--port'
			, metavar = 'PORT'
				, type = int
				, default = 21
                        , help = 'Set ftp port, default is 21')
	parser.add_argument('--delay'
			, '-d'
			, metavar = 'DELAY'
			, type = float
			, default = 0.5
                        , help = 'Delay between attempts in seconds')

	parser.add_argument('--reverse'
                        , '-r'
                        , action = 'store_true'
                        , help = 'Set brute force attack type. Default' \
				 'attack type is login:password[i],' \
				 'reverse is login[i]:password')
	return parser


def define_login_group(login_group):
		login_group.add_argument('-l'
					, metavar = 'LOGIN'
					, help = 'Set login')

		login_group.add_argument('-L'
					, metavar = 'dict.txt'
					, help = 'Set login wordlist')


def define_password_group(password_group):
		password_group.add_argument('-p'
					, metavar = 'PASSWORD'
					, help = 'Set password')

		password_group.add_argument('-P'
					, metavar = 'dict.txt'
					, help = 'Set password wordlist')




### START PROGRAM ###
if __name__ == "__main__":
	parser = define_args()
	args = vars(parser.parse_args())
	main(args)
### PROGRAM FINISHED ###
