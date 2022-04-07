import hashlib

class Encrypt:

    def encrypt_code(self, code):
        pass_encrypt = hashlib.md5(str(code).encode())
        encriptado = pass_encrypt.hexdigest()
        return encriptado

    def verify(self, code, code_db):
        code_enc = self.encrypt_code(code)
        if code_enc == code_db:
            return True
        return False