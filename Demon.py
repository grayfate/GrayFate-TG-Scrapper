import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
from csv import reader
from datetime import MINYEAR, datetime, timedelta
from colorama import Fore, Back, Style, init
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek, PeerUser, PeerChannel, InputPeerChannel, InputPeerUser
from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.messages import GetDialogsRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError, YouBlockedUserError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.sessions import StringSession



API_ID = 2392599
HashID = '7e14b38d250953c8c1e94fd7b2d63550'

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wi="\033[1,35m"

if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists('phone.csv'):
    open("phone.csv","w")



def login():



    banner()
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            client.disconnect()
            print()
        done = True
    print(Style.BRIGHT + Fore.RESET + 'All Number Login Done !' if done else "Error!")
    print(Style.BRIGHT + Fore.YELLOW + 'Press Enter to back')
    input()
def BanFilter():

    api_id = int(API_ID)
    api_hash = str(HashID)
    MadeByDevOp = []

    done = False
    with open('phone.csv', 'r') as f:
        str_list = [row[0] for row in csv.reader(f)]

        po = 0
        for unparsed_phone in str_list:
            po += 1

            phone = utils.parse_phone(unparsed_phone)

            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
            # client.start(phone)
            client.connect()
            if not client.is_user_authorized():
                try:
                    print('This Phone Has Been Revoked')
                    DevOp = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByDevOp.append(Nero_op)
                    continue

                except PhoneNumberBannedError:
                    print('Ban')
                    DevOp = str(po)
                    Nero_op = str(unparsed_phone)
                    MadeByDevOp.append(Nero_op)

                    continue

            # client.disconnect()
            print()
        done = True
        print('List Of Banned Numbers')
        print(*MadeByDevOp, sep='\n')
        print('Saved In BanNumers.csv')
        with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(MadeByDevOp)


    def autoremove():


        collection = []
        nc = []
        collection1 = []
        nc1 = []
        maind = []

        with open("phone.csv", "r") as infile:
            for line in infile:
                collection.append(line)

        for x in collection:
            mod_x = str(x).replace("\n", "")
            nc.append(mod_x)

        with open("BanNumbers.csv") as infile, open("outfile.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        with open("outfile.csv", "r") as outfile:
            for line1 in outfile:
                collection1.append(line1)

        for i in collection1:
            mod_i = str(i).replace("\n", "")
            nc1.append(mod_i)

        unique = set(nc)
        unique1 = set(nc1)

        itd = unique.intersection(unique1)

        for x in nc:
            if x not in itd:
                maind.append(x)

        with open('unban.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(maind)

        with open("unban.csv") as last, open("phone.csv", "w") as final:
            for line3 in last:
                mod_i = str(line3).replace("\n", "")
                final.write(mod_i)

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")
        print("Done,All Banned Number Have Been Removed")


    def dellst():
        import csv
        import os

        with open("phone.csv") as infile, open("unban.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))

        os.remove("phone.csv")
        os.rename("unban.csv", "phone.csv")

        print("complete")


    autoremove()
    dellst()

    input("Done!" if done else "Error!")
def SpamBotChecker():
    banner()
    bot = 'SpamBot'
    m = "Good news, no limits are currently applied to your account. You’re free as a bird!"
    DevOp = "bird"
    r = 0
    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            client(functions.contacts.UnblockRequest(id='@SpamBot'))
            client.send_message(bot, '/start')
            time.sleep(1)
            msg = str(client.get_messages(bot))
            if DevOp in msg:
                print(m)
                r += 1
            else:
                print('you are limited')
            client.disconnect()
            print()
            done = True
    print(f'{r} - Accounts Are Usable')
    input("Done!" if done else "Error!")
def Scraper():
    config = configparser.ConfigParser()
    config.read("config.ini")
    link1 = (config['DevOp']['FromGroup']).strip()
    links = link1.split(',')
    phone = (config['DevOp']['PhoneNumber']).strip()
    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'login Done')
            count = 1
            today = datetime.now()
            last_week = today + timedelta(days=-7)
            last_month = today + timedelta(days=-30)
            f = open("data.csv", "w", encoding='UTF-8')
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            try:
                for link in links:
                    try:
                        client(JoinChannelRequest(link))
                    except Exception as e:
                        pass
                    print(Style.BRIGHT + Fore.YELLOW + f'Scrabing Members from {link} group.....')
                    all_participants = []
                    try:
                        all_participants = client.get_participants(link, aggressive=True)
                    except Exception as e:
                        # print(e)
                        pass
                    for user in all_participants:
                        if user.username:
                            username = user.username
                        else:
                            username = ""
                        if user.first_name:
                            name = user.first_name
                        else:
                            name = "DevOp"
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        writer.writerow([count, username, user.id, name, link, date_online_str])
                        count = count + 1
            except Exception as e:
                # print(1,e)
                pass
            f.close()
            print('Count : ', count)
        else:
            print(Style.BRIGHT + Fore.RED + f'login fail {phone}')
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f'login fail')

    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Task completed")
    print(Style.BRIGHT + Fore.RESET + "Enter any key to exit")
    input()
def DailyFilter():

    colorama.init(autoreset=True)
    print(Style.BRIGHT + Fore.RESET + 'Welcome To DevOp Program\n')

    def nfilter(client, link, last_day):
        today = datetime.now()
        last_week = today + timedelta(days=-7)
        last_month = today + timedelta(days=-30)
        today = today.strftime("%Y%m%d")
        a = [['sr. no.', 'username', 'user id', 'name', 'group', 'Status']]
        count = 1
        dialogs = client.get_dialogs()
        for i in link:
            print(Style.BRIGHT + Fore.RESET + f'Filter Members from {i} group.....')
            group = client.get_entity(i)
            try:
                all_participants = client.get_participants(group.id, aggressive=True)
            except Exception as e:
                continue
            for user in all_participants:
                if user.username != None:
                    try:
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        if (str(date_online_str) >= str(last_day)):
                            b = [count, str(user.username), str(user.id), str(user.first_name + ' ' + user.last_name),
                                 str(group.title), str(date_online_str)]
                            a.append(b)
                            count += 1
                    except:
                        pass
        if a:
            with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                write = csv.writer(f)
                write.writerows(a)
        print('Members : ', count)
        client.disconnect()
        print()


    print(Style.BRIGHT + Fore.YELLOW + "\nEnter the day for filter :")
    n = int(input())
    n = n
    last_day = (datetime.now() + timedelta(days=-n)).strftime("%Y%m%d")
    dele = []

    config = configparser.ConfigParser()
    config.read("config.ini")
    links = (config['DevOp']['FromGroup']).strip()
    link = links.split(',')
    phone = (config['DevOp']['PhoneNumber']).strip()

    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'login Done')
            a = nfilter(client, link, last_day)

        else:
            print(Style.BRIGHT + Fore.RED + f'{phone} login fail')
    except Exception as e:
        print(e)
        print(Style.BRIGHT + Fore.YELLOW + f'Please Enter Vailed Group')
    # username filter start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Filter completed")
    print(Style.BRIGHT + Fore.YELLOW + "Enter any key to exit")
    input()
