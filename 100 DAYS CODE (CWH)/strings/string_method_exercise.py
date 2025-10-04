'''
str = 'X-DSPAM-Confidence: 0.8475'
use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
'''

str = 'X-DSPAM-Confidence: 0.8475'
sliced_string = str[str.find(':') + 1:].strip()
new_num = float(sliced_string)
print(new_num)
print(type(new_num))


