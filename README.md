# Lab_Python-Lib

Steps for Building 

### Install Dependencies

```
pip3 install -r requirements.txt
```

### Build 

```
hatch build -t sdist
hatch build -t wheel
```

### Deploy Local

```
pip3 install dist/my_hw-0.0.1-py3-none-any.whl --force-reinstall
```

#### Test

Get Package Info: 
```
pip3 show my-hw
```

Execute: 
```
hello-world
```

> ¡Hello, world from a python package!
