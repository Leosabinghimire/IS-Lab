from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta, timezone

def generate_private_key():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

def create_self_signed_certificate(private_key):
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Example Inc."),
    ])
    
    cert = x509.CertificateBuilder().subject_name(subject
    ).issuer_name(issuer
    ).public_key(private_key.public_key()
    ).serial_number(x509.random_serial_number()
    ).not_valid_before(datetime.now(timezone.utc)
    ).not_valid_after(datetime.now(timezone.utc) + timedelta(days=365)
    ).add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True
    ).add_extension(x509.SubjectAlternativeName([x509.DNSName(u"example.com")]), critical=False
    ).sign(private_key, hashes.SHA256())
    
    return cert

def save_certificate(cert, private_key):
    with open("certificate.pem", "wb") as cert_file:
        cert_file.write(cert.public_bytes(serialization.Encoding.PEM))
    
    with open("private_key.pem", "wb") as key_file:
        key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

if __name__ == "__main__":
    private_key = generate_private_key()
    cert = create_self_signed_certificate(private_key)
    save_certificate(cert, private_key)
    
    print("Certificate and private key have been generated and saved.")
