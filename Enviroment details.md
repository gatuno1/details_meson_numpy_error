# Environment for test

## System and OS

- Windows 11 23H2 compilation.  
  Execute: `winver.exe`

- Ubuntu 22.04 LTS on WSL 2.2.4 VM.  
  Execute: `wsl.exe --version`
  <details>

  ```cmd
  Versión de WSL: 2.2.4.0
  Versión de kernel: 5.15.153.1-2
  Versión de WSLg: 1.0.61
  Versión de MSRDC: 1.2.5326
  Versión de Direct3D: 1.611.1-81528511
  Versión DXCore: 10.0.26091.1-240325-1447.ge-release
  Versión de Windows: 10.0.22631.3880
  ```

  </details>

  Execute: `lsb_release -a` on WSL2 running session (ex. `wsl.exe -d Ubuntu`).
  <details>

  ```bash
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 22.04.4 LTS
  Release:        22.04
  Codename:       jammy
  ```

  </details>

## Command host programs

- cmd.exe - Default version 10.0.22631.3880 installed.  
  Execute: `cmd.exe -v`

- Windows Powershell - Default version 5.1.22621.3880 installed.  
  Execute: `powershell.exe -c "$PSVersionTable"`
  <details>

  ```cmd
  Name                           Value
  ----                           -----
  PSVersion                      5.1.22621.3880
  PSEdition                      Desktop
  PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
  BuildVersion                   10.0.22621.3880
  CLRVersion                     4.0.30319.42000
  WSManStackVersion              3.0
  PSRemotingProtocolVersion      2.3
  SerializationVersion           1.1.0.1
  ```

  I<details>

- Terminal Windows - Version: 1.20.11781.0 installed from Microsoft Store.  
  Execute: `wt.exe --version`

- zsh command interpreter version 5.8.1, running on Ubuntu WSL virtual machine.  
  Execute: `zsh --version`

  ```bash
  zsh 5.8.1 (x86_64-ubuntu-linux-gnu)
  ```

## Python interpreters for Windows

- PyPy is installed globally on `"C:\Program Files\PyPy\pypy3.10-v7.3.16-win64\"` and present in system environment variable `$PATH`.  
  Downloaded from official site: <https://pypy.org/download.html>.  
  Execute: `pypy -V`
  <details>

  ```cmd
  Python 3.10.14 (75b3de9d9035, Apr 21 2024, 13:13:38)
  [PyPy 7.3.16 with MSC v.1929 64 bit (AMD64)]
  ```

  <details>

- Anaconda Python instalation version 3.11.7 (64 bits), installed only for user profile, and not in system environment variables.  
  Donwloaded from official site: <https://www.anaconda.com/download/success>.  
  Execute: `conda -info`
  <details>

  ```cmd
         active environment : None
              shell level : 0
         user config file : C:\Users\Antonio\.condarc
   populated config files : C:\Users\Antonio\.condarc
            conda version : 24.5.0
      conda-build version : 24.1.2
           python version : 3.11.7.final.0
                   solver : libmamba (default)
         virtual packages : __archspec=1=x86_64_v3
                            __conda=24.5.0=0
                            __win=0=0
         base environment : C:\Users\Antonio\anaconda3  (writable)
        conda av data dir : C:\Users\Antonio\anaconda3\etc\conda
    conda av metadata url : None
             channel URLs : <https://repo.anaconda.com/pkgs/main/win-64>
                            <https://repo.anaconda.com/pkgs/main/noarch>
                            <https://repo.anaconda.com/pkgs/r/win-64>
                            <https://repo.anaconda.com/pkgs/r/noarch>
                            <https://repo.anaconda.com/pkgs/msys2/win-64>
                            <https://repo.anaconda.com/pkgs/msys2/noarch>
                            <https://conda.anaconda.org/conda-forge/win-64>
                            <https://conda.anaconda.org/conda-forge/noarch>
            package cache : C:\Users\Antonio\anaconda3\pkgs
                            C:\Users\Antonio\.conda\pkgs
                            C:\Users\Antonio\AppData\Local\conda\conda\pkgs
         envs directories : C:\Users\Antonio\anaconda3\envs
                            C:\Users\Antonio\.conda\envs
                            C:\Users\Antonio\AppData\Local\conda\conda\envs
                 platform : win-64
               user-agent : conda/24.5.0 requests/2.31.0 CPython/3.11.7 Windows/10 Windows/10.0.22631 solver/libmamba conda-libmamba-solver/24.1.0 libmambapy/1.5.6 aau/0.4.3 c/CZvsdkbdKKdrUus-rcgesA s/AGA59FCFw1VSLGZBWYkonw e/sWoh93ZmX0nDFMyZmc9vRw
            administrator : False
               netrc file : None
             offline mode : False
  ```

  </details>
