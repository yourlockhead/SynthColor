from Encoder_Base import Encoder
import sys

user_input = input('Enter a message to encode: ')
e = Encoder()
e.encodeFile(user_input)
e.buildPixels()
e.buildCanvas()
e.save()
