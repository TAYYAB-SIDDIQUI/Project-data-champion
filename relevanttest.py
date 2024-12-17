def relevant(filename):
    import pandas as pd
    df=pd.read_excel(filename)
    null_percentage=(df.isnull().sum())/len(df)*100
    for i,j in zip(null_percentage,df.columns):
        if i>15.0:
            df.drop(columns=[j],inplace=True)
    df.drop(columns=df.columns[0],inplace=True)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(inplace=True)
    relevent=[]
    for i in range(len(df)):
        if df["Category"][i]=="F&B":
            if df["Probiotics"][i]=="Yes" and df["Fortification"][i]=="Yes":
                relevent.append("Yes")
            else:
                relevent.append("No")
        elif df["Category"][i]=="Bulk (manufacturer)" or df["Category"][i]=="Bulk (distributor)":
            if df["Gut Health"][i]=="Yes" and df["Womens Health"][i]=="Yes" and df["Cognitive Health"][i]=="Yes":
                relevent.append("Yes")
            else:
                relevent.append("No")
    df["relvent"]=relevent
    df.to_excel("Task_2_view.xlsx")
relevant("Task 1 view.xlsx")