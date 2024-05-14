import cv2 as cv
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans as km


img = mpl.image.imread("image_02.jpg")
plt.imshow(img)
plt.show()

x = img.reshape(-1, 3)
print(x.shape)

kmeans = km(n_clusters=2)
kmeans.fit(x)

seg_img = kmeans.cluster_centers_[kmeans.labels_]
seg_img = seg_img.reshape(img.shape)
plt.imshow(seg_img / 255)

plt.show()