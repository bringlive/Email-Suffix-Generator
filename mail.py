#!/usr/bin/python3

import random
import string
import os

output = []
path = os.path.realpath(os.path.dirname(__file__))

def get_random_string(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Full Mail.com vanity domains (official list, supports + addressing)
MAIL_COM_DOMAINS = {
    "accountant.com","activist.com","adexec.com","africamail.com","airforce.net","alumnidirector.com",
    "angelic.com","aolmail.com","appraiser.net","archaeologist.com","arcticmail.com","army.com","armyspy.com",
    "artlover.com","asia.com","asianavenue.com","atheist.com","auctioneer.net","australiamail.com","backpacker.com",
    "barmail.com","bartender.net","berlin.com","bikerider.com","birdlover.com","blader.com","blowfish.com",
    "brew-master.com","brazilmail.com","brewery.com","bsdmail.com","buddhist.com","builder.com","businessman.net",
    "cabincrew.com","californiamail.com","campuscircle.net","care2.com","cash4u.com","cashflow.com","catholic.org",
    "chemist.com","cheerful.com","chef.net","christianmail.com","clerk.com","clubmember.org","collector.org",
    "columnist.com","comic.com","consultant.com","contractor.net","coolsite.net","counsellor.com","countrylover.com",
    "countrysinger.com","couple.com","cpaonline.net","craftsman.net","critic.net","crossroads.com","cryingmail.com",
    "cutey.com","cyberdude.com","cybergal.com","cyberservices.com","dallasmail.com","datajunkie.net","dayrep.com",
    "deliveryman.com","diplomats.com","discofan.com","disposable.com","doctor.com","dr.com","dublin.com",
    "earthling.net","easymail.com","ecologist.com","email.com","engineer.com","englandmail.com","europe.com",
    "execs.com","fastservice.com","financier.com","fireman.net","flashmail.com","footballer.com","footballmail.com",
    "freeaccount.com","freelance.com","freemail.com","germanymail.com","graduate.org","graphic-designer.com",
    "greenmail.net","groupmail.com","hackermail.com","hairdresser.net","handbag.com","happymail.com","hardworking.com",
    "heavymail.com","homeemail.com","homemail.com","hot-shot.com","housemail.com","humanoid.net","iamcalifornia.com",
    "iamnewyork.com","iname.com","inbox.com","innocent.com","instruction.com","insurer.com","intelligencia.com",
    "intensemail.com","internet.com","investormail.com","iname.net","iname.org","iname.email","iname.info","iname.biz",
    "inorbit.com","instructor.net","journalist.com","keromail.com","kittymail.com","lawyer.com","legislator.com",
    "letterboxes.org","linuxmail.org","lobbyist.com","lovemail.com","mac.com","madonnafan.com","mahmood.com",
    "mail.com","mail.org","mailandftp.com","mailbox.com","mailcenter.com","mailcity.com","mailforce.net","mailservice.ms",
    "manager.de","marchmail.com","marketingdude.com","me.com","metalfan.com","minister.com","musician.org",
    "myself.com","netshopping.com","neuro.com","newmail.com","nospam.com","nycmail.com","officer.com","openmailbox.org",
    "optician.com","orthodontist.net","pacific-ocean.com"
}

# GMX domains
GMX_DOMAINS = {
    "gmx.com","gmx.net","gmx.us","gmx.co.uk","gmx.at","gmx.ch","gmx.fr",
    "gmx.es","gmx.de","gmx.it","gmx.eu"
}

# Other providers supporting plus addressing
SUPPORTED_PLUS = {
    "gmail.com","protonmail.com","proton.me","tutanota.com",
    "icloud.com","me.com","mac.com","fastmail.com","zoho.com",
    "zoho.eu","yandex.com","yandex.ru","mail.ru","posteo.de",
    "mailbox.org","runbox.com","disroot.org","riseup.net","hey.com",
    "startmail.com","web.de","seznam.cz","office.com","outlook.office365.com"
}.union(MAIL_COM_DOMAINS).union(GMX_DOMAINS)

def generate_alias(base_email, count):
    domain = base_email.split("@")[-1].lower()
    local = base_email.split("@")[0]

    if domain in SUPPORTED_PLUS:
        for _ in range(count):
            rand = get_random_string(5)
            alias = f"{local}+{rand}@{domain}"
            output.append(alias)
    else:
        print(f"\033[31m⚠️ Aliases are not supported for {domain}. Skipping...\033[0m")
        output.append(base_email)  # keep the original email only

def exportprefix(exportdir):
    try:
        Directory = os.path.join(exportdir, "Output.txt")
        print("File location: " + Directory)
        with open(Directory, 'w') as fp:
            for item in output:
                fp.write("%s\n" % item)
        print('\033[32m' + "Suffixes exported successfully!" + '\033[0m')
    except Exception as e:
        print('\033[31m' + f"Export failed: {e}" + '\033[0m')

def mainmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[35m' + """  
     ___ ___   ____  ____  _           _____ __ __  _____  _____  ____  __ __
    |   |   | /    ||    || |         / ___/|  |  ||     ||     ||    ||  |  |
    |  o  | |  | | |        (   \_ |  |  ||   __||   __| |  | |  |  |
    |  \_/  ||     | |  | | |___      \__  ||  |  ||  |_  |  |_   |  | |_   _|
    |   |   ||  _  | |  | |     |     /  \ ||  :  ||   _] |   _]  |  | |     |
    |   |   ||  |  | |  | |     |     \    ||     ||  |   |  |    |  | |  |  |
    |___|___||__|__||____||_____|      \___| \__,_||__|   |__|   |____||__|__|

                        Origin by   :       IntelCoreI6
                        Updated by  :       BringLive              
                                                                                       
""" + '\033[0m')

    print('\033[35m' + """ 
    [1] Generate suffix
    [2] Close program                                                                                          
""" + '\033[0m')

    answer = input("Choose: ")
    if answer == "1":
        genAmount = int(input("How many suffixes do you want to generate? "))
        emailinput = input("Enter the email you want to use: ").strip()
        generate_alias(emailinput, genAmount)
        print(output)
        exportprefix(path)
        input("Press Enter to continue...")
    elif answer == "2":
        quit()
    else:
        print('\033[31m' + "Invalid option" + '\033[0m')

if __name__ == "__main__":
    mainmenu()

