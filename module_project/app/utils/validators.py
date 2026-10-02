class Validator:
    def validate_name(self, name: str) -> str | None:
        if (
            isinstance(name, str)
            and (len(name) > 0 and len(name) < 11)
            and self.is_valid_name(name)
        ):
            return name
        else:
            return None

    @staticmethod
    def is_valid_name(name: str) -> bool:
        if not name:
            return False
        for char in name:
            code = ord(char)
            if not (65 <= code <= 90 or 97 <= code <= 122):
                return False
        return True

    def validate_age(age: int) -> int | None:
        return age if age > 13 and age < 120 else None

    def validate_email(self, email: str) -> str | None:
        if 0 < len(email) < 11 and self.is_valid_email(email):
            return email

        return None

    @staticmethod
    def is_valid_email(email: str) -> bool:
        if email == "":
            return False
        for i in range(len(email)):
            code = ord(email[i])
            if i == 0 and email[0] != "@":
                return False
            elif not (65 <= code <= 90 or 97 <= code <= 122 or code == 46):
                return False
        return True
