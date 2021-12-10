import doctest
from morse import decode
from morse import encode


def test_decode(string):
   """
   morse to letter
   >>> test_decode('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.')
   'MAI-PYTHON-2019'
   """
   return decode(string)


def test_encode(string):
   """
   letter to morse
   >>> test_encode('SOS')
   '... --- ...'
   >>> test_encode('P' * 30) #doctest: +ELLIPSIS
   '.--. ... .--.'
   >>> test_encode('S   O   S') # doctest: +NORMALIZE_WHITESPACE
   '... --- ...'
   >>> test_encode(30.1)
   Traceback (most recent call last):
        ...
   TypeError: 'float' object is not iterable
   """
   return encode(string)


if __name__ == '__main__':
   doctest.testmod()
   
