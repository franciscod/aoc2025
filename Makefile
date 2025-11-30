TODAY = $(shell date +"%d")
YEAR = 2025

today: $(TODAY)/Makefile

times:
	echo "# Advent of Code $(YEAR)" > README.md
	echo '```' >> README.md
	curl "https://adventofcode.com/$(YEAR)/leaderboard/self" \
	  -H 'cookie: session=$(shell cat cookie)' | htmlq -t pre >> README.md
	echo '```' >> README.md

$(TODAY)/Makefile:
	mkdir -p $(TODAY)
	cd $(TODAY); ln -s ../Makefile_day Makefile
	cd $(TODAY); ln -s ../lib.py
	cp skel.py $(TODAY)/solve.py
