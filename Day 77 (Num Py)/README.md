# NumPy and N-Dimensional Arrays

A comprehensive Jupyter notebook covering NumPy fundamentals including array creation, manipulation, mathematical operations, broadcasting, and working with multi-dimensional data. Includes practical examples with images and real-world datasets.

## Features

- **Array Basics**: Creating 1D, 2D, and 3D arrays
- **Array Operations**: Mathematical operations, broadcasting, and vectorization
- **Indexing & Slicing**: Access and modify array elements
- **Array Manipulation**: Reshape, transpose, flatten, and stack arrays
- **Mathematical Functions**: Trigonometry, statistics, linear algebra
- **Image Processing**: Work with images as NumPy arrays
- **Performance**: Understand why NumPy is faster than Python lists
- **Broadcasting**: Automatic array shape manipulation for operations

## How to Use

1. Install required dependencies:
   ```bash
   pip install jupyter numpy matplotlib scipy pillow
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `Computation_with_NumPy_and_N_Dimensional_Arrays_(start).ipynb`

4. Run cells sequentially to learn NumPy concepts

5. Experiment with code examples

## Dataset & Images

### Files Included
- **`yummy_macarons.jpg`**: Sample image for array manipulation exercises
- **SciPy datasets**: Built-in raccoon image for practice

### Image as Array Concept
- Images are 3D arrays (height × width × color channels)
- RGB images have 3 channels (Red, Green, Blue)
- Each pixel is represented by values 0-255
- NumPy enables direct pixel manipulation

## Topics Covered

### 1. Understanding NumPy Arrays (ndarray)
- What are NumPy arrays and why use them
- Arrays vs Python lists
- Speed and memory advantages
- Creating arrays from lists
- Array attributes (shape, dtype, size, ndim)

### 2. 1-Dimensional Arrays (Vectors)
- Creating vectors
- Mathematical operations (+, -, *, /)
- Dot products
- Vector norms
- Element-wise operations

### 3. 2-Dimensional Arrays (Matrices)
- Creating matrices
- Matrix operations
- Matrix multiplication
- Transpose operations
- Identity and zero matrices

### 4. 3-Dimensional Arrays (Tensors)
- Understanding tensor structure
- Creating 3D arrays
- Image representation
- Channel manipulation
- Tensor operations

### 5. Array Creation Methods
- `np.array()`: From Python lists
- `np.arange()`: Range of values
- `np.linspace()`: Evenly spaced values
- `np.zeros()`: Array of zeros
- `np.ones()`: Array of ones
- `np.eye()`: Identity matrix
- `np.random`: Random arrays

### 6. Indexing and Slicing
- Single element access
- Row and column selection
- Slicing syntax [start:stop:step]
- Boolean indexing
- Fancy indexing with arrays

### 7. Array Manipulation
- `reshape()`: Change array dimensions
- `flatten()`: Convert to 1D
- `ravel()`: Flattened view
- `transpose()`: Switch dimensions
- `concatenate()`: Join arrays
- `stack()`: Stack arrays along axis

### 8. Mathematical Operations
- Element-wise operations
- Aggregate functions (sum, mean, std)
- Min/max and argmin/argmax
- Trigonometric functions
- Exponential and logarithmic
- Statistical functions

### 9. Broadcasting
- Automatic shape matching
- Operating on differently shaped arrays
- Broadcasting rules
- Common broadcasting patterns

### 10. Working with Images
- Loading images with PIL
- Converting images to arrays
- Manipulating RGB channels
- Image arithmetic
- Creating image filters
- Saving modified images

## Technical Details

### Libraries Used
- **NumPy**: Core numerical computing library
- **Matplotlib**: Displaying images and plotting
- **SciPy**: Additional datasets (raccoon image)
- **PIL (Pillow)**: Image file I/O

### Key NumPy Concepts

**Array Properties**:
- `shape`: Dimensions of array
- `dtype`: Data type of elements
- `size`: Total number of elements
- `ndim`: Number of dimensions

**Performance Advantages**:
- Vectorized operations (no loops)
- Contiguous memory layout
- Efficient C implementation
- Broadcasting eliminates explicit loops
- 10-100x faster than Python lists

**Memory Layout**:
- Row-major (C-style) by default
- Contiguous memory blocks
- Efficient for mathematical operations
- Views vs copies

## File Structure

```
Day 77 (Num Py)/
├── Computation_with_NumPy_and_N_Dimensional_Arrays_(start).ipynb
├── yummy_macarons.jpg
└── .DS_Store
```

## Learning Concepts

### Computational Efficiency
- Vectorization vs loops
- Memory efficiency
- Computational complexity
- Benchmarking operations

### Array Mathematics
- Linear algebra foundations
- Matrix operations
- Vector operations
- Tensor operations

### Data Manipulation
- Reshaping data for algorithms
- Flattening and unflattening
- Transposing dimensions
- Combining arrays

### Image Processing Basics
- Image representation
- Color channel manipulation
- Pixel-level operations
- Image transformations

## Practical Examples in Notebook

### Basic Operations
```python
# Create array
arr = np.array([1, 2, 3, 4, 5])

