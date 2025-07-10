from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = [
    Extension(name="pipeline", sources=["pipeline.pyx"]),
    Extension(name="pipeline_parallel", sources=["pipeline_parallel.pyx"]),
]

setup(
    ext_modules=cythonize(extensions, language_level=3)
)
