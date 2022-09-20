#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Shaiykirra Jones
# DATE CREATED: 13/09/2022                                 
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()
    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    
    def get_input_args():
       # Creates parse 
        parser = argparse.ArgumentParser()

        # Creates 3 command line arguments args.dir for path to images files,
        # args.arch which CNN model to use for classification, args.labels path to
        # text file with names of dogs.
        parser.add_argument('--dir', type=str, default='pet_images/', 
                            help='path to folder of images')
        # TODO: 1a. EDIT parse.add_argument statements BELOW to add type & help for:
        #          --arch - the CNN model architecture
        #          --dogfile - text file of names of dog breeds
        parser.add_argument('--arch', type=str, default = 'vgg',
                            help= 'CNN Model Architecture')
        parser.add_argument('--dogfile', type=str, default = 'dognames.txt', 
                            help= 'Text File with Dog Names')

        # TODO: 1b. Replace None with parser.parse_args() parsed argument 
        # collection that you created with this function 
        return parser.parse_args()

        in_arg = get_input_args()

        # Function that checks command line arguments using in_arg  
        check_command_line_arguments(in_arg)


        # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
        # Once the get_pet_labels function has been defined replace 'None' 
        # in the function call with in_arg.dir  Once you have done the replacements
        # your function call should look like this: 
        #             get_pet_labels(in_arg.dir)
        # This function creates the results dictionary that contains the results, 
        # this dictionary is returned from the function call as the variable results
    #results = get_pet_labels(None)
    
def get_pet_labels(image_dir):
    
        #results = []
    
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0]) 
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if in_files[idx][0] != ".":

            # Creates temporary label variable to hold pet label name extracted 
            image_name = in_files[idx].split("_")
          
            pet_label = ""

        # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
        #          filename in the in_files list to extract the dog breed 
        #          name from the filename. Recall that each filename can be
        #          accessed by in_files[idx]. Be certain to place the 
        #          extracted dog breed name in the variable pet_label 
        #          that's created as an empty string ABOVE
            for word in image_name:         
        # Sets string to lower case letters
                if word.isalpha():
                    pet_label += word.lower() + " "

        # Splits lower case string by _ to break into words 
        
        
        # Strip off starting/trailing whitespace characters 
            pet_label = pet_label.strip()
        
        # Prints resulting pet_name
            print("\nFilename=", in_files[idx], "   Label=", pet_label)

        # If filename doesn't already exist in dictionary add it and it's
        # pet label - otherwise print an error message because indicates 
        # duplicate files (filenames)
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
              
            else:
                print("** Warning: Duplicate files exist in directory:", 
                    in_files[idx])
 
    # TODO 2b. Replace None with the results_dic dictionary that you created
    # with this function
    return results_dic

    #results = get_pet_labels(image_dir)

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)


    # TODO 3: Define classify_images function within the file classiy_images.py
    # Once the classify_images function has been defined replace first 'None' 
    # in the function call with in_arg.dir and replace the last 'None' in the
    # function call with in_arg.arch  Once you have done the replacements your
    # function call should look like this: 
    #             classify_images(in_arg.dir, results, in_arg.arch)
    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and adds these results to the results dictionary - results
def classify_images(images_dir, results_dic, model):
    
        
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
       # TODO: 3a. Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
        model_label = classifier(images_dir+key, model)

       # TODO: 3b. BELOW REPLACE pass with CODE to process the model_label to 
       #           convert all characters within model_label to lowercase 
       #           letters and then remove whitespace characters from the ends
       #           of model_label. Be certain the resulting processed string 
       #           is named model_label.
       #
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
        model_label = model_label.lower().strip()
              
       # defines truth as pet image label 
        truth = results_dic[key][0]

       # TODO: 3c. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           1 (where the value of 1 indicates a match between pet image 
       #           label and the classifier label) to the results_dic dictionary
       #           for the key indicated by the variable key 
       #
       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match(1) using extend list function
        if truth in model_label:
            results_dic[key].extend((model_label, 1))

       # TODO: 3d. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           0 (where the value of 0 indicates NOT a match between the pet 
       #           image label and the classifier label) to the results_dic 
       #           dictionary for the key indicated by the variable key
       #                   
       # if not found then added to results dictionary as NOT a match(0) using
       # the extend function 
        else:
            results_dic[key].extend((model_label, 0))

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    
    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    # Once the adjust_results4_isadog function has been defined replace 'None' 
    # in the function call with in_arg.dogfile  Once you have done the 
    # replacements your function call should look like this: 
    #          adjust_results4_isadog(results, in_arg.dogfile)
    # Adjusts the results dictionary to determine if classifier correctly 
    # classified images as 'a dog' or 'not a dog'. This demonstrates if 
    # model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, None)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)


    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages). This
    # dictionary is returned from the function call as the variable results_stats    
    # Calculates results of run and puts statistics in the Results Statistics
    # Dictionary - called results_stats
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)


    # TODO 6: Define print_results function within the file print_results.py
    # Once the print_results function has been defined replace 'None' 
    # in the function call with in_arg.arch  Once you have done the 
    # replacements your function call should look like this: 
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, None, True, True)
    
    # TODO 0: Measure total program runtime by collecting end time
    end_time = time()
    
    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    #calculate difference between end time and start time
    total_time = start_time() - end_time()
    
    print("\n** Total Elapsed Runtime:",
          str(int((total_time/3600)))+":"+str(int((total_time%3600)/60))+":"
          +str(int((total_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
