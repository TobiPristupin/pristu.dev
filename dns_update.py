from requests import get
import datetime
ip = get('https://api.ipify.org').text
user, password = "", ""
with open("credentials.txt") as f:
	user, password = f.readline().strip(), f.readline().strip()
req = get("https://{user}:{password}@domains.google.com/nic/update?hostname=www.pristu.dev&myip={ip}".format(user=user, password=password, ip=ip))
with open("dns_log.txt", "w") as f:
	f.write(req.text + " " + str(datetime.datetime.now()) + "\n")

