from classes.head import Head
from classes.tape import Tape
from classes.instructions import Instructions
import argparse


def display_machine_state(tape, header):
    position = header.position()
    tape_view = "".join(tape.content())
    # Adding a marker for the head position
    tape_view = tape_view[:position] + "^" + tape_view[position:]
    print(tape_view)
    print(f"Current state: {header.state()}\n")


def main():
    move_cap = 20

    parser = argparse.ArgumentParser()
    parser.add_argument("tapecontent", help="initial tape content")
    parser.add_argument("instructionfile", help="file that contains instructions")
    args = parser.parse_args()

    tape = Tape(list(args.tapecontent))
    header = Head(0, "init")
    instructions = Instructions(open(args.instructionfile, "r"))

    move_count = 0
    while True:
        display_machine_state(tape, header)
        try:
            instr_input = (tape.input(header.position()), header.state())
        except IndexError:
            print(
                f"Error: program ended. Header: {(header.position(), header.state())}"
            )
            break
        try:
            new_value, new_state, direction = instructions.command(instr_input)
        except KeyError:
            print(f"Command not found for {instr_input} input")
            break

        if move_count > move_cap:
            print(f"Move count exceeded {move_cap}, program closed")
            break

        tape.change_value(header.position(), new_value)
        header.change_state(new_state)
        header.move(direction)
        move_count += 1


if __name__ == "__main__":
    main()
