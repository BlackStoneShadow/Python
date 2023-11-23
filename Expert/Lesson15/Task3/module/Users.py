# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. 
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import os
import json
from collections import defaultdict 
from logging import basicConfig
from logging import getLogger
from logging import INFO
from module import ApplicationExceptions

class User:
    def __init__(self, user_name, user_level, user_id):
        self.user_name = user_name
        self.user_level = user_level
        self.user_id = user_id    
    
    def __repr__(self) -> str:
        return f'User({self.user_name}, {self.user_level}, {self.user_id})'
    
    def __eq__(self, other):
        if self.user_name == other.user_name and self.user_id == other.user_id:
            return True
        else:
            return False
        
    def __hash__(self) -> int:
        return hash((self.user_name, self.user_id))
 

class ProjectUser:
    def __init__(self):
        self.users = set()
        self.user = None
        
        self.logger = getLogger(__name__)
        
        self._load()

    def __str__(self):
        return str(self.users)

    def _load(self):
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                levels = json.load(f)      

            for level, value in levels.items():
                for item in value:                    
                    self.users.add(User(**item))   
        except:
            self.users.add(User('root', '0', '0'))

    def _save(self):
        levels = defaultdict(list)
        for item in self.users:
            levels[item.user_level].append(item)

        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(levels, f, default=vars)
    
    def login_2_sys(self, name, user_id):
        local_user = User(name, None, user_id)
        if local_user in self.users:            
            self.user = next(filter(lambda item: item == local_user, self.users))
            self.logger.info(f'login {local_user}')            
        else:
            raise ApplicationExceptions.AccessExeption
  
    def add_user(self, name, level, user_id):

        if self.user is not None and self.user.user_level < level:
            local_user = User(name, level, user_id)
            if local_user not in self.users:
                self.users.add(local_user)
                self.logger.info(f'add {local_user}')            
                try:
                    self._save()
                except TypeError as text:
                    self.logger.error(text)            
        else:
            raise ApplicationExceptions.LevelExetion

basicConfig(format="{asctime:<25}{levelname:<8}{name:<15}{msg}", style="{", filename="ProjectUser.log", filemode="w", level=INFO)

if __name__ == "__main__":       
    users = ProjectUser() 
    users.login_2_sys('root', '0')
    users.add_user('Ann', '1', '1')
    users.add_user('Pit', '2', '2')

    print(users.user)
    print(users.users)
    