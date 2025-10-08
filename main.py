import tkinter as tk
from tkinter import ttk

def caliculate(input_H,input_W,kernel_H,kernel_W,stride,padding):
   output_H=(input_H+2*padding-kernel_H)//stride+1
   output_W=(input_W+2*padding-kernel_W)//stride+1
   return output_H,output_W
class Layer:
    def __init__(self,master,layer_index):
        self.frame=ttk.Frame(master,padding=5)
        self.frame.grid(column=0,sticky="w")
        ttk.Label(self.frame,text=f"{layer_index+1}層").grid(row=0,column=0)
        ttk.Label(self.frame,text="カーネルH").grid(row=0,column=1)
        ttk.Label(self.frame,text="カーネルW").grid(row=0,column=2)
        ttk.Label(self.frame,text="ストライド").grid(row=0,column=3)
        ttk.Label(self.frame,text="パディング").grid(row=0,column=4)

        self.kernelH_entry=ttk.Entry(self.frame,width=5)
        self.kernelW_entry=ttk.Entry(self.frame,width=5)
        self.stride_entry=ttk.Entry(self.frame,width=5)
        self.padding_entry=ttk.Entry(self.frame,width=5)
        self.padding_entry.insert(0,"0")

        self.kernelH_entry.grid(row=1,column=1)
        self.kernelW_entry.grid(row=1,column=2)
        self.stride_entry.grid(row=1,column=3)
        self.padding_entry.grid(row=1,column=4)

    def value(self):
        try:
            kernelH_val=int(self.kernelH_entry.get())
            kernelW_val=int(self.kernelW_entry.get())
            stride_val=int(self.stride_entry.get())
            padding_val=int(self.padding_entry.get())

            return kernelH_val, kernelW_val,stride_val,padding_val
        
        except :
            pass

class CNN_caliculate:
    def __init__(self,root):
        self.root=root
        root.geometry("400x800")
        self.root.title("CNN計算機")
      

        self.layers=[]
        self.layer_frame=ttk.Frame(root)
        self.layer_frame.pack()

        input_frame=ttk.Frame(root)
        input_frame.pack()
        ttk.Label(input_frame,text="入力のサイズ   (Height×Width)").grid(row=0,column=0,columnspan=2)
        self.input_entry1=ttk.Entry(input_frame,width=8)
        self.input_entry1.insert(0,"")
        self.input_entry1.grid(row=1,column=0,padx=0)

        self.input_entry2=ttk.Entry(input_frame,width=8)
        self.input_entry2.insert(0,"")
        self.input_entry2.grid(row=1,column=1,padx=0)

        button_frame=ttk.Frame(root)
        button_frame.pack()
        ttk.Button(button_frame,text="層を追加",command=self.add_layer).pack(side="left")
        ttk.Button(button_frame,text="計算",command=self.caliculate).pack(side="left")

        self.result=ttk.Label(root,text="結果")
        self.result.pack()
        layer=Layer(self.layer_frame,len(self.layers))
        self.layers.append(layer)

        
    
    def add_layer(self):
        layer=Layer(self.layer_frame,len(self.layers))
        self.layers.append(layer)

    def caliculate(self):
        input_H=int(self.input_entry1.get())
        input_W=int(self.input_entry2.get())
        output_H=input_H
        output_W=input_W
        result_text=f"入力:     {input_H}×{input_W}\n"

        for i,layer in enumerate(self.layers):
            kernel_H,kernel_W,stride,padding=layer.value()
            output_H,output_W=caliculate(output_H,output_W,kernel_H,kernel_W,stride,padding)
            result_text+=f"{i+1}層目:     出力={output_H}×{output_W}\n"
        
        self.result.config(text=result_text)





root=tk.Tk()
app=CNN_caliculate(root)


root.mainloop()