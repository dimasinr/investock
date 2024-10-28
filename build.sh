echo "Building project packages..."
sudo apt-get update
sudo apt-get install sqlite3 libsqlite3-dev
echo "Installing project requirements..."
python3 -m pip install -r requirements.txt
python3 manage.py runserver
# echo "Migrating Database..."
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

# echo "Collecting static files..."
# python3 manage.py collectstatic --noinput