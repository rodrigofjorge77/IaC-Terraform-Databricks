from pyspark.sql.types import StructType, StructField, StringType, DateType, DecimalType
from pyspark.sql import functions as F
from pyspark.sql.functions import to_date, col
from pyspark.sql import DataFrame

def file_Export_to_S3(df: DataFrame, texto: str) -> None:
    
    bucket_path = "s3a://rodrigojorge-projeto202410-pispark/output/" + texto
    
    # Carregar o DataFrame para o S3 no formato CSV
    df.write \
        .format("csv") \
        .mode("overwrite") \
        .option("header", "true") \
        .save(bucket_path)

# Define o schema do DataFrame
schema = StructType([
    StructField("Invoice Date", DateType(), True),
    StructField("Product", StringType(), True),
    StructField("Region", StringType(), True),
    StructField("Retailer", StringType(), True),
    StructField("Sales Method", StringType(), True),
    StructField("State", StringType(), True),
    StructField("Price per Unit", DecimalType(precision=10, scale=0), True),
    StructField("Total Sales", DecimalType(precision=10, scale=0), True),
    StructField("Units Sold", DecimalType(precision=10, scale=0), True)
])

# Configuração de credenciais (substitua com suas próprias credenciais)
spark.conf.set("fs.s3a.access.key", "")
spark.conf.set("fs.s3a.secret.key", "")
spark.conf.set("fs.s3a.endpoint", "s3.amazonaws.com")  # Endpoint padrão do S3

# Caminho do arquivo no bucket S3
s3_path = "s3a://rodrigojorge-projeto202410-pispark/nike_dt_s3.csv"

# Ler o arquivo CSV e carregá-lo em um DataFrame
df = spark.read.csv(s3_path, header=True, schema=schema)

# Remover linhas duplicadas considerando todas as colunas
df = df.dropDuplicates()

# Encontrar o valor mais frequente na coluna "State"
most_frequent_state = df.groupBy("State").count().orderBy(F.desc("count")).first()[0]

# Preencher valores nulos na coluna "State" com o valor mais frequente
df = df.fillna({"State": most_frequent_state})

sum_product = df.groupBy("Product").agg({"Units Sold": "sum"})  # produtos mais vendidos
sum_region = df.groupBy("Region").agg({"Units Sold": "sum"}) # produtos mais vendidos por região
sum_Retailer = df.groupBy("Retailer").agg({"Units Sold": "sum"}) # produtos mais vendidos por Retailer
sum_Sales_Method = df.groupBy("Sales Method").agg({"Units Sold": "sum"}) # produtos mais vendidos por Sales Method
sum_state = df.groupBy("State").agg({"Units Sold": "sum"}) # produtos mais vendidos por State

sum_ano_mes = df.groupBy(                       #---produtos mais vendidos por ano e mes
    F.year("Invoice Date").alias("Year"),
    F.month("Invoice Date").alias("Month")
).agg(
    F.sum("Units Sold").alias("Units Sold")
).orderBy(F.asc("Year"), F.asc("Month"))

sum_rent_product = df.groupBy("Product").agg({"Total Sales": "sum"}) #rentabilidade por produto
sum_rent_region = df.groupBy("Region").agg({"Total Sales": "sum"}) #rentabilidade por região
sum_rent_retailer = df.groupBy("Retailer").agg({"Total Sales": "sum"}) #rentabilidade por Retailer
sum_rent_sales_method = df.groupBy("Sales Method").agg({"Total Sales": "sum"}) #rentabilidade por Sales Method
sum_rent_state = df.groupBy("State").agg({"Total Sales": "sum"}) #rentabilidade por State

sum_rent_ano_mes = df.groupBy(                      #rentabilidade por ano e mes
    F.year("Invoice Date").alias("Year"),
    F.month("Invoice Date").alias("Month")
).agg(
    F.sum("Total Sales").alias("Total Sales")
).orderBy(F.asc("Year"), F.asc("Month"))

avg_product = df.groupBy("Product").agg({"Units Sold": "avg"}) #média de unidades vendidas por produto no periodo
avg_total_sales = df.groupBy("Product").agg({"Total Sales": "avg"}) #média de vendas por produto no periodo

std_prod = df.groupBy("Product").agg(                           #desvio padrão das unidades vendidas por produto
    F.stddev("Units Sold").alias("Standard Deviation"),
    F.avg("Units Sold").alias("Average")
)

# Carregando no S3------------
file_Export_to_S3(sum_product, "sum_product")
file_Export_to_S3(sum_region, "sum_region")
file_Export_to_S3(sum_Retailer, "sum_Retailer")
file_Export_to_S3(sum_Sales_Method, "sum_Sales_Method")
file_Export_to_S3(sum_state, "sum_state")
file_Export_to_S3(sum_ano_mes, "sum_ano_mes")
file_Export_to_S3(sum_rent_product, "sum_rent_product")
file_Export_to_S3(sum_rent_region, "sum_rent_region")
file_Export_to_S3(sum_rent_retailer, "sum_rent_retailer")
file_Export_to_S3(sum_rent_sales_method, "sum_rent_sales_method")
file_Export_to_S3(sum_rent_state, "sum_rent_state")
file_Export_to_S3(sum_rent_ano_mes, "sum_rent_ano_mes")
file_Export_to_S3(avg_product, "avg_product")
file_Export_to_S3(avg_total_sales, "avg_total_sales")
file_Export_to_S3(std_prod, "std_prod")

