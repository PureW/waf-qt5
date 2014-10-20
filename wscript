#! /usr/bin/env python
# encoding: utf-8
# Thomas Nagy, 2005, 2011 (ita)

"""
Including the moc files *is* the best practice (KDE), not doing it is easy,
but makes the compilations about 30-40% slower on average.

If you still want the slow version (we warned you!), see the example located
in the folder playground/slow_qt/
"""

VERSION = '0.0.1'
APPNAME = 'priceplotter'

top = '.'
out = 'build'


def options(opt):
    opt.load('compiler_cxx qt5')


def configure(conf):
    conf.load('compiler_cxx qt5')
    conf.env.append_value('CXXFLAGS', ['-g', '-std=c++11', '-fPIC'])


def build(bld):

    bld(
        features='qt5 cxx cxxprogram',
        use='QTCORE5 QTGUI5 BASE5',
        #shlib='Qt5Gui Qt5Core',
        source='main.cpp notepad.cpp notepad.ui',
        target=APPNAME,
        includes='. /usr/include/qt5',
        #defines='WAF=1 QT_CORE5_LIB=1 QT_GUI_LIB=1',  # test
        #lang=bld.path.ant_glob('linguist/*.ts'),
        #langname='somefile',  # include the .qm files from somefile.qrc
    )

# use the following if you want to add the include paths automatically
if 1:
     from waflib.TaskGen import feature, before_method, after_method
     @feature('cxx')
     @after_method('process_source')
     @before_method('apply_incpaths')
     def add_includes_paths(self):
        incs = set(self.to_list(getattr(self, 'includes', '')))
        for x in self.compiled_tasks:
            incs.add(x.inputs[0].parent.path_from(self.path))
        self.includes = list(incs)

@feature('qt')
@before_method('process_source')
def add_qt_module_defines(task_gen):
    use = set(task_gen.to_list(getattr(task_gen, 'use', '')))

    for module_name in use:
        if module_name.startswith('QT') and not '_' in module_name:
            task_gen.env.append_unique('DEFINES',
                                       'QT_' + module_name[2:] + '_LIB')
