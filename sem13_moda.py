# -*- coding: utf-8 -*-
"""Sem13_Moda

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zdrHOrOotG_mLbakyYPTqoqIw5xlHXXr
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadistica").getOrCreate()

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

#Un poco más de lo mismo con "var_moda" pero en esta ocación ".groupBy" se usará para agrupar
#las edades y ordenarlos
var_moda = variable.groupBy("Edad").count().orderBy(col("Count").desc()).first()

#Con "print" vamos a mostrar el resultado del codigo anterior
print("La moda es:", var_moda["Edad"])