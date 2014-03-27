# from: http://stackoverflow.com/questions/11059104/given-a-2d-numeric-height-map-matrix-in-r-how-can-i-find-all-local-maxima
library(raster)

## Construct an example matrix
set.seed(444)
msize <- 10
x <- matrix(sample(seq_len(msize), msize^2, replace=TRUE), ncol=msize)

## Convert it to a raster object
r <- raster(x)
extent(r) <- extent(c(0, msize, 0, msize) + 0.5)

## Find the maximum value within the 9-cell neighborhood of each cell
f <- function(X) max(X, na.rm=TRUE)
localmax <- focal(r, fun = f, pad=TRUE, padValue=NA)

## Does each cell have the maximum value in its neighborhood?
r2 <- r==localmax

## Get x-y coordinates of those cells that are local maxima
maxXY <- xyFromCell(r2, Which(r2==1, cells=TRUE))
head(maxXY)
#       x  y
# [1,]  8 10
# [2,] 10 10
# [3,]  3  9
# [4,]  4  9
# [5,]  1  8
# [6,]  6  8

# Visually inspect the data and the calculated local maxima
plot(r)   ## Plot of heights
windows() ## Open a second plotting device
plot(r2)  ## Plot showing local maxima