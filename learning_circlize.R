## based on https://jokergoo.github.io/circlize_book/book/introduction.html#principle-of-design
## creating a chord diagram

df_gpsc <- read.xlsx("allData_analysis.xlsx", 
                     sheetName = "gpsc_small", header = T)

# getting freq of each categorical variable with each GPSC
gpsc_mdr_men <- data.frame(table(df_gpsc$Strain, df_gpsc$MDR_MEN))
gpsc_mdr_nm <- data.frame(table(df_gpsc$Strain, df_gpsc$MDR_NM))
gpsc_pcv <- data.frame(table(df_gpsc$Strain, df_gpsc$PCV13))
gpsc_inv <- data.frame(table(df_gpsc$Strain, df_gpsc$Invasive.Non.invasive))

# merging dataframes
df_list <- list(gpsc_mdr_men, gpsc_mdr_nm, gpsc_pcv, gpsc_inv)  
df_data <- Reduce(function(x, y) merge(x, y, all=TRUE), df_list)

# create simple chord diagram
chordDiagram(df_data)
