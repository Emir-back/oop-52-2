class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__cpu

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f' Computer with {self.__cpu} CPU and memory - {self.__memory}GB'

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory


    def make_computations(self):
        result = self.__cpu * self.__memory
        return result

class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return super().__str__() + f' Sim_cards_list - {self.__sim_cards_list} '




    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} ({sim_card})")
        else:
            print("Сим-карта с таким номером не существует.")

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps (self , location):
        return f'Маршрут до {location} построен'

    def __str__(self):
        computer_info = Computer.__str__(self)
        phone_info = Phone.__str__(self)
        return f"{computer_info} {phone_info}"

computer = Computer(4, 16)
print(computer)
phone = Phone(["Beeline", "O!", "MegaCom"])  # 3 сим-карты
print(phone)
smartphone1 = SmartPhone(8, 64, ["Beeline", "O!"])
print(smartphone1)
smartphone2 = SmartPhone(6, 32, ["MegaCom", "Beeline"])
print(smartphone2)

print("Result of make_computations for computer:", computer.make_computations())

# Для объекта Phone
phone.call(1, "+996 777 59 48 11")
phone.call(2, "+996 777 59 48 32")
phone.call(3, "+996 777 59 48 23")

smartphone1.use_gps("Geeks")
smartphone2.use_gps("home")
print("smartphone1 > smartphone2:", smartphone1 > smartphone2)
print("computer == smartphone2:", computer == smartphone2)
