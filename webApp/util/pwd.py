import hashlib


def hashpwd(pwd):
    hash = hashlib.md5(b'1234')
    hash.update(bytes(pwd, encoding='utf-8'))
    hash_pwd = hash.hexdigest()
    return hash_pwd