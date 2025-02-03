import tkinter as tk

class IncrementalGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Incremental Game")
        
        self.number = 0
        self.label = tk.Label(root, text=str(self.number), font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)
        
        self.root.bind("<Button-1>", self.increment_number)
    
    def increment_number(self, event):
        self.number += 1
        self.label.config(text=str(self.number))

if __name__ == "__main__":
    root = tk.Tk()
    app = IncrementalGame(root)
    root.mainloop()
