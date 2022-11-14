head(cars)
scatter.smooth(x = cars$speed,y=cars$dist,main="Dist~Speed")
par(mfrow=c(1,2))
boxplot(cars$speed,main="Speed",sub=paste("Outlier rows:"))
boxplot(cars$speed,main="Speed",sub=paste("Outlier rows:",boxplot.stats(cars$speed)$out))
boxplot(cars$dist,main="Distance",sub=paste("Outlier rows:",boxplot.stats(cars$dist)$out))
# library(e1071) #for skewness
par(mfrow=c(1,2))
plot(density(cars$speed),main="Density Plot:speed",ylob="frequency",sub=paste("skewness:",round(e1071::skewness(cars$speed),2)))
cor(cars$speed,cars$dist)
linearMode<-lm(dist~speed,data=cars )
print(linearMode)
dist = -17.579+3.932*speed
summary(linearMode)