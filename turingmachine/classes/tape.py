class Tape:
    """Tape which the turing machine goes through. The tape contains a list of values that can be replaced by the turing machine.
    """
    def __init__(self, input):
        """Creates instance of Tape class.

        Args:
            input (list): List of values to be put as the tape content.
        """
        self._content = ['_'] + input + ['_']

    def content(self):
        """Get tape content.

        Returns:
            list: List of values in the tape.
        """
        return self._content

    def change_value(self, position, value):
        """Changes a value inside the tape at a certain position into a new value.

        Args:
            position (int): Position at which a value will be changed.
            value (str): New value to be put into the tape.
        """
        if position >= len(self._content):
            self._content += ['_'] * (position - len(self._content) + 1)
        self._content[position] = value

    def input(self, position):
        """Checks if position is outside the tape and returns value inside the tape at a certain position.

        Args:
            position (int): Position of the header.

        Raises:
            IndexError: Exception if position is less than 0.

        Returns:
            str: Value inside the tape at the header position.
        """
        if position < 0:
            raise IndexError
        if position >= len(self._content):
            self._content.extend(["_"] * (position - len(self._content) + 1))
        return self.content()[position]
