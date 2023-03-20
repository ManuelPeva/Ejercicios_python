'''Definir una función max_de_lista(), que tome los numeros de una lista como argumentos
y devuelva el mayor de ellos'''

nums = input("Digite los valores separados por una coma: ")

nums = [int(num) for num in nums.split(',')]

#list_valores = [1,99,22,34,312,832,222,837,231,238]

maximo = max(nums)

print(f"El valor más alto de tu lista es: {maximo}")