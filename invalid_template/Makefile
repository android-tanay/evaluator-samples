prepare:

compile:

test:	tests/autograde.py submission/template.py tests/prepend.py tests/append.py
	cat tests/prepend.py submission/template.py tests/append.py tests/autograde.py > answer.py
	PYTHONPATH="$(shell pwd)/submission":"$(shell pwd)/tests" python3 answer.py

clean:
	-rm answer.py
	-rm report.xml
