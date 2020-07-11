#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现一个文本编辑器

@author: baoqiang
@time: 2020/7/10 9:22 下午
"""

import tkinter as tk
import tkinter.scrolledtext as tst
import tkinter.filedialog
import tkinter.colorchooser


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.textEdit = tst.ScrolledText(self, width=80, height=20)
        self.textEdit.grid(row=0, column=0, rowspan=6)

        self.btnOpen = tk.Button(self, text="Open", command=self.f_open)
        self.btnOpen.grid(row=1, column=1)

        self.btnSave = tk.Button(self, text="Save", command=self.f_save)
        self.btnSave.grid(row=2, column=1)

        self.btnSaveAs = tk.Button(self, text="SaveAs", command=self.f_save_as)
        self.btnSaveAs.grid(row=3, column=1)

        self.btnColor = tk.Button(self, text="Color", command=self.f_color)
        self.btnColor.grid(row=4, column=1)

        self.btnQuit = tk.Button(self, text="Quit", command=self.f_quit)
        self.btnQuit.grid(row=5, column=1)

    def f_open(self):
        self.textEdit.delete(1.0, tk.END)
        self.fname = tk.filedialog.askopenfilename(filetypes=[('文本文件', '.txt')])
        with open(self.fname, 'r') as f:
            str1 = f.read()
        self.textEdit.insert(0.0, str1)

    def f_save(self):
        str1 = self.textEdit.get(1.0, tk.END)
        with open(self.fname, 'w') as f:
            f.write(str1)

    def f_save_as(self):
        str1 = self.textEdit.get(1.0, tk.END)
        # fname = tk.filedialog.askopenfilename(filetypes=[('文本文件', '.txt')])
        fname = tk.filedialog.asksaveasfilename(filetypes=[('文本文件', '.txt')])
        with open(fname, 'w') as f:
            f.write(str1)

    def f_color(self):
        t, c = tk.colorchooser.askcolor(title='askcolor')
        self.textEdit.config(bg=c)

    def f_quit(self):
        root.destroy()


root = tk.Tk()


def run():
    """
    https://blog.csdn.net/apaking/article/details/45532381
    https://blog.csdn.net/tangwg5/article/details/77298136
    """
    root.title('Simple Text Editor')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    run()
