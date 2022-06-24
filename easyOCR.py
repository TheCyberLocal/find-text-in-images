import easyocr

# ['en', 'ch_tra']
reader = easyocr.Reader(['en'])

results = reader.readtext('images1.png')

print(str(results))

posi = ''
text = ''
prob = ''
for result in results:
    posi += str(result[0]) + ' '
    text += str(result[1]) + ' '
    prob += str(result[2]) + ' '

print(posi)
print(text)
print(prob)

"""
pip install opencv-python
pip install virtualenv
pip install virtualenvwrapper

# in terminal
python -m venv env

# in cmd
env\Scripts\activate
pip install easyocr
deactivate

"""
