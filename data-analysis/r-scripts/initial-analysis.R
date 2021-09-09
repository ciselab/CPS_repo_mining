source('dataclean.r')

raw_df <-getRawData()


# hard coded timinng
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Impatient_requester","New:Hard-coded-timing",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:General:Hard-coded-fine-tuning","New:Hard-coded-timing",as.character(raw_df$antipattern))


# general
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Hard-coding","General",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Lack_of_documentation","General",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General: Deadlock","General",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Code_Duplication","General",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:java:Unbuffered_Streams","General",as.character(raw_df$antipattern))


# Fix caps lock issue
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Rounded_numbers","New:rounded_numbers",as.character(raw_df$antipattern))


# replace - with X
raw_df$antipattern <- ifelse(raw_df$antipattern == "-","X",as.character(raw_df$antipattern))

# general performance antipatterns
# categorizing  antipatterns starting with General:performance in this category
#General:recreate_objects is also a general performance antipattern
#Network:performance should also be considered as general performance antipattern

raw_df$antipattern <- ifelse(
  str_starts(raw_df$antipattern,"General:performance") | str_starts(raw_df$antipattern,"Network:performance") | raw_df$antipattern == "General:recreate_objects"
  ,"General Performance Antipattern",as.character(raw_df$antipattern))



# CI/CD 
# ToDo: anything starting with CI/CD and New:build is under this category
raw_df$antipattern <- ifelse(str_starts(raw_df$antipattern,"CI/CD") | str_starts(raw_df$antipattern,"New:build"),
                             "CI/CD",as.character(raw_df$antipattern))
#antipatterns_df$antipattern <- as.factor(antipatterns_df$antipattern)
antipatterns_df <- raw_df %>%
  group_by(antipattern) %>%
  summarise(count = n())

# ?
antipatterns_df$antipattern <- ifelse(antipatterns_df$antipattern == "?","in progress",as.character(antipatterns_df$antipattern))


