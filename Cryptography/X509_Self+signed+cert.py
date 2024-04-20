# to setup the expiration date
from datetime import datetime, timedelta
# digital certificate standard
from cryptography import x509
# assign name to the cert in a form of object ID
from cryptography.x509.oid import NameOID
# hashes to sign our own certificate
from cryptography.hazmat.primitives import hashes
# default_backend to shield form the comlexity of crypto functions
from cryptography.hazmat.backends import default_backend
# to save the private keys and certs to a file
from cryptography.hazmat.primitives import serialization
# to create RSA public and private keys
from cryptography.hazmat.primitives.asymmetric import rsa
#
import ipaddress


server_IP = '10.80.104.231' # It is recommended to use IP address for selfsigned certificate
h_name = 'ca_server' # Host name which required to configure it correctly to use some of the browsers such as chrome

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend(),
)

name = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, h_name)
])

alt_names = [x509.DNSName(h_name)]
alt_names.append(x509.DNSName(server_IP))
alt_names.append(x509.IPAddress(ipaddress.ip_address(server_IP))) # import so chrome does not complain

basic_contraints = x509.BasicConstraints(ca=True, path_length=0)
now = datetime.utcnow()
cert = (
    x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(1000)
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=365))
        .add_extension(basic_contraints, True)
        .add_extension(x509.SubjectAlternativeName(alt_names), False)
        .sign(key, hashes.SHA256(), default_backend())
)

my_cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
my_key_pem = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

with open('test_ubuntu_new.crt', 'wb') as c:
    c.write(my_cert_pem)

with open('test_ubuntu_new.key', 'wb') as c:
    c.write(my_key_pem)

