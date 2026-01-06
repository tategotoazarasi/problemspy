import sys


class addtwonumbers:
	@staticmethod
	def main(stream_in=sys.stdin, stream_out=sys.stdout):
		input_data = stream_in.read().split()
		iterator = iter(input_data)
		a = int(next(iterator))
		b = int(next(iterator))
		stream_out.write(str(a + b))
