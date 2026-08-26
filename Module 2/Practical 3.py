def encode(m, e, n):
    return (m ** e) % n

def decode(m, d, n):
    return (m ** d) % n

def transmit(message, e, d, n):
    encrypted = encode(message, e, n)
    print("Transmitting:", encrypted)
    decrypted = decode(encrypted, d, n)
    return decrypted