# Mathematical operations
arr * 2  # Multiply all elements
np.sqrt(arr)  # Square root
arr.mean()  # Average
```

### Matrix Operations
```python
# Create matrix
matrix = np.array([[1, 2], [3, 4]])

# Operations
matrix.T  # Transpose
matrix @ matrix.T  # Matrix multiplication
np.linalg.inv(matrix)  # Inverse
```

### Image Manipulation
```python
# Load image
from PIL import Image
img = Image.open('yummy_macarons.jpg')
img_array = np.array(img)

# Manipulate
red_channel = img_array[:, :, 0]  # Extract red
img_array[:, :, 2] = 0  # Remove blue channel
```

### Broadcasting Example
```python
# Add scalar to array (broadcasting)
arr = np.array([1, 2, 3])
arr + 10  # [11, 12, 13]

# Add row to matrix
matrix = np.array([[1, 2], [3, 4]])
row = np.array([10, 20])
matrix + row  # Adds row to each row of matrix
```

## Requirements

- Python 3.x
- Jupyter Notebook
- numpy (numerical computing)
- matplotlib (visualization)
- scipy (scientific computing)
- pillow (image processing)

## Environment Setup

### Windows (PowerShell):
```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install jupyter numpy matplotlib scipy pillow
jupyter notebook
```

### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jupyter numpy matplotlib scipy pillow
jupyter notebook
```

## How the Code Works

1. **Introduction**: Overview of NumPy and its advantages
2. **Array Creation**: Different methods to create arrays
3. **Basic Operations**: Mathematics on arrays
4. **Indexing**: Accessing array elements
5. **Manipulation**: Reshaping and transforming arrays
6. **Advanced Operations**: Broadcasting and vectorization
7. **Image Processing**: Working with images as arrays
8. **Performance**: Comparing NumPy to Python lists

## Real-World Applications

### Scientific Computing
- Physics simulations
- Mathematical modeling
- Statistical analysis
- Signal processing

### Data Science
- Feature engineering
- Data preprocessing
- Matrix operations for ML
- Batch processing

### Image Processing
- Computer vision
- Image filters
- Color manipulation
- Image transformation

### Machine Learning
- Neural network operations
- Matrix computations
- Batch normalization
- Gradient calculations

## Next Steps/Improvements

- Add more complex linear algebra operations
- Explore NumPy's random number generation
- Practice with larger datasets
- Implement custom image filters
- Study NumPy memory management
- Learn about structured arrays
- Explore NumPy's C API
- Practice with sparse matrices
- Study numerical optimization
- Learn about masked arrays

Perfect for learning NumPy fundamentals, array operations, vectorization, image processing basics, and building a foundation for data science and machine learning!
