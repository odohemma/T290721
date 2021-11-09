# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:35:53 2021

@author: USER
"""

import pywikibot
from pywikibot.data import api

# Connect to english wiki
en_wiki = pywikibot.Site('en', 'wikipedia')

# Then connect to wikidata
en_wiki_repo = en_wiki.data_repository()


def search_entities(site, itemtitle):
     params = { 'action' :'wbsearchentities', 
                'format' : 'json',
                'language' : 'en',
                'type' : 'item',
                'search': itemtitle}
     request = api.Request(site=site, parameters=params)
     return request.submit()
 
search_term = input("Type a term to be searched for in the appropriate capitalization: ")
 
wikidataEntries = search_entities(en_wiki_repo, search_term)
if wikidataEntries['search'] != []:
    results = wikidataEntries['search']
    numresults = len(results)
    returned_labels = []
    returned_aliases = []
    
    for i in range(0,numresults):
        returned_labels.append(results[i]['label'])
        if 'aliases' in results[i]:
            returned_aliases.append(results[i]['aliases'][0])    
        
    if search_term not in returned_labels and search_term not in returned_aliases:
        print ("There isn't an exact match, but see below for closely related matches:")
        for i in range(0,numresults):
            qid = results[i]['id']
            label = results[i]['label']
            print (qid + " - " + label)
            
    #The block of code below ensures that the QID of the search term as inputted 
    #is printed, if the search term matches the wikidata label.            
    elif search_term in returned_labels:    
        for i in range(0,numresults):
            if results[i]['label'] == search_term:
                qid = results[i]['id']
                label = results[i]['label']
                print ("Here is an exact match: " + qid + " - " + label)
    
    #The block of code below makes it possible to search for a wikidata item
    #using aliases. An example is Dassault Rafale.               
    elif search_term in returned_aliases:
        for i in range(0,numresults):
            if results[i]['aliases'][0] == search_term:
                qid = results[i]['id']
                aliases = results[i]['aliases'][0]
                print ("Here is an exact match: " + qid + " - " + aliases)

else:
    print ("The inputted term does not have a QID in Wikidata.")