MAIN_FILE=gtourdia_python_module_00_tester.py
TEST_FILES=test_ex0.py test_ex1.py test_ex2.py\
		test_ex3.py test_ex4.py test_ex5_iter.py\
		test_ex5_recurs.py test_ex6.py test_ex7_area.py\
		test_ex7_grams.py test_ex7_packets.py\
		test_ex7_unknown.py
MOVED_FILES=../test_ex0.py ../test_ex1.py ../test_ex2.py\
		../test_ex3.py ../test_ex4.py ../test_ex5_iter.py\
		../test_ex5_recurs.py ../test_ex6.py ../test_ex7_area.py\
		../test_ex7_grams.py ../test_ex7_packets.py\
		../test_ex7_unknown.py

all: start

start: move
	python3 ../gtourdia_python_module_00_tester.python3

ex0: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex0

ex1: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex1

ex2: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex2

ex3: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex3

ex4: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex4

ex5: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex5

ex6: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex6

ex7: move
	python3 ../gtourdia_python_module_00_tester.python3 --ex7

move:
	mv $(TEST_FILES) $(MAIN_FILE) ../

clean:
	mv $(MOVED_FILES) ../$(MAIN_FILE) ./

fclean: clean

.PHONY: