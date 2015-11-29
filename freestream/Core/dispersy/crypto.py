#Embedded file name: freestream\Core\dispersy\crypto.pyo
from hashlib import sha1, sha224, sha256, sha512, md5
from math import ceil
from random import randint
from struct import pack
def _progress(*args):
    pass

def ec_public_pem_to_public_bin(pem):
    return ''.join(pem.split('\n')[1:-2]).decode('BASE64')


def ec_private_pem_to_private_bin(pem):
    return ''.join(pem.split('\n')[1:-2]).decode('BASE64')

def ec_to_private_bin(ec):
    return ec_private_pem_to_private_bin(ec_to_private_pem(ec))


def ec_to_public_bin(ec):
    return ec_public_pem_to_public_bin(ec_to_public_pem(ec))


def ec_from_private_bin(string):
    return ec_from_private_pem(''.join(('-----BEGIN EC PRIVATE KEY-----\n', string.encode('BASE64'), '-----END EC PRIVATE KEY-----\n')))


def ec_from_public_bin(string):
    return ec_from_public_pem(''.join(('-----BEGIN PUBLIC KEY-----\n', string.encode('BASE64'), '-----END PUBLIC KEY-----\n')))


def ec_signature_length(ec):
    return int(ceil(len(ec) / 8.0)) * 2


def ec_sign(ec, digest):
    length = int(ceil(len(ec) / 8.0))
    r, s = ec.sign_dsa(digest)
    return '\x00' * (length - len(r) + 4) + r[4:] + '\x00' * (length - len(s) + 4) + s[4:]


def ec_verify(ec, digest, signature):
    length = len(signature) / 2
    prefix = pack('!L', length)
    try:
        return bool(ec.verify_dsa(digest, prefix + signature[:length], prefix + signature[length:]))
    except:
        return False


def rsa_to_private_bin(rsa, cipher = 'aes_128_cbc', password = None):
    pem = rsa_to_private_pem(rsa, cipher, password)
    lines = pem.split('\n')
    return ''.join(lines[4:-2]).decode('BASE64')

def rsa_to_public_bin(rsa, cipher = 'aes_128_cbc', password = None):
    pem = rsa_to_public_pem(rsa, cipher, password)
    lines = pem.split('\n')
    return ''.join(lines[1:-2]).decode('BASE64')

if __name__ == '__main__':

   
    import math
    import time
    for curve in [u'low', u'medium', u'high']:
        ec = ec_generate_key(curve)
        private_pem = ec_to_private_pem(ec)
        public_pem = ec_to_public_pem(ec)
        public_bin = ec_to_public_bin(ec)
        private_bin = ec_to_private_bin(ec)
        print 'generated:', time.ctime()
        print 'curve:', curve, '<<<', EC_name(_curves[curve]), '>>>'
        print 'len:', len(ec), 'bits ~', ec_signature_length(ec), 'bytes signature'
        print 'pub:', len(public_bin), public_bin.encode('HEX')
        print 'prv:', len(private_bin), private_bin.encode('HEX')
        print 'pub-sha1', sha1(public_bin).digest().encode('HEX')
        print 'prv-sha1', sha1(private_bin).digest().encode('HEX')
        print public_pem.strip()
        print private_pem.strip()
        print
        ec2 = ec_from_public_pem(public_pem)
        ec2 = ec_from_private_pem(private_pem)
        ec2 = ec_from_public_bin(public_bin)
        ec2 = ec_from_private_bin(private_bin)
