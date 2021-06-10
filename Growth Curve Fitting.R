library(growthcurver)
library(Cairo)

sourcePath <- "/Users/xinhao/Desktop/20210608_Source.csv"
d <- read.table(sourcePath, header = TRUE, sep = ",", stringsAsFactors = FALSE)
fitParams <- SummarizeGrowthByPlate(d, plot_fit = TRUE, 
                                    plot_file = "20210608_Fit_Curves.pdf")
fitParams

outputPath <- "/Users/xinhao/Desktop/20210608_Fit_Params.csv"
write.table(fitParams, file = outputPath, 
            quote = FALSE, sep = ",", row.names = FALSE)
