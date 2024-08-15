set notebook=%1 
python -m nbconvert --output-dir="./templates/notebooks/" --to html ./notebooks/%notebook%.ipynb 
