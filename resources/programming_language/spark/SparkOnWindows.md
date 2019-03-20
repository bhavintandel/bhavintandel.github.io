# Install the python packages

pip install findspark
pip install ipython
pip install notebook


# Set the path on terminal

setx SPARK_HOME E:\opt\spark\spark-2.3.0-bin-hadoop2.7

setx HADOOP_HOME E:\opt\spark\spark-2.3.0-bin-hadoop2.7

setx PYSPARK_DRIVER_PYTHON ipython

setx PYSPARK_DRIVER_PYTHON_OPTS notebook

set PYTHONPATH $SPARK_HOME/python:$PYTHONPATH

set PYTHONPATH $SPARK_HOME/python/lib/py4j-0.10.6-src.zip:$PYTHONPATH


Add ;E:\opt\spark\spark-2.3.0-bin-hadoop2.7\bin to the environmental variable in Path 

# To test
* open anaconda terminal
```
import findspark
findspark.init()

import pyspark # only run after findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()
```

# Pycharm

## Edit configuration in pycham
* Add python and py4j to the path



