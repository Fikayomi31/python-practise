#!/usr/bin/python3
import sys
stderr_fileno = sys.stderr
data = "and that piece of art is useful - Dora Korpar, 2015-10-19"
stderr_fileno.write(data)
sys.exit(0)