#!/bin/bash


echo "Hi, now executing webscrape to FHI Website:"
#conda activate corona_related
/home/efs/anaconda3/envs/corona_related/bin/python3.8 fhi_webscrape.py 

echo "Then executing MSIS webscrape and download the report(xls):"
/home/efs/anaconda3/envs/corona_related/bin/python3.8 msis_webscrape.py

echo "Save the result to pickle:"
/home/efs/anaconda3/envs/corona_related/bin/python3.8 msis_to_pickle.py

#echo "this is the whole list of dir"

