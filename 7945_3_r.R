library(readxl)
library(dplyr)
df<- read_excel('C:/Users/prathyusha.gandi/Downloads/SaleData.xlsx')
#Q1 Find least sales amount for each item
q1<-function(dataframe)
{
  return(aggregate(dataframe[,"Sale_amt"], list(dataframe$Item), min))
}
q1(df)
# Q2 compute total sales at each year X region
q2<-function(dataframe)
{
dataframe['year']=format(as.Date(dataframe$OrderDate, format="%m/%d/%Y"),"%Y")
return(aggregate(dataframe[,'Sale_amt'], list(dataframe$year,dataframe$Region), sum))
}
q2(df)
# Q3 append column with no of days difference from present date to each order date
df$OrderDate <- as.Date(df$OrderDate,format="%m/%d/%y")
q3<-function(dataframe)
 {
   dataframe$days_diff <- (Sys.Date() - dataframe$OrderDate)
   return(dataframe)
 }
 q3(df)
 # Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
 q4<-function(dataframe)
 {
   dataframe1<-aggregate((dataframe['SalesMan']), list(dataframe$Manager), unique)
   colnames(dataframe1)[1]<-"manager"
   colnames(dataframe1)[2]<-"list_of_salesmen"
   return(dataframe1)
 }
 q4(df)
 # Q5 For all regions find number of salesman and number of units
 q5<-function(dataframe)
 {
   dataframe1<-aggregate((dataframe['Units']), list(dataframe$Region), sum)
   dataframe2<-aggregate((dataframe['SalesMan']), list(dataframe$Region),unique)
   dataframe2$new_col<-length(dataframe2$SalesMan)
   a<-list(dataframe1,dataframe2)
   return(a)
   }
 q5(df)
 # Q6 Find total sales as percentage for each manager
 
 q6<-function(dataframe)
 {
   dataframe1<-aggregate((dataframe["Sale_amt"]),list(dataframe$Manager),sum)
   s<-sum(dataframe$Sale_amt)
   dataframe1["sales_percent"]<-(dataframe1["Sale_amt"]/s)*100
   return(dataframe1)
 }
q6(df)
df2<-read.csv("C:/Users/prathyusha.gandi/Downloads/imdb.csv")
#Q7 get imdb rating for fifth movie of dataframe
q7<-function(dataframe)
{
  return(dataframe[5,c('imdbRating')]) 
}
q7(df2)
#Q8 return titles of movies with shortest and longest run time
q8<-function(dataframe)
{
  mini=dataframe$title[which.min(dataframe$duration)]
  maxi=dataframe$title[which.max(dataframe$duration)]
  a=list(mini,maxi)
  return(a)
}
q8(df2)
# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)

q9<-function(dataframe)
{
  dataframe$year <- as.numeric(as.character(dataframe$year))
  dataframe$imdbRating <- as.numeric(as.character(dataframe$imdbRating))
  dataframe1=dataframe[order(dataframe["year"], -dataframe["imdbRating"]),]
  return(dataframe1)
}
q9(df2)
# 10. Subset the dataframe with movies having the following prameters. revenue more than 2 million spent less than 1 million duration between 30 mintues to 180 minutes 
df1<-read.csv("C:/Users/prathyusha.gandi/Downloads/movie_metadata.csv")
q10<-function(df)
{
  df<-subset(df,(duration>30)&(duration<180)&(gross>2000000)&(budget<1000000))
  return(df)
}
q10(df1)

df3<-read.csv("C:/Users/prathyusha.gandi/Downloads/diamonds.csv")
# Q11 count the duplicate rows of diamonds DataFrame.
q11<-function(dataframe)
{
  return(nrow(dataframe)-nrow(unique(dataframe)))
}
q11(df3)
# Q12 droping those rows where any value in a row is missing in carat and cut columns
q12<-function(dataframe)
{
  dataframe<-dataframe[complete.cases(dataframe[ , 1:2]),]
  return(dataframe)
}
q12(df3)
# Q13 subset only numeric columns
q13<-function(dataframe)
{
  data<-select_if(dataframe,is.numeric)
  return(data)
}
q13(df3)
# Q14 compute volume as (x*y*z) when depth > 60 else 8
q14<-function(dataframe)
{
  dataframe$z<-as.numeric(as.character(dataframe$z))
  dataframe$z[is.na(dataframe$z)] <- 0
  vol<-dataframe$x*dataframe$y*dataframe$z
  dataframe$volume<-ifelse(dataframe$depth>60,vol,8)
  return(dataframe)
}
q14(df3)
#Q15 impute missing price values with mean
q15<-function(dataframe)
{
 dataframe$price<-ifelse(is.na(dataframe$price), mean(dataframe$price, na.rm = TRUE),dataframe$price)
return(dataframe)
}
q15(df3)
 


 
 
 
 