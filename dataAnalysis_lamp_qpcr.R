## data of only cases where both qPCR and qLAMP were positive
df_ct <- read.csv("LAMP_PCR_ct.csv", header = T) 
summary(df_ct)                                        
shapiro.test(df_ct$qlamp)
shapiro.test(df_ct$qpcr)
dfCSF = subset(df_ct, df_ct$group == "csf")
dfCAP = subset(df_ct, df_ct$group == "Blood")


### Menigitis ###
mean(dfCSF$qlamp)
mean(dfCSF$qpcr)
qLAMP2 = (dfCSF$qlamp - mean(dfCSF$qlamp))/sd(dfCSF$qlamp)
qPCR2 = (dfCSF$qpcr -mean(dfCSF$qpcr))/sd(dfCSF$qpcr)
shapiro.test(qPCR)
shapiro.test(qLAMP)
var.test(qLAMP, qPCR)
t.test(qLAMP,qPCR, var.equal = F)
cor.test(qLAMP,qPCR)

### CAP ##
mean(dfCAP$qlamp)
sd(dfCAP$qlamp)
mean(dfCAP$qpcr)
sd(dfCAP$qpcr)
#Z-score normalization
qLAMP = (dfCAP$qlamp - mean(dfCAP$qlamp))/sd(dfCAP$qlamp)
qPCR = (dfCAP$qpcr -mean(dfCAP$qpcr))/sd(dfCAP$qpcr)
shapiro.test(qPCR)
shapiro.test(qLAMP)
wilcox.test(qLAMP, qPCR) # data not normally distributed
cor.test(qLAMP,qPCR)
hist(qPCR)
hist(qLAMP)
