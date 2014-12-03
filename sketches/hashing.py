from hashlib import sha1


def sha1_32(v):
    return int(sha1(str(v).encode('utf-8')).hexdigest()[:8], 16)
