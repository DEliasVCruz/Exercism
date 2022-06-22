from secrets import SystemRandom

random_generator = SystemRandom()

def private_key(p: int) -> int:
    return random_generator.randrange(2, p)


def public_key(p: int, g: int, private: int) -> int:
    return (g ** private) % p


def secret(p: int, public: int, private: int) -> int:
    return (public ** private) % p
