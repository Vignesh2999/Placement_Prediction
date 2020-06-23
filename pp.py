#Final 2
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
  # number of observations/points 
  n = np.size(x) 

  # mean of x and y vector 
  m_x, m_y = np.mean(x), np.mean(y) 

  # calculating cross-deviation and deviation about x 
  SS_xy = np.sum(y*x) - n*m_y*m_x 
  SS_xx = np.sum(x*x) - n*m_x*m_x 

  # calculating regression coefficients 
  b_1 = SS_xy / SS_xx 
  b_0 = m_y - b_1*m_x 

  return(b_0, b_1) 

def plot_regression_line(x, y, b,x1=0,y1=0): 
  # plotting the actual points as scatter plot 
  plt.scatter(x, y, color = "c",marker = "o", s = 30) 
  plt.scatter(x1,y1, color = "r",marker = "X", s = 30) 
  
  # predicted response vector 
  y_pred = b[0] + b[1]*x 

  # plotting the regression line 
  #plt.ylim(0.5,1.5)
 # plt.ylim(0,3)
  plt.plot(x, y_pred, color = "g") 

  # putting labels 
  plt.xlabel('SCORE') 
  plt.ylabel('NO. OF COMPANIES PLACED') 
  plt.grid(True)

  # function to show plot 
  plt.show() 

#MAIN
#f = pd.read_csv("https://raw.githubusercontent.com/wunderkinduo/aimini/master/Book3.csv",encoding = "ISO-8859-1")
Test = pd.read_csv("https://raw.githubusercontent.com/wunderkinduo/aimini/master/2015.csv",encoding = "ISO-8859-1")
#f = pd.read_csv("https://raw.githubusercontent.com/wunderkinduo/aimini/master/abcd.csv")
f = pd.read_csv("https://raw.githubusercontent.com/wunderkinduo/aimini/master/2015%20-%202019%20(RMK%20GROUP)%20(1).csv")

l=min([len(f["UG Degree % or CGPA (uptolast semester for which results announced)"]),len(f["12th %"]),len(f["12th %"]),len(f["Company"])])

#Data Cleaning
less=0
droplist=[]
for i in range(len(f["UG Degree % or CGPA (uptolast semester for which results announced)"])):
  if(f["UG Degree % or CGPA (uptolast semester for which results announced)"][i]>10 ):   #or f["Standing Arrears"][i]>2
    droplist.append(i)

f=f.drop(droplist)
f=f.reset_index(drop=True)

l=min([len(f["UG Degree % or CGPA (uptolast semester for which results announced)"]),len(f["12th %"]),len(f["12th %"]),len(f["Company"])])
score=[]
placed=[]

cgpa=6
hsc=1.5
ssl=1.5
dip=1.5
med=1
for i in range(l):
  # if(i in droplist):
  #   continue
  t=0
  if(  not(pd.isnull(f["Company"][i])) and (f["Company"][i]!=" " and f["Company"][i]!="#N/A") ):
    t+=1
#   if( not(pd.isnull(f["Placed Company2"][i]))):
#     t+=1
#   if( not(pd.isnull(f["Placed Company3"][i]))):
#     t+=1
  m=0
  if(not(pd.isnull(f["12th %"][i]))):
    m+=hsc*f["12th %"][i]
  if(not(pd.isnull(f["Diploma  %"][i])) and f["Diploma  %"][i]!="NA" ):
    m+=dip*f["Diploma  %"][i]
    
  if( not(pd.isnull(f["12th %"][i]))):
    m+=ssl*f["12th %"][i]
    
  if(not(pd.isnull(f["UG Degree % or CGPA (uptolast semester for which results announced)"][i]))):
    m+=cgpa*f["UG Degree % or CGPA (uptolast semester for which results announced)"][i]
    
  if( not(pd.isnull(f["12th Medium (Tamil/English/Telugu/Others)"][i]))  and (f["12th Medium (Tamil/English/Telugu/Others)"][i]=="ENGLISH" or f["12th Medium (Tamil/English/Telugu/Others)"][i]==" english" or f["12th Medium (Tamil/English/Telugu/Others)"][i]=="english")):
    m+=med*1
  m/=10
  m=int(round(m,2))
  score.append(m)
  placed.append(int(t))

f["score"]=score
f["Placed"]=placed
x=f["score"]
y=placed

# estimating coefficients 
b = estimate_coef(x, y) 
#print("Estimated coefficients:\nb_0 = {} \\nb_1 = {}".format(b[0], b[1])) 

# plotting regression line 
plot_regression_line(x, y, b) 

m=b[1] 
    
    


#Getting input
while(1):
  print("Enter Any Value as 0 to stop")
  #CGPA
  arrear=float(input("Enter No.of Standing Arrear"))
  if(arrear>2):
    print("You are not eligible for Placement")
    continue
    
  t1=float(input("Enter Your CGPA : "))  
  if(t1==0):
    print("Bye")
    break
  elif(t1<0):
    print("CGPA Cannot be Negative")
    continue
  elif(t1>10):
    print("CGPA Cannot be greater than 10")
    continue
  d=input("Are you an Diploma Graduate ? Enter y/n :")
  if(d=="y" or d=="Y"):
    t2=float(input("Enter Your Diploma Percentage : "))
    if(t2==0):
      print("Bye")
      break
    elif(t2<0):
      print("Diploma Percent Cannot be Negative")
      continue
    elif(t2>100):
      print("Diploma Percent Cannot be greater than 100")
      continue
    
  elif(d=="n" or d=="N"):  
    #12th Mark 
    t2=float(input("Enter Your 12th Percentage : "))
    if(t2==0):
      print("Bye")
      break
    elif(t2<0):
      print("12th Percent Cannot be Negative")
      continue
    elif(t2>100):
      print("12th Percent Cannot be greater than 100")
      continue      
  else:
    print("Enter y/n")
    continue
  #10th Mark
  t3=float(input("Enter Your 10th Percentage : "))
  if(t3==0):
    print("Bye")
    break
  elif(t3<0):
    print("10th Percent Cannot be Negative")
    continue
  elif(t3>100):
    print("10th Percent Cannot be greater than 100")
    continue
  x1=cgpa*t1+hsc*t2+ssl*t3
    
  
  x1/=10
  x1=int(round(x1,2))
  y1=round(m*x1,5)*0.632959465275843
  
  plot_regression_line(x, y, b,x1,y1) 
  print("X1 ",x1)
  print("Your Probability of getting placed is",y1*100," Percentage")  #*0.8038462435
  ran=int(input("Enter 1 to calculate range or 0 to not"))
  
  if(ran):
    a=float(input("Enter Intial Range"))
    b=float(input("Enter Final Range"))

    #Students list
    placeCount=0
    dt=Test[Test["UG Degree % or CGPA (uptolast semester for which results announced)"].between(a,b)]
    dt=dt.reset_index(drop=True)

    #print(type(dt))
    #print("CGPA",dt["UG Degree % or CGPA (uptolast semester for which results announced)"],"10th",dt["12th %"],"12th",dt["12th %"])
    for i in range(len(dt)):
      #print(dt["12th %"][i])
      T1=dt["UG Degree % or CGPA (uptolast semester for which results announced)"][i]
      T2=dt["12th %"][i]
      T3=dt["12th %"][i]
      x1=cgpa*T1+ssl*T2+hsc*T3
      x1/=11.2
      x1=int(round(x1,2))
      y1=round(m*x1,5)*0.632959465275843

      if(y1>0.5):
        placeCount+=1
    print("Count : ",placeCount)



#Final 2