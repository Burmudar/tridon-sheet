import hashlib

def hash_file(file):
    hasher = hashlib.sha256()
    hasher.update(file.read())
    file_hash = hasher.hexdigest()
    return file_hash
