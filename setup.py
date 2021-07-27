from distutils.core import setup

setup(
    name='cvzone',
    packages=['cvzone'],
    version='1.3.0',
    license='MIT',
    description='Computer Vision Helping Library',
    author=' NEW Computer Vision Zone',
    author_email='Georgge.naishel208@gmail.com',
    url='https://github.com/cvzone/cvzone',
    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation'],
    install_requires=[
        'opencv-python',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)