# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
df=pd.read_excel('test.xlsx')

#%%
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# %%
while True:
    try:
        a=input()
        if a=='del':
            df.drop(df.index[-1],inplace=True)
            speaker.Speak('上一行已删除')
            continue
        elif a=='exit':
            break
        a=a[:4]+'/'+a[4:6]+'/'+a[6:]
        b=float(input())
        c=float(input())
        speaker.Speak(a+'收入'+str(b)+'支出'+str(c))
        s=pd.Series([a,b,c],index=df.columns)
        df=df.append(s,ignore_index=True)
    except (Exception) as wrong:
        print(wrong)
        df.to_excel('test1.xlsx')
df.to_excel('test1.xlsx')
