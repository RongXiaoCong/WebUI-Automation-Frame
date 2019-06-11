import os
import unittest


class CaseStrategy:
	def __init__(self):
		self.suite_path = 'test_suites'
		self.case_path = 'test_baidu'
		self.case_pattern = 'test_0*.py'

	def _collect_cases(self, cases, top_dir=None):
		suites = unittest.defaultTestLoader.discover(self.case_path,
													 pattern=self.case_pattern, top_level_dir=top_dir)
		for suite in suites:
			for case in suite:
				cases.addTest(case)

	def collect_cases(self, suite=True):
		"""collect cases

		collect cases from the giving path by case_path via the giving pattern by case_pattern

		return: all cases that collected by the giving path and pattern, it is a unittest.TestSuite()

		"""
		cases = unittest.TestSuite()

		if suite:
			test_suites = []
			project_dir = os.path.dirname(os.path.dirname(__file__))
			for file in os.listdir(project_dir):
				if self.suite_path in file:
					suites_dir = os.path.join(project_dir,file)
					if os.path.isdir(suites_dir):
						test_suites.append(suites_dir)
			for test_suite in test_suites:
				self._collect_cases(cases, top_dir=test_suite)
		else:
			self._collect_cases(cases, top_dir=None)

		return cases
