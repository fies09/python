#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/12 21:18
# @Author     : fany
# @Project    : PyCharm
# @File       : 01_python的cryptography加密与解密.py
# @description:
# from cryptography.fernet import Fernet
# # =========生成密钥============
# secret_key = Fernet.generate_key()  # 加密key
# print("密钥", secret_key)
#
# # =========加密数据============
# msg = "hello python"
#
# cipher = Fernet(secret_key)
# ret = cipher.encrypt(msg.encode("utf-8"))
# print("加密数据", ret.decode("utf-8"))
#
# # =========解密数据============
# msg = cipher.decrypt(ret)
# print("解密数据", msg.decode("utf-8"))

# 对上述代码进行封装
# import base64
# from cryptography.fernet import Fernet
# def generate_key():
#     return Fernet.generate_key()
# class Cipher:
#
#     def __init__(self, secret_key):
#         if not isinstance(secret_key, bytes):
#             secret_key = secret_key.encode()
#         self.cipher = Fernet(secret_key)
#
#     def encrypt(self, data):
#         encrypt_data = self.cipher.encrypt(data.encode("utf-8")).decode()
#         return encrypt_data
#
#     def decrypt(self, encrypt_data):
#         decrypt_data = self.cipher.decrypt(encrypt_data.encode("utf-8")).decode()
#         return decrypt_data
#
#
# if __name__ == '__main__':
#     sk = "Oe4PWwBs0oEKnYlmWUZcFehfHv2AWPTU8J7tH0un3YI="
#     c = Cipher(sk)
#     e = c.encrypt("asd")
#     d = c.decrypt(e)
#     print(e)
#     print(d)

# AES-ECB加解密
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
#
# import base64
#
# block_size = 128
#
#
# def aes_encrypt(secret_key, data):
#     """加密数据
#     :param secret_key: 加密秘钥
#     :param data: 需要加密数据
#     """
#     # 将数据转换为byte类型
#     data = data.encode("utf-8")
#     secret_key = secret_key.encode("utf-8")
#
#     # 填充数据采用pkcs7
#     padder = padding.PKCS7(block_size).padder()
#     pad_data = padder.update(data) + padder.finalize()
#
#     # 创建密码器
#     cipher = Cipher(
#         algorithms.AES(secret_key),
#         mode=modes.ECB(),
#         backend=default_backend()
#     )
#     # 加密数据
#     encryptor = cipher.encryptor()
#     encrypted_data = encryptor.update(pad_data)
#     return base64.b64encode(encrypted_data).decode()
#
#
# def aes_decrypt(secret_key, data):
#     """解密数据
#     """
#     secret_key = secret_key.encode("utf-8")
#     data = base64.b64decode(data)
#
#     # 创建密码器
#     cipher = Cipher(
#         algorithms.AES(secret_key),
#         mode=modes.ECB(),
#         backend=default_backend()
#     )
#     decryptor = cipher.decryptor()
#     decrypt_data = decryptor.update(data)
#     unpadder = padding.PKCS7(block_size).unpadder()
#     unpad_decrypt_data = unpadder.update(decrypt_data) + unpadder.finalize()
#     return unpad_decrypt_data.decode("utf-8")
#
#
# if __name__ == '__main__':
#     key = "22a1d4c4263e83d7f8c33a321eb19ae7"
#     data = "asdASD73j8H9k6C1asvhBOK0PXOzJM7dsqXysssW"
#
#     print("原始数据：%s" % data)
#     r = aes_encrypt(key, data)
#     print("加密数据：%s" % r)
#     r = aes_decrypt("22a1d4c4263e83d7f8c33a321eb19ae7", r)
#     print("解密数据：%s" % r)

# AES-GCM加解密
import random
import string

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64


def encrypt_aes_gcm(key, data, associated_data=None, nonce=None):
    """
    AES-GCM加密
    :param key: 密钥。16, 24 or 32字符长度的字符串
    :param data: 待加密字符串
    :param associated_data: 附加数据，一般为None
    :param nonce: 随机值，和MD5的“加盐”有些类似，目的是防止同样的明文块，始终加密成同样的密文块
    """
    key = key.encode('utf-8')
    data = data.encode('utf-8')
    # 假如先后端约定随机值为16位长度的字符串
    nonce = nonce or "1234567812345678"
    nonce = nonce.encode("utf-8")
    if associated_data is not None:
        associated_data = associated_data.encode()

    # 生成加密器
    cipher = AESGCM(key)
    # 加密数据
    crypt_bytes = cipher.encrypt(nonce, data, associated_data)
    return base64.b64encode(nonce + crypt_bytes).decode()


def decrypt_aes_gcm(key, cipher_data, associated_data=None):
    """
    AES-GCM解密
    :param cipher_data: encrypt_aes_gcm 方法返回的数据
    :return:
    """
    key = key.encode('utf-8')

    # 进行base64解码
    debase64_cipher_data = base64.b64decode(cipher_data)

    # 分割数据
    nonce = debase64_cipher_data[:16]
    cipher_data = debase64_cipher_data[16:]

    cipher = AESGCM(key)
    if associated_data is not None:
        associated_data = associated_data.encode()

    # 解密数据
    plaintext = cipher.decrypt(nonce, cipher_data, associated_data)
    return plaintext.decode()


if __name__ =='__main__':
    aes_key = 'DnKRYZbvVzdhPlF10rtcxmi5Cj36AbCd'
    associated_data = None
    nonce = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    data = '{"lang":"zh-CN","pageNumber":1,"pageSize":10,"cycleId":"1522973936269266945"}'
    print("原始数据：" + data)

    cipher_data = encrypt_aes_gcm(aes_key, data, associated_data=associated_data, nonce=nonce)
    print("加密数据：" + cipher_data)

    de_data = decrypt_aes_gcm(aes_key, cipher_data, associated_data)
    print("解密数据：" + de_data)