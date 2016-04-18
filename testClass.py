import random
from PIL import Image
import os, sys
import datetime

class Encoder(object):
    def __init__(self):
        self.Encoded = [] # List holding the input message characters encoded to RGB values
        self.Pixels = [] # List of Tuples, each tuple representing a pixel for the final Image
        self.EncodedKeys = {} # DIctionary of Key(alphanumeric) Values(RGB representation) for encoding input... THE CIPHER
        self.Alphabet = ' abcdefghijklmnopqrstuvwxyz.,()-'
        self.fileName = str(datetime.date.today()) + "-" + str(random.randint(1,100)) + ".png"
        self.buildList()

    # build out a dictionary for all the characters in self.Alphabet and their corresponding rgb values
    def buildList(self):
        byteValues = list(map(ord, self.Alphabet))
        for i in self.Alphabet:
            self.EncodedKeys[i] = byteValues[self.Alphabet.index(i)]
            # TODO: could write a randomization algo here to make the byte value something based off of a key
            #ex self.EncodedKeys[i] = self.randomizeByte(byteValues[self.Alphabet.index(i)])

    # take a message from the user and encode it with the encoding keys.
    def encodeMessage(self,msg):
        for i in msg.lower():
            self.Encoded.append(self.EncodedKeys[i])

        # we break off the encoded values into tuples of 3 so the Encoded list needs x%3==0 to be true for pixel processing
        while(len(self.Encoded)%3 != 0):
            self.Encoded.append(255)

    def buildPixels(self):
        index = 0
        for i in range(len(self.Encoded)//3):
            self.Pixels.append((self.Encoded[i], self.Encoded[i+1], self.Encoded[i+2], 150))
            counter = index + 3

    def buildCanvasBlock(self):
        dimension = len(self.Pixels)
        self.canvas = Image.new('RGBA', (dimension,dimension))
        for x in range(dimension):
            for y in range(dimension):
                self.canvas.putpixel((x,y), self.Pixels[x])

    def buildCanvas(self):
        self.canvas = Image.new('RGBA', (1, len(self.Pixels)))
        for x in range(len(self.Pixels)):
            self.canvas.putpixel((0,x), self.Pixels[x])

    def save(self):
        print('Saving file ', self.fileName)
        self.canvas.save('Images/' + self.fileName)
        os.system("start Images/" + self.fileName)
