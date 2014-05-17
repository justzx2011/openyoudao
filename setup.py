import os
import glob
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='openyoudao',
    version=0.3,
    description='A Youdao client for Linux',
    long_description=readme,
    author='justzx',
    author_email='justzx2011@gmail.com',
    url='http://github.com/justzx2011/openyoudao/',
    py_modules=['fusionyoudao', 'gl', 'openyoudao', 'webshot'],
    data_files = [("/usr/share/applications/", ['desktop/openyoudao.desktop']),
		("/usr/share/doc/openyoudao",['LICENSE','README.md']),
		("/usr/share/icons/hicolor/scalable/apps",['openyoudao.svg']),
		("/usr/share/openyoudao",glob.glob("cache/*.html")),
		("/usr/lib/openyoudao",glob.glob("*.py")),
		("/usr/share/openyoudao/construction/youdao",['cache/construction/youdao/head.html']),
		("/usr/share/openyoudao/css",glob.glob("cache/css/*.css")),
		("/usr/share/openyoudao/images/icon/",['cache/images/icon/icon.jpg']),
		("/usr/share/openyoudao/images/donate/",['cache/images/icon/alipay.png']),
		("/usr/share/openyoudao/js", glob.glob("cache/js/*.js")),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
	'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
	'Topic :: Utilities'
    ],
    scripts = ['scripts/openyoudao'],
)
