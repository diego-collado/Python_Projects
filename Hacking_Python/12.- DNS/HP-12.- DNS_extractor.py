'''
Extracción DNS con Python
    Query   ¿Para qué lo uso?
    A	    IPv4
    AAAA	IPv6
    MX	    MailServers
    NS	    NameServers

'''

import dns.resolver
import sys

def dnsQuery(domain, lookuptype):
    try:
        answer = dns.resolver.query(domain,lookuptype)
        for ans in answer:
            if lookuptype == 'A' or lookuptype=='a':
                print('Dominio: {} - DNS Lookuptype: {} - Respuesta: {}'.format(domain,lookuptype,ans.address))
            elif lookuptype == 'AAAA' or lookuptype=='aaaa':
                print('Dominio: {} - DNS Lookuptype: {} - Respuesta: {}'.format(domain,lookuptype,ans.address))
            elif lookuptype == 'MX' or lookuptype=='mx':
                print('Dominio: {} - DNS Lookuptype: {} - Respuesta: {} - Preference: {}'.format(domain,lookuptype,ans.exchange,ans.preference))
            elif lookuptype == 'NS' or lookuptype=='ns':
                print('Dominio: {} - DNS Lookuptype: {} - Respuesta: {}'.format(domain,lookuptype,ans.target))
    except Exception as e:
            print(e)

if __name__ == '__main__':
    if len (sys.argv) != 3 :
        print("\nUSO: python dnsextractor.py [dominio] [querytype]\n")
        print("\tTipos de Query: A(IPv4), AAAA(IPv6), MX(MailServers), NS(NameServers)\n")
        print("Ejemplo: python dnsextractor.py github.com NS\n")
        sys.exit (1)
    else:
        dnsQuery(sys.argv[1], sys.argv[2])