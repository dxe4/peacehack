peacehack
=========

peacehack

Next time go for [spark...](https://spark.apache.org/) 


Some interesting stats on a `db.r3.xlarge` (30gb ram 4 cpu, ~20gb data, 58 cols):


```
# For more info read here
# http://en.wikipedia.org/wiki/2014_Ukrainian_revolution

```

![index](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/index.png)

![reads](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/reads_4.png)

![queue depth](https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/q_d_4.png)

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
