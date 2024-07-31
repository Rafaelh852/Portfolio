set notebook=%1 
python -m nbconvert --output-dir="./template/notebooks/" --to html ./notebooks/%notebook%.ipynb 
