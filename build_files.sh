echo "BUILD START"
python3 -m pip install -r requirements.txt
mkdir staticfiles_build
python3 manage.py collectstatic --noinput
echo "BUILD END"