def WeeklyFilter():
    def nfilter(client, link, last_day):
        today = datetime.now()
        last_week = today + timedelta(days=-7)
        last_month = today + timedelta(days=-30)
        today = today.strftime("%Y%m%d")
        a = [['sr. no.', 'username', 'user id', 'name', 'group', 'Status']]
        count = 1
        dialogs = client.get_dialogs()
        for i in link:
            print(Style.BRIGHT + Fore.RESET + f'Filter Members from {i} group.....')
            group = client.get_entity(i)
            try:
                all_participants = client.get_participants(group.id, aggressive=True)
            except Exception as e:
                continue
            for user in all_participants:
                if user.username != None:
                    try:
                        if isinstance(user.status, UserStatusRecently):
                            date_online = today
                        else:
                            if isinstance(user.status, UserStatusLastMonth):
                                date_online = last_month
                            if isinstance(user.status, UserStatusLastWeek):
                                date_online = last_week
                            if isinstance(user.status, UserStatusOffline):
                                date_online = user.status.was_online
                        date_online_str = date_online.strftime("%Y%m%d")
                        if (str(date_online_str) >= str(last_day)):
                            b = [count, str(user.username), str(user.id), str(user.first_name + ' ' + user.last_name),
                                 str(group.title), str(date_online_str)]
                            a.append(b)
                            count += 1
                    except:
                        pass
        if a:
            with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                write = csv.writer(f)
                write.writerows(a)
        print('counting : ', count)
        client.disconnect()
        print()


    print(Style.BRIGHT + Fore.YELLOW + "\nEnter the week for filter :")
    n = int(input())
    n = n * 7
    last_day = (datetime.now() + timedelta(days=-n)).strftime("%Y%m%d")
    dele = []

    config = configparser.ConfigParser()
    config.read("config.ini")
    links = (config['DevOp']['FromGroup']).strip()
    link = links.split(',')
    phone = (config['DevOp']['PhoneNumber']).strip()

    logging.basicConfig(level=logging.WARNING)

    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')
    try:
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.connect()
        if client.is_user_authorized():
            print(Style.BRIGHT + Fore.GREEN + f'Login Done')
            a = nfilter(client, link, last_day)

        else:
            print(Style.BRIGHT + Fore.RED + f'login fail {phone}')
    except Exception as e:
        print(e)
        print(Style.BRIGHT + Fore.YELLOW + f'Please Enter A Vailed Group')
    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")
    print(Style.BRIGHT + Fore.GREEN + "Filter completed")
    print(Style.BRIGHT + Fore.YELLOW + "Enter any key to exit")
    input()
