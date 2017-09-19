from pylab import imread,subplot,imshow,title,gray,figure,show,NullLocator
import pca_fn
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('chart.png')
implot=plt.imshow(img)

A = imread('chart.png') # load an image
A = mean(A,2) # to get a 2-D array
full_pc = size(A,axis=1) # numbers of all the principal components
i = 1
dist = []
for numpc in range(0,full_pc+10,10): # 0 10 20 ... full_pc
 coeff, score, latent = princomp(A,numpc)
 Ar = dot(coeff,score).T+mean(A,axis=0) # image reconstruction
 # difference in Frobenius norm
 dist.append(linalg.norm(A-Ar,'fro'))
 # showing the pics reconstructed with less than 50 PCs
 if numpc <= 50:
  ax = subplot(2,3,i,frame_on=False)
  ax.xaxis.set_major_locator(NullLocator()) # remove ticks
  ax.yaxis.set_major_locator(NullLocator())
  i += 1 
  imshow(flipud(Ar))
  title('PCs # '+str(numpc))
  gray()

figure()
imshow(flipud(A))
title('numpc FULL')
gray()
show()