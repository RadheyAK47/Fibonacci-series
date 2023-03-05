from tkinter import *
root=Tk()

root.title("fibonacci series")
root.geometry("400x400")

label_series=Label(root,text="fibonacci series: ")

def fibonacci():
    num=50
    first_num=0
    second_num=1
    sum=0
    counter=1
    while(counter<=num):
        label_series["text"]+=str(sum)+"  "
        counter=counter+1
        first_num=second_num
        second_num=sum
        sum=first_num+second_num
        
btn=Button(root,text="fibonacci series",command=fibonacci)
btn.pack()
label_series.pack()
root.mainloop()

#fibonacci series = 0 1 1 2 3 5 8 13 21 34 55 89 144