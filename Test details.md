# Tests Details

I've done the test varying:

- System host: {Windows 11, Ubuntu 22.04 LTS in WSL2 host}.

- Host command processor {cmd, windows powershell, windows terminal, WSL}.

- Shell {cmd, anaconda enabled cmd, Powershell, anaconda enabled Powershell , zsh on WSL}.

| Case # | System Host | Host Command Processor | Shell |
|:------:|:------------|:-----------------------|:------|
| 1 | Windows | cmd ||
| 2 | 

1. `cmd.exe` with default python: **PyPy 7.3.16, as CPython 3.10.14**.

  Run two times: the first one gives this output, and the second time give something similar, but the function `os.path.exists()` seem to have an error when using a `b""` string.

  ```cmd
  Python version: 3.10.14 (75b3de9d9035, Apr 21 2024, 13:13:38)
  [PyPy 7.3.16 with MSC v.1929 64 bit (AMD64)]
  
  Directory b'fi\xc5\x9fier.dir' was not detected.
  Creating directory: b'fi\xc5\x9fier.dir'
  
  Deleting existing directory: fi├à┬ƒier.dir
  Creating directory: fi├à┬ƒier.dir
  
  Matching dirs: ['fi├à\x9fier.dir', 'fi┼ƒier.dir']
  ```

  ```cmd
  Python version: 3.10.14 (75b3de9d9035, Apr 21 2024, 13:13:38)
  [PyPy 7.3.16 with MSC v.1929 64 bit (AMD64)]
  
  Directory b'fi\xc5\x9fier.dir' was not detected.
  Creating directory: b'fi\xc5\x9fier.dir'
  Directory b'fi\xc5\x9fier.dir' already exists, so it was not created.
  
  Deleting existing directory: fi├à┬ƒier.dir
  Creating directory: fi├à┬ƒier.dir
  
  Matching dirs: ['fi├à\x9fier.dir', 'fi┼ƒier.dir']
  ```

  Results:
  - Directories `fişier.dir` and `fiÅier.dir` was created.