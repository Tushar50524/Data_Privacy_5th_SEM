document = "This is a sample document that needs to be signed digitally."

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

# Step 2.1: Generate RSA private and public key pair (sender's keys)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Step 2.2: Sign the document with the private key
document_bytes = document.encode('utf-8')
signature = private_key.sign(
    document_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

print("Digital Signature (base64-encoded):", signature.hex())

# Step 4.1: Verify the signature with the public key
from cryptography.exceptions import InvalidSignature

try:
    public_key.verify(
        signature,
        document_bytes,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("The signature is valid. The document is authentic and unaltered.")
except InvalidSignature:
    print("The signature is invalid. The document may have been altered or the signature is not from the expected sender.")