def DeleteALreadyMembers():

    logging.basicConfig(level=logging.WARNING)

    config = configparser.ConfigParser()
    config.read("config.ini")
    link = (config['DevOp']['ToGroup']).strip()
    phone = (config['DevOp']['PhoneNumber']).strip()

    #with open('data.csv', 'r' , encoding='utf-8') as f:
    #     existing_numbers = f.read().split('\n')
    #     print(type(existing_numbers))
    #     exit()

    with open('data.csv', 'r', encoding='utf-8') as f:
        users1 = csv.reader(f)
        users = [i for i in users1]

    with open('data.csv', 'r', encoding='utf-8') as f:
        users1 = csv.reader(f)
        userlist = [str(i[2]) for i in users1]

    client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
    client.connect()
    if not client.is_user_authorized():
        print(f'\nLogin fail, for number {phone} need Login first\n')
    else:
        chats = []
        last_date = None
        chunk_size = 200
        groups = []
        n = 0
        while n != -1:
            try:
                group = client.get_entity(link)
                if group.megagroup == True:
                    group_id = str(group.id)
                    all_participants = client.get_participants(group, aggressive=True)
                    results = []
                    results1 = []
                    count = 0
                    index1 = []
                    for user in all_participants:
                        try:
                            if str(user.id) in userlist:
                                index1.append(userlist.index(str(user.id)))
                        except:
                            print("Error get user")
                    f.close()
                    client.disconnect()
                    index1.sort(reverse=True)
                    for i in index1:
                        del users[i]
                    with open('data.csv', 'w', encoding="utf-8", newline='') as f:
                        write = csv.writer(f)
                        write.writerows(users)
                    n = -1
                else:
                    print(Style.BRIGHT + Fore.RED + "\nInvalid Group..\n")
                n = -1
            except telethon.errors.rpcerrorlist.ChatWriteForbiddenError:
                client(JoinChannelRequest(link))
            except ValueError:
                print(Style.BRIGHT + Fore.GREEN + "\nOnly Public Group Allowed..\n")
                n = -1
            except:
                print(Style.BRIGHT + Fore.RED + "\nInvalid Group....\n")
                n = -1
    # Filter by usname start from here
    lines = list()


    def main():
        lines = list()
        with open('data.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == '':
                        lines.remove(row)
        with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    def main1():
        lines = list()
        with open('1.csv', 'r', encoding='UTF-8') as readFile:

            reader = csv.reader(readFile)

            for row in reader:

                lines.append(row)

                for field in row:

                    if field == 'username':
                        lines.remove(row)

        with open('2.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

            writer.writerows(lines)


    main()
    main1()

    with open("2.csv", "r", encoding='UTF-8') as source:
        rdr = csv.reader(source)

        with open("data.csv", "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
            i = 0
            for row in rdr:
                i += 1
                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))

    os.remove("1.csv")
    os.remove("2.csv")
    # os.remove("data.csv")

    print(Style.BRIGHT + Fore.RESET + "Already Member Deleted Done !")
    print(Style.BRIGHT + Fore.GREEN + 'Task Completed')
    print(Style.BRIGHT + Fore.YELLOW + "Press Enter to exit")
    input()
def SetProfile():

    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1

            print(Style.BRIGHT + Fore.GREEN + f"Changing in {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            result = client(functions.photos.UploadProfilePhotoRequest(
                file=client.upload_file('set.jpg'),
            ))
            print('done! profile pic has been changed')
            done = True
    input("Done!" if done else "Error!")
