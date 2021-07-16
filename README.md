### run-code-securely


# What is run-code-securely?
run-code-securely is a python package to run python3 code securely using the Piston API.


## Examples

# Example 1

For example, let's say that you want to run `print('hello world')` with the <bold>3.7.0 version of Python.</bold>
<small>*Note the single quotes.*</small>

The following code can do that.

```python3

import run-code-securely

run-code-securely.run("print('hello world')", 3.7.0)
```