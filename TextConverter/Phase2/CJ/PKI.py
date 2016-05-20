A public key infrastructure (PKI) is a set of roles, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and manage public-key encryption.

PKI can also be incorporated into the Python language. This is mainly used to encrypt files and documents.

Generating a public/private key: 


 from Crypto.PublicKey import RSA

 from Crypto import Random

 random_generator = Random.new().read

 key = RSA.generate(1024, random_generator)

 key
<_RSAobj @0x7f60cf1b57e8 n(1024),e,d,p,q,u,private>


Encrypting the Data: 
 1
>>> public_key = key.publickey()
2
>>> enc_data = public_key.encrypt('abcdefgh', 32)
3
>>> enc_data
4
('\x11\x86\x8b\xfa\x82\xdf\xe3sN ~@\xdbP\x85
5
\x93\xe6\xb9\xe9\x95I\xa7\xadQ\x08\xe5\xc8$9\x81K\xa0\xb5\xee\x1e\xb5r
6
\x9bH)\xd8\xeb\x03\xf3\x86\xb5\x03\xfd\x97\xe6%\x9e\xf7\x11=\xa1Y<\xdc
7
\x94\xf0\x7f7@\x9c\x02suc\xcc\xc2j\x0c\xce\x92\x8d\xdc\x00uL\xd6.
8
\x84~/\xed\xd7\xc5\xbe\xd2\x98\xec\xe4\xda\xd1L\rM`\x88\x13V\xe1M\n X
9
\xce\x13 \xaf\x10|\x80\x0e\x14\xbc\x14\x1ec\xf6Rs\xbb\x93\x06\xbe',)

 
