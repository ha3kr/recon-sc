#!/usr/bin/python3

import time
import json
import requests
import argparse
from termcolor import colored

logo = """
'########::'########::'######:::'#######::'##::: ##:::::::::::'######:::'######::
 ##.... ##: ##.....::'##... ##:'##.... ##: ###:: ##::::::::::'##... ##:'##... ##:
 ##:::: ##: ##::::::: ##:::..:: ##:::: ##: ####: ##:::::::::: ##:::..:: ##:::..::
 ########:: ######::: ##::::::: ##:::: ##: ## ## ##:'#######:. ######:: ##:::::::
 ##.. ##::: ##...:::: ##::::::: ##:::: ##: ##. ####:........::..... ##: ##:::::::
 ##::. ##:: ##::::::: ##::: ##: ##:::: ##: ##:. ###::::::::::'##::: ##: ##::: ##:
 ##:::. ##: ########:. ######::. #######:: ##::. ##::::::::::. ######::. ######::
..:::::..::........:::......::::.......:::..::::..::::::::::::......::::......:::
..:::::..::....Created By Sherwood Chaser......:::::::::::::::......::::......:::
..:::::..::........:::......::::.......:::..::::..::::::::::::......::::......:::

"""

pr = argparse.ArgumentParser(description="Get Subdomains Tool Using Crt.sh..")
pr.add_argument("-d", "--domain", help="Specify Domain Name.")
pr.add_argument("-s", "--silent", action="store_true", help="Silent Output.")
pr.add_argument("-o", "--output", help="Save Output Into A File.")
args = pr.parse_args()


def getSubdomain():
	list_domains = []
	url = requests.get("https://crt.sh/?q=%25.{}&output=json".format(args.domain))
	content = url.text
	json_data = json.loads(content)
	for (key,value) in enumerate(json_data):
		if value['name_value'] not in list_domains:
			list_domains.append(value['name_value'])
			print(colored(value['name_value'], "green", attrs=['bold']))
	return list_domains


def save_output(all_subs, filename):
	with open(filename, "w+") as file:
		for sub in all_subs:
			file.write(sub)



if args.domain and args.output and args.silent:
	searchResult = getSubdomain()
	save_output(searchResult, args.output)

elif args.domain and args.output:
	print(logo)
	print(colored("[+] Getting Subdomains of : ", "yellow", attrs=['bold']) + colored( args.domain + "\n", "cyan", attrs=['bold']))
	searchResult = getSubdomain()
	save_output(searchResult, args.output)
	print("\n" + colored("[+] Discovered ", "grey", attrs=['bold']) + colored(str(len(searchResult)) + " Subdomains.", "magenta"))

elif args.domain and args.silent:
	searchResult = getSubdomain()

elif args.domain:
	print(logo)
	print(colored("[+] Getting Subdomains of : ", "yellow", attrs=['bold']) + colored( args.domain + "\n", "cyan", attrs=['bold']))
	searchResult = getSubdomain()
	print("\n" + colored("[+] Discovered ", "grey", attrs=['bold']) + colored(str(len(searchResult)) + " Subdomains.", "magenta"))
