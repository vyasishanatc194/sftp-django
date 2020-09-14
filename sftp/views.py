from django.shortcuts import render
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.
import pandas as pd

from django.http import HttpResponse
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

# SFTP info:
# URL: stagingsecureftp.hostanalytics.com
# User: Peets_sftp
# PW: 1HZUS9YGVVOZ9ojkFmNJ
# Port: 22

# File: TEST.CSV 

def index(request):



    host = "stagingsecureftp.hostanalytics.com"
    user = "Peets_sftp"
    password = "1HZUS9YGVVOZ9ojkFmNJ"
    port = 22
    filename = "TEST.CSV"
    df = False
    
    try:
        cnopts = sftp.CnOpts()
        cnopts.hostkeys = None
        s = sftp.Connection(host=host, username=user, password=password, cnopts=cnopts, port=port)
        
        with s.open("/"+filename, "r+", bufsize=32768) as f:
            df = pd.read_csv(f)
            

        print("Connection succesfully stablished ... ")
        print(df)

        s.close()  
    except:
        raise Http404("Question does not exist")

    context = {
        'data': df.values.tolist(),
    }

    print(context)

    return render(request, 'sftp/index.html', context)

