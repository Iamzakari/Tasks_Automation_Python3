#!/usr/bin/env python3


import os
import requests
import json



def process_text_to_dictionary(path):
    '''THis function take a given director process a text files and return a dictionary'''
    file_list = os.listdir(path)
    #make sure that the path is not a directory
    only_file = [dir for dir  in file_list if os.path.isfile(dir)]
    keys = ["title", "name", "date", "feedback"]
    for file in only_file:
        keys_index = 0
        feedbacks = {}
        with open(path + file, "r") as file_read:
            for line in file_read:
                value = line.strip()
                feedbacks[keys[keys_index]] = value
                keys_index += 1
        return feedbacks

def upload_to_webservice(d,url):
    response = requests.post(url, json=d)
    if not response.ok:
        raise Exception("GET failed with status code {}".format(response.status_code))
    print(response.request.body)
    print(response.status_code)
    print(response.ok)




def main():
    filePath = "/data/feedback/"
    result_dict = process_text_to_dictionary(filePath)
    urls = "http://34.122.49.144/feedback"
    upload_to_webservice(result_dict, urls)

if __name__ == "__main__":
    main()
