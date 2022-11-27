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