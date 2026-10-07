def equation(coefficients: tuple) -> int | float:

    try:
        if type(coefficients) != tuple:
            raise TypeError
        try:
            if len(coefficients) != 2:
                raise ValueError("Необходимо передать 2 коэффициента")

        except ValueError as e:
            print(f"Описание оишбки: {e}")
        else:
            a, b = coefficients
            try:

                if a**2 - 1 != 0:
                    x = b / (a**2 - 1)
                    return x
            except ZeroDivisionError as e:
                print(f"Описание ошибки {e}")

    except TypeError as e:
        print(f"Описание ошибки: {e}")
