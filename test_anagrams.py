# -*- coding: ISO-8859-1 -*-
import unittest
from anagrams import Anagrams

class TestAnagrams(unittest.TestCase):

    def setUp(self):
        self.anagram =  Anagrams()

    #list_from_file
    def test_get_list_from_file(self):
        self.assertEqual(['hola','python',
                          'azul', 'maiz',
                          'laho','thonpy',
                          'noythp'],self.anagram.getListFromFile('test_list_anagrams.txt'))
    #list_from_file
    def test_get_list_from_file_in_blank(self):
        self.assertEqual([],self.anagram.getListFromFile('test_list_blank.txt'))

    #count words of wordlist.txt
    def test_get_list_from_file_wordlist_all_list(self):
        self.assertEqual(338882,len(self.anagram.getListFromFile('wordlist.txt')))

    # not found_field
    def test_get_list_from_file_not_found_field(self):
        self.assertRaises(FileNotFoundError, self.anagram.getListFromFile,'notfield')


    def test_get_dic_sorted(self):
        self.assertEqual({'ahlo':['hola','laoh'],
                          'hnopty': ['python']},self.anagram.getDicSorted(['hola','laoh','python']))

    #get dic_blank
    def test_get_dic_sorted_blank(self):
        self.assertEqual({},self.anagram.getDicSorted([]))

    #get dic_blank
    def test_get_dic_sorted_kata(self):
        self.assertEqual({''.join(sorted(list('kata'))):['kata']},self.anagram.getDicSorted(['kata']))


    #is anagram true
    def test_is_anagram_true(self):
        self.assertTrue(self.anagram.isAnagram('hola',{'ahlo':['hola','laoh'],'hnopty': ['python']}))

    # is anagram False
    def test_is_anagram_true(self):
        self.assertFalse(self.anagram.isAnagram('python', {'ahlo': ['hola', 'laoh'], 'hnopty': ['python']}))

    # get anagrams from dic
    def test_get_anagram_from_dic(self):
        list_words = ['hola','laoh', 'python']
        dic_sorted = {'ahlo': ['hola', 'laoh'], 'hnopty': ['python']}
        self.assertEqual([['hola','laoh']],self.anagram.getAnagramFromDicList(list_words,dic_sorted))

    # get anagrams from dic blank
    def test_get_anagram_from_dic_blank(self):
        list_words = ['hola', 'python']
        dic_sorted = {'ahlo': ['hola'], 'hnopty': ['python']}
        self.assertEqual([],self.anagram.getAnagramFromDicList(list_words,dic_sorted))

    #get anagrams
    def test_get_anagrams(self):
        self.assertEqual([['hola','laho'],['python','thonpy','noythp']],self.anagram.getAnagrams('test_list_anagrams.txt'))

    #get anagrams blanks
    def test_get_anagrams_blank(self):
        self.assertEqual([],self.anagram.getAnagrams('test_list_blank.txt'))

    #get not found document
    def test_get_anagrams_not_field(self):
        self.assertRaises(FileNotFoundError, self.anagram.getListFromFile,'notfield')

    def test_get_anagrams_count_of_field_wordlist(self):
        self.assertEqual(20683,len(self.anagram.getAnagrams('wordlist.txt')))


















































