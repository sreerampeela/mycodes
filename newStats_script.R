## script new
library(ggplot2)
library(reshape2)
library(dplyr)
library(tidyr)

df2 <- read.csv("allData_analysis.csv", header = T)

## demographic plots
gender <- as.factor(df$GENDER)
boxplot(df$PATIENT.AGE ~ gender)

## creating age groups
df$ageGrp <- cut(df$PATIENT.AGE, breaks = c(0, 5,13,45,60, 100), 
                 labels = c("Young child", "child", "young adult", "adult", "old adult"))

df_age <- data.frame(table(df$ageGrp))
barplot(df_age$Freq, names.arg = df_age$Var1, 
        xlab = "Age group", ylab = "Frequency")
# other bar plots
df_year <- data.frame(table(df$Year))
barplot(df_year$Freq, names.arg = df_year$Var1, 
        xlab = "Year", ylab = "Frequency")

## year-wise invasive non-invasive
df_yr_in <- data.frame(table(select(df, c("Year", "Invasive.Non.invasive"))))

ggplot(data = df_yr_in, aes(x=Year, y= value, fill = Invasive.Non.invasive)) + 
  geom_bar(stat = "identity") + 
  scale_x_continuous(breaks=c(2015:2023), 
                     labels=c("2015", "2016", "2017", "2018","2019", "2020", 
                              "2021", "2022", 2023)) + 
  ylab("Frequency")

# GPSC frequency year wise
gpsc_yr_in <- data.frame(table(select(df, c("Year", "Strain"))))
ggplot(data = gpsc_yr_in, aes(x=Strain, y= Freq, fill = Year)) + 
  geom_bar(stat = "identity") + 
  ylab("Frequency")
cumFreq <- data.frame(table(select(df, c("Strain", "Year", "PCV13"))))
gpsc_counts <- data.frame(table(df$Strain))
freq_gpsc_counts <- gpsc_counts[gpsc_counts$Freq >= 2, ] #ignoring <1% frequency
## selecting entries with most frequent gpsc counts
freq_gpscs <- cumFreq[cumFreq$Strain %in% freq_gpsc_counts$Var1, ]
ggplot(data = freq_gpscs, aes(x = Strain, y=Freq, fill = PCV13)) + 
  geom_bar(stat = "identity")
ggplot(data = freq_gpscs, aes(x=Strain, y = reorder(x = Strain, X= Freq, decreasing = T))) + 
  geom_bar(stat = "identity", na.rm = T)

## gpsc pre and post vacc

gpsc_prevacc <- data.frame(table(select(df, c("PreVacc", "Strain"))))
gpsc_prevacc <- gpsc_prevacc[gpsc_prevacc$Freq >= 2, ]
ggplot(data = gpsc_prevacc, aes(x=Strain, y= Freq, fill = PreVacc)) + 
  geom_bar(stat = "identity") + 
  ylab("Frequency") + guides(fill=guide_legend(title="Prevaccine period"))

## histograms for various continuous values
hist(df$No..Contigs, xlab = "Number of contigs", 
     ylab = "Frequency", main = "Number of contigs", ylim = c(0,150))




