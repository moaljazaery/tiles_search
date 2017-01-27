from config import Config
from utils import Utils

out_file=open(Config.preprocessed_dictionary_path,"w")
dic_file=open(Config.dictionary_path)
words=dic_file.readlines()
for word in words:
    word=word.replace("\n","")
    if word!="" and len(word) <= Config.tiles_length:
        out_word= "".join(Utils.sort_word(word))
        out_file.write(word+","+out_word+"\n")


