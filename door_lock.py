import time #I added it to wait for engine speed. / Motor dönüşünü beklemek için ekledim.
import os ##I added it to clean the text in the terminal. / Terminaldeki yazıları temizlemek için ekledim.

class DoorLock:
    def __init__(self, default_password):
        self.password = default_password
        self.password_change = False
        self.password_history = []
        self.lock_engine_speed_duration = 2 #Waiting time for engine speed. / Motorun dönüşü için bekleme süresi.

    def auto_lock(self, auto_lock_time):
        print("After ",auto_lock_time," seconds it will automatically lock. / ",auto_lock_time," saniye sonra otomatik olarak kilitlenecektir.")
        time.sleep(auto_lock_time)
        self.lock_door()
        
    def terminal_cleaner(self):
         # If Operating System is Windows / İşletim Sistemi Windows ise
        if os.name == 'nt':
            _ = os.system('cls')
        # If Operating System is MacOS / İşletim Sistemi MacOS ise
        elif os.name == 'mac':
            _ = os.system('clear')
        # If Operating System is Linux / İşletim Sistemi Linux ise
        elif os.name == 'posix':
            _ = os.system('clear')
        # Another operating system is / Başka bir işletim sistemi ise
        else:
            _ = os.system('clear')

    def lock_door(self):
        print("The door is locking... / Kapı kilitleniyor...")
        #Add the code here to lock the door by turning the motor. / Motoru döndererek kapıyı kilitlemek için gerekli kodu buraya ekleyin.
        time.sleep(self.lock_engine_speed_duration ) #motorun dönüşü için bekleme
        self.run()

    def unlock_door(self):
        print("The door is unlocking... / Kapı kilidi açılıyor...")
        #Add the code here to open the door by rotating the motor. / Motoru döndererek kapıyı açmak için gerekli kodu buraya ekleyin.
        time.sleep(self.lock_engine_speed_duration) #motorun dönüşü için bekleme
        self.terminal_cleaner()
        print("**DOOR UNLOCKED / KAPI KİLİTİ AÇIK**")

    def change_password(self):
        new_password = input("Enter your new password: / Yeni şifrenizi giriniz:\n>")
        if new_password == self.password:
            self.terminal_cleaner()
            print("Error! Failed to change password. Your new password cannot be the same as your old password. / Hata! Şifre değiştirilemedi. Yeni şifreniz eski şifrenizle aynı olamaz.")
        elif new_password in self.password_history:
            self.terminal_cleaner()
            print("Error! Failed to change password. Your new password cannot be one of your old passwords. / Hata! Şifre değiştirilemedi. Yeni şifreniz eski şifrelerinizden biri olamaz.")
        else:
            self.terminal_cleaner()
            new_password_matching = input("Enter your new password again: / Yeni sifrenizi tekrar giriniz:\n>")
            if new_password == new_password_matching:  
                self.password_history.append(self.password)
                self.password = new_password
                self.password_change = True
                self.terminal_cleaner()
                print("Your password was successfully changed. / Şifreniz başarıyla değiştirildi.")
            else:
                self.terminal_cleaner()
                print("Error! Failed to change password. Your new passwords do not match. / Hata! Şifre değiştirilemedi. Yeni şifreleriniz birbirleri ile eşleşmiyor.")
            


    def run(self):
        self.terminal_cleaner()
        while True:
            print("**DOOR LOCKED / KAPI KİLİTLİ**")
            user_password = input("Enter your password to unlock: / Kilidi açmak için şifrenizi giriniz:\n>")
            self.terminal_cleaner()
            if user_password == self.password:
                self.unlock_door()
                break
            else:
                #print("Incorrect password. Please try again. / Hatalı şifre. Lütfen tekrar deneyiniz.")
                continue

        while True:
            
            command = input("----\nMenu / Menü\n----\n[1] - Lock the door. / Kapıyı kilitle.\n[2] - Change password. / Şifreyi değiştir.\n>")
            if command == "1":
                self.terminal_cleaner()
                self.lock_door()
                
            elif command == "2":
                self.terminal_cleaner()
                self.change_password()
            else:
                print("Invalid command. Please try again. / Geçersiz komut. Lütfen tekrar deneyin.")

        return

lock = DoorLock("1234")
lock.run()
