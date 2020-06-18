# Function Interpolation on Python using Genetic Algorithm

Point function interpolation using genetic algorithm

## Using
```
>>> from main import GenAlg
```
-----
```
>>> GenAlg(x, y, power_polynom, step=1, tol=0.001, childs=10)
```
> x - x coord
> y - y coord
> power_polynom - power of expected polynom
> step - start step of algorithm
> tol - max error before stop
> childs - number of childrens

-----
```
>>> GenAlg.calculate()
```
> Interpolate function
-----
```
>>> GenAlg.plot()
```
> Plot result function

## Example
```
>>> from main import GenAlg
>>> x = [0, -1, 1]  # x coord
>>> y = [1, 2, 2]  # y coord
>>> power_polynom = 3  # power of polynom
>>> cl = GenAlg(x, y, power_polynom)
>>> cl.calculate()
best error - 0.0009477044271553048
function: + 1.0024014141335753*x**0 + -0.0001327670274979374*x**1 + 0.9973777362924794*x**2 
>>> cl.plot()
```
