import sys
import os
from pdf2image import convert_from_path


def make_dir_for_results(pdf_path):
    #make new directory for results
    result_dir_name = os.path.basename(pdf_path)+"_result"
    os.mkdir(result_dir_name)
    print(result_dir_name)
    
    #change current working directory
    current_working_dir = os.getcwd()
    os.chdir(current_working_dir+result_dir_name)
    print(current_working_dir+result_dir_name)
    
    
    

def convert_to_images(pdf_path):
    #Load images from pdf
    images = convert_from_path(pdf_path,thread_count=8)
    
    #create result directory 
    
 
 
if __name__ =="__main__":
    if len(sys.argv) <2 :
        print("Usage:python convert_pdf_to_img.py <file1.pdf> <file2.pdf> <file3.pdf>")
    
    for pdf_path in sys.argv[1:]:
        
       