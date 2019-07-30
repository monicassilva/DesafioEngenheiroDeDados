# bibliotecas 
library(sqldf)
library(stringr)
library(dplyr)

# Importa os datasets
logAug <- data.frame(readLines("~/Downloads/access_log_Aug95", warn = FALSE))
logJul <- data.frame(readLines("~/Downloads/access_log_Jul95", warn = FALSE))

# Junta os datasets
log <- sqldf("Select * from logAug union all Select * from logJul")

# Renomeia a coluna do data frame gerado pelos datasets			 
names(log) <- "Dados"

# Extrai os campos de cada registro
host <- str_extract(log$Dados, pattern = "(.+) - -")
data <- str_sub(str_extract(log$Dados, pattern = "\\[(.+)") %>% str_extract(pattern = "(.+)]"),2,12)
url <- str_extract(log$Dados, pattern = "(.+)\"") %>% str_extract(pattern = "\"(.+)") %>% str_replace_all("\"","")
retorno <- str_trim(str_trim(str_extract(log$Dados, pattern = "\" (.+)") %>% str_extract(pattern = "[0-9]{3}")))
bytes <- as.numeric(str_replace(str_extract(log$Dados, pattern = "\" [0-9]{3}(.+)") %>% str_replace(pattern = "\" [0-9]{3} ", ""),"-","0"))

# Cria um novo data frae com as novas colunas
r <- data.frame(cbind(host,data,url,retorno,bytes))

# QUESTÕES

# 1 - Número de hosts únicos
length(unique(r$host)) 

# 2 - Total de erros 404
count(filter(r,retorno == '404'))

# 3 - Os 5 URLs que mais causaram erro 404
head(sqldf("Select url, count(retorno) from r where retorno like '%404%' group by url order by count(retorno) desc"),5)

# 4 - Quantidade de erros 404 por dia
sqldf("Select data, count(retorno) as qtd_404 from r where retorno like '%404%' group by data order by data")

# 5 - Total de bytes retornados
sqldf("Select sum(bytes) total_bytes from r")
