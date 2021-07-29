"""
read large file in chunks

read()
read(size)
readline()
readline(size)
readlines()

chunks
"""

def read_in_chunks(file_path, chunk_size=1024*1024):
    """
    Lazy function (generator) to read a file piece by piece
    1 MB per chunk
    :param file_path:
    :param chunk_size:
    :return:
    """

    file_objet = open(file_path)

    while True:
        chunk_data = file_objet.read(chunk_size)
        if not chunk_data:
            break

        yield chunk_data

    pass


# main
filepath = 'file_large_1.txt'

# read_in_chunks(filepath, 2*1024*1024)
content = read_in_chunks(filepath)
print(list(content))

