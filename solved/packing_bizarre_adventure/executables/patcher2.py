#! /usr/bin/python3

decode_elf_position = 0x01011b9
decode_elf_start = 0x100000


def patch(unpacked):
    with open("./copia", "r+b") as f:
        original = f.read()
    patch_len = len(unpacked)
    offset = decode_elf_position-decode_elf_start
    print("offset:", hex(offset))
    print("offset + patch_len:", hex(offset+patch_len))
    patched = original[0:offset]+unpacked+original[offset+patch_len:]
    with open("./patched_v3", "wb") as patched_file:
        patched_file.write(patched)


with open("./unpacked2", "rb") as f_unpacked:
    unpacked = f_unpacked.read()
    patch(unpacked)
