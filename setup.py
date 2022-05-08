from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='zero-shot-re',
      version='0.0.4',
      url='http://github.com/fractalego/zero-shot-relation-extractor',
      author='Alberto Cetoli',
      author_email='alberto@nlulite.com',
      description="A zero-shot relation extractor",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['zero_shot_re',
                ],
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      include_package_data=True,
      zip_safe=False)
