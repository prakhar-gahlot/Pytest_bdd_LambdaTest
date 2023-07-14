import platform
import threading

from paver.easy import *
from paver.setuputils import setup

setup(
    name = "pytest-bdd-browserstack",
    version = "1.0.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Pytest BDD Integration with BrowserStack"),
    license = "MIT",
    keywords = "example pytest bdd browserstack",
    url = "https://github.com/ashwingonsalves/pytest-bdd-browserstack",
    packages=['Tests']
)

def run_pytest_bdd(config, feature, output, task_id=0 ):
    if platform.system() == 'Windows':
        sh('SET CONFIG_FILE=config/%s.json & SET TASK_ID=%s & pytest %s --cucumberjson %s -v -s' % (config, task_id, feature, output))
    else:
        sh('export CONFIG_FILE=config/%s.json && export TASK_ID=%s && pytest %s --cucumberjson %s -v -s' % (config, task_id, feature, output))

@task
@consume_nargs(3)
def run(args):
    """Run remote, local and parallel test using different config."""
    if args[0] in ('remote', 'local'):
        run_pytest_bdd(args[0], args[1], args[2])
    else:
        jobs = []
        for i in range(3):
            p = threading.Thread(target=run_pytest_bdd,args=(args[0], args[1], args[2],i))
            jobs.append(p)
            p.start()

        for th in jobs:
            th.join()

@task
def test():
    """Run all tests"""
    sh("paver run remote")
    sh("paver run local")
    sh("paver run parallel")