from os import system
import sys
from time import sleep, strftime
import telepot
import lampu


global pin_lampu
pin_lampu = lampu.pin_lampu


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Pesan diterima: %s' % command

    if command == "Menu" or command == "menu" or command == "/menu":
        bot.sendMessage(chat_id, \
	"Silakan pilih menu yang tersedia: \n"\
	"1. Lampu Luar Ruko \n"\
	"2. CCTV ")

    if command == "Lampu Luar Ruko":
        status1 = open("status1.txt", "r").read()
        bot.sendMessage(chat_id, "Status sebelumnya --> %s" % (status1))
        if status1 == "mati":
            lampu.lampu_on(pin_lampu)
            file = open("status1.txt", "w")
            file.write("menyala")
            file.close()
            bot.sendMessage(chat_id, "Lampu Luar Ruko \nDINYALAKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))
        elif status1 == "menyala":
            lampu.lampu_off(pin_lampu)
            file = open("status1.txt", "w")
            file.write("mati")
            file.close()
            bot.sendMessage(chat_id, "Lampu Luar Ruko \nDIMATIKAN pada " + strftime("%A %d %B %Y %X %Z"))
            status1 = open("status1.txt", "r").read()
            bot.sendMessage(chat_id, "Status sekarang --> %s" % (status1))

    elif command == "CCTV":
        system("sudo python camera.py")
        file = open("status2.txt", "w")
        file.write("Gambar CCTV terakhir diambil pada " + strftime("%A %d %B %Y %X %Z"))
        file.close()
        #bot.sendMessage(chat_id, "Gambar berhasil diampil. Sedang dalam proses pengiriman ke Telegram.")
        bot.sendMessage(chat_id, 'Mengirim gambar CCTV. Harap tunggu...')
        bot.sendPhoto(chat_id, open('image1.jpg', 'rb'), caption='Situasi terkini')


    if command == 'Status':
        status1 = open('status1.txt', 'r').read()
        status2 = open('status2.txt', 'r').read()
        
        bot.sendMessage(chat_id, \
        "Status kondisi perangkat listrik saat ini --> \n"\
        "1. Lampu Luar Ruko	--> %s\n" \
        "2. CCTV		--> %s\n" % (status1, status2))

    show_keyboard = {'keyboard': [['Lampu Luar Ruko'], ['CCTV'], ['Menu', 'Status']]}
    bot.sendMessage(chat_id, 'Pilih menu cepat :', reply_markup=show_keyboard)

bot = telepot.Bot('194671155:AAFQ4Veb_Xy5HG17NI3yJ5w2xULKDmAIvOI')
bot.message_loop(handle)
print 'Mendengarkan ...'

while 1:
    sleep(10)
