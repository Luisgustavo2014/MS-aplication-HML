from shutil import ExecError
from argon2 import PasswordHasher

## encapsulamento
class EncriptPassword():

    def __init__(self, password):
        self.ph = PasswordHasher()
        self.password = password
        self.__password = ''

    def get_pass(self):
        return self.__password
    
    def set_pass(self, password_imput):
        self.__password = password_imput
    
    # @password.setter
    # def show_pass(self, new_pass):
    #      raise ValueError("Impossivel alterar password diretamente. Use a funcao hash().")

    def hash_password(self):
        self.__password = self.ph.hash(self.password)

    def verify_hash(self):
        try:
            return self.ph.verify(self.__password, self.password)
        except Exception as error:
            print('Erro in verify hash',error)
            return False

    def change_password(self, data, pass_imput):
        self.password = pass_imput
        self.hash_password()



if __name__ == '__main__':
    ec = EncriptPassword('senha%&$¨123578')
    ec.hash_password()    
    print(ec.get_pass())


    