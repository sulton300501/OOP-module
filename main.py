from banking_card_model import BankingCard
class Person:
    def __init__(self,name,lastName,dateOfBirth) -> None:
        self.__name = name
        self.__lastName = lastName
        self.__cards = []
        self.dateOfBirth =  dateOfBirth

    
    def getName(self):
        return f'{self.__name} {self.__lastName}'
    
    def setName(self):
        self.__name = input("Enter your name: ")
        self.__lastName = input("Enter your last name: ")
        print('Your name updates successfully!')
    
    def addCard(self,card:BankingCard):
        self.__cards.append(card)
        print('You have added a new card!')
    
    def removeCard(self,card:BankingCard):
        self.__cards.remove(card)
        print('You have removed a new card!')

    def getBalance(self):
        sum = 0
        for i in self.__cards:
            sum+= i.getBalance()

        return sum
    
    def getAllCards(self):
        for i in self.__cards:
            print(f'{i.cardNumber} - {i.getBalance()} UZS')

    



