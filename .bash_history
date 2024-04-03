ls
sudo mount -t vboxsf -o uid=$(id -u),gid=$(id -g) vagrant vagrant
cd ..
sudo mount -t vboxsf -o uid=$(id -u),gid=$(id -g) vagrant vagrant
ls
cd vagrant
ls
python3 -m venv ~/env
source ~/env/bin/activate
python manage.py makemigrations profile_api
python manage.py makemigrations profiles_api
python manage.py migrate
python manage.py createsuperuser
python manage.py migrate
python manage.py createsuperuser
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
deactivate
exit