def DeleteProfile():


    done = False
    with open('phone.csv', 'r')as f:
        str_list = [row[0] for row in csv.reader(f)]
        po = 0
        for pphone in str_list:
            phone = utils.parse_phone(pphone)
            po += 1
            print(Style.BRIGHT + Fore.RED + f"Deleting in {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.start(phone)
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            print(Style.BRIGHT + Fore.GREEN + 'Profile Pic Deleted')
            done = True
    input("Done!" if done else "Error!")
def banner():
    os.system('clear')
    print(f"""



██████╗░███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗██╔════╝████╗░████║██╔══██╗████╗░██║
██║░░██║█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██║░░██║██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
██████╔╝███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝

░█████╗░██████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████║██║░░██║██║░░██║█████╗░░██████╔╝
██╔══██║██║░░██║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██████╔╝██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
{cy}          Version : 2.0                
{cy}              MADE BY @SMITMOREXD
                  @THE_DEMON_NETWORK 
{cy}                    
   {gr}FUCK ALL OTHER NETWORKS DEMON IS THE BEST!
DEV - @smitmorexd
        """)
def AutoaddContactPhone():

    init()
    r = Fore.LIGHTRED_EX
    gr = Fore.GREEN
    n = Fore.RESET
    bl = Fore.BLUE
    ye = Fore.YELLOW

    banner()

    api_id = []
    api_hash = []
    phone = []

    with open('phone.csv', 'r') as delta_obj:
        csv_reader = reader(delta_obj)
        list_of_phone = tuple(csv_reader)
        for phone_ in list_of_phone:
            phone.append(int(phone_[0]))


    pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')


    def autos():
        From = int(input(f'{bl}From Account No : {n}')) - 1
        Upto = int(input(f'{bl}Upto Account No : {n}'))
        rex = int(input(f'{bl}From where you want to start : {n}'))
        hacks = int(input(f'{bl}How many contacts you want to add in one Account : {n}'))

        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(Style.BRIGHT + Fore.GREEN + f"Login {Style.RESET_ALL} {Style.BRIGHT + Fore.RESET} {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = 'data.csv'
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.contacts.AddContactRequest(
                            id=user['username'],
                            first_name=user['name'],
                            last_name=str('DevOp'),
                            phone='gdf',
                            add_phone_privacy_exception=True))
                        status = f'{it} - done'





                    except errors.RPCError as e:
                        status = e.__class__.__name__





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

                    print(status)

            a += 1
        os.remove("memory.csv")
        again()


    def again():
        stat = input(f'{r}Done!\nChoose From Below:\n\n1 - Repeat The Script\nOR Just Hit Enter To Quit\n\nEnter: {n}')
        if stat == '1':
            autos()
        else:
            quit()


    autos()
def DeleteContact():


    colorama.init(autoreset=True)


    print(Style.BRIGHT + Fore.GREEN + 'Enter Accounts List : ')
    phonecsv = input()

    with open(f'{phonecsv}.csv', 'r') as f:
        global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))

    DevOp_ne_script_banaya_hai = int(input('From Account No : ')) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(input('Upto Account No : '))
    indexx = 0
    global DevOppro
    DevOppro = 0
    for DevOponyt in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(DevOponyt)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)

        contacts = client(GetContactsRequest(hash=0))

        rexadd = 0
        for rexop in contacts.users:
            rexadd += 1

            try:
                client(DeleteContactsRequest(id=[rexop]))
                print(Style.BRIGHT + Fore.GREEN + f"{rexadd} - {rexop.id} - DELETE")
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(f'{rexadd} - {rexop.id} - {erro}')
                continue
