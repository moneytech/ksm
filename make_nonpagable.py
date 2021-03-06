#!/usr/bin/env python
# Mark executable sections as non-pagable, this is necessary because VMX root mode runs
# with interrupts off, so all pages must be physically contiguous.
# This file is only for the MinGW build!
import sys
import pefile

pe = pefile.PE(sys.argv[1])
for section in pe.sections:
    if (section.Characteristics & 0x20) != 0:
        section.Characteristics |= 0x08000000

pe.write(sys.argv[1])

