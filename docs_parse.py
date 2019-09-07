# -*- coding: utf-8 -*-
"""
文档句子的解析和标注
"""
import os
from act_series_extract_2 import ExtractFrame


# root_dir = os.path.dirname(os.path.realpath(__file__))
# os.chdir(root_dir)


class DocsParse():
    def __init__(self,doc_file, dest_file=None):
        assert os.path.isfile(doc_file), f"目标文档<{doc_file}>不存在！！！"
        self.doc_file = doc_file
        self.dest_file = dest_file if dest_file else doc_file[:-4]+"_parse"+doc_file[-4:]
    
    def doc_load(self):
        with open(self.doc_file, encoding="utf-8") as doc_f:
            self.docs = doc_f.readlines()
    
    def action_extract(self):
        dp.doc_load()
        i_start = 0
        
        # warm start
        if os.path.isfile(self.dest_file):
            with open(self.dest_file, encoding="utf-8") as f:
                series = f.readlines()
            for line in series[::-1]:
                if line.startswith('Sentence: '):
                    try:
                        i_start = int(line.strip().split()[1]) + 1
                    except:
                        pass
                    finally:
                        break
            
        for ind in range(i_start, len(self.docs)):
            sentence = self.docs[ind].strip()
            words = sentence.split()
            print("Sentence:", ind)
            
            series = []
            ef = ExtractFrame()
            ef.series = series
            ef.sentence_feed(words)
            ef.show()
            
            self.series_save(ind, words, series)
        
        print(f"<{self.doc_file}>[{len(self.docs)}] parsed!")
        print(f"Infos are saved in <{self.dest_file}>!")
            
    def series_save(self, ind, words, series):
        with open(self.dest_file, 'a', encoding="utf-8") as dest_f:
            print(f"Sentence: {ind}", file=dest_f)
            print('Words:', words, file=dest_f)
            for action in series:
                print('action:', action, file=dest_f)
    
    
if __name__ == "__main__":
    doc_file = r"D:\FILE\Tencent\scooby_doo.txt"
    dp = DocsParse(doc_file)
    dp.action_extract()