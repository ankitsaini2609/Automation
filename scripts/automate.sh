cp ~/dataset/scripts/resize.py .
python resize.py
cd resized
cp ~/dataset/scripts/to_black_white.py .
python to_black_white.py
cd black_n_white
cp ~/dataset/scripts/invert.py .
python invert.py
cd changed
cp ~/dataset/scripts/directory_creating.py .
python directory_creating.py
rm directory_creating.py
cp ~/dataset/scripts/script.py .
