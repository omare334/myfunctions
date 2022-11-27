#running assumptions plots
function(model){
  assumptions<-ols_plot_cooksd_bar(model)
  ols_plot_dfbetas(model)
  ols_plot_resid_qq(model)
  ols_plot_resid_fit(model)
  plot(model)
  bptest(model)
  
}
#plotting linear regression 
function(a,b,z){
  linearregressionplot<-ggplot(z, aes(x = a, y = b)) +
    geom_point() +
    geom_parallel_slopes(se = TRUE) +
    labs(x = a, y = b)
  return(linearregressionplot)
  
}
#making ny-times table summary
function(table){
  nytimestable<-broom::tidy(summary(table))%>%
    setDT()%>%
    head() %>% 
    gt() %>% 
    gt_theme_nytimes()
  return(nytimestable)
}
#new york times durbin-watson summary
function(table){
  dwtest<-broom::tidy(durbinWatsonTest(table))%>%
    setDT()%>%
    head() %>% 
    gt() %>% 
    gt_theme_nytimes()
  return(dwtest)
}
#new york times breusch pagan test
function(table){
  bptest1<-broom::tidy(bptest(table))%>%
    setDT()%>%
    head() %>% 
    gt() %>% 
    gt_theme_nytimes()
  return(bptest1)
}
#qqplot of linear regression 
function(x){
  plotofx<-qqnorm(x, pch = 1, frame = FALSE)
  qqline(x, col = "steelblue", lwd = 2)
  return(plotofx)
}
#finding confidence interval for binomial T=case F=no case
function(df, die){
  ci <- NULL
  if(die) {
    table<-df %>% table() %>% data.frame ()
    ci<-prop.test(x= table [2,2], n=(length(df)), conf.level=.95, correct=FALSE)
  } else {
    table<-df %>% table() %>% data.frame ()
    ci<-prop.test(x= table [1,2], n=(length(df)), conf.level=.95, correct=FALSE)
  }
  return(ci)
}
#risk difference calculation 
function(x,y){
  t<-table(x,y) %>% data.frame ()
  a<-t[3,3]
  b<-t[4,3]
  no<-t[1,3]+t[3,3]
  n1<-t[2,3]+t[4,3]
  exposed<-riskdifference(a, b, no, n1, CRC=TRUE, conf.level=0.95)
  return(exposed)
}
