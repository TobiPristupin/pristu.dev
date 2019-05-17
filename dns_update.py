from requests import get
import datetime
path = "/var/www/html/"
ip = get('https://api.ipify.org').text
user, password = "", ""
open(path + "dns_log.txt", "w").close() #Clear contents of log file

def request_and_log(user, password, ip, domain):
    req = get("https://{user}:{password}@domains.google.com/nic/update?hostname={domain}&myip={ip}".format(user=user, password=password, ip=ip, domain=domain))
    with open(path + "dns_log.txt", "a") as f:
        f.write(req.text + " " + str(datetime.datetime.now()) + "\n")

with open(path + "credentials.txt") as f:
    user, password = f.readline().strip().split("*")
    request_and_log(user, password, ip, "www.pristu.dev")
    user, password = f.readline().strip().split("*")
    request_and_log(user, password, ip, "pristu.dev")

