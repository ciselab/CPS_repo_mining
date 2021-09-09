library(stringr)
library(dplyr)

getRawData <- function(){
  csvFile='../results.csv'
  df <- read.csv(csvFile, stringsAsFactors = FALSE)
  
  # split multi categories
  
  final_df <- df[0,]
  for(row in seq(from=1, to=nrow(df), by=1)){
    antipattern <- as.character(df[[row, 'antipattern']])
    if (str_detect(antipattern,"\\n")){
      antipatterns <- str_split(antipattern,"\\n",simplify = TRUE)
      for (ap in antipatterns){
        if(ap == "?" | ap =="New:?"){
          next
        }
        
        ap <- str_replace(ap,"\\\\","")
        row_to_import <- df[row,] 
        
        row_to_import['antipattern'] <- ap
        final_df[nrow(final_df) + 1,] <- row_to_import
      }
    }else{
      final_df[nrow(final_df) + 1,] <- df[row,]
    }
  }
  return(final_df)
}