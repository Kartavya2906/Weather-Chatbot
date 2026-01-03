import schedule
import time
import subprocess
s=time.perf_counter()
f=open(r"C:\Users\hp\Desktop\Programming\Python\Independent\crawl\crawl\districtweather.json","w")
f.write("")
f.close() 
print("cleared json")
def runprog():
    subprocess.run(["scrapy","crawl","spider","-o","districtweather.json"],cwd=r"C:\Users\hp\Desktop\Programming\Python\Independent\crawl\crawl")      #executes directly without shell
    #subprocess.run("scrapy crawl spider -o districtweather.json", shell=True, cwd=r"C:\Users\hp\Desktop\Programming\Python\Independent\crawl\crawl")    runs in shell toh hacker may attack
    subprocess.run(["python",r"C:\Users\hp\Desktop\Programming\Python\Independent\crawl\database.py"])
    print("Crawled n updated")
runprog()
e=time.perf_counter()
t=e-s
print(t//60," minutes ",t%60," seconds ")