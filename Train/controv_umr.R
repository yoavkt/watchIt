#Code for finding most interesting movies to show

umr_matrix <- read.csv("C:/Users/ylazar/Dropbox/DataHack/Train/umr_matrix.csv", header=F)
umr_matrix <- umr_matrix[-1,]
umr_matrix <- data.matrix(umr_matrix, rownames.force = NA)
umr_matrix[umr_matrix==0] <- 3
umr_matrix <- umr_matrix-3
#?View(umr_matrix)

ups <- vector()
downs <- vector()
for(i in 1:dim(umr_matrix)[2]){
  ups[i] <- sum(umr_matrix[,i][umr_matrix[,i]>0])
  downs[i] <- sum(abs(umr_matrix[,i][umr_matrix[,i]<0]))
}

controversy <- vector()
magnitude <- colSums(abs(umr_matrix))
for(i in 1:dim(umr_matrix)[2]){
  if (ups[i]<=0 || downs[i]<= 0) {
    controversy[i] <- 0
  } else if (ups[i] > downs[i]) {
    controversy[i] <- magnitude[i]*ups[i]/downs[i]
  } else {
    controversy[i] <- magnitude[i]*downs[i]/ups[i]
  } 
}
sort(controversy, index.return=1)$ix
umr_matrix[,480][umr_matrix[,480] != 0]