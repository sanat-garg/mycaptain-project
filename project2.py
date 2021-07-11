import mimetypes
name = input('\nInput the Filename: ')
filetype = (mimetypes.guess_type(name))
filetype = str(filetype[0])
filetype = filetype.split('/')[1]
if "-" in filetype:
    filetype = filetype.split('-')[1]
print('The extension of the file is: '+filetype+'\n')