def BulkAdder():

    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['DevOp']['ToGroup']
    groupid = config['DevOp']['GroupID']
    stopnum = config['DevOp']['EnterStop']
    stacno = config['DevOp']['StartingAccount']
    endacno = config['DevOp']['EndAccount']


    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))
    print(Style.BRIGHT + Fore.GREEN + 'Enter Y if group has private link else N (Y/N) : ')
    prchk = input()
    print(Style.BRIGHT + Fore.GREEN + 'In A Batch How many Members You Want To Add : ')
    Legenddevismain = int(input())
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    Legend_dev =int(input())
    if prchk == 'Y':
        id = int(groupid)
        prlink = grouplink
    elif prchk == 'N':
        id = int(groupid)
        prlink = grouplink
    stop = int(stopnum)
    start_from = int(stacno) - 1
    upto = int(endacno)
    indexx = 0
    global Legenddev_is_main_developer
    Legenddev_is_main_developer = 0
    for pythondeveloper in phlist[start_from:upto]:
        indexx += 1

        phone = utils.parse_phone(pythondeveloper)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        print(f'Index : {indexx}')
        try:
            channel = client.get_entity(PeerChannel(id))
        except ValueError:
            if prchk == 'Y':
                client(ImportChatInviteRequest(prlink))
                channel = client.get_input_entity(PeerChannel(id))
            # This Script Is Made My T.Me/DevOp.
            elif prchk == 'N':
                client(JoinChannelRequest(prlink))
                time.sleep(5)
                channel = client.get_input_entity(PeerChannel(id))
        channelinfo = client(GetFullChannelRequest(channel=channel))
        Legenddev_is_main_developer = int(channelinfo.full_chat.participants_count)
        print(f'Members: {Legenddev_is_main_developer}')
        if Legenddev_is_main_developer >= stop:
            print(f'The Goal Of {stop} Has Been Completed')
            input()
            quit()

        members = client(GetContactsRequest(hash=0))
        user_to_add = members.users
        countcon = len(user_to_add)
        print(f'Total : {countcon}')

        batchcount = 0
        lol = 0
        while batchcount < countcon:
            semen = [delta for delta in user_to_add[:Legenddevismain]]
            # print(f'Left {len(lit)}')
            try:
                time.sleep(Legend_dev)
                client(functions.channels.InviteToChannelRequest(
                    channel=id,
                    users=semen
                ))
                # print(f'Added : {added}')
                batchcount += Legenddevismain
                for i in range(0, 10):
                    try:
                        del user_to_add[i]
                    except Exception as D:
                        continue
                print(Style.BRIGHT + Fore.GREEN + f'BATCH: {batchcount}')
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(str(erro))
                break
                # continue
