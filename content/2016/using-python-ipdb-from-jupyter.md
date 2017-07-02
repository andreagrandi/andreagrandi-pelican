Title: Using Python ipdb from Jupyter
Date: 2016-05-10 10:13
Author: Andrea Grandi
Category: Development
Tags: debugging, ipdb, Python
Slug: using-python-ipdb-from-jupyter
Status: published

If we try to use the usual ipdb commands from a Jupyter (IPython
notebook)

    :::python
    import ipdb; ipdb.set_trace()

we will get a similar error:

    :::python
    --------------------------------------------------------------------------
    MultipleInstanceError                     Traceback (most recent call last)
    <ipython-input-1-f2b356251c56> in <module>()
        1 a=4
    ----> 2 import ipdb; ipdb.set_trace()
        3 b=5
        4 print a
        5 print b

    /home/nnn/anaconda/lib/python2.7/site-packages/ipdb/__init__.py in <module>()
        14 # You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
        15 
    ---> 16 from ipdb.__main__ import set_trace, post_mortem, pm, run, runcall, runeval, launch_ipdb_on_exception
        17 
        18 pm                       # please pyflakes

    /home/nnn/anaconda/lib/python2.7/site-packages/ipdb/__main__.py in <module>()
        71         # the instance method will create a new one without loading the config.
        72         # i.e: if we are in an embed instance we do not want to load the config.
    ---> 73         ipapp = TerminalIPythonApp.instance()
        74         shell = get_ipython()
        75         def_colors = shell.colors

    /home/nnn/anaconda/lib/python2.7/site-packages/traitlets/config/configurable.pyc in instance(cls, *args, **kwargs)
        413             raise MultipleInstanceError(
        414                 'Multiple incompatible subclass instances of '
    --> 415                 '%s are being created.' % cls.__name__
        416             )
        417 

    MultipleInstanceError: Multiple incompatible subclass instances of TerminalIPythonApp are being created.

The solution is to use Tracer instead:

    :::python
    from IPython.core.debugger import Tracer
    Tracer()()

**Source:** <http://stackoverflow.com/questions/35613249/using-ipdb-to-debug-python-code-in-one-cell-jupyter-or-ipython>
