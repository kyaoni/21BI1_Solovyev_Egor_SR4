A = str(input('Введите имя студента '))
B = str(input('Введите фамилию студента '))
C = int(input('Введите год рождения студента '))
print(A+'_'+B+'_'+str(C))
A,B=B,A
C+=60
print(A+'_'+B+'_'+str(C))