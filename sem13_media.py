# -*- coding: utf-8 -*-
"""Sem13_Media

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jrCi0YQ9gA_kEukvFJfAfMDjhgPRmPGJ
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadistica").getOrCreate()

spark.stop()

spark

#Creamos un data con los valores para posteriosmente poder umplementar codigo donde haremos la resolucion
data = [("Jess",20),
        ("José",40),
        ("Crisvalencia",17),
        ("Pablito",25),
        ("Alisson",19),
        ("Sasha",18),
        ("Ana",15),
        ("Samantha",21)
        ]
columns = ["Nombre", "Edad"]
variable = spark.createDataFrame(data,columns)

#seleccionamos la columna edad y con ".alias" cambiamos el nombre y mostrarlo con el ".show()"
variable.select(mean(col("Edad")).alias("Media")).show()

#Y esto seria la misma forma de mostrarlo pero con el ".collect()"
variable.select(mean(col("Edad")).alias("Media")).collect()[0]["Media"]