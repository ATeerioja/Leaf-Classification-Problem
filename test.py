from skimage import io, filters
import numpy as np

image = np.random.rand(100, 100)
edges = filters.sobel(image)

print(edges.shape)