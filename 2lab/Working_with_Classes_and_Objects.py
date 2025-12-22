class MyName:
    """Опис класу / Документація"""
    
    total_names = 0  # Class variable

    def __init__(self, name=None, domain="itcollege.lviv.ua") -> None:
        """Ініціалізація класу"""
        if name is None:
            self.name = self.anonymous_user().name
        else:
            self.name = self.validate_name(name)
        self.name = self.name.capitalize()  # завжди з великої літери
        self.domain = domain
        MyName.total_names += 1  # змінюємо класову змінну
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        """Class property: повертаємо імя"""
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property: повертаємо емейл"""
        return self.create_email()
    
    @property
    def full_name(self) -> str:
        """Нова властивість full_name"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain=None) -> str:
        """Instance method: створюємо email, можна змінити домен"""
        return f"{self.name}@{domain or self.domain}"

    @classmethod
    def anonymous_user(cls):
        """Class method: об'єкт з ім'ям Anonymous"""
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method: можна змінити текст привітання"""
        return f"You say: {message}"

    def count_letters(self) -> int:
        """Рахує кількість букв у імені"""
        return len(self.name)

    def save_to_file(self, filename="users.txt") -> None:
        """Додає інформацію про користувача у файл"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")
    
    @staticmethod
    def validate_name(name: str) -> str:
        """Перевірка, що ім'я містить лише літери"""
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        return name


# ------------------------------
# Приклад використання класу
# ------------------------------

print("Розпочинаємо створювати об'єкти!")

names = ("Bohdan", "Marta", None, "oleg")  # додано своє ім'я
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("Hi there!")} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
Letters in name: {me.count_letters()}
Full info: {me.full_name}
{"<*>"*20}""")

# Збереження даних у файл
for me in all_names.values():
    me.save_to_file("users.txt")

print(f"We are done. We create {len(all_names)} names! Class total_names: {MyName.total_names}")
