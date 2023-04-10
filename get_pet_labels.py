#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nick Ferguson
# DATE CREATED: 2/6/23                      
# REVISED DATE: 2/26/23
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create a list with image file names
    in_files = listdir(image_dir)
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
    
    # Create empty dictionary for the results (pet labels, etc.)
    results_dic = {}
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in in_files[0:len(in_files):1]:
        
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if filename[0] != ".":
            
            # Uses split to extract words of filename into list image_name
            image_name = filename.split("_")
            
             
            pet_label = " ".join([word.lower() for word in image_name if word.isalpha()])
            """
            Takes a list of words (image_name) and returns a string that contains only 
            the words that are all alphabetic characters (i.e., only letters). The words are converted 
            to lowercase and joined with spaces to form a single string (pet_label).

            Args:
            - image_name: a list of strings representing words in an image filename

            Returns:
            - A string representing the pet label for the image, which is a concatenation 
            of all the words in the image filename that consist only of alphabetic characters (i.e., 
            no numbers or special characters). The words are joined with spaces and converted to lowercase.
            """
                    
            # Strips off trailing whitespace
            pet_label = pet_label.strip()
            
            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates
            # duplicate files (filename)
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
                
            else:
                print("** Warning: Duplicate files exist in directory:",
                      filename)
  
    return results_dic
