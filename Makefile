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
PYTHON=python3

all: start

start: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py

ex0: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex0

ex1: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex1

ex2: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex2

ex3: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex3

ex4: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex4

ex5: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex5

ex6: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex6

ex7: move
	$(PYTHON) ../gtourdia_python_module_00_tester.py --ex7

move:
	mv $(TEST_FILES) $(MAIN_FILE) ../

clean:
	mv $(MOVED_FILES) ../$(MAIN_FILE) ./

fclean: clean

.PHONY: