## Length of vector

$$\text{Vector:} \space v = [v_1,v_2,..., v_n]^T$$
$$\text{Legnth of a vector: }\space ||v|| = \sqrt{v_1^2 + v_1^2 + ... +v_n^2}$$

* Example 
```markdown
>>> v = np.array([1,2,3,4])
>>> v
[1 2 3 4]
>>> np.linalg.norm(v)
5.477225575051661
```
```markdown 
def compute_length_vector(vector):
    return np.sqrt(np.sum(vector*vector))

>>> print(compute_length_vector(v))
5.477225575051661
```

## Dot Product between two vector 

$$
\text{Vector: } \quad v = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}, \quad u = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix}
$$

$$
\text{Dot Product: } \quad v \cdot u = v_1 u_1 + v_2 u_2 + \cdots + v_n u_n = \sum_{i=1}^{n} v_i u_i
$$


```markdown
>>> a = np.array([2,3,4])
>>> b = np.array([5,6,7])
>>> print(np.dot(a,b))
56 
```

```markdown
def compute_dot_vector(vector1, vector2):
    return np.sum(vector1* vector2)

>>> print(compute_dot_vector(a,b))
56
```

## Multiplying a Vector by a Matrix

$$
\text{Matrix } A = \begin{bmatrix} 
a_{11} & \cdots & a_{1n} \\ 
\vdots & \ddots & \vdots \\ 
a_{m1} & \cdots & a_{mn} 
\end{bmatrix}, \quad A \in \mathbb{R}^{m \times n}
$$

$$
\text{Vector: } \quad v = \begin{bmatrix} 
v_1 \\ 
v_2 \\ 
\vdots \\ 
v_n 
\end{bmatrix}, \quad v \in \mathbb{R}^{n}
$$

$$
c = Av = \begin{bmatrix} 
a_{11}v_1 + \cdots + a_{1n}v_n \\ 
\vdots \\ 
a_{m1}v_1 + \cdots + a_{mn}v_n 
\end{bmatrix}
$$

## Matrix Inverse

$$
\text{Matrix } \mathbf{A} = \begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}, \quad \mathbf{A} \in \mathbb{R}^{2 \times 2}
$$

$$
\text{Determinant of } \mathbf{A} \in \mathbb{R}^{2 \times 2} : \det(\mathbf{A}) = ad - bc
$$

$$
\text{if } \det(\mathbf{A}) \neq 0 \text{, A is invertible}
$$

$$
\text{Inverse Matrix } \mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{bmatrix} 
d & -b \\ 
-c & a 
\end{bmatrix}
$$

## Eigenvalue and Eigenvector 

$$
\mathbf{A} \in \mathbb{R}^{n \times n}, \quad \mathbf{I} \text{ (identity matrix) } \in \mathbb{R}^{n \times n}, \quad v \in \mathbb{R}^{n}
$$

$$
\text{Eigenvalue } (\lambda): \det (\mathbf{A} - \lambda \mathbf{I}) = 0
$$

$$
\text{Eigenvector } (v): \quad \mathbf{A}v = \lambda v \iff (\mathbf{A} - \lambda \mathbf{I})v = 0
$$

$$
\text{Normalize vector: } \frac{v}{||v||}, \quad v_i = \frac{v_{i}}{\sqrt{\sum_{i=1}^{n}v_{i}^2}}
$$


```python 
import numpy as np
matrix_a =np.array([[0.9,0.2],[0.1,0.8]])

eigenvalues, eigenvector  = np.linalg.eig(matrix_a)
print(f'Eigenvalue: \n{eigenvalues}')
print()
print(f'Eigenvector: \n{eigenvector}')
Eigenvalue: 
[1.  0.7]

Eigenvector:
[[ 0.89442719 -0.70710678]
 [ 0.4472136   0.70710678]]
```
