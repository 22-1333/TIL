import matplotlib.pyplot as plt

# practice_1: if x, y are the same
plt.plot([1, 2, 3, 4])
plt.show()

# erase the former plot
plt.clf()

# practice_2: if x, y are not the same
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
plt.show()

# practice_3: title + detail
plt.plot(x, y)
# title
plt.title("Test Graph")
# x, y axis
plt.ylabel('y label')
plt.xlabel('x label')

plt.show()

# save as file - without plt.show()
plt.savefig('filename.png')