from dotenv import load_dotenv
load_dotenv()
from colorama import Fore
import dj_database_url
from colorama import init, Fore
from urllib.parse import urlparse
from pathlib import Path
import os,sys
init(autoreset=True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = os.getenv('DEBUG', 'False') == 'True'
server_stage = 'prod'

if DEBUG == False:
	server_stage = 'prod'
	print(f"{Fore.RED} {server_stage}")
else:
	server_stage= 'dev'
	print(f"{Fore.GREEN} {server_stage}")
