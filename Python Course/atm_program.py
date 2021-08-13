import random
import datetime
from customer import Costumer

cust1 = Costumer(id)

while True:
    pin = int(input('Masukkan nomor PIN anda: '))
    trial_count = 0

    while pin != int(cust1.checkPin()) and trial_count < 3:
        pin = int(input('PIN salah. Silahkan masukkan nomor PIN anda: '))
        trial_count += 1

    if trial_count == 3:
        print('Error. Anda telah salah memasukkan PIN sebanyak tiga kali. Silakan coba lagi.')
        exit()
    
    while True:
        print('\n\nSelamat datang di ATM Progate\n')
        print('1 - Cek Saldo')
        print('2 - Tarik Tunai')
        print('3 - Deposit')
        print('4 - Ganti Pin')
        print('5 - Keluar')
        print('\n------------------------------\n')
        selected_menu = int(input('Silahkan pilih menu: '))

        if selected_menu == 1:
            pass
            #print('Saldo anda saat ini: Rp. '+str(cust1.checkBalance()))

        elif selected_menu == 2:
            value = float(input('Masukkan nominal saldo yang akan ditarik: '))
            verify_withdraw = input('Anda akan melakukan tarik tunai dengan jumlah berikut? (y/n) '+str(value)+' ')

            if verify_withdraw == 'y':
                print('\nSaldo awal anda adalah: Rp. '+str(cust1.checkBalance())+'\n')
            else:
                break
            
            if cust1.checkBalance() < value:
                print("Maaf. Saldo anda tidak cukup untuk melakukan penarikan tunai!")
            else:
                cust1.withdraw(value)
                print('Transaksi berhasil!\nSisa saldo anda saat ini: Rp. '+str(cust1.checkBalance()))

        elif selected_menu == 3:
            value = float(input('Masukkan nominal saldo yang akan disimpan: '))
            verify_deposit = input('Anda akan melakukan deposit dengan jumlah berikut? (y/n) '+str(value)+' ')

            if verify_deposit == 'y':
                cust1.deposit(value)
                print('Saldo anda saat ini: Rp. '+str(cust1.checkBalance()))
            else:
                break
            
        elif selected_menu == 4:
            verify_pin = int(input('Masukkan PIN anda: '))

            while verify_pin != cust1.checkPin():
                verify_pin = int(input('PIN salah. Silahkan masukkan PIN anda: '))

            new_pin = int(input('Silahkan masukkan nomor PIN baru: '))
            verify_newpin = int(input('Masukkan PIN baru anda sekali lagi: '))

            if new_pin == verify_newpin:
                print('PIN berhasil diganti!')
                cust1.pin = new_pin
            else:
                print('PIN tidak sama. PIN gagal diubah!')

        elif selected_menu == 5:
            print('--> Mencetak Resi\n\n')
            print(' Harap simpan tanda terima ini \n sebagai bukti transaksi anda.')
            print('No. : ', random.randint(100000, 1000000))
            print('Tanggal: ', datetime.datetime.now())
            print('Saldo akhir: ',cust1.checkBalance())
            print('\n\nThank you for using this ATM.')
            exit()
        
        else:
            print('Menu tidak tersedia. Silahkan ulangi lagi')