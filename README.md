# Fetal Health Dataset Analysis

COM725 AE2 Assessment

## How to run

You can utilise Makefile if you are running on MacOs, else you may either have to do the steps below or install make on your Windows/Linux.

### With Makefile

```bash
conda create --name data python

make install

make run
```

### Without Makefile

```bash
conda create --name data python

pip install -r requirements.txt

python src
```

## Important

You must use ```Python 3.10``` as ```typing``` with the new Union operator is used throughout this project.
