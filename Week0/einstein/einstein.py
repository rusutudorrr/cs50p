def einstein():
    user_mass = int(input("m: "))

    light_speed = 300000000

    E = user_mass * (light_speed ** 2)

    print(f"E: {E}")

einstein()