def poisonousPlants(p):
    stack = []
    max_dias = 0

    for i in range(len(p)):
        dias = 0

        while stack and stack[-1][0] > p[i]:
            planta_que_muere = stack.pop()
            dias = max(dias, planta_que_muere[1])

        if stack:
            dias += 1
        else:
            dias = 0

        max_dias = max(max_dias, dias)

        stack.append((p[i], dias))

    return max_dias
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
