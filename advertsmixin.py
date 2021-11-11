import json
import keyword
# создаем экземпляр класса Advert из JSON

class Information:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                self.__dict__[key]=Information(value)
            elif keyword.iskeyword(key) or key =='price':
                key = '_'+key
                self.__dict__[key] = value
            else:
                self.__dict__[key] = value
                
class ColorizeMixin:
    def __repr__(self):
        return f'\033[0;{self.repr_color_code}m{self.title} | {self.price} ₽\033[0;0m'
        
class AdForRepr:
    def __repr__(self):
        return f'{self.title} | {self.price} ₽'
    
class Advert(ColorizeMixin, Information, AdForRepr):
    repr_color_code = 32 # green
    def __init__(self, dict_data):
        super().__init__(dict_data)
        self.price
    
    @property
    def price(self):
        if not hasattr(self, '_price'):
            self._price = 0
        if not isinstance(self._price, int):
            raise TypeError('should be int')
        if self._price < 0:
            raise ValueError('must be >==0')
        return self._price

    @price.setter
    def price(self, value):
        self._price=value     

lesson_str = """{
"title": "python",
"price": 4,
"location": {
"address": "город Москва, Лесная, 7",
"metro_stations": ["Белорусская"]
}
}"""
lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)
# обращаемся к атрибуту location.address
lesson_ad.__dict__
lesson_ad.location.address

corgi={
"title": "Вельш-корги",
"price": 1000,
"class": "dogs",
"location": {
"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
}
}
corgi_ad = Advert(corgi)
corgi_ad._class
#lesson_ad.price = 3
  
iphone_ad = Advert(corgi)
print(iphone_ad)
