# -*- coding: ISO-8859-1 -*-
class Anagrams:

    def getListFromFile(self,file_name):
        file = open(file_name,encoding='ISO-8859-1')
        return_list = file.read().splitlines()
        file.close()
        return return_list

    def getDicSorted(self,list_file):
        dic_return = {}
        for word in list_file:
            sorted_word = ''.join(sorted(list(word)))
            if sorted_word not in dic_return:
                dic_return[sorted_word] = []
            dic_return[sorted_word].append(word)
        return dic_return

    def isAnagram(self,word,dic):
        sorted_word = ''.join(sorted(list(word)))
        if len(dic[sorted_word]) > 1:
            return True
        return False

    def getAnagramFromDicList(self,list_words,dic_sorted):
        return_list = []

        for word in list_words:
            sorted_word = ''.join(sorted(list(word)))
            if self.isAnagram(word,dic_sorted) and dic_sorted[sorted_word] not in return_list:
                return_list.append(dic_sorted[sorted_word])

        return return_list

    def getAnagrams(self,file_name):
        list_file = self.getListFromFile(file_name)
        dic_sorted = self.getDicSorted(list_file)
        return_list = self.getAnagramFromDicList(list_file,dic_sorted)
        return return_list