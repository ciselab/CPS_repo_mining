#!/usr/bin/env python
"""
Classes for mocking git commits.
"""


class MockableCommit:
    def __init__(self, hash, msg, modifications, committer_date, files):
        self.hash = hash
        self.msg = msg
        self.modifications = modifications
        self.committer_date = committer_date
        self.files = files


class MockableModifications:
    def __init__(self, filename):
        self.filename = filename
        self.length = len(filename)
        self.backup_filename = self.filename

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.backup_filename):
            self.filename = self.backup_filename[self.n]
            self.n += 1
            return self
        else:
            raise StopIteration
