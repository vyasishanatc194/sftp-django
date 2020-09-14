import pysftp as sftp
from paramiko import transport
transport.Transport._preferred_kex = (
        'ecdh-sha2-nistp256',
        'ecdh-sha2-nistp384',
        'ecdh-sha2-nistp521',
        # 'diffie-hellman-group16-sha512',  # disable
        'diffie-hellman-group-exchange-sha256',
        'diffie-hellman-group14-sha256',
        'diffie-hellman-group-exchange-sha1',
        'diffie-hellman-group14-sha1',
        'diffie-hellman-group1-sha1',
)
def push_file_to_server():

    host = "stagingsecureftp.hostanalytics.com"
    user = "Peets_sftp"
    password = "1HZUS9YGVVOZ9ojkFmNJ"
    port = 22
    filename = "TEST.CSV"


    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    s = sftp.Connection(host=host, username=user, password=password, cnopts=cnopts)
    print("connection success")
    # local_path = "testme.txt"
    # remote_path = "/home/testme.txt"

    # s.put(local_path, remote_path)
    s.close()

push_file_to_server()