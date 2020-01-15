var= input('Enter ip address - ')
print('Entered IP Address is - ',var)
forIP = 'a-w-s'+var
print('formatted IP addr  - ',forIP)
file1= open('ip.gedit','w')
file1.write('Entered IP Address is - '+var+'\n')
file1.write('formatted IP addr  - '+forIP)
