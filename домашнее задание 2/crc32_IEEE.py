def crc32(text: str) -> str:
    message = ''
    for symbol in text:
        message += bin(ord(symbol))[2:]  # [2:] для 0b1101000 -> 1101000
    g = '100110000010001110110110111'  # 0x04C11DB7
    message = message + '0' * (len(g) - 1)  # дописываем N нулей, где N степень многочлена

    block = message[0:len(g)]
    point = len(g) - 1
    while point < len(message):
        block = bin(int(block, 2) ^ int(g, 2))[2:]  # исключающее побитовое ИЛИ
        while len(block) < len(g):
            point += 1
            if point < len(message):
                block += message[point]
            else:
                return hex(int(block, 2))
