# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from utils import *

def createLabel(frame, label_text, entry_var=None, position={}):
    label = ttk.Label(frame, text=label_text, textvariable=entry_var, font=NORMAL_FONT)
    if(entry_var):
        entry_var.set(label_text)
    label.grid(row=position['row'], column=position['col'], padx=5, pady=5, stick='w')

    return label

def createEntry(frame, entry_var, default_entry='', position={}):
    entry = ttk.Entry(frame, textvariable=entry_var)
    entry.insert(-1, default_entry)  
    entry.grid(row=position['row'], column=position['col'], padx=5, pady=5, stick='w')
    
    return entry

def createComboBox(frame, combo_var, combo_list=[], default_entry='', position={}):
    combo = ttk.Combobox(frame, textvariable=combo_var, values=combo_list)
    combo.insert(-1, default_entry)
    combo.grid(row=position['row'], column=position['col'], padx=5, pady=5, stick='w')
    
    return combo

class MainFrame(tk.Frame):    
        
    def __init__(self, master=None):
        super().__init__(master)
        computador = {
            "escola" : tk.StringVar(), 
            "local" : tk.StringVar(),
            "tipo": tk.StringVar(), 
            "marca": tk.StringVar(),
            "modelo": tk.StringVar(),
            "numero_serie": tk.StringVar(),
            "numero_inventario": tk.StringVar(),            
            "funciona": tk.StringVar(),
            "sistema operacional": " ",  
            "processador": " ", 
            "ram": " ", 
            "hostname": " ",
            "ip": " ",  
            "mac address": " ",             
        }
        self.master = master
        self.pack()
        self.data = computador
        self.create_widgets()      
    
    def sendInfo(self):
        pc = {
            "escola": self.data['escola'].get(),
            "local": LOCALS_LIST.index(self.data['local'].get())+1,
            "tipo": TYPE_LIST.index(self.data['tipo'].get())+1,
            "marca": self.data['marca'].get(),
            "modelo": self.data['modelo'].get(),
            "numero_serie": self.data['numero_serie'].get(),
            "numero_inventario": self.data['numero_inventario'].get(),
            "sistema_operacional": self.data['sistema operacional'],
            "funciona": self.data['funciona'].get(),
            "cpu_freq": self.data['processador'],
            "ram": self.data['ram'],
            "hostname": self.data['hostname'],
            "ip": self.data['ip'],
            "mac_address": self.data['mac address'],            
        }
        
        response = addSystemInfo(pc)
                
        messagebox.showinfo("Resposta", response.text)

    def create_widgets(self):             
        pc_info = getSystemInfo()       
        self.data['sistema operacional']  = pc_info['sistema_operacional']
        self.data['processador'] = pc_info['processador']
        self.data['ram'] = pc_info['ram']
        self.data['hostname'] = pc_info['hostname']
        self.data['ip']  = pc_info['ip']
        self.data['mac address']  = pc_info['mac_address']
        combo_itens = ['local', 'tipo', 'funciona']
        label_itens = ['sistema operacional','processador', 'ram', 'hostname', 'ip', 'mac address']
        combo_lists = {
            'local': LOCALS_LIST,
            'tipo': TYPE_LIST,
            'funciona': STATUS_LIST
        }
        i=1
        
        head_frame=tk.Frame()      
        label = ttk.Label(head_frame, text="Informações do Dipositivo:", font=LARGE_FONT)
        label.pack(padx=10, pady=10)        
        head_frame.pack(anchor='n')
        
        
        middle_frame = tk.Frame()
        for key in self.data.keys():
            if( key in combo_itens ):                
                createLabel(middle_frame, key.capitalize(), position={'row':i, 'col':0})
                createComboBox(middle_frame,  self.data[key], combo_list=combo_lists[key], default_entry=combo_lists[key][0], position={'row':i, 'col':2})
            elif( key in label_itens):
                createLabel(middle_frame, key.capitalize(), position={'row':i, 'col':0})
                createLabel(middle_frame, self.data[key], position={'row':i, 'col':2})
            else:
                createLabel(middle_frame, key.capitalize(), position={'row':i, 'col':0})
                createEntry(middle_frame, self.data[key], position={'row':i, 'col':2})               

            i+=1
        middle_frame.pack(anchor='center')
           
                

        bottom_frame = tk.Frame()
        self.send_button = ttk.Button(bottom_frame, text= "Enviar", command = self.sendInfo)        
        self.send_button.pack(padx=50, pady=10)               
        self.send_button.pack(side='left')

        self.quit = ttk.Button(bottom_frame, text="Fechar", command = self.master.destroy)        
        self.quit.pack(padx=100, pady=10)
        self.quit.pack(side='right')
        bottom_frame.pack(anchor='s')
       
    
root = tk.Tk()
root.title('ratPAd Asset Management 0.1.0b')
root.maxsize(600, 800)
app = MainFrame(master=root)
app.mainloop()
