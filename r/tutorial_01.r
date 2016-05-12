#!/usr/bin/Rscript
X11()
x.vals = seq(-4,4,length=150)
plot(x.vals, dnorm(x.vals),type="l", lwd=2, col="blue", xlab="x", ylab="pdf")
invisible(readLines("stdin", n=1))
