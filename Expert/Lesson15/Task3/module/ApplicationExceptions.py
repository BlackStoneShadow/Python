# Создайте класс с базовым исключением и дочерние классы-исключения: 
# ошибка уровня, ошибка доступа.
class BaseExption(Exception):
    pass

class LevelExetion(BaseExption):
    pass

class AccessExeption(BaseExption):
    pass