import unittest
from flask_script import Manager
from project import app, db
import coverage

COV = coverage.coverage(
branch=True,
include='project/*',
omit=['project/tests/*']
)
COV.start()

manager = Manager(app)

@manager.command
def cov():
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
if __name__ == '__main__':
    manager.run()
