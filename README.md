# DesafioEngenheiroDeDados

Questões Teoricas

Qual o objetivo do comando cache em Spark?
Armazena um resultado salvo em memória

O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?
No Spark a execução é feita em memoria, já no Map Reduce é no disco rigido

Qual é a função do SparkContext ?
É onde estão todas as funções nativas do Spark.

Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
São elementos distribuidos paralelamente pelo cluster

GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
O reduceByKey agrupa efetuando a redução do dados de maneira perfomativa através das chaves já
o GroupByKey agrupa todos os elementos para depois efetuar a redução dos dados


Explique o que o código Scala abaixo faz.

val textFile = sc . textFile ( "hdfs://..." ) - recebe algum arquivo do hdfs

val counts = textFile . flatMap ( line => line . split ( " " )) - conta a listagem de palavras do arquivo

.map ( word => ( word , 1 )) - listagem de tuplas atraves da listagem feita no comando anterior

.reduceByKey ( _ + _ ) - reduz a lista por chave ou seja não teremos duplicidades

counts.saveAsTextFile ("hdfs://...") - salva o resultado final em um novo arquivo
