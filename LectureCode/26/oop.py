#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:08:01 2025

@author: smcrony
"""


class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    def __repr__(self):
        return f"{self.title} {self.author} {self.ISBN}"



class Member(Person):
    def __init__(self, name, person_id, membership_no):
        super().__init__(name, person_id)
        self.membership_no = membership_no
        self.borrow_books = []

    def borrow_book(self, ISBN):
        lib = self.library
        book = lib.borrow_book(ISBN, self)
        self.borrow_books.append(book)

    def __repr__(self):
        return f"{self.borrow_books} {self.name}"

class Librarian(Person):
    def __init__(self, name, person_id, employee_id):
        super().__init__(name, person_id)
        self.employee_id = employee_id

    def __repr__(self):
        return f"{self.name}, {self.person_id}, {self.employee_id}, {self.library}"

    def add_book_to_library(self, book):
        lib = self.library
        lib.add_book(book)


class Library:
    def __init__(self, name):
        self.name = name
        self.librarians = []
        self.members = []
        self.books = []
        self.borrow_books = []

    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        librarian.library = self

    def add_member(self, member: Member):
        self.members.append(member)
        member.library = self  # now, member object has a new attribute, library

    def add_book(self, book: Book):
        self.books.append(book)
        book.library = self
    def borrower(self, ISBN) -> Member:
        for book, borrower in self.borrow_books:
            if book.ISBN == ISBN:
                return borrower

    def __repr__(self):
        return f"{self.name}, {len(self.members)}, {len(self.librarians)}, {len(self.books)}"

    def borrow_book(self, ISBN: str, borrower : Member) -> Book:
        for b in self.books:
            if b.ISBN == ISBN:
                # check if this book is already reserved
                for b2, _ in self.borrow_books:   #borrower의 경우 사용되지 않으므로 _ 처리.
                    if b2.ISBN == ISBN:
                        raise ValueError("This book is already borrowed")

                self.borrow_books.append((b, borrower))
                return b
        raise KeyError("Book is not found.")


if __name__ == "__main__":

    print(Library.__init__)
    # 도서관 인스턴스 생성
    lib = Library("Central Library")

    # 사서 등록
    librarian_john = Librarian("John Doe", person_id=1001, employee_id="L001")
    lib.add_librarian(librarian_john)
    librarian_ally = Librarian("Ally Kin", person_id=1531, employee_id="L002")
    print(librarian_john)
    lib.add_librarian(librarian_ally)
    print(librarian_john)

    # 회원 등록
    member_alice = Member("Alice", person_id=2001, membership_no="M123")
    member_bob = Member("Bob", person_id=2002, membership_no="M124")

    lib.add_member(member_alice)
    lib.add_member(member_bob)
    print(librarian_john)
    # 새 책 생성 & 등록
    book_1 = Book("Python OOP", "Guido", "ISBN-12345")
    book_2 = Book("Learn C++", "Bjarne", "ISBN-67890")

    # # 사서가 도서 추가
    librarian_john.add_book_to_library(book_1)
    librarian_john.add_book_to_library(book_2)

    print(lib)  # Library 상태 확인

    # # 회원 Alice가 책 대출
    member_alice.borrow_book("ISBN-12345")
    member_alice.borrow_book("ISBN-67890")  # 두 권 대출 시도
    print('hi')
    # print(member_alice)  # 대출 목록 확인
    print(lib.borrower("ISBN-12345"))  # borrowed_by가 Alice인지 확인

    # # Bob이 이미 대출된 책을 빌리려고 시도
    # member_bob.borrow_book(lib, "ISBN-12345")  # 실패할 것
    # print(member_bob)

    # # Alice 반납
    # member_alice.return_book(lib, "ISBN-12345")
    # member_alice.return_book(lib, "ISBN-11111")  # 없는 책 반납 시도

    # # Bob이 다시 대출 시도
    # member_bob.borrow_book(lib, "ISBN-12345")

    # print(member_bob)
    # print(lib)