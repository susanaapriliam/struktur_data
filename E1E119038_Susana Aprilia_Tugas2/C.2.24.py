#C-2.24
"""
Suppose you are on the design team for a new e-book reader. What are the
primary classes and methods that the Python software for your reader will
need? You should include an inheritance diagram for this code, but you
do not need to write any actual code. Your software architecture should
at least include ways for customers to buy new books, view their list of
purchased books, and read their purchased books.
Book class --> get_price(), get_id(), get_author(), num_of_pages(), get_summary()
	Book(title, author, price, unique_id, summary, pages)
Nested in Book will be a Page class --> read_text(), highlight_chars(seq_of_chars), 
get_page_number(), next_page(), go_to_page(n)
	Page(page_number, text)
Customer Class --> get_account_info(), see_shelf(), read_book(title), buy_book(title)
	Customer(account_info, shelf)
"""
