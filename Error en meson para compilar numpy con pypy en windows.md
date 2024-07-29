# Error en meson para compilar numpy con pypy en windows

En Windows en que se instaló un ambiente  virtual con `pypy` Versión 7.3.16 (equivalente ambiente Python 3.10), intenta instalar el paquete `numpy`, falla la compilación por un problema en el instalador `meson`.

|   Módulo    |   Version   | Tipo instalación |
|:-----------:|------------:|:----------------:|
|meson        |1.5.0        | pip              |

## Reporte de errores en repositorio

- Unhandled python exception when installing numpy with pypy on Windows: [issue #12979](https://github.com/mesonbuild/meson/issues/12979) - **Cerrada**.

  - Commit *compilers: fix crash when compiler check returns None output* [commit #7cec299](https://github.com/mesonbuild/meson/commit/7cec2997c596a5b99790aac68d9979a682c2a4ea).

    Con la corrección consistió en verificar que si el texto era vacío para Alguno de los streams out y error, se devolviera un objeto `None`.

    Detalles:

    ```markdown
      Popen_safe_logged has a small inefficiency. It evaluates the stripped
      version of stdout/stderr before checking if it exists, for logging
      purposes. This would sometimes crash, if it was None instead of ''.

      Fixes #12979

      (cherry picked from commit c99fc40)
    ```
  - Pull *Misc fixes*: [pull #13017](https://github.com/mesonbuild/meson/pull/13017).

    Discusión sobre la corrección del error.

  - En mensaje de [mattip del 25 Mar](https://github.com/mesonbuild/meson/issues/12979#issuecomment-2018511954):  
  Se consulta  por el resultado de la llamada siguiente, si está en `UTF-8` o no.
  
  ```cmd
  "C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vswhere.exe" -latest -prerelease -requiresAny -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -requires Microsoft.VisualStudio.Workload.WDExpress -products * -utf8 -format json
  ```

  La gran pregunta que hay que hacer es ¿en que ambiente? o más bien si la codificación es distinta según los ambientes o programas invocados.

- Unhandled python exception when configuring project with MSVC backend: [issue #12935](https://github.com/mesonbuild/meson/issues/12935) - **Abierta**.

  Creo que en la causa el error era igual o similar al error original del issue \#12979, y que debería cerrarse ambas al corregir el problema.

- Tracking issue: Windows handling of unicode is buggy: [issue #3890](https://github.com/pypy/pypy/issues/3890) - **Abierta**.

  Muestra diferencia de comportamiento entre PyPy y CPython a la hora de crear un directorio con caracteres unicode como `ş`.
  
  **Creo que a este issue es al que debería postear los experimentos de comportamientoss diferentes entre ambientes.**

## Problemas actuales

- detect.py, [línea 330](https://github.com/mesonbuild/meson/blob/master/mesonbuild/compilers/detect.py#L330)

- universal.py, [línea 1419](https://github.com/mesonbuild/meson/blob/5022fd30e1a922ad7f2dfc81648d3c73c5f2aa22/mesonbuild/utils/universal.py#L1419)

## Documentación posibles soluciones

### Codificación unicode en Windows

- Post sobre diferencias en manejo de unicode entre powershell y windows powershell: [Respuesta clave](https://stackoverflow.com/a/68106198/17892898) 

- Post sobre codificacion UTF-8 en variables en powershell: [set {Console}::OutputEncoding] to match the encoding used by the external program](https://stackoverflow.com/a/58438716/17892898)

- Post  sobre comportamiento de powershell: [comprehensive overview of how PowerShell interacts with external programs, which includes sending data to them](https://stackoverflow.com/questions/59110563/different-behaviour-and-output-when-piping-in-cmd-and-powershell/59118502#59118502)

- Documentación de codificación unicode en PowerShell en Microsoft: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-7.4>

- Búsqueda google: ["powershell capture standard output and error in different files"](https://www.google.com/search?q=powershell+capture+standard+output+and+error+in+different+files)

### Detección y conversión de textos unicode en windows

- convertir `utf-*` en CLI <https://superuser.com/questions/1786434/convert-utf-16-le-to-utf-8-in-windows-via-command-line>

- Explicación de uso programa ´iconv`: [Converting Unicode to UTF-8 Using Console Tools in Linux](https://www.baeldung.com/linux/unicode-utf-8-conversion)

## Documentación modulos en Python 3.10

- Artículo sobre uso de módulo `subprocess` : <https://realpython.com/python-subprocess/#basic-usage-of-the-python-subprocess-module>

- `subprocess.Popen()` <https://docs.python.org/3.10/library/subprocess.html#subprocess.Popen>

- `subprocess.Popen.communicate()` <https://docs.python.org/3.10/library/subprocess.html#subprocess.Popen.communicate>

- Guía de como migrar `os.popen` a `subprocess`: PEP0324 <https://peps.python.org/pep-0324/#replacing-os-popen>

- Python HOWTO Unicode  <https://docs.python.org/3.10/howto/unicode.html>

- `unicodedata.normalize()` <https://docs.python.org/3.10/library/unicodedata.html#unicodedata.normalize>

- Módulo `codecs` <https://docs.python.org/3.10/library/codecs.html#standard-encodings>
