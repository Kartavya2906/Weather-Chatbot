import psycopg2
import speechinput
import speechoutpyttsx

con=psycopg2.connect(dbname="Weather",user="postgres",password="Kg2411",host="localhost",port="5432")
cursor=con.cursor()
def para(l):
     s1=f"\n\nHere’s the latest weather update for {l[0][1]}.\n\nToday, the weather is {l[0][10]} with a maximum temperature of {l[0][2]}°C and a minimum of {l[0][3]}°C."
     s2="\nOverall the day is "
     d=((float)(l[0][2])+(float)(l[0][3]))/2
     if (d>30):
          s3="hot"
          s5="stay hydrated!"
     elif (d<30 and d>22):
          s3="warm"
          s5="engage yourself in outdoor activities!"
     elif (d<22 and d>18):
          s3="pleasant"
          s5="go outside and enjoy the weather!"
     else:
          s3="chilly"
          s5="wear warm clothes!"
     s4=". It is advised to "
     r=l[0][4]
     try:
          rain=(int)(r)
     except:
          rain=0
     if (rain!=0):
          s13=f"\n\n{rain}mm of rainfall was recorded.It is advised to carry an umbrella.\n"
     else:
          s13="\n\nNo rain today! A great day to enjoy the outdoors.\n"
     s6=f"The humidity is around {l[0][5]}%, Air feels like "
     h=(float)(l[0][5])
     if (h>50):
          s7="humid."
     elif (h<50 and h>30):
          s7="comfortable. "
     else:
          s7="dry. "
     daylight=(((int)((l[0][6])[:2])*60)+((int)((l[0][6])[3:])))-(((int)((l[0][7])[:2])*60)+((int)((l[0][7])[3:])))
     s8=f"""\n\nThe sun would give us {daylight//60} hours and {daylight%60} minutes of daylight from {l[0][7]}.
The moon cycle is from {l[0][9]} to {l[0][8]}.
Tomorrow's weather is anticipated as {l[0][12]}.

Do u want forecast of next 6 days? (say confirm or no)"""
     speechoutpyttsx.tts(s1+s2+s3+s4+s5+s13+s6+s7+s8)
     f=speechinput.voicein()
     if ((('confirm' in f.lower()) or ('yes' in f.lower())) and (('no' not in f.lower()) and ('not' not in f.lower()))):
          s9=f"""\nWeather on 
{l[0][11]} is {l[0][12]}
{l[0][13]} is {l[0][14]}
{l[0][15]} is {l[0][16]}
{l[0][17]} is {l[0][18]}
{l[0][19]} is {l[0][20]} """
          if (l[0][21]!=""):
               s9+=f"\n{l[0][21]} is {l[0][22]}\n"
          else:
               s9+="\nWeather of 6th Day is not available.\n"
     else: 
          s9=""
     s10="\nFor more info visit the following url:"
     speechoutpyttsx.tts(s9+s10)
     s11=l[0][0]
     print(s11)
     s12="\nStay prepared, stay safe, and have a wonderful day ahead!"
     speechoutpyttsx.tts(s12)

def fetch(k):
    cursor.execute("""select "Place" from "DistrictWeather" """)
    place=cursor.fetchall()
    for i in place:      
            for j in i:
                if (k.lower()==j.lower()):
                    k=j
    cursor.execute("""select * from "DistrictWeather" where "Place"=%s """,(k,))
    m=cursor.fetchall()
    print()
    if (len(m)==0):
         p=k
         for i in place:      
            for j in i:
                if k.lower() in j.lower():
                    k=j
         cursor.execute("""select * from "DistrictWeather" where "Place"=%s """,(k,))
         m=cursor.fetchall()
         if(len(m)==0):
            speechoutpyttsx.tts(str(k)+" is not present. ")
         else:
              speechoutpyttsx.tts(str(p)+" is not present. But we have another district: ")
    if (len(m)!=0):
          for i in range(len(m[0])):
               print(str(col[i][0])+": "+str(m[0][i]))
               # speechoutpyttsx.tts(str(col[i][0])+": "+str(m[0][i])   
          para(m)
    print()

def voiceindistrict():
    speechoutpyttsx.tts("\nWhich District do you want? : ")
    k=speechinput.voicein()
    speechoutpyttsx.tts("you gave input "+str(k)+"\n confirm or no\n")
    yn=speechinput.voicein()
    while ((('confirm' not in yn.lower()) and ('yes' not in yn.lower())) or (('no' in yn.lower()) or ('not' in yn.lower()))):
        speechoutpyttsx.tts("Which District do you want? : ")
        k=speechinput.voicein()
        speechoutpyttsx.tts("you gave input "+str(k)+"\nconfirm or no\n")
        yn=speechinput.voicein()
    print()
    fetch(k)
    print()
    # return k

cursor.execute(""" SELECT column_name FROM information_schema.columns 
    WHERE table_name = 'DistrictWeather' """)
col=cursor.fetchall()
#fetch column name

voiceindistrict()
speechoutpyttsx.tts("Do you want to continue(say confirm): ")
i=speechinput.voicein()
while ((('confirm' in i.lower()) or ('yes' in i.lower())) and (('no' not in i.lower()) and ('not' not in i.lower()))):
        voiceindistrict()
        speechoutpyttsx.tts("Do you want to continue(say confirm): ")
        i=speechinput.voicein()
        print()
print()
speechoutpyttsx.tts("THANKS FOR COMING")
con.commit()
cursor.close()
con.close()
