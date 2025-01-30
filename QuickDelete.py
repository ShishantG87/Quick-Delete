import os
import tkinter as tk
from PIL import Image, ImageTk

class GUI: # implementation of gui
    def main(self):
        self.root = tk.Tk()
        self.root.title("QuickDelete")
        self.root.geometry("400x300")
        self.background("SAE.jpg")
        self.Temp_button()
        self.PreFetch_button()
        self.root.mainloop()
    
    def background(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        
        background_label = tk.Label(self.root, image = photo)
        background_label.place(relheight=1, relwidth=1)
        
        background_label.image = photo
        
        
        
        
        
        
        
        
        
        
        
    def Temp_button(self):
        self.button = tk.Button(self.root, text = "Delete Temp Files", command = lambda : self.delete_temp_files(r'C:\Windows\Temp'))
        self.button.place(relx=0.5, rely=0.4, anchor="center")
    def PreFetch_button(self):
        self.sec_button = tk.Button(self.root, text = "Delete Prefetch Files", command = lambda : self.delete_preFetch_files(r'C:\Windows\Prefetch') )
        self.sec_button.place(relx=0.5, rely=0.5, anchor="center")
        
        
        
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
            
        

            
            
    
    
if __name__ == '__main__':
    kk = GUI()
    kk.main()

    

        