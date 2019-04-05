import os
import sys
import unittest
from models import db, Shark, Investment
class DBTestCases(unittest.TestCase):
	#these tests have not been run yet and may not work
	
	#tests if inserting a shark in to the db works
	def test_source_insert_1(self):
		s = Shark(name='Bob Ross',picture='https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Bob_at_Easel.jpg/220px-Bob_at_Easel.jpg')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Shark).filter_by(name='Bob Ross').one()
		self.assertEqual(str(r.name),'Bob Ross')
		db.session.query(Shark).filter_by(name='Bob Ross').delete()
		db.session.commit()
	def test_source_insert_2(self):
		s = Shark(name='Barack Obama',picture='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/480px-President_Barack_Obama.jpg')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Shark).filter_by(name='Barack Obama').one()
		self.assertEqual(str(r.name),'Barack Obama')
		db.session.query(Shark).filter_by(name='Barack Obama').delete()
		db.session.commit()
	def test_source_insert_3(self):
		s = Shark(name='Obi Wan Kenobi',picture='https://vignette.wikia.nocookie.net/swfans/images/d/d1/ObiWanKenobi.jpg/revision/latest?cb=20130604153336')
		db.session.add(s)
		db.session.commit()
		r = db.session.query(Shark).filter_by(name='Obi Wan Kenobi').one()
		self.assertEqual(str(r.name),'Obi Wan Kenobi')
		db.session.query(Shark).filter_by(name='Obi Wan Kenobi').delete()
		db.session.commit()
		
	#tests if inserting an investment into the db works
	def test_source_insert_4(self):
		i = Investment(name='Coca Cola',id=5,episode=10,founders = ['Asa Griggs Candler'])
		db.session.add(i)
		db.session.commit()
		r = db.session.query(Investment).filter_by(id=5).one()
		self.assertEqual(str(r.id),str(5))
		db.session.query(Investment).filter_by(id=5).delete()
		db.session.commit()
	def test_source_insert_5(self):
		i = Investment(name='NASA',id=2,episode=15,founders = ['Dwight D. Eisenhower'])
		db.session.add(i)
		db.session.commit()
		r = db.session.query(Investment).filter_by(id=2).one()
		self.assertEqual(str(r.id),str(2))
		db.session.query(Investment).filter_by(id=2).delete()
		db.session.commit()
	def test_source_insert_4(self):
		i = Investment(name='JUUL',id=10,episode=1,founders = ['Jamaes Monsees','Adam Bowen'])
		db.session.add(i)
		db.session.commit()
		r = db.session.query(Investment).filter_by(id=10).one()
		self.assertEqual(str(r.id),str(10))
		db.session.query(Investment).filter_by(id=10).delete()
		db.session.commit()
		
	
	


if __name__ == '__main__':
    unittest.main()
