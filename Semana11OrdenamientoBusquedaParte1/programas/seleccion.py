def ordenar_vec_seleccion(A):    
   n = len(A)    
   for i in range(n):        
      aux = A[i]        
      pos = i        
      for j in range(i + 1, n):            
          if A[j] < aux:                
              aux = A[j]                
              pos = j        
      # Intercambio        
      A[pos], A[i] = A[i], aux
# Ejemplo de uso
A = [64, 34, 25, 12, 22, 11, 90]
ordenar_vec_seleccion(A)
print("Arreglo ordenado:", A)
