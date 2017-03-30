a = c(13,13, 
         14,14,14,14,14,14,
         15,15,15,15,15,15,
         16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,
         17,17,17,17,17,17,17,
         18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,
         19,19,19,19,19,19,19,19,19,19,19,
         20,20,20,20,20,20,20,20,20,
         21,21,21,21,21,21,21,21,21,21,21,
         22,22,22,22,22,22,22,22,22,
         23,23,23,24,25,25,27)
table(a)

ggplot(train,aes(x=as.factor(label)))+
  geom_bar(stat="count")+
  labs(title="Digits in Train Data",x="Digits")

sample = sample(1:nrow(train),50)
var = t(train[sample,-1])
var_matrix = lapply(1:50,function(x) matrix(var[,x],ncol=28))
opar = par(no.readonly = T)
par(mfrow=c(5,10),mar=c(.1,.1,.1,.1))

for(i in 1:5) {
  for(j in 1:28) {
    var_matrix[[i]][j,] <- rev(var_matrix[[i]][j,])
  }
  image(var_matrix[[i]],col=grey.colors(225),axes=F)
}