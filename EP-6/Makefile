PHONY: run

run: main
	python main.py

main: main.c 
	gcc -fPIC -shared -o libfunction.so main.c
	sudo cp libfuncao.so /usr/local/lib
	sudo cp main.conf /etc/ld.so.conf.d/
	sudo ldconfig
	python main.py