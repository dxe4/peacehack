peacehack
=========

peacehack

Next time go for [spark...](https://spark.apache.org/) 

```
sudo apt-get install python-virtualenv
git clone git@github.com:papaloizouc/peacehack.git
cd peacehack/peacehack
virtualenv venv
source venv/bin/activate
sourve dev.env
pip install -r req.txt
python manage.py collectstatic
python manage.py runserver
```