#legal characters. Only these are taken into consideration when shifting. Other characters are excluded (see below - "characters_to_exclude")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) # including 0, to account for 10, 20 etc.
# exclude these characters when looking at the text to translate
characters_to_exclude = [' ', ',', '!', '?', '.', '-', '_', [0-9]]

#Exceptions to catch selection of invalid options as to encoding or shift
#class invalid_input(user_input):
#   pass

#class invalid_enc_or_dec(invalid_input):
#    if u_inp.encode_or_decode_variable not in ['1', '2', 'encode', 'decode']:
#        print('invalid input, \n exitting')
        #exit()

#class invalid_shift_opt(invalid_input):
#    if u_inp.shift_direction_var not in ['1', '2', 'left', 'right']:
#        print('invalid input, \n exitting')
        #exit()
#doesn't work because I don't have access to u_inp, the instance of the user_inputclass, which is on the main top-level script.
#I need to figure this out: review exception class coding
###############################################


class user_input():
    "store the values of the options : encode/decode, left/right, offset etc"
    def __init__(self):
        self.encode_or_decode_var = ''
        self.shift_direction_var = ''
        self.offset = None
        self.input_text_case_intact = None
        self.input_text_var = None #self.input_text_case_intact.lower()

                
    # def encode_or_decode(self):
        

    # def shift_direction(self): 
        

    # def shift_number(self):
        

    # def input_text(self):
        




class translator():
    def __init__(self, offset_direction, offset_amount, text):
          self.dir = offset_direction
          self.num = offset_amount
          self.txt = text
    left_shift_encoded = '' #unlike the above in the init constructor, these are class
    right_shift_encoded = '' #attributes, which stay the same with every instance
    right_shift_decoded = '' #it doesn't really matter, but since they start out as empty strings, without any arguments passed in to initialize values
                            #and need to be accessible from everywhere, having them as class attributes works well
    left_shift_decoded = ''
#######################################################
#ENCODING
#########################################################
class encoder(translator):

    #left shift encoding
    def left_shift(self):       # add a shift_digits with a default of NONE, to also shift digits
        for i in self.txt:

            if i not in alphabet:
                translator.left_shift_encoded += i

            elif i in alphabet:
                key = int(self.num)

                if alphabet.index(i) - key >= 0:
                    i = alphabet[alphabet.index(i) - key]
                    translator.left_shift_encoded += i

                elif alphabet.index(i) - key < 0:
                    remainder = alphabet.index(i) - key
                    i = alphabet[remainder]
                    translator.left_shift_encoded += i

    #right shift encoding
    def right_shift(self):
        #self.encoded = ''
        for i in self.txt:

            if i not in alphabet:
                translator.right_shift_encoded += i

            elif i in alphabet:
                key = int(self.num)

                if len(alphabet) >= alphabet.index(i) + key + 1:
                    i = alphabet[alphabet.index(i) + key]
                    translator.right_shift_encoded += i

                elif len(alphabet) < alphabet.index(i) + key + 1:
                  remainder = (alphabet.index(i) + key) - len(alphabet)
                  i = alphabet[remainder]
                  translator.right_shift_encoded += i
#######################################################
#DECODING
#########################################################
class decoder(encoder, translator):
    def right_shift(self):
        encoder.right_shift(self)
        translator.right_shift_decoded = translator.right_shift_encoded
        #return translator.right_shift_decoded

    def left_shift(self):
        encoder.left_shift(self)
        translator.left_shift_decoded = translator.left_shift_encoded

##############################################################
#function to return the encoded or deoded result with the case intact, as in the initial input string
##############################################################
def case_restorer(original_text, encoded_or_decoded_text):
    orig = original_text
    #strings don't support index assignment : they're immutable
    recase = list(encoded_or_decoded_text)
    ind = [x for x,y in enumerate(orig) if y.isupper()]

    for i in ind:
        recase[i] = recase[i].upper()

    restored = ''.join(recase)
    return restored
    #I struggled quite a bit before I tried the 'enumerate' approach. It wasn't working, because
    #the 'ind' list would return the same index for the same character in 'orig', even though
    #they occupied different positions. "Enumerate" offers a nice and clean solution to that.

    #This could also as easily or even more easily be coded usin the zip function.
    #it would return a list of tuples consisting of each character at the same index in both lists,
    #and then you could just do somehting like if x.isupper(), listb(y).upper()




