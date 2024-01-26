### Python Door Lock Software

#### Purpose:
This Python program simulates a door lock system. It allows users to lock and unlock a virtual door, change the password, and perform other related functions.

#### Classes and Functions:
1. **DoorLock Class:**
   - `__init__(self, default_password)`: Initializes the door lock system with a default password and other parameters.
   - `auto_lock(self, auto_lock_time)`: Sets a timer to automatically lock the door after a specified time.
   - `terminal_cleaner(self)`: Clears the terminal screen based on the operating system.
   - `lock_door(self)`: Simulates the process of locking the door by turning a motor.
   - `unlock_door(self)`: Simulates unlocking the door by rotating the motor, and clears the terminal screen.
   - `change_password(self)`: Allows users to change the door lock password with certain constraints.
   - `run(self)`: Main function that runs the door lock system, displaying a menu for different actions.

#### Usage:
Instantiate the `DoorLock` class with a default password, and then call the `run()` method to start the door lock system. The user can interact with the system through the terminal menu.


### Python Kapı Kilit Yazılımı

#### Amaç:
Bu Python programı sanal bir kapı kilidi sistemini simüle eder. Kullanıcılara sanal bir kapı kilitleme ve açma, şifre değiştirme ve diğer ilgili işlevleri gerçekleştirme imkanı tanır.

#### Sınıflar ve Fonksiyonlar:
1. **DoorLock Sınıfı:**
   - `__init__(self, default_password)`: Kapı kilidi sistemini varsayılan bir şifre ve diğer parametrelerle başlatır.
   - `auto_lock(self, auto_lock_time)`: Belirli bir süre sonra kapıyı otomatik olarak kilitlemek için bir zamanlayıcı ayarlar.
   - `terminal_cleaner(self)`: İşletim sistemine bağlı olarak terminal ekranını temizler.
   - `lock_door(self)`: Kapıyı bir motoru çevirerek kilitlenmiş gibi simüle eder.
   - `unlock_door(self)`: Motoru çevirerek kapıyı açma işlemini simüle eder ve terminal ekranını temizler.
   - `change_password(self)`: Kullanıcılara belirli kısıtlamalarla kapı kilidi şifresini değiştirme imkanı tanır.
   - `run(self)`: Kapı kilidi sistemini çalıştıran ana fonksiyon, farklı işlemleri gerçekleştirmek için bir menü gösterir.

#### Kullanım:
`DoorLock` sınıfını varsayılan bir şifre ile örneklendirin ve ardından kapı kilidi sistemini başlatmak için `run()` yöntemini çağırın. Kullanıcı sistemle terminal menüsü aracılığıyla etkileşimde bulunabilir.
