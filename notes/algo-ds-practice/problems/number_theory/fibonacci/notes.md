For proof, put the following in the math.stackExchange editor:

```
For $n>1$ you can recover  $F_n$ as the (1,0) component of
$$A^{n}=
\begin{pmatrix}1 & 1\\ 1& 0\end{pmatrix}^{n} =
\begin{pmatrix}F_{n+1} & F_{n}\\ F_{n}& F_{n-1}\end{pmatrix}$$

We know that $$A^{N} * A^{M} = A^{N+M}$$ that is by multiplying the matrices of $n^{th}$ and $m^{th}$ fibonacci numbers, we'll get the matrix of $(n+m)^{th}$ fibonacci.

Now putting $n$ =$m$ :
 $$A^{N} * A^{N} = A^{2N}$$


$$\begin{pmatrix}F_{n+1} & F_{n}\\ F_{n}& F_{n-1}\end{pmatrix}
\times \begin{pmatrix}F_{n+1} & F_{n}\\ F_{n}& F_{n-1}\end{pmatrix}
=\begin{pmatrix}F_{n+1}^2 + F_{n}^2 & F_{n}(F_{n+1}+ F_{n-1})\\ F_{n}(F_{n+1}+ F_{n-1}) & F_{n}^2 + F_{n-1}^2\end{pmatrix} = A^{2n} = \begin{pmatrix}F_{2n+1} & F_{2n}\\ F_{2n}& F_{2n-1}\end{pmatrix}
$$

For even indices, compare $(0,1)$ entry:

$$F_{2n} = F_{n}(F_{n+1}+ F_{n-1})$$

For odd indices, compare $(0,0)$ entry:

$$F_{2n+1} = F_{n+1}^2 + F_{n}^2$$
```
