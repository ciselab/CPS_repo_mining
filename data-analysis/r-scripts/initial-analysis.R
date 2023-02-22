setwd("C:/Users/Imara/PycharmProjects/CPS_repo_mining/data-analysis/r-scripts")

# Install dataclean, functions needed to capture the raw data frames.
source('dataclean.r')
# Using these libraries.
library(ggplot2)
library(ggVennDiagram)
# For the last figure / pivot table
library(pivottabler)
# Get the raw data frame.
raw_df <-getRawData()

# Fix inconsistency with the names.
# hard coded timing
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Impatient_requester","New:Magical-Waiting-Number",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Hard-coded-timing","New:Magical-Waiting-Number",as.character(raw_df$antipattern))

# hard coded tuning
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Hard-coded-fine-tuning","New:Hard-Coded-Fine-Tuning",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:General:Hard-coded-fine-tuning","New:Hard-Coded-Fine-Tuning",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:General:hard_coded_fine_tuning","New:Hard-Coded-Fine-Tuning",as.character(raw_df$antipattern))

# Bad Noise Handling
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:unstable_and_slow_noise_handling","New:Bad-Noise-Handling",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Bad-noise-handling","New:Bad-Noise-Handling",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Bad_Noise_Handling","New:Bad-Noise-Handling",as.character(raw_df$antipattern))

# general (Non-performance Antipatterns)
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Hard-coding","Non-performance-Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Lack_of_documentation","Non-performance-Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General: Deadlock","Non-performance-Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Code_Duplication","Non-performance-Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:bottleneck","Non-performance-Antipatterns",as.character(raw_df$antipattern))

# Fix caps lock issue
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:rounded_numbers","New:Rounded_Numbers",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Rounded_numbers","New:Rounded_Numbers",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Fixed-communication-rate","New:Fixed_Communication_Rate",as.character(raw_df$antipattern))

# replace - with X
raw_df$antipattern <- ifelse(raw_df$antipattern == "-","X",as.character(raw_df$antipattern))

# FI where was I antipattern
raw_df$antipattern <- ifelse(raw_df$antipattern == "Smith:Where_am_I_?","Smith:Where_Was_I",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "Known:Where_was_I","Smith:Where_Was_I",as.character(raw_df$antipattern))

# Fix Fixed Communication Rate
raw_df$antipattern <- ifelse(raw_df$antipattern == "Fixed_Communication_Rate","New:Fixed_Communication_Rate",as.character(raw_df$antipattern))

# Fix Is everything ok
raw_df$antipattern <- ifelse(raw_df$antipattern == "Known:Is-everything-ok","Smith:Is_Everything_OK",as.character(raw_df$antipattern))

# general performance antipatterns
# categorizing  antipatterns starting with General:performance in this category
#General:recreate_objects is also a general performance antipattern
#Network:performance should also be considered as general performance antipattern

genera_performance_ap_df <- raw_df %>%
  filter(str_starts(raw_df$antipattern,"General:performance") | str_starts(raw_df$antipattern,"General:Performance") |
           str_starts(raw_df$antipattern,"Network:performance") | str_starts(raw_df$antipattern,"Smith:General") |
           raw_df$antipattern == "General:recreate_objects")

genera_performance_ap_df <- genera_performance_ap_df %>%
  mutate(introduced_by_Smith = ifelse(str_starts(antipattern,"Smith:General"), "Yes","No"))

genera_performance_ap_df$antipattern <- ifelse(str_starts(genera_performance_ap_df$antipattern,"General:performance:"),substring(genera_performance_ap_df$antipattern,21),genera_performance_ap_df$antipattern)
genera_performance_ap_df$antipattern <- ifelse(str_starts(genera_performance_ap_df$antipattern,"General:Performance:"),substring(genera_performance_ap_df$antipattern,21),genera_performance_ap_df$antipattern)
genera_performance_ap_df$antipattern <- ifelse(str_starts(genera_performance_ap_df$antipattern,"Network:performance:"),substring(genera_performance_ap_df$antipattern,21),genera_performance_ap_df$antipattern)
genera_performance_ap_df$antipattern <- ifelse(str_starts(genera_performance_ap_df$antipattern,"General:"),substring(genera_performance_ap_df$antipattern,9),genera_performance_ap_df$antipattern)
genera_performance_ap_df$antipattern <- ifelse(str_starts(genera_performance_ap_df$antipattern,"Smith:General:"),substring(genera_performance_ap_df$antipattern,15),genera_performance_ap_df$antipattern)
genera_performance_ap_df$antipattern <- str_replace_all(genera_performance_ap_df$antipattern,"_"," ")

genera_performance_ap_df <- genera_performance_ap_df %>%
  group_by(antipattern,introduced_by_Smith) %>%
  summarise(count = n())

###
# OLD GRAPH - UNUSED
###

ggplot(genera_performance_ap_df, aes(x = reorder(antipattern, -count), y = as.numeric(count), fill=introduced_by_Smith)) + geom_bar(stat = "identity") +   theme(axis.text.x = element_text(angle=65, vjust=1, hjust=1,face = "bold", size=20), axis.text.y = element_text(face = "bold", size=16)) +
  scale_fill_grey(start = 0, end = .7) +   theme(legend.title = element_text( size=17, face="bold"),
                                                 legend.text = element_text( size = 17, face = "bold"),
                                                 legend.position = "top") +  
  guides(fill=guide_legend(title="Reported by Smith"))+
  xlab("Identified General Performance antipatterns") +
  ylab("Number of occurance") +
  theme(axis.title=element_text(size=25,face="bold"))

raw_df$antipattern <- ifelse(
  str_starts(raw_df$antipattern,"General:performance") | str_starts(raw_df$antipattern,"General:Performance") | 
    str_starts(raw_df$antipattern,"Network:performance") | str_starts(raw_df$antipattern,"Smith:General") |
    raw_df$antipattern == "General:recreate_objects"
  ,"General Performance Antipattern",as.character(raw_df$antipattern))


# CI/CD 
# ToDo: anything starting with CI/CD and New:build is under this category
raw_df$antipattern <- ifelse(str_starts(raw_df$antipattern,"CI/CD") | str_starts(raw_df$antipattern,"New:build"),
                             "CI/CD Performance Issues",as.character(raw_df$antipattern))
#antipatterns_df$antipattern <- as.factor(antipatterns_df$antipattern)
antipatterns_df <- raw_df %>%
  group_by(antipattern) %>%
  summarise(count = n())

# ?
antipatterns_df$antipattern <- ifelse(antipatterns_df$antipattern == "?","Needs Pair Analysis",as.character(antipatterns_df$antipattern))

bigger_picture_df <- antipatterns_df %>%
  mutate(high_level_cat = ifelse(antipattern == "X","Not an Antipattern/Performance Issue", 
                                 ifelse(antipattern == "in porgress","Needs Pair Analysis",
                                        ifelse(str_starts(antipattern,"New:") | str_starts(antipattern,"Smith:") | antipattern == "General Performance Antipattern","Performance Issues",antipattern)
                                        )))



#performance_antipatterns_df <- bigger_picture_df %>%
 # filter(high_level_cat %in% c("General Performance Antipattern","CPS Performance Antipatterns"))

cps_antipatterns_df <- bigger_picture_df %>%
  filter(high_level_cat == "Performance Issues")



bigger_picture_df <- bigger_picture_df %>%
  group_by(high_level_cat) %>%
  summarise(total_count = sum(count)) %>%
  mutate(label_text = paste0(total_count," (",
                            formatC(100 *total_count/sum(total_count), digits = 0, format = "f"),"%)")
                            )%>%
  filter(high_level_cat != "Needs Pair Analysis")

###
# Old Graph: Commits Categories, used in the report
###

ggplot(bigger_picture_df, aes(x = "", y = total_count, fill = high_level_cat)) +
  geom_col(color = "black") +

  geom_label(aes(label = label_text),
             position = position_stack(vjust = 0.4),
             size = 7,
             show.legend = FALSE,
             fontface = "bold") +
  coord_polar(theta = "y") + 
  scale_fill_brewer()  +
  guides(fill=guide_legend(title="Commits Categories")) +
  theme(panel.background = element_blank(),
        axis.ticks = element_blank(),
        axis.text.x = element_blank(),
        axis.text.y = element_blank(),
        axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        legend.title = element_text( size=16, face="bold"),
        legend.text = element_text( size = 16, face = "bold"))

cps_antipatterns_df <- cps_antipatterns_df %>%
  mutate(performance_cat = ifelse(str_starts(antipattern,"New:"),"New CPS-PAs",
                                  ifelse(str_starts(antipattern,"Smith:"),"Known CPS-PAs","General SPAs")
  ))


cps_antipatterns_df$antipattern <- ifelse(str_starts(cps_antipatterns_df$antipattern,"New:"),substring(cps_antipatterns_df$antipattern,5),cps_antipatterns_df$antipattern)
cps_antipatterns_df$antipattern <- ifelse(str_starts(cps_antipatterns_df$antipattern,"Smith:"),substring(cps_antipatterns_df$antipattern,7),cps_antipatterns_df$antipattern)
cps_antipatterns_df$antipattern <- str_replace_all(cps_antipatterns_df$antipattern,"_"," ")
cps_antipatterns_df$antipattern <- str_replace_all(cps_antipatterns_df$antipattern,"-"," ")
cps_antipatterns_df$antipattern <- ifelse(cps_antipatterns_df$antipattern == "Where am I ?","Where am I?",cps_antipatterns_df$antipattern)

###
# First bar graph - USED
###

# Hardcoded removed the first row, to remove the generic category.
cps_antipatterns_df <- cps_antipatterns_df[-1,]

ggplot(cps_antipatterns_df, aes(x=reorder(antipattern, -count), y=as.numeric(count), fill = performance_cat)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=16)) +
  geom_label(aes(label = count),
             position = position_stack(vjust = 0.5),
             fill ="white",
             size = 9,
             show.legend = FALSE)+
  # scale_fill_manual(values=c("#ffeda0","#fc8d59","#d7301f")) +
  scale_fill_manual(values=c("#fc8d59","#d7301f")) +
  guides(fill=guide_legend(title="Performance Issues Categories")) +
  theme(legend.title = element_text( size=17, face="bold"),
        legend.text = element_text( size = 17, face = "bold"),
        legend.position = "top")+
  xlab("Identified Performance issues and antipatterns") +
  ylab("Frequency") +
  theme(axis.title=element_text(size=25,face="bold"))
  #xlab("Identified Performance issues and antipatterns") +
  #ylab("Number of occurance") +
  #theme(axis.title=element_text(size=25,face="bold"))


venn_df <- raw_df %>%
  filter(antipattern != "X" & antipattern != "?" & antipattern != "CI/CD") %>%
  mutate(case = paste0(project,"-",commit))
unique(venn_df$antipattern)


test <- venn_df %>% group_by(case)%>%
  summarise(count = n()) %>%
  filter(count > 1)


unique_Ms <- test$case

test2 <- venn_df %>% filter(case %in% unique_Ms)

venn_list = list()
for (ap in unique(test2$antipattern)){
  temp_df <- test2 %>%
    filter(antipattern == ap)
  venn_list[[ap]] <- temp_df$case
}

ggVennDiagram(venn_list)


###
# Second bar graph - USED
###

raw_df$keyword <- ifelse(raw_df$keyword == "Slow","slow",raw_df$keyword)
raw_df$keyword <- ifelse(raw_df$keyword == "Fast","fast",raw_df$keyword)
raw_df$keyword <- ifelse(raw_df$keyword == "Increase" | raw_df$keyword == "increases","increase",raw_df$keyword)

keywords_df <- raw_df %>%
  mutate(is_ap = ifelse(antipattern == "X","No","Yes")) %>%
  group_by(keyword,is_ap) %>%
  summarise(count = n())


keywords_df$is_ap <- as.factor(keywords_df$is_ap)


answers <- unique(keywords_df$is_ap)
kws <- unique(keywords_df$keyword)

final_keywords_df <- keywords_df[0,]
final_keywords_df$count <- as.integer(final_keywords_df$count)
for (kw in kws){
  for (ans in answers){
    temp_df <- keywords_df %>%
      filter(is_ap == ans & keyword == kw)
    print(nrow(temp_df))
    if (nrow(temp_df) == 1){
      final_keywords_df <- rbind(final_keywords_df, temp_df)
    }else{
      final_keywords_df <- rbind(final_keywords_df, as.dataframe(c(keyword = kw,is_ap = ans,count = as.integer(0))))
    }
  }
}



ggplot(data = keywords_df, mapping = aes(x = keyword, y = as.numeric(count), fill = is_ap)) +
  geom_bar(stat = "identity",  position = "dodge") +
  scale_fill_manual(values=c("#fc8d59","#d7301f")) +
  #ylab("Number of occurance") +
  ylab("Frequency") +
  theme(legend.title = element_text( size=17, face="bold"),
        legend.text = element_text( size = 17, face = "bold"),
        #legend.position = "top") +
        legend.position = c(0.9, 0.9)) +
  guides(fill=guide_legend(title="Is it an antipattern?")) +
  theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=16),
        axis.text.y = element_text(face= "bold", size = 16),
        axis.title = element_text(face = "bold", size = 16)) +
  geom_text(aes( label=count), position = position_dodge(0.9),
            vjust = -0.5,
            color="black", size=7)
  geom_label(aes(label = count),
             fill ="white",
             size = 9,
             show.legend = FALSE)
  

###
# Try out, keyword counting
###
  
# ggplot(cps_antipatterns_df, aes(x=reorder(antipattern, -count), y=as.numeric(count), fill = performance_cat)) + 
#   geom_bar(stat = "identity") + 
#   theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=16)) +
#   geom_label(aes(label = count),
#              position = position_stack(vjust = 0.5),
#              fill ="white",
#              size = 9,
#              show.legend = FALSE)+
#   scale_fill_manual(values=c("#ffeda0","#fc8d59","#d7301f")) +
#   guides(fill=guide_legend(title="Performance Issues Categories")) +
#   theme(legend.title = element_text( size=17, face="bold"),
#         legend.text = element_text( size = 17, face = "bold"),
#         legend.position = "top")+
#   xlab("Identified Performance issues and antipatterns") +
#   ylab("Frequency") +
#   theme(axis.title=element_text(size=25,face="bold"))
  

  
keyword_list <- c('performance','memory','runtime','slow','slower','slowing','fast','faster','increase','decrease','memory-heap','memory-leak','bottleneck','overhead','deadlock','livelock','infinite','impasse','hang')
#message_content <- raw_df$message
csvFile='../results.csv'
real_raw_df <- read.csv(csvFile, stringsAsFactors = FALSE)
message_content <- real_raw_df$message
#keywords_df <- data.frame(message_content, keyword_list, stringsAsFactors=FALSE)
#raw_df$exists_in_message <- mapply(grepl, pattern=keywords_df$keyword_list, x=keywords_df$message_content)
#grep("performance", message_content, value = TRUE)

print('performance')
deadlock_results <- str_detect(tolower(message_content), 'performance')
length(deadlock_results[deadlock_results==TRUE])
print('memory')
deadlock_results <- str_detect(tolower(message_content), 'memory')
length(deadlock_results[deadlock_results==TRUE])
print('runtime')
deadlock_results <- str_detect(tolower(message_content), 'runtime')
length(deadlock_results[deadlock_results==TRUE])
print('slow')
deadlock_results <- str_detect(tolower(message_content), 'slow')
length(deadlock_results[deadlock_results==TRUE])  
print('slower')
deadlock_results <- str_detect(tolower(message_content), 'slower')
length(deadlock_results[deadlock_results==TRUE])
print('slowing')
deadlock_results <- str_detect(tolower(message_content), 'slowing')
length(deadlock_results[deadlock_results==TRUE])
print('fast')
deadlock_results <- str_detect(tolower(message_content), 'fast')
length(deadlock_results[deadlock_results==TRUE])
print('faster')
deadlock_results <- str_detect(tolower(message_content), 'faster')
length(deadlock_results[deadlock_results==TRUE])
print('increase')
deadlock_results <- str_detect(tolower(message_content), 'increase')
length(deadlock_results[deadlock_results==TRUE])
print('decrease')
deadlock_results <- str_detect(tolower(message_content), 'decrease')
length(deadlock_results[deadlock_results==TRUE])
print('memory-heap')
deadlock_results <- str_detect(tolower(message_content), 'memory-heap')
length(deadlock_results[deadlock_results==TRUE])
print('memory-leak')
deadlock_results <- str_detect(tolower(message_content), 'memory-leak')
length(deadlock_results[deadlock_results==TRUE])
print('bottleneck')
deadlock_results <- str_detect(tolower(message_content), 'bottleneck')
length(deadlock_results[deadlock_results==TRUE])
print('overhead')
deadlock_results <- str_detect(tolower(message_content), 'overhead')
length(deadlock_results[deadlock_results==TRUE])
print('deadlock')
deadlock_results <- str_detect(tolower(message_content), 'deadlock')
length(deadlock_results[deadlock_results==TRUE])
print('livelock')
deadlock_results <- str_detect(tolower(message_content), 'livelock')
length(deadlock_results[deadlock_results==TRUE])
print('infinite')
deadlock_results <- str_detect(tolower(message_content), 'infinite')
length(deadlock_results[deadlock_results==TRUE])
print('impasse')
deadlock_results <- str_detect(tolower(message_content), 'impasse')
length(deadlock_results[deadlock_results==TRUE])
print('hang')
deadlock_results <- str_detect(tolower(message_content), 'hang')
length(deadlock_results[deadlock_results==TRUE])
print('speed')
deadlock_results <- str_detect(tolower(message_content), 'speed')
length(deadlock_results[deadlock_results==TRUE])
print('memory leak')
deadlock_results <- str_detect(tolower(message_content), 'memory leak')
length(deadlock_results[deadlock_results==TRUE])
print('stuck')
deadlock_results <- str_detect(tolower(message_content), 'stuck')
length(deadlock_results[deadlock_results==TRUE])
#print('Performance')
#deadlock_results <- str_detect(tolower(message_content), 'performance')
#length(deadlock_results[deadlock_results==TRUE])



###
# Figure 4: antipatterns occuring in Projects
###

raw_df$project <- str_replace_all(raw_df$project,"\n","")

antpatternprojects_df <- raw_df %>%
  # mutate(is_ap = ifelse(antipattern == "X","No","Yes")) %>%
  # mutate(is_ap = ifelse(antipattern == "X","No","Yes")) %>%
  group_by(project,antipattern) %>%
  summarise(count = n())

print(antpatternprojects_df, n = 59)

# ggplot(data = antpatternprojects_df, mapping = aes(x = project, y = as.numeric(count), fill = antipattern)) +
#   geom_bar(stat = "identity",  position = "dodge") +
#   #scale_fill_manual(values=c("#fc8d59","#d7301f")) +
#   ylab("Antipattern") +
#   theme(legend.title = element_text( size=17, face="bold"),
#         legend.text = element_text( size = 17, face = "bold"),
#         #legend.position = "top") +
#         legend.position = c(0.9, 0.9)) +
#   guides(fill=guide_legend(title="Antipatterns in each Project")) +
#   theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=16),
#         axis.text.y = element_text(face= "bold", size = 16),
#         axis.title = element_text(face = "bold", size = 16)) +
#   geom_text(aes( label=count), position = position_dodge(0.9),
#             vjust = -0.5,
#             color="black", size=7)
# geom_label(aes(label = count),
#            fill ="white",
#            size = 9,
#            show.legend = FALSE)

# pt <- PivotTable$new()
# pt$addData(antpatternprojects_df)
# pt$addColumnDataGroups("project")
# pt$addRowDataGroups("antipattern")
# pt$defineCalculation(calculationName="count", summariseExpression="n()")
# pt$renderPivot()

# print("done one")
# 
# 
# antpatternprojects_df <- antpatternprojects_df %>% mutate(
#   project = factor(project),
#   antipattern = factor(antipattern),
# )
# 
# print(antpatternprojects_df, n = 59)

print("done two")

#antpatternprojects_df$count %>% tidyr::replace_na(0) %>%
# cln_df <- antpatternprojects_df$count %>% tidyr::replace_na(0) %>%
cln_df <- tidyr::pivot_wider(antpatternprojects_df, names_from = project, values_from = count) %>% replace(is.na(.), 0)
# cln_df <- tidyr::pivot_wider(antpatternprojects_df, names_from = project, values_from = count)

# Filter out Generic APs
#cln_df %>%
#  filter(antipattern=='New:Magical-Waiting-Number' | antipattern=='Smith:Where_Was_I' | antipattern=='New:Fixed_Communication_Rate' | antipattern=='New:Hard-Coded-Fine-Tuning' | antipattern=='New:Rounded_Numbers' | antipattern=='New:Bad-Noise-Handling' | antipattern=='Known:Is-everything-ok' | antipattern=='New:Delayed_Sync_With_Physical_Events' | antipattern=='Smith:Are_We_There_Yet' | antipattern=='Smith:Is_Everything_OK')
cln_df

# cln_df <- filter(antipattern=='New:Magical-Waiting-Number' | antipattern=='Smith:Where_Was_I' | antipattern=='New:Fixed_Communication_Rate' | antipattern=='New:Hard-Coded-Fine-Tuning' | antipattern=='New:Rounded_Numbers' | antipattern=='New:Bad-Noise-Handling' | antipattern=='Known:Is-everything-ok' | antipattern=='New:Delayed_Sync_With_Physical_Events' | antipattern=='Smith:Are_We_There_Yet' | antipattern=='Smith:Is_Everything_OK')

# print(cln_df, width = Inf) %>%
#   filter(antipattern=='New:Magical-Waiting-Number' | antipattern=='Smith:Where_Was_I' | antipattern=='New:Fixed_Communication_Rate' | antipattern=='New:Hard-Coded-Fine-Tuning' | antipattern=='New:Rounded_Numbers' | antipattern=='New:Bad-Noise-Handling' | antipattern=='Known:Is-everything-ok' | antipattern=='New:Delayed_Sync_With_Physical_Events' | antipattern=='Smith:Are_We_There_Yet' | antipattern=='Smith:Is_Everything_OK')


# print(cln_df, width = Inf)

# New:Magical-Waiting-Number
# Smith:Where_Was_I
# New:Fixed_Communication_Rate
# New:Hard-Coded-Fine-Tuning
# New:Rounded_Numbers
# New:Bad-Noise-Handling
# Known:Is-everything-ok
# New:Delayed_Sync_With_Physical_Events
# Smith:Are_We_There_Yet
# Smith:Is_Everything_OK

# cln_df

print("done three")


