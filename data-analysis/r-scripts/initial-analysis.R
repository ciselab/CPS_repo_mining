# Install dataclean, functions needed to capture the raw data frames.
source('dataclean.r')
# Using these libraries.
library(ggplot2)
library(ggVennDiagram)
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

# general
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


ggplot(cps_antipatterns_df, aes(x=reorder(antipattern, -count), y=as.numeric(count), fill = performance_cat)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=16)) +
  geom_label(aes(label = count),
             position = position_stack(vjust = 0.5),
             fill ="white",
             size = 9,
             show.legend = FALSE)+
  scale_fill_manual(values=c("#ffeda0","#fc8d59","#d7301f")) +
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
  

  
