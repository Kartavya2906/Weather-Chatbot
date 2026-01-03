import json
import psycopg2
f=open(r"C:\Users\hp\Desktop\Programming\Python\Independent\crawl\crawl\districtweather.json","r")
data=json.load(f)
con=psycopg2.connect(dbname="Weather",user="postgres",password="Kg2411",host="localhost",port="5432")
cursor=con.cursor()
c=0
for record in data:
    l=list((record.values()))
    newl=l[1:]
    newl.append(l[0])
    t=tuple(newl)
    cursor.execute("""UPDATE "DistrictWeather" SET 
                   "Place"=%s,
                    "MaxTemp"=%s,
                    "MinTemp"=%s,
                    "Rainfall(mm)"=%s,
                    "Relative_Humidity(17:30)"=%s,
                    "Sunset"=%s,
                    "Sunrise"=%s,
                    "Moonset"=%s,
                    "Moonrise"=%s,
                    "Weather_Today"=%s,
                    "Day1"=%s,
                   "Weather_Day1"=%s,
                    "Day2"=%s,
                   "Weather_Day2"=%s,
                    "Day3"=%s,
                   "Weather_Day3"=%s,
                    "Day4"=%s,
                   "Weather_Day4"=%s,
                    "Day5"=%s,
                   "Weather_Day5"=%s,
                    "Day6"=%s,
                   "Weather_Day6"=%s
                   WHERE "URL"=%s """,t)
    c+=1
con.commit()
cursor.close()
con.close()
print("updated",c)