def SingleAdder():

    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['DevOp']['ToGroup']
    groupid = config['DevOp']['GroupID']
    stopnum = config['DevOp']['EnterStop']
    stacno = config['DevOp']['StartingAccount']
    endacno = config['DevOp']['EndAccount']

    with open('phone.csv', 'r') as f:
        #global phlist
        phlist = [row[0] for row in csv.reader(f)]
    print('Total account: ' + str(len(phlist)))

    print(Style.BRIGHT + Fore.GREEN + 'Enter Y if group has private link else N (Y/N) : ')
    prchk = input()
    print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
    Legend_dev =int(input())
    if prchk == 'Y':
        id = int(groupid)
        prlink = grouplink
    elif prchk == 'N':
        id = int(groupid)
        prlink = grouplink
    stop = int(stopnum)
    DevOp_ne_script_banaya_hai = int(stacno) - 1
    telegram_script_banyane_ke_liye_DevOp_ko_dm_kro = int(endacno)
    indexx = 0
    global DevOppro
    DevOppro = 0
    for deltaxd in phlist[DevOp_ne_script_banaya_hai:telegram_script_banyane_ke_liye_DevOp_ko_dm_kro]:
        indexx += 1
        print(f'Index : {indexx}')
        phone = utils.parse_phone(deltaxd)
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
        client.start(phone)
        try:
            channel = client.get_entity(PeerChannel(id))
        except ValueError:
            if prchk == 'Y':
                client(ImportChatInviteRequest(prlink))
                channel = client.get_input_entity(PeerChannel(id))

            elif prchk == 'N':
                client(JoinChannelRequest(prlink))
                time.sleep(5)
                channel = client.get_input_entity(PeerChannel(id))
        channelinfo = client(GetFullChannelRequest(channel=channel))
        DevOppro = int(channelinfo.full_chat.participants_count)
        print(f'Members: {DevOppro}')
        if DevOppro >= stop:
            print(f'The Goal Of {stop} Has Been Completed')
            input()
            quit()
        contacts = client(GetContactsRequest(hash=0))

        deltaadd = 0
        for deltaop in contacts.users:
            deltaadd += 1

            try:
                client(InviteToChannelRequest(channel=id, users=[deltaop]))
                print(Style.BRIGHT + Fore.GREEN + f'{deltaadd} - {deltaop.id} - DONE')
                time.sleep(Legend_dev)
            except errors.RPCError as e:
                erro = e.__class__.__name__
                print(Style.BRIGHT + Fore.RED + f'{deltaadd} - {deltaop.id} - {erro}')
                continue
def Adder():
    print(Style.BRIGHT + Fore.YELLOW + 'Which Account You Want To Use?\n\nEnter: ')
    Legend_devinput = int(input())


    with open('phone.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        row_number = Legend_devinput
        col_number = 1
        value = list_of_rows[row_number - 1][col_number - 1]

    api_id = API_ID
    api_hash = HashID
    pphone = value

    config = configparser.ConfigParser()
    config.read("config.ini")
    to_group = config['DevOp']['ToGroup']


    def autos():

        channel_username = to_group
        phone = utils.parse_phone(pphone)

        client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter code: '))
                print('')
                client.sign_in(phone)
            except SessionPasswordNeededError:
                password = input('Enter password: ')
                print('')
                client.sign_in(password=password)

        input_file = 'data.csv'
        users = []
        with open(input_file, encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=",", lineterminator="\n")
            next(rows, None)
            for row in rows:
                user = {}
                user['srno'] = row[0]
                user['username'] = row[1]
                user['id'] = int(row[2])
                # user['access_hash'] = int(row[2])
                user['name'] = row[3]
                users.append(user)

        startfrom = int(input("Start From = "))
        endto = int(input("End To = "))

        for user in users:
            if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                try:
                    status = 'Legend_dev'
                    if user['username'] == "":
                        print("no username, moving to next")
                        continue

                    client(InviteToChannelRequest(channel_username, [user['username']]))
                    status = Style.BRIGHT + Fore.GREEN + 'DONE'

                    print(Style.BRIGHT + Fore.YELLOW + "Moving To Next")
                    time.sleep(1)

                except UserPrivacyRestrictedError:
                    status = Style.BRIGHT + Fore.RED + 'PrivacyRestrictedError'
                    time.sleep(2)

                except UserAlreadyParticipantError:
                    status = 'ALREADY'

                except PeerFloodError as g:
                    status = 'PeerFloodError'
                    print(Style.BRIGHT + Fore.YELLOW + 'Script Are In Progress So Please Wait...')
                    time.sleep(5)

                except ChatWriteForbiddenError as cwfe:
                    client(JoinChannelRequest(channel_username))
                    time.sleep(5)
                    continue

                except errors.RPCError as e:
                    status = e.__class__.__name__

                except Exception as d:
                    status = d

                except:
                    traceback.print_exc()
                    print("Unexpected Error")
                    continue
                channel_connect = client.get_entity(channel_username)
                channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
                countt = int(channel_full_info.full_chat.participants_count)

                print(Style.BRIGHT + Fore.RESET + f"Group Members {(countt)}{Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status}")
            elif int(user['srno']) > int(endto):
                print("Members Added Successfully!")
                input()
                exit()



    autos()
def AdderForPhone():

    init()
    r = Fore.LIGHTRED_EX
    gr = Fore.GREEN
    n = Fore.RESET
    bl = Fore.BLUE
    ye = Fore.YELLOW


    config = configparser.ConfigParser()
    config.read("config.ini")
    grouplink = config['DevOp']['ToGroup']
    groupid = config['DevOp']['GroupID']
    stopnum = config['DevOp']['EnterStop']
    stacno = config['DevOp']['StartingAccount']
    endacno = config['DevOp']['EndAccount']

    phone = []

    with open('phone.csv', 'r') as delta_obj:
        csv_reader = reader(delta_obj)
        list_of_phone = tuple(csv_reader)
        for phone_ in list_of_phone:
            phone.append(int(phone_[0]))
    pphone = phone

    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')



    def autos():
        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
        Legend_dev = int(input())
        DevOp = 'data.csv'
        rexlink = str(grouplink)
        id = int(groupid)
        From = int(stacno) - 1
        Upto = int(endacno)
        rex = int(1)
        hacks = int(50) - 1
        stop = int(stopnum)

        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = DevOp
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            client(JoinChannelRequest(rexlink))
            time.sleep(5)
            channel = client.get_input_entity(PeerChannel(id))
            channelinfo = client(GetFullChannelRequest(channel=channel))

            rexprodeltanoob = int(channelinfo.full_chat.participants_count)
            print(f'Members: {rexprodeltanoob}')
            if rexprodeltanoob >= stop:
                print(f'The Goal Of {stop} Has Been Completed')
                input()
                quit()

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))
                        print(f'{it} - done')
                        time.sleep(Legend_dev)


                    except ChatWriteForbiddenError as cwfe:
                        client(JoinChannelRequest(rexlink))
                        time.sleep(5)
                        continue



                    except errors.RPCError as e:
                        status = e.__class__.__name__
                        print(f'{it} - {status}')





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

            a += 1
        os.remove("memory.csv")


    def private():
        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')
        Legend_dev = int(input())
        DevOp = 'data.csv'
        rexlink = str(grouplink)
        id = int(groupid)
        From = int(stacno) - 1
        Upto = int(endacno)
        rex = int(1)
        hacks = int(50) - 1
        stop =int(stopnum)
        with open('memory.csv', 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter=",", lineterminator="\n")
            writer.writerow([rex, rex + hacks])
        a = 0
        indexx = 0
        for xd in pphone[From:Upto]:
            indexx += 1
            print(f'Index : {indexx}')
            phone = utils.parse_phone(xd)
            print(f"Login {phone}")
            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
            client.connect()
            if not client.is_user_authorized():
                print(f'{r}some thing has changed{n}')
                client.send_code_request(phone)
                client.sign_in(phone, input('Enter the code: '))

            input_file = DevOp
            users = []
            with open(input_file, encoding='UTF-8') as f:
                rows = csv.reader(f, delimiter=",", lineterminator="\n")
                next(rows, None)
                for row in rows:
                    user = {}
                    user['srno'] = row[0]
                    user['username'] = row[1]
                    user['id'] = int(row[2])
                    # user['access_hash'] = int(row[2])
                    user['name'] = row[3]
                    users.append(user)

            with open('memory.csv', 'r') as hash_obj:

                csv_reader = reader(hash_obj)

                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 1
                numnext = list_of_rows[row_number - 1][col_number - 1]

            startfrom = int(numnext)
            nextstart = startfrom + hacks

            with open('memory.csv', 'r') as hash_obj:
                csv_reader = reader(hash_obj)
                list_of_rows = list(csv_reader)
                row_number = 1
                col_number = 2
                numend = list_of_rows[row_number - 1][col_number - 1]

            endto = int(numend)
            nextend = endto + hacks

            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.

                writer = csv.writer(df, delimiter=",", lineterminator="\n")

                writer.writerow([nextstart, nextend])

            client(ImportChatInviteRequest(rexlink))
            time.sleep(5)
            channel = client.get_input_entity(PeerChannel(id))
            channelinfo = client(GetFullChannelRequest(channel=channel))
            rexprodeltanoob = int(channelinfo.full_chat.participants_count)
            print(f'Members: {rexprodeltanoob}')
            if rexprodeltanoob >= stop:
                print(f'The Goal Of {stop} Has Been Completed')
                input()
                quit()

            it = 0
            for user in users:
                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
                    print(f'Members: {rexprodeltanoob}')
                    try:
                        it += 1
                        if user['username'] == "":
                            print(f"{r}no username, moving to next{n}")
                            continue

                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))
                        print(f'{it} - done')

                        time.sleep(Legend_dev)

                    except ChatWriteForbiddenError as cwfe:
                        client(ImportChatInviteRequest(rexlink))
                        time.sleep(5)
                        continue



                    except errors.RPCError as e:
                        status = e.__class__.__name__

                        print(f'{it} - {status}')





                    except:
                        traceback.print_exc()
                        print(f"{ye}Unexpected Error{n}")
                        continue

            a += 1
        os.remove("memory.csv")


    rexchoose = str(input(f'{bl}Press Y if group is private else N : {n}'))
    if rexchoose == 'Y':
        private()
    elif rexchoose == 'N':
        autos()
