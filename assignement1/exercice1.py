import imageio
vol = imageio.volread('data')
import matplotlib.pyplot as plt
fig, axes =plt.subplots(nrows=1, ncols=21)
axes[0].imshow(vol[0],cmap='gray')
axes[1].imshow(vol[1],cmap='gray')
axes[2].imshow(vol[2],cmap='gray')
axes[3].imshow(vol[3],cmap='gray')
axes[4].imshow(vol[4],cmap='gray')
axes[5].imshow(vol[5],cmap='gray')
axes[6].imshow(vol[6],cmap='gray')
axes[7].imshow(vol[7],cmap='gray')
axes[8].imshow(vol[8],cmap='gray')
axes[9].imshow(vol[9],cmap='gray')
axes[10].imshow(vol[10],cmap='gray')
axes[11].imshow(vol[11],cmap='gray')
axes[12].imshow(vol[12],cmap='gray')
axes[13].imshow(vol[13],cmap='gray')
axes[14].imshow(vol[14],cmap='gray')
axes[15].imshow(vol[15],cmap='gray')
axes[16].imshow(vol[16],cmap='gray')
axes[17].imshow(vol[17],cmap='gray')
axes[18].imshow(vol[18],cmap='gray')
axes[19].imshow(vol[19],cmap='gray')
axes[20].imshow(vol[20],cmap='gray')
for ax in axes:
    ax.axis('off')
plt.show()
# you have to stack these slices on top of each other, as in image1->image2->image-3