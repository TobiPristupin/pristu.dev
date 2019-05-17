from requests import get
import datetime
path = "/var/www/html/"
ip = get('https://api.ipify.org').text
user, password = "", ""
with open(path + "credentials.txt") as f:
	user, password = f.readline().strip(), f.readline().strip()
req = get("https://{user}:{password}@domains.google.com/nic/update?hostname=pristu.dev&myip={ip}".format(user=user, password=password, ip=ip))
with open(path + "dns_log.txt", "w") as f:
	f.write(req.text + " " + str(datetime.datetime.now()) + "\n")

