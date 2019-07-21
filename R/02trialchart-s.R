library(highcharter)
library(rCharts)
library(tidyr)
library(dplyr)
library(RColorBrewer)

## 
gender_df <- total_df %>% gather(key = "gender",value = "population","male","female")



##rcharts
hair_eye_male <- subset(as.data.frame(HairEyeColor), Sex == "Male")
n1 <- nPlot(Freq ~ Hair, group = "Eye", data = hair_eye_male, 
            type = 'multiBarChart')
n1

chart <- nPlot(population ~ state, color = cols, group = "gender", data = gender_df,
               type = 'multiBarChart')
chart



cols <- brewer.pal(n = 2, name = "Set1")
hchart(gender_df, "column", hcaes(x = state, y = population, group = gender)) %>% 
  hc_colors(cols)


pop_house_df <- total_df %>% gather(key = "type",value = "n",-state,-male,-female)

hchart(pop_house_df,"column", hcaes(x= state, y = n, group = type)) %>% hc_colors(cols)
