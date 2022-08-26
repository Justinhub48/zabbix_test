import sys
import argparse
import datetime
from pyzabbix import ZabbixMetric, ZabbixSender, ZabbixResponse

def skaiciuokle(n):
    i=1
    array=[]
    while n != 1:
        #print(n) 
        array.append(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        i=i+1
        
    else:
        #print(n)
        #print('Atlikta!')
        #print('zngsniai iki ciklo:',i)
        #print(array)
        maks = max(array)
        #print(maks)
        metrics = []
        m = ZabbixMetric('zabbixagent', 'highest.number', maks)
        metrics.append(m)
        ZabbixSender('10.0.2.4').send(metrics)

def laikas():
    time = datetime.datetime.now()
    minutes = time.minute
    sekundes = time.second
    return(minutes*sekundes)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=laikas())
    args = parser.parse_args()

    n = args.input

    try:
    	sk = int(n)
    except ValueError:
    	print('blogas simbolis')
    	time = str(datetime.datetime.now())
    	f=open('validationerrlog.txt', 'a+')
    	f.write(time + ' blogas simbolis \n')
    	return()

    if  sk >= 1:
        skaiciuokle(sk)
    else:
        print('neigiamas skaicius')
        time = str(datetime.datetime.now())
        f=open('validationerrlog.txt', 'a+')
        f.write( time + ' neigiamas skaicius \n')
main()
