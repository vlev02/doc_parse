# -*- coding: utf-8 -*-
"""
动作序列提取GUI
"""
import tkinter as tk
import os
from functools import reduce


class SingleItemFrame(tk.Frame):
    """一个句子的单选操作面板"""
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.words = []
        self.items = tk.Frame(self)  # 词语界面
        self.var = None
        
    def set_arg(self, var, start):
        self.var, self.start = var, start
        
    def words_feed(self, words):
        self.words = words
        
    def show(self, ind):
        self.words_pack(ind)
        self.pack(padx=10, side=tk.LEFT)
        
    def words_pack(self, ind):
        for value, word in enumerate(self.words):
            tk.Radiobutton(self.items, text=word, variable=self.var,
                value=self.start+value).pack(anchor=tk.W)
        self.items.pack()

class MutilItemFrame(tk.Frame):
    """一个句子的多选操作面板"""
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.words = []
        self.vars = []
        self.items = tk.Frame(self)  # 词语界面
        
    def words_feed(self, words):
        self.words = words
        self.vars = [tk.IntVar() for _ in self.words]
        
    def show(self):
        self.words_pack()
        self.pack(padx=10, side=tk.LEFT)
        
    def words_pack(self):
        for var, word in zip(self.vars, self.words):
            b = tk.Checkbutton(self.items, text=word, variable=var)
            b.pack(anchor=tk.W)
        self.items.pack()
        

class ExtractFrame(tk.Frame):
    """动作提取的操作面板"""
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.words = []
        self.select_f = tk.Frame(self)
        self.button_f = tk.Frame(self)
        self.max_row = 20
        self.act_f = []
        self.objs_f = []
        self.series = None
        
    def sentence_feed(self, words):
        self.words = words
        
        start = 0
        self.act_ind = tk.IntVar()
        for start in  range(0, len(self.words), self.max_row):
            self.act_f.append(SingleItemFrame(self.select_f))  # 动作界面
            self.objs_f.append(MutilItemFrame(self.select_f))  # 对象界面
            self.act_f[-1].words_feed(self.words[start:start+self.max_row])
            self.act_f[-1].set_arg(self.act_ind, start)
            self.objs_f[-1].words_feed(self.words[start:start+self.max_row])
        
    def button_pack(self):
        tk.Button(self.button_f, text = 'Action1', command = lambda t=1:self.b_append_fun(t)).pack(side = tk.LEFT, padx=5, pady=5)
        tk.Button(self.button_f, text = 'Action2', command = lambda t=2:self.b_append_fun(t)).pack(side = tk.LEFT, padx=5, pady=5)
        tk.Button(self.button_f, text = 'Action3', command = lambda t=3:self.b_append_fun(t)).pack(side = tk.LEFT, padx=5, pady=5)
    
    def b_append_fun(self, act_type):
        act_ind = self.act_ind.get()
        objs_ind = reduce(list.__add__, [[var.get() for var in obj.vars] for obj in self.objs_f])
        objs_ind = [i for i, var in enumerate(objs_ind) if var]
        [[var.set(0) for var in obj.vars] for obj in self.objs_f]
        self.series.append([act_ind, act_type, objs_ind])
        print(self.series[-1])
        pass

    # def b_next_fun(self):
        # super().quit()
        
    def show(self):
        [[act.show(ind), objs.show()] for ind, (act, objs) in enumerate(zip(self.act_f, self.objs_f))]
        self.button_pack()
        self.select_f.pack()
        self.button_f.pack()
        self.pack()
        tk.mainloop()

if __name__ == "__main__":
    ef = ExtractFrame()
    sentence = "Python is all about automating repetitive tasks, leaving more time for your other SEO efforts."
    ef.sentence_feed(sentence)
    ef.show()
    
    

















