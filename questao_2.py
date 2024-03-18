def fibonacci(num):
    if num <= 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        seq = [0, 1]
        while seq[-1] < num:
            seq.append(seq[-1] + seq[-2])
        return seq

def verifica_na_sequencia(num, seq):
    if num in seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."
        
num = int(input("Digite um número: "))
seq = fibonacci(num)

mensagem = verifica_na_sequencia(num, seq)
print(mensagem)