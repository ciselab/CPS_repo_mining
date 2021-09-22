source('dataclean.r')

library(ggplot2)
library(ggVennDiagram)
raw_df <-getRawData()


# hard coded timing
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Impatient_requester","New:Hard-coded-timing",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:General:Hard-coded-fine-tuning","New:Hard-coded-fine-tuning",as.character(raw_df$antipattern))


# general
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Hard-coding","Non-performance Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Lack_of_documentation","Non-performance Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General: Deadlock","Non-performance Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:Code_Duplication","Non-performance Antipatterns",as.character(raw_df$antipattern))
raw_df$antipattern <- ifelse(raw_df$antipattern == "General:bottleneck","Non-performance Antipatterns",as.character(raw_df$antipattern))


# Fix caps lock issue
raw_df$antipattern <- ifelse(raw_df$antipattern == "New:Rounded_numbers","New:rounded_numbers",as.character(raw_df$antipattern))


# replace - with X
raw_df$antipattern <- ifelse(raw_df$antipattern == "-","X",as.character(raw_df$antipattern))

# general performance antipatterns
# categorizing  antipatterns starting with General:performance in this category
#General:recreate_objects is also a general performance antipattern
#Network:performance should also be considered as general performance antipattern

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
  mutate(performance_cat = ifelse(str_starts(antipattern,"New:"),"New CPS SPAs",
                                  ifelse(str_starts(antipattern,"Smith:"),"Known CPS  SPAs","General SPAs")
                                  ))

cps_antipatterns_df$antipattern <- ifelse(str_starts(cps_antipatterns_df$antipattern,"New:"),substring(cps_antipatterns_df$antipattern,5),cps_antipatterns_df$antipattern)
cps_antipatterns_df$antipattern <- ifelse(str_starts(cps_antipatterns_df$antipattern,"Smith:"),substring(cps_antipatterns_df$antipattern,7),cps_antipatterns_df$antipattern)
cps_antipatterns_df$antipattern <- str_replace_all(cps_antipatterns_df$antipattern,"_"," ")
cps_antipatterns_df$antipattern <- str_replace_all(cps_antipatterns_df$antipattern,"-"," ")
cps_antipatterns_df$antipattern <- ifelse(cps_antipatterns_df$antipattern == "Where am I ?","Where am I?",cps_antipatterns_df$antipattern)


ggplot(cps_antipatterns_df, aes(x=reorder(antipattern, -count), y=as.numeric(count), fill = performance_cat)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x = element_text(angle=50, vjust=1, hjust=1,face = "bold", size=12)) +
  geom_label(aes(label = count),
             position = position_stack(vjust = 0.5),
             fill ="white",
             size = 5,
             show.legend = FALSE)+
  scale_fill_manual(values=c("#ffeda0","#fc8d59","#d7301f")) +
  guides(fill=guide_legend(title="Performance Issues Categories")) +
  theme(legend.title = element_text( size=12, face="bold"),
        legend.text = element_text( size = 12, face = "bold"),
        legend.position = "top")+
  xlab("Identified Performance issues and antipatterns") +
  ylab("Number of occurance") +
  theme(axis.title=element_text(size=14,face="bold"))


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
