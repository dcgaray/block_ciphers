# block_ciphers
The objectives for this lab assignment are as follows: 
● To explore symmetric key cryptography security with different modes o Electronic Codebook Mode (ECB) o Cipher Block Chaining Mode (CBC)
● Explore the limits of block ciphers in their use 
● Performance Study of Public/Symmetric key Algorithms

Our implementationw is written in python and uses the PyCryptodome library. It is installed using pip. To install simply use the '''_pip install pycryptodome_'''

Task1: Modes of Operation. Explore the differences in security attained by the ECB and CBC modes of encryption. Using the AES-128 primitive provided by 
your cryptographic library, implement the ECB and CBC modes of operations.

Task2: Limits of confidentiality. In this task, you will explore some of the
limits of block ciphers in their use within a secure system. Start by using the
PKCS#7 padding and CBC code from Task 1 to write two “oracle” functions that
emulate a web server that wants to use cryptography to protect access to a site
administration page.

Task 3: Performance Comparison. In this task, we will quantify the performance differences between public and symmetric key algorithms.
Fortunately, OpenSSL provides a simple interface for doing so. => _Openssl speed RSA_ && => _Openssl speed AES_
can perform and measure their respective public and symmetric key operations using different parameters.
