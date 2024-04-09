import findspark
from pyspark import SparkContext
from pyspark.sql import SparkSession, Window, Row
from pyspark.sql.functions import *
from pyspark.sql.types import *
import matplotlib.pyplot as plt

#https://spark.apache.org/docs/latest/sql-getting-started.html
spark = SparkSession \
        .builder \
        .appName("firstSpark") \
        .getOrCreate()

def load_dataframe(filename):
    df = spark.read.format('csv').options(header='true').load(filename)
    return df

#creating a dataframe
df_matches = load_dataframe('./Data/Matches.csv')
df_matches.limit(5).show()

###