def MultipleAdder():
    with open('memory.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")
        writer.writerow([1, 1, 50])
    a = int(input("How many accounts do you want to run ? => ")) - 1
    x = 0
    while x <= a:
        subprocess.Popen('python v1-1.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        x = x + 1
        time.sleep(3)
    time.sleep(10)
    os.remove("memory.csv")

def main_menu():
    banner()
    a=int(input(re+"Choose Option from Following:"+cy+"\n       [1]. Accounts \n       [2]. Scraper \n       [3]. Adder \n       [4]. Message Sender"+gr+" \n Enter:"))
    if a==1:
        banner()
        b=int(input(re+"Choose Option from Following:"+cy+"\n       [1]. Login \n       [2]. Ban Filter \n       [3]. AccStats \n       [4]. Change Profile \n       [5]. Clear Profile \n       [6]. Back"+gr+" \n Enter:"))
        if b==1:
            login()
        elif b==2:
            BanFilter()
        elif b==3:
            SpamBotChecker()
        elif b==4:
            SetProfile()
        elif b==5:
            DeleteProfile()
        elif b==6:
            main_menu()
    elif a==2:
        banner()
        b=int(input(re+"Choose Option from Following:"+cy+"\n       [1]. Normal Scraper \n       [2]. Daily Filter \n       [3]. Weekly Filter \n       [4]. Delete ALready Members \n       [5]. Auto Add Contact Phone \n       [6]. Delete Contact \n       [7]. Back"+gr+" \n Enter:"))
        if b==1:
            Scraper()
        elif b==2:
            DailyFilter()
        elif b==3:
            WeeklyFilter()
        elif b==4:
            DeleteALreadyMembers()
        elif b==5:
            AutoaddContactPhone()
        elif b==6:
            DeleteContact()
        elif b==7:
            main_menu()
    elif a==3:
        banner()
        b=int(input(re+"Choose Option from Following:"+cy+"\n       [1]. Adder \n       [2]. Bulk Adder Phone \n       [3]. Bulk Adder Pc \n       [4]. Contact Adder \n       [5]. Multiple Contact Adder \n       [6]. Back"+gr+" \n Enter:"))
        if b==1:
            Adder()
        elif b==2:
            AdderForPhone()
        elif b==3:
            MultipleAdder()
        elif b==4:
            SingleAdder()
        elif b==5:
            BulkAdder()
        elif b==6:
            main_menu()
main_menu()