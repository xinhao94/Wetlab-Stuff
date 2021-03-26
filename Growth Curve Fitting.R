library(growthcurver)
library(Cairo)

sourcePath <- "Desktop/source1.csv"
d <- read.table(sourcePath, header = TRUE, sep = ",", stringsAsFactors = FALSE)
fitParams <- SummarizeGrowthByPlate(d, plot_fit = TRUE, 
                                    plot_file = "Fit_Curves.pdf")
fitParams