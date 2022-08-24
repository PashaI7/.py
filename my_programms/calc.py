#from cProfile import label
from  tkinter import *   #графический интерфейс
from decimal import  *   # вычесление с большой точностью, float - не будет хватать
root = Tk()
root.title('Calculator')
buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
            )
activestr = ''
stack = []
#   !!! Вычисление результата   !!!
  
def calculate(): #функция сalculate получает из списка stack операнды и операцию, которую над ними надо сделать
    global stack
    global label #Результат будет отображаться в надписи label
    result = 0
    operand2 = Decimal(stack.pop()) #А получать результат будем с помощью  метода .pop() 
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))
    
#   !!! Обработка нажатия   !!!

def click(text): #click обрабатывает нажатые клавиши(прослушка). Это определяется с помощью текста, который написан на самой кнопке, которую нажали
    global activestr
    global stack
    if text == 'CE':
        stack.clear()
        activestr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activestr += text
        label.configure(text=activestr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activestr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                activestr = ''
                label.configure(text='0')
                
#   !!! Внешний вид   !!!

label = Label(root, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text = buttons[row][col],command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column = col, sticky="nsew")
        
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight = 1)
        
root.mainloop()
        
#Для того, чтобы кнопки правильно работали, пришлось для каждой из кнопок создать свою функцию с помощью lambda
#git
            
                    