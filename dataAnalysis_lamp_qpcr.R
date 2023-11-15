## data of only cases where both qPCR and qLAMP were positive
df_ct <- read.csv("LAMP_PCR_ct.csv", header = T) 
summary(df_ct)                                        
shapiro.test(df_ct$qlamp)
shapiro.test(df_ct$qpcr)
dfCSF = subset(df_ct, df_ct$group == "csf")
dfCAP = subset(df_ct, df_ct$group == "Blood")

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


### Menigitis ###
mean(dfCSF$qlamp)
mean(dfCSF$qpcr)
qLAMP2 = (dfCSF$qlamp - mean(dfCSF$qlamp))/sd(dfCSF$qlamp)
qPCR2 = (dfCSF$qpcr -mean(dfCSF$qpcr))/sd(dfCSF$qpcr)
shapiro.test(qPCR2)
shapiro.test(qLAMP2)
var.test(qLAMP2, qPCR2)
t.test(qLAMP2,qPCR2, var.equal = F)
cor.test(qLAMP2,qPCR2)

boxplot(qLAMP, qPCR, qLAMP2, qPCR2, names = c("qLAMP-CAP", "qPCR-CAP","qLAMP-MEN","qPCR-MEN"), ylab = " Normalised CT/CLAMP value")

## comparing mean Ct of lamp+ve and lamp-ve pcr
df_pcr <- read.csv("lamp_p_vs_n.csv", header = T)
lampPos = subset(df_pcr$ct, df_pcr$lamp == "lamp+")
shapiro.test(lampPos)
lampNeg = subset(df_pcr$ct, df_pcr$lamp == "lamp -ve")
shapiro.test(lampNeg)
## not normally distributed
boxplot(lampPos, lampNeg, names = c("qLAMP +ve", "qLAMP -ve"), ylab = "CT value")
wilcox.test(lampPos, lampNeg)

