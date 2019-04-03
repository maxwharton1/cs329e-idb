import os
import sys
import unittest
from models import db, Shark, Investment
class DBTestCases(unittest.TestCase):
	#def test_source_insert_1(self):
	#	s = Book(id='20', title = 'C++')
	#	db.session.add(s)
	#	db.session.commit()
	#	r = db.session.query(Shark).filter_by(id = '20').one()
	#	self.assertEqual(str(r.id), '20')
	#	db.session.query(Shark).filter_by(id = '20').delete()
	#	db.session.commit()
	
	def test_source_insert_1(self):
		s = Shark(name='Bob Ross',picture='https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Bob_at_Easel.jpg/220px-Bob_at_Easel.jpg')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Shark).filter_by(name='Bob Ross').one()
		self.assertEqual(str(r.name),'Bob Ross')
		db.session.query(Shark).filter_by(name='Bob Ross').delete()
		db.session.commit()


if __name__ == '__main__':
    unittest.main()
