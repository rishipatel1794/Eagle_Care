echo "BUILD START"
python3 -m pip instsll -r requirements.txt
mkdir staticfiles_build
python3 manage.py collectstatic --noinput
echo "BUILD END"