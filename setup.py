import os
import glob
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='openyoudao',
    version=1.0,
    description='A Youdao client for Linux',
    long_description=readme,
    author='justzx',
    author_email='justzx2011@gmail.com',
    url='http://github.com/justzx2011/openyoudao/',
    py_modules=['fusionyoudao', 'gl', 'openyoudao', 'webshot'],
    data_files = [("/usr/share/applications/", ['desktop/openyoudao.desktop']),
		("/usr/share/doc/packages/openyoudao",['LICENSE','README.md']),
		("/usr/share/icons/hicolor/scalable/apps",['openyoudao.svg']),
		("/usr/share/openyoudao",glob.glob("cache/*.html")),
		("/usr/share/openyoudao",['cache/openyoudao.log']),
		("/usr/share/openyoudao/construction/youdao",['cache/construction/youdao/head.html']),
		("/usr/share/openyoudao/css",glob.glob("cache/css/*.css")),
		("/usr/share/openyoudao/images/icon/",['cache/images/icon/icon.jpg']),
		("/usr/share/openyoudao/js", glob.glob("cache/js/*.js")),
		("/usr/share/openyoudao/static/css",glob.glob("cache/static/css/*.css")),
		("/usr/share/openyoudao/static/css",['cache/static/css/css.tar.gz']),
		("/usr/share/openyoudao/static/css/highlight",glob.glob("cache/static/css/highlight/*.css")),
		("/usr/share/openyoudao/static/css/highlight",glob.glob("cache/static/css/highlight/*.png")),
		("/usr/share/openyoudao/static/css/highlight",glob.glob("cache/static/css/highlight/*.jpg")),
		("/usr/share/openyoudao/static/fonts",glob.glob("cache/static/fonts/*.svg")),
		("/usr/share/openyoudao/static/fonts",glob.glob("cache/static/fonts/*.eot")),
		("/usr/share/openyoudao/static/fonts",glob.glob("cache/static/fonts/*.*f")),
		("/usr/share/openyoudao/static/fonts",glob.glob("cache/static/fonts/*.json")),
("/usr/share/openyoudao/static/fonts/lato",glob.glob("cache/static/fonts/lato/*.svg")),
                ("/usr/share/openyoudao/static/fonts/lato",glob.glob("cache/static/fonts/lato/*.eot")),
                ("/usr/share/openyoudao/static/fonts/lato",glob.glob("cache/static/fonts/lato/*.*f")),
		("/usr/share/openyoudao/static/img",glob.glob("cache/static/img/*.png")),
		("/usr/share/openyoudao/static/img",glob.glob("cache/static/img/*.jpg")),
		("/usr/share/openyoudao/static/img",glob.glob("cache/static/img/*.gif")),
		("/usr/share/openyoudao/static/img/images",glob.glob("cache/static/img/images/*.png")),
		("/usr/share/openyoudao/static/img/images",glob.glob("cache/static/img/images/*.gif")),
		("/usr/share/openyoudao/static/js",glob.glob("cache/static/js/*.js")),
		("/usr/share/openyoudao/static/js",glob.glob("cache/static/js/*.html")),
                ("/usr/share/openyoudao/static/js/adapters",glob.glob("cache/static/js/adapters/*.js")),
                ("/usr/share/openyoudao/static/js/jsdifflib",glob.glob("cache/static/js/jsdifflib/*.js")),
                ("/usr/share/openyoudao/static/js/modules",glob.glob("cache/static/js/modules/*.js")),
                ("/usr/share/openyoudao/static/js/themes",glob.glob("cache/static/js/themes/*.js"))
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
