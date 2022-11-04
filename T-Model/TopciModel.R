library(XML)
library(tm)
library(slam)
library(cluster) 
library(snakecase)
library(stopwords) 
library(xtable) 
library(Matrix)
library(devtools) 
library(topicmodels)
library(igraph)
library(stringr)
library(jsonlite)
library(corpus)

output_path = "dir_split_files/GAAS"

corpus <- SimpleCorpus(DirSource(output_path, encoding = "UTF-8"), control = list(language = "en"))
corpus <- tm_map(corpus, stripWhitespace) # remove white spaces
corpus <- tm_map(corpus, removeNumbers)   # remove numbers
corpus <- tm_map(corpus, removePunctuation) # remove punctuation
corpus <- tm_map(corpus, content_transformer(tolower)) # transform everything to lower case
# Apply stopword lists
corpus <- tm_map(corpus, removeWords, stopwords("en")) 
corpus <- tm_map(corpus, removeWords, stopwords(language = "en", source = "smart"))
corpus <- tm_map(corpus, removeWords, stopwords(language = "en", source = "snowball"))
corpus <- tm_map(corpus, removeWords, stopwords(language = "en", source = "stopwords-iso"))
corpus <- tm_map(corpus, removeWords, c("build", "pull", "push", "merge", "branch", "add", "plan","file","bug","docker","fixed","docs","tools","planning","framework","data","code"))
# Applying stemming
#corpus <- tm_map(corpus, stemDocument, language = "english")

# Build the document-by-term matrix
tdm <- DocumentTermMatrix(corpus, control = list(stemming = FALSE, wordLengths = c(2,Inf), bounds = list(global=c(2,Inf))))

rowTotals <- apply(tdm , 1, sum) #Find the sum of words in each Document
tdm   <- tdm[rowTotals> 0, ] 

ldm <- topicmodels::LDA(tdm, method="Gibbs", control = list(alpha=0.5, delta=0.2, iter=100, seed=1:10, nstart=10), k = 20)
post = topicmodels::posterior(ldm)
lda_model = ldm
print(topicmodels::terms(lda_model, k=20))
