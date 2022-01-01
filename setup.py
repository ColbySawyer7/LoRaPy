from distutils.core import setup
setup(
  name = 'LoRaPy',         # How you named your package folder (MyLib)
  packages = ['LoRaPy'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implementation of the LoRaWAN intended to connect to the Things Network Stack (V2-V3)',   # Give a short description about your library
  author = 'Colby Sawyer',                   # Type in your name
  author_email = 'sawyerco21@ecu.edu',      # Type in your E-Mail
  url = 'https://github.com/ColbySawyer7/LoRaPy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ColbySawyer7/LoRaPy/archive/refs/tags/v_0.5.tar.gz',    # I explain this later on
  keywords = ['LoRaWAN', 'Lora', 'Things Network', 'TTN', 'v3'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'RPi.GPIO',
          'spidev',
          'argparse',
          'LoRaWAN',
          'spi-lora>=0.2.1',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
