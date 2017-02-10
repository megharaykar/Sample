import subprocess

#dictionary containing region and IP address with their latencies
IPwithlatency = {'us-east-1 50.17.255.254':0,'us-west-1 52.52.63.252':0,'eu-west-1 52.30.63.252':0,'ap-north-east-1 52.196.63.252':0,'us-east-2 52.14.64.0':0,'us-west-2 52.32.63.252':0,'eu-central-1 52.29.63.252':0,'ap-northeast-2 52.78.63.252':0,'us-gov-west-1 52.222.9.163':0,'eu-west-2 52.56.34.0':0,'ap-southeast-2 52.76.191.252':0,'ca-central-1 52.64.63.253':0,'eu-west-2 52.66.66.2':0,'ap-southeast-2 54.94.191.252':0,'ap-south-1 52.72.63.252':0}
for key,value in IPwithlatency.items():
 keys=key.split(" ")
 host=keys[1]
 ping = subprocess.Popen(["ping","-n","3",host],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 out, error = ping.communicate()
 output=out.decode().split("=")
 out=output[15]
 out1=out.split("ms")[0].strip()
 IPwithlatency[key]=int(out1)

#sorting based on average latency
 sortedlatencies=sorted(IPwithlatency.items(), key=lambda item: item[1])

inc=0
#print the results
for key,value in sortedlatencies:
 inc=inc+1
 print(str(inc)+'. ' + str(key) +' - '+ str(value) + 'ms')


