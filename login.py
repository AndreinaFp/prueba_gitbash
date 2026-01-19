nota1=float(input("ingrese la nota1:"))
nota2=float(input("ingrese la nota2:"))
nota3=float(input("ingrese la nota3:"))

promedio= (nota1 + nota2 + nota3)/3

print("El promedio es:",promedio)

if promedio < 3:
 print("Alumno reprobado")

elif promedio >= 4 and promedio < 7:
    
 print ("Alumno aprobado")

elif promedio > 7 and promedio <= 10:
 print("Alumno promocionado")
    
else:
 print("Debes redir finales")
 print("login")  