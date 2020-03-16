# file = open('new_file.text','w')
# txt='this is our first txt in file'
# file.write(txt)
# file.close

# file = open('new_file.text','r')
# print(file.readlines())
# file.close()
# #
# file=open('new _file.text','a')
# text= '''this our first file but we are not interested in this file.
# we are creating new file.'''
# file.write(text)
# file.close()

import os
os.rename ('filenew,docx','new_file.text')
os.remove('new_file.text')

