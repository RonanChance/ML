from keras.datasets import mnist
# mnist is the 'modified national institute of standards and technology database'

import matplotlib.pyplot as plt
# matplotlib pyplot is how we can plot our data in a visual way

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten


# Going to download the mnist data, then split into training and testing sets.

(X_train, y_train), (X_test, y_test) = mnist.load_data()


# Let's plot the first image and check it
plt.imshow(X_train[0])

# Let's check the shape of the image
print(str(X_train[0].shape))

# Reshape our data to fit the model
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print(y_train[0])


# Creating our model
model = Sequential()

# Adding model layers
model.add(Conv2D(64, kernel_size = 3, activation= 'relu', input_shape = (28, 28, 1)))
model.add(Conv2D(32, kernel_size = 3, activation = 'relu'))
model.add(Flatten())
model.add(Dense(10, activation = 'softmax'))

# Compile our model
model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 1)

print(model.predict(X_test[:4]))


