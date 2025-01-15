import os
import tkinter as tk

class GUI: # implementation of gui
    def main(self):
        self.root = tk.Tk()
        self.root.title("QuickDelete")
        self.root.geometry("400x300")
        self.Temp_button()
        self.root.mainloop()
    
    def Temp_button(self):
        self.button = tk.Button(self.root, text = "Delete Temp Files", command = lambda : self.delete_temp_files(r'C:\Windows\Temp'))
        self.button.pack()
    
    def delete_temp_files(self,path_temp):  
        os.chdir(path_temp)   # change directory to the temp folder
        list_temp = os.listdir(path_temp)  #  use list to get all file and delete

        for file in list_temp: 
            try:
                file_path = os.path.join(path_temp, file) # join file directory with file name, and delete if possible same thing with other function, except it deletes prefetch files
                os.remove(file_path)
            except PermissionError:
                print('Cannot delete')
                continue
            
            print("file '% s' deleted" % file)

    def delete_preFetch_files(self,path_temp):
        os.chdir(path_temp)
        list_temp = os.listdir(path_temp)

        for file in list_temp:
            try:
                file_path = os.path.join(path_temp, file)
                os.remove(file_path)
            except PermissionError:
                print('Cannot delete')
                continue
            
            print("file '% s' deleted" % file)
            
        
def main():
    while True:
       
        choice = int(input('Delete Temp files for Prefetch?\n\t 1 for Temp\n\t 2 for Prefetch\nEnter Here: '))
        match choice:
            case 1:
                    delete_temp_files(r'C:\Windows\Temp')
            case 2:
                    delete_preFetch_files(r'C:\Windows\Prefetch')
            case _:
                print("invalid choice")
                continue
        False
                
            
            
    
    
if __name__ == '__main__':
    kk = GUI()
    kk.main()